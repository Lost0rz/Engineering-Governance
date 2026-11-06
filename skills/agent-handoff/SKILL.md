---
name: agent-handoff
description: Use for cross-context engineering construction/execution cards (施工卡), audit/review cards (审计卡), Codex Desktop/local AI handoff commands, verification cards and execution receipts. Transports approved Issue/Task authority; does not create approval or authorize mutation.
---

# Agent Handoff

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff transports responsibility/evidence; it does not create task authority, import a second engineering framework, or copy sender runtime configuration into the receiver.

## Trigger

Use this Skill whenever the requested output itself is intended to transfer engineering responsibility or evidence to another agent, session, machine, reviewer, or execution context. This includes requests to generate an execution/construction card, audit card, review card, verification/test-run card, diagnostic card, or structured return receipt for another context.

Do not fall back to a legacy free-form execution-card format because the task is corrective or detailed. The transfer artifact must satisfy this Skill even when Project Governance, a plan, or a FILE_CONTROL Task / approved ISSUE_CONTROL Issue already contains extensive implementation detail.
### Sender and receiver entry rule

For a plain-language Web request such as "给我施工卡", first let Project Governance resolve the *actual* project, existing Task/Issue and stage; then use this Skill to deliver one **compact** Card. In ISSUE_CONTROL, distinguish (a) no suitable Issue: prepare/design the Issue under Project Governance, (b) Issue exists but unapproved or incomplete: link it as **non-executable** with the blocking reason, and (c) verified approved exact spec: emit the nine-field EXECUTE Card plus actual repository/Issue/revision/digest/approval provenance. Do not manufacture selectors or copy the nineteen-field spec into the Card.

For "给我审计卡", reference the existing approved/current Issue and observed PR/ref where available; use `MODE: AUDIT`, `CAPABILITY: evidence-audit` only for a formal verdict, and preserve read-only scope. Do not equate creating an audit Card with performing an audit. If the user asks *about* cards rather than to transfer an actual task, explain the format without creating Issue/PR/approval.

The **receiver** first invokes the available Governance entry, checks accepted `AGENTS.md`, mode-selected source authority and fresh host/writer facts, then revalidates approval before writes; the transport Card never skips those steps. If the plugin/Skill cannot actually load, or GitHub identity/digest/authorization is unavailable, return a bounded STOP/UNKNOWN receipt, not a claim that Engineering Governance ran. The detailed receiver checklist lives in `references/handoff-contract.md`; avoid mandatory multi-Skill startup cascades.


## Engineering framework ownership

A governed Engineering Governance Handoff Card transfers work **inside the Engineering Governance framework boundary**.

- `CAPABILITY` may name only a bounded Engineering Governance Skill/capability, or `NONE`.
- Do not add `SKILLS_REQUIRED`, `USE_SKILLS`, workflow steps, or equivalent directives that require external engineering framework/Skill/plugin names.
- External frameworks may be cited only as reference/provenance/evidence when genuinely relevant; mentioning them does not authorize the receiver to invoke or defer to them.
- Do not copy historical external Skill names from plans, prior receipts, chat/session history, installed catalogs, repository paths, or reference documents into a new execution requirement.
- TDD, debugging, review, planning, verification, or completion expectations belong as behavior/acceptance requirements or to the owning Engineering Governance capability, not as external Skill dependencies.
- If the card exposes a reusable capability gap, return to Project Governance/owning capability for reconciliation rather than routing the receiver into another engineering framework.

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
CAPABILITY: <Engineering Governance skill | NONE>
TARGET
AUTHORITY
DELTA: <fresh transfer delta | NONE>
BOUNDARY
RETURN_CONTRACT
```

Conditional fields include `PURPOSE`, `PROFILE`, `ISSUE`, `SPEC_REVISION`, `OBSERVED_BASIS`, source/target context, transfer-specific `STOP`, claim/evidence fields, and human-acceptance state when product-interface acceptance is material. Carry verification details only when they change the receiver's next decision; otherwise reference the task's verification contract rather than triggering another broad test/audit loop. See `references/handoff-contract.md`.

## Issue execution transfer and durable receipt

For ISSUE_CONTROL, hand off only the verified repository/Issue/approved SPEC_REVISION and transfer-specific delta; do not copy the long Issue body. The local receiver retrieves the current approved spec via `gh`/connector and follows deterministic WPs and L0/L1/L2/L3 deviation policy. PAUSE/TERMINATE/final execution receipts must be posted as comments on the **same Issue** and the actual comment receipt verified. Comment evidence cannot reauthorize a new scope or new model topology. See Project Governance `issue-control.md` and `issue-execution-contract.md`.

## Human UI acceptance preservation

For state-changing work that materially changes a real product interface, human UI/UX/product acceptance is the default final product-interface gate unless an owning user/project authority explicitly waives it. A missing field or silent task does not imply `NOT_REQUIRED`.

The receiving AI may still run Playwright/Cypress/E2E or other automated browser verification and may use browser/Computer Use/screenshots for debugging, evidence gathering, internal Design review, or corrective work. Those machine-driven checks must not be promoted into final human acceptance.

The Card/receipt should keep these claims separate when material:

```text
AUTOMATED_BROWSER_VERIFICATION
AI_RENDERED_INSPECTION
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

