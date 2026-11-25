---
name: evidence-audit
description: >-
  Formal read-only code review, bug-severity calibration (P0-P2 /
  BLOCKING-MINOR), collateral-impact checks, PR-merge, CI, or release provenance
  verdicts bound to exact commits and evidence. Do not use for quick advisory
  status checks, active code fixes (engineering-workflow), UI screenshot/render
  walkthroughs (ui-design), or as a substitute for human UI acceptance.
---

# Evidence Audit

Issue formal `PASS`, `PASS_WITH_FOLLOWUPS`, or `STOP` verdicts strictly from directly observed evidence.

## Fast route

| Audit scope | Mode | Next reading |
| --- | --- | --- |
| Code review, severity triage (`P0`–`P2`), or bounded `CODE_DIFF` / `PR_MERGE` verdict (with live PR gate state) | `DIFF_OR_PR_AUDIT` | **NONE (this file)** (load [audit-contract.md](references/audit-contract.md) for `SANDBOXED_APP` profile) |
| Standalone `CI` workflow, `RELEASE_PROVENANCE`, `POST_CHANGE`, or multi-artifact audit | `DEEP_PROVENANCE_OR_CI_AUDIT` | [audit-contract.md](references/audit-contract.md) |

## Inline diff, review & severity calibration workflow

1. **Bind identity, threat profile & independence:** state exact repo, base/head SHA or PR, active `THREAT_PROFILE` (`SERVICE_OR_UNTRUSTED_INPUT` default; `SANDBOXED_APP` when declared by project `AGENTS.md`), live host check state, and `AUDIT_INDEPENDENCE` (`SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN`). Never count an implementation self-check as independent acceptance.
2. **Collateral & root-vs-leaf check FIRST (before single-point findings):** inspect sibling entrypoints/screens sharing the state, whether only one leaf symptom was patched, upgrade/data-retention safety, and whether extra defensive layers create new bugs. Collateral regressions outrank isolated defects.
3. **Real-path severity gate (`BLOCKING`/`P0`, `IMPORTANT`/`P1`, `MINOR`/`P2`):**
   - `BLOCKING` (`P0`) and `IMPORTANT` (`P1`) findings **must** state all 3: **(a) reachable trigger path** under `THREAT_PROFILE`, **(b) observable user/caller impact**, and **(c) trigger condition/frequency**. Missing any 1 auto-downgrades to `MINOR` (`P2`, log 1-line reason; non-blocking); `>=3` independent low-probability conditions or sub-ms races without a real path become 1-line `BACKLOG_NOTE` (`NO_FIX`).
   - **Midline non-negotiables:** never downgrade reachable data/message loss, upgrade data/settings wipe, crash/hang, wrong-recipient/privacy leak, unconfirmed billing/delete, broken core flow, weakened `tests/**`, or unreviewed `.github/**` edits.
4. **Emit evidence-backed verdict:** list concrete checks, scenarios, and surfaces actually audited (`"no issues found"` alone is invalid):
   - `BLOCKING` (`P0`), required `UNKNOWN`, or failing host gate -> `STOP`;
   - `IMPORTANT` (`P1`) -> `STOP` unless responsible owner explicitly defers;
   - `MINOR` (`P2`) only (or 2 consecutive review rounds surfacing only `MINOR`/`BACKLOG_NOTE`) -> `PASS_WITH_FOLLOWUPS`;
   - All required claims verified with zero open findings -> `PASS`.

## Boundaries

- Strictly read-only: findings never authorize unapproved writes, implementer self-downgrades, or auto-fix commits.
- Never transfer `PASS` across unverified commits or promote AI screenshots into human UI acceptance.
