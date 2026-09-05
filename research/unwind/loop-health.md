# Loop health — daily

Opened 2026-09-04. This file is a process note, not a book. Presence of a score here is not a short.

Write every daily report in easy-to-understand, grammatically correct, complete sentences. Tables may hold numbers. The judgment, the reason the danger level moved or held, the snapshot log, and the open questions must be full sentences.

The finance loop is a race condition because several clocks run at once. Token prices can fall the day after a residual-value guarantee is filed. A capex guide can rise in the same week that a cheap-tier API rate is cut by 80 percent. Scoring one clock in isolation hides the loop.

## Danger scale

| Level | Name | Meaning |
|---|---|---|
| 1 | Intact | Token and rental conversion still funds the last generation. New paper rolls without extra collateral. Hub free cash flow is not the earnings-call topic. |
| 2 | Watch | One clock is moving against the others. No bind has printed yet. |
| 3 | Stressed | Two or more clocks conflict. Cash conversion is weaker than the paper that funded the last build. Hub equity marks still hold. |
| 4 | Fragile | A rim credit event, a guarantee-language change, or a token or rental gap makes residual value a live question. Hub marks still mostly hold. |
| 5 | Unwinding | A hub missed payment, a drawn guarantee, a hyperscaler capex cut, or a token and rental collapse arrives with a hub equity gap. |

This scale is a judgment over Measured inputs. It is not a model output. Label the inputs. Do not average them into false precision.

## Daily report — 2026-09-04 America/New_York

The danger level is **3, Stressed**. The level is held at 3 rather than raised to 4 because no guarantee has been drawn, no rim payment has been missed, no hyperscaler has cut capex, and NVIDIA still trades about 3 percent below its May all-time high. The level is not cut to 2 because spender free cash flow is already the earnings-call topic, cheap-tier token prices were cut hard in July, and neocloud rental on last-generation silicon sits far below hyperscaler list rates.

The installed base is being asked to service 2026-sized paper at 2026-cheap token and rental rates, while the next generation's guarantees are already on the books.

Frontier token prices still show a split. Cheap-tier list rates are in a price war after OpenAI cut GPT-5.6 Luna by 80 percent on 30 July 2026, to $0.20 input and $1.20 output per million tokens, and cut Terra by 20 percent. Reasoning and pro-tier cards have not followed that cut. A secondary index from BenchLM puts the September 2026 frontier median near $6 blended per million tokens, which is useful as slope and is not a filing.

GPU rental shows the same split by venue. On 4 September 2026 the CCIR guaranteed on-demand series printed H100 at $10.53 an hour at hyperscalers, $3.71 at neoclouds, and $3.03 on the marketplace. H200 printed $10.30 / $4.40 / $4.00. B200 printed $14.24 / $6.69 / $5.99. Interruptible H100 at neoclouds printed $2.15. A neocloud that financed GPUs on a 2025 residual deck and now clears H100 near $3 to $4 an hour is the first place the race can show.

Circular paper has not shrunk. NVIDIA filed a $105 billion SB Energy residual-value cap on 17 August 2026. Amazon has closed $50 billion of OpenAI equity and expanded the AWS-OpenAI commercial commitment by $100 billion over eight years. No guarantee was drawn on this pass. New paper at 2026 size raises the stock of promises that later token prices have to service.

Spender cash remains tight. Amazon's trailing-twelve-month free cash flow is −$7.6 billion. Alphabet printed −$5.9 billion of free cash flow in the second quarter. Meta printed $0.78 billion. Oracle printed −$23.7 billion for fiscal 2026. July capex guides moved up at three of the four hyperscalers and down at none. Capex is being paid from the balance sheet and the bond market, not from incremental AI cash.

Rim credit is stressed and still current. CoreWeave carried about $35 billion of debt at 30 June 2026. The July delayed-draw term loan cleared wider than marketed, and five-year CDS round-tripped. Financing still closed. A token or rental miss would show here as a payment miss first. That miss has not printed.

The hub equity mark is intact. NVIDIA closed at $228.45 on 3 September 2026, about 3.4 percent below the 14 May high of $236.54. The Magnificent Seven still reconstruct to about 33.6 percent of SPY. That mark is the collateral for the next circular round, and it is why the danger level is 3 rather than 5.

Volume growth can still rescue price times quantity. Volume is not scored in this file until a primary utilization print exists.

### Clock table

