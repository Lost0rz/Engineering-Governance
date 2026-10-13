# Project Agent Guidance

Derive this durable guidance from verified target-repository evidence and accepted decisions. Keep unknowns explicit as `unknown` or `not established`. Do not invent project facts, commands, authority, or workflow.

## Project purpose and durable boundaries

[Record the verified project purpose, stable boundaries, and accepted constraints. Do not put current task progress here.]

## Project truth and authoritative entry points

[Point to verified sources for product, domain, data, runtime, repository, and durable planning facts. Preserve one owner per fact class; link to authorities instead of copying their detailed content.]

## Durable planning authority

[Record the project's accepted location/authority for long-lived design and multi-task or large-PR planning when one exists. Reuse an existing architecture/product/design authority rather than inventing `documents/` merely for convention. When no accepted location exists and durable planning is justified, `documents/**` is the default pattern. Durable planning documents own rationale/design/work-package structure, not current task authorization or live progress. `CURRENT_TASK.md` may link to a bounded planning section; `CURRENT_STATUS.md` may summarize the current planning position. Omit or state `not established` when the project has no durable planning need.]

## Domain and navigation authorities

[Link to accepted business/product/domain/capability authorities already present in the project and, only when it adds durable routing value, any derived navigation projection. A literal `DOMAIN_MAP.md` is not required. Keep unclear ownership `unknown` rather than inferring it from directory names.]

## Global routing boundary

[Do not copy the Engineering Governance global managed routing block into this project file by default. Global routing selects reusable Skills; this file owns repository-specific durable rules. Record only project-specific routing exceptions or constraints that are actually verified and needed here.]

## Normal development flow

[Describe durable repository-specific workflow rules supported by current evidence. Do not copy the active task or current progress from `CURRENT_TASK.md` or `CURRENT_STATUS.md`. Record that governed state-changing work must run a final Control Alignment Gate before successful handoff: reread current status/task and any materially affected linked planning document, update only sources whose owned semantics changed, and explicitly report document/status/task alignment. The check is mandatory; writes are conditional. Routine external evidence such as CI/review/audit does not force a write when no owned semantic changed. Strict read-only work reports stale alignment without mutating controls. If the project uses Git, branches, worktrees, or multiple checkouts, record only the verified lifecycle/freshness rules it actually needs: non-destructive handling of unknown local work, bounded task-relevant pre-task workspace classification, overlapping-write-authority/predecessor rules, retained-workspace write-capability and release conditions, project-defined terminal closeout expectations, and what baseline/control/workspace drift requires a stop. Distinguish literal Repository HEAD from Delivery / Semantic HEAD when implementation freshness matters: by default only `CURRENT_STATUS.md` and `CURRENT_TASK.md` are excluded from delivery identity, while their content remains authoritative for owned control semantics. Planning documents and `AGENTS.md` are not part of that default exclusion. Distinguish provenance/transition/planning revision bases from explicit semantic or literal current/locked-head equality gates. Keep repository-host gates separate from semantic implementation identity: required checks/reviews, current mergeability/conflicts, merge queue, current-base/latest-head rules, or similar host requirements remain live for the literal identity the repository host governs. A broad Domain/capability label alone should not create an automatic writer lock, and unrelated historical workspaces should not require routine full classification unless the active decision or an explicit legacy-reconciliation task requires it. Do not impose worktrees on projects that do not use them. For project-controlled durable development state, use the canonical project location as the default storage authority; record a different path/authority here only when the project has an explicit durable exception that actually needs to override that default. Do not require a separate storage manifest just to restate the default.]

## Doctor on demand

[State the verified boundary for incident diagnosis: use it only for a real blocked problem when existing evidence is insufficient.]

## Verification policy

[Describe the repository's evidence-based `V0`–`V3` policy and any repository-specific verification cadence. Preserve the principle that verification effort follows change risk, not change count: use focused checks during construction, group related acceptance findings into a bounded corrective where practical, and run broader affected regression at justified corrective/task/merge boundaries. Keep current task checks in `CURRENT_TASK.md`. When CI/review/audit evidence is bound to an implementation identity, allow reuse across `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only Repository HEAD advances when semantic-tree equivalence is proven and no task-owned condition invalidates the evidence. Before merge/release, separately read current repository-host gate state and do not infer host-gate PASS from semantic equivalence or an older commit's host state.]

## Project-specific commands

[Include only commands verified in this target repository and needed for safe work. Omit this section when no command is established; never guess a command.]

## Stop conditions

[List evidence, authority, baseline, planning-context, workspace, or safety conditions that require stopping and identify what verified input is needed to continue. In source-controlled projects, unknown unique work, a task-relevant predecessor that can still write an overlapping authority, a failed explicit semantic/literal head lock, task-relevant authority/baseline drift, a linked-plan change that materially invalidates active task authorization, and an unsatisfied required live repository-host gate are stop conditions unless the repository's accepted workflow explicitly resolves them without data loss or parallel writers. Do not stop merely because a historical transition/planning revision basis differs from a verified later revision, or because Repository HEAD advanced only through `CURRENT_STATUS.md` / `CURRENT_TASK.md`, when no applicable equality lock or material task-content change exists.]
