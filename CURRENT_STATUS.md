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
- State: `WAITING_FOR_INDEPENDENT_AUDIT`.
- Start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Task branch: `codex/global-routing-v0.4.0`.
- Candidate package metadata: `0.4.0`.
- This is a source candidate only; no Plugin v0.4.0 GitHub Release has been published.
- `main` remained at the authorized start revision during construction and author self-audit.

## Implemented capability changes

1. **Global Skill routing** — Project Governance is now the normal route for project/repository engineering work; Domain Navigation is conditional for unclear semantic/source routes; Incident Doctor remains reactive and evidence-gated.
2. **Agent-mediated adoption/upgrade** — the Plugin payload now carries an exact marker-bounded global `AGENTS.md` routing template plus an idempotent adoption contract. Installation is complete only when all three Skills are available and exactly one current global routing block is verified.
3. **Control identity semantics** — provenance/transition parents, current-control heads, explicit locked/execution heads, and remote freshness are separate identity classes. Relationship checks are no longer silently converted into equality checks.
4. **Workspace identity semantics** — local branch, remote branch, worktree registration, filesystem path, HEAD, working-tree/unique-work state, write capability, and overlapping authority are verified as separate facts.
5. **Verification cadence** — `V0`–`V3` remains the sole risk/scope taxonomy; construction/corrective/task/merge-release cadence is separate. Verification effort follows change risk, not change count.
6. **Project templates** — `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` templates now carry the new routing boundary, control-identity, workspace-identity, and cadence semantics without copying the full reusable contracts.

## Author self-audit

A detailed remote exact-source self-audit was performed during construction. It found and corrected two material design-propagation issues before handoff:

- **Important — template propagation gap:** reusable control-identity/cadence rules were initially absent from `CURRENT_TASK.md`/`CURRENT_STATUS.md` templates. Corrected.
- **Important — installation/default-route gap:** the initial adoption text did not bind Skill availability and global routing adoption into one installation-completion gate, and the first routing wording allowed simple repository work to bypass Project Governance. Corrected.

After corrective changes:

- top-level Skill directory count remains exactly three;
- routing/adoption files are inside `skills/**` and therefore inside the established Plugin payload boundary;
- the managed global block contains one BEGIN/END marker pair and names the three expected Skills;
- no Router Skill, installer executable, Bootstrap CLI, daemon, hook, MCP service, background runtime, or automatic remediation was added;
- the historical-control-parent false-positive case is explicitly guarded while explicit locked-head equality remains a hard gate;
- no competing L1–L4 validation taxonomy was introduced.

Because the same remote session authored the changes and performed this self-audit, the self-audit is not represented as independent review.

## Verification posture

`V0 + semantic scenario audit` is the accepted level for this documentation/contract/package-metadata task. No executable product runtime changed, so no runtime/build test claim is made. Final handoff requires an exact-PR-head diff/path/link/semantic check and explicit disclosure that independent reviewer evidence is still absent unless a separate reviewer performs it.

## Next milestone

Open the v0.4.0 candidate PR against `main`, verify its exact final head, and obtain an independent merge decision. A separate task is required to publish Plugin v0.4.0 and to apply the new installation/adoption contract to target environments/projects.
