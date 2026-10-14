---
name: evidence-audit
description: Use when an independent or explicit implementation, code, PR, CI, release, or merge-readiness audit is requested, or when governed work needs an evidence-based acceptance verdict separate from implementation.
---

# Evidence Audit

Use this Skill for evidence evaluation at a distinct audit/acceptance boundary. It may be called from Project Governance under an authorized AUDIT/VERIFY purpose or directly for a bounded read-only audit request.

Invoking this Skill does **not** automatically make an implementer's self-check independent. When formal independence matters, the task/acceptance boundary declares the required independence basis.

Read [Audit contract](references/audit-contract.md).

## Audit profiles

- `CODE_DIFF` — requirement vs changed paths/source behavior.
- `PR_MERGE` — semantic evidence + live PR host gates + readiness.
- `CI` — workflow/run/job/source identity and actual coverage/result.
- `RELEASE_PROVENANCE` — source/tag/artifact/builder/hash/provenance expectations.
- `POST_CHANGE` — merged/delivered/runtime identity vs named claim.

## Independence basis

When independence is material, report one of:

- `SELF_CHECK` — implementation verification; not independent acceptance.
- `FRESH_CONTEXT` — a fresh context without relying on implementation reasoning history.
- `SEPARATE_AGENT` — a separate reviewer/auditor agent.
- `HUMAN` — human independent review/acceptance.

The required level follows the task/risk/user requirement; stronger independence is not mandatory for every small check.

## Identity and required claims before verdict

Before findings, bind repository/artifact/runtime target, task/audit purpose, base/head/range or immutable identity, requirement/design authority, evidence freshness, literal host identity where live gates matter, and the claims this audit must actually establish.

Track:

```text
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

Do not transfer PASS from one identity to another unless accepted equivalence/provenance proves that reuse is valid. A required claim without adequate evidence remains `UNKNOWN`.

## Findings, disposition, and verdict

Findings: `BLOCKING`, `IMPORTANT`, `MINOR`, `UNKNOWN`.

Severity and boundary disposition are different:

- `BLOCKING` -> `STOP`.
- `IMPORTANT` -> `STOP` when correction is required before the requested boundary; it may become an explicit follow-up only when the responsible authority accepts/defer it outside that boundary.
- `MINOR` -> may remain under `PASS_WITH_FOLLOWUPS`.
- required `UNKNOWN` -> `STOP`.

Verdict: `PASS`, `PASS_WITH_FOLLOWUPS`, `STOP`.

`UNKNOWN` is first-class evidence state, not silent PASS/FAIL. Reviewer suggestions are evidence to verify, not automatic mutation instructions. Corrective work returns to Project Governance authorization, often as a distinct CORRECTIVE task when the engineering purpose changes.
