# Project Agent Guidance

Derive this durable guidance from verified target-repository evidence and accepted decisions. Keep unknowns explicit as `unknown` or `not established`. Do not invent project facts, commands, authority, or workflow.

## Project purpose and durable boundaries

[Record the verified project purpose, stable boundaries, and accepted constraints. Do not put current task progress here.]

## Project truth and authoritative entry points

[Point to verified sources for product, domain, data, runtime, and repository facts. Preserve one owner per fact class; link to authorities instead of copying their detailed content.]

## Domain and navigation authorities

[Link to accepted business/product/domain/capability authorities already present in the project and, only when it adds durable routing value, any derived navigation projection. A literal `DOMAIN_MAP.md` is not required. Keep unclear ownership `unknown` rather than inferring it from directory names.]

## Global routing boundary

[Do not copy the Engineering Governance global managed routing block into this project file by default. Global routing selects reusable Skills; this file owns repository-specific durable rules. Record only project-specific routing exceptions or constraints that are actually verified and needed here.]

## Normal development flow

[Describe durable repository-specific workflow rules supported by current evidence. Do not copy the active task or current progress from `CURRENT_TASK.md` or `CURRENT_STATUS.md`. If the project uses Git, branches, worktrees, or multiple checkouts, record only the verified lifecycle/freshness rules it actually needs: non-destructive handling of unknown local work, bounded task-relevant pre-task workspace classification, overlapping-write-authority/predecessor rules, retained-workspace write-capability and release conditions, project-defined terminal closeout expectations, and what baseline/control/workspace drift requires a stop. Distinguish provenance/transition parents from explicit current/locked-head equality gates. A broad Domain/capability label alone should not create an automatic writer lock, and unrelated historical workspaces should not require routine full classification unless the active decision or an explicit legacy-reconciliation task requires it. Do not impose worktrees on projects that do not use them. For project-controlled durable development state, use the canonical project location as the default storage authority; record a different path/authority here only when the project has an explicit durable exception that actually needs to override that default. Do not require a separate storage manifest just to restate the default.]

## Doctor on demand

[State the verified boundary for incident diagnosis: use it only for a real blocked problem when existing evidence is insufficient.]

## Verification policy

[Describe the repository's evidence-based `V0`–`V3` policy and any repository-specific verification cadence. Preserve the principle that verification effort follows change risk, not change count: use focused checks during construction, group related acceptance findings into a bounded corrective where practical, and run broader affected regression at justified corrective/task/merge boundaries. Keep current task checks in `CURRENT_TASK.md`.]

## Project-specific commands

[Include only commands verified in this target repository and needed for safe work. Omit this section when no command is established; never guess a command.]

## Stop conditions

[List evidence, authority, baseline, workspace, or safety conditions that require stopping and identify what verified input is needed to continue. In source-controlled projects, unknown unique work, a task-relevant predecessor that can still write an overlapping authority, a failed explicit head lock, and task-relevant authority/baseline drift are stop conditions unless the repository's accepted workflow explicitly resolves them without data loss or parallel writers. Do not stop merely because a historical transition parent differs from the verified current control head when no equality lock was declared.]
