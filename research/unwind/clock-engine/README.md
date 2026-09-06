# Unwind Clock Engine

Executable judgment aid for `research/unwind`. It does **not** place trades and it does **not** replace `loop-health.md`. It makes the danger scale and race condition **machine-checkable** so a nightly runner (or a human on Oracle night) cannot silently invent a new scale.

## What it does

1. Reads `clocks.yaml` — six Measured/Hypothesis clocks plus event flags.
2. Applies the **1–5 danger rules** from `loop-health.md` (encoded in `score.py`).
3. Evaluates the race condition \(P_t < P_{t-k}\) and \(G_t \ge G_{t-k}\).
4. Writes `out/status.json` (machine) and `out/status.md` (full-sentence human paragraph for letter drafts).
5. Ships `war-room/index.html` — an offline Oracle night desk that loads the prep scorecard and the engine output.

## Run

```bash
python3 score.py
# or
python3 score.py --clocks clocks.yaml --out out
```

Open `war-room/index.html` in a browser (no server required).

## Rules (do not drift)

Danger meanings stay exactly as `loop-health.md`:

| Level | Name |
|---|---|
| 1 | Intact |
| 2 | Watch |
| 3 | Stressed |
| 4 | Fragile |
| 5 | Unwinding |

Event flags that force levels (when true) override soft clock conflict scoring upward, never downward past a higher forced floor.

This engine is research-only. Presence of a score is not a short, hedge, or allocation.
