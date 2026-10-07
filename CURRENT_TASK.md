# CURRENT TASK — Doctor Foundation Implementation Plan

Task ID: `EG-V01-DOCTOR-FOUNDATION-PLAN-003`

State: `CLOSED — PLAN_ACCEPTED`

Mode: `IMPLEMENTATION_PLAN_ACCEPTED`

## Result

The first-slice Doctor implementation plan is accepted after independent Web re-review.

- Accepted plan content head: `1aa9f4b0e42e73d7e0433fe4c0297b1b0e5eea61`.
- Plan: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`.
- PR #3 remains OPEN / DRAFT / UNMERGED and stacked on `codex/eg-v01-tooling-design`.
- No unresolved BLOCKER or MAJOR remains in the plan.

## Accepted execution contract

- Four implementation tasks use genuine RED → GREEN TDD in order.
- Task 5 is verification-only and creates no implementation commit.
- Task 2 owns local Git identity and the exact read-only subprocess contract, including allowlist, `shell=False`, bounded timeout, environment flags, and timeout-to-`DoctorStop` behavior.
- Task 3 owns root control-file observation and deterministic Task ID boundary semantics.
- Task 4 owns Doctor orchestration, exit `0` / `2` / `3`, no-mutation snapshots, and timeout-to-exit-2 proof.
- First slice is macOS Apple silicon, Python 3.11+, standard-library-only, local/offline, read-only.
- No CLI packaging, Bootstrap, deep Audit, AI contribution runtime, remote query, MCP, daemon, enforcement, migration, remediation, or pilot changes are included.

## Closeout

This plan task is closed. Do not create source/tests/fixtures or execute implementation under this task ID.

The next authorized stage must use a separate implementation task and branch based on this accepted plan. The implementation task must load the accepted spec and plan, use `superpowers:test-driven-development`, and execute the plan task-by-task without scope expansion.

PR #3 must remain Draft / unmerged unless the user separately authorizes merge.
