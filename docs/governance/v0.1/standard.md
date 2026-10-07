# EngineeringGovernanceStandard

## Identity and status

| Field | Accepted value |
|---|---|
| `standard_id` | `EngineeringGovernanceStandard` |
| `standard_version` | `0.1.0` |
| `status` | `ACCEPTED — STABLE` |
| `effective_date` | `2026-10-07` |
| `supersedes` | none |
| `compatibility` | projects adopting v0.1 MUST pin `0.1.0`; later changes follow the versioning rules below |

Version format uses `MAJOR.MINOR.PATCH` plus an optional prerelease label.
A major increment may change authority routing, required evidence meaning,
profile semantics, or decision states; a minor increment may add
backward-compatible optional fields or checks; a patch increment may clarify
wording without changing obligations. If a purported patch changes meaning,
it is a minor or major change instead.

## Core invariants

1. A governance record MUST point to the canonical owner of the fact it
   describes. A projection, check result, finding, or profile MUST NOT silently
   become that fact's authority.
2. Every evaluation MUST identify the target, standard/profile version,
   applicable check version, evidence, evaluator/reviewer mode, and time.
3. An evaluation result, evidence freshness, exception state, and project
   decision disposition MUST be recorded separately. Missing evidence MUST
   NOT be treated as pass.
4. AI-derived analysis MUST cite underlying source evidence and MUST remain
   derived/advisory. It MUST NOT independently satisfy a factual PASS/FAIL
   evidence requirement unless the check explicitly evaluates the AI artifact
   itself. AI output is never canonical project authority or final acceptance
   of its own earlier output.
5. Evaluation and enforcement MUST be separately identified. v0.1 is
   advisory; any gate requires an explicitly named human/project gate owner.
6. An exception or project decision may affect the current disposition of one
   bounded governance obligation; neither rewrites an underlying fact or
   historical evaluation result, nor makes false evidence true.
7. Observed current state (`AS_IS`) and proposed future state (`TO_BE`) MUST
   be labeled separately.

## Normative terms

- **MUST / MUST NOT:** required / prohibited for a profile claiming
  conformance to this accepted version.
- **SHOULD / SHOULD NOT:** expected unless the project records a reasoned,
  scoped deviation.
- **MAY:** permitted option.

Adopting the standard does not by itself prove project conformance.

## Conformance and decision boundary

An evaluation records `result`: `PASS`, `FAIL`, `UNVERIFIED`, or
`NOT_APPLICABLE`. A separate, time-scoped freshness assessment records
`CURRENT`, `STALE`, or `UNKNOWN` for its evidence and dependencies. The
historical result MUST NOT be rewritten when freshness changes. A stale or
unknown assessment cannot support a current PASS claim; it requires a new
evaluation before a current conformance decision.

Exception state and project decision disposition are separate records from
both result and freshness. Expiry or revocation changes the exception's
current state, not the historical result. A `FAIL` may create a finding. Only
the project's authorized decision-maker or an explicitly configured gate
decides the finding's current disposition and whether it blocks a project
action. The evaluator MUST NOT repair source state. A status check or CI gate
is an external decision consumer, not an implicit property of a check.

## Acceptance provenance

Independent Web re-review of corrective head
`a44939856d78cc50e55eac0d812b5b6b7a8645a5` found no unresolved BLOCKER or
MAJOR finding. Acceptance-control head
`96a3e2212bfa2ffcfcd31a64557f86380fa8d642` was merged by PR #1 in merge
commit `8e734bcf55805e54b40ff203d73fca97d9fa29fd` after explicit user
authorization. This post-merge closeout on `main` freezes the accepted stable
version as `0.1.0`.
