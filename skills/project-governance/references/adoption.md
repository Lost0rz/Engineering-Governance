# Adoption across repositories and hosts

The plugin provides reusable work methods, not remote write credentials or a new task database.

1. Package or install the intended plugin version (`scripts/package-plugin.py` produces a clean runtime directory/archive containing `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `rules/AGENTS.md`, and `skills/**`, excluding repo tests and `archive/**`).
2. Register it through the host's standard plugin mechanism so it can be toggled on/off cleanly without editing global user prompts:
   - **Antigravity**: place under a standard `plugins/engineering-governance/` root (or reference in `plugins.json`) and toggle via the Settings UI or `agy plugin enable|disable engineering-governance`. Individual specialist Skills can also be mounted selectively via `skills.json` (`include_only`).
   - **Codex / Claude Code**: install via `.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json`, or `.claude-plugin/plugin.json`.
3. Leave project `AGENTS.md` with project-specific product, source, data/runtime constraints; remove duplicated generic approval, Issue, and CI workflow rules from target repositories when migrating.
4. Use an Issue as an **optional** shared plan. Existing old-format Issue content may be read as historical task context, but former mandatory approval/digest mechanics are not supported.
5. Keep real GitHub/local writer permissions, project safety rules, and explicit host orchestration/model-routing preferences intact. Cross-host transfer of a URL does not transfer credentials or user authorization.
6. A target repository maps affected tests and CI events to `.github/ci-capabilities.json` and validates it with `ci-router.py check-catalog`. Draft iterative edits should not trigger broad CI; significant integration/release boundaries should.
7. Verify installation, package, and runtime identity separately from source commit or passing CI.

Future repositories should switch to this workflow **explicitly when updated**; do not claim their old control files, workflow triggers, Issues, or installed plugins have been migrated solely because this source PR exists. No mass rewrite of other repos occurs here.
