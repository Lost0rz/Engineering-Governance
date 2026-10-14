# Handoff Card & Receipt contract

## Authority

A Card is transport, not a second task contract. Reference current authority and carry only fresh transfer-specific delta. The receiver rereads accessible authorities; material conflict returns to Project Governance.

If the requested output itself will be sent to another agent, session, machine, reviewer, or execution context as engineering instructions/evidence, the transfer artifact uses this Handoff contract. A free-form “execution card” is not an alternate schema.

## Capability vs Mode

These are orthogonal:

```text
CAPABILITY = bounded Skill/capability requested of the receiver, or NONE
MODE       = receiver action / side-effect class
```

`MODE: AUDIT` or `MODE: VERIFY` does not by itself invoke `evidence-audit`. When a formal Evidence Audit verdict is intended across contexts, state both, for example:

```text
CAPABILITY: evidence-audit
MODE: AUDIT
```

Valid `MODE` values are exactly:

```text
EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
```

Task-purpose labels such as `CORRECTIVE`, `FEATURE`, `RELEASE`, or `HOTFIX` belong in `PURPOSE` or `DELTA`, not `MODE`.

## Common Card schema

### Required core

```text
CARD_ID
TASK_ID
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
CAPABILITY: <Engineering Governance skill | NONE>
TARGET
AUTHORITY
DELTA: <fresh transfer-specific delta | NONE>
BOUNDARY
RETURN_CONTRACT
```

### Conditional

Use only when decision-relevant:

```text
PURPOSE
PROFILE
OBSERVED_BASIS
SOURCE_CONTEXT / TARGET_CONTEXT
STOP
CLAIM
EXPECTED_EVIDENCE
AUDIT_INDEPENDENCE
```

Do not omit required core fields. Do not duplicate the full objective/scope/acceptance/STOP/workspace policy already owned by `CURRENT_TASK.md`. A Card cannot expand authorization.

## Card generation rules

Before returning a generated Card, check and correct all of the following in the same pass:

1. **Route** — the output has actually been shaped as an Agent Handoff Card when it crosses contexts.
2. **Core schema** — all nine required core fields are present.
3. **Mode** — `MODE` is one accepted side-effect class, not a task-purpose adjective.
4. **Task identity** — preserve the current `TASK_ID` for the same engineering purpose. Context changes alone do not create tasks.
5. **Authority compression** — `AUTHORITY` points to the current task/rules/design sources; do not re-copy the entire task contract.
6. **Fresh delta** — `DELTA` contains only transfer-specific facts/instructions that are not recoverable by rereading those authorities.
7. **Boundary** — the Card cannot grant writes, scope, side effects, or repository authority beyond the owning task.
8. **Identity semantics** — sender-observed commits/refs belong in `OBSERVED_BASIS` by default. Promote an identity to `EXPECTED_HEAD`, `REQUIRED_HEAD`, `MUST_EQUAL`, or an equivalent lock only when an owning authority explicitly defines that lock and the Card is merely referencing it.
9. **Outcome-neutral return** — `RETURN_CONTRACT` requests actual evidence/outcome. Do not predeclare `FINAL_STATE: READY`, `PASS`, merge/release completion, or another success that the receiver has not observed.

A Card that knowingly fails one of these checks is not returned with a warning; revise it until compliant or return to Project Governance when the owning authority itself is ambiguous/conflicting.

## Mode profiles

### EXECUTE

Focus on mutation target, fresh delta, allowed mutation boundary, transfer-specific STOP and return evidence. Use `PURPOSE: DIAGNOSTIC_PROBE` or `PURPOSE: TEST_IMPLEMENTATION` when those state changes are specifically authorized.

### AUDIT / REVIEW

Read-only. Add target/range/observed identity and, when material, required claims or independence expectation. Findings do not authorize fixes.

### VERIFY

Read-only confirmation of a named proposition/check. A normal test-run card is:

```text
MODE: VERIFY
CAPABILITY: NONE
PROFILE: TEST_RUN
CLAIM
EXPECTED_EVIDENCE
```

If the job changes test/source/config, it is EXECUTE instead.

### DIAGNOSE

Read-only diagnostic question/evidence/hypothesis transfer. State-changing probes use EXECUTE.

## Runtime/configuration isolation

Runtime/model/tool/capacity values belong to the receiving environment unless an accepted portable project artifact owns them. Sender observations never become receiver defaults merely through the Card.

## Standard receipt core

Every structured handoff receipt starts with:

```text
CARD_ID
TASK_ID
MODE
CAPABILITY
TARGET
OUTCOME
```

`OUTCOME` is always observed, not predetermined. The receiver may return success, failure, stop, blocked, unknown, no-change, or another mode-appropriate result supported by evidence.

Then add only mode-relevant evidence.

### EXECUTE

```text
START_IDENTITY
FINAL_IDENTITY
CHANGED_PATHS
VERIFICATION
LIFECYCLE
UNRESOLVED
CONTROL_ALIGNMENT
NEXT_SAFE_ACTION
```

### AUDIT / REVIEW

```text
OBSERVED_IDENTITY / RANGE
EVIDENCE / FINDINGS
UNKNOWN
VERDICT
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION
```

### VERIFY

```text
CLAIM
OBSERVED_IDENTITY
RESULT: PASS | FAIL | UNKNOWN
EVIDENCE
PROVES
DOES_NOT_PROVE
NEXT_SAFE_ACTION
```

Keep receipts decision-oriented and explicitly report legitimate no-change/no-output success. Human-facing conversational status receipts are a Project Governance concern and do not replace cross-context receipts.
