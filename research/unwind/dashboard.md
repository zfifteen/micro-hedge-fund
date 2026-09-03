# Dashboard v1 — AI capex unwind watch

Opened 2026-09-03. Snapshot date **2026-09-02 close** unless a row says otherwise.

This file is a measurement panel, not a trade. Presence here is not a short, not a hedge, and not an allocation. It does not replace a session log and does not change `state/portfolio.json` or `STRATEGY_LOG.md`.

Rule from the plan: no new unwind *narrative* until at least two of {2, 3, 5, 6, 10} move together.

Every input is tagged **Measured** or **Hypothesis**. Commentary used only when the primary print is named.

---

## Ten-number panel

| # | Metric | Latest print | Tag | Source |
| --- | --- | --- | --- | --- |
| 1 | Combined CY2026 capex guide (AMZN, MSFT, GOOGL, META) | About **$735–750B** after July revisions. Working midpoint **~$747B** if AMZN $220B + GOOGL mid $200B + META mid $137.5B + MSFT calendar ~$190B. Bases are **not identical** (Meta includes finance-lease principal; Microsoft lease mix is shifting). | Measured (company guides) | AMZN Q2 2026 release / call ($220B cash capex). GOOGL Q2 call ($195–205B). META Q2 exhibit 99-1 ($130–145B incl. lease principal). MSFT FY26 Q4 call + prior calendar commentary (~$190B CY; FY27 outlook $175B is a different basis). Platformonomics Q2 2026 scoreboard 2026-07-31 ($735–750B). |
| 2 | Combined capex / OCF | Calendar Q2 cash PPE / OCF: AMZN 53.1 / 45.4 = **1.17**; MSFT 35.8 / 55.4 = **0.65**; GOOGL 44.9 / 39.1 = **1.15**; META PPE 30.1 / 31.9 = **0.94**. Four-name sum **163.9 / 171.8 ≈ 0.95**. ORCL FY26 (year ended 2026-05-31) **55.7 / 32.0 = 1.74**. | Measured | See `capex-cash.md`. AMZN 10-Q MD&A cash capex $53.1B, OCF $45.387B. MSFT FY26 Q4 call. GOOGL Q2 8-K / 10-Q. META exhibit 99-1. ORCL FY26 10-K. |
| 3 | Combined FCF | AMZN TTM to 2026-06-30 **−$7.6B**. MSFT Q4 FY26 **+$19.6B**. GOOGL Q2 **−$5.855B**. META Q2 **+$0.784B**. ORCL FY26 **−$23.686B**. Definitions are company-specific; do not add them into one “true” total. | Measured | AMZN Q2 2026 press release (exhibit 99-1). MSFT FY26 Q4 call. GOOGL Q2 8-K non-GAAP FCF. META exhibit 99-1. ORCL FY26 results / 10-K. |
| 4 | NVDA data-center YoY and gross margin | Q2 FY27 (ended 2026-07-26): Data Center **$89.023B**, **+117% YoY**, **+18% QoQ**. Company gross margin **75.0%**. Total revenue $96.221B. Q3 guide $108.0B ±2%. | Measured | NVDA 10-Q accession `0001045810-26-000075`. |
| 5 | NVDA customer concentration / financed-commitment notes | Q2 FY27: **one direct customer 16%** of revenue. H1 FY27: three directs **16% / 15% / 13%**. Filing also states one AI research-and-deployment company contributed a meaningful amount *indirectly* by buying cloud from NVDA customers. Guarantee / site notes live in `circular-finance.md` (SB Energy residual-value guarantees; AI-cloud land/power/shell). | Measured | Same 10-Q, customer-concentration and commitments discussion. |
| 6 | One neocloud credit or equity stress print | **CoreWeave (CRWV)**. Equity ~$82, about **−47%** from 52-week high. Debt about **$35B** at 2026-06-30 vs ~$21B YE2025. July delayed-draw term loan: marketed near SOFR+425–450 at 99, reported clearing as wide as SOFR+500 at 97 / ~9.1% with tighter lockbox terms. 5y CDS ~**855 bps** late July vs ~452 early June vs ~881 Dec 2025 (round-trip, not a new peak). Financing **still closed**. No missed-payment or failed-deal print found this pass. | Measured (equity, debt stock, ratings) / Hypothesis-adjacent (CDS and new-issue levels from secondary reporting) | Motley Fool 2026-09-01 (price, debt, interest expense). Fitch May 2026 IDR BB- Positive. FT 2026-07-30 (DDTL concessions). Friedman 2026-08-09 (new-issue concession and CDS path). |
| 7 | Mag7 weight in SPX | **~33.6%** reconstructed from SPY weights on 2026-09-02: NVDA 8.01 + AAPL 7.26 + MSFT 5.66 + AMZN 3.80 + GOOGL 2.99 + GOOG 2.39 + META 1.93 + TSLA 1.53. Early-August commentary ~34%. Early-June commentary ~35% → ~32% shortly after. Current print is **modest deconcentration**, not a collapse. | Measured (SPY weights) / Hypothesis (June 35→32 path is commentary) | TradeSmith SPY holdings 2026-09-02. Motley Fool / ETF.com Aug 2026 ~34%. CME OpenMarkets June path. |
| 8 | SOX vs SPX, 3-month | SOX **−18.52%** 3-month (MarketWatch as of 2026-09-02). SPY **+1.4%** 3-month (Quantlake as of 2026-08-31). SOX last **11,339.25** vs ATH **14,655.29** (~2026-06-22), about **−23%** from the high. Semis have already de-rated versus the cap-weight index. | Measured | FRED NASDAQSOX 2026-09-02. MarketWatch SOX performance table. Quantlake SPY vs RSP 2026-08-31. |
| 9 | Equal-weight SPX vs cap-weight, 3-month | RSP **+5.3%** vs SPY **+1.4%** for the 3 months to 2026-08-31. Early-August YTD: RSP +13.1% vs VOO ~10%. Equal-weight is winning on a multi-month basis. | Measured | Quantlake 2026-08-31. TheStreet / Benzinga via 2026-08-27 RSP AUM piece. S&P DJI equal-weight dashboard through 2026-07-31 (EW beat cap-weight in June and July). |
| 10 | Capex revision count this season | July Q2 prints: AMZN **$200B → $220B** (up). GOOGL **$180–190B → $195–205B** (up). META floor **$125B → $130B**, range **$130–145B** (up / narrowed). MSFT FY27 outlook **$175B** vs prior calendar ~$190B is a **lease-mix change**, not scored as a cut. **3 up / 0 down** on CY2026 company guides. Sequence step 6 (a hyperscaler capex *cut*) has **not** printed. | Measured | Company Q2 2026 guidance language. |

