# CURRENT TASK — Capability Model v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-MODEL-V060-061`

State: `COMPLETE`

Mode: remote source design, external-reference audit, capability-model expansion, routing integration, and source evidence audit

## Objective

Expand Engineering Governance from three top-level Skills to a seven-Skill capability model that preserves the existing three-file authority/control semantics while adding distinct reusable capabilities for solution design, execution orchestration, agent handoff, and evidence audit.

The expansion must reduce duplicated execution-card content, prevent handoff prompts from becoming second task authorities, make subagent/model/parallel behavior explicit and bounded, and keep audit claims tied to concrete evidence identity.

## Planning context

- Related document: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: Task 061 implements the initial v0.6.0 capability-model source framework and routing described by that document.

## Accepted baseline

- Start Repository HEAD: `3b8d99c3dba13ca01098abade5c6e696454ddd10`.
- Published/installed release baseline remains `plugin-v0.5.5`; release/distribution was not changed by this task.
- Source branch: `codex/capability-model-v0.6.0`.

## Completed execution

1. Audited Superpowers and selected external high-signal engineering/agent projects.
2. Created durable design authority `documents/engineering-governance-capability-model-v0.6.0.md` with explicit adopt/adapt/reject decisions.
3. Added four top-level Skills:
   - `solution-design`
   - `execution-orchestrator`
   - `agent-handoff`
   - `evidence-audit`
4. Preserved and re-integrated:
   - `project-governance`
   - `domain-navigation`
   - `incident-doctor`
5. Updated global routing/adoption/template semantics from three to seven Skills.
6. Updated root `AGENTS.md`, README, plugin metadata (`0.6.0`), upstream conceptual references, and Incident Doctor systematic-technique references.
7. Created PR `#26` as OPEN / DRAFT / UNMERGED.
8. Performed final remote source/routing evidence audit.

## Accepted design constraints

- `CURRENT_TASK.md` remains the single active execution authorization; handoff requests never authorize work independently.
- `CURRENT_STATUS.md` remains current-state authority; handoff/receipt/ledger/audit artifacts do not become second status stores.
- `AGENTS.md` and Skills own durable engineering rules; execution/audit cards reference them rather than copy them.
- Agent Handoff carries authority references, fresh delta, action boundary, and return contract.
- Execution Orchestrator prefers one executor/parallel readers, requires proven-disjoint write scopes/workspaces for multiple writers, and forbids silent model escalation.
- Evidence Audit owns independent evidence verdicts but does not authorize corrective mutation.
- Solution Design is conditional; clear small changes do not acquire mandatory design/spec ceremony.
- Incident Doctor retains its blocking evidence-gap trigger.
- Universal mandatory TDD and unconditional subagent dispatch are not adopted.
- External projects remain conceptual references only; no runtime dependency was introduced.

## Verification result

`V2 remote source/routing audit: PASS`.

Evidence:

- Delivery / Semantic HEAD: `c97d3cef13ac5546bf00d9d1eb4d620c88ffad57`.
- Exactly seven intended top-level Skill directories observed.
- Four new `SKILL.md` files reread from the task branch with distinct trigger/authority boundaries.
- PR #26 diff: 23 changed paths at source-audit head; reusable-source changes are Markdown/JSON only and do not add runtime/daemon/workflow code.
- PR #26 host state at source-audit time: OPEN / DRAFT / UNMERGED / `mergeable=true`.
- Source-head commit statuses: none reported; CI PASS is **not** claimed.
- Historical `.github/workflows/release-plugin-v0.5.5.yml` is outside the changed-path set and remains a frozen v0.5.5 artifact.

## Acceptance criteria

Remote-source acceptance criteria for Task 061 are satisfied.

Local installed Plugin discovery/routing/runtime behavior and release publication are explicitly outside this task and remain unverified.

## Handoff / terminal state

Task 061 is complete as remote reusable-source construction.

PR #26 remains Draft pending a separate local Plugin/runtime acceptance task. If local acceptance reveals reusable-source defects, return them to the Web/remote source flow; local acceptance must not patch reusable source directly.

Control Alignment Gate:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-model-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UNCHANGED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
