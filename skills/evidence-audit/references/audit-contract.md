# Audit contract

## 1. Advisory inspection vs formal verdict

Keep two read-only purposes distinct:

- **ADVISORY_READ_ONLY_INSPECTION** — report current evidence/status without a formal acceptance/readiness claim. It may remain under Project Governance and does not require a new AUDIT task solely because evidence is viewed.
- **FORMAL_ACCEPTANCE_OR_READINESS** — return an Evidence Audit verdict for an explicit boundary. If the active task already authorizes that acceptance, use it; if this is a materially distinct engineering purpose, Project Governance authorizes the corresponding AUDIT/VERIFY task purpose.

Neither purpose grants corrective mutation.

## 2. Audit purpose and independence

Implementation self-check remains useful verification but is not automatically independent acceptance. When independence is material, declare:

```text
AUDIT_INDEPENDENCE: SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN
```

The required level follows user/task/risk requirements; do not force expensive independence for every local check.

## 3. Evidence before verdict

Every material finding names supporting evidence: requirement/authority, path/symbol/diff, test result, CI run/job, PR/host gate, release/provenance record, artifact hash or runtime observation.

Do not substitute confidence, prior summaries or matching names for underlying evidence when available.

## 4. Common identity and coverage envelope

Before a formal verdict establish as applicable:

```text
TASK_ID
AUDIT_PROFILE
AUDIT_INDEPENDENCE
TARGET
EXPECTED_AUTHORITY_OR_REQUIREMENT
BASE_HEAD_RANGE_OR_ARTIFACT_ID
DELIVERY_SEMANTIC_IDENTITY
LITERAL_HOST_IDENTITY
EVIDENCE_FRESHNESS
KNOWN_EQUIVALENCE_OR_PROVENANCE
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

Evidence proves the identity/claim it actually observed. A required claim with insufficient evidence remains `UNKNOWN`.

## 5. Audit profiles

### CODE_DIFF
Determine whether a bounded source change satisfies accepted requirements and preserves canonical authority/interfaces. Inspect diff, relevant surrounding authority, tests/checks and regression boundary. Do not inflate into repository-wide health review without need.

### PR_MERGE
Evaluate both semantic implementation evidence for the audited Delivery/Semantic identity and **current live repository-host gates** for the literal PR/base/head identity.

### CI
Verify expected repository/ref/head or merge ref, workflow/job identity, trigger/context, actual conclusion, relevant step coverage and artifact/result identity. `no status reported` is not `PASS`.

### RELEASE_PROVENANCE
Check source commit/tag, producer/workflow, artifact identity/hash, package contents/version and provenance chain as material.

### POST_CHANGE
Name the observed merge commit/tree, package/build/install/deploy/runtime identity and proposition being verified. Do not infer installed/runtime behavior solely from source success without provenance/equivalence.

## 6. Semantic evidence vs host gates

Semantic test/CI/review/audit evidence may remain valid across proven `CONTROL_ONLY_DRIFT` when semantic-tree equivalence/task conditions permit reuse. Live repository-host gates are separate and are reread at the boundary they govern.

## 7. Findings and boundary disposition

- `BLOCKING` -> `STOP`.
- `IMPORTANT` -> `STOP` when correction is required before the boundary; otherwise follow-up only when responsible authority explicitly accepts/defers it.
- `MINOR` -> may coexist with `PASS_WITH_FOLLOWUPS`.
- required `UNKNOWN` -> `STOP`.

## 8. Verdict

- `PASS` — all required claims supported and no blocking/required-before-boundary issue remains.
- `PASS_WITH_FOLLOWUPS` — required claims supported and only explicitly non-blocking/deferred items remain.
- `STOP` — blocking defect, required-before-boundary issue, required unknown, identity mismatch or applicable host gate blocks acceptance.

State the exact boundary. `CODE_DIFF PASS` does not imply `PR_MERGE PASS`; source audit does not imply installed-runtime acceptance.

## 9. Reviewer finding validation

A reviewer/agent suggestion is a claim. Verify it before corrective mutation. If valid but outside current task purpose, return to Project Governance for reconciliation/corrective authorization.

## 10. Read-only rule

Evidence Audit may report stale controls:

```text
CONTROL_ALIGNMENT_OBSERVATION: STALE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

It does not update controls/source merely to make an audit clean.
