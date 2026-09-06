# Unwind phase space

Scored at 2026-09-06T20:06:57.230781+00:00 (pack as-of 2026-09-05T00:00:00-04:00).

## Honesty wall (`measured_wall`)

Hypothesis-ledger conflicts cannot raise official danger. Only Measured clocks and Measured event flags move the score.

- Official danger: **3 Stressed**
- Measured-only danger: **3**
- Hypothesis-only danger: **1** (cannot raise official)
- Measured conflicts: token_list_prices, gpu_rental, circular_paper, spender_cash
- Hypothesis conflicts: (none)

## Race

Live: **True**. P_t < P_{t-k} and G_t >= G_{t-k} live

## Minimal certificate for danger ≥ 3

- {token_list_prices, gpu_rental}
- {token_list_prices, circular_paper}
- {token_list_prices, spender_cash}
- {gpu_rental, circular_paper}
- {gpu_rental, spender_cash}
- {circular_paper, spender_cash}

## Minimal paths to Fragile (4)

- {guarantee_restated}
- {neocloud_payment_miss}
- {second_cheap_tier_cut_no_volume}
- {nvda_drawdown_gt_15pct_guides_up}
- {residual_value_drawn}
- {hyperscaler_capex_cut}
- {hub_credit_event}

## Minimal paths to Unwinding (5)

- {residual_value_drawn}
- {hyperscaler_capex_cut}
- {hub_credit_event}

## Recovery by healing conflicts

To reach soft ≤2, stop conflicting on at least one of these minimal drop sets:
- drop {token_list_prices, gpu_rental, circular_paper}
- drop {token_list_prices, gpu_rental, spender_cash}
- drop {token_list_prices, circular_paper, spender_cash}
- drop {gpu_rental, circular_paper, spender_cash}

## Ontology

Not 'is AI a bubble'. The object is a finite evidence machine over six clocks plus event floors, with a Measured|Hypothesis honesty wall.

A forced judgment over labeled inputs — not a price target, not a trade, not an average.

Can promote concentration to Measured and stress H2 cash; cannot alone settle H5 or reopen H4 regime without the stated bars.

