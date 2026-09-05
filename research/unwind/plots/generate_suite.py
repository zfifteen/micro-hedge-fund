#!/usr/bin/env python3
"""Unwind visualization suite — chart generator.

Identity charts (01–07) are Hypothesis sketches of
Profit = (P − Cv) · V − F.

Loop charts (08–20) use figures from research/unwind notes
as of 2026-09-05. Each axis is labeled. None of this is a trade.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "charts"
OUT.mkdir(exist_ok=True)

INK = "#e8eadc"
MUTED = "#9aa186"
BG = "#0c0f0c"
AX = "#141914"
GRID = "#262b1e"
EDGE = "#3a4030"
GREEN = "#7cb389"
AMBER = "#c4a35a"
RED = "#d45d4a"
BLUE = "#7aa0b4"
PURPLE = "#b08dcc"
WHITE = "#e8eadc"

plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": AX,
        "axes.edgecolor": EDGE,
        "axes.labelcolor": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": INK,
        "grid.color": GRID,
        "legend.facecolor": "#1a1f16",
        "legend.edgecolor": EDGE,
        "legend.labelcolor": INK,
        "savefig.facecolor": BG,
        "savefig.dpi": 170,
        "axes.grid": True,
        "axes.axisbelow": True,
        "axes.titleweight": "medium",
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "font.size": 11,
        "legend.fontsize": 9.5,
    }
)


def money_fmt(x, _p=None):
    if abs(x) >= 1000:
        return f"${x / 1000:.1f}B"
    if abs(x) >= 1:
        return f"${x:.0f}M"
    return f"${x:.2f}M"


def billions(x, _p=None):
    return f"${x:.0f}B"


def save(fig, name, tight=True):
    path = OUT / name
    if tight:
        fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(path.name)


def footer(ax, text):
    ax.text(
        0.0,
        -0.16,
        text,
        transform=ax.transAxes,
        fontsize=8.5,
        color=MUTED,
        ha="left",
        va="top",
        clip_on=False,
    )


def new_ax(h=5.5, w=11.2):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_color(EDGE)
    return fig, ax


# ---------------------------------------------------------------------------
# 01–07 Hypothesis identity
# ---------------------------------------------------------------------------
months = np.arange(0, 25)
F = 900.0
P_A, Cv_A = 4.00 * 0.96**months, 1.10 * 0.96**months
V_A = 200e6 * 1.12**months
P_B = np.clip(4.00 * 0.88**months, 0.50, None)
Cv_B, V_B = 1.10 * 0.95**months, 200e6 * 1.16**months
P_C = np.clip(4.00 * 0.85**months, 0.35, None)
Cv_C, V_C = 1.30 * 0.97**months, 200e6 * 1.18**months


def pnl(P, Cv, V):
    rev = P * V / 1e6
    vc = Cv * V / 1e6
    return rev, vc, rev - vc - F


def fig_01():
    rev_A, _, _ = pnl(P_A, Cv_A, V_A)
    rev_B, _, _ = pnl(P_B, Cv_B, V_B)
    rev_C, _, _ = pnl(P_C, Cv_C, V_C)
    fig, ax = new_ax()
    ax.plot(months, rev_A, color=GREEN, lw=2.4, label="A  P and Cv fall together")
    ax.plot(months, rev_B, color=AMBER, lw=2.4, label="B  price war, floor $0.50")
    ax.plot(months, rev_C, color=RED, lw=2.4, label="C  P falls faster than V grows")
    ax.set_xlabel("Months from the start of the sketch")
    ax.set_ylabel("Monthly revenue")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
    ax.legend(loc="upper left")
    footer(ax, "Hypothesis · illustrative paths, not a company filing")
    save(fig, "01_revenue_peak.png")


def fig_02():
    V = np.linspace(10e6, 800e6, 200)
    fig, ax = new_ax()
    for P, Cv, c, lab in [
        (3.50, 1.00, GREEN, "A  P > Cv   volume helps"),
        (1.40, 1.10, AMBER, "B  thin margin"),
        (0.70, 1.10, RED, "C  P < Cv   volume hurts"),
    ]:
        ax.plot(V / 1e6, (P - Cv) * V / 1e6 - F, color=c, lw=2.5, label=lab)
    ax.axhline(0, color=INK, ls=":", lw=1)
    ax.set_xlabel("Volume (trillion tokens / month, sketch units)")
    ax.set_ylabel("Monthly profit")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
    ax.legend()
    footer(ax, "Hypothesis · F = $900M / month held fixed")
    save(fig, "02_three_regimes.png")


def fig_03():
    V = np.linspace(10e6, 800e6, 200)
    fig, ax = new_ax()
    for P, Cv, c, lab in [
        (3.50, 1.00, GREEN, "P > Cv  volume helps"),
        (1.40, 1.10, AMBER, "thin margin"),
        (0.70, 1.10, RED, "P < Cv  volume hurts"),
    ]:
        ax.plot(V / 1e6, (P - Cv) * V / 1e6 - F, color=c, lw=2.5, label=lab)
    ax.axhline(0, color=INK, ls=":", lw=1)
    ax.set_xlabel("Volume (trillion tokens / month, sketch units)")
    ax.set_ylabel("Monthly profit")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
    ax.legend()
    footer(ax, "Hypothesis · Profit = (P − Cv)·V − F with P and Cv held fixed")
    save(fig, "03_volume_identity.png")


def fig_04():
    P_line = np.linspace(0.3, 4.0, 250)
    Cv_be = 0.90
    ok = P_line > Cv_be + 0.02
    Vbe = np.full_like(P_line, np.nan)
    Vbe[ok] = (F * 1e6) / (P_line[ok] - Cv_be) / 1e6
    fig, ax = new_ax()
    ax.plot(P_line, Vbe, color=PURPLE, lw=2.6)
    ax.axvline(Cv_be, color=RED, ls="--", label=f"Cv = ${Cv_be:.2f} per million tokens")
    ax.set_ylim(0, 12)
    ax.set_xlabel("P (dollars per million tokens)")
    ax.set_ylabel("Tokens needed to cover F (trillions, sketch units)")
    ax.legend()
    footer(ax, "Hypothesis · break-even volume = F / (P − Cv)")
    save(fig, "04_breakeven.png")


def fig_05():
    rev_C, _, profit_C = pnl(P_C, Cv_C, V_C)
    fig, ax = new_ax()
    ax.plot(months, V_C / 1e6, color=BLUE, lw=2.2, label="Volume (sketch units)")
    ax2 = ax.twinx()
    ax2.plot(months, rev_C, color=GREEN, lw=2.2, label="Revenue")
    ax2.plot(months, np.full_like(months, F), color=MUTED, ls="--", lw=1.6, label="Fixed cost F")
    ax2.plot(months, profit_C, color=RED, lw=2.6, label="Profit")
    ax.set_xlabel("Months from the start of the sketch")
    ax.set_ylabel("Volume (trillion tokens / month, sketch units)")
    ax2.set_ylabel("Dollars")
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(money_fmt))
    ax2.tick_params(colors=MUTED, length=0)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left")
    footer(ax, "Hypothesis · path C  ·  F does not shrink when P falls")
    save(fig, "05_pnl_path.png")


def fig_06():
    gpu_hours = 1.2e6
    cost_per_hour = F * 1e6 / gpu_hours
    rev_per_hour = (P_C * V_C) / gpu_hours
    fig, ax = new_ax()
    ax.plot(months, rev_per_hour, color=BLUE, lw=2.5, label="Revenue per GPU-hour")
    ax.axhline(
        cost_per_hour,
        color=RED,
        ls="--",
        lw=1.8,
        label="Committed cost per GPU-hour",
    )
    ax.set_xlabel("Months from the start of the sketch")
    ax.set_ylabel("Dollars per GPU-hour")
    ax.legend()
    footer(ax, "Hypothesis · GPU-hour pool held fixed at 1.2 million hours / month")
    save(fig, "06_gpu_hour.png")


def fig_07():
    flagship_p = np.full_like(months, 4.00, dtype=float)
    budget_p = np.clip(2.00 * 0.86**months, 0.25, None)
    flagship_share = np.clip(0.70 * 0.94**months, 0.12, None)
    blended = flagship_share * flagship_p + (1 - flagship_share) * budget_p
    fig, ax = new_ax()
    ax.plot(months, flagship_p, color=GREEN, lw=2.4, label="Flagship list P")
    ax.plot(months, budget_p, color=AMBER, lw=2.2, label="Budget-model P")
    ax.plot(months, blended, color=RED, lw=2.6, label="Blended realized P")
    ax.set_xlabel("Months from the start of the sketch")
    ax.set_ylabel("Dollars per million tokens")
    ax.legend()
    footer(ax, "Hypothesis · blended P is what enters the profit formula")
    save(fig, "07_mix_shift.png")


# ---------------------------------------------------------------------------
# 08–20 Measured / mixed from unwind notes as-of 2026-09-05
# ---------------------------------------------------------------------------
def blended(inp, out, w_in=3, w_out=1):
    return (w_in * inp + w_out * out) / (w_in + w_out)


def fig_08():
    rows = [
        ("GPT-6 Astra", 10.00, 50.00, "flagship"),
        ("Claude Fable 5.1", 10.00, 50.00, "flagship"),
        ("Claude Opus 5", 5.00, 25.00, "flagship"),
        ("GPT-5.6 Sol promo", 4.00, 20.00, "mid"),
        ("GPT-5.6 Terra", 2.00, 12.00, "mid"),
        ("Gemini 3.1 Pro ≤200k", 2.00, 12.00, "mid"),
        ("Claude Sonnet 5", 2.00, 10.00, "mid"),
        ("Grok 4.6 <200k", 2.00, 6.00, "mid"),
        ("Claude Haiku 4.5", 1.00, 5.00, "cheap"),
        ("Gemini 3.8 Flash intro", 0.75, 3.75, "cheap"),
        ("GPT-5.6 Luna", 0.20, 1.20, "cheap"),
    ]
    labels = [r[0] for r in rows][::-1]
    vals = [blended(r[1], r[2]) for r in rows][::-1]
    colors = [{"flagship": GREEN, "mid": AMBER, "cheap": RED}[r[3]] for r in rows][::-1]
    fig, ax = new_ax(h=6.4)
    ax.barh(labels, vals, color=colors, height=0.72)
    ax.set_xlabel("Blended dollars per million tokens  ·  (3×input + 1×output) / 4")
    ax.legend(
        handles=[
            plt.Line2D([0], [0], color=GREEN, lw=6, label="Flagship"),
            plt.Line2D([0], [0], color=AMBER, lw=6, label="Mid-tier"),
            plt.Line2D([0], [0], color=RED, lw=6, label="Cheap tier"),
        ],
        loc="lower right",
    )
    footer(ax, "Measured · official API cards read 2026-09-05  ·  3:1 blend is a convention, not a filing")
    save(fig, "08_token_cards.png")


def fig_09():
    rows = [
        ("Astra", 10, 50),
        ("Fable 5.1", 10, 50),
        ("Opus 5", 5, 25),
        ("Sol promo", 4, 20),
        ("Terra", 2, 12),
        ("Gemini Pro", 2, 12),
        ("Sonnet 5", 2, 10),
        ("Grok 4.6", 2, 6),
        ("Haiku 4.5", 1, 5),
        ("Flash intro", 0.75, 3.75),
        ("Luna", 0.20, 1.20),
    ]
    x = np.arange(len(rows))
    inp = [r[1] for r in rows]
    out = [r[2] for r in rows]
    fig, ax = new_ax(h=5.8)
    w = 0.38
    ax.bar(x - w / 2, inp, w, color=BLUE, label="Input  $/1M")
    ax.bar(x + w / 2, out, w, color=AMBER, label="Output  $/1M")
    ax.set_xticks(x, [r[0] for r in rows], rotation=28, ha="right")
    ax.set_ylabel("Dollars per million tokens")
    ax.legend()
    footer(ax, "Measured · official API cards 2026-09-05  ·  standard processing, not batch")
    save(fig, "09_input_output.png")


def fig_10():
    labels = [
        "Luna input",
        "Luna output",
        "Terra input",
        "Terra output",
    ]
    before = [1.00, 6.00, 2.50, 15.00]
    after = [0.20, 1.20, 2.00, 12.00]
    x = np.arange(len(labels))
    w = 0.36
    fig, ax = new_ax()
    ax.bar(x - w / 2, before, w, color=MUTED, label="Before 2026-07-30")
    ax.bar(x + w / 2, after, w, color=RED, label="Still listed 2026-09-05")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Dollars per million tokens")
    ax.legend()
    footer(ax, "Measured · OpenAI first-party cut 2026-07-30  ·  Terra −20% implied prior card 2.50 / 15.00")
    save(fig, "10_july_cuts.png")


def fig_11():
    sil = ["B300", "B200", "H200", "H100", "A100"]
    hs = [np.nan, 14.24, 10.30, 10.53, 4.45]
    neo = [7.67, 6.69, 4.40, 3.71, 2.04]
    mkt = [7.42, 5.99, 4.00, 3.03, 1.43]
    x = np.arange(len(sil))
    w = 0.26
    fig, ax = new_ax()
    ax.bar(x - w, hs, w, color=BLUE, label="Hyperscaler guaranteed")
    ax.bar(x, neo, w, color=AMBER, label="Neocloud guaranteed")
    ax.bar(x + w, mkt, w, color=RED, label="Marketplace")
    ax.set_xticks(x, sil)
    ax.set_ylabel("Dollars per GPU-hour")
    ax.legend()
    footer(ax, "Measured as a published series · CCIR 2026-09-04 07:30 ET · US & EU on-demand")
    save(fig, "11_gpu_rental.png")


def fig_12():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 5.6))
    fig.subplots_adjust(bottom=0.22, wspace=0.55, left=0.22, right=0.97, top=0.88)
    for ax in (ax1, ax2):
        ax.set_facecolor(AX)
        ax.tick_params(length=0, colors=MUTED)
        for s in ax.spines.values():
            s.set_color(EDGE)
        ax.grid(True, color=GRID, axis="x")
        ax.set_axisbelow(True)

    names = ["AI-cloud land / power / shell", "SB Energy residual-value cap"]
    vals = [3.5, 105.0]
    ax1.barh(names, vals, color=[BLUE, AMBER], height=0.5)
    ax1.set_xlabel("Gross maximum exposure, $ billions")
    ax1.set_title("NVIDIA guarantee book", loc="left", fontsize=11, color=INK, pad=10)

    labs = ["H100 marketplace", "H100 neocloud", "H100 hyperscaler"]
    rents = [3.03, 3.71, 10.53]
    cols = [RED, AMBER, BLUE]
    ax2.barh(labs, rents, color=cols, height=0.5)
    ax2.set_xlabel("Dollars per GPU-hour")
    ax2.set_title("Last-gen rental, same day", loc="left", fontsize=11, color=INK, pad=10)

    fig.text(
        0.01,
        0.03,
        "Measured · NVDA 8-K 2026-08-17 / 10-Q  ·  CCIR 2026-09-04  ·  different units on purpose",
        color=MUTED,
        fontsize=8.5,
    )
    save(fig, "12_guarantee_vs_rental.png", tight=False)


def fig_13():
    rows = [
        ("Oracle remaining performance obligations", 638),
        ("AWS performance obligations not yet recognized", 496),
        ("Microsoft uncommenced datacenter leases", 329),
        ("Microsoft contracted incremental Azure (OpenAI)", 250),
        ("AWS–OpenAI commercial (38 + 100)", 138),
        ("NVIDIA residual-value cap", 105),
        ("AWS–Anthropic expansion (more than)", 100),
        ("Amazon OpenAI equity closed", 50),
        ("NVIDIA funded OpenAI equity", 30),
    ]
    labels = [r[0] for r in rows][::-1]
    vals = [r[1] for r in rows][::-1]
    fig, ax = new_ax(h=6.2)
    ax.barh(labels, vals, color=AMBER, height=0.66)
    ax.set_xlabel("Dollars, billions  ·  do not add these into one total")
    footer(
        ax,
        "Measured from filings and IR  ·  announced is not funded is not guaranteed is not revenue  ·  2026-09-05 pack",
    )
    save(fig, "13_circular_book.png")


def fig_14():
    names = ["AMZN\nQ2", "GOOGL\nQ2", "META\nQ2", "MSFT\nFY Q4", "ORCL\nFY26"]
    capex = [53.1, 44.9, 30.1, 35.8, 55.7]
    ocf = [45.4, 39.1, 31.9, 55.4, 32.0]
    fcf = [-7.6, -5.9, 0.78, 19.6, -23.7]
    # AMZN FCF shown is TTM −7.6; others are the period in the notes
    x = np.arange(len(names))
    w = 0.26
    fig, ax = new_ax()
    ax.bar(x - w, capex, w, color=AMBER, label="Cash capex / PPE")
    ax.bar(x, ocf, w, color=BLUE, label="Operating cash flow")
    ax.bar(x + w, fcf, w, color=RED, label="Free cash flow (company)")
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_xticks(x, names)
    ax.set_ylabel("Billions of dollars")
    ax.legend()
    footer(
        ax,
        "Measured · company FCF definitions differ  ·  AMZN FCF is TTM; ORCL is full FY26; others are the quarter cited",
    )
    save(fig, "14_capex_ocf_fcf.png")


def fig_15():
    names = ["AMZN", "GOOGL mid", "META floor"]
    before = [200, 185, 125]
    after = [220, 200, 130]
    x = np.arange(len(names))
    fig, ax = new_ax(h=5.0)
    for i, (b, a) in enumerate(zip(before, after)):
        ax.plot([i, i], [b, a], color=AMBER, lw=2)
        ax.scatter([i], [b], color=MUTED, s=50, zorder=3, label="Prior guide" if i == 0 else "")
        ax.scatter([i], [a], color=GREEN, s=70, zorder=3, label="July revision (up)" if i == 0 else "")
        ax.text(i + 0.08, a, f"${a}B", color=GREEN, va="center", fontsize=9)
    ax.set_xticks(x, names)
    ax.set_ylabel("Calendar 2026 capex guide, $ billions")
    ax.set_ylim(110, 240)
    ax.legend()
    footer(ax, "Measured · July Q2 season  ·  3 up / 0 down  ·  MSFT FY27 $175B is a lease-mix change, not scored as a cut")
    save(fig, "15_guide_revisions.png")


def fig_16():
    names = ["AMZN Q2", "GOOGL Q2", "META Q2", "MSFT Q4", "ORCL FY26"]
    ratio = [1.17, 1.15, 0.94, 0.65, 1.74]
    colors = [RED if r >= 1 else AMBER if r >= 0.9 else GREEN for r in ratio]
    fig, ax = new_ax()
    ax.bar(names, ratio, color=colors, width=0.55)
    ax.axhline(1.0, color=INK, ls="--", lw=1.2, label="Capex equals operating cash flow")
    ax.set_ylabel("Cash capex / operating cash flow")
    ax.legend()
    footer(ax, "Measured · four-name Q2 sum 163.9 / 171.8 ≈ 0.95  ·  ratio above 1 means capex exceeded OCF")
    save(fig, "16_capex_ocf_ratio.png")


def fig_17():
    names = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "META", "TSLA"]
    wgt = [8.01, 7.26, 5.66, 3.80, 2.99, 2.39, 1.93, 1.53]
    fig, ax = new_ax()
    ax.bar(names, wgt, color=BLUE, width=0.62)
    ax.set_ylabel("Weight in SPY, percent")
    ax.axhline(0, color=EDGE)
    tot = sum(wgt)
    ax.text(
        0.99,
        0.95,
        f"Mag7 reconstruction  {tot:.1f}%",
        transform=ax.transAxes,
        ha="right",
        va="top",
        color=INK,
        fontsize=11,
    )
    footer(ax, "Measured · TradeSmith SPY holdings 2026-09-04  ·  top-10 of SPY was 37.83%")
    save(fig, "17_mag7_weights.png")


def fig_18():
    labels = ["3-month", "Year to date"]
    rsp = [4.48, 15.04]
    spy = [0.99, 12.80]
    x = np.arange(len(labels))
    w = 0.32
    fig, ax = new_ax(h=5.0)
    ax.bar(x - w / 2, rsp, w, color=GREEN, label="RSP  equal-weight S&P")
    ax.bar(x + w / 2, spy, w, color=BLUE, label="SPY  cap-weight S&P")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Total return, percent")
    ax.legend()
    footer(ax, "Measured · ETF.com as-of early September 2026")
    save(fig, "18_equal_weight.png")


def fig_19():
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 5.0))
    for ax in axes:
        ax.set_facecolor(AX)
        ax.tick_params(length=0, colors=MUTED)
        for s in ax.spines.values():
            s.set_color(EDGE)
        ax.grid(True, color=GRID)
        ax.set_axisbelow(True)

    ax = axes[0]
    ax.bar(["52-week high", "Close 2026-09-04"], [153.20, 89.36], color=[MUTED, RED], width=0.55)
    ax.set_ylabel("Share price, dollars")
    ax.set_title("CoreWeave equity", loc="left", fontsize=11, color=INK, pad=10)

    ax = axes[1]
    ax.plot(
        ["Dec 2025", "Early Jun", "Late Jul"],
        [881, 452, 855],
        color=AMBER,
        lw=2.4,
        marker="o",
    )
    ax.set_ylabel("5-year CDS, basis points")
    ax.set_title("CDS path (secondary)", loc="left", fontsize=11, color=INK, pad=10)

    ax = axes[2]
    ax.bar(["YE 2025", "2026-06-30"], [21, 35], color=[BLUE, AMBER], width=0.55)
    ax.set_ylabel("Debt, $ billions")
    ax.set_title("Debt stock", loc="left", fontsize=11, color=INK, pad=10)

    fig.text(
        0.01,
        0.02,
        "Mixed · equity and debt stock Measured  ·  CDS and new-issue path Hypothesis-adjacent (secondary tape)",
        color=MUTED,
        fontsize=8.5,
    )
    save(fig, "19_rim_credit.png")


def fig_20():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 5.4))
    for ax in (ax1, ax2):
        ax.set_facecolor(AX)
        ax.tick_params(length=0, colors=MUTED)
        for s in ax.spines.values():
            s.set_color(EDGE)
        ax.grid(True, color=GRID, axis="y")
        ax.set_axisbelow(True)

    ax1.bar(
        ["Rest of NVIDIA", "Data Center"],
        [96.221 - 89.023, 89.023],
        color=[MUTED, GREEN],
        width=0.5,
    )
    ax1.set_ylabel("Q2 FY27 revenue, $ billions")
    ax1.set_title("NVIDIA Q2 FY27 mix", loc="left", fontsize=11, color=INK, pad=10)

    ax2.bar(
        ["Customer A", "Customer B", "Customer C"],
        [16, 15, 13],
        color=BLUE,
        width=0.5,
    )
    ax2.set_ylabel("Share of H1 FY27 revenue, percent")
    ax2.set_title("Three direct customers", loc="left", fontsize=11, color=INK, pad=10)

    fig.text(
        0.01,
        0.02,
        "Measured · NVDA 10-Q Q2 FY27  ·  Data Center $89.023B, +117% YoY, +18% QoQ  ·  company GM 75.0%",
        color=MUTED,
        fontsize=8.5,
    )
    save(fig, "20_nvda_hub.png")


def fig_21():
    fig, ax = plt.subplots(figsize=(11.2, 5.2))
    ax.set_facecolor(AX)
    for s in ax.spines.values():
        s.set_color(EDGE)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.add_patch(
        FancyBboxPatch(
            (0.08, 0.22),
            0.84,
            0.56,
            boxstyle="round,pad=0.02,rounding_size=0.02",
            linewidth=1.0,
            edgecolor=EDGE,
            facecolor="#10140f",
        )
    )
    ax.text(0.5, 0.58, "Not scored", ha="center", va="center", fontsize=22, color=INK)
    ax.text(
        0.5,
        0.42,
        "Tokens sold and GPU utilization have no first-class primary print\n"
        "in this pack. A rate card is not utilization. A rental series is not volume.",
        ha="center",
        va="center",
        fontsize=11,
        color=MUTED,
        linespacing=1.5,
    )
    footer(ax, "Empty on purpose · H5 stays open until a volume offset is measured")
    save(fig, "21_unscored_volume.png")


def main():
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    fig_08()
    fig_09()
    fig_10()
    fig_11()
    fig_12()
    fig_13()
    fig_14()
    fig_15()
    fig_16()
    fig_17()
    fig_18()
    fig_19()
    fig_20()
    fig_21()
    print("done", len(list(OUT.glob("*.png"))), "pngs")


if __name__ == "__main__":
    main()
