# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release is `plugin-v0.5.4`.

- Release title: `Engineering Governance Plugin v0.5.4`
- Frozen publication source: `3e028cdbe21e9637cbf7bf9b00a5664d44c272c0`
- GitHub Actions run: `38346638985` — `success`
- Release asset: `engineering-governance-plugin.zip`
- Asset size: `64200` bytes
- SHA-256: `2a39d1bf705b56b53f2514b5bb8012380606278989afabdc4f3c7424dd0f0367`
- Package file entries: `29`
- Included top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

## Accepted v0.5.4 governance and distribution state

- Accepted governance semantics from PR #18 are merged at `999c649e499f69bffe7bf870f38e953a0abd59af`.
- Portable root `plugin.json` version `0.5.4` was integrated by PR #19 at `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- Repo-backed `engineering-governance-personal` marketplace was integrated by PR #20 at `6185a1be962956422b7e4eeb56727ccb9a9386fa`.
- ChatGPT Web Plugin is `0.5.4` with exactly three top-level Skills.
- Mac mini and MacBook Air are independently verified on one active `engineering-governance@engineering-governance-personal / 0.5.4` authority each.
- The 0.5.4 payload contains `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and the separate repository-host gate boundary.

## Current planning context

- Planning document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Current work package: Task 058 reusable Project Governance contract and template update.
- Current task: `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058`.
- Task branch: `codex/planning-doc-control-alignment-v055`.

## Active development state

Task `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058` is active in source construction.

The task addresses two linked governance gaps:

1. durable large-plan/design context has no formal reusable relationship to the active Task/Status controls;
2. current lazy/batched lifecycle reconciliation can leave status/task semantics stale across cross-session or cross-machine handoff because final control alignment is not mandatory.

The accepted design keeps `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` as the three-file control plane, introduces durable planning documents only when justified, and makes end-of-execution alignment checking mandatory while keeping control writes conditional.

## Active problems and blockers

No implementation blocker is currently known. The source contract still requires construction and independent audit before any Plugin `0.5.5` version/distribution work.

## Next intended milestone

Complete Task 058 source construction and V0 scenario audit, then open a Draft PR for independent Web audit. Plugin version bump/distribution/release remains a separate later task after the source contract is accepted.
