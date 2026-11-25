---
name: evidence-audit
description: >-
  Formal read-only evidence, code-diff, PR-merge, CI, or release provenance
  verdicts bound to exact commits, host gates, and audit independence. Do not
  use for quick advisory status checks, active code fixes
  (engineering-workflow), or as a substitute for human UI acceptance.
---

# Evidence Audit

Issue formal `PASS`, `PASS_WITH_FOLLOWUPS`, or `STOP` verdicts strictly from directly observed evidence.

## Fast route

| Audit scope | Mode | Next reading |
| --- | --- | --- |
| Bounded `CODE_DIFF` or `PR_MERGE` readiness verdict | `DIFF_OR_PR_AUDIT` | **NONE (this file)** |
| `CI`, `RELEASE_PROVENANCE`, `POST_CHANGE`, or multi-claim audit | `DEEP_PROVENANCE_OR_CI_AUDIT` | [audit-contract.md](references/audit-contract.md) |

## Inline diff & PR audit workflow

1. **Bind identity & independence:** state exact repo, base/head SHA or PR number, live host check state, and `AUDIT_INDEPENDENCE` (`SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN`). Never present an implementation self-check as independent acceptance.
2. **Verify required claims:** inspect actual diff, regressions, executed tests (watch for weakened assertions in `tests/**` or unreviewed `.github/**` edits), and live CI/review gates separately. Keep `G0`–`G3` risk separate from `V0`–`V3` test depth.
3. **Emit verdict:**
   - `BLOCKING` finding, required `UNKNOWN`, or failing host gate -> `STOP`;
   - `IMPORTANT` finding -> `STOP` unless responsible owner explicitly defers it;
   - `MINOR` only -> `PASS_WITH_FOLLOWUPS`;
   - All required claims verified -> `PASS`.

## Boundaries

- Strictly read-only: findings do not authorize code mutations or auto-fix commits.
- Never transfer `PASS` across unverified commits or promote AI screenshots into human UI acceptance.