---

## Tape context (not in the ten)

| Object | Print | Tag |
| --- | --- | --- |
| NVDA last / ATH | Close **$224.41** on 2026-09-02. 52-week / cycle high **$236.54** on 2026-05-14 (intraday; 2026-05-14 close near $235.74). About **5%** below that high. Market cap ~**$5.3T**. Trailing P/E ~**27–28**. | Measured |
| SPX / NDX levels | S&P 500 **7,666.60**. Nasdaq-100 **29,143.33**. VIX **15.20**. | Measured (2026-09-02) |
| SPY top-10 | About **37.8%** (TradeSmith SPY) to **40.6%** (tradmap S&P list). Different universes; do not average. | Measured |
| July spender air pocket | META sold off after raising the capex floor and showing FCF $0.78B. GOOGL printed first negative quarterly FCF in its disclosed history and raised capex again. AMZN printed TTM FCF −$7.6B and *raised* capex to $220B; the stock was bid the next session. | Measured (results + subsequent tape) |
| NVDA post-print tape | Q2 FY27 released 2026-08-26. Revenue and DC growth still explosive. Shares were not a crash print. | Measured |

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

- Step 2 is **live** at AMZN, GOOGL, META, and ORCL. MSFT FCF is still positive but down YoY.
- Step 3 is **partially live** at the rim (CoreWeave new-issue concession + CDS round-trip). No hub missed payment.
- Step 8 is **partially live** (RSP beating SPY on 3-month and YTD; Mag7 weight off the June commentary high, still ~34%).
- Step 6 is **not live**. Guides went *up* in July.
- Step 7 is **not scored** this pass (no supplier book-to-bill primary pack yet).
- Layer C (NVDA earnings) is **intact**.

That is spender-and-index repricing inside a still-rising capex *level*. It is not a completed unwind sequence.

---

## H4 read from this panel only

H4 = “July–August 2026 was the start of a regime change, not a violent reset inside an intact boom.”

**Fail as regime change.** July completed a loud FCF scare at the spenders, a SOX drawdown from the June high, and some Path-4 deconcentration. It did not produce a capex cut, a supplier order break, or a NVDA earnings break. NVDA’s August print still showed triple-digit DC growth and a higher Q3 guide.

**Live as a narrower claim:** the market has started to price *spend without near-term cash payback* separately from *chip shipments*. That is a useful split. It is not “the bubble is popping.”

Kill condition from the plan: by year-end 2026, AI-infra median stocks reclaim June highs, NVDA makes a new ATH on rising (not just stable) data-center growth, and capex guidance is revised *up* again without another FCF scare. Not yet reached and not yet killed. Revisit after Q3 prints.

---

## Refresh rules

- Update on a fixed calendar after each hyperscaler / NVDA print, not when social media is loud.
- Change a row only with a dated source.
- Next forced refresh: Q3 2026 earnings season (ORCL FY27 Q1 due ~2026-09-14; then MSFT/META/GOOGL/AMZN late October).
- WS3 utilization and WS4 hub CDS still empty as first-class rows. Do not fill them with anecdotes.

See `hypotheses.md` for pass/fail on H1–H4 and `capex-cash.md` for the filing table behind rows 1–3.
