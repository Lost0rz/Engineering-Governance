---
name: agent-handoff
description: Use when engineering responsibility crosses agents, sessions, machines, or execution contexts and the receiver needs a standardized bounded card or the sender needs a structured receipt.
---

# Agent Handoff

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff transports responsibility/evidence; it does not create task authority or copy sender runtime configuration into the receiver.

## Standard card

Use the common envelope from `references/handoff-contract.md`:

```text
CARD_ID
TASK_ID
MODE
TARGET
AUTHORITY
OBSERVED_BASIS
DELTA
BOUNDARY
STOP
RETURN_CONTRACT
```

Omit fields that add no decision value, but do not replace missing authority with pasted chat history.

## Modes

- `EXECUTE` — authorized state change;
- `AUDIT` — read-only evidence/acceptance verdict;
- `REVIEW` — read-only evaluation;
- `VERIFY` — confirm a named claim/identity/check; normal test-run cards map here;
- `DIAGNOSE` — read-only diagnostic evidence/question transfer.

Changing test code or diagnostic instrumentation is state-changing and therefore uses `EXECUTE` with an explicit purpose/boundary.

Same-purpose continuation preserves the same `TASK_ID`. The receiver resolves its own runtime/configuration capabilities. Detailed mode profiles and receipt standards are in `references/handoff-contract.md`.
