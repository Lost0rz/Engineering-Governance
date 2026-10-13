# Audit contract

## Evidence before verdict

Every material finding should name the evidence that supports it: path/symbol/diff, test result, CI run/job, PR/host gate, release/provenance record, or authoritative requirement. Do not substitute confidence or agent summaries for the underlying evidence when it is available.

## Diff-bounded vs repository-wide findings

When asked to audit a PR/change, distinguish:

- defects introduced/exposed by the audited diff;
- pre-existing repository problems relevant to acceptance;
- unrelated observations.

Do not inflate a change audit into an unbounded repository health review unless requested or required for the decision.

## Semantic evidence vs host gates

Semantic verification evidence can remain valid across a proven `CONTROL_ONLY_DRIFT` when semantic-tree equivalence and task conditions permit reuse.

Repository-host gates are different: required checks, review state, conflicts, mergeability, merge queue, latest-head/current-base rules, and similar conditions must be read from the live host for the literal identity governed by that rule.

## Provenance expectation

For release/artifact/CI identity claims, verify observed provenance against expected repository/ref/commit/producer or other declared expectation. Provenance that is never compared to expectations is only metadata, not acceptance evidence.

## Read-only rule

A read-only audit may report:

```text
CONTROL_ALIGNMENT_OBSERVATION: STALE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

It must not update controls merely to make the audit look clean. A later authorized state-changing transition owns reconciliation.
