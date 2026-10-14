# Audit contract

## 1. Audit purpose and independence

Evidence Audit evaluates an explicit audit/acceptance boundary. When that boundary is a distinct engineering purpose, Project Governance authorizes the corresponding AUDIT/VERIFY task; the audit does not borrow implementation authority merely because it examines implementation work.

Implementation self-check remains useful verification but is not automatically independent acceptance.

When independence is material, declare:

```text
AUDIT_INDEPENDENCE: SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN
```

- `SELF_CHECK` — same implementation context; not independent acceptance.
- `FRESH_CONTEXT` — fresh context without relying on implementation reasoning history.
- `SEPARATE_AGENT` — separate reviewer/auditor agent.
- `HUMAN` — human independent review/acceptance.

The required independence level follows user/task/risk requirements; do not force expensive independence for every local check.

## 2. Evidence before verdict

Every material finding names the evidence that supports it: requirement/authority, path/symbol/diff, test result, CI run/job, PR/host gate, release/provenance record, artifact hash or runtime observation.

Do not substitute confidence, prior summaries or a matching name for the underlying evidence when it is available.

## 3. Common identity and coverage envelope

Before verdict establish:

```text
TASK_ID
AUDIT_PROFILE
AUDIT_INDEPENDENCE
TARGET
EXPECTED_AUTHORITY_OR_REQUIREMENT
BASE_HEAD_RANGE_OR_ARTIFACT_ID
DELIVERY_SEMANTIC_IDENTITY (when relevant)
LITERAL_HOST_IDENTITY (when host gates matter)
EVIDENCE_FRESHNESS
KNOWN_EQUIVALENCE_OR_PROVENANCE
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

Evidence proves the identity and claim it actually observed. A required claim with insufficient evidence remains `UNKNOWN`.

## 4. Audit profiles

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

## 5. Semantic evidence vs host gates

Semantic test/CI/review/audit evidence may remain valid across proven `CONTROL_ONLY_DRIFT` when semantic-tree equivalence and task conditions permit reuse.

Live repository-host gates are separate. Re-read them at the boundary whose decision they govern.

## 6. Findings and boundary disposition

Severity describes the issue; disposition describes what the requested acceptance boundary may do.

- `BLOCKING` — unsafe/incorrect to accept or proceed -> `STOP`.
- `IMPORTANT` — material issue. If correction is required before the requested boundary -> `STOP`. If the responsible authority explicitly accepts/defers it outside that boundary -> follow-up may remain.
- `MINOR` — non-blocking improvement/follow-up -> may coexist with `PASS_WITH_FOLLOWUPS`.
- `UNKNOWN` — evidence unavailable/insufficient for a claim. If that claim is required -> `STOP`.

Do not infer disposition from prose volume or severity name alone; state it explicitly.

## 7. Verdict

- `PASS` — all required claims for this audit boundary are adequately supported and no blocking/required-before-boundary issue remains.
- `PASS_WITH_FOLLOWUPS` — required claims are supported and only explicitly non-blocking/deferred items remain.
- `STOP` — blocking defect, required-before-boundary IMPORTANT issue, required unknown, identity mismatch or applicable host gate prevents safe acceptance.

The verdict must state what boundary it covers. A `CODE_DIFF PASS` is not automatically `PR_MERGE PASS`; a source audit is not installed-runtime acceptance.

## 8. Reviewer finding validation

A reviewer/agent suggestion is a claim. Before corrective mutation, verify it against actual code/requirements/evidence. If valid but outside the current task purpose, return to Project Governance for a CORRECTIVE/reconciled task rather than mutating under audit authority.

## 9. Read-only rule

Evidence Audit is read-only by default. It may report stale controls:

```text
CONTROL_ALIGNMENT_OBSERVATION: STALE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

It does not update controls/source merely to make the audit look clean. An authorized state-changing transition owns reconciliation/correction.
