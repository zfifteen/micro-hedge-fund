# Dashboard v1 — AI capex unwind watch

Opened 2026-09-03. Snapshot date for market tape on this pass is the **2026-09-04 close**. Filing rows remain the last company prints. The nightly pass on 2026-09-05 confirmed no new hyperscaler 8-K and no new list-price cut. Official provider cards were upgraded from aggregator quotes to first-party pages.

This file is a measurement panel, not a trade. Presence here is not a short, not a hedge, and not an allocation. It does not replace a session log and does not change `state/portfolio.json` or `STRATEGY_LOG.md`.

Rule from the plan: do not write a new unwind narrative until at least two of {2, 3, 5, 6, 10} move together. Token-price and rental prints can move H5 and the danger level without rewriting that narrative rule.

Write dated snapshot lines in easy-to-understand, grammatically correct, complete sentences. Tables may hold numbers.

Every input is tagged **Measured** or **Hypothesis**. Use commentary only when the primary print is named.

---

## Loop health (added 2026-09-04)

The full write-up lives in `loop-health.md`. Token and rental cards live in `token-prices.md`.

| Field | Print | Tag |
|---|---|---|
| Danger level | **3 — Stressed** | Judgment over Measured clocks |
| Why | The danger level is 3 because cheap-tier token prices and neocloud H100 rental have already fallen, while NVIDIA's $105 billion residual-value cap is still on the books and the hub equity mark is intact. Friday's close moved NVIDIA to $230.36, about 2.6 percent below the May high, and that bounce does not change the conversion-rate race. | Mixed |
| H5 | Hypothesis H5 is open. It is live on the cheap tier and is not yet a bind on hub paper. | See hypotheses.md |

The scale is 1 Intact, 2 Watch, 3 Stressed, 4 Fragile, and 5 Unwinding.

---

## Ten-number panel

