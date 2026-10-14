---
name: agent-handoff
description: Use when engineering responsibility crosses agents, sessions, machines, or execution contexts and the receiver needs a bounded request or the sender needs a structured evidence receipt.
---

# Agent Handoff

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff transports responsibility/evidence; it does not create task authority or copy sender runtime configuration into the receiver. Read `references/handoff-contract.md` for mode/receipt details.

## Same-task continuation

Preserve the same `TASK_ID` when engineering purpose/authorization is unchanged. Reference accepted task/design authority rather than asking each receiver to reconstruct the solution from chat history.

## Environment boundary

The receiver resolves its own runtime/configuration capabilities. A handoff may carry policy or a task-relevant capability requirement, but not sender-specific model/reasoning/concurrency/tool values as receiver defaults.

## Modes

- `EXECUTE` — authorized state-changing work in another context.
- `AUDIT` — read-only evidence/acceptance verdict.
- `DIAGNOSE` — read-only diagnostic evidence/question transfer.
- `REVIEW` — read-only evaluation.
- `VERIFY` — confirm a named claim/identity/check.

If diagnosis requires adding/removing/changing instrumentation or another state-changing probe, use `MODE: EXECUTE` with `PURPOSE: DIAGNOSTIC_PROBE` under explicit authorization. Diagnosis capability may still be Incident Doctor; the handoff mode reflects side effects.

## Request

Use only needed fields:

```text
HANDOFF_ID
TASK_ID
MODE
TARGET
AUTHORITY
AUTHORITY_OBSERVED_BASIS: <when material>
SOURCE_CONTEXT / TARGET_CONTEXT: <when useful>
DELTA
BOUNDARY
RETURN_CONTRACT
```

Receiver rereads accessible authorities. Incompatible drift stops for Project Governance reconciliation. Do not paste full controls, planning docs, generic governance, unrelated secrets/personal data, or sender runtime configuration by default.

## Receipt

Return decision-useful evidence: actual identity/changes/checks/findings/unknowns, authority compatibility when material, and control alignment for final state-changing handoffs. Explicitly state legitimate no-change/no-output success.
