# Project Agent Guidance

Derive this durable guidance from verified target-repository evidence and accepted decisions. Keep unknowns explicit as `unknown` or `not established`. Do not invent project facts, commands, authority, or workflow.

## Project purpose and durable boundaries

[Record the verified project purpose, stable boundaries, and accepted constraints. Do not put current task progress here.]

## Project truth and authoritative entry points

[Point to verified sources for product, domain, data, runtime, and repository facts. Preserve one owner per fact class; link to authorities instead of copying their detailed content.]

## Domain and navigation authorities

[Link to accepted business/product/domain/capability authorities already present in the project and, only when it adds durable routing value, any derived navigation projection. A literal `DOMAIN_MAP.md` is not required. Keep unclear ownership `unknown` rather than inferring it from directory names.]

## Normal development flow

[Describe durable repository-specific workflow rules supported by current evidence. Do not copy the active task or current progress from `CURRENT_TASK.md` or `CURRENT_STATUS.md`. If the project uses Git, branches, worktrees, or multiple checkouts, record only the verified lifecycle/freshness rules it actually needs: non-destructive handling of unknown local work, bounded pre-task workspace classification, conflicting-writer/predecessor rules, explicit retention conditions, terminal closeout expectations, and what baseline/control/workspace drift requires a stop. Do not impose worktrees on projects that do not use them.]

## Doctor on demand

[State the verified boundary for incident diagnosis: use it only for a real blocked problem when existing evidence is insufficient.]

## Verification policy

[Describe the repository's evidence-based verification policy and when each applicable level is required. Keep current task checks in `CURRENT_TASK.md`.]

## Project-specific commands

[Include only commands verified in this target repository and needed for safe work. Omit this section when no command is established; never guess a command.]

## Stop conditions

[List evidence, authority, baseline, workspace, or safety conditions that require stopping and identify what verified input is needed to continue. In source-controlled projects, unknown unique work, an unresolved conflicting predecessor workspace, and task-relevant authority/baseline drift are stop conditions unless the repository's accepted workflow explicitly resolves them without data loss.]
