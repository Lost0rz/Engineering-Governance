---
name: evidence-audit
description: Use when an independent or explicit implementation, code, PR, CI, release, or merge-readiness audit is requested, or when governed work needs an evidence-based acceptance verdict separate from implementation.
---

# Evidence Audit

Use this Skill for independent evidence evaluation. It may be called from Project Governance before integration/acceptance or directly for a bounded read-only audit.

Read [Audit contract](references/audit-contract.md).

## First bind the claim to an identity

Before findings, establish what is actually being audited:

- repository and target ref/PR/release;
- base/head or evidence range;
- Delivery / Semantic HEAD when relevant;
- literal repository-host identity for live required checks/reviews/mergeability;
- requirements/task/design authority being evaluated;
- freshness of CI/test/review evidence.

Do not say `PASS` for one identity because evidence passed on another unless the accepted equivalence rule explicitly permits reuse.

## Audit dimensions

Apply only dimensions relevant to the requested verdict:

1. **Requirement coverage** — does the work satisfy the authorized objective/acceptance contract?
2. **Diff/source correctness** — do changed paths preserve canonical authority, ownership, interfaces, and expected behavior?
3. **Verification evidence** — do the tests/checks actually prove the claimed behavior for the audited identity?
4. **CI/host evidence** — required checks/reviews/conflicts/mergeability/current-base/latest-head conditions are live repository-host facts and must be read for the identity the host governs.
5. **Lifecycle/control observation** — note stale or contradictory controls, but strict read-only audit must not mutate them.
6. **Unknowns** — distinguish `UNKNOWN`/`UNVERIFIED` from `FAIL`.

## Findings and verdict

Classify findings as:

- `BLOCKING` — unsafe/incorrect to accept or proceed;
- `IMPORTANT` — material defect that should be corrected before the requested acceptance boundary;
- `MINOR` — non-blocking improvement/follow-up;
- `UNKNOWN` — evidence unavailable or insufficient for a material claim.

Verdict:

- `PASS` — required evidence for the requested boundary is satisfied;
- `PASS_WITH_FOLLOWUPS` — acceptance can proceed; only non-blocking items remain;
- `STOP` — blocking defect, required unknown, identity mismatch, or host gate prevents safe acceptance.

A reviewer suggestion is evidence to verify, not an automatic instruction to mutate code. Corrective work returns to Project Governance/task authorization.