For a material product-interface change, default to `HUMAN_UI_ACCEPTANCE: PENDING` until an explicit human decision is observed. `NOT_REQUIRED` needs an explicit owning waiver or a clearly non-product-interface acceptance surface.

A receiver must not return `HUMAN_UI_ACCEPTANCE: PASS` merely because it opened the page, clicked through the workflow, or inspected screenshots/renders itself. `PASS`/`FAIL` requires an explicit human decision.

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
ENGINEERING_FRAMEWORK_OWNERSHIP_PRESERVED: YES
EXTERNAL_ENGINEERING_SKILL_REQUIREMENTS_ABSENT: YES
HUMAN_UI_ACCEPTANCE_OWNER_PRESERVED_IF_APPLICABLE: YES
```

Interpretation:

- every required core field is present;
- `MODE` is exactly one accepted side-effect class;
- same-purpose transfer keeps the current `TASK_ID` unless Project Governance already changed task authority;
- `AUTHORITY` points to FILE_CONTROL Task or ISSUE_CONTROL approved Issue/rules/design authorities instead of copying their full objective/scope/acceptance/STOP/workspace policy;
- `DELTA` carries only new context the receiver would not recover from the referenced authorities;
- a Card never expands mutation/write authority;
- a SHA/ref observed by the sender belongs in `OBSERVED_BASIS` unless an owning authority explicitly declares an equality/lock requirement; the Card must not invent `EXPECTED_HEAD`, `MUST_EQUAL`, or equivalent lock semantics;
- `RETURN_CONTRACT` requests the actual result/evidence. Do not prefill a successful `FINAL_STATE`, `READY`, `PASS`, or merge/release outcome that has not yet been observed;
- `CAPABILITY` is an Engineering Governance capability or `NONE`, and no external engineering framework/Skill/plugin is prescribed as required execution workflow;
- external framework names may remain only where they are genuinely reference/provenance/evidence, never as routing/execution authority;
- when human product-interface acceptance is required, the Card keeps it human-owned and does not delegate that final acceptance to AI Computer Use or screenshot inspection.

A known `NO` is a generation failure and must be fixed before the Card is returned. Do not return the noncompliant draft with an explanatory note.

Before returning a structured Handoff Receipt, likewise verify that its required core fields are present, that `OUTCOME` reports the observed result rather than a predetermined success state, that reported `Skills used`/capability route does not promote external reference Skills into Engineering Governance execution, and that any human UI acceptance field reflects an explicit human decision rather than machine observation.

## Modes

- `EXECUTE` — authorized state change;
- `AUDIT` — read-only audit action;
- `REVIEW` — read-only evaluation;
- `VERIFY` — confirm a named claim/identity/check; normal test-run cards map here;
- `DIAGNOSE` — read-only diagnostic evidence/question transfer.

Changing test code or diagnostic instrumentation is state-changing and therefore uses `EXECUTE` with an explicit `PURPOSE`/boundary.

Same-purpose continuation preserves the same `TASK_ID`. The receiver resolves its own runtime/configuration capabilities. A Card cannot expand authorization or import a second engineering framework.
