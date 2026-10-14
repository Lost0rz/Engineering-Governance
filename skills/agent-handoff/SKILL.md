---
name: agent-handoff
description: Use when engineering responsibility crosses agents, sessions, machines, or execution contexts and the receiver needs a standardized bounded card or the sender needs a structured receipt.
---

# Agent Handoff

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff transports responsibility/evidence; it does not create task authority or copy sender runtime configuration into the receiver.

## Trigger

Use this Skill whenever the requested output itself is intended to transfer engineering responsibility or evidence to another agent, session, machine, reviewer, or execution context. This includes requests to generate an execution/construction card, audit card, review card, verification/test-run card, diagnostic card, or structured return receipt for another context.

Do not fall back to a legacy free-form execution-card format because the task is corrective or detailed. The transfer artifact must satisfy this Skill even when Project Governance, a plan, or `CURRENT_TASK.md` already contains extensive implementation detail.

## Two independent dimensions

- `CAPABILITY` — which bounded Engineering Governance Skill, if any, the receiver should use (`NONE` when no specialist capability is needed).
- `MODE` — the receiver action/side-effect class: `EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE`.

`MODE` does **not** select or replace a Skill. Example: a formal cross-context evidence verdict may use `CAPABILITY: evidence-audit` with `MODE: AUDIT`.

Task-purpose labels such as `CORRECTIVE`, `FEATURE`, `RELEASE`, or `HOTFIX` are not valid `MODE` values. Put them in `PURPOSE` or describe them in `DELTA` when decision-relevant.

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

## Mandatory pre-return compliance gate

Before returning any generated Handoff Card, correct the draft in the same pass until all are true:

```text
HANDOFF_ROUTE_APPLIED: YES
REQUIRED_CORE_COMPLETE: YES
MODE_VALID: YES
TASK_AUTHORITY_PRESERVED: YES
AUTHORITY_REFERENCED_NOT_DUPLICATED: YES
DELTA_IS_TRANSFER_SPECIFIC: YES
BOUNDARY_DOES_NOT_EXPAND_AUTHORITY: YES
OBSERVED_IDENTITY_NOT_PROMOTED_TO_LOCK: YES
RETURN_CONTRACT_OUTCOME_NEUTRAL: YES
```

Interpretation:

- every required core field is present;
- `MODE` is exactly one accepted side-effect class;
- same-purpose transfer keeps the current `TASK_ID` unless Project Governance already changed task authority;
- `AUTHORITY` points to current task/rules/design authorities instead of copying their full objective/scope/acceptance/STOP/workspace policy;
- `DELTA` carries only new context the receiver would not recover from the referenced authorities;
- a Card never expands mutation/write authority;
- a SHA/ref observed by the sender belongs in `OBSERVED_BASIS` unless an owning authority explicitly declares an equality/lock requirement; the Card must not invent `EXPECTED_HEAD`, `MUST_EQUAL`, or equivalent lock semantics;
- `RETURN_CONTRACT` requests the actual result/evidence. Do not prefill a successful `FINAL_STATE`, `READY`, `PASS`, or merge/release outcome that has not yet been observed.

A known `NO` is a generation failure and must be fixed before the Card is returned. Do not return the noncompliant draft with an explanatory note.

Before returning a structured Handoff Receipt, likewise verify that its required core fields are present and that `OUTCOME` reports the observed result rather than a predetermined success state.

## Modes

- `EXECUTE` — authorized state change;
- `AUDIT` — read-only audit action;
- `REVIEW` — read-only evaluation;
- `VERIFY` — confirm a named claim/identity/check; normal test-run cards map here;
- `DIAGNOSE` — read-only diagnostic evidence/question transfer.

Changing test code or diagnostic instrumentation is state-changing and therefore uses `EXECUTE` with an explicit `PURPOSE`/boundary.

Same-purpose continuation preserves the same `TASK_ID`. The receiver resolves its own runtime/configuration capabilities. A Card cannot expand authorization.
