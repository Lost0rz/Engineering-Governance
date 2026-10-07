# Governance Model v0.1 Candidate

**Status:** `CANDIDATE — INDEPENDENT_WEB_AUDIT_PASSED / READY_FOR_MERGE`.
The candidate has passed independent Web review at corrective head
`a44939856d78cc50e55eac0d812b5b6b7a8645a5`, but is not yet the frozen stable
standard until PR #1 is merged and acceptance closeout is recorded on `main`.
It does not assert any project's conformance.

## Documents

- [Standard contract](standard.md)
- [Project profile](project-profile.md)
- [Authority model](authority-model.md)
- [Lifecycle layers and cross-cutting axes](lifecycle.md)
- [Checks, evidence, findings, and decisions](checks-evidence-findings.md)
- [Exceptions, freshness, and versioning](exceptions-freshness-versioning.md)
- [Reference synthesis and open questions](../../reference-audit/synthesis.md)
- [InvestDesk read-only reality check](../../reality-checks/investdesk.md)
- [Adversarial review](adversarial-review.md)

## Candidate identity

- Standard: `EngineeringGovernanceStandard`
- `standard_version`: `0.1.0-candidate.1`
- Compatibility status: candidate accepted for merge; do not claim stable
  conformance until merge/freeze closeout establishes the accepted version.
- Scope: governance records and evaluation contracts. This candidate does
  not implement an evaluator or enforcement adapter.

## How to read this candidate

MUST/SHOULD/MAY define candidate normative strength only until stable
acceptance is recorded on `main`. A project adopts a version by recording it in
its own profile; that declaration is not conformance evidence. All fields and
lifecycles below are conceptual contracts until a later task authorizes schemas
or executable tooling.
