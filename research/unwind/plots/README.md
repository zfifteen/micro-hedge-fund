# Token-economics plots

Open [`index.html`](index.html) in a browser from this folder. That file is the visualization suite: a chaptered letter with twenty-one figures, a glossary, and a caption under every chart. Keys `J` and `K` move between figures.

This directory is a process file. Presence of these charts is not a short, not a hedge, and not an allocation.

Every number is tagged in the suite. **Measured** means a filing, an official API card, or a named published series. **Hypothesis** means the value was chosen to show a relationship. Measured token and rental prices live in `../token-prices.md`. Capex and cash live in `../capex-cash.md`. Circular paper lives in `../circular-finance.md`.

H5 is the standing claim the identity sketch belongs to. H5 says listed token prices and GPU rental are the cash that installed computer chips actually produce, and that a fall in those prices can threaten financing that was sized as if the old, higher prices would continue.

## The formula

The first seven figures treat monthly profit as:

```text
Profit = (P − Cv) · V − F
```

That is the same as writing revenue minus variable cost minus fixed cost:

```text
Profit = P · V − Cv · V − F
```

### P — price per unit of tokens

**P** is the money the seller receives for one million tokens. In the script the unit is dollars per million tokens, written `$ / MTok`. A token is a small piece of text the model reads or writes. One million tokens is a convenient billing unit used on public API price lists.

**P** is a realized price, not always the advertised list price of the flagship model. If customers move to cheaper models, the average **P** across all tokens can fall even when the flagship list price is unchanged.

### Cv — variable cost per unit of tokens

**Cv** is the extra cost of serving one more million tokens, in the same unit as **P**. Variable means the cost scales with volume. In this sketch that extra cost stands for energy, cloud markup, and the share of running a cluster that rises when more tokens are served.

**Cv** is not the whole cost of the business. Training runs, data-center leases, and chips that have already been bought sit in **F**, not in **Cv**.

If **P** is larger than **Cv**, each extra million tokens contributes cash toward covering **F**. If **P** equals **Cv**, extra tokens contribute nothing toward **F**. If **P** is smaller than **Cv**, each extra million tokens loses money before **F** is even subtracted.

### V — volume

**V** is how many tokens are sold in the month. Volume is not the same as revenue. Revenue is **P** times **V**. Volume can rise while revenue falls if **P** falls faster than **V** grows.

### F — fixed cost

**F** is the monthly cost that does not shrink when fewer tokens are sold. In the identity sketch **F** is 900 million dollars per month. That number is Hypothesis.

Because **F** is treated as already committed, leaving the chips idle does not cancel **F**. The sketch therefore asks what happens when the seller keeps filling the machines at whatever **P** the market will pay.

### (P − Cv) — contribution margin per unit

**P − Cv** is the cash left from one million tokens after paying the extra cost of serving them, and before paying **F**.

- If **P − Cv** is positive and large, more **V** raises profit and can cover **F**.
- If **P − Cv** is positive but small, a very large **V** is required to cover **F**.
- If **P − Cv** is zero, no finite **V** covers **F**.
- If **P − Cv** is negative, more **V** makes the monthly loss larger.

### Break-even volume

If **P** is greater than **Cv**, the volume that makes profit exactly zero is:

```text
V_break_even = F / (P − Cv)
```

As **P** gets closer to **Cv**, the required volume grows without bound. When **P** is less than or equal to **Cv**, selling more cannot cover **F**.

## Units in the identity sketch

| Symbol | Meaning | Unit in the script |
|---|---|---|
| P | Price received per million tokens | dollars per million tokens |
| Cv | Extra cost per million tokens | dollars per million tokens |
| V | Tokens sold in the month | million-token units internally; charts often show trillions |
| F | Committed monthly cost | millions of dollars per month |
| P · V | Revenue | millions of dollars per month |
| Cv · V | Variable cost | millions of dollars per month |
| (P − Cv) · V − F | Profit | millions of dollars per month |

Paths A, B, and C are not three companies. They are three Hypothesis trajectories for how **P**, **Cv**, and **V** might move over 25 months.

