# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Published Plugin v0.2.0

- GitHub Release `plugin-v0.2.0` remains the published release.
- Package version: `0.2.0`.
- Exact release/source SHA: `cf2df83e7e6bde39a5cce7f51e47d59e3911d71c`.
- Release asset SHA-256: `99ab0679c5692dd382d515cf39a92c6fb1e9c68ae119c43637b3cec65b19436e`.
- The published v0.2.0 artifact does not include the workspace-lifecycle work from tasks 039/040. Publishing those accepted repository changes remains a separate future task.

## Accepted repository main

- Task `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-CORRECTIVE-040` merged through PR #12.
- Merge commit: `4fe236b91295fe4594c4d5932da8375086a7648d`.
- Merged tree: `8b0f15dbe15164bcf40d45661c6881955b6f90f9`, exactly matching final PR-head tree.
- `project-governance` now has the corrected workspace lifecycle semantics: bounded task-relevant classification, overlapping-authority writer gating, retained write-capability handling, and project-defined terminal-event semantics.
- `skills/project-governance/references/workspace-lifecycle.md` is the canonical detailed lifecycle authority.
- No new top-level Skill, runtime, CLI, daemon, database, hook, installer, automatic cleanup/remediation, or Plugin publication was added.

## Current task

- Task: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-CORRECTIVE-040`.
- State: `CLOSED`.
- Outcome: `MERGED_VERIFIED`.
- PR: #12, merged 2026-10-09.
- Final PR head: `77c0f3c4ae68472a09386a22573a8d8e15b5ba2e`.
- Merge commit: `4fe236b91295fe4594c4d5932da8375086a7648d`.
- Post-merge audit: PASS; comparing final PR head to merge commit shows one merge commit and zero file differences.
- Main `workspace-lifecycle.md` blob: `832b1a46085968b6b340f03f78d0e4fc6920ed94`.
- Main `project-governance/SKILL.md` blob: `b98e62a60e95ff570d2261ae0dc872e94fc26059`.
- Remote 040 task branch remains present because the available GitHub connector exposes no branch-ref deletion action. It is fully merged and no longer authorizes writes. No local worktree-cleanliness/removal claim is made by this remote-only task.

## Next milestone

Use the corrected lifecycle contract in governed projects. Any Plugin release (recommended as a separate versioned release task), further reusable Skill enhancement, or physical branch cleanup beyond available verified tooling requires a separately authorized task/action.
