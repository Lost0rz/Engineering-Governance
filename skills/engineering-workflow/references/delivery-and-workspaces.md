# Delivery, workspaces, optional Issues, and plugin adoption

## 1. Workspaces and canonical ownership

- **Reuse first:** continue in the existing safe branch, checkout, or PR for an ongoing objective. Do not create a new branch, Git worktree, or PR solely because a session restarted, a correction was found, or a Sub Agent was used.
- **Protect unique local work:** inspect `git status` and target refs before switching, merging, or deleting worktrees; a remote PR merge proves neither a clean local checkout nor safe deletion.
- **Canonical writer (SSOT):** locate the existing module, service, schema, or API owner and extend it cohesively rather than creating duplicate state or racing writers.

## 2. Optional Issue collaboration & remote delivery

- **Issues are shared plans, never credentials:** any agent with trusted user intent and GitHub Issue permissions may create or update an Issue using [task-plan.md](../../../.github/ISSUE_TEMPLATE/task-plan.md) or blank Issues. No privileged author, approval comment, or digest hash is required.
- **Local commit != remote delivery:** before claiming a push or PR update, push only the authorized branch and verify remote ref readback (`PUSHED_VERIFIED`). Report `NOT_REQUIRED_LOCAL_ONLY` or `NOT_APPLICABLE_NO_REMOTE` when no remote publication applies.
- **Separate gates:** local unit checks, PR mergeability/required CI checks, package builds, and installed host runtime are distinct claims. Never infer remote CI `PASS` from local edits.

## 3. Standard toggleable plugin adoption across hosts

Build a deterministic, symlink-safe runtime plugin package or standalone directory from the source repository using `scripts/package-plugin.py`:

- **Antigravity:** place under `plugins/engineering-governance/` or declare in `plugins.json`, then toggle cleanly via the Settings UI or `agy plugin enable|disable engineering-governance`. You can also mount individual Skills via `skills.json` (`include_only`).
- **Codex / Claude Code:** install via `.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json`, or `.claude-plugin/plugin.json` and manage via host plugin toggles.
- **Project `AGENTS.md`:** keep project-specific product, architecture, data-safety, and test commands in each target repo's `AGENTS.md` (see [AGENTS.md template](../assets/templates/AGENTS.md)), without duplicating generic plugin routing rules.

## 4. Artifact ownership summary

| Surface | Owns | Refresh rule |
| --- | --- | --- |
| Source, schema, config | Implemented behavior | Updated directly by authorized edits |
| `AGENTS.md` | Project-specific constraints | Updated only when project constraints change |
| Issue / PR / CI | Plan context, diff, remote checks | Owned by GitHub host; no status-only commits |
| `PROJECT_PROFILE.md` / `DOMAIN_MAP.md` | Derived orientation leads | Refresh only affected stale entries when needed |
