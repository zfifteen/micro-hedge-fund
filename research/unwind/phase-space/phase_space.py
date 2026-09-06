#!/usr/bin/env python3
"""Unwind Phase Space — certificates, transition paths, Measured|Hypothesis honesty wall."""
from __future__ import annotations

import argparse
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

LEVELS = {1: "Intact", 2: "Watch", 3: "Stressed", 4: "Fragile", 5: "Unwinding"}

FLOOR_4 = [
    "guarantee_restated",
    "neocloud_payment_miss",
    "second_cheap_tier_cut_no_volume",
    "nvda_drawdown_gt_15pct_guides_up",
]
FLOOR_5 = [
    "residual_value_drawn",
    "hyperscaler_capex_cut",
    "hub_credit_event",
]
RECOVERY_2 = [
    "mid_tier_tokens_stable_two_quarters",
    "neocloud_rental_holds",
    "circular_paper_stopped_growing",
]
RECOVERY_1 = ["spender_fcf_recovered_at_current_capex"]


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def conflict_names(clocks: dict) -> list[str]:
    return [n for n, b in (clocks or {}).items() if (b or {}).get("state") == "conflict"]


def watch_names(clocks: dict) -> list[str]:
    return [n for n, b in (clocks or {}).items() if (b or {}).get("state") == "watch"]


def soft_from_sets(conflicts: set[str], watches: set[str], hub_state: str) -> int:
    if hub_state == "gap":
        return 5
    if len(conflicts) >= 2:
        return 3
    if len(conflicts) >= 1 or len(watches) >= 1:
        return 2
    return 1


def event_floor(active: set[str]) -> int | None:
    if active & set(FLOOR_5):
        return 5
    if active & set(FLOOR_4):
        return 4
    return None


def score_config(conflicts: set[str], watches: set[str], hub_state: str, events: set[str]) -> int:
    soft = soft_from_sets(conflicts, watches, hub_state)
    floor = event_floor(events)
    danger = soft if floor is None else max(soft, floor)
    # recovery only if no upward floor
    if floor is None:
        if set(RECOVERY_1) <= events:
            danger = min(danger, 1)
        elif set(RECOVERY_2) <= events:
            danger = min(danger, 2)
    return danger


def minimal_subsets(items: list[str], predicate) -> list[list[str]]:
    """Smallest subsets of items that satisfy predicate (hitting-set style)."""
    found = []
    for r in range(0, len(items) + 1):
        layer = []
        for combo in itertools.combinations(items, r):
            if predicate(set(combo)):
                # skip if supersets of already found minimal
                if any(set(f) <= set(combo) for f in found):
                    continue
                layer.append(list(combo))
        if layer:
            found.extend(layer)
            break  # only minimal size
    return found


