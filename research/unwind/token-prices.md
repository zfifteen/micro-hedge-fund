# WS-T — Token prices and GPU rental

As-of: 2026-10-06. Process note, not a book.

These are the output prices of the finance loop. Filings tell you what was promised. This file tells you what the installed silicon can charge today. Announced is not funded is not a token. A rate card is not utilization.

Rule: quote provider cards and dated rental series. Aggregator indexes are Hypothesis unless the constituent cards are named.

## Why this file exists

H2 watches whether capex earns cash. H3 watches how capex is financed. This file watches the price that turns a GPU-hour into a dollar after the GPU is plugged in. If that price falls while circular paper stays large, H3’s architecture is still standing and the loop is still in trouble.

Two prices, not one:

- API token list prices ($/1M input and output). What labs and clouds bill the end user.
- GPU rental ($/GPU-hr). What neoclouds and hyperscalers bill each other and third parties.

Do not blend them into one "AI price."

## API tokens — flagship cards

Units: USD per 1 million tokens. Standard processing, not batch, not priority, unless noted.

| Model | Provider | Input | Output | As-of | Tag | Source |
|---|---|---:|---:|---|---|---|
| GPT-6 Astra | OpenAI | 10.00 | 50.00 | 2026-10-06 official card | Measured | developers.openai.com/api/docs/pricing |
| GPT-6.1 Sol | OpenAI | 2.00 | 10.00 | 2026-10-06 official flagship table | Measured | developers.openai.com/api/docs/pricing |
| GPT-6 Luna | OpenAI | 0.10 | 0.50 | 2026-10-06 official flagship table | Measured | developers.openai.com/api/docs/pricing |
| GPT-5.6 Sol | OpenAI | 4.00 short-context promo (long-context 8.00); company language calls this promotional through at least 2026-11-21 | 20.00 short (30.00 long) | 2026-10-06 | Measured | official pricing page |
| GPT-5.6 Terra | OpenAI | 2.00 | 12.00 | 2026-07-30 cut, last confirmed 2026-10-04 | Measured | OpenAI 2026-07-30 announcement; official pricing page |
| GPT-5.6 Luna | OpenAI | 0.20 | 1.20 | 2026-07-30 cut, last confirmed 2026-10-04 | Measured | OpenAI 2026-07-30; official pricing page |
| GPT-Rosalind research | OpenAI | 5.00 | 25.00 | 2026-10-06 official card; billing began 2026-10-05; approved-program access | Measured | developers.openai.com/api/docs/pricing |
| Claude Opus 5.5 | Anthropic | 4.00 | 20.00 | 2026-10-06 last confirmed official card | Measured | platform.claude.com/docs |
| Claude Opus 5 | Anthropic | 5.00 | 25.00 | 2026-10-06 last confirmed official card | Measured | platform.claude.com/docs |
| Claude Sonnet 5.5 | Anthropic | 2.00 | 10.00 | 2026-10-06 official card; same list as Sonnet 5 | Measured | platform.claude.com/docs |
| Claude Sonnet 5 | Anthropic | 2.00 | 10.00 | 2026-10-06 last confirmed official card | Measured | platform.claude.com/docs |
| Claude Haiku 4.5 | Anthropic | 1.00 | 5.00 | 2026-10-06 last confirmed official card | Measured | platform.claude.com/docs |
| Claude Fable 5.1 | Anthropic | 10.00 | 50.00 | 2026-10-06 last confirmed official card; cache hits $0.25 / 1M | Measured | platform.claude.com/docs |
| Gemini 3.1 Pro | Google | 2.00 (<=200k tokens); 4.00 above 200k | 12.00 (<=200k); 18.00 above 200k | 2026-10-06 official page, last page-update stamp seen 2026-10-01 UTC | Measured | ai.google.dev/gemini-api/docs/pricing |
| Gemini 3.8 Flash | Google | 0.75 intro through 2026-12-31; 1.50 starting 2027-01-01 | 3.75 intro through 2026-12-31; 7.50 starting 2027-01-01 | 2026-10-06 official page, intro rate reconfirmed | Measured | ai.google.dev/gemini-api/docs/pricing |
| Grok 4.7 | xAI | 2.00 | 6.00 | 2026-10-06 official model page; page last updated 2026-09-21; input cell still $2.00 | Measured | docs.x.ai model pricing |

