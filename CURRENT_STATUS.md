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
- State: `READY_FOR_INSTALLATION_ACCEPTANCE`.
- Start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Sealed audited source before this status-only seal: `a1c737deb50628762e4f1326a8afce0c97dca96b`.
- Task branch: `codex/global-routing-v0.4.0`.
- Pull request: #14, Draft / Open / Unmerged.
- Candidate package metadata: `0.4.0`.
- This is a source candidate only; no Plugin v0.4.0 GitHub Release has been published.
- Live `main` remained at the authorized start revision through the final exact-head audit.

## Implemented capability changes

1. **Global Skill routing** — Project Governance is the normal route for project/repository engineering work, including simple low-risk edits while keeping procedure lightweight; Domain Navigation is conditional for unclear semantic/source routes; Incident Doctor remains reactive and evidence-gated.
2. **Agent-mediated adoption/upgrade** — the Plugin payload carries an exact marker-bounded global `AGENTS.md` routing template plus an idempotent adoption contract. Installation is complete only when all three Skills are available and exactly one current global routing block is verified.
3. **Control identity semantics** — provenance/transition parents, current-control heads, explicit locked/execution heads, and remote freshness are separate identity classes. Relationship checks are not silently converted into equality checks.
4. **Workspace lifecycle prevention** — local branch, remote branch, worktree registration, filesystem path, HEAD, working-tree/unique-work state, write capability, and overlapping authority are separate facts. Bounded lifecycle checkpoints run during normal development at workspace selection, successor-writer decisions, retained-state transitions, terminal events, and before overlapping next tasks; historical full reconciliation is exceptional.
5. **Construction-time code structure** — file/module organization is governed by Domain/capability/responsibility/authority/lifecycle/reason-to-change boundaries, never by a universal line-count threshold. A new responsibility boundary is established while code is being written rather than deferred to final cleanup; cohesive large files are not split mechanically.
6. **Verification cadence** — `V0`–`V3` remains the sole risk/scope taxonomy; construction/corrective/task/merge-release cadence is separate. Verification effort follows change risk, not change count.
7. **Domain navigation** — existing semantic business/product/domain/capability maps are reused as authorities regardless of filename; an optional navigation projection is derived and does not duplicate product/domain truth.
8. **Project templates** — `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` carry routing-boundary, control-identity, workspace-identity, and cadence semantics without copying full reusable contracts.

## Multi-pass audit outcome

Five audit passes were run against the PR/source, including routing/adoption, Domain/code-structure, workspace lifecycle, historical failure regression, and anti-bypass/exact-head review.

Four material issue categories were found across construction plus audit and corrected:

- template propagation of identity/cadence;
- installation completion + simple-work default routing;
- proactive construction-time structure enforcement, including removal of edit-size as a possible bypass;
- proactive bounded workspace lifecycle checkpoints so closeout is not deferred into later archaeology.

After the corrective passes, no remaining Critical or Important issue was found.

## Core regression results

- Large-file handling is responsibility-driven, not line-count driven: PASS.
- Structure checks occur during construction when a new responsibility/authority boundary is introduced: PASS.
- Existing Domain/semantic maps route code ownership/source/test discovery without requiring duplicate map files: PASS.
- Stale/retained worktree handling occurs at bounded lifecycle checkpoints during development: PASS.
- Unrelated historical worktrees do not trigger routine full archaeology: PASS.
- Explicit one-time legacy reconciliation remains available for repositories that already accumulated ambiguous workspace debt: PASS.
- Single canonical authority / no parallel writer principle remains enforced: PASS.
- Historical control-parent false STOP is guarded while explicit locked-head equality remains hard: PASS.
- Verification effort follows risk, not edit count: PASS.
- Incident Doctor remains evidence-gated and does not become a routine diagnostics program: PASS.
- Global routing remains selection-only and does not duplicate Skill procedures into global `AGENTS.md`: PASS.

## Review-independence boundary

The audit was performed as a separate adversarial review pass over exact PR source and did not rely on implementation claims. The same ChatGPT conversation also authored corrective commits, so separate-actor/separate-model independence is not claimed. The user authorized this multi-pass audit as the pre-installation gate; strict external reviewer identity can remain an optional merge gate.

## Verification posture

`V0 + multi-pass semantic/adversarial audit` is the accepted level for this documentation/contract/package-metadata task. No executable product runtime changed and the sealed candidate HEAD has no CI/status checks, so no runtime/build/CI PASS is claimed.

## Next milestone

Proceed to real installation acceptance of Plugin v0.4.0 + managed global routing in a controlled target environment while PR #14 remains Draft/unmerged. Merge and publication remain separate decisions after installation evidence.
