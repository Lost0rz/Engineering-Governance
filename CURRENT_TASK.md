# CURRENT TASK — Capability Model v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-MODEL-V060-061`

State: `ACTIVE`

Mode: remote source design, external-reference audit, capability-model expansion, and routing integration

## Objective

Expand Engineering Governance from three top-level Skills to a seven-Skill capability model that preserves the existing three-file authority/control semantics while adding distinct reusable capabilities for solution design, execution orchestration, agent handoff, and evidence audit.

The expansion must reduce duplicated execution-card content, prevent handoff prompts from becoming second task authorities, make subagent/model/parallel behavior explicit and bounded, and keep audit claims tied to concrete evidence identity.

## Planning context

- Related document: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: this task implements the initial v0.6.0 capability-model framework and routing described by that document.

## Accepted baseline

- Start Repository HEAD: `3b8d99c3dba13ca01098abade5c6e696454ddd10`.
- Published/installed release baseline remains `plugin-v0.5.5` until a later release task explicitly changes distribution state.
- Existing top-level Skills at task start: `project-governance`, `domain-navigation`, `incident-doctor`.
- Existing root controls remain authoritative for this repository.

## In scope

1. Audit Superpowers and selected external high-signal projects for reusable concepts relevant to design, orchestration, handoff, and evidence audit.
2. Create and document the seven-Skill capability model:
   - `project-governance`
   - `solution-design`
   - `execution-orchestrator`
   - `agent-handoff`
   - `evidence-audit`
   - `domain-navigation`
   - `incident-doctor`
3. Add the four new Skill modules with distinct triggers, boundaries, composition rules, and output contracts.
4. Update Project Governance routing/adoption/global-routing material so the new Skills compose without creating duplicate task authority or control planes.
5. Update repository-level rules, README, upstream-reference notes, and plugin metadata to describe the new capability model.
6. Preserve the existing evidence-gated Incident Doctor semantics and risk-proportional `V0`–`V3` verification model; do not import mandatory universal TDD or unconditional debugging gates.
7. Perform a final source/diff/routing audit and leave the branch ready for separate local Plugin/runtime acceptance.

## Explicit design constraints

- `CURRENT_TASK.md` remains the single active execution authorization; a handoff request never authorizes work independently.
- `CURRENT_STATUS.md` remains the concise verified current-state snapshot; handoff/receipt content does not become a second status store.
- `AGENTS.md` and Skills own durable engineering rules; execution/audit cards must reference those authorities rather than restate them.
- `agent-handoff` carries authority references, fresh delta, bounded action focus, and a return contract; it must not copy whole control files by default.
- `execution-orchestrator` owns task decomposition, subagent/parallel/model policy, and ephemeral recovery/ledger behavior. Parallel readers are preferred; overlapping writers require proven disjoint authority/workspaces.
- No silent model escalation. Agent/model selection must be explicit or remain within an allowed bounded fallback policy.
- `evidence-audit` owns independent implementation/PR/CI/merge evidence evaluation, but it does not authorize fixes or mutate source in read-only audit mode.
- `solution-design` is conditional for materially ambiguous or cross-boundary design work; simple clear changes must not acquire mandatory brainstorming/spec overhead.
- External projects are conceptual references only; no external runtime dependency is introduced.

## Verification level

`V2 — cross-Skill governance/routing behavior`.

Required evidence:

- exactly seven intended top-level Skill directories;
- valid `SKILL.md` frontmatter/name/description for all new Skills;
- routing references resolve and ownership boundaries are internally consistent;
- global routing/adoption material names the correct Skills and return paths without duplicating full procedures;
- repository rules and README no longer assert a three-Skill model;
- plugin metadata reflects the new capability set without changing the already-published v0.5.5 release workflow;
- diff audit finds no second task/status authority, mandatory universal TDD gate, unconditional subagent dispatch, or silent high-model escalation;
- final Control Alignment Gate completed for this branch handoff.

## Acceptance criteria

- Four new Skills exist and are independently discoverable by trigger.
- Project Governance remains the normal project/repository entry and authority/lifecycle owner rather than becoming an orchestration/audit monolith.
- Web-to-local and local-to-Web handoff semantics are explicitly defined, including compact request and receipt contracts.
- External-reference findings are recorded with clear adopt/adapt/reject decisions.
- The source branch passes final routing/content/diff audit and is suitable for a subsequent local Plugin/runtime validation task.

## STOP conditions

Stop state-changing work if:

- live `main` changes in an implementation-relevant way that invalidates this task's source assumptions;
- the seven-Skill split produces overlapping ownership that cannot be resolved without a materially different capability model;
- a proposed external concept would require a runtime/daemon/database/enforcement system outside repository purpose;
- unknown or conflicting source state makes safe remote mutation ambiguous.

## Handoff expectation

At final remote handoff report:

- start/final branch identity;
- changed paths;
- external references used and what was adopted/adapted/rejected;
- source/routing verification result;
- PR state if created;
- unresolved items for local Plugin/runtime acceptance;
- `RELATED_DOCUMENT`, `DOCUMENT_ALIGNMENT`, `CURRENT_STATUS_RECONCILIATION`, `CURRENT_TASK_RECONCILIATION`, and `CONTROL_ALIGNMENT`.
