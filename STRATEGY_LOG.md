# Strategy Log — Evolution of Approach

Because there is no fixed strategy, this file tracks how the decision process itself changes over time.

Format for each entry:

```
## YYYY-MM-DD
**What changed**  
**Why**  
**Expected impact on future decisions**
```

---

## 2026-08-16 — Launch
**What changed**  
Initial setup. No strategy locked in. Daily reasoning from first principles, news, fundamentals, and technicals as judged relevant. Full autonomy, no hard risk limits.

**Why**  
Maximize learning surface area. A rigid systematic strategy at $100 scale would teach less about judgment under uncertainty than open-ended daily reasoning.

**Expected impact**  
Early days will likely be high-variance in approach. The log and this file will surface patterns worth hardening (or discarding).

## 2026-08-16 — Fractional preference locked in
**What changed**  
Fractional equity trades are now the preferred and default method. Whole-share trades are secondary.

**Why**  
$100 starting capital. Whole shares force the fund into 1–2 large positions. Fractional allows multiple simultaneous ideas, finer sizing, and more decision artifacts per dollar.

**Expected impact**  
More positions in the early log. Learning surface area expands. Trades will preferentially use market / dollar_amount orders during regular hours only.

## 2026-08-16 — INFOSEC / redaction rules added
**What changed**  
Non-negotiable information security rules added to AGENTS.md, TRADING_RULES.md, and the daily automation prompt. Full account numbers, PII, and unnecessary identifiers are forbidden in the public repo.

**Why**  
The repository is public for educational value. Real identifiers would destroy that value and create unnecessary risk.

**Expected impact**  
All future logs and state files will be written with deliberate redaction. Last-4 only (or omit). Clean public artifact stream preserved.

## 2026-08-16 — AGENTS.md made single source of truth
**What changed**  
Removed duplicated INFOSEC and operating rules from TRADING_RULES.md and slimmed the automation prompt. AGENTS.md is now the canonical location for all standing agent rules (including INFOSEC). Other documents and the automation prompt reference it instead of repeating content.

**Why**  
Duplication creates maintenance problems and drift risk. Single source of truth is cleaner and more reliable.

**Expected impact**  
Future rule changes only need to be made in AGENTS.md. Lower chance of inconsistent instructions across files and the daily automation.

## 2026-08-16 — Priority hierarchy clarified
**What changed**  
Explicit priority order added to AGENTS.md and the automation prompt:
1. Grow the account.
2. Preserve capital while attempting to grow it.
3. Produce high-quality decision artifacts as a natural byproduct.

Losses are never a planned educational tool. Every decision must be oriented toward increasing account value over time.

**Why**  
Previous framing risked the agent treating losses as acceptable or intentional for learning. That is incorrect. Education occurs through competent attempts to compound capital, not through accepting losses.

**Expected impact**  
All future decisions will be made with growth as the primary objective. Inaction remains valid when no high-conviction opportunity exists; deliberate loss-seeking does not.

## 2026-08-18 — Direct-to-main only
**What changed**  
Standing rule added: all routine session updates (portfolio.json, daily logs, process notes) must be pushed directly to the `main` branch. No feature branches or pull requests for daily runs on this repository.

**Why**  
Explicit operator instruction. For this small, single-agent, high-frequency educational experiment, the PR workflow adds friction without benefit. Direct main keeps the public artifact stream continuous and simple.

**Expected impact**  
Future daily sessions will always land on main. AGENTS.md updated to make the rule non-negotiable for any agent running the fund.

## 2026-08-19 — Session FAILED: local git is not a completed run
**What changed**  
The 2026-08-19 session is recorded as FAILED. Trading decision (hold) was made and logged locally, but the write to GitHub `main` did not complete in-session. Operator had to call it out. Recovery write happened later via the GitHub connector.

Standing rule added: a session is FAILED unless `main` contains that day’s log and updated portfolio.json before the agent reports done. Write path is the GitHub connector only. Local clone + `git push` is not an acceptable completion path.

**Why**  
The public repo is the system of record. A local commit that never leaves the sandbox is invisible. Treating that as success is a process error. The extra hop (clone, commit, HTTPS push) failed on missing credentials and should not have been used.

**Expected impact**  
Future sessions write straight to `main` through the connector first, then report done. If the write fails, the run is FAILED and must be recovered immediately, not described as complete.

## 2026-08-19 — Write retries are mandatory
**What changed**  
Added a standing retry rule. If a GitHub write fails, retry immediately. Minimum 3 in-session attempts. Switch method on retry (connector `push_files`, then per-file create-or-update, then read-back verification from `main`). Do not report done after one failed attempt. Keep recovering until the files are on `main` or the operator stops the run.

**Why**  
The first 2026-08-19 write failed once on missing local git credentials and the agent stopped. That is insufficient. Transient auth/path failures are expected. One attempt is not a serious try.

**Expected impact**  
A single failed push will no longer end a session. Agents will burn retries and alternate write methods before declaring failure.

## 2026-08-20 — Public framing: retail, not a scaled-up fund
**What changed**  
README purpose text only. AGENTS.md and trading behavior unchanged. Status line updated from pre-launch “no positions” to live retail book.

**Why**  
Outside readers were treating “later inform a much larger hedge fund” as a scaling plan. This is a retail-brokerage autonomous trading experiment. The $100 ceiling is the whole book, not a seed for an institutional fund.

**Expected impact**  
No change to daily reasoning, priority hierarchy, or execution. Public docs stop implying an institutional destination.

## 2026-08-27 — Contributions are not P&L; cash from deposits is not an automatic buy signal
**What changed**  
Operator added $100 cash to the Agentic account. Total contributed capital is now $200. portfolio.json now tracks `contributed_capital` separately from mark-to-market value. Mid-session deposits do not trigger an unscheduled deployment. Cash remains a valid position until the next full reasoning cycle.

**Why**  
Mixing contributions into reported performance would make the book look like it doubled when it only received new capital. Spending new cash the hour it arrives, especially after a same-day catalyst pop in the largest idea, is an impulse — not a decision. The morning session already completed a hold with no buying power; the deposit arrived after that work.

**Expected impact**  
Future reports quote contributed capital and account value separately. Trading P&L is account value minus total contributions. New cash is available to deploy but is not required to be deployed the same day. Next session owns allocation of the $100 sleeve.

## 2026-08-28 — Convenience lists
**What changed**  
Added two Robinhood lists for convenience: `+MHF-candidates` and `+MHF-macro`. The agent may modify them or create new lists.

**Why**  
Operator instruction.

**Expected impact**  
The lists are available as a convenience. The agent may modify them or create new lists.