| # | Metric | Latest print | Tag | Source |
| --- | --- | --- | --- | --- |
| 1 | Combined CY2026 capex guide (AMZN, MSFT, GOOGL, META) | About **$735–750B** after July revisions. Working midpoint **~$747B** if AMZN $220B + GOOGL mid $200B + META mid $137.5B + MSFT calendar ~$190B. Bases are **not identical** (Meta includes finance-lease principal; Microsoft lease mix is shifting). | Measured (company guides) | AMZN Q2 2026 release / call ($220B cash capex). GOOGL Q2 call ($195–205B). META Q2 exhibit 99-1 ($130–145B incl. lease principal). MSFT FY26 Q4 call + prior calendar commentary (~$190B CY; FY27 outlook $175B is a different basis). Platformonomics Q2 2026 scoreboard 2026-07-31 ($735–750B). |
| 2 | Combined capex / OCF | Calendar Q2 cash PPE / OCF: AMZN 53.1 / 45.4 = **1.17**; MSFT 35.8 / 55.4 = **0.65**; GOOGL 44.9 / 39.1 = **1.15**; META PPE 30.1 / 31.9 = **0.94**. Four-name sum **163.9 / 171.8 ≈ 0.95**. ORCL FY26 (year ended 2026-05-31) **55.7 / 32.0 = 1.74**. | Measured | See `capex-cash.md`. AMZN 10-Q MD&A cash capex $53.1B, OCF $45.387B. MSFT FY26 Q4 call. GOOGL Q2 8-K / 10-Q. META exhibit 99-1. ORCL FY26 10-K. |
| 3 | Combined FCF | AMZN TTM to 2026-06-30 **−$7.6B**. MSFT Q4 FY26 **+$19.6B**. GOOGL Q2 **−$5.855B**. META Q2 **+$0.784B**. ORCL FY26 **−$23.686B**. Definitions are company-specific; do not add them into one “true” total. | Measured | AMZN Q2 2026 press release (exhibit 99-1). MSFT FY26 Q4 call. GOOGL Q2 8-K non-GAAP FCF. META exhibit 99-1. ORCL FY26 results / 10-K. |
| 4 | NVDA data-center YoY and gross margin | Q2 FY27 (ended 2026-07-26): Data Center **$89.023B**, **+117% YoY**, **+18% QoQ**. Company gross margin **75.0%**. Total revenue $96.221B. Q3 guide $108.0B ±2%. | Measured | NVDA 10-Q accession `0001045810-26-000075`. |
| 5 | NVDA customer concentration / financed-commitment notes | Q2 FY27: **one direct customer 16%** of revenue. H1 FY27: three directs **16% / 15% / 13%**. Filing also states one AI research-and-deployment company contributed a meaningful amount *indirectly* by buying cloud from NVDA customers. Guarantee / site notes live in `circular-finance.md` (SB Energy residual-value guarantees; AI-cloud land/power/shell). | Measured | Same 10-Q, customer-concentration and commitments discussion. |
| 6 | One neocloud credit or equity stress print | **CoreWeave (CRWV)**. Equity **$89.36** on 2026-09-04, about **−42%** from the 52-week high of $153.20. Debt about **$35B** at 2026-06-30 vs ~$21B YE2025. July delayed-draw term loan: marketed near SOFR+425–450 at 99, reported clearing as wide as SOFR+500 at 97 / ~9.1% with tighter lockbox terms. 5y CDS ~**855 bps** late July vs ~452 early June vs ~881 Dec 2025 (round-trip, not a new peak). Financing **still closed**. No missed-payment or failed-deal print found this pass. Friday's bounce is an equity mark, not a credit event. | Measured (equity, debt stock, ratings) / Hypothesis-adjacent (CDS and new-issue levels from secondary reporting) | MarketWatch / FinanceCharts 2026-09-04 close. Motley Fool 2026-09-01 (debt, interest expense). Fitch May 2026 IDR BB- Positive. FT 2026-07-30 (DDTL concessions). Friedman 2026-08-09 (new-issue concession and CDS path). |
| 7 | Mag7 weight in SPX | **~33.6%** reconstructed from SPY weights on 2026-09-04: NVDA 8.01 + AAPL 7.26 + MSFT 5.66 + AMZN 3.80 + GOOGL 2.99 + GOOG 2.39 + META 1.93 + TSLA 1.53. Early-August commentary ~34%. Early-June commentary ~35% → ~32% shortly after. Current print is **modest deconcentration**, not a collapse. | Measured (SPY weights) / Hypothesis (June 35→32 path is commentary) | TradeSmith SPY holdings 2026-09-04 still lists NVDA 8.01% top weight and top-10 37.83%. |
| 8 | SOX vs SPX, 3-month | SOX closed **11,735.26** on 2026-09-04, up 3.37% on the day, versus ATH **14,655.29** (~2026-06-22), about **−19.9%** from the high. Barchart 3-month print about **−13.8%** since early June. SPX closed **7,718.60** on 2026-09-04. Semis have already de-rated versus the cap-weight index even after Friday's bounce. | Measured | MarketWatch / Nasdaq SOX 2026-09-04. AP News SPX 2026-09-04. |
| 9 | Equal-weight SPX vs cap-weight, 3-month | ETF.com as-of early Sep shows RSP 3M **+4.48%** vs SPY **+0.99%**; YTD RSP **+15.04%** vs SPY **+12.80%**. Quantlake as-of 2026-09-04 shows RSP 3M +5.8% vs SPY +4.7%. TotalRealReturns through 2026-09-04: YTD RSP +15.26% vs SPY +13.54%. Equal-weight continues to lead on multi-month and year-to-date basis. | Measured | ETF.com comparison; Quantlake 2026-09-04; TotalRealReturns through 2026-09-04. |
| 10 | Capex revision count this season | July Q2 prints: AMZN **$200B → $220B** (up). GOOGL **$180–190B → $195–205B** (up). META floor **$125B → $130B**, range **$130–145B** (up / narrowed). MSFT FY27 outlook **$175B** vs prior calendar ~$190B is a **lease-mix change**, not scored as a cut. **3 up / 0 down** on CY2026 company guides. Sequence step 6 (a hyperscaler capex *cut*) has **not** printed. No new guide action through 2026-09-04. | Measured | Company Q2 2026 guidance language. No subsequent 8-K cut found. |

---

## Tape context (not in the ten)

