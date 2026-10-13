---
name: evidence-audit
description: Use when an independent or explicit implementation, code, PR, CI, release, or merge-readiness audit is requested, or when governed work needs an evidence-based acceptance verdict separate from implementation.
---

# Evidence Audit

Use this Skill for independent evidence evaluation. It may be called from Project Governance before integration/acceptance or directly for a bounded read-only audit.

Read [Audit contract](references/audit-contract.md).

## Audit profiles

- `CODE_DIFF` — requirement vs changed paths/source behavior.
- `PR_MERGE` — semantic evidence + live PR host gates + readiness.
- `CI` — workflow/run/job/source identity and actual coverage/result.
- `RELEASE_PROVENANCE` — source/tag/artifact/builder/hash/provenance expectations.
- `POST_CHANGE` — merged/delivered/runtime identity vs named claim.

## Identity before verdict

Before findings, bind repository/artifact/runtime target, base/head/range or immutable identity, requirement/task/design authority, evidence freshness and literal host identity where live host gates matter.

Do not transfer PASS from one identity to another unless accepted equivalence/provenance proves that reuse is valid.

## Findings and verdict

Findings: `BLOCKING`, `IMPORTANT`, `MINOR`, `UNKNOWN`.

Verdict: `PASS`, `PASS_WITH_FOLLOWUPS`, `STOP`.

`UNKNOWN` is first-class evidence state, not silent PASS/FAIL. Reviewer suggestions are evidence to verify, not automatic mutation instructions. Corrective work returns to Project Governance authorization.
