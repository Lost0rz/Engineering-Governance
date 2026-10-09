# CURRENT TASK — Plugin v0.3.0 Release

Task ID: `EG-PLUGIN-V0.3.0-RELEASE-041`

State: `READY_FOR_SOURCE_PR`

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

Use package version `0.3.0` and Release tag `plugin-v0.3.0`.

## Release-source change

Authorized release-source branch: `codex/plugin-v0.3.0-release-v1`.

Fresh audit before PR established:

- reviewed release-source implementation HEAD before this control update: `20a7787bc67090d5f19be1a8e4c958b3254c11da`;
- relative to exact start `fe59b6eb38a40f312f86872248d26f2e151bf07b`, the branch was ahead 3 / behind 0;
- the only changed paths were `plugin.json`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`;
- `plugin.json` changed only `0.2.0 -> 0.3.0`;
- no file under `skills/**` changed during release preparation;
- GitHub returned 404 for both Release `plugin-v0.3.0` and tag ref `refs/tags/plugin-v0.3.0`, so no conflicting release identity exists.

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

Include exactly `plugin.json` and `skills/**`. Exclude repository controls, docs/history, examples, root references, Git metadata, release transport files, caches, editor/OS metadata, secrets, credentials, absolute-path metadata, and temporary files.

## Publication transport boundary

The current GitHub connector does not expose direct tag/Release/asset creation. After the source PR is merged and the exact merged source SHA is locked, a one-shot remote publisher branch is authorized only as transport.

That publisher branch:

- must be created from the exact accepted source SHA only after source merge verification;
- may add a narrowly scoped workflow outside `main` that checks out the locked source SHA, verifies `plugin.json=0.3.0`, packages only the authorized payload, records size/SHA-256, and publishes `plugin-v0.3.0` with `permissions: contents: write`;
- must fail rather than overwrite if the tag/Release already exists;
- must never be merged into `main`;
- must not be the Release target;
- must not be included in the ZIP or tagged source tree;
- becomes terminal after publication and is explicitly retained if current tooling cannot delete the remote branch.

## Release identity requirements

PASS requires all of the following:

1. exact merged `SOURCE_HEAD` is established;
2. `plugin.json` version is exactly `0.3.0`;
3. source diff changes no Skill semantics;
4. ZIP contains exactly the authorized Plugin payload under one `engineering-governance/` root;
5. exactly three top-level Skills are packaged;
6. ZIP byte size and SHA-256 are known before upload;
7. Release tag `plugin-v0.3.0` targets exact `SOURCE_HEAD`;
8. Release is published, non-draft, non-prerelease;
9. asset name is exactly `engineering-governance-plugin.zip`;
10. GitHub-reported asset size/digest matches package evidence;
11. `main` contains no publisher workflow or transport-only file.

## Release notes requirements

Title: `Engineering Governance Plugin v0.3.0`.

Notes must include package version, exact source SHA, asset name/size/SHA-256, three Skills, and these major changes since v0.2.0:

- reusable workspace/worktree lifecycle and closeout contract;
- bounded task-relevant workspace classification instead of routine repository archaeology;
- overlapping fact/state/policy/behavior-authority writer gating;
- retained write-capability / frozen-read-only distinction;
- project-defined terminal-event semantics;
- legacy workspace reconciliation and remote/local evidence boundaries.

Also state that no MCP, hooks, daemon, runtime service, DB, telemetry, installer, automatic cleanup, or automatic remediation was added.

## Workspace lifecycle

- Release-source branch: active and authorized until source PR merge or explicit abandonment.
- Prior 039/040 branches: terminal and no longer write-authorized.
- Publisher branch: not yet created; if created, transport-only and non-main.
- Local workspace state: not claimed by this remote-only task.

## STOP conditions

STOP without publication if source identity, source diff, package contents/hash/size, version, tag target, Release state, or asset identity cannot be verified; if any Skill semantic change appears during release prep; if the publisher cannot prove it packages the exact locked source SHA; or if GitHub Actions lacks write permission.

## Handoff / current stop point

Create a PR from the exact current release-source branch to `main`, independently re-read the actual PR diff, verify mergeability/status evidence, and merge only with expected-head protection. After merge, lock the merged source SHA before creating any publisher transport.
