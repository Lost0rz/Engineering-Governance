# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Released baseline

- Latest published Plugin is still `0.3.0`.
- Release tag: `plugin-v0.3.0`.
- Source SHA: `d11ed12bfdac4c8ff22d37961753190a400358da`.
- Asset SHA-256: `c60dcf4860701e394f308ccaf293cc348166008b6e198fcb29e6e08bf5ebf400`.

## Accepted v0.4.0 source

- Governance/routing PR #14 merged successfully.
- Exact merged source before release-control changes: `879521028a056a9fed4ce6fb9be89a6221eb80bf`.
- PR head -> merge comparison: zero file differences.
- Final audited reusable payload within that source was sealed at `0a00ebf1a5ebe17163431fa099249b8e2fc70a22`; later PR changes before merge were control-only.
- `plugin.json` version: `0.4.0`.
- Exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.
- Release identity checks: GitHub Release `plugin-v0.4.0` = absent (404); tag ref `refs/tags/plugin-v0.4.0` = absent (404).

## Current task

- Task: `EG-PLUGIN-V0.4.0-RELEASE-043`.
- State: `READY_FOR_SOURCE_PR`.
- Branch: `codex/plugin-v0.4.0-release-v1`.
- Release-source preparation is control-only; Skill/plugin payload semantics are frozen.

## v0.4.0 release content

Major accepted changes since v0.3.0:

1. managed global Skill routing/adoption with Project Governance default routing;
2. installation completion requires three Skills plus exactly one current global routing block;
3. responsibility/Domain/authority-based code structure enforced during construction, independent of line count/edit size;
4. bounded workspace lifecycle checkpoints during normal development, with legacy archaeology exceptional;
5. control identity semantics preventing historical-parent/current-head category errors while preserving explicit head locks;
6. canonical authority / parallel-writer prevention;
7. verification risk tier separated from validation cadence;
8. Domain navigation reuses accepted semantic maps and keeps optional projections derived.

## Publication boundary

Release asset must be exactly `engineering-governance-plugin.zip` with one `engineering-governance/` root containing only `plugin.json` and `skills/**`. Publisher transport is one-shot, remote-only, never merged into `main`, never the Release target, and never packaged.

## Next milestone

Merge the release-source control-only PR after verifying no Skill/plugin payload change, lock the exact merged release-source SHA, run the one-shot publisher, and verify Release/tag/asset/package hash and contents. After verified publication, proceed to local reinstall and real routing acceptance.
