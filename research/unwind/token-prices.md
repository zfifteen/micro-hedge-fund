# WS-T — Token prices and GPU rental

As-of: 2026-09-04. Process note, not a book.

These are the output prices of the finance loop. Filings tell you what was promised. This file tells you what the installed silicon can charge today. Announced is not funded is not a token. A rate card is not utilization.

Rule: quote provider cards and dated rental series. Aggregator indexes are Hypothesis unless the constituent cards are named.

## Why this file exists

H2 watches whether capex earns cash. H3 watches how capex is financed. This file watches the price that turns a GPU-hour into a dollar after the GPU is plugged in. If that price falls while circular paper stays large, H3's architecture is still standing and the loop is still in trouble.

Two prices, not one:

- API token list prices ($/1M input and output). What labs and clouds bill the end user.
- GPU rental ($/GPU-hr). What neoclouds and hyperscalers bill each other and third parties.

Do not blend them into one "AI price."

## API tokens — flagship cards

Units: USD per 1 million tokens. Standard processing, not batch, not priority, unless noted.

| Model | Provider | Input | Output | As-of | Tag | Source |
|---|---|---:|---:|---|---|---|
| GPT-6 Astra | OpenAI | 10.00 | 50.00 | 2026-09-03/04 lists | Hypothesis-adjacent (aggregator; confirm on openai.com/api when the Astra card is first-party) | aipricing.guru 2026-09-04 |
| GPT-5.6 Sol | OpenAI | 5.00 (promo card on openai.com/api also shows 4.00 / 20.00 through at least 2026-11-21) | 30.00 (or 20.00 promo) | 2026-09-04 | Measured on the official API page; promo vs list is split | openai.com/api |
| GPT-5.6 Terra | OpenAI | 2.00 | 12.00 | 2026-07-30 cut, still listed | Measured | OpenAI 2026-07-30 announcement; openai.com/api |
| GPT-5.6 Luna | OpenAI | 0.20 | 1.20 | 2026-07-30 cut (−80% from 1.00 / 6.00) | Measured | OpenAI 2026-07-30; openai.com/api |
| Claude Opus 5 | Anthropic | 5.00 | 25.00 | 2026-09-04 lists | Hypothesis-adjacent until the Anthropic card is pulled first-party this pass | aipricing.guru / BenchLM |
| Claude Sonnet 5 | Anthropic | 2.00 | 10.00 | BenchLM notes a mid-tier blended increase | Hypothesis-adjacent | BenchLM Sep 2026 |
| Gemini 3.1 Pro | Google | 2.00 | 12.00 | 2026-09-04 lists | Hypothesis-adjacent | aggregator cards |
| Grok 4.6 | xAI | 2.00 | 6.00 | 2026-09-04 lists | Hypothesis-adjacent | aggregator cards |

OpenAI 2026-07-30 is the last *first-party* cheap-tier shock in this file: Luna −80%, Terra −20%. Company language: serving-cost improvements passed through. That is a Measured price cut. It is not a Measured statement that volume rose enough to hold dollar revenue.

## Index (secondary)

BenchLM Token Price Index, released 2026-09-03 for September 2026:

- Frontier sub-index **16** vs March 2023 = 100 (−84% from the base). MoM 0%.
- Median blended frontier **$6.00 / 1M** across 21 constituents (3:1 input:output blend).
- Mid-tier index 50, median blended $3.00.
- Budget index 116.3, median blended $0.58.

Tag: **Hypothesis** (constructed index). Use it as a slope, not as a filing.

Read-through: the long deflation from 2023 is already in the price. The live question for the loop is not "are tokens cheaper than 2023." It is "did July–September 2026 cheap-tier cuts change the conversion rate that 2025–2026 circular paper assumed."

## GPU rental — 2026-09-04

CCIR guaranteed on-demand, US & EU, USD/GPU-hr, as of 2026-09-04 07:30 ET. Secondary series. Tag: **Measured as a published series, not as a company filing.**

| Silicon | Hyperscaler | Neocloud | Marketplace |
|---|---:|---:|---:|
| B300 | — | 7.67 | 7.42 |
| B200 | 14.24 | 6.69 | 5.99 |
| H200 | 10.30 | 4.40 | 4.00 |
| H100 | 10.53 | 3.71 | 3.03 |
| A100 | 4.45 | 2.04 | 1.43 |

Interruptible (same source, not a substitute for guaranteed):

| Silicon | Hyperscaler | Neocloud |
|---|---:|---:|
| H200 | 6.37 | 2.45 |
| H100 | 2.78 | 2.15 |
| A100 | 1.22 | 1.14 |

What this does to the loop:

- Last-gen (H100/H200) already clears on the neocloud at roughly one-third of the hyperscaler sticker.
- A residual-value guarantee written against a 2025–early-2026 rental deck is looking at a different $P$ than the deck.
- Hyperscaler stickers staying high does not rescue a neocloud that financed at the low print. It may even be the circular offtake: the same parties that signed take-or-pay are not the parties posting $3 H100s on the marketplace.

Do not treat marketplace $3.03 H100 as CoreWeave's realized yield. Realized yield needs utilization and mix. That print is not in this file.

## Transmission into H2 / H3 / H5

- H2: cheaper tokens can raise volume and still leave FCF compressed if the capex to serve the volume was already spent. July guides went *up* after the Luna cut. That is consistent with "price war plus more silicon," not with "price war plus less silicon."
- H3: the $105B NVDA residual-value cap (8-K 2026-08-17) sits *after* the 2026-07-30 OpenAI cheap-tier cut. Sequence is price-down, then more guarantee. That is the race condition, not a shrink.
- H5: live on the cheap tier. Not proven as a bind on hub paper. Missing: a filing that restates residual value, or a rim payment that does not clear.

## Refresh rules

- Pull OpenAI / Anthropic / Google / xAI official cards before quoting aggregators.
- Pull CCIR (or a named successor series) for rental. Do not invent a blended "GPU price."
- A rate-card cut is a first-class event for this folder, same rank as a capex guide revision.
- Utilization and tokens-sold remain out of this file until a primary print exists.
