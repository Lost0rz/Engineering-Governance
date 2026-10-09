# CURRENT TASK — Plugin v0.4.0 Release

Task ID: `EG-PLUGIN-V0.4.0-RELEASE-043`

State: `READY_FOR_SOURCE_PR`

Mode: `PLUGIN_RELEASE`

## Objective

Publish Engineering Governance Plugin v0.4.0 from the already audited and merged routing/governance source, without changing Skill/plugin payload semantics during release preparation.

## Authoritative baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted merged source before release-control changes: `879521028a056a9fed4ce6fb9be89a6221eb80bf`.
- Governance/routing PR #14 was merged from exact head `3b969e45230923629d23bb0d1a432c1740b4ae3b`; comparison from PR head to merge commit shows zero file differences.
- Final audited reusable payload inside the merged source was sealed at `0a00ebf1a5ebe17163431fa099249b8e2fc70a22`; subsequent pre-merge changes were control-only.
- Published predecessor: `plugin-v0.3.0`, source `d11ed12bfdac4c8ff22d37961753190a400358da`.
- Release identity `plugin-v0.4.0` was unused at task start: both Release lookup and tag-ref lookup returned 404.

## Version and release identity

- Package version: `0.4.0`.
- Release tag: `plugin-v0.4.0`.
- Release title: `Engineering Governance Plugin v0.4.0`.
- Asset: `engineering-governance-plugin.zip`.

## Release-source branch

Authorized branch: `codex/plugin-v0.4.0-release-v1`.

Release-source changes are limited to `CURRENT_STATUS.md` and `CURRENT_TASK.md`. No `plugin.json` or `skills/**` mutation is authorized in this task.

Before merging the release-source PR, verify:

- branch starts from exact source `879521028a056a9fed4ce6fb9be89a6221eb80bf`;
- diff contains only the two control files;
- `plugin.json` remains exactly `0.4.0`;
- exactly three top-level Skill directories remain;
- the Plugin payload tree is unchanged from the accepted merged source.

## Package contract

Create exactly one Release asset: `engineering-governance-plugin.zip`.

ZIP root must be:

```text
engineering-governance/
├── plugin.json
└── skills/
    ├── project-governance/
    ├── domain-navigation/
    └── incident-doctor/
```

Include exactly `plugin.json` and `skills/**`. Exclude root controls, docs, examples, root references, Git metadata, publisher workflow/transport files, caches, temporary files, secrets, credentials, absolute-path metadata, and symlinks.

## Publisher transport

The current connector does not expose direct GitHub Release creation, so a one-shot publisher branch is authorized after the release-source PR is merged and the exact source SHA is locked.

Publisher requirements:

- create from the exact accepted release-source SHA only after merge verification;
- workflow exists only on the publisher branch and is never merged into `main`;
- `permissions: contents: write` only;
- fail if either `plugin-v0.4.0` Release or tag already exists;
- checkout the exact locked source SHA, not publisher HEAD;
- verify `plugin.json=0.4.0` and exactly three top-level Skills;
- package only the authorized payload and reject symlinks/extra paths;
- record package byte size and SHA-256 before upload;
- publish tag/Release `plugin-v0.4.0` targeting the exact source SHA;
- publisher branch is transport-only, is not the Release target, and must not appear in the ZIP/tagged source.

## Release notes requirements

Release notes must include version, exact source SHA, asset name, size, SHA-256, the three included Skills, and major changes since v0.3.0:

- global managed Skill routing/adoption;
- Project Governance default engineering route with lightweight behavior for simple work;
- Domain Navigation conditional routing and accepted-map reuse;
- Incident Doctor reactive evidence gate;
- construction-time responsibility/Domain/authority-based code structure independent of line count/edit size;
- canonical authority / parallel-writer prevention;
- bounded worktree lifecycle checkpoints with exceptional legacy reconciliation;
- control identity semantics for provenance/current/locked heads;
- verification tier/cadence separation.

State that no fourth Router Skill, MCP, hook, daemon, runtime service, database, telemetry, installer executable, automatic cleanup, or automatic remediation was added.

## Release verification PASS criteria

1. exact merged release-source SHA is established;
2. `plugin.json` is `0.4.0`;
3. release-prep diff changes no Plugin payload path;
4. ZIP contains exactly the authorized payload under one root;
5. exactly three top-level Skills are packaged;
6. package byte size and SHA-256 are known;
7. tag `plugin-v0.4.0` targets exact release-source SHA;
8. Release is published, non-draft, non-prerelease;
9. asset name is exact;
10. GitHub-reported size/digest matches publisher evidence;
11. `main` and tagged source contain no publisher workflow/transport file.

## Stop conditions

Stop before publication if source identity, source diff, package content/hash/size, release/tag availability, tag target, or asset identity cannot be verified; if `plugin.json` or `skills/**` changes during release preparation; or if GitHub Actions cannot publish with contents write permission.

## Handoff / current stop point

Create a control-only release-source PR to `main`, audit its exact diff, and merge with expected-head protection. Lock the resulting source SHA. Only then create the one-shot publisher branch and publish. After verified Release publication, the next task is local reinstall + routing acceptance.