| Object | Print | Tag |
| --- | --- | --- |
| NVDA last / ATH | Close **$230.36** on 2026-09-04 (+0.84%). 52-week / cycle high **$236.54** on 2026-05-14. About **2.6%** below that high. Market cap ~**$5.5T**. | Measured |
| SPX / NDX levels | S&P 500 **7,718.60** (2026-09-04, AP). Nasdaq-100 **29,544.15**. | Measured |
| SPY top-10 | About **37.83%** (TradeSmith SPY 2026-09-04). | Measured |
| July spender air pocket | META sold off after raising the capex floor and showing FCF $0.78B. GOOGL printed first negative quarterly FCF in its disclosed history and raised capex again. AMZN printed TTM FCF −$7.6B and *raised* capex to $220B; the stock was bid the next session. | Measured (results + subsequent tape) |
| NVDA post-print tape | Q2 FY27 released 2026-08-26. Revenue and DC growth still explosive. Shares recovered toward the May high and closed 2026-09-04 at $230.36. | Measured |
| Cheap-tier token cut | OpenAI 2026-07-30: GPT-5.6 Luna −80% to $0.20/$1.20 per 1M; Terra −20% to $2.00/$12.00. Still listed on the official API page on 2026-09-05. | Measured (provider card) |
| GPU rental | CCIR 2026-09-04 07:30 ET guaranteed on-demand: H100 hyperscaler $10.53 / neocloud $3.71 / marketplace $3.03. No newer daily print at midnight Eastern on 2026-09-05. | Measured as a published series |

---

## What the panel says about the sequence

Plan order of prints if an unwind is underway:

1. Second derivative of capex growth rolls over while the *level* stays huge.
2. FCF and net issuance become the earnings-call topic.
3. Credit, not equity, gaps first in the leveraged tier.
4. Circular deals get smaller, slower, or more collateralized.
5. Utilization or rental-rate softness in secondary compute.
6. Capex guidance cut at one hyperscaler; a second cut confirms regime.
7. Supplier book-to-bill and lead times break.
8. Index deconcentration continues; equal-weight wins multi-quarter.
9. Only then a broad AI-equity drawdown that does not get bought in two weeks.

**As of this snapshot:**

Step 2 is live at Amazon, Alphabet, Meta, and Oracle. Microsoft free cash flow is still positive but down year over year. Step 3 is partially live at the rim because CoreWeave printed a new-issue concession and a CDS round-trip. No hub missed payment has printed. Friday's CoreWeave bounce to $89.36 is an equity mark and does not retire the debt stock. Step 4 is not live as a shrink. The form shifted from a letter of intent to a funded stake plus a residual-value cap, and the size did not shrink. Step 5 is partially live as price and is not live as utilization. Neocloud H100 guaranteed rental is about $3.71 an hour against a hyperscaler list near $10.53, and cheap-tier API tokens were cut in July. Tokens sold and utilization are still unscored. Step 8 is partially live because RSP is beating SPY on a three-month and year-to-date basis, and Magnificent Seven weight is off the June commentary high while still near 34 percent. Step 6 is not live. Guides went up in July, and none have been cut since. Step 7 is not scored on this pass because no supplier book-to-bill primary pack exists yet. Layer C, NVIDIA earnings, is intact. Friday's SOX bounce and the NVIDIA move toward the May high argue against a completed regime change.

That is spender-and-index repricing inside a still-rising capex level, with the output price of the loop already moving down on the cheap tier. It is not a completed unwind sequence.

---

## H4 / H5 read from this panel only

H4 is the claim that July through August 2026 was the start of a regime change, not a violent reset inside an intact boom.

H4 fails as regime change. July completed a loud free-cash-flow scare at the spenders, a SOX drawdown from the June high, and some Path-4 deconcentration. It did not produce a capex cut, a supplier order break, or an NVIDIA earnings break. NVIDIA's August print still showed triple-digit data-center growth and a higher third-quarter guide. Later tape recovered NVIDIA to about 2.6 percent off the May all-time high.

A narrower claim is live. The market has started to price spend without near-term cash payback separately from chip shipments. That split is useful. It is not a claim that the bubble is popping.

H5 is the claim that token and rental prices can jeopardize paper sized on a higher conversion rate.

