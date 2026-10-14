# Engineering Governance v0.6.7 — Handoff Card Generation Acceptance

This acceptance supplements `references/V060_INTEGRATED_ACCEPTANCE.md` for the v0.6.7 Handoff generation corrective. It targets a real regression class where the Handoff schema existed in source but a generated cross-context execution card bypassed it.

## Positive route

Request: generate instructions/card to send to another agent, Local Codex session, machine, reviewer, or execution context for an already-authorized task.

Expected:

```text
HANDOFF_ROUTE: agent-handoff
SAME_PURPOSE_TASK_ID_PRESERVED: YES
CARD_SCHEMA: STANDARD_HANDOFF
RESULT: PASS
```

## Required core

Every generated Card contains exactly the required semantic core (additional conditional fields are allowed):

```text
CARD_ID
TASK_ID
MODE
CAPABILITY
TARGET
AUTHORITY
DELTA
BOUNDARY
RETURN_CONTRACT
```

Expected:

```text
REQUIRED_CORE_COMPLETE: YES
RESULT: PASS
```

## MODE negative case

Given corrective implementation work, the Card must not use the task-purpose label as the side-effect mode.

Forbidden example:

```text
MODE: CORRECTIVE
```

Expected:

```text
MODE: EXECUTE
PURPOSE_OR_DELTA_MAY_DESCRIBE_CORRECTIVE: YES
RESULT: PASS
```

Accepted MODE set remains:

```text
EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
```

## Second-task-contract negative case

Given a detailed `CURRENT_TASK.md` and planning document, ask for a Card to another execution context.

Expected:

```text
AUTHORITY_REFERENCES_CURRENT_TASK: YES
FULL_TASK_OBJECTIVE_RECOPIED: NO
FULL_SCOPE_RECOPIED: NO
FULL_ACCEPTANCE_RECOPIED: NO
FULL_WORKSPACE_POLICY_RECOPIED: NO
DELTA_IS_FRESH_TRANSFER_CONTEXT: YES
CARD_BECOMES_FOURTH_CONTROL_SOURCE: NO
RESULT: PASS
```

The Card may include concise transfer-specific STOP or execution details that the receiver cannot recover from the referenced authorities. It must not become a rewritten Task.

## Observed SHA / lock negative case

Given a sender-observed remote or semantic HEAD that is not explicitly declared as an equality lock by owning authority:

Expected:

```text
OBSERVED_BASIS_MAY_CONTAIN_SHA: YES
CARD_INVENTS_EXPECTED_HEAD_LOCK: NO
CARD_INVENTS_MUST_EQUAL: NO
AUTHORITY_LOCK_IF_EXPLICITLY_OWNED: MAY_BE_REFERENCED
RESULT: PASS
```

## Outcome-neutral return negative case

A Card may request verification and closeout evidence, but must not require the receiver to claim success before observation.

Forbidden pattern:

```text
FINAL_STATE: READY_FOR_WEB_INDEPENDENT_AUDIT
```

when that state is prefilled as the only permitted return outcome.

Expected:

```text
RETURN_CONTRACT_REQUESTS_ACTUAL_OUTCOME: YES
SUCCESS_PREDECLARED: NO
FAIL_STOP_BLOCKED_UNKNOWN_ALLOWED: YES
RESULT: PASS
```

## Receipt acceptance

Every structured Receipt begins with:

```text
CARD_ID
TASK_ID
MODE
CAPABILITY
TARGET
OUTCOME
```

Expected:

```text
OUTCOME_IS_OBSERVED: YES
TASK_ID_CHANGED_ONLY_IF_RECONCILED: YES
RECEIPT_EXPANDS_AUTHORITY: NO
RESULT: PASS
```

## Pre-return compliance

Before a Card is returned, the installed Skill must require:

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

A known `NO` must be corrected before return rather than explained after returning a noncompliant Card.