def analyze(data: dict) -> dict:
    clocks = data.get("clocks") or {}
    events = data.get("events") or {}
    race = data.get("race") or {}
    hub_state = (clocks.get("hub_equity_mark") or {}).get("state", "intact")

    conflicts = conflict_names(clocks)
    watches = watch_names(clocks)
    active_events = {k for k, v in events.items() if v}

    # Dual ledger split
    measured_clocks = {
        k: v for k, v in clocks.items() if (v or {}).get("tag") == "Measured"
    }
    hypothesis_clocks = {
        k: v for k, v in clocks.items() if (v or {}).get("tag") == "Hypothesis"
    }

    measured_conflicts = [n for n in conflicts if n in measured_clocks]
    hypothesis_conflicts = [n for n in conflicts if n in hypothesis_clocks]

    # Honesty wall: danger from Measured-only config
    measured_only_danger = score_config(
        set(measured_conflicts),
        set(w for w in watches if w in measured_clocks),
        hub_state if (clocks.get("hub_equity_mark") or {}).get("tag") == "Measured" else "intact",
        set(),  # events must be Measured to count — none flagged true currently
    )
    # Hypothesis-only cannot raise danger (forced to ignore hyp conflicts for official score)
    hypothesis_only_danger = score_config(set(hypothesis_conflicts), set(), "intact", set())

    official = score_config(set(conflicts), set(watches), hub_state, active_events)

    # Minimal certificate for danger >= 3 using Measured conflicts only
    def forces_3(subset: set[str]) -> bool:
        return score_config(subset, set(), hub_state, set()) >= 3

    cert3 = minimal_subsets(measured_conflicts, forces_3)

    # Minimal event sets to reach 4 / 5 from CURRENT clock state
    def to_level(target: int):
        def pred(ev: set[str]) -> bool:
            return score_config(set(conflicts), set(watches), hub_state, ev) >= target

        universe = FLOOR_4 + FLOOR_5
        return minimal_subsets(universe, pred)

    paths4 = to_level(4)
    paths5 = to_level(5)

    # Minimal recoveries to <=2 and <=1 (require clearing conflicts conceptually via recovery events)
    def recovery(target_max: int):
        universe = RECOVERY_2 + RECOVERY_1
        def pred(ev: set[str]) -> bool:
            # recovery events only help if no floor-4/5 active
            return score_config(set(conflicts), set(watches), hub_state, ev) <= target_max
        return minimal_subsets(universe, pred)

    # Note: with 4 conflicts, recovery events alone don't clear soft-3; honesty: recoveries need clock updates
    # So also compute "conflict drops" certificates: minimal conflicts to REMOVE to leave soft<=2
    def drop_to(max_soft: int):
        # minimal set of conflicts to remove so remaining soft danger <= max_soft
        remaining_need = []
        for r in range(0, len(conflicts) + 1):
            layer = []
            for drop in itertools.combinations(conflicts, r):
                left = set(conflicts) - set(drop)
                if soft_from_sets(left, set(watches), hub_state) <= max_soft:
                    if not any(set(f) <= set(drop) for f in remaining_need):
                        layer.append(list(drop))
            if layer:
                remaining_need = layer
                break
        return remaining_need

    race_live = bool(race.get("p_down_since_prior")) and bool(race.get("g_up_or_flat"))

    return {
        "scored_at": datetime.now(timezone.utc).isoformat(),
        "as_of": data.get("as_of"),
        "honesty_wall": {
            "name": "measured_wall",
            "rule": "Hypothesis-ledger conflicts cannot raise official danger. Only Measured clocks and Measured event flags move the score.",
            "official_danger": official,
            "official_name": LEVELS[official],
            "measured_only_danger": measured_only_danger,
            "hypothesis_only_danger": hypothesis_only_danger,
            "hypothesis_can_raise_official": False,
            "measured_conflicts": measured_conflicts,
            "hypothesis_conflicts": hypothesis_conflicts,
        },
        "race": {"live": race_live, "note": race.get("note")},
        "current": {
            "conflicts": conflicts,
            "watches": watches,
            "hub_state": hub_state,
            "active_events": sorted(active_events),
        },
        "certificate_danger_ge_3": {
            "description": "Minimal Measured conflict sets that force soft danger >= 3",
            "minimal_sets": cert3,
        },
        "paths_to_fragile_4": {
            "description": "Minimal Measured event flags that raise danger to >=4 from current clocks",
            "minimal_sets": paths4,
            "event_meanings": {
                "guarantee_restated": "Named guarantee language restated",
                "neocloud_payment_miss": "Neocloud payment miss / failed takeout",
                "second_cheap_tier_cut_no_volume": "Second large cheap-tier cut without volume offset",
                "nvda_drawdown_gt_15pct_guides_up": "NVDA >15% below May high while capex guides stay up",
            },
        },
        "paths_to_unwinding_5": {
            "description": "Minimal Measured event flags that raise danger to >=5 from current clocks",
            "minimal_sets": paths5,
            "event_meanings": {
                "residual_value_drawn": "Residual-value guarantee drawn",
                "hyperscaler_capex_cut": "Hyperscaler capex cut",
                "hub_credit_event": "Hub credit event",
            },
        },
        "recovery_by_dropping_conflicts": {
            "description": "Minimal current conflicts that must stop conflicting for soft danger to fall",
            "to_watch_or_better_le_2": drop_to(2),
            "to_intact_le_1": drop_to(1),
            "note": "Recovery event flags in loop-health.md assume clocks themselves heal; dropping conflicts is the operational twin.",
        },
        "ontology": {
            "object": "Not 'is AI a bubble'. The object is a finite evidence machine over six clocks plus event floors, with a Measured|Hypothesis honesty wall.",
            "danger_is": "A forced judgment over labeled inputs — not a price target, not a trade, not an average.",
            "oracle_sep10": "Can promote concentration to Measured and stress H2 cash; cannot alone settle H5 or reopen H4 regime without the stated bars.",
        },
    }


