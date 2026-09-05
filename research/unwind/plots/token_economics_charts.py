#!/usr/bin/env python3
"""Illustrative token-lab P&L charts. Not audited financials.

Profit = (P − Cv) · V − F
When P − Cv shrinks or turns negative, more volume does not close the hole.

Knobs at the top: F, starting P/Cv, and the monthly decay/growth rates.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

OUT = Path(__file__).resolve().parent / "charts"
OUT.mkdir(exist_ok=True)

plt.rcParams.update(
    {
        "figure.facecolor": "#0f1419",
        "axes.facecolor": "#161b22",
        "axes.edgecolor": "#30363d",
        "axes.labelcolor": "#e6edf3",
        "xtick.color": "#8b949e",
        "ytick.color": "#8b949e",
        "text.color": "#e6edf3",
        "grid.color": "#21262d",
        "legend.facecolor": "#1c2128",
        "legend.edgecolor": "#30363d",
        "legend.labelcolor": "#e6edf3",
        "savefig.facecolor": "#0f1419",
        "savefig.dpi": 160,
        "axes.grid": True,
        "axes.axisbelow": True,
        "axes.titleweight": "bold",
    }
)

months = np.arange(0, 25)
F = 900.0  # $ millions / month fixed cost

# Paths: V in million tokens, P and Cv in $ / MTok
P_A = 4.00 * 0.96**months
Cv_A = 1.10 * 0.96**months
V_A = 200e6 * 1.12**months
P_B = np.clip(4.00 * 0.88**months, 0.50, None)
Cv_B = 1.10 * 0.95**months
V_B = 200e6 * 1.16**months
P_C = np.clip(4.00 * 0.85**months, 0.35, None)
Cv_C = 1.30 * 0.97**months
V_C = 200e6 * 1.18**months


def money_fmt(x, _p=None):
    return f"${x / 1000:.1f}B" if abs(x) >= 1000 else f"${x:.0f}M"


def pnl(P, Cv, V):
    rev = P * V / 1e6
    vc = Cv * V / 1e6
    return rev, vc, rev - vc - F


def save(fig, name):
    path = OUT / name
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    print(path)


# 1. Price falls faster than volume grows → revenue peaks, then drops
rev_A, _, _ = pnl(P_A, Cv_A, V_A)
rev_B, _, _ = pnl(P_B, Cv_B, V_B)
rev_C, _, _ = pnl(P_C, Cv_C, V_C)
fig, ax = plt.subplots(figsize=(11, 5.4))
ax.plot(months, rev_A, color="#3fb950", lw=2.4, label="A  P and Cv fall together")
ax.plot(months, rev_B, color="#d29922", lw=2.4, label="B  price war, floor $0.50")
ax.plot(months, rev_C, color="#f85149", lw=2.4, label="C  P falls faster than V grows")
ax.set_xlabel("Months")
ax.set_ylabel("Monthly revenue")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
ax.set_title("1. Revenue can peak and fall when P drops faster than V grows")
ax.legend()
save(fig, "01_revenue_peak.png")

# 2. Three regimes — healthy, thin, below variable cost
V = np.linspace(10e6, 800e6, 200)
fig, ax = plt.subplots(figsize=(11, 5.4))
for P, Cv, c, lab in [
    (3.50, 1.00, "#3fb950", "A  P > Cv  volume helps"),
    (1.40, 1.10, "#d29922", "B  thin margin"),
    (0.70, 1.10, "#f85149", "C  P < Cv  volume hurts"),
]:
    ax.plot(V / 1e6, (P - Cv) * V / 1e6 - F, color=c, lw=2.5, label=lab)
ax.axhline(0, color="#e6edf3", ls=":", lw=1)
ax.set_xlabel("Volume (trillion tokens / month)")
ax.set_ylabel("Monthly profit")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
ax.set_title("2. Three regimes — only A is saved by volume")
ax.legend()
save(fig, "02_three_regimes.png")

# 3. Identity, holding P and Cv fixed
fig, ax = plt.subplots(figsize=(11, 5.4))
for P, Cv, c, lab in [
    (3.50, 1.00, "#3fb950", "P > Cv  volume helps"),
    (1.40, 1.10, "#d29922", "thin margin"),
    (0.70, 1.10, "#f85149", "P < Cv  volume hurts"),
]:
    ax.plot(V / 1e6, (P - Cv) * V / 1e6 - F, color=c, lw=2.5, label=lab)
ax.axhline(0, color="#e6edf3", ls=":", lw=1)
ax.set_xlabel("Volume (trillion tokens / month)")
ax.set_ylabel("Monthly profit")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
ax.set_title("3. Profit = (P − Cv)·V − F   (P and Cv held fixed)")
ax.legend()
save(fig, "03_volume_identity.png")

# 4. Break-even volume as P → Cv
P_line = np.linspace(0.3, 4.0, 250)
Cv_be = 0.90
ok = P_line > Cv_be + 0.02
Vbe = np.full_like(P_line, np.nan)
Vbe[ok] = (F * 1e6) / (P_line[ok] - Cv_be) / 1e6
fig, ax = plt.subplots(figsize=(11, 5.4))
ax.plot(P_line, Vbe, color="#a371f7", lw=2.6)
ax.axvline(Cv_be, color="#f85149", ls="--", label=f"Cv=${Cv_be:.2f}")
ax.set_ylim(0, 12)
ax.set_xlabel("P ($ / MTok)")
ax.set_ylabel("Tokens to cover F (trillions)")
ax.set_title("4. Break-even volume → ∞ as P → Cv")
ax.legend()
save(fig, "04_breakeven.png")

# 5. Price-war path as a P&L (volume and revenue can look fine)
rev_C, vc_C, profit_C = pnl(P_C, Cv_C, V_C)
fig, ax = plt.subplots(figsize=(11, 5.4))
ax.plot(months, V_C / 1e6, color="#58a6ff", lw=2.2, label="Volume (trillions)")
ax2 = ax.twinx()
ax2.plot(months, rev_C, color="#3fb950", lw=2.2, label="Revenue")
ax2.plot(months, np.full_like(months, F), color="#8b949e", ls="--", lw=1.6, label="Fixed cost F")
ax2.plot(months, profit_C, color="#f85149", lw=2.6, label="Profit")
ax.set_xlabel("Months")
ax.set_ylabel("Volume (trillion tokens / month)")
ax2.set_ylabel("Dollars")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
ax.set_title("5. Path C P&L — volume and revenue vs profit (F does not shrink)")
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper left")
save(fig, "05_pnl_path.png")

# 6. Realization per already-bought GPU-hour
gpu_hours = 1.2e6  # committed hours / month
cost_per_hour = F * 1e6 / gpu_hours
rev_per_hour = (P_C * V_C) / gpu_hours
fig, ax = plt.subplots(figsize=(11, 5.4))
ax.plot(months, rev_per_hour, color="#58a6ff", lw=2.5, label="Revenue / GPU-hour")
ax.axhline(cost_per_hour, color="#f85149", ls="--", lw=1.8, label="Committed cost / GPU-hour")
ax.set_xlabel("Months")
ax.set_ylabel("$ / GPU-hour")
ax.set_title("6. Fill the boxes cheaper → each GPU-hour more underwater")
ax.legend()
save(fig, "06_gpu_hour.png")

# 7. Mix shift: flagship list holds, blended P collapses
flagship_p = np.full_like(months, 4.00, dtype=float)
budget_p = np.clip(2.00 * 0.86**months, 0.25, None)
flagship_share = np.clip(0.70 * 0.94**months, 0.12, None)
blended = flagship_share * flagship_p + (1 - flagship_share) * budget_p
fig, ax = plt.subplots(figsize=(11, 5.4))
ax.plot(months, flagship_p, color="#3fb950", lw=2.4, label="Flagship list P")
ax.plot(months, budget_p, color="#d29922", lw=2.2, label="Budget-model P")
ax.plot(months, blended, color="#f85149", lw=2.6, label="Blended realized P")
ax.set_xlabel("Months")
ax.set_ylabel("$ / MTok")
ax.set_title("7. Mix shift — list price holds, blended P still collapses")
ax.legend()
save(fig, "07_mix_shift.png")

print("done")
