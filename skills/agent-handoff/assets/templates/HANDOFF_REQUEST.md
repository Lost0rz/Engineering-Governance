# Handoff Card

A Card is transport, not a second task contract. Reference current authority and carry only transfer-specific delta.

## Required core

```text
CARD_ID: <id>
TASK_ID: <same authorized task unless Project Governance changed the task boundary>
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
CAPABILITY: <Engineering Governance Skill | NONE>
TARGET: <immediate requested outcome / object>
AUTHORITY: <current task + other decision-relevant authority references>
DELTA: <fresh transfer-specific delta | NONE>
BOUNDARY: <allowed read/write/action boundary>
RETURN_CONTRACT: <evidence/result required for the next decision>
```

`CAPABILITY` selects the bounded Skill/capability the receiver should use. `MODE` classifies receiver action/side effects. A mode name never replaces Skill routing or grants mutation authority.

## Conditional fields

Use only when decision-relevant:

```text
PURPOSE: <for example DIAGNOSTIC_PROBE | TEST_IMPLEMENTATION>
PROFILE: <for example TEST_RUN>
OBSERVED_BASIS: <revision/observation/head>
SOURCE_CONTEXT: <web/local/cloud/subagent/reviewer/session/machine>
TARGET_CONTEXT: <web/local/cloud/subagent/reviewer/session/machine>
STOP: <transfer-specific stop condition>
CLAIM: <named proposition for VERIFY/AUDIT when needed>
EXPECTED_EVIDENCE: <what would establish the claim>
AUDIT_INDEPENDENCE: <SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN>
```

Do not duplicate the full objective, scope, acceptance, STOP conditions or workspace policy already owned by `CURRENT_TASK.md`. If accessible authority conflicts materially with the Card, return to Project Governance rather than following the stale Card.

## Mode hints

- `EXECUTE` — authorized state change only within `BOUNDARY`; use explicit `PURPOSE` for state-changing test/probe work.
- `AUDIT` — read-only audit action. `MODE: AUDIT` does not itself mean `CAPABILITY: evidence-audit`.
- `REVIEW` — read-only work-product evaluation.
- `VERIFY` — read-only named claim/check; normal test runs use `PROFILE: TEST_RUN`.
- `DIAGNOSE` — read-only diagnostic evidence/question transfer; state-changing probes use `EXECUTE`.

Context changes alone do not create a new task. A materially different engineering purpose must be authorized/reconciled through Project Governance first.