| Clock | State | Tag | Transmission into the loop |
|---|---|---|---|
| Token list prices | Frontier median blended about $6 per million tokens on the BenchLM September 2026 index of 16 versus a March 2023 base of 100. OpenAI cut Luna 80 percent and Terra 20 percent on 30 July 2026. GPT-6 Astra is listed at $10 / $50. The cheap tier is in a price war. The reasoning and pro tier is not. | Measured for provider cards. Hypothesis for the BenchLM index. | A lower dollar-per-token rate is the cash the GPU prints. Volume must rise faster than price falls, or take-or-pay and residual-value math gaps. |
| GPU rental | On 4 September 2026 CCIR guaranteed on-demand rates, United States and Europe, printed H100 at $10.53 hyperscaler / $3.71 neocloud / $3.03 marketplace. H200 printed $10.30 / $4.40 / $4.00. B200 printed $14.24 / $6.69 / $5.99. Interruptible H100 at neoclouds printed $2.15. | Measured as a published series. | Rental is the intermediate price. The race shows first at a neocloud that financed at 2025 residual assumptions and now clears H100 near $3 to $4 an hour. |
| Circular paper | NVIDIA filed a $105 billion SB Energy residual-value cap on 17 August 2026. Amazon closed $50 billion of OpenAI equity and added $100 billion of AWS-OpenAI commercial commitment over eight years. No guarantee was drawn on this pass. | Measured | New paper is still being written at 2026 size. That is the opposite of a shrink. It raises the stock of promises that later token prices have to service. |
| Spender cash | Amazon trailing-twelve-month free cash flow is −$7.6 billion. Alphabet second-quarter free cash flow is −$5.9 billion. Meta second-quarter free cash flow is $0.78 billion. Oracle fiscal 2026 free cash flow is −$23.7 billion. July guides: three up, zero down. | Measured | Capex is being paid from the balance sheet and the bond market, not from incremental AI cash. The loop is running on issuance and marks. |
| Rim credit | CoreWeave debt was about $35 billion at 30 June 2026. The July delayed-draw term loan cleared wider. Five-year CDS round-tripped. Financing still closed. | Measured for debt stock. Hypothesis-adjacent for CDS. | The rim is where a token or rental miss becomes a payment miss first. That miss has not printed. |
| Hub equity mark | NVIDIA closed at $228.45 on 3 September 2026 against a May high of $236.54, about 3.4 percent below. The Magnificent Seven reconstruct to about 33.6 percent of SPY. | Measured | The mark is the collateral for the next circular round. It is intact. That is why danger is 3, not 5. |

### Race, stated as a condition

Let $P_t$ be the blended token or GPU-hour conversion rate the installed generation actually prints. Let $G_{t-k}$ be the residual-value or take-or-pay stock written $k$ periods earlier at assumed rate $P_{t-k}$. The loop is in a race when

$$
P_t < P_{t-k} \quad \text{and} \quad G_t \ge G_{t-k}
$$

at the same time. That pair is live today. Cheap-tier $P$ is down hard since midsummer. $G$ stepped up in mid-August with the NVIDIA $105 billion cap.

### What would move the level

The level would move to 4 if a named guarantee is restated, if a neocloud misses a payment or fails a takeout, if a second large cheap-tier cut arrives without an offsetting volume print, or if NVIDIA falls more than 15 percent from the May high while capex guides stay up.

The level would move to 5 if a residual-value guarantee is drawn, if a hyperscaler cuts capex, or if a hub credit event prints.

The level would move to 2 if mid-tier token prices are stable or rising for two consecutive quarters and neocloud H100 and H200 guaranteed rental holds while circular paper stops growing.

The level would move to 1 if spender free cash flow recovers at the current capex level.

### Open questions

Does cheap-tier token deflation raise demand by giving buyers more tokens per dollar, or does it give away margin at labs that still have take-or-pay contracts with clouds?

Does hyperscaler list rental above $10 an hour for an H100 still clear, or is that a sticker that circular offtake ignores?

What utilization would make a $105 billion residual-value cap a cash question before fiscal 2029?

Can NVIDIA's mark stay within a few percent of the all-time high if $P_t$ keeps falling on everything that is not a reasoning or pro SKU?

Which clock prints first if the race is lost: rim CDS, a capex-guide cut, or the hub mark?

## Nightly snapshot log

- **2026-09-04 America/New_York (structure and first score).** The danger level is 3, Stressed. OpenAI cut Luna by 80 percent on 30 July 2026, and neocloud H100 guaranteed rental printed about $3.71 an hour on 4 September, while NVIDIA added a $105 billion residual-value cap in mid-August and the hub mark stayed intact. Hypothesis H4 remains a fail as regime change. Hypothesis H5 is open and live on the cheap tier. The next forced refresh is Oracle's fiscal 2027 first quarter, expected around 10 September 2026, or any provider rate-card move.