- Path A: **P** and **Cv** fall at the same modest rate, and volume grows.
- Path B: **P** falls faster, but is not allowed to go below 0.50 dollars per million tokens.
- Path C: **P** falls still faster, with a floor of 0.35 dollars per million tokens, while **Cv** stays stickier. This is the price-war path used in the profit-and-loss chart.

A **knob** is a number at the top of the identity sketch that you can change. The main knobs are **F**, the starting values of **P** and **Cv**, and the monthly multipliers that make those series fall or grow.

## Chart index

Identity charts are Hypothesis. Loop charts use the 2026-09-05 unwind pack. Full captions live in `index.html`.

| File | Tag | Claim | What it is |
|---|---|---|---|
| `charts/01_revenue_peak.png` | Hypothesis | H5 | Revenue can peak when **P** falls faster than **V** grows |
| `charts/02_three_regimes.png` | Hypothesis | H5 | Healthy margin, thin margin, and **P** below **Cv** |
| `charts/03_volume_identity.png` | Hypothesis | H5 | Profit versus volume with **P** and **Cv** held fixed |
| `charts/04_breakeven.png` | Hypothesis | H5 | Tokens needed to cover **F** as **P** nears **Cv** |
| `charts/05_pnl_path.png` | Hypothesis | H5 | Path C volume and revenue versus profit |
| `charts/06_gpu_hour.png` | Hypothesis | H5 | Revenue per already-bought GPU-hour |
| `charts/07_mix_shift.png` | Hypothesis | H5 | Flagship list holds while blended **P** falls |
| `charts/08_token_cards.png` | Measured | H5 | Official API cards, 3:1 blended |
| `charts/09_input_output.png` | Measured | H5 | Input versus output list prices |
| `charts/10_july_cuts.png` | Measured | H5 | OpenAI Luna and Terra, 2026-07-30 |
| `charts/11_gpu_rental.png` | Measured series | H5 | Hyperscaler / neocloud / marketplace GPU-hour |
| `charts/12_guarantee_vs_rental.png` | Measured | H3, H5 | NVIDIA guarantee book beside H100 rental |
| `charts/13_circular_book.png` | Measured | H3 | Backlog, leases, equity, residual-value caps |
| `charts/14_capex_ocf_fcf.png` | Measured | H2 | Capex, operating cash flow, free cash flow |
| `charts/15_guide_revisions.png` | Measured | H2, H4 | July CY2026 capex guides, 3 up / 0 down |
| `charts/16_capex_ocf_ratio.png` | Measured | H2 | Cash capex divided by operating cash flow |
| `charts/17_mag7_weights.png` | Measured | H1 | SPY weights on 2026-09-04 |
| `charts/18_equal_weight.png` | Measured | H1 | RSP versus SPY, 3-month and year-to-date |
| `charts/19_rim_credit.png` | Mixed | H3 | CoreWeave equity, CDS path, debt stock |
| `charts/20_nvda_hub.png` | Measured | H4 | NVIDIA data-center mix and customer concentration |
| `charts/21_unscored_volume.png` | Not scored | H5 | Tokens sold and utilization have no primary print |

## How to regenerate

From this directory:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python generate_suite.py
```

`generate_suite.py` writes all twenty-one PNG files into `charts/`. `token_economics_charts.py` still draws only the original identity seven. `.venv/` is local and is not part of the repository.

To see a harsher identity sketch, change knobs in `generate_suite.py`:

- Make **P** fall faster, for example by using a smaller monthly multiplier such as `0.85 ** months`.
- Raise **Cv** if energy or cloud markup does not fall when token prices fall.
- Raise **F** if new clusters are still being financed while prices fall.

`0.85 ** months` means each month’s price is 85 percent of the previous month’s price.

## Files

| File | Job |
|---|---|
| `index.html` | Navigable letter. Open this. |
| `generate_suite.py` | Draws all twenty-one charts |
| `token_economics_charts.py` | Original identity-seven generator |
| `requirements.txt` | NumPy and Matplotlib |
| `charts/` | PNG files named in the index above |
