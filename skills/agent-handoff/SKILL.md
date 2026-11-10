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
### Sender and receiver boundary

Project Governance selects the task and validates the applicable approval or trusted grant. This Skill only transports a bounded Card or observed Receipt. Missing execution authority means a non-executable explanation/link, not an invented Card; the receiver verifies current authority through Project Governance before writing. Details belong to `references/handoff-contract.md`.


## Two independent dimensions

- `CAPABILITY` — which bounded Engineering Governance Skill, if any, the receiver should use (`NONE` when no specialist capability is needed).
- `MODE` — the receiver action/side-effect class: `EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE`.

`MODE` does **not** select or replace a Skill. Example: a formal cross-context evidence verdict may use `CAPABILITY: evidence-audit` with `MODE: AUDIT`.

Task-purpose labels such as `CORRECTIVE`, `FEATURE`, `RELEASE`, or `HOTFIX` are not valid `MODE` values. Put them in `PURPOSE` or describe them in `DELTA` when decision-relevant.

## Card schema

Use the minimal `TASK_ID, MODE, TARGET, AUTHORITY, BOUNDARY, DELTA, RETURN_CONTRACT` fields defined in `references/handoff-contract.md`. `CARD_ID` and `CAPABILITY` are conditional, not approval gates. Do not copy an Issue/Task spec into a Card or create one for an ordinary same-task continuation.


## Issue execution and receipt

Issue approval and comment/receipt rules belong to Project Governance's `issue-control.md` and `issue-execution-contract.md`. This Skill carries the selected authority reference and resulting evidence; it does not redefine either legacy or autonomous approval/receipt requirements.


## Human UI evidence

Carry automated/browser findings separately from `HUMAN_UI_ACCEPTANCE` when relevant. AI clicking or screenshots cannot supply the human decision. The owning project and Project Governance acceptance rules determine the gate; the Card/Receipt only records its observed state.


## Pre-return integrity check

Do not return a Card that invents authority, changes the selected task, expands write/risk limits, copies a long planning document, claims an unobserved PASS, or delegates human UI acceptance to AI. Prefer a concise corrected Card over a checklist of booleans. The receiver validates current authority and actual changed paths when that decision matters. A structured receipt reports observed results and real evidence rather than satisfying a universal output schema.
## Receiver action

`EXECUTE` is state-changing; `AUDIT`, `REVIEW`, `VERIFY` and `DIAGNOSE` are read-only. A state-changing test/probe uses `EXECUTE`. The receiving runtime chooses actual tools/models; a Card cannot elevate authority or impose an external workflow.

