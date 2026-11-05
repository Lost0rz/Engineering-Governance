# Handoff Card

A Card is transport, not a second task contract. Reference current authority and carry only transfer-specific delta.

## Required core

```text
CARD_ID: <id>
TASK_ID: <same authorized task unless Project Governance changed the task boundary>
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
CAPABILITY: <Engineering Governance Skill | NONE>
TARGET: <immediate requested outcome / object>
AUTHORITY: <FILE_CONTROL Task or ISSUE_CONTROL approved Issue URL/revision/provenance, plus relevant project/design pointers>
DELTA: <fresh transfer-specific delta | NONE>
BOUNDARY: <allowed read/write/action boundary>
RETURN_CONTRACT: <actual evidence/result required for the next decision; do not predeclare success>
```

`CAPABILITY` selects the bounded Skill/capability the receiver should use. `MODE` classifies receiver action/side effects. A mode name never replaces Skill routing or grants mutation authority.

Task-purpose labels such as `CORRECTIVE`, `FEATURE`, `RELEASE`, or `HOTFIX` are not `MODE` values. Put them in `PURPOSE` or `DELTA` when useful.

## ISSUE_CONTROL compact example (requires real verified selectors)

The sender populates **actual** Issue identity, revision, SHA256 and authenticated approval comment; these labels are *illustrative only*. Do not output placeholders as an executable Card.

```text
CARD_ID: <current-card-id>
TASK_ID: <same approved Issue TASK_ID>
MODE: EXECUTE
CAPABILITY: project-governance
TARGET: <owner/repo and concrete bounded outcome>
ISSUE: <owner/repo#number>
SPEC_REVISION: <approved revision>
AUTHORITY: AGENTS.md + selected Issue + SPEC_SHA256 <verified> + approval comment <GitHub URL/actor>
DELTA: <only sender-to-receiver fresh handoff change | NONE>
BOUNDARY: revalidate selected Issue/current approval, reuse safe workspace, execute only approved WPs; stop on conflict
RETURN_CONTRACT: observed WP/PR/CI results + same-Issue EXECUTION_RECEIPT_V1 URL, human UI gate separate
```

For an **audit handoff**, use the same nine core fields with `MODE: AUDIT`, `CAPABILITY: evidence-audit` when a formal verdict is intended, observed PR/ref, evidence/claim and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`. An audit Card is not an audit verdict.

When no valid Issue spec/approval exists, return a non-executable design/review result and the blocking Issue URL; do not manufacture an EXECUTE Card or clone the approved plan into chat.

## Conditional fields

Use only when decision-relevant:

```text
PURPOSE: <for example CORRECTIVE | DIAGNOSTIC_PROBE | TEST_IMPLEMENTATION>
PROFILE: <for example TEST_RUN>
ISSUE: <owner/repo#number when ISSUE_CONTROL EXECUTE>
SPEC_REVISION: <approved material spec revision when ISSUE_CONTROL EXECUTE>
OBSERVED_BASIS: <sender-observed revision/observation/head; not automatically a lock>
SOURCE_CONTEXT: <web/local/cloud/subagent/reviewer/session/machine>
TARGET_CONTEXT: <web/local/cloud/subagent/reviewer/session/machine>
STOP: <transfer-specific stop condition>
CLAIM: <named proposition for VERIFY/AUDIT when needed>
EXPECTED_EVIDENCE: <what would establish the claim>
AUDIT_INDEPENDENCE: <SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN>
```

Do not duplicate objective, scope, acceptance, STOP conditions or workspace policy already owned by the mode-selected Task/Issue. If accessible authority conflicts materially with the Card, return to Project Governance rather than following the stale Card.

A sender-observed SHA/ref belongs in `OBSERVED_BASIS` by default. Use `EXPECTED_HEAD`, `REQUIRED_HEAD`, `MUST_EQUAL`, or another equality-lock field only when the referenced owning authority explicitly defines that lock.

## Mandatory pre-return gate

Before returning this Card, revise the draft until every item is YES:

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

Do not return a known-noncompliant draft plus commentary. Correct it before return.

## Mode hints

- `EXECUTE` — authorized state change only within `BOUNDARY`; use explicit `PURPOSE` for corrective/test/probe work when decision-relevant.
- `AUDIT` — read-only audit action. `MODE: AUDIT` does not itself mean `CAPABILITY: evidence-audit`.
- `REVIEW` — read-only work-product evaluation.
- `VERIFY` — read-only named claim/check; normal test runs use `PROFILE: TEST_RUN`.
- `DIAGNOSE` — read-only diagnostic evidence/question transfer; state-changing probes use `EXECUTE`.

Context changes alone do not create a new task. A materially different engineering purpose must be authorized/reconciled through Project Governance first.
