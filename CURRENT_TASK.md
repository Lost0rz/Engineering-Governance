# CURRENT TASK — Doctor Foundation Plan Review Handoff

Task ID: `EG-V01-DOCTOR-FOUNDATION-PLAN-003`

State: `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`

Mode: `PLAN_REVIEW_HANDOFF`

## Objective

Submit the final corrected first-slice Doctor implementation plan for independent review. This handoff authorizes no implementation.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Branch: `codex/eg-v01-doctor-foundation-plan`.
- Corrective control start HEAD: `3e1ef69bfeff86360a18f0d7e54e2ebe3ad23ea4`.
- Accepted design control head: `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`.
- Accepted spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Plan: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`.
- PR #3 remains OPEN / DRAFT / UNMERGED, stacked on `codex/eg-v01-tooling-design`.

## Final corrective result

- Task 4 adds its `DoctorMutationSnapshot` and `snapshot_doctor_mutation_state` in `tests/support.py`, and that file is listed in Task 4 Files and commit. Task 2 adds only its temporary Git repository helper; Task 3 adds its fixture materializer. Task 4's RED is absent `run_doctor`, not absent support.
- Task 2 has named tests for the actual `subprocess.run` adapter, including exact local argv/cwd, `shell=False`, bounded timeout, environment flags and preserved `PATH`/`HOME`, captured UTF-8 text and `CommandResult`; timeout raises `DoctorStop` once without retry. Task 4 pins root identity timeout to exit `2`, no report, and no evaluation result.
- The prior three findings remain resolved: genuine TDD ordering, exact named-test surface, and deterministic Task ID boundary semantics.
- The plan preserves four implementation tasks, a verification-only gate, the first local/offline/read-only slice, Python 3.11+/stdlib-only, and the existing exit `0` / `2` / `3` contract. Accepted spec and `EngineeringGovernanceStandard 0.1.0` are unchanged.

## Scope and exclusions

Only the plan and the two control-plane files are changed. No source, tests, fixtures, manifests, schemas, CLI, Bootstrap, deep Audit, AI runtime, remote query, MCP, daemon, enforcement, migration, remediation, or pilot changes are authorized. Implementation requires independent plan review and a separate implementation task.

## Validation and handoff

- Plan self-review covers exact future file map versus each task Files/commit boundary, staged helper ownership, genuine RED causes, adapter/timeout assertions, first-slice scope, interfaces, review focus, and task proportion.
- `git diff --check` is required; no implementation tests are run because this is plan-only.
- Commit and push the authorized plan/control changes to this branch; verify local HEAD equals the live remote branch HEAD, the worktree is clean, and PR #3 remains OPEN / DRAFT / UNMERGED.
- Next action: independent Web re-review. Stop at `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`.
