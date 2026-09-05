# Token-economics plots

This directory holds an illustrative model of one claim in the unwind research: if the price a lab can charge for tokens falls toward or below the extra cost of serving those tokens, selling more tokens does not cover the money already spent on clusters, leases, and training. The model is a teaching sketch. It is not a measurement of any company.

Presence of these charts is not a trading instruction. A **short** would be a bet that a price will fall. A **hedge** would be a position taken to offset another position. An **allocation** would be a decision to put cash into a name. This folder does none of those things.

Every number in the script is **Hypothesis**. Hypothesis means the value was chosen to show a relationship, not read from a filing or a rate card. Measured token and rental prices, when they exist, live in `../token-prices.md`.

H5 is the standing claim this sketch belongs to. H5 says listed token prices and GPU rental are the cash that installed computer chips actually produce, and that a fall in those prices can threaten financing that was sized as if the old, higher prices would continue.

## The formula

The script treats monthly profit as:

```text
Profit = (P − Cv) · V − F
```

That is the same as writing revenue minus variable cost minus fixed cost:

```text
Profit = P · V − Cv · V − F
```

The four symbols mean the following.

### P — price per unit of tokens

**P** is the money the seller receives for one million tokens. In the script the unit is dollars per million tokens, written `$ / MTok`. A token is a small piece of text the model reads or writes. One million tokens is a convenient billing unit used on public API price lists.

**P** is a realized price, not always the advertised list price of the flagship model. If customers move to cheaper models, the average **P** across all tokens can fall even when the flagship list price is unchanged. Chart 7 is about that mix shift.

### Cv — variable cost per unit of tokens

**Cv** is the extra cost of serving one more million tokens, in the same unit as **P** (`$ / MTok`). Variable means the cost scales with volume. In this sketch that extra cost is meant to stand for energy, cloud markup, and the share of running a cluster that rises when more tokens are served.

**Cv** is not the whole cost of the business. Training runs, data-center leases, and chips that have already been bought sit in **F**, not in **Cv**.

If **P** is larger than **Cv**, each extra million tokens contributes cash toward covering **F**. If **P** equals **Cv**, extra tokens contribute nothing toward **F**. If **P** is smaller than **Cv**, each extra million tokens loses money before **F** is even subtracted.

### V — volume

**V** is how many tokens are sold in the month. In the script **V** is stored in million-token units so that `P * V / 1e6` lands in millions of dollars. The charts label large volumes in trillions of tokens per month because that is an easier scale to read.

Volume is not the same as revenue. Revenue is **P** times **V**. Volume can rise while revenue falls if **P** falls faster than **V** grows. Chart 1 is about that case.

### F — fixed cost

**F** is the monthly cost that does not shrink when fewer tokens are sold, and does not disappear when more tokens are sold. In the script **F** is 900, meaning 900 million dollars per month. That number is Hypothesis. It is a round stand-in for clusters, leases, training amortization, and power contracts that are already committed.

Because **F** is treated as already committed, leaving the chips idle does not cancel **F**. The sketch therefore asks what happens when the seller keeps filling the machines at whatever **P** the market will pay.

### (P − Cv) — contribution margin per unit

**P − Cv** is the cash left from one million tokens after paying the extra cost of serving them, and before paying **F**. That difference is the contribution margin.

- If **P − Cv** is positive and large, more **V** raises profit and can cover **F**.
- If **P − Cv** is positive but small, a very large **V** is required to cover **F**.
- If **P − Cv** is zero, no finite **V** covers **F**.
- If **P − Cv** is negative, more **V** makes the monthly loss larger.

### Break-even volume

If **P** is greater than **Cv**, the volume that makes profit exactly zero is:

```text
V_break_even = F / (P − Cv)
```

As **P** gets closer to **Cv**, the denominator shrinks and the required volume grows without bound. When **P** is less than or equal to **Cv**, the formula has no useful solution: selling more cannot cover **F**. Chart 4 draws that curve.

## Units in the script

| Symbol | Meaning | Unit in the script |
|---|---|---|
| P | Price received per million tokens | dollars per million tokens |
| Cv | Extra cost per million tokens | dollars per million tokens |
| V | Tokens sold in the month | million-token units internally; charts often show trillions |
| F | Committed monthly cost | millions of dollars per month |
| P · V | Revenue | millions of dollars per month |
| Cv · V | Variable cost | millions of dollars per month |
| (P − Cv) · V − F | Profit | millions of dollars per month |

