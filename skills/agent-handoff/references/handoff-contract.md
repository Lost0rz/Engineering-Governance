# Handoff contract

## 1. Authority and freshness

The receiver must reread named authorities it can access. `AUTHORITY` identifies where truth/authorization lives; it is not copied into the card by default.

`DELTA` contains only recent action-specific information not safely represented in those authorities, such as:

- a fresh remote audit observation;
- current PR/CI/repository state needed for the next action;
- a user decision made after the controls were authored;
- bounded focus for this pass;
- current cross-repository dependency fact;
- transfer-specific STOP/output condition.

Do not put durable engineering principles, full control-file text, stale chat history or speculative facts into DELTA.

If DELTA conflicts with the authority that owns that semantic class, the card does not silently win. A newer explicit user decision may require Project Governance task reconciliation before mutation.

## 2. Common request envelope

```text
HANDOFF_ID
MODE: EXECUTE | AUDIT | DIAGNOSE | REVIEW | VERIFY
TARGET
AUTHORITY
DELTA
BOUNDARY
RETURN_CONTRACT
```

A request should be short enough to reveal the immediate action without archaeology and complete enough to identify what to do, where authority lives, what changed, what may be mutated, when to STOP and what evidence must return.

## 3. Mode profiles

### EXECUTE

Use for authorized mutation in another execution context.

Request adds only transfer-specific detail such as selected workspace/identity when material, immediate mutation focus and unique side-effect/STOP boundary. It must not re-authorize work that is absent from `CURRENT_TASK.md`.

Return at minimum:

- start/final execution identity;
- changed paths or `NONE`;
- verification actually run/result;
- branch/PR/worktree lifecycle effects when material;
- unresolved evidence;
- document/status/task reconciliation and Control Alignment for final successful state-changing handoff;
- next safe action.

### AUDIT

Strict read-only unless a separate task explicitly authorizes mutation. Request identifies audit target/range/identity and requested verdict boundary.

Return target/range/observed identity, evidence, findings by severity, unknown/unverified items, CI/test/host evidence where relevant, verdict and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`.

### DIAGNOSE

Use only as transport for an already valid diagnostic route. The request identifies the blocked question, current evidence/hypothesis state, allowed observation/probe boundary and mutation restrictions.

Return observations, hypothesis support/falsification, root-cause confidence only where evidence supports it, probe effects, unresolved gap and minimum evidence-supported fix boundary. Do not silently implement the fix unless the active task authorizes it.

### REVIEW

Read-only evaluation of specified work product. Give the reviewer target/range, requirements/authority references and relevant verification evidence; do not send the implementer's private reasoning history as a substitute for work-product evidence.

Return findings + evidence + severity/unknown state. A review finding is not corrective authorization.

### VERIFY

Confirm a named claim, identity or check. Request states exactly what proposition must be established and the evidence source expected.

Return the observation, identity/freshness, `PASS | FAIL | UNKNOWN`, what that result proves and what it does not prove. If success means no change/no output, say that explicitly.

## 4. Receipt profiles

### State-changing compact receipt

```text
HANDOFF_ID:
MODE: EXECUTE
TASK_ID:
SKILLS_USED:
OUTCOME: PASS | PARTIAL | STOP
START_IDENTITY:
FINAL_IDENTITY:
CHANGED_PATHS:
VERIFICATION:
LIFECYCLE:
UNRESOLVED: NONE | ...
RELATED_DOCUMENT:
DOCUMENT_ALIGNMENT:
CURRENT_STATUS_RECONCILIATION:
CURRENT_TASK_RECONCILIATION:
CONTROL_ALIGNMENT:
NEXT_SAFE_ACTION:
```

### Read-only compact receipt

```text
HANDOFF_ID:
MODE: AUDIT | REVIEW | VERIFY | DIAGNOSE(read-only)
TARGET:
OBSERVED_IDENTITY:
EVIDENCE_RANGE:
SKILLS_USED:
FINDINGS_OR_OBSERVATION:
UNKNOWN_OR_UNVERIFIED:
CI_TEST_HOST_EVIDENCE:
CONTROL_ALIGNMENT_OBSERVATION: MATCH | STALE | UNKNOWN | NOT_APPLICABLE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
VERDICT_OR_RESULT:
NEXT_SAFE_ACTION:
```

Fields may be omitted only when genuinely not applicable and the decision signal remains unambiguous. Absence is not evidence of `UNCHANGED`.

## 5. Context-package economy

Prefer references + bounded fresh delta. Include exact excerpts only when the receiver cannot access the source or exact wording is necessary. Avoid full chat history and repeated generic governance rules.

The handoff should be self-contained enough to act without reconstructing conversation history but small enough that authority remains in its owning source.