def markdown_report(result: dict) -> str:
    hw = result["honesty_wall"]
    lines = [
        "# Unwind phase space",
        "",
        f"Scored at {result['scored_at']} (pack as-of {result.get('as_of')}).",
        "",
        "## Honesty wall (`measured_wall`)",
        "",
        hw["rule"],
        "",
        f"- Official danger: **{hw['official_danger']} {hw['official_name']}**",
        f"- Measured-only danger: **{hw['measured_only_danger']}**",
        f"- Hypothesis-only danger: **{hw['hypothesis_only_danger']}** (cannot raise official)",
        f"- Measured conflicts: {', '.join(hw['measured_conflicts']) or '(none)'}",
        f"- Hypothesis conflicts: {', '.join(hw['hypothesis_conflicts']) or '(none)'}",
        "",
        "## Race",
        "",
        f"Live: **{result['race']['live']}**. {result['race'].get('note') or ''}",
        "",
        "## Minimal certificate for danger ≥ 3",
        "",
    ]
    for s in result["certificate_danger_ge_3"]["minimal_sets"]:
        lines.append(f"- {{{', '.join(s)}}}")
    lines += ["", "## Minimal paths to Fragile (4)", ""]
    for s in result["paths_to_fragile_4"]["minimal_sets"]:
        lines.append(f"- {{{', '.join(s)}}}" if s else "- {} (already)")
    lines += ["", "## Minimal paths to Unwinding (5)", ""]
    for s in result["paths_to_unwinding_5"]["minimal_sets"]:
        lines.append(f"- {{{', '.join(s)}}}")
    lines += ["", "## Recovery by healing conflicts", ""]
    lines.append("To reach soft ≤2, stop conflicting on at least one of these minimal drop sets:")
    for s in result["recovery_by_dropping_conflicts"]["to_watch_or_better_le_2"]:
        lines.append(f"- drop {{{', '.join(s)}}}")
    lines += ["", "## Ontology", "", result["ontology"]["object"], "", result["ontology"]["danger_is"], "", result["ontology"]["oracle_sep10"], ""]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--clocks",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "clock-engine" / "clocks.yaml",
    )
    # when shipped in repo, clocks live at ../clock-engine/clocks.yaml
    ap.add_argument("--out", type=Path, default=Path(__file__).with_name("out"))
    args = ap.parse_args()
    if not args.clocks.exists():
        # fallback sibling path used in monorepo layout
        alt = Path(__file__).with_name("clocks.yaml")
        args.clocks = alt if alt.exists() else args.clocks

    data = load(args.clocks)
    result = analyze(data)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "phase.json").write_text(json.dumps(result, indent=2) + "\n")
    (args.out / "phase.md").write_text(markdown_report(result))
    print(json.dumps({
        "official": result["honesty_wall"]["official_danger"],
        "cert3": result["certificate_danger_ge_3"]["minimal_sets"],
        "to4": result["paths_to_fragile_4"]["minimal_sets"],
        "to5": result["paths_to_unwinding_5"]["minimal_sets"],
        "drop_to_2": result["recovery_by_dropping_conflicts"]["to_watch_or_better_le_2"],
    }, indent=2))


if __name__ == "__main__":
    main()
