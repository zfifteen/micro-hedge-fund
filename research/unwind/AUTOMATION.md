# Nightly automation

Research runner only. Not a trading session.

| Field | Value |
| --- | --- |
| Name | MHF research/unwind |
| taskId | `ee1e7066-8dca-4e7e-b38e-4dfdf2c9ccc7` |
| scheduleId | `1dc9f387-d7ab-47e8-b71c-91a5ec8882ef` |
| Cadence | Daily 00:00 America/New_York |
| Next run at create | 2026-09-04 00:00 ET |
| Prompt revised | 2026-09-04 23:40 ET — open-ended loop-health + token-price mandate |
| Workspace | `35525612-1d6b-4f4b-ba9d-e5a26a8076d7` (this project) |
| Write target | `research/unwind/` on `refs/heads/main` |
| Commit subject | `research/unwind: nightly YYYY-MM-DD` |

Separated from the weekday 12:15 ET trading session (`59a783da-2917-49fa-b064-f5e6a6479603`). This task must not place trades, edit `state/`, `logs/`, `STRATEGY_LOG.md`, `AGENTS.md`, or watchlists, or send the 12:15 Gmail activation.

## Mandate (revised 2026-09-04)

The folder is open-ended. The runner does not close the watch when H4 fails. The standing object is the precarious, race-condition finance loop: hub equity marks and circular paper fund silicon; token list prices and GPU rental convert that silicon into cash; guarantees and take-or-pay assume a conversion rate that may already be stale.

Every run must:

1. Refresh H1–H5 from primaries.
2. Refresh token-price and GPU-rental prints into `token-prices.md`.
3. Write a dated loop-health analysis in `loop-health.md` with an explicit danger level (1 Intact / 2 Watch / 3 Stressed / 4 Fragile / 5 Unwinding) and the one-sentence reason the level moved or held.
4. If the tape is unchanged, still write a dated snapshot line to `dashboard.md` *and* a dated line in `loop-health.md` so main receives one commit that calendar date.

Do not skip the git write because "nothing happened."
