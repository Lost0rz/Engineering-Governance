# Handoff Card & Receipt contract

## Authority

A Card is transport, not a second task contract. Reference current authority and carry only fresh transfer-specific delta. The receiver rereads accessible authorities; material conflict returns to Project Governance.

## Common Card envelope

```text
CARD_ID
TASK_ID
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
TARGET
AUTHORITY
OBSERVED_BASIS: <when freshness matters>
SOURCE_CONTEXT / TARGET_CONTEXT: <when useful>
DELTA
BOUNDARY
STOP
RETURN_CONTRACT
```

Do not duplicate full objective/scope/acceptance/STOP/workspace policy already owned by `CURRENT_TASK.md`. A Card cannot expand authorization.

## Mode profiles

### EXECUTE
Focus the Card on mutation target, fresh delta, allowed mutation boundary, STOP conditions and return evidence. Use `PURPOSE: DIAGNOSTIC_PROBE` or `PURPOSE: TEST_IMPLEMENTATION` when those state changes are specifically authorized.

### AUDIT / REVIEW
Read-only. Add the target/range/observed identity and, when material, required claims or independence expectation. Findings do not authorize fixes.

### VERIFY
Read-only confirmation of a named proposition/check. A normal test-run card is:

```text
MODE: VERIFY
PROFILE: TEST_RUN
CLAIM
EXPECTED_EVIDENCE
```

If the job changes test/source/config, it is EXECUTE instead.

### DIAGNOSE
Read-only diagnostic question/evidence/hypothesis transfer. State-changing probes use EXECUTE.

## Runtime/configuration isolation

Runtime/model/tool/capacity values belong to the receiving environment unless an accepted portable project artifact owns them. Sender observations never become receiver defaults merely through the Card.

## Standard receipts

### EXECUTE receipt

```text
CARD_ID / TASK_ID
OUTCOME
START_IDENTITY
FINAL_IDENTITY
CHANGED_PATHS
VERIFICATION
LIFECYCLE
UNRESOLVED
CONTROL_ALIGNMENT
NEXT_SAFE_ACTION
```

### AUDIT / REVIEW receipt

```text
CARD_ID / TASK_ID
OUTCOME
OBSERVED_IDENTITY / RANGE
EVIDENCE / FINDINGS
UNKNOWN
VERDICT
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION
```

### VERIFY receipt

```text
CARD_ID / TASK_ID
CLAIM
OBSERVED_IDENTITY
RESULT: PASS | FAIL | UNKNOWN
EVIDENCE
PROVES
DOES_NOT_PROVE
NEXT_SAFE_ACTION
```

Keep receipts decision-oriented. Explicitly report legitimate no-change/no-output success. Human-facing conversational status receipts are a Project Governance concern and are not substitutes for cross-context receipts.
