---
name: agent-handoff
description: Use for cross-context engineering construction/execution cards (施工卡), audit/review cards (审计卡), Codex Desktop/local AI handoff commands, verification cards and execution receipts. Transports approved Issue/Task authority; does not create approval or authorize mutation.
---

# Agent Handoff

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff transports responsibility/evidence; it does not create task authority, import a second engineering framework, or copy sender runtime configuration into the receiver.

## Trigger

Use this Skill when the user actually requests an explicit cross-context execution, review, audit, verification or diagnosis handoff or structured receipt. Ordinary same-session continuation, source inspection, status advice and routine agents sharing a known task do **not** require a new Card just because context exists.

Do not fall back to a legacy free-form execution-card format because the task is corrective or detailed. The transfer artifact must satisfy this Skill even when Project Governance, a plan, or a FILE_CONTROL Task / approved ISSUE_CONTROL Issue already contains extensive implementation detail.
### Sender and receiver entry rule

For "给我施工卡", resolve the current project and task once and deliver a minimal executable Card **only if** its actual legacy approval or independently accepted host-verified autonomy grant can be checked. An unapproved or incomplete legacy Issue yields a non-executable link and the smallest blocking fact, not a fabricated Card. For opted-in delegated approval, include genuine comment provenance and `DELEGATED_ACCOUNT_ATTESTED`; never misrepresent an AI proxy comment as direct human provenance. Do not duplicate the Issue spec or invent a new task.

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

For an expressly requested executable cross-context transfer, include only what the receiver cannot safely recover from the selected task:

```text
TASK_ID: <selected task>
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
TARGET: <immediate outcome>
AUTHORITY: <current task/Issue + applicable approval or verified grant locator>
BOUNDARY: <specific risk/write/STOP limits>
DELTA: <fresh context or NONE>
RETURN_CONTRACT: <decisive result/evidence>
```

Add `CAPABILITY`, `CARD_ID`, exact Issue revision/digest/approval identity, host grant identity, UI gate or runtime details **only when needed**. Existing longer nine-field Cards remain readable; this is not a new schema-enforcement service. The receiver independently reads current authority. A Card is not a permission grant.
## Issue execution transfer and durable receipt

For ISSUE_CONTROL, hand off only the verified repository/Issue/current SPEC_REVISION and transfer-specific delta; do not copy the long Issue body. The local receiver retrieves the selected current spec and verifies the applicable legacy approval or separately accepted, independently host-verified autonomy grant. Under **legacy/default ISSUE_CONTROL**, post meaningful PAUSE/TERMINATE/final execution receipts to the same Issue and verify their delivery. In an actually active, independently verified G1/G2 autonomy mode, routine Issue comments are optional when evidence is recoverable from the task/PR/commit/CI/handoff; material risk expansion still needs a valid new authorization. Comments are evidence to consult, not an extra Writer-release permission and cannot expand scope. See Project Governance `issue-control.md` and `issue-execution-contract.md`.

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

## Pre-return integrity check

Do not return a Card that invents authority, changes the selected task, expands write/risk limits, copies a long planning document, claims an unobserved PASS, or delegates human UI acceptance to AI. Prefer a concise corrected Card over a checklist of booleans. The receiver validates current authority and actual changed paths when that decision matters. A structured receipt reports observed results and real evidence rather than satisfying a universal output schema.
## Modes

- `EXECUTE` — authorized state change;
- `AUDIT` — read-only audit action;
- `REVIEW` — read-only evaluation;
- `VERIFY` — confirm a named claim/identity/check; normal test-run cards map here;
- `DIAGNOSE` — read-only diagnostic evidence/question transfer.

Changing test code or diagnostic instrumentation is state-changing and therefore uses `EXECUTE` with an explicit `PURPOSE`/boundary.

Same-purpose continuation preserves the same `TASK_ID`. The receiver resolves its own runtime/configuration capabilities. A Card cannot expand authorization or import a second engineering framework.