OpenAI 2026-07-30 is still the last first-party cheap-tier shock on the GPT-5.6 rows. The official flagship table on 2026-10-06 still lists a GPT-6 family at Astra $10 / $50, GPT-6.1 Sol $2 / $10, and Luna $0.10 / $0.50 on short context. That is a Measured new-name stack at a lower list than the July GPT-5.6 cheap tier. Sol short-context promo remains labeled through at least 21 November 2026. The same official page says billing for gpt-rosalind-research began on 5 October 2026 at $5.00 / $25.00 and that access is limited to an approved program. That line is Measured as a billing start. It is not a flagship list cut.

Google Gemini 3.8 Flash introductory rate of $0.75 / $3.75 is a dated promo that reverts on 1 January 2027. The official page still shows those lists.

Anthropic official page last confirmed Claude Opus 5.5 at $4.00 / $20.00 while Claude Opus 5 remains $5.00 / $25.00. Claude Sonnet 5.5 lists at the same $2.00 / $10.00 as Sonnet 5.

xAI official page still names Grok 4.7 at $2.00 / $6.00 below 200k prompt tokens. The page stamp last seen was 21 September 2026. The input cell was still $2.00 on this pass.

## Index (secondary)

BenchLM Token Price Index, released 2026-09-03 for September 2026:

- Frontier sub-index **16** vs March 2023 = 100.
- Median blended frontier **$6.00 / 1M**.
- Mid-tier index 50, median blended $3.00.
- Budget index 116.3, median blended $0.58.

Tag: **Hypothesis** (constructed index). Use it as a slope, not as a filing. Do not treat 2023-to-now deflation as a 2026 bind by itself.

## GPU rental — 2026-10-04 series, read 2026-10-06

CCIR guaranteed on-demand, US & EU, USD/GPU-hr, as of 2026-10-04 07:30 ET. Tag: **Measured as a published series, not as a company filing.** Source: ccir.io/rates.

| Silicon | Hyperscaler | Neocloud | Marketplace |
|---|---:|---:|---:|
| B300 | — | 7.67 | 7.89 |
| B200 | 14.24 | 7.09 | 6.79 |
| H200 | 10.30 | 4.14 | 4.42 |
| H100 | 11.25 | 3.18 | 3.07 |
| A100 | 4.45 | 1.65 | 1.49 |

Interruptible (same source, not a substitute for guaranteed):

| Silicon | Hyperscaler | Neocloud |
|---|---:|---:|
| B300 | — | 5.07 |
| B200 | — | 3.67 |
| H200 | 6.68 | 2.60 |
| H100 | 2.79 | 2.00 |
| A100 | 2.51 | 1.14 |

Neocloud H100 guaranteed printed $3.18 on the 4 October series, down sixteen cents from the 3 October cell of $3.34. That is the first break of the $3.34 to $3.39 band that had held from late September through 3 October. Marketplace H100 printed $3.07, unchanged. Hyperscaler H100 printed $11.25, unchanged. B200 neocloud printed $7.09, up three cents from $7.06. H200 marketplace printed $4.42, up from $4.38. B300 neocloud printed $7.67, unchanged from the 3 October cell. A100 neocloud printed $1.65, down from $1.80. Interruptible neocloud H100 printed $2.00, unchanged. Interruptible hyperscaler A100 printed $2.51, down from $2.55. The neocloud H100 move is a real slip inside the cheap band, not a regime change in rental, and not a missed payment.

## Transmission into H2 / H3 / H5

- H2: cheaper tokens can raise volume and still leave FCF compressed if the capex to serve the volume was already spent.
- H3: the $105B NVDA residual-value cap sits after the 2026-07-30 OpenAI cheap-tier cut. CoreWeave priced $3.7 billion of 2.875% converts due 2033 on 18 September. A 1 October Reuters report on pipeline guarantees is Hypothesis and is not a draw on that cap.
- H5: live on the cheap tier. Not proven as a bind on hub paper. Missing: a filing that restates residual value, or a rim payment that does not clear.

## Refresh rules

- Pull OpenAI / Anthropic / Google / xAI official cards before quoting aggregators.
- Pull CCIR (or a named successor series) for rental. Do not invent a blended GPU price.
- A rate-card cut is a first-class event for this folder, same rank as a capex guide revision.
- Utilization and tokens-sold remain out of this file until a primary print exists.
