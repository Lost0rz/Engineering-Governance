# Handoff contract

## Authority and freshness

Same-purpose continuation preserves `TASK_ID`. `AUTHORITY` names current truth; the receiver rereads it when accessible. When drift matters, `AUTHORITY_OBSERVED_BASIS` allows:

- `CURRENT_COMPATIBLE` — continue under current truth;
- `CURRENT_CONFLICT` — stop for Project Governance reconciliation;
- `AUTHORITY_UNAVAILABLE` — stop when required authority cannot be accessed and a bounded snapshot is insufficient.

`DELTA` contains only recent transfer-specific facts/boundaries.

## Request envelope

```text
HANDOFF_ID
TASK_ID
MODE: EXECUTE | AUDIT | DIAGNOSE | REVIEW | VERIFY
TARGET
AUTHORITY
AUTHORITY_OBSERVED_BASIS: <when material>
SOURCE_CONTEXT / TARGET_CONTEXT: <when useful>
DELTA
BOUNDARY
RETURN_CONTRACT
```

## Runtime/configuration isolation

Runtime/model/tool/capacity configuration belongs to the receiving execution environment unless an accepted portable project artifact owns it. Sender observations may be evidence about the sender, not receiver defaults.

Under `ENVIRONMENT_DEFAULT_ONLY`, concrete Sub Agent model/reasoning values never propagate as receiver defaults. The same rule applies to concurrency/delegation/tool/runtime values unless a portable authority explicitly owns them.

## Mode side effects

- `EXECUTE` — state change allowed only within active authorization.
- `AUDIT`, `REVIEW`, `VERIFY` — read-only.
- `DIAGNOSE` — read-only transfer of diagnostic question/evidence/hypothesis state.

A state-changing diagnostic probe uses `MODE: EXECUTE` and `PURPOSE: DIAGNOSTIC_PROBE`, with its mutation/cleanup boundary explicitly authorized. This keeps diagnosis capability separate from handoff side-effect class.

## Same task vs new task

Different agent/session/machine/context does not require a new task. A materially different engineering purpose (independent audit, distinct corrective, new design objective) returns to Project Governance for task reconciliation.

## Context economy

Prefer authority references + bounded fresh delta. Exact excerpts are for inaccessible sources or exact-wording needs only. Do not send full chat history or repeated generic governance.

## Receipts

State-changing receipts report task/handoff identity, outcome, start/final identity, changed paths, verification, lifecycle effects, unresolved evidence, and final control alignment when applicable.

Read-only receipts report target/range/identity, evidence/findings/unknowns, verdict/result, and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`.
