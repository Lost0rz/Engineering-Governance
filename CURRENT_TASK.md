# CURRENT TASK — Engineering Governance Plugin v0.5.4 Formal Release

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.5.4-FORMAL-RELEASE-057`

State: `AUTHORIZED`

Mode: formal GitHub Plugin release

## Objective

Publish the already accepted Engineering Governance Plugin `0.5.4` payload as a formal GitHub release with immutable tag `plugin-v0.5.4` and release asset `engineering-governance-plugin.zip`.

## Accepted baseline

- Current repository main before task authorization: `4a4611cd4f0b9302b79bd151bb2b4bd2a70ae377`.
- Accepted PR #18 governance semantics: `999c649e499f69bffe7bf870f38e953a0abd59af`.
- Portable manifest 0.5.4 integration: `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- Repo-backed marketplace integration: `6185a1be962956422b7e4eeb56727ccb9a9386fa`.
- ChatGPT Web, Mac mini, and MacBook Air are already verified on Plugin version `0.5.4`.
- Formal historical GitHub Plugin release is currently `plugin-v0.5.3`.

## Authorized scope

- Add one one-shot workflow at `.github/workflows/release-plugin-v0.5.4.yml`.
- Verify root `plugin.json` name/version are `engineering-governance` / `0.5.4`.
- Verify exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`.
- Verify the 0.5.4 control/delivery identity semantics are present.
- Build an exact Plugin ZIP from `plugin.json` plus files under `skills/**` only.
- Require exactly `29` package file entries.
- Create tag `plugin-v0.5.4` at the frozen publication workflow commit without moving any existing tag.
- Create GitHub release `Engineering Governance Plugin v0.5.4` and upload `engineering-governance-plugin.zip`.
- Record release asset size and SHA-256 in release notes.
- Verify the resulting workflow run, tag, release, and release asset.

## Out of scope

- Any new Skill semantics or behavior.
- Fourth Skill or new runtime/daemon/service/database/installer/remediation machinery.
- Manifest version beyond `0.5.4`.
- ChatGPT Web Plugin mutation.
- Local Codex marketplace/cache/source mutation.
- Moving/replacing any existing release tag.
- Packaging repository controls, docs, marketplace catalogs, or workflows into the Plugin ZIP.

## Stop conditions

- `plugin-v0.5.4` tag or release already exists unexpectedly.
- Root manifest is not `engineering-governance` version `0.5.4`.
- Top-level Skill set differs from the expected three.
- Required 0.5.4 governance semantics are missing.
- Package entry count is not exactly `29` or contains files outside `plugin.json` / `skills/**`.
- GitHub Actions release job fails or publishes an asset whose identity cannot be verified.

## Completion criteria

Task 057 is complete only after the formal GitHub release exists, tag identity is verified, the release asset is present, release notes report the source SHA / size / SHA-256 / entry count, and no Plugin payload or local distribution authority was changed by the publication operation.
