# EngineeringGovernanceStandard

## Identity and status

| Field | Candidate value |
|---|---|
| `standard_id` | `EngineeringGovernanceStandard` |
| `standard_version` | `0.1.0-candidate.1` |
| `status` | `CANDIDATE` |
| `effective_date` | unset until independent acceptance |
| `supersedes` | none |
| `compatibility` | candidate consumers must pin the exact version and may not claim conformance |

Version format uses `MAJOR.MINOR.PATCH` plus a prerelease label. A candidate
version is unstable. After acceptance, a major increment may change authority
semantics, required evidence meaning, profile precedence, or decision states;
a minor increment may add backward-compatible optional fields or checks; a
patch increment may clarify wording without changing obligations. If a
purported patch changes meaning, it is a minor or major change instead.

## Core invariants

1. A governance record MUST point to the canonical owner of the fact it
   describes. A projection, check result, finding, or profile MUST NOT silently
   become that fact's authority.
2. Every evaluation MUST identify the target, standard/profile version,
   applicable check version, evidence, evaluator/reviewer mode, and time.
3. Unknown, unavailable, stale, not applicable, and failed are distinct
   outcomes. Missing evidence MUST NOT be treated as pass.
4. AI output is an input to review, never canonical project authority or a
   final human acceptance.
5. Evaluation and enforcement MUST be separately identified. v0.1 is
   advisory; any gate requires an explicitly named human/project gate owner.
6. A waiver changes the disposition of one bounded governance obligation; it
   does not rewrite the underlying fact or make false evidence true.
7. Observed current state (`AS_IS`) and proposed future state (`TO_BE`) MUST
   be labeled separately.

## Normative terms

- **MUST / MUST NOT:** required / prohibited for a profile claiming
  conformance to an accepted version.
- **SHOULD / SHOULD NOT:** expected unless the project records a reasoned,
  scoped deviation.
- **MAY:** permitted option.

These terms describe the candidate contract and do not claim any repository
currently conforms.

## Conformance and decision boundary

An evaluation may produce `PASS`, `FAIL`, `UNVERIFIED`, `NOT_APPLICABLE`, or
`STALE`. A `FAIL` may create a finding. Only the project's authorized
decision-maker or an explicitly configured gate decides whether a finding
blocks a project action. The evaluator MUST NOT repair source state. A status
check or CI gate is an external decision consumer, not an implicit property
of a check.

Candidate state is `WAITING_FOR_INDEPENDENT_WEB_AUDIT`. Only that audit can
accept, require correction, request more evidence, or declare the task
blocked. Executor completion does not imply acceptance.
