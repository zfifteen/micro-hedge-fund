<p align="center">
  <img src="assets/mhf-banner.jpg" alt="Micro Hedge Fund" width="100%">
</p>

# Micro Hedge Fund (MHF)

**One agent. Real money. Full autonomy. Pure learning.**

## Purpose
This is a real-money experiment in autonomous retail trading.

One agent trades a Robinhood cash account with full autonomy, starting at $100 of learning capital. The environment is retail: fractional equities, regular-hours constraints, and brokerage API friction. The name is historical. This is a retail book, not a seed for an institutional hedge fund.

The $100 was starting capital. Treat it seriously — allocation, information, and risk still apply at this size. This same account continues as more capital is added. Decision artifacts and failure modes are a byproduct of trying to grow this book.

## Fund Parameters
- **Starting capital**: $100 USD (2026-08-16), held in a connected Robinhood account (the agentic-enabled individual cash account).
- **Contributed capital**: $200 USD as of 2026-08-27 ($100 launch + $100 operator contribution). Contributions are not trading P&L.
- **Trades**: Fractional shares supported where the broker allows.
- **Asset scope**: Anything the Robinhood connector currently supports — equities, ETFs, options (subject to account level), crypto where available, etc. Nothing is off-limits by default.
- **Strategy**: None fixed. Every trading day the agent reasons from scratch using whatever mix of news, fundamentals, technicals, macro, order-flow signals, and first-principles analysis is judged relevant that day.
- **Risk limits**: No hard stop-losses, no forced kill-switch, no maximum drawdown circuit breaker. Judgment is applied daily. The absence of automatic limits is intentional — it forces continuous, conscious risk assessment.
- **Autonomy**: Full. No human approval step for trades, either at launch or in the subsequent daily automation. The agent places, cancels, and manages positions on its own.

## Daily Process
1. Observe current portfolio state (`state/portfolio.json`) and recent logs.
2. Ingest fresh information (market data, Robinhood lists, news, filings, social signals, macro releases, etc.).
3. Reason in public (in the day’s log file) about context, hypotheses, position sizing, and risk.
4. Execute zero or more trades via the Robinhood connector.
5. Update `state/portfolio.json` with the post-trade snapshot.
6. Write a complete daily log entry under `logs/YYYY-MM-DD.md`.
7. If the decision process itself changed in a meaningful way, append a note to `STRATEGY_LOG.md`.

## Repo Layout
```
README.md              # Public description
AGENTS.md              # Standing rules for any agent running the book
TRADING_RULES.md       # Self-imposed operating rules
STRATEGY_LOG.md        # Evolution of approach over time
assets/
  mhf-banner.jpg       # Hero banner
state/
  portfolio.json       # Canonical current state (cash + positions)
logs/
  YYYY-MM-DD.md        # One file per trading day
  _TEMPLATE.md         # Structure every log entry must follow
```

## Status
**Launch date**: 2026-08-16  
**Phase**: Live retail book. Daily autonomous sessions since 2026-08-17.  
**Capital**: $200 contributed as of 2026-08-27.
