# Skill installation and routing adoption

The source repository publishes reusable Skills; an installed runtime decides whether they are discoverable and what tools/permissions it provides. An installation manifest or repo file is not execution authority.

## Adoption checks

1. Check the installed plugin source/version against its intended repository/ref; verify the Skill entry is available in that **actual** host.
2. Exercise a normal repository task: `project-governance` owns task intent and only needed specialist Skills are loaded.
3. For a genuine cross-context transfer, confirm that `agent-handoff` carries a compact authority reference and change request; receiver verifies its own permissions.
4. Verify the target repo's local `AGENTS.md` contains only project-specific facts. Governance modes and host grants come from the installed policy.
5. For authorized source edits, check the real execution host's write capability, not a copied installation result from another machine.
6. When packaging, verify manifest identity, actual archived files, target platform import and installed version independently. CI success alone is not runtime installation evidence.

## Verification routing

The repository's own CI executes a trusted-base `VERIFICATION_PLAN_V1`, selecting affected tests; full test selection and Web preview packaging are separate actions. A target repo maintains its own test commands and dependency map.

Historical FILE_CONTROL-to-ISSUE_CONTROL enrollment must be established from a verified merged migration; consult [issue-control-migration.md](issue-control-migration.md) only for migration or disputed enrollment. A failed or unavailable host trust check cannot be supplied by project prose.
