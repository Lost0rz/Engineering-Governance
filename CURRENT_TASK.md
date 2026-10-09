# CURRENT TASK — Plugin v0.3.0 Release

Task ID: `EG-PLUGIN-V0.3.0-RELEASE-041`

State: `AUTHORIZED_FOR_RELEASE_PREP_AND_PUBLICATION`

Mode: `PLUGIN_RELEASE`

## Objective

Publish Engineering Governance Plugin v0.3.0 containing the accepted reusable workspace/worktree lifecycle capability merged after Plugin v0.2.0, without changing Skill semantics during release preparation.

## Authoritative baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted pre-release `main` HEAD: `fe59b6eb38a40f312f86872248d26f2e151bf07b`.
- Published predecessor: GitHub Release `plugin-v0.2.0`, package version `0.2.0`, source SHA `cf2df83e7e6bde39a5cce7f51e47d59e3911d71c`.
- Accepted reusable changes since v0.2.0: task 039 workspace lifecycle contract and task 040 semantic corrective.
- Exactly three top-level reusable Skills remain: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Version decision

Use package version `0.3.0` and release tag `plugin-v0.3.0`.

Reason: this release adds a new reusable project-governance capability and materially extends normal governed development semantics, so it is a minor release rather than a patch-only correction.

## Authorized source change

Before packaging, release-source changes are limited to:

- `plugin.json`: `"version": "0.2.0"` -> `"version": "0.3.0"`;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md`: release task/evidence state only.

Do not modify Skill content during release preparation. If any Skill semantic change is needed, STOP and create a separate reusable-Skill task.

## Package contract

Create exactly one Release asset:

`engineering-governance-plugin.zip`

ZIP root must be:

```text
engineering-governance/
├── plugin.json
└── skills/
    ├── project-governance/
    ├── domain-navigation/
    └── incident-doctor/
```

Include exactly:

- `plugin.json`
- `skills/**`

Exclude repository controls, maintainer docs/history, examples, root references, Git metadata, release transport files, caches, editor/OS metadata, secrets, credentials, absolute-path metadata, and temporary files.

## Exact identity requirements

Before packaging, establish the exact merged source revision containing the `0.3.0` metadata. Package from that exact revision, not a moving branch name.

Record and verify:

- `SOURCE_HEAD`;
- `plugin.json` version = `0.3.0`;
- exact ZIP file list;
- ZIP byte size;
- ZIP SHA-256;
- Release tag target;
- published Release state;
- asset name, size, and GitHub-reported digest/identity.

## Release notes

Release title:

`Engineering Governance Plugin v0.3.0`

Release tag:

`plugin-v0.3.0`

Release notes should state:

- package version `0.3.0`;
- exact source SHA;
- asset name, byte size, and SHA-256;
- included Skills: `project-governance`, `domain-navigation`, `incident-doctor`;
- major changes since v0.2.0:
  - reusable workspace/worktree lifecycle and closeout contract;
  - bounded task-relevant workspace classification instead of routine repository archaeology;
  - overlapping fact/state/policy/behavior-authority writer gating;
  - explicit retained write-capability / frozen-read-only distinction;
  - project-defined terminal-event semantics;
  - legacy workspace reconciliation and remote/local evidence boundaries;
- no MCP, hooks, daemon, runtime service, DB, telemetry, installer, automatic cleanup, or automatic remediation added.

Do not create an ambiguous plain `v0.3.0` tag. Use `plugin-v0.3.0`.

## Publication transport boundary

The current GitHub connector does not expose direct tag/Release/asset creation. A one-shot remote publisher branch is authorized only as transport if needed.

Requirements for that transport:

- it is separate from the release-source branch and from `main`;
- it is created only after the exact release-source commit is merged and verified;
- it may contain a narrowly scoped GitHub Actions workflow that packages the exact locked `SOURCE_HEAD` and publishes `plugin-v0.3.0`;
- the workflow must use `permissions: contents: write`, target the exact locked source SHA, verify version/file list/hash/size before publishing, and fail if the tag/release already exists;
- its workflow/transport files must not be merged to `main`, must not be included in the source tag, and must not be included in the ZIP;
- if GitHub Actions cannot run or lacks write permission, STOP publication rather than changing release identity or weakening verification.

## Verification

Use `V0 + release artifact identity verification`.

PASS only if:

1. release-source diff changes no Skill semantics;
2. package version is exactly `0.3.0`;
3. exactly three top-level reusable Skills are packaged;
4. ZIP contains only the authorized Plugin payload under one `engineering-governance/` root;
5. forbidden repository/control/transport files are absent;
6. ZIP SHA-256 and byte size are established before upload and reflected in release notes/evidence;
7. Release tag resolves to the exact accepted merged source SHA;
8. published Release is neither draft nor prerelease;
9. asset name is exactly `engineering-governance-plugin.zip`;
10. post-publication verification confirms release target, asset size, and digest/identity;
11. `main` contains no publisher workflow or transport-only file.

## Workspace lifecycle

- Release-source branch: `codex/plugin-v0.3.0-release-v1`, active until merged or explicitly abandoned.
- Prior task branches 039/040 are terminal and no longer authorize writes.
- Any publisher branch is transport-only, must be terminal after publication, and must be explicitly recorded as retained if branch deletion capability is unavailable.
- This remote-only task does not claim local worktree cleanliness.

## STOP conditions

STOP without publishing if:

- source HEAD or Release target is ambiguous;
- release-source diff changes Skill semantics;
- package includes unauthorized files;
- version is not `0.3.0`;
- package file list/hash/size cannot be verified;
- existing `plugin-v0.3.0` tag/release already exists with conflicting identity;
- publisher workflow cannot prove it packaged the exact locked source SHA;
- GitHub Actions lacks required write permission;
- publication succeeds but post-publication target/asset identity does not match expected evidence.

## Handoff

Return at completion:

```text
TASK_ID: EG-PLUGIN-V0.3.0-RELEASE-041
START_MAIN:
RELEASE_SOURCE_BRANCH:
ACCEPTED_SOURCE_HEAD:
PLUGIN_VERSION: 0.3.0
SKILL_SEMANTICS_CHANGED_DURING_RELEASE: NO
PACKAGE_SIZE_BYTES:
PACKAGE_SHA256:
PACKAGE_FILE_LIST_CHECK: PASS/STOP
RELEASE_TAG: plugin-v0.3.0
RELEASE_TARGET_SHA:
RELEASE_PUBLISHED: YES/NO
RELEASE_DRAFT: NO
RELEASE_PRERELEASE: NO
ASSET_NAME: engineering-governance-plugin.zip
PUBLISHED_ASSET_SIZE_BYTES:
PUBLISHED_ASSET_SHA256_OR_VERIFIED_IDENTITY:
POST_PUBLISH_VERIFICATION: PASS/STOP
PUBLISHER_BRANCH_DISPOSITION:
LOCAL_WORKSPACE_STATUS: NOT_CLAIMED
FINAL_STATE: RELEASED / STOP
```
