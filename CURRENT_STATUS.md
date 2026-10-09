# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Released baseline

- Latest published Plugin remains `0.3.0`.
- Release tag: `plugin-v0.3.0`.
- Accepted release/source SHA: `d11ed12bfdac4c8ff22d37961753190a400358da`.
- Published asset SHA-256: `c60dcf4860701e394f308ccaf293cc348166008b6e198fcb29e6e08bf5ebf400`.
- Published capability set remains exactly three top-level Skills: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Current development task

- Task: `EG-GLOBAL-ROUTING-V0.4.0-042`.
- State: `ACTIVE`.
- Start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Task branch: `codex/global-routing-v0.4.0`.
- Goal: produce a v0.4.0 source candidate that adds global Skill routing/adoption semantics and folds verified v0.3.0 pilot corrections into Project Governance.
- This task is source evolution only. No Plugin v0.4.0 GitHub Release or target-project installation is authorized here.

## Verified motivation

v0.3.0 application established three follow-up needs:

1. The three Skills contain their own triggers, but the shipped model lacks a reusable global `AGENTS.md` routing contract that tells an agent which Skill to invoke before the Skill has already been selected.
2. A pilot produced a false `STOP_CONTROL_HEAD_DRIFT` when a recorded control parent was treated as the required current HEAD; the corrected evidence showed the parent was provenance for a control transition. Project Governance must distinguish provenance/transition anchors from explicit current/locked-head requirements.
3. Verification needs an explicit cadence rule in addition to `V0`–`V3`: construction should use focused checks appropriate to risk, while broader regression/CI belongs at justified corrective/task/merge boundaries rather than after every small acceptance correction.

## Design direction

- Keep exactly three Skills; do not create a Router Skill.
- `project-governance` is the normal engineering entry point.
- `domain-navigation` is conditional when semantic/source ownership or route is unclear.
- `incident-doctor` is reactive and evidence-gated for a real blocking failure with insufficient evidence.
- Ship the routing/adoption contract and managed global-`AGENTS.md` block template inside `skills/**` so the existing Plugin payload can carry them.
- Adoption remains agent-mediated and non-destructive; no installer runtime, daemon, hook, MCP service, or automatic remediation is introduced.
- Preserve project-local governance ownership: global routing selects Skills; project `AGENTS.md` describes that repository; Skill references own reusable workflow detail.

## Verification posture

This is a documentation/contract/package-metadata change, so the active task uses `V0 + semantic scenario audit`. The final branch must be checked for exact diff scope, link/frontmatter/layout consistency, three-Skill packaging shape, routing/adoption scenario coverage, control-identity semantics, verification-cadence consistency, and duplication/conflict across authorities.

## Next milestone

Complete the v0.4.0 candidate on the task branch, create a reviewable PR, and perform a detailed exact-head remote audit before any merge or release decision.
