# CURRENT TASK — Engineering Governance Plugin Release

Task ID: `EG-CODEX-PLUGIN-RELEASE-034`

State: `AUTHORIZED_FOR_LOCAL_RELEASE_PACKAGING`

Mode: `PLUGIN_RELEASE`

## Objective

From the independently audited and merged plugin payload, produce one clean downloadable ZIP on the Mac mini and publish it as the first Engineering Governance Plugin GitHub Release for MacBook Air installation.

## Authority and exact source

- Repository: `Lost0rz/Engineering-Governance`.
- Packaging PR: `#6` — merged.
- Exact accepted plugin payload HEAD: `a29c3ecbc513e4db6fc9663c8b933b39bc088292`.
- Plugin manifest version: `0.1.0`.
- Reusable Skill baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Do not build the release payload from an unverified later working-tree state; archive the exact accepted payload HEAD.

## Release tag

The repository already has an existing historical `v0.1.0` tag. It is immutable and must not be moved, deleted, overwritten, or reused.

Use this release tag instead:

`plugin-v0.1.0`

Release title:

`Engineering Governance Plugin v0.1.0`

The package version remains `0.1.0`; the `plugin-` prefix only disambiguates the repository Release tag namespace.

## Fixed local output

Create exactly:

`/Users/ox_miles/Documents/Code/Engineering-Governance/dist/engineering-governance-plugin.zip`

The ZIP root must be:

`engineering-governance/`

Allowed payload only:

```text
engineering-governance/
├── plugin.json
└── skills/
    ├── project-governance/
    ├── domain-navigation/
    └── incident-doctor/
```

Preserve each Skill's existing `SKILL.md`, `references/`, `assets/`, and `scripts/` exactly as present at the accepted payload HEAD.

## Forbidden ZIP contents

Do not include:

- `.git/`
- root `AGENTS.md`
- root `CURRENT_STATUS.md`
- root `CURRENT_TASK.md`
- `docs/`
- `examples/`
- root `references/`
- local marketplace/config files
- Codex caches
- build caches
- secrets
- machine-specific absolute-path metadata

## Packaging procedure

1. Freshness gate: fetch canonical remote and confirm `origin/main` contains accepted payload HEAD `a29c3ecbc513e4db6fc9663c8b933b39bc088292`; preserve unknown local work and STOP if the canonical checkout is not safe to use.
2. Do not modify the accepted three Skill trees or `plugin.json` during packaging.
3. Recreate `dist/engineering-governance-plugin.zip` from exact accepted payload HEAD. Prefer a deterministic Git archive equivalent to:

```bash
git archive \
  --format=zip \
  --prefix=engineering-governance/ \
  --output=dist/engineering-governance-plugin.zip \
  a29c3ecbc513e4db6fc9663c8b933b39bc088292 \
  plugin.json skills
```

4. Compute SHA-256 and byte size.
5. Extract to a temporary directory and verify:
   - exactly one top-level directory `engineering-governance/`;
   - `plugin.json` parses;
   - all three `SKILL.md` files exist;
   - no forbidden path exists;
   - extracted Skill tree identities/content match the accepted payload.
6. Verify existing historical tag `v0.1.0` is unchanged.
7. Verify `plugin-v0.1.0` does not already exist. STOP rather than overwrite an existing tag/release.
8. Publish GitHub Release tag `plugin-v0.1.0` targeting exact accepted payload HEAD `a29c3ecbc513e4db6fc9663c8b933b39bc088292` and upload exactly one required asset: `engineering-governance-plugin.zip`.
9. Release notes must record:
   - plugin package version `0.1.0`;
   - source HEAD `a29c3ecbc513e4db6fc9663c8b933b39bc088292`;
   - ZIP SHA-256;
   - included Skills: `project-governance`, `domain-navigation`, `incident-doctor`;
   - no MCP/hooks/runtime.
10. Verify from GitHub after publishing:
   - release exists and is not draft unless a platform constraint requires review first;
   - tag is `plugin-v0.1.0`;
   - target resolves to the exact accepted payload HEAD;
   - asset name is exactly `engineering-governance-plugin.zip`;
   - asset is downloadable.

## Repository changes

No reusable Skill or plugin payload source change is authorized in this task.

Do not commit the ZIP into Git unless a later task explicitly authorizes that. `dist/` is a local release-output location, not a required tracked source directory.

Control-only closeout changes after verified publication are allowed only to record release evidence and hand off to independent Web audit.

## Verification level

`V0 + release artifact acceptance`.

Reason: source payload was already independently audited; this task verifies archive composition, identity, release targeting, integrity, and downloadability.

## STOP conditions

STOP without destructive correction if:

- accepted payload HEAD is not reachable from canonical remote;
- local unknown work would be overwritten or cleaned;
- any Skill/plugin source differs from accepted payload during archive creation;
- ZIP contains forbidden files or misses required payload;
- existing historical `v0.1.0` would need to move/change;
- `plugin-v0.1.0` already exists with different content/target;
- release target cannot be fixed to the accepted payload HEAD;
- uploading would require changing plugin source or business repositories.

## Handoff

After publication and verification, update control files with evidence, commit/push only those control closeout changes if needed, and stop at:

`WAITING_FOR_INDEPENDENT_WEB_RELEASE_AUDIT`

Return:

```text
TASK_ID: EG-CODEX-PLUGIN-RELEASE-034
ACCEPTED_PAYLOAD_HEAD:
LIVE_REMOTE_MAIN:
HISTORICAL_V0_1_0_UNCHANGED: YES/NO
RELEASE_TAG: plugin-v0.1.0
RELEASE_TITLE:
RELEASE_TARGET_HEAD:
ZIP_PATH:
ZIP_SHA256:
ZIP_SIZE_BYTES:
ZIP_ROOT:
ZIP_REQUIRED_PATHS: PASS/STOP
ZIP_FORBIDDEN_PATHS: PASS/STOP
SKILL_PAYLOAD_MATCH: PASS/STOP
RELEASE_PUBLISHED: PASS/STOP
RELEASE_ASSET_NAME:
RELEASE_ASSET_DOWNLOADABLE: PASS/STOP
SOURCE_MUTATED: NO
WORKING_TREE:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_RELEASE_AUDIT / STOP
```

Do not clean merged branches or perform unrelated repository lifecycle cleanup under this task.
