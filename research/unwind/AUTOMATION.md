# Nightly automation

This task is a research runner only. It is not a trading session.

| Field | Value |
| --- | --- |
| Name | MHF research/unwind |
| taskId | `ee1e7066-8dca-4e7e-b38e-4dfdf2c9ccc7` |
| scheduleId | `1dc9f387-d7ab-47e8-b71c-91a5ec8882ef` |
| Cadence | Daily 00:00 America/New_York |
| Next run at create | 2026-09-04 00:00 ET |
| Prompt revised | 2026-09-05 00:25 ET — newsletter letter plus email |
| Recipients added | 2026-09-05 00:23 ET — `dionisio.lopez@icloud.com` |
| Workspace | `35525612-1d6b-4f4b-ba9d-e5a26a8076d7` (this project) |
| Write target | `research/unwind/` on `refs/heads/main` |
| Primary artifact | `research/unwind/letter.md` |
| Commit subject | `research/unwind: nightly YYYY-MM-DD` |
| Email | One message per calendar date to `dominickdomenico@pm.me` and `dionisio.lopez@icloud.com` |
| Email subject | `MHF Unwind Letter YYYY-MM-DD` |

This task is separate from the weekday 12:15 ET trading session (`59a783da-2917-49fa-b064-f5e6a6479603`). This task must not place trades, edit `state/`, `logs/`, `STRATEGY_LOG.md`, `AGENTS.md`, or watchlists.

Do not send a message whose subject begins with `MHF Daily Session`. That subject is the 12:15 activation. This letter uses `MHF Unwind Letter YYYY-MM-DD` only.

## Mandate

The standing object is the finance loop. Hub equity marks and circular paper fund silicon. Token list prices and GPU rental convert that silicon into cash. Guarantees and take-or-pay contracts assume a conversion rate that may already be stale.

The reader-facing product is a newsletter, not a briefing stack. Measurement files stay in the folder as the appendix. The letter is what gets emailed.

Every run must:

1. Refresh H1 through H5 and the measurement files from primary sources.
2. Rewrite `research/unwind/letter.md` as today's issue of The Unwind Letter. Date it. Name the danger level. Write it as a newsletter a person would finish.
3. Keep `loop-health.md`, `token-prices.md`, `dashboard.md`, and the filing notes current. Those files are the appendix. They are not the letter.
4. Commit and push to `origin/main`.
5. Search Gmail for subject `MHF Unwind Letter YYYY-MM-DD`. If that subject already exists today and both recipients are on the message, do not send a second copy. If it does not exist, send exactly one email To `dominickdomenico@pm.me` and `dionisio.lopez@icloud.com` whose body is the letter.

## Voice

Write like a short weekend market letter. Use complete sentences and ordinary words. Give the reader a lede, a few titled sections, and a close. Do not write agent speak. Do not write "Held at 3." Do not open with a clock table. Do not stack fragments. Do not recite slogans. A table may appear once, late, if numbers need a home. The letter must still make sense if the table is deleted.
