---
name: agent-handoff
description: Use when engineering responsibility crosses agents, sessions, machines, or execution contexts and the receiver needs a standardized bounded card or the sender needs a structured receipt.
---

# Agent Handoff

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff transports responsibility/evidence; it does not create task authority or copy sender runtime configuration into the receiver.

## Two independent dimensions

- `CAPABILITY` — which bounded Engineering Governance Skill, if any, the receiver should use (`NONE` when no specialist capability is needed).
- `MODE` — the receiver action/side-effect class: `EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE`.

`MODE` does **not** select or replace a Skill. Example: a formal cross-context evidence verdict may use `CAPABILITY: evidence-audit` with `MODE: AUDIT`.

## Standard card

Required core fields:

```text
CARD_ID
TASK_ID
MODE
CAPABILITY: <skill | NONE>
TARGET
AUTHORITY
DELTA: <fresh transfer delta | NONE>
BOUNDARY
RETURN_CONTRACT
```

Conditional fields include `PURPOSE`, `PROFILE`, `OBSERVED_BASIS`, source/target context, transfer-specific `STOP`, and claim/evidence fields. See `references/handoff-contract.md`.

## Modes

- `EXECUTE` — authorized state change;
- `AUDIT` — read-only audit action;
- `REVIEW` — read-only evaluation;
- `VERIFY` — confirm a named claim/identity/check; normal test-run cards map here;
- `DIAGNOSE` — read-only diagnostic evidence/question transfer.

Changing test code or diagnostic instrumentation is state-changing and therefore uses `EXECUTE` with an explicit `PURPOSE`/boundary.

Same-purpose continuation preserves the same `TASK_ID`. The receiver resolves its own runtime/configuration capabilities. A Card cannot expand authorization.
