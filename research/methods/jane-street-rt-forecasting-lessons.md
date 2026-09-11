# Methods lessons — Jane Street Real-Time Market Data Forecasting

**Source trigger:** [@Rossst_03](https://x.com/Rossst_03/status/2098147737527087452) (2026-09-10) pointing at Jane Street’s Kaggle contest.  
**Contest:** [Jane Street Real-Time Market Data Forecasting](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting) (Oct 2024 → Jul 2025).  
**Status:** Closed. Data, eval API, and winning notebooks remain public.  
**This note:** Research methods only. Not a trade. Not a short. Not an allocation. Presence here does not change Unwind danger.

Labels: **Measured** = contest rules / public writeups / verified URLs. **Hypothesis** = how we apply the idea to Micro Hedge Fund research.

---

## What Jane Street actually tested (Measured)

They did not ask “who has the smartest offline model on a fixed backtest.”

They tested whether a pipeline can:

1. Train on anonymized production-derived features (~79 features, 9 responders; target `responder_6`).
2. Freeze a submission, then score for months on **market data that did not exist at freeze**.
3. Survive **new symbol ids** in the future set (instruments never seen in training).
4. Finish inside a hard notebook budget (8h train / 9h forecast phase) — best model that *completes*.
5. Be judged by **sample-weighted R² taken about zero**: predicting nothing scores exactly 0; a bad model goes negative.

Prize board: $50k first, $120k across top ten; thousands of teams. The durable prize for us is the **evaluation design**, not the dollar prize.

---

## Lessons to keep (map to MHF)

### 1. Score on a future the model never had
**Measured:** Submissions froze ~13 Jan 2025; scoring continued for months against live future data.  
**Hypothesis for MHF:** Prefer tests that can only be settled by prints that have not happened yet (Oracle night, receivables prints, used-GPU marks). A beautiful story that cannot lose on tomorrow’s data is not a test.

### 2. Zero baseline must be honest
**Measured:** Weighted R² about zero → null prediction = 0; worse than null goes negative.  
**Hypothesis for MHF:** Same species as Unwind’s `measured_wall` / dual ledger. A Hypothesis overlay that cannot beat “do nothing / keep danger unchanged” should not raise official danger. Measure lift vs an explicit null.

### 3. Online adaptation beats frozen genius
**Measured (writeups):** Top solutions leaned on **online learning** once new labeled days arrived (small LR updates per `date_id`). Offline-only trees often underperformed once the live window moved. Three-stage pipelines (warm-up → sequential adjust → live online) were common.  
**Hypothesis for MHF:** Research clocks and any future signal models should have a defined **update rule when new Measured data lands**, not only a one-shot fit to the catch-up pack.

### 4. Validate like the private board, not like a shuffled CV
**Measured:** Strong teams simulated public/private with **chronological holdouts and gaps** (e.g. train → gap days → eval), because shuffled K-fold did not track the live board.  
**Hypothesis for MHF:** When we “test” Unwind claims, prefer time-ordered falsifiers (what must print next) over cherry-picked historical analogies.

### 5. Optimize the metric you are judged on
**Measured:** Teams trained with weighted R² / weighted losses matching the official score, not MSE-by-habit.  
**Hypothesis for MHF:** If the object is danger / race / residual exclusion, score those objects — do not optimize narrative fluency or Twitter engagement and call it research quality.

### 6. Runtime and coverage are part of the model
**Measured:** Time limits forced “best that finishes”; heavy feature theaters lost. Minimal features + lag responders often beat ornate engineering that drifted.  
**Hypothesis for MHF:** Prefer pipelines that complete on the agentic cash/research loop (cheap, repeatable, within credit budgets) over ornate one-offs that cannot re-run after the next print.

### 7. New instruments / regimes are first-class
**Measured:** Future test introduced unseen `symbol_id`s.  
**Hypothesis for MHF:** Watchlists and Unwind clocks must degrade gracefully when a new neocloud, SPV, or GPU generation appears — not assume the training universe is closed.

---

## Explicit non-lessons

- Do **not** treat anonymized Jane Street responders as tradable alpha for the MHF book.
- Do **not** import Kaggle ensembling as a reason to place trades.
- Do **not** confuse “online learning on labeled days” with “react to every tweet.” Online updates require **Measured labels** (settled targets), same honesty wall as Unwind.

---

## Standing habits this note commits us to

1. When proposing a research claim, name the **null** and what future print would make the claim lose.
2. Prefer **time-ordered** checks over shuffled retrospectives.
3. When a Measured print lands (filings, rate cards, credit events), update clocks with a written rule — do not only rewrite the narrative.
4. Keep research artifacts **re-runnable** under credit/runtime budgets (same spirit as five vowel searches under a 30-minute cooldown elsewhere).

---

## References

- Contest hub: https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting
- Trigger post: https://x.com/Rossst_03/status/2098147737527087452
- Example writeup themes: [8th place — online learning + weighted R²](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/writeups/evgeniia-grigoreva-private-lb-8th-solution); public repos summarizing three-stage + online updates (e.g. Billy1900/JS-Kaggle-2025).
- Related internal honesty object: `research/unwind/phase-space/` (`measured_wall`).
