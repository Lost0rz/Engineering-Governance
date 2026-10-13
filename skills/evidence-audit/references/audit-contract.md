# Audit contract

## 1. Evidence before verdict

Every material finding names the evidence that supports it: requirement/authority, path/symbol/diff, test result, CI run/job, PR/host gate, release/provenance record, artifact hash or runtime observation.

Do not substitute confidence, prior summaries or a matching name for the underlying evidence when it is available.

## 2. Common identity envelope

Before verdict establish:

```text
AUDIT_PROFILE
TARGET
EXPECTED_AUTHORITY_OR_REQUIREMENT
BASE_HEAD_RANGE_OR_ARTIFACT_ID
DELIVERY_SEMANTIC_IDENTITY (when relevant)
LITERAL_HOST_IDENTITY (when host gates matter)
EVIDENCE_FRESHNESS
KNOWN_EQUIVALENCE_OR_PROVENANCE
```

Evidence proves the identity it actually observed.

## 3. Audit profiles

### CODE_DIFF

Purpose: determine whether a bounded source change satisfies accepted requirements and preserves canonical authority/interfaces.

Inspect changed paths/diff, relevant surrounding authority, tests/checks and regression boundary. Separate:

- defect introduced/exposed by the diff;
- pre-existing issue material to acceptance;
- unrelated observation.

Do not inflate a change audit into repository-wide health review without need.

### PR_MERGE

Purpose: decide whether the requested merge boundary is safe.

Evaluate both:

1. semantic implementation evidence for the audited Delivery / Semantic identity;
2. **current live repository-host gates** for the literal PR/base/head identity the host governs.

Required reviews/checks/conflicts/mergeability/merge queue/current-base/latest-head are host facts. Semantic tree equivalence does not make a live host gate pass.

### CI

Purpose: determine what a workflow/run/job actually establishes.

Verify expected repository/ref/head or merge ref, workflow/job identity, trigger/context, actual conclusion, relevant step coverage and artifact/result identity. `no status reported` is not `PASS`.

A green job proves only the checks it actually ran on the identity it actually checked.

### RELEASE_PROVENANCE

Purpose: verify published/package identity against explicit expectations.

Check source commit/tag, producer/workflow, artifact identity/hash, package contents/version and provenance chain as material. Provenance metadata never compared with expected values is not acceptance evidence.

### POST_CHANGE

Purpose: verify a merged/delivered/installed/runtime identity after the change.

Name the observed merge commit/tree, package/build/install/deploy/runtime identity and the proposition being verified. Do not infer installed/runtime behavior solely from source success without provenance/equivalence.

## 4. Semantic evidence vs host gates

Semantic test/CI/review/audit evidence may remain valid across proven `CONTROL_ONLY_DRIFT` when semantic-tree equivalence and task conditions permit reuse.

Live repository-host gates are separate. Re-read them at the boundary whose decision they govern.

## 5. Findings

- `BLOCKING` — unsafe/incorrect to accept or proceed.
- `IMPORTANT` — material defect expected to be corrected before the requested boundary.
- `MINOR` — non-blocking improvement/follow-up.
- `UNKNOWN` — evidence unavailable/insufficient for a material claim.

A required `UNKNOWN` produces `STOP`, not optimistic PASS.

## 6. Verdict

- `PASS` — required evidence for this audit boundary is satisfied.
- `PASS_WITH_FOLLOWUPS` — acceptance may proceed; only non-blocking items remain.
- `STOP` — blocking defect, required unknown, identity mismatch or applicable host gate prevents safe acceptance.

The verdict must state what boundary it covers. A `CODE_DIFF PASS` is not automatically `PR_MERGE PASS`; a source audit is not installed-runtime acceptance.

## 7. Reviewer finding validation

A reviewer/agent suggestion is a claim. Before corrective mutation, verify it against actual code/requirements/evidence. If valid but out of current scope, return to Project Governance for authorization. Do not blindly implement review prose.

## 8. Read-only rule

Evidence Audit is read-only by default. It may report stale controls:

```text
CONTROL_ALIGNMENT_OBSERVATION: STALE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

It does not update controls/source merely to make the audit look clean. An authorized state-changing transition owns reconciliation/correction.
