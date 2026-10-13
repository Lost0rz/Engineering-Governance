# Handoff contract

## What belongs in DELTA

Good delta is recent and action-specific:

- a fresh Web/remote audit observation;
- a PR/CI/repository state just verified for the next action;
- a user decision made after the current task/control text;
- a bounded focus for this pass;
- a cross-repository dependency fact needed now;
- a transfer-specific STOP/output condition.

Do not put durable engineering principles, full control-file text, stale chat history, or speculative facts into DELTA.

## Freshness and conflict

The receiver must reread named authorities that it can access. If handoff delta conflicts materially with an authority that owns that semantic class, the handoff does not silently override it. Stop/reconcile through Project Governance unless the delta is itself the user's newer explicit instruction and the task can be reconciled safely.

## Request minimum

A request should be short enough that the receiver can see the immediate action without archaeology, but complete enough to identify:

- what to do;
- where authoritative context lives;
- what changed since that authority was written;
- what may/may not be mutated;
- what evidence must return.

## Receipt profiles

### State-changing

```text
HANDOFF_ID:
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

### Read-only audit/review

```text
HANDOFF_ID:
MODE: AUDIT | REVIEW | VERIFY
AUDIT_TARGET:
OBSERVED_IDENTITY:
EVIDENCE_RANGE:
SKILLS_USED:
FINDINGS:
  BLOCKING:
  IMPORTANT:
  MINOR:
UNKNOWN_OR_UNVERIFIED:
CI_TEST_HOST_EVIDENCE:
CONTROL_ALIGNMENT_OBSERVATION: MATCH | STALE | UNKNOWN
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
VERDICT: PASS | PASS_WITH_FOLLOWUPS | STOP
NEXT_SAFE_ACTION:
```

Fields may be omitted only when genuinely not applicable and that is clear; do not silently omit a required decision signal.
