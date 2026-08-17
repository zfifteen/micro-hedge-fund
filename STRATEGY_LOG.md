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
Early days will likely be high-variance in approach. The log and this file will surface patterns worth hardening (or discarding) for the larger fund.

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
