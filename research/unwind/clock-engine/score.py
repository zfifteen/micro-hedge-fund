#!/usr/bin/env python3
"""Unwind Clock Engine — score danger + race from clocks.yaml."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

LEVELS = {
    1: "Intact",
    2: "Watch",
    3: "Stressed",
    4: "Fragile",
    5: "Unwinding",
}

MEANINGS = {
    1: "Token and rental conversion still funds the last generation. New paper rolls without extra collateral. Hub free cash flow is not the earnings-call topic.",
    2: "One clock is moving against the others. No bind has printed yet.",
    3: "Two or more clocks conflict. Cash conversion is weaker than the paper that funded the last build. Hub equity marks still hold.",
    4: "A rim credit event, a guarantee-language change, or a token or rental gap makes residual value a live question. Hub marks still mostly hold.",
    5: "A hub missed payment, a drawn guarantee, a hyperscaler capex cut, or a token and rental collapse arrives with a hub equity gap.",
}


def load_clocks(path: Path) -> dict:
    text = path.read_text()
    if yaml is not None:
        return yaml.safe_load(text)
    # Minimal fallback parser for our simple YAML subset
    raise SystemExit("PyYAML required: pip install pyyaml")


def conflict_count(clocks: dict) -> tuple[int, int, list[str]]:
    conflict, watch, names = 0, 0, []
    for name, body in (clocks or {}).items():
        state = (body or {}).get("state", "")
        if state == "conflict":
            conflict += 1
            names.append(name)
        elif state == "watch":
            watch += 1
    return conflict, watch, names


def soft_danger(conflict: int, watch: int, hub_intact: bool) -> int:
    if conflict >= 2 and hub_intact:
        return 3
    if conflict >= 1 or watch >= 1:
        return 2
    return 1


def event_floor(events: dict) -> int | None:
    e = events or {}
    if e.get("residual_value_drawn") or e.get("hyperscaler_capex_cut") or e.get("hub_credit_event"):
        return 5
    if (
        e.get("guarantee_restated")
        or e.get("neocloud_payment_miss")
        or e.get("second_cheap_tier_cut_no_volume")
        or e.get("nvda_drawdown_gt_15pct_guides_up")
    ):
        return 4
    return None


def event_ceiling_down(events: dict) -> int | None:
    """Optional downward moves only when recovery flags are explicit."""
    e = events or {}
    if e.get("spender_fcf_recovered_at_current_capex"):
        return 1
    if (
        e.get("mid_tier_tokens_stable_two_quarters")
        and e.get("neocloud_rental_holds")
        and e.get("circular_paper_stopped_growing")
    ):
        return 2
    return None


def score(data: dict) -> dict:
    clocks = data.get("clocks") or {}
    events = data.get("events") or {}
    race = data.get("race") or {}
    hub = clocks.get("hub_equity_mark") or {}
    hub_intact = hub.get("state") in ("intact", "watch", None) and hub.get("state") != "conflict"

    conflict, watch, conflict_names = conflict_count(clocks)
    soft = soft_danger(conflict, watch, hub_intact=True if hub.get("state") != "gap" else False)

    # If hub mark is in a gap (collapse), soft path can already be stressed+
    if hub.get("state") == "gap":
        soft = max(soft, 5)

    floor = event_floor(events)
    danger = soft if floor is None else max(soft, floor)
    ceiling = event_ceiling_down(events)
    # Recovery ceilings only apply when no upward floor is active
    if floor is None and ceiling is not None:
        danger = min(danger, ceiling)

    race_live = bool(race.get("p_down_since_prior")) and bool(race.get("g_up_or_flat"))

    return {
        "as_of": data.get("as_of"),
        "scored_at": datetime.now(timezone.utc).isoformat(),
        "danger": danger,
        "danger_name": LEVELS[danger],
        "danger_meaning": MEANINGS[danger],
        "soft_danger": soft,
        "event_floor": floor,
        "conflict_count": conflict,
        "watch_count": watch,
        "conflict_clocks": conflict_names,
        "hub_state": hub.get("state"),
        "race_live": race_live,
        "race_note": race.get("note"),
        "hypotheses": data.get("hypotheses"),
        "next_forced_print": data.get("next_forced_print"),
        "pack_danger_baseline": data.get("pack_danger_baseline"),
        "baseline_match": data.get("pack_danger_baseline") == danger,
    }


def human_paragraph(result: dict, data: dict) -> str:
    d = result["danger"]
    name = result["danger_name"]
    clocks = data.get("clocks") or {}
    bits = []
    for key in result["conflict_clocks"]:
        summary = (clocks.get(key) or {}).get("summary")
        if summary:
            bits.append(f"{key.replace('_', ' ')}: {summary}")
    conflict_sentence = (
        " The conflicting clocks include " + "; ".join(bits) + "."
        if bits
        else ""
    )
    race_sentence = (
        " The race condition is live: cheap-tier conversion is down while residual-value or take-or-pay stock is up or flat."
        if result["race_live"]
        else " The race condition flags are not both live in clocks.yaml."
    )
    nxt = data.get("next_forced_print") or {}
    next_sentence = ""
    if nxt.get("name"):
        next_sentence = f" The next forced print named in the engine input is {nxt.get('name')} ({nxt.get('when')})."

    return (
        f"The danger level is {d}, {name}. "
        f"{MEANINGS[d]}"
        f"{conflict_sentence}"
        f"{race_sentence}"
        f"{next_sentence} "
        f"This score is a judgment over labeled inputs in clocks.yaml. It is not a model output and it is not a trade."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--clocks", type=Path, default=Path(__file__).with_name("clocks.yaml"))
    ap.add_argument("--out", type=Path, default=Path(__file__).with_name("out"))
    args = ap.parse_args()

    data = load_clocks(args.clocks)
    result = score(data)
    paragraph = human_paragraph(result, data)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "status.json").write_text(json.dumps(result, indent=2) + "\n")
    (args.out / "status.md").write_text(
        f"# Clock engine status\n\n{paragraph}\n\n```json\n{json.dumps(result, indent=2)}\n```\n"
    )
    print(json.dumps(result, indent=2))
    print("\n" + paragraph)


if __name__ == "__main__":
    main()