The three lettered paths in the script (A, B, and C) are not three companies. They are three Hypothesis trajectories for how **P**, **Cv**, and **V** might move over 25 months.

- Path A: **P** and **Cv** fall at the same modest rate, and volume grows. Contribution margin stays healthier than in B or C.
- Path B: **P** falls faster, but is not allowed to go below 0.50 dollars per million tokens. Volume grows faster than in A.
- Path C: **P** falls still faster, with a floor of 0.35 dollars per million tokens, while **Cv** stays stickier. Volume grows fastest. This is the price-war path used in the profit-and-loss chart.

A **knob** is a number at the top of the script that you can change to see a different sketch. The main knobs are **F**, the starting values of **P** and **Cv**, and the monthly multipliers that make those series fall or grow.

## What each chart shows

1. **Revenue peak.** Revenue is **P** times **V**. If **P** falls faster than **V** grows, monthly revenue can rise for a while and then fall. A rising token count is not enough, by itself, to keep revenue rising.

2. **Three regimes.** Profit is drawn against volume at three fixed pairs of **P** and **Cv**. In the healthy case, the profit line slopes up. In the thin-margin case, it slopes up slowly. In the case where **P** is below **Cv**, the profit line slopes down: more volume deepens the loss.

3. **Volume identity.** The same formula as chart 2, with **P** and **Cv** held fixed so the slope versus volume is easy to see. Negative unit margin means the line falls as volume rises.

4. **Break-even volume.** For a fixed **Cv**, the chart shows how many tokens would be needed to cover **F** at each **P**. The required volume heads toward infinity as **P** approaches **Cv**. To the left of **Cv**, there is no break-even volume.

5. **Path C profit and loss.** Along the price-war path, volume and even revenue can look acceptable while profit gets worse, because **F** does not shrink when **P** falls.

6. **Revenue per GPU-hour.** A GPU-hour is one hour of time on one graphics processor. The sketch assumes a committed pool of GPU-hours whose monthly cost is **F**. Revenue per GPU-hour is then total token revenue divided by those hours. If the machines stay full but **P** falls, each already-bought hour produces less cash while its committed cost stays the same.

7. **Mix shift.** The flagship model's advertised price can stay put while a larger share of tokens is served by cheaper models. The blended realized **P** is the volume-weighted average of the flagship price and the budget-model price. That blended **P** is what enters the profit formula, not the flagship list price alone.

## How to regenerate the charts

From this directory:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python token_economics_charts.py
```

`python3 -m venv .venv` creates a private Python environment in a folder named `.venv` so the libraries used here do not mix with the rest of the machine. `pip install -r requirements.txt` installs NumPy (array math) and Matplotlib (plotting). Running the script writes PNG image files into `charts/`. The `.venv` folder is local and is not stored in the repository.

To see a harsher sketch, change knobs in `token_economics_charts.py`:

- Make **P** fall faster, for example by using a smaller monthly multiplier such as `0.85 ** months`, to represent a deeper price war.
- Raise **Cv** if energy or cloud markup does not fall when token prices fall.
- Raise **F** if new clusters are still being financed while prices fall.

`0.85 ** months` means each month's price is 85 percent of the previous month's price. After two months the price is `0.85 × 0.85` of the start, and so on.

## Files

| File | Job |
|---|---|
| `token_economics_charts.py` | Python script that draws the seven charts from the formula above |
| `requirements.txt` | List of Python libraries the script needs (NumPy and Matplotlib) |
| `charts/01_revenue_peak.png` | Chart 1, revenue versus month on paths A, B, and C |
| `charts/02_three_regimes.png` | Chart 2, profit versus volume in three margin regimes |
| `charts/03_volume_identity.png` | Chart 3, profit versus volume with **P** and **Cv** fixed |
| `charts/04_breakeven.png` | Chart 4, tokens needed to cover **F** as **P** nears **Cv** |
| `charts/05_pnl_path.png` | Chart 5, path C volume, revenue, **F**, and profit |
| `charts/06_gpu_hour.png` | Chart 6, revenue per committed GPU-hour versus that hour's cost |
| `charts/07_mix_shift.png` | Chart 7, flagship list **P**, budget **P**, and blended realized **P** |
