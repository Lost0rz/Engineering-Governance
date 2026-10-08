# CURRENT TASK — Plugin v0.2.0 Release

Task ID: `EG-PLUGIN-V0.2.0-RELEASE-038`

State: `AUTHORIZED_FOR_RELEASE_PREP_AND_PUBLICATION`

Mode: `PLUGIN_RELEASE`

## Objective

Publish an overall Engineering Governance Plugin v0.2.0 containing the accepted reusable changes merged after Plugin v0.1.0, without changing Skill semantics during release preparation.

## Authoritative baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted pre-release main HEAD: `302dd233036ec77a423fa870d1ca994613d415c4`.
- Accepted changes included in the release:
  - PR #7: Domain Navigation current-task authority gate / DN-001 corrective;
  - PR #8: Project Governance canonical authority + code structure principles;
  - PR #9: Project Governance task lifecycle + evidence identity + selected workspace integrity.
- Published predecessor: GitHub Release `plugin-v0.1.0`, package version `0.1.0`.
- Historical repository tag `v0.1.0` is unrelated to Plugin release numbering and must remain immutable.

## Version decision

Use package version `0.2.0` and release tag `plugin-v0.2.0`.

Reason: this release contains multiple accepted reusable capability enhancements in addition to a corrective; it is an overall minor release, not merely a single patch fix.

## Authorized source change

Only release metadata may change before packaging:

- `plugin.json`: `"version": "0.1.0"` -> `"version": "0.2.0"`.
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` may record release handoff and verified facts.

Do not modify any Skill content during release preparation. If a Skill semantic change is needed, STOP and create a separate reusable-skill task.

## Package contract

Create exactly one release asset:

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

Exclude at minimum:

- `.git/**` and Git metadata;
- root `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`;
- `docs/**`, including `docs/superpowers/**`;
- `examples/**`;
- root `references/**` maintainer/upstream notes;
- `dist/**` inputs from prior releases;
- caches, editor settings, secrets, credentials, absolute-path metadata, OS metadata, and temporary files.

Do not copy the entire repository into the ZIP and then rely on users to ignore extra files.

## Exact identity requirements

Before packaging, establish the exact accepted source revision containing the v0.2.0 metadata. Package from that exact revision/worktree.

Record and verify:

- `SOURCE_HEAD`;
- `plugin.json` version = `0.2.0`;
- exact ZIP file list;
- ZIP byte size;
- ZIP SHA-256;
- release tag target;
- published asset name and uploaded asset identity.

The published Release must target the exact accepted v0.2.0 source revision. Do not publish from a moving branch name without recording the resolved SHA.

## Release notes

Release title:

`Engineering Governance Plugin v0.2.0`

Release tag:

`plugin-v0.2.0`

Release notes should concisely state:

- package version `0.2.0`;
- exact source SHA;
- asset name and SHA-256;
- three included Skills;
- major changes since v0.1.0:
  - Domain Navigation current-task authority gate and bounded historical navigation;
  - canonical authority and domain-coherent code-structure guidance;
  - task lifecycle integrity;
  - evidence/artifact identity binding with proven-equivalence reuse;
  - selected task-workspace identity with bounded discovery;
- no MCP, hooks, daemon, runtime service, DB, telemetry, installer, or automatic remediation added.

Do not create or move repository tag `v0.1.0` or create an ambiguous plain `v0.2.0` tag. Use `plugin-v0.2.0` for this Plugin release.

## Verification

Use `V0 + release artifact identity verification`.

PASS only if:

1. release-prep source diff contains no Skill semantic changes;
2. package version is exactly `0.2.0`;
3. exactly three top-level reusable Skills are packaged;
4. ZIP contains only the authorized Plugin payload under one `engineering-governance/` root;
5. file list contains no control files, maintainer docs, examples, Git metadata, caches, secrets, or unrelated files;
6. ZIP SHA-256 and byte size are recorded before upload;
7. release tag resolves to the exact accepted source SHA;
8. published Release is neither draft nor prerelease unless explicitly changed by the user;
9. published asset name is exactly `engineering-governance-plugin.zip`;
10. post-publication verification confirms release target and asset metadata.

## Workspace safety

Use an exact clean source checkout or dedicated release worktree aligned to the authorized source revision. Preserve unknown local work. Do not reset, stash, clean, delete, overwrite, or force merely to create the package.

An unrelated preserved `dist/` in another workspace must not be treated as release input. Generate the new archive from the exact accepted v0.2.0 source identity.

## STOP conditions

STOP without publishing if:

- source HEAD or release tag target is ambiguous;
- release-prep diff changes Skill semantics;
- package includes unauthorized files;
- version is not `0.2.0`;
- package file list cannot be verified;
- asset hash/size cannot be established;
- release target is not the exact accepted source revision;
- existing `plugin-v0.2.0` tag/release already exists with a conflicting identity;
- unknown local work would need destructive cleanup.

## Handoff

Return at completion:

```text
TASK_ID: EG-PLUGIN-V0.2.0-RELEASE-038
CONTROL_HEAD:
RELEASE_BRANCH:
ACCEPTED_SOURCE_HEAD:
PLUGIN_VERSION: 0.2.0
SKILL_SEMANTICS_CHANGED_DURING_RELEASE: NO
PACKAGE_PATH:
PACKAGE_SIZE_BYTES:
PACKAGE_SHA256:
PACKAGE_FILE_LIST_CHECK: PASS/STOP
RELEASE_TAG: plugin-v0.2.0
RELEASE_TARGET_SHA:
RELEASE_PUBLISHED: YES/NO
RELEASE_DRAFT: NO
RELEASE_PRERELEASE: NO
ASSET_NAME: engineering-governance-plugin.zip
PUBLISHED_ASSET_SIZE_BYTES:
PUBLISHED_ASSET_SHA256_OR_VERIFIED_IDENTITY:
POST_PUBLISH_VERIFICATION: PASS/STOP
WORKING_TREE:
FINAL_STATE: RELEASED / STOP
```
