# Repository enrollment — historical FILE_CONTROL to global ISSUE_CONTROL

The installed Engineering Governance CONTROL_POLICY_V1 owns the generic workflow and mode selection. Target repository AGENTS.md contains **only project-specific business, architecture, data and runtime safety**; it must not contain CONTROL_MODE, ISSUE_APPROVERS, ISSUE_WEB_SPEC_AUTHORING, ISSUE_DELEGATED_APPROVAL or RISK_SCOPED_AUTONOMY declarations.

## Trust and compatibility boundary

- Installing or updating the plugin does **not** migrate an existing project. Unknown or unverified repositories remain on historical FILE_CONTROL and do not gain implicit write permissions.
- A migrated repository is enrolled through an actual **merged GitHub migration PR** whose merge commit is verified in the current main ancestry by live host readback. The migration PR locator is a global user-routing preference, **not** authority by itself. The bundled `scripts/control-policy.py` exposes a read-only `verify_migration` adapter via authenticated local `gh api`; Web must perform equivalent live GitHub connector checks. Missing host capability is STOP, never a guessed PASS.
- A versioned plugin policy file defines generic defaults. Authenticated approvers and repo/organization trust are derived from independent user/host identity/permission evidence, never from target AGENTS.md or an AI-authored comment. Direct Issue approval, checked against current digest/revocation, remains a **separate** prerequisite for source writes.
- Delegated approval and G1/G2 autonomy remain disabled unless separately authorized through trusted global user/host channels; source-policy tests or project markdown cannot activate them.
- A local user routing file may hold repository and migration-PR **locators** for convenience. It must not be treated as signed host evidence or an approver grant. ChatGPT Web cannot read local Mac configuration unless a supported connection makes it accessible and authenticated.

## Per-repository adoption process

1. Read current project AGENTS for project constraints, Task/Status when historical FILE_CONTROL is active, open Issue/PR state, main SHA and overlapping writers. Keep unrelated work and business/data facts intact.
2. Under the **current** authorized mode, prepare each still-executable task's exact Issue spec, keep its current boundaries and obtain independent exact-revision GitHub approval. Do not backfill historical closed tasks or invent approval.
3. In one approved migration PR, remove any existing generic governance selectors from project AGENTS and remove stale Task/Status from *live* authority only after every continuing task has an accepted handoff. Update repository-owned scripts that incorrectly require the old selectors.
4. Verify that migration PR is actually merged into the target repository main; use live GitHub PR merge SHA and commit ancestry. Only **after** this cutover may the global policy select ISSUE_CONTROL for that repository.
5. Verify local gh capabilities separately from Web connector permissions, the installed plugin version in Web/Codex/Claude, and the selected approved Issue. Reuse active branches/worktrees when safe.
6. Do not activate G1/G2 autonomy through migration; do not edit project business rules merely to fit the plugin.

## Failure and rollback

If PR merge, main ancestry, current task approval, user/host identity, local writer safety or permission evidence is unknown, retain the previous authorized mode and STOP any write dependent on migration. A caller-supplied merged boolean or a local policy snapshot is not host proof. A reversed migration requires a new authorized transition, preserving the old branch, Issue approvals and unique work. Never infer success from deleting AGENTS fields, installing Skills, or a green selector with tests skipped.
