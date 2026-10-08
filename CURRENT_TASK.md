# CURRENT TASK — InvestDesk Minimal Bounded Adoption

Task ID: `EG-INVESTDESK-BOUNDED-ADOPTION-030`

State: `WAITING_FOR_USER_MERGE_AUTHORIZATION`

Mode: `ADOPTION_AUDIT_PASSED`

## Objective

Hold the independently audited InvestDesk minimal adoption at the explicit merge-decision gate. Do not mutate the target further, merge it, or begin the real business-task trial until the user authorizes merge.

## Accepted reusable baseline

- Engineering-Governance Skill/content baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- No reusable Skill change occurred during this adoption.

## Target audit evidence

- Repository: `Lost0rz/InvestDesk`.
- Authorized / still-live target `main`: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- Branch: `codex/engineering-governance-minimal-adoption`.
- Final branch head: `26eca91e54d14a6b5ab545e6320076d4f74bc6ce`.
- Compare against `main`: ahead 5 / behind 0; merge base equals `main`.
- Changed paths: exactly `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.
- Product/test/schema/migration/dependency/business-contract/runtime changes: none.
- Added governance/domain/incident/runtime artifacts: none.

## Accepted target content

`AGENTS.md` contains only the approved bounded semantics:

1. task-relevant/conditional PR-branch-worktree verification while preserving STOP for unexplained drift and unknown dirty/unique local work;
2. `CURRENT_STATUS.md` fact-only semantics and mandatory task reconciliation when a verified fact invalidates a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary.

Target controls demonstrate stable Task ID, affected domains, exact start baseline, risk/verification rationale, acceptance criteria, consolidated STOP conditions, and handoff state.

## Merge gate

Merge is **not** authorized by this task state alone. Before any merge action, freshly verify that target `main` is still `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc` and the branch diff remains limited to the same three paths.

After explicit user merge authorization and successful closeout, the next target task should restore MVP-D Decision ↔ Transaction Traceability planning and then run the first real-business-task adoption trial.

## Current stop point

`WAITING_FOR_USER_MERGE_AUTHORIZATION`
