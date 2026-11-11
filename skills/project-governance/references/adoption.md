# Adoption across repositories and hosts

The plugin provides reusable work methods, not remote write credentials or a new task database.

1. Install the intended plugin version in each execution host and verify the Skill entry/routing actually works there.
2. Leave project `AGENTS.md` with project-specific product, source, data/runtime constraints; remove duplicated generic approval, Issue and CI workflow rules from target repositories when migrating.
3. Use an Issue as an **optional** shared plan. Existing old-format Issue content may be read as historical task context, but former mandatory approval/digest mechanics are not supported.
4. Keep real GitHub/local writer permissions and project safety constraints. Cross-host transfer of a URL does not transfer credentials or user authorization.
5. A target repository maps affected tests and CI events to its own commands. Draft iterative edits should not trigger broad CI; significant integration/release boundaries should.
6. Verify installation, package and runtime identity separately from source commit or a passing CI.

Future repositories should switch to this workflow **explicitly when updated**; do not claim their old control files, workflow triggers, Issues or installed plugins have been migrated solely because this source PR exists. No mass rewrite of other repos occurs here.
