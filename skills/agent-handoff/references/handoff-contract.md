# Handoff contract

## 1. Task, authority, context, and freshness

A handoff moves responsibility between execution contexts. It does not define engineering purpose and does not create task authority.

For same-purpose continuation, preserve the same `TASK_ID`. `AUTHORITY` identifies where current truth/authorization lives; the receiver rereads the named authorities it can access.

When freshness/drift matters, record `AUTHORITY_OBSERVED_BASIS` such as a control revision, task observation, PR/head identity, or equivalent bounded basis. The receiver compares current authority with that basis:

- `CURRENT_COMPATIBLE` — current authority is the same or newer without invalidating the handoff action boundary; continue.
- `CURRENT_CONFLICT` — current authority materially changes objective/scope/side effects/writer boundary/acceptance/stop conditions; stop and return to Project Governance.
- `AUTHORITY_UNAVAILABLE` — required authority cannot be accessed and a bounded snapshot is insufficient; stop rather than infer.

`DELTA` contains only recent action-specific information not safely represented in those authorities, such as:

- fresh repository/PR/CI/runtime state;
- a newer user/project decision requiring reconciliation;
- bounded focus for this pass;
- current cross-repository dependency fact;
- transfer-specific STOP/output condition.

Do not put durable engineering principles, full control-file text, stale chat history, speculative facts, unrelated secrets/credentials, or unnecessary personal data into DELTA.

## 2. Common request envelope

```text
HANDOFF_ID
TASK_ID
MODE: EXECUTE | AUDIT | DIAGNOSE | REVIEW | VERIFY
TARGET
AUTHORITY
AUTHORITY_OBSERVED_BASIS: <when material>
SOURCE_CONTEXT: <optional context label>
TARGET_CONTEXT: <optional context label>
DELTA
BOUNDARY
RETURN_CONTRACT
```

Source/target context may be Web, local Codex, cloud agent, Sub Agent, reviewer context, machine/session, or project-equivalent. These labels are operational context only.

A request should be short enough to reveal the immediate action without archaeology and complete enough to identify what to do, where authority lives, what changed, what may be mutated, when to STOP and what evidence must return.

## 3. Same task vs distinct task

Use the same `TASK_ID` when the engineering objective/authorization is unchanged across context transfer, including:

- Web/session -> local/session implementation continuation;
- controller -> Sub Agent delegated unit;
- one machine/session -> another after interruption/compaction;
- implementation-local verification supporting the same task.

Do not manufacture a new task merely because a different agent/machine/session acts.

If the receiver is being asked to perform a materially different engineering purpose, such as a separately commissioned independent acceptance audit or distinct corrective objective, Project Governance establishes/reconciles that task purpose first. Agent Handoff transports it; Agent Handoff does not invent it.

## 4. Mode profiles

### EXECUTE

Use for authorized mutation in another execution context.

Request adds only transfer-specific detail such as selected workspace/identity when material, immediate mutation focus and unique side-effect/STOP boundary. It must not re-authorize work absent from `CURRENT_TASK.md`.

Return at minimum:

- `TASK_ID` and handoff identity;
- start/final execution identity;
- changed paths or `NONE`;
- verification actually run/result;
- branch/PR/worktree lifecycle effects when material;
- unresolved evidence;
- authority compatibility/conflict observation when material;
- document/status/task reconciliation and Control Alignment for final successful state-changing handoff;
- next safe action.

### AUDIT

Strict read-only unless a separate task explicitly authorizes mutation. Use when the active engineering purpose is an audit/acceptance boundary.

Request identifies audit target/range/identity, required claims, independence expectation, and requested verdict boundary.

Return target/range/observed identity, evidence, required-claim coverage, findings by severity, unknown/unverified items, independence basis, CI/test/host evidence where relevant, verdict and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`.

### DIAGNOSE

Use as transport for an already authorized diagnostic route. The request identifies the blocked question, current evidence/hypothesis state, allowed observation/probe boundary and mutation restrictions.

Return observations, hypothesis support/falsification, root-cause confidence only where evidence supports it, probe effects, unresolved gap and minimum evidence-supported fix boundary. Do not silently implement an out-of-scope fix.

### REVIEW

Read-only evaluation of specified work product. Give the reviewer target/range, requirements/authority references and relevant verification evidence; do not send the implementer's private reasoning history as a substitute for work-product evidence.

Return findings + evidence + severity/unknown state. A review finding is not corrective authorization.

### VERIFY

Confirm a named claim, identity or check. Request states exactly what proposition must be established and the evidence source expected.

Return the observation, identity/freshness, `PASS | FAIL | UNKNOWN`, what that result proves and what it does not prove. If success means no change/no output, say that explicitly.

## 5. Receipt profiles

### State-changing compact receipt

```text
HANDOFF_ID:
TASK_ID:
MODE: EXECUTE
SKILLS_USED:
AUTHORITY_COMPATIBILITY: CURRENT_COMPATIBLE | CURRENT_CONFLICT | UNKNOWN
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
TASK_ID:
MODE: AUDIT | REVIEW | VERIFY | DIAGNOSE(read-only)
TARGET:
OBSERVED_IDENTITY:
EVIDENCE_RANGE:
SKILLS_USED:
AUTHORITY_COMPATIBILITY: CURRENT_COMPATIBLE | CURRENT_CONFLICT | UNKNOWN
FINDINGS_OR_OBSERVATION:
UNKNOWN_OR_UNVERIFIED:
CI_TEST_HOST_EVIDENCE:
CONTROL_ALIGNMENT_OBSERVATION: MATCH | STALE | UNKNOWN | NOT_APPLICABLE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
VERDICT_OR_RESULT:
NEXT_SAFE_ACTION:
```

Fields may be omitted only when genuinely not applicable and the decision signal remains unambiguous. Absence is not evidence of `UNCHANGED`.

## 6. Context-package economy

Prefer references + bounded fresh delta. Include exact excerpts only when the receiver cannot access the source or exact wording is necessary. Avoid full chat history and repeated generic governance rules.

The handoff should be self-contained enough to act without reconstructing conversation history but small enough that authority remains in its owning source. An accepted plan/design should be referenced by identity/path rather than repeatedly paraphrased into every execution prompt.
