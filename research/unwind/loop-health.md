# Loop health — daily

Opened 2026-09-04. Process note, not a book. Presence here is not a short.

The finance loop is a race condition: several clocks run at once. Token prices can gap the day after a residual-value guarantee is filed. A capex guide can be raised the same week a cheap-tier API rate is cut 80%. Scoring one clock in isolation is how the loop hides.

## Danger scale

| Level | Name | Meaning |
|---|---|---|
| 1 | Intact | Token/rental conversion still funds the last generation; paper rolls without extra collateral; hub FCF not the call topic. |
| 2 | Watch | One clock is moving against the others. No bind yet. |
| 3 | Stressed | Two or more clocks conflict. Cash conversion is weaker than the paper that funded the last build. Hub marks still hold. |
| 4 | Fragile | A rim credit event, a guarantee language change, or a token/rental gap that makes residual value a live question. Hub marks still mostly hold. |
| 5 | Unwinding | Hub missed payment, drawn guarantee, hyperscaler capex *cut*, or token/rental collapse with hub equity gap. |

This scale is a judgment over Measured inputs. It is not a model output. Label the inputs. Do not average them into false precision.

## As-of 2026-09-04 America/New_York

**Danger level: 3 — Stressed.**

Held at 3. Not raised to 4: no guarantee drawn, no missed rim payment, no capex cut, NVDA still ~3% off the May ATH. Not cut to 2: spender FCF is already the earnings-call topic, cheap-tier token prices were cut hard in July, and neocloud rental on last-gen silicon sits far below hyperscaler lists.

### One-sentence reason

The installed base is being asked to service 2026-sized paper at 2026-cheap token and rental rates, while the next generation's guarantees are already on the books.

### Clock table

| Clock | State | Tag | Transmission into the loop |
|---|---|---|---|
| Token list prices | Frontier median blended ~$6 / 1M (BenchLM Sep 2026 index = 16 vs Mar 2023 = 100). OpenAI 2026-07-30 cut Luna 80% and Terra 20%. GPT-6 Astra listed $10 / $50. Cheap tier is in a price war; reasoning/pro tier is not. | Measured (provider cards + BenchLM secondary index) | Lower $/token is the cash the GPU prints. Volume must rise faster than price falls or take-or-pay and residual-value math gaps. |
| GPU rental | 2026-09-04 CCIR guaranteed on-demand, US+EU: H100 hyperscaler $10.53 vs neocloud $3.71 vs marketplace $3.03. H200 $10.30 / $4.40 / $4.00. B200 $14.24 / $6.69 / $5.99. Interruptible H100 neocloud $2.15. | Measured (CCIR series, secondary) | Rental is the intermediate price. A neocloud that financed GPUs at 2025 residual assumptions and now clears H100 near $3–4/hr is the first place the race shows. |
| Circular paper | NVDA $105B SB Energy residual-value cap filed 2026-08-17. AMZN OpenAI equity $50B closed; AWS-OpenAI +$100B / 8y. No guarantee drawn this pass. | Measured | New paper is still being written at 2026 size. That is the opposite of a shrink. It raises the stock of promises that later token prices have to service. |
| Spender cash | AMZN TTM FCF −$7.6B. GOOGL Q2 FCF −$5.9B. META Q2 FCF $0.78B. ORCL FY26 FCF −$23.7B. July guides 3 up / 0 down. | Measured | Capex is being paid from the balance sheet and the bond market, not from incremental AI cash. The loop is running on issuance and marks. |
| Rim credit | CRWV ~$35B debt at 6/30. July DDTL cleared wider. 5y CDS round-tripped. Financing still closed. | Measured / Hypothesis-adjacent on CDS | Rim is where a token/rental miss becomes a payment miss first. Not there yet. |
| Hub equity mark | NVDA 2026-09-03 close $228.45 vs May ATH $236.54 (~3.4%). Mag7 ~33.6% of SPY. | Measured | The mark is the collateral for the next circular round. It is intact. That is why danger is 3, not 5. |

### Race, stated as a condition

Let $P_t$ be the blended token (or GPU-hour) conversion rate the installed generation actually prints, and $G_{t-k}$ the residual-value / take-or-pay stock written $k$ periods earlier at assumed rate $P_{t-k}$. The loop is in a race when

$$
P_t < P_{t-k} \quad \text{and} \quad G_t \ge G_{t-k}
$$

at the same time. That pair is live today: cheap-tier $P$ is down hard since midsummer; $G$ stepped *up* in mid-August with the NVDA $105B cap. Volume growth can still rescue $P \times Q$. Volume is not scored in this file until a primary utilization print exists.

### What would move the level

- To 4: a named guarantee restated, a neocloud payment miss or failed takeout, a second large cheap-tier cut without an offsetting volume print, or NVDA down >15% from the May ATH while capex guides stay up.
- To 5: a drawn residual-value guarantee, a hyperscaler capex *cut*, or a hub credit event.
- To 2: two consecutive quarters of stable or rising mid-tier token prices *and* neocloud H100/H200 guaranteed rental holding while circular paper stops growing.
- To 1: spender FCF recovers at the current capex level.

### Open questions (do not retire)

1. Is cheap-tier token deflation a demand gift (more tokens per dollar) or a margin gift given away by labs that still have take-or-pay with clouds?
2. Does hyperscaler list rental ($10+/hr H100) still clear, or is that a sticker the circular offtake ignores?
3. What utilization would make a $105B residual-value cap a cash question before fiscal 2029?
4. Can NVDA's mark stay within a few percent of ATH if $P_t$ keeps falling on everything that is not a reasoning/pro SKU?
5. Which clock prints first if the race is lost: rim CDS, a guide cut, or the hub mark?

## Nightly snapshot log

- **2026-09-04 America/New_York (structure + first score):** Danger **3 Stressed**. Cheap-tier token cut (OpenAI Luna −80% on 2026-07-30) and neocloud H100 guaranteed ~$3.71/hr coexist with a mid-August $105B NVDA residual-value cap and intact hub marks. H4 remains fail as regime change. H5 open and live on the cheap tier. Next forced refresh: ORCL FY27 Q1 (~2026-09-10) or any provider rate-card move.