H5 is open and live on the cheap tier. The 30 July 2026 Luna cut and the 4 September 2026 neocloud rental stack are the price side of the race. The 17 August 2026 $105 billion NVIDIA cap is the paper side. First-party confirmation of OpenAI, Anthropic, Google, and xAI cards on this pass raises source quality and does not add a new cut. Hub marks have not broken. The danger level is 3, not 4 or 5.

The kill condition from the plan for H4 is that by year-end 2026, AI-infra median stocks reclaim June highs, NVIDIA makes a new all-time high on rising data-center growth, and capex guidance is revised up again without another free-cash-flow scare. That condition has not been reached and has not been killed. Revisit it after third-quarter prints.

---

## Nightly snapshot log

- **2026-09-03 America/New_York (nightly).** No new hyperscaler 8-K or 10-Q printed. NVIDIA data-center growth did not roll over on a sequential basis, and no capex guide was cut. The primary panel remains the 2026-09-02 close. SOX closed at 11,339.25. NVIDIA closed at $224.41, about 5 percent off the May high. SPY top-10 weight was 37.83 percent. The Magnificent Seven reconstruction was about 33.6 percent. H4 stays a fail as regime change. The next forced refresh is after Oracle fiscal 2027 first quarter, expected around 10 to 14 September 2026, or after any capex-cut print.

- **2026-09-04 America/New_York (nightly).** No new hyperscaler 8-K or 10-Q printed, and no capex guide was cut. NVIDIA data-center growth did not roll over on a sequential basis. Primary panel numbers are unchanged. NVIDIA closed at $228.45 on 3 September 2026, about 3.4 percent off the May high of $236.54. SOX closed at 11,352.13. The S&P 500 closed at 7,747.71. SPY top-10 weight was still 37.83 percent on TradeSmith. The Magnificent Seven reconstruction was about 33.6 percent. H4 remains a fail as regime change. The next forced refresh is after Oracle fiscal 2027 first quarter, announced for about 10 September 2026, or after any capex-cut print.

- **2026-09-04 America/New_York (late, structure).** The folder was made open-ended and hypothesis H5 was added. `loop-health.md` and `token-prices.md` were opened. The danger level is 3, Stressed, because cheap-tier token prices and neocloud rental have fallen while the August guarantee was added and the hub mark stayed intact. The automation prompt was revised to require a daily loop-health score written in complete sentences. This is not a trading session.

- **2026-09-05 America/New_York (nightly).** No new hyperscaler 8-K or 10-Q printed, and no capex guide was cut. NVIDIA data-center growth did not roll over on a sequential basis. Official OpenAI, Anthropic, Google, and xAI rate cards were confirmed first-party and showed no new list-price cut. CCIR rental was unchanged from the 4 September 07:30 Eastern print. NVIDIA closed at $230.36 on 4 September 2026, about 2.6 percent off the May high of $236.54. SOX closed at 11,735.26, up 3.37 percent on the day and about 19.9 percent below the June high. The S&P 500 closed at 7,718.60. CoreWeave closed at $89.36. SPY top-10 weight was still 37.83 percent on TradeSmith. The Magnificent Seven reconstruction was about 33.6 percent. H4 remains a fail as regime change. H5 remains open and live on the cheap tier. The danger level held at 3, Stressed. The next forced refresh is after Oracle fiscal 2027 first quarter on 10 September 2026, or after any capex-cut or rate-card print.

---

## Refresh rules

Update on a fixed calendar after each hyperscaler or NVIDIA print, not when social media is loud. A provider rate-card cut is a first-class event for H5 and `loop-health.md`, at the same rank as a capex guide revision. Change a row only with a dated source. Write each new snapshot line in complete sentences. The next forced refresh is the third-quarter 2026 earnings season. Oracle fiscal 2027 first quarter is due on 10 September 2026 after the close. Microsoft, Meta, Alphabet, and Amazon follow in late October. WS3 utilization and WS4 hub CDS are still empty as first-class rows. Do not fill them with anecdotes.

See `hypotheses.md` for pass/fail on H1 through H5, `loop-health.md` for the danger level, and `capex-cash.md` for the filing table behind rows 1 through 3.
