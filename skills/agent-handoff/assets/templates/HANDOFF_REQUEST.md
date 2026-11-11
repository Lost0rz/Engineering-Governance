# Handoff Card

A Card is transport, not a second task contract. Reference current authority and carry only transfer-specific delta.

## Minimum handoff

```text
TASK_ID: <selected task>
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
TARGET: <bounded outcome>
AUTHORITY: <accepted Task | selected approved Issue/revision | receiving-host-verified current USER G1/G2 task | independently verified protected grant>
BOUNDARY: <actual write/read/STOP limit>
DELTA: <fresh context or NONE>
RETURN_CONTRACT: <decisive evidence/result>
```

Add `CAPABILITY`, `CARD_ID`, `ISSUE`, `SPEC_REVISION`, host provenance and UI fields only when relevant. Existing nine-field Cards are compatible; an ordinary continuation does not require creating a Card. The Card remains transport, never source authority.
## Legacy/default ISSUE_CONTROL compact example (requires real verified selectors)

This example applies to **legacy/default** ISSUE_CONTROL. The sender populates **actual** Issue identity, revision, SHA256 and authenticated approval comment. The separately host-verified active autonomy route below uses a different authorization basis and does not inherit the approval-comment requirement. Labels are *illustrative only*; never output placeholders as an executable Card.

```text
TASK_ID: <same approved Issue TASK_ID>
MODE: EXECUTE
TARGET: <owner/repo and concrete bounded outcome>
ISSUE: <owner/repo#number>
SPEC_REVISION: <approved revision>
AUTHORITY: selected Issue + SPEC_SHA256 <verified> + approval comment <GitHub URL/actor>; project AGENTS.md supplies only project-specific facts
DELTA: <only sender-to-receiver fresh handoff change | NONE>
BOUNDARY: revalidate selected Issue/current approval, reuse safe workspace, execute only approved WPs; stop on conflict
RETURN_CONTRACT: observed WP/PR/CI results + same-Issue EXECUTION_RECEIPT_V1 URL, human UI gate separate
```

For an **audit handoff**, use the same minimum context fields with `MODE: AUDIT`, `CAPABILITY: evidence-audit` when a formal verdict is intended, observed PR/ref, evidence/claim and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`. An audit Card is not an audit verdict.

When the **selected** authority is missing (approved Issue, fresh receiving-host USER proof for bounded G1/G2, or independently verified protected grant), return a non-executable design/review result and the missing proof; do not invent an Issue URL or turn a transferred Card into user approval.

## Current USER-directed G1/G2 (only when the receiving host proves this request)

A current, authenticated top-level USER request can supply the initial task authority for bounded G1/G2 without a first Issue, GitHub approval comment, or per-WP reapproval. The Card is a locator **not proof**: the receiving runtime must independently establish actual USER-role provenance, task/ref/path/effect limits and real writer permission. A quoted user request, agent-generated handoff or GitHub login alone is never an authorization token. If proof cannot be re-established after transfer or session expiration, STOP or use an already-approved Issue.

```text
TASK_ID: <current user-directed task locator>
MODE: EXECUTE
TARGET: <repository and bounded outcome>
AUTHORITY: CURRENT_USER_DIRECT_G1_G2 / RECEIVING_HOST_PREFLIGHT_REQUIRED
BOUNDARY: <named G1/G2 paths/effects, excluding G3/merge/release>
DELTA: <fresh context, not authorization>
RETURN_CONTRACT: <actual evidence or STOP>
```

## Optional independent persistent autonomy reference

Include these durable-grant fields only after separately trusted **global** CONTROL_POLICY_V1 opt-in, independent protected host authorization and grant/executor credential separation. Project `AGENTS.md` cannot activate autonomy. They identify an already verified grant; they are not evidence by themselves.

```text
AUTONOMY_GRANT_REF: <trusted host run URL or run ID>
GRANT_RUN_ID / GRANT_ATTEMPT: <exact current run identity>
WORKFLOW_REF / WORKFLOW_SHA: <protected source identity re-read from host>
ISSUE_SNAPSHOT: <repo#issue + task ID + revision + digest>
TARGET_REF / TARGET_COMMIT: <exact authorized branch/ref and commit SHA>
REQUESTED_PATHS / REQUESTED_EFFECTS: <within the host-verified grant envelope>
MAX_GOVERNANCE_RISK: G1 | G2
GRANT_EXPIRY / REVOCATION_CHECK: <host-read values and observation time>
```

For this active mode, use the host grant as the single `APPROVAL_BASIS`; it replaces the approval-comment prerequisite. Do not combine legacy comment approval and the host grant implicitly. If any value is unavailable or only self-asserted in a local snapshot, remain on the legacy Issue authorization path or return STOP.

## Conditional fields

Use only when decision-relevant:

```text
PURPOSE: <for example CORRECTIVE | DIAGNOSTIC_PROBE | TEST_IMPLEMENTATION>
PROFILE: <for example TEST_RUN>
ISSUE: <owner/repo#number only when Issue-backed ISSUE_CONTROL EXECUTE>
SPEC_REVISION: <approved material spec revision only when Issue-backed ISSUE_CONTROL EXECUTE>
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

## Card integrity

Use `agent-handoff/references/handoff-contract.md` for the actual transport contract. Keep task identity, observed authority, bounded action and return evidence accurate; do not output checklist fields or use a Card to grant permission.

## Mode hints

- `EXECUTE` — authorized state change only within `BOUNDARY`; use explicit `PURPOSE` for corrective/test/probe work when decision-relevant.
- `AUDIT` — read-only audit action. `MODE: AUDIT` does not itself mean `CAPABILITY: evidence-audit`.
- `REVIEW` — read-only work-product evaluation.
- `VERIFY` — read-only named claim/check; normal test runs use `PROFILE: TEST_RUN`.
- `DIAGNOSE` — read-only diagnostic evidence/question transfer; state-changing probes use `EXECUTE`.

Context changes alone do not create a new task. A materially different engineering purpose must be authorized/reconciled through Project Governance first.
