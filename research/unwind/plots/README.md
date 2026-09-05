# Token-economics plots

This directory holds an illustrative model of the token-lab identity behind H5. It is a process file. Presence of these charts is not a short, not a hedge, and not an allocation.

Every number in the script is **Hypothesis**. The charts show relationships, not audited lab financials and not measured rate-card prints. Measured token and rental prices live in `../token-prices.md`.

## Claim under illustration

Profit is `(P − Cv) · V − F`. Volume only helps when contribution margin `P − Cv` is positive and stays positive as list prices fall. When `P` approaches or undercuts `Cv`, extra tokens scale the loss. Break-even volume goes to infinity as `P` approaches `Cv`, then becomes undefined.

That is the cash-conversion half of the loop: token list prices and GPU-hours are the only cash the installed silicon prints. If those output prices gap down while committed clusters and paper are already live, filling the boxes at the new price does not cover the fixed cost base.

## Files

| File | Job |
|---|---|
| `token_economics_charts.py` | Generator. Knobs at the top: `F`, starting `P`/`Cv`, monthly decay and growth rates |
| `requirements.txt` | `numpy` and `matplotlib` |
| `charts/01_revenue_peak.png` | Revenue can peak and fall when `P` drops faster than `V` grows |
| `charts/02_three_regimes.png` | Healthy margin, thin margin, and `P < Cv` |
| `charts/03_volume_identity.png` | Same identity with `P` and `Cv` held fixed |
| `charts/04_breakeven.png` | Tokens required to cover `F` as `P` approaches `Cv` |
| `charts/05_pnl_path.png` | Path C P&L: volume and revenue versus profit |
| `charts/06_gpu_hour.png` | Realization per already-bought GPU-hour |
| `charts/07_mix_shift.png` | Flagship list holds while blended realized `P` collapses |

## How to regenerate

From this directory:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python token_economics_charts.py
```

Charts write to `charts/`. `.venv/` is local and is not part of the repository.

Stress-test the claim by changing three knobs in the script:

- Cut `P` faster (for example `0.85 ** months`) to deepen the price war.
- Raise `Cv` if energy or cloud markup is sticky.
- Raise `F` if new clusters are still being financed while prices fall.
