# Research note — watchlist decision tree — 2026-08-28

Profile: process, not a trading session. No orders. Presence on a list is not a buy. Cash is a valid position.

**Measured** = live Robinhood book/quotes, company IR already in the 8/27 log and 8/22 research note, Kansas City Fed symposium page. **Hypothesis** = secondary Jackson Hole preview copy and bottleneck commentary. Personal/curated account lists were not used as input.

## Why a tree at all

Two lists exist on the Agentic account (last4 7524):

- `+MHF-candidates` — names that could absorb part of the $100 cash sleeve at the next 12:15 session
- `+MHF-macro` — instruments quoted for tape/context only

The lists are a scratchpad. The public repo remains the system of record. This tree is a filter for *this* tape, not a standing strategy.

## Live state used (measured, ~01:50 ET 2026-08-28)

- Cash $100.00 / buying power $100.00 / equity ~$93.95 / account ~$193.95
- Positions unchanged: MU 0.048553 @ 1029.80, NVDA 0.132240 @ 226.86, QQQ 0.027306 @ 732.44
- Prior close 8/27: MU 935.39, NVDA 227.98, QQQ 721.11
- Overnight prints were softer in the book names (MU ~914, NVDA ~226, QQQ ~719) — treat as after-hours, not a session fill
- Agentic option level empty. Crypto order placement still not a reliable write path.
- Warsh Jackson Hole keynote: Friday 10:00 ET, before the 12:15 session. Kansas City Fed symposium page lists it as opening remarks.

## Tree

```
0. Executable on this account in regular hours with this connector?
   No options / no crypto / no futures → reject
   Fractional equity or ETF → continue

1. What job does the name have?
   Read the tape at 12:15 → +MHF-macro
   Could take part of the $100 sleeve today → +MHF-candidates
   Neither → reject

2. MACRO — keep only if it answers a live session question
   Broad risk → SPY
   Nasdaq vs broad (book already holds QQQ) → QQQ
   Risk appetite outside mega-tech → IWM
   Semi complex vs the single names → SMH (not also SOXX)
   Policy / duration (Warsh 10:00) → TLT
   Real-rate shock → GLD
   Dollar / Treasury-channel shock → UUP
   Cap ~7. Reject duplicates and third-order credit/financials.

3. CANDIDATES — must pass all
   a. A live question exists for *this* session (not “interesting company”)
   b. $100 can express it in regular hours
   c. Distinct from other names on the list (no clone cluster)
   d. Tied to a primary source or to the standing book thesis *this week*
   e. Changes the book: add-to-held, cheaper expression of the same factor, or a missing factor

4. After two sessions without a sentence in the daily log → remove
```

## Run — candidates

| Name | Gate | Result |
|---|---|---|
| MU | Add-to-held. NVDA 8/26 print named memory as a constraint. Largest hole vs cost. 8/27 log already asked this question. | KEEP |
| NVDA | Add-to-held. Own print confirmed the compute thesis. Must still pass a chase check after Thursday’s move. | KEEP |
| QQQ | Already held Nasdaq beta; look-through overlaps MU/NVDA. Weakest use of new cash. Context only. | REJECT → macro |
| SMH / SOXX | Same factor the book already has. | REJECT → SMH on macro |
| AVGO / TSM / AMAT / LRCX / ASML | No session-primary source. Equipment was not the named bottleneck. | REJECT |
| MRVL | No thesis for this sleeve. Overnight print looked noisy vs the official close. | REJECT |
| SNDK | NAND is not the HBM constraint NVDA named. | REJECT |
| CEG | Missing factor. Power is the other named AI-infra bottleneck; book has zero power. One name, not a power basket. Hypothesis, not a company primary from this week. | KEEP |
| VST / VRT | Second and third power names. One is enough. | REJECT |
| CRM | Software-spend confirmation. Dilutes an infra book at $100 scale. | REJECT |
| AMD | Competitor GPU, not a complement. | REJECT |
| TLT | Policy-hedge alternative to leaving the sleeve in cash after Warsh. | KEEP |
| GLD | Weaker policy expression than TLT or cash. | REJECT → macro |

Seeded `+MHF-candidates`: **MU, NVDA, CEG, TLT**

## Run — macro

Intended seed: **SPY, QQQ, IWM, SMH, TLT, GLD, UUP**

First write to `+MHF-candidates` succeeded. The follow-up write to `+MHF-macro` was blocked by connector dedup on `add_to_watchlist` in this session. Recover on the next tool-capable turn if the list is still empty. Session can still quote those seven symbols directly.

## What 12:15 still owns

The list is not an allocation. Allocation of the $100 sleeve after the Warsh text is a trading decision: add MU, add NVDA, open CEG, buy TLT, or keep cash. Inaction remains valid.
