# Nightly automation

Research runner only. Not a trading session.

| Field | Value |
| --- | --- |
| Name | MHF research/unwind |
| taskId | `ee1e7066-8dca-4e7e-b38e-4dfdf2c9ccc7` |
| scheduleId | `1dc9f387-d7ab-47e8-b71c-91a5ec8882ef` |
| Cadence | Daily 00:00 America/New_York |
| Next run at create | 2026-09-04 00:00 ET |
| Workspace | `35525612-1d6b-4f4b-ba9d-e5a26a8076d7` (this project) |
| Write target | `research/unwind/` on `refs/heads/main` |
| Commit subject | `research/unwind: nightly YYYY-MM-DD` |

Separated from the weekday 12:15 ET trading session (`59a783da-2917-49fa-b064-f5e6a6479603`). This task must not place trades, edit `state/`, `logs/`, `STRATEGY_LOG.md`, `AGENTS.md`, or watchlists, or send the 12:15 Gmail activation.

If the tape is unchanged, the run still writes a dated snapshot line to `dashboard.md` so main receives one commit that calendar date.
