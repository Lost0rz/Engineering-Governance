# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Released baseline

- Latest published Plugin remains `0.3.0`.
- Release tag: `plugin-v0.3.0`.
- Accepted release/source SHA: `d11ed12bfdac4c8ff22d37961753190a400358da`.
- Published asset SHA-256: `c60dcf4860701e394f308ccaf293cc348166008b6e198fcb29e6e08bf5ebf400`.
- Published capability set remains exactly three top-level Skills: `project-governance`, `domain-navigation`, and `incident-doctor`.

## v0.4.0 candidate

- Task: `EG-GLOBAL-ROUTING-V0.4.0-042`.
- State: `READY_FOR_MERGE`.
- Start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Final audited reusable source before this control-only release handoff: `0a00ebf1a5ebe17163431fa099249b8e2fc70a22`.
- Task branch: `codex/global-routing-v0.4.0`.
- Pull request: #14, Draft / Open / Unmerged at the time of this handoff.
- Candidate package metadata: `0.4.0`.
- No Plugin v0.4.0 GitHub Release has yet been published.
- Live `main` remained at the authorized start revision through the final reusable-source audit.

## Accepted v0.4.0 capabilities

1. **Global Skill routing** — Project Governance is the normal route for project/repository engineering work, including simple low-risk edits while keeping procedure lightweight; Domain Navigation is conditional for unclear semantic/source routes; Incident Doctor remains reactive and evidence-gated.
2. **Agent-mediated adoption/upgrade** — installation is complete only when all three Skills resolve and exactly one current managed global routing block is present; repeated adoption is idempotent and unrelated global rules are preserved.
3. **Control identity semantics** — provenance/transition parents, current-control heads, explicit locked/execution heads, and remote freshness are distinct; historical parent inequality is not automatically current-head drift.
4. **Workspace lifecycle prevention** — task-relevant workspaces are checked at bounded lifecycle transitions during normal development; local/remote branch, registration/path, HEAD, unique-work state, write capability, and overlapping authority remain separate facts; full historical reconciliation is exceptional.
5. **Construction-time code structure** — module/file boundaries follow Domain/capability/responsibility/authority/lifecycle/reason-to-change, not line count or edit size. The final pre-release audit removed the last checklist wording that could let a small edit bypass this guard.
6. **Canonical authority** — one authority per fact/state/behavior class; multiple consumer surfaces may delegate to it, but parallel writers require reconciliation or an explicit migration boundary.
7. **Verification cadence** — `V0`–`V3` remains the only risk/scope taxonomy; construction/corrective/task/merge-release cadence is separate, and effort follows risk rather than edit count.
8. **Domain navigation** — accepted semantic maps are reused regardless of filename; an optional navigation projection is derived routing evidence rather than competing product/domain truth.

## Final pre-release audit

Multiple adversarial passes covered routing/adoption, Domain/code structure, workspace lifecycle, historical-failure regression, anti-bypass behavior, package boundary, and exact-head identity.

Material findings discovered and corrected across construction/audit:

- identity/cadence template propagation gap;
- partial-install and simple-work routing ambiguity;
- construction-time structure enforcement and edit-size bypass wording;
- bounded workspace lifecycle checkpoints needed during PR/QA/freeze/terminal/successor transitions.

The final release-preflight pass found one residual Important wording issue: the structure checklist still said `Before writing substantial new code`, which could allow a small responsibility-changing edit to bypass the guard. It was corrected at reusable source `0a00ebf1a5ebe17163431fa099249b8e2fc70a22` to make the trigger independent of line count and edit size.

After that corrective and exact-source re-read, no remaining Critical or Important issue was found.

## Verification posture

`V0 + multi-pass semantic/adversarial audit` is the accepted level for the governance contracts/templates and Plugin metadata. No executable product runtime changed. Package verification and publication evidence will be produced by a separate exact-source release task and one-shot publisher.

## Next milestone

Merge PR #14 using expected-head protection after a final control-only seal check. Then open a separate Plugin v0.4.0 release task from the exact merged source, publish `plugin-v0.4.0`, verify tag/asset/hash/package contents, and only after publication proceed to local reinstallation and real routing acceptance.
