# Operator instruction

Status: ACTIVE
Issued: 2026-09-16 ~06:18 America/New_York
Target session: next weekday 12:15 America/New_York fund run

## Order

Cash out the Agentic cash account (last4 7524).

Sell every equity, option, and crypto position. Do not open new positions in the same session. End the session in cash only.

This is an operator order. It overrides independent thesis for this session. Do not hold through the 16 Sep FOMC 2:00 PM ET decision. Do not keep a residual sleeve in any name.

## Why it is queued for 12:15

Issued premarket. Fractional equity sells are market / dollar_amount during regular hours only. Do not queue a regular-hours market sell at the 09:30 open. Execute during the scheduled session while cash equities are open.

## What you must read before any order

1. AGENTS.md
2. This file
3. state/portfolio.json
4. logs/2026-09-15.md and STRATEGY_LOG.md
5. Live Robinhood on the Agentic account only: get_accounts, get_portfolio, get_equity_positions, get_option_positions (nonzero), get_crypto_positions, get_equity_orders for open states

Reconcile live state against portfolio.json. Trade the live lots, not the file, if they differ.

## Live snapshot at issue (premarket 2026-09-16)

Account value ~$191.58. Cash $15.03. Equity ~$176.55. Options $0. Crypto $0. Buying power $15.03.

Sellable lots, all available:

| Symbol | Quantity | Avg cost | 15 Sep regular close |
|--------|----------|----------|----------------------|
| MU | 0.092126 | 976.92 | 927.60 |
| NVDA | 0.132240 | 226.86 | 212.17 |
| QQQ | 0.027306 | 732.44 | 704.54 |
| CEG | 0.107417 | 279.29 | 259.89 |
| GLD | 0.037549 | 399.48 | 394.15 |

Premarket prints at issue were higher than those closes. Use live regular-hours quotes at 12:15. Do not invent fills.

Contributed capital remains $200. Trading P&L is account value minus $200 after the sells.

## Execution

For each open equity lot:

- side sell
- type market
- market_hours regular_hours
- quantity = shares_available_for_sells from live get_equity_positions
- review_equity_order first
- place_equity_order with a fresh UUID ref_id; never reuse a ref_id

If an options or crypto lot exists at 12:15, close it the same session with the matching review then place path.

If a name is halted or a sell rejects, keep selling the rest, log the blocker, and do not treat a partial book as a completed cash-out.

Do not buy anything after the sells, including GLD, QQQ, or cash-like ETFs.

## After fills

1. Re-read live positions and portfolio. Confirm quantity is zero on every name and crypto is empty.
2. Write state/portfolio.json to cash-only with live cash and total value.
3. Write logs/2026-09-16.md from logs/_TEMPLATE.md. Record that the action was an operator cash-out, not a discretionary hold.
4. Add a STRATEGY_LOG line that the order executed (or that it partially failed).
5. Change this file Status to EXECUTED and add fill notes. Leave the file in place so later sessions can see the order.
6. Remove the one-run cash-out block from the Micro Hedge Fund automation prompt after the book is flat so later sessions are not stuck in a permanent liquidation order.
7. Push main. Send the Daily Session email as usual.

If this file already says EXECUTED and live positions are already flat, do not sell again. Reason that session from a cash book.
