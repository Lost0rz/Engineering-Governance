---
name: evidence-audit
description: Perform a requested formal evidence, code, PR, CI, release or post-change review using current source and host facts. Routine status checks need no formal audit.
---

# Evidence Audit

Use for an explicitly requested audit/readiness verdict. Establish what is being claimed, which code/PR/CI identity it covers, and what evidence must exist. Inspect only the affected implementation, contracts and host gates, then report actual findings.

| Audit purpose | Evidence focus |
| --- | --- |
| Code change | Target behavior, source diff, regressions and affected tests |
| PR integration | Current head/base, CI, mergeability and material risks |
| CI | Workflow event, actual jobs, skipped checks and result |
| Release/installed state | Artifact source/provenance and observed runtime |
| Issue/plan quality | Clear goal, grounded assumptions, actionable acceptance and remaining choices |

Issues do not need a special author, form, approval comment or revision digest to be useful for audit and implementation. Audit evidence does not grant write permission. Findings inside an already authorized corrective task can be fixed there without creating a new independent approval.

Distinguish `PASS`, `PASS_WITH_FOLLOWUPS` and `STOP` according to actual required evidence. Report uncertainty honestly; do not call an implementation self-check independent acceptance. See [audit contract](references/audit-contract.md) when a formal verdict needs detail.
