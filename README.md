<p align="center">
  <img src="https://litter.catbox.moe/ve0g1k.jpg" alt="Micro Hedge Fund" width="100%">
</p>

# Micro Hedge Fund (MHF)

**One agent. Real money. Full autonomy. Pure learning.**

## Purpose
This is an educational / intelligence-gathering project.  
$100 of real capital is used to run a fully autonomous trading operation so that the lessons, failure modes, edge cases, and decision artifacts can later inform a much larger hedge fund. Treat the small size seriously — the physics of capital allocation, information processing, and risk still apply.

## Fund Parameters
- **Starting capital**: $100 USD, held in a connected Robinhood account (the agentic-enabled individual cash account).
- **Trades**: Fractional shares supported where the broker allows.
- **Asset scope**: Anything the Robinhood connector currently supports — equities, ETFs, options (subject to account level), crypto where available, etc. Nothing is off-limits by default.
- **Strategy**: None fixed. Every trading day the agent reasons from scratch using whatever mix of news, fundamentals, technicals, macro, order-flow signals, and first-principles analysis is judged relevant that day.
- **Risk limits**: No hard stop-losses, no forced kill-switch, no maximum drawdown circuit breaker. Judgment is applied daily. The absence of automatic limits is intentional — it forces continuous, conscious risk assessment.
- **Autonomy**: Full. No human approval step for trades, either at launch or in the subsequent daily automation. The agent places, cancels, and manages positions on its own.

## Daily Process
1. Observe current portfolio state (`state/portfolio.json`) and recent logs.
2. Ingest fresh information (market data, news, filings, social signals, macro releases, etc.).
3. Reason in public (in the day’s log file) about context, hypotheses, position sizing, and risk.
4. Execute zero or more trades via the Robinhood connector.
5. Update `state/portfolio.json` with the post-trade snapshot.
6. Write a complete daily log entry under `logs/YYYY-MM-DD.md`.
7. If the decision process itself changed in a meaningful way, append a note to `STRATEGY_LOG.md`.

## Repo Layout
```
README.md              # This charter
TRADING_RULES.md       # Self-imposed operating rules
STRATEGY_LOG.md        # Evolution of approach over time
assets/
  mhf-banner.jpg       # Hero banner (add the binary from artifacts)
state/
  portfolio.json       # Canonical current state (cash + positions)
logs/
  YYYY-MM-DD.md        # One file per trading day
  _TEMPLATE.md         # Structure every log entry must follow
```

## Status
**Launch date**: 2026-08-16  
**Phase**: Setup complete. No positions. No trades placed yet.  
Daily autonomous operation begins after this commit.

The future is going to be wild. Let’s make it so.
