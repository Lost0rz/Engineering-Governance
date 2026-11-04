# CURRENT TASK — transitional FILE_CONTROL authorization for EG-093

TASK_ID: EG-ISSUE-CONTROL-MIGRATION-093
TASK_CLASS: SOURCE_GOVERNANCE_MIGRATION
STATUS: AUTHORIZED / SOURCE_CONSTRUCTION
REPOSITORY: Lost0rz/Engineering-Governance
CONTROL_MODE: FILE_CONTROL_UNTIL_CUTOVER
BRANCH: codex/issue-control-execution-contract-093
BASE_MAIN: 98ba99045984d365b58f9da970a0435c49c15fcd
ISSUE_SPEC: https://github.com/Lost0rz/Engineering-Governance/issues/40
PR: TO_BE_CREATED / DRAFT
OBJECTIVE: Adopt explicitly approved Issue-driven task authority and detailed execution/deviation/receipt/migration contracts in existing nine Skills; migrate this source repository at its own accepted main cutover.

## Scope
- Change existing relevant Governance Skills, references, templates, repository AGENTS/README, issue form and focused acceptance specification.
- Preserve FILE_CONTROL for unadopted repositories, no tenth top-level Skill, no service/daemon/model router.
- On the same implementation PR, remove this transitional CURRENT_TASK.md and CURRENT_STATUS.md only when the Issue path and AGENTS issue mode are documented and reviewable.
- No changes to downstream repositories; no Web/local plugin distribution or release before separate verified boundary.

## Authorization and safety
User explicitly authorized remote source implementation on 2026-11-04.
Read issue #40 for verified design and specific work packages; while main remains FILE_CONTROL this document provides transition execution authorization, and the Issue is planning context rather than simultaneous authority.
No direct-main commits. Preserve separate merge/host/installed acceptance. Do not merge automatically; Draft PR for review.
STOP on main/ref drift, conflicting writers, unknown unique work when relevant, or material design changes.
Risk V2 source-contract changes; review exact diff and scenario matrix.
