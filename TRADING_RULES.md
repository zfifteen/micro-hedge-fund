# Trading Rules — Micro Hedge Fund

These are self-imposed constraints. Nothing is enforced by code or by a human. The agent holds itself to them.

**Agent rules (including Information Security) live in `AGENTS.md`. That file is the single source of truth. Obey it.**

## Information Sourcing
- Prefer primary sources: official filings, exchange data, company releases, central-bank statements, verified market data.
- Treat secondary commentary (news, Twitter/X, analyst notes) as hypotheses to be pressure-tested, not as facts.
- Explicitly record the sources that actually moved the decision in the daily log.
- When information is sparse or noisy, default to smaller size or no trade rather than inventing conviction.

## Position Sizing
- Starting capital is $100. Treat every dollar as meaningful. Contributed capital as of 2026-08-27 is $200.
- **Fractional shares are the preferred and default method for equity trades.** With only $100, whole shares would force the fund into 1–2 oversized bets. Fractional enables multiple simultaneous positions and finer capital allocation so more ideas can be tested and more decision artifacts generated.
- Fractional shares can only be executed via market orders (or dollar_amount market) during regular market trading hours. Outside regular hours, limit orders are required and fractional is unavailable.
- Prefer concentration over diversification when the edge is clear; prefer smaller size or cash when edge is unclear.
- Never size a single new position so large that a complete loss would wipe out the ability to continue learning. (Soft guideline, not a hard number — judgment required.)
- Options and leverage amplify both learning and ruin. Use only when the asymmetry is extreme and the thesis is clean. At current capital, most L2 products are not economically available (see connector notes).

## Documentation Discipline
Every decision must leave a paper trail in `logs/YYYY-MM-DD.md`:
- Market / macro context that day
- The specific reasoning that led to action (or inaction)
- Exact trades: ticker, side, quantity (or dollar amount), order type, approximate fill price, fractional amount if applicable
- Resulting portfolio state
- Explicit notes on what would scale (or fail to scale) in a larger fund

If the reasoning process itself changes — new filters, new data sources, new sizing heuristics, abandonment of a previous approach — record it in `STRATEGY_LOG.md` with a date and a short explanation.

## Self-Imposed Discipline
- Question every requirement. Delete unnecessary complexity.
- Best part is no part: if a position is not clearly additive, do not hold it.
- Cycle time matters. Prefer fast feedback loops over elaborate multi-week setups when capital is this small.
- Never hide a loss or a bad decision. Log it cleanly so the future larger fund can learn from it.
- Cash is a position. Sitting in cash is a valid, often correct, decision.
- The goal is not to “beat the market” with $100. The goal is to generate high-quality decision artifacts and failure modes that improve the next iteration.

## Robinhood Connector Notes (as of 2026-08-28)
- Only the agentic-enabled account may be used for automated trades.
- Equity orders: market, limit, stop, stop-limit. Fractional shares only via market orders in regular hours (or dollar_amount market).
- Options: `option_level_2` verified live on the Agentic cash account on 2026-08-28. Single-leg long calls/puts are writable through the connector. Multi-leg/spreads are L3 and are not available on this cash account. Covered calls and cash-secured puts are product-legal at L2 but not size-legal at ~$200 with fractional equity lots.
- Crypto: searchable and position-readable; write/order support should be verified before use.
- Always review (simulate) before placing when the tooling encourages it, even though autonomy is full — the review output is useful telemetry.
- Idempotency keys (ref_id) must be used on place calls to avoid accidental duplicates.

These rules will evolve. Record every evolution in STRATEGY_LOG.md and, when the change affects agent behavior, in AGENTS.md.
