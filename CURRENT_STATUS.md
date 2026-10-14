# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.6.6`.

Release provenance:

- PR #26: `MERGED`;
- merge/release source SHA: `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`;
- release workflow: `Release Plugin v0.6.6`;
- workflow run: `38549662373` — `success`;
- tag: `plugin-v0.6.6` -> `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`;
- GitHub Release ID: `412590103`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `90618` bytes;
- asset SHA-256: `433831130c2f85358ba75c4f07ef5063318a8ef00b255a8fa5966b2e7f16b93b`;
- package entries: `47`;
- package scope: `plugin.json` + `skills/**` only;
- package version: `0.6.6`;
- exact top-level Skills: `8`.

The release workflow verified the manifest, exact eight-Skill set, Project Profile pre-return/Domain-pointer contract, Handoff core fields and package scope before publication.

## Accepted Web baseline

Personal Web Plugin:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.6`;
- Web release: `pluginrel_6acf45f2c8208191937f142f6c7198a8`;
- scope/discoverability: `USER / PRIVATE`;
- installed root/platform manifests read back as `0.6.6`.

Project Profile Web regressions:

- Gift: PASS;
- Merloom: PASS;
- MemoX: PASS;
- FloatTabs: PASS.

The blocking Profile classes no longer reproduce: Memory/history fact backfill, old-Profile self-bootstrap, current-stage/runtime promotion, temporary endpoint leakage, Domain ownership mini-map under `Authority map`, code maps in `Environment`, and expanded per-Skill routing.

Web routing/discovery acceptance is accepted for the release boundary.

## Current local distribution state

Previously accepted Local Codex baseline on Mac mini and MacBook Air is `0.5.5`.

Local `0.6.6` installation/acceptance is now the remaining boundary. The configured marketplace source is `engineering-governance-personal`, backed by this repository on `main`.

Do not claim full Web+Local integrated acceptance until the local marketplace/plugin is refreshed to `0.6.6` and the required local checks pass.

## Current task

Task: `EG-V066-RELEASE-078`

State: `WAITING_LOCAL_ACCEPTANCE`

Next:

1. refresh the local `engineering-governance-personal` marketplace from `main`;
2. confirm the installed/cache Plugin version is `0.6.6` with exactly eight Skills;
3. verify the authoritative global routing surface is singular/current where that environment uses it;
4. run bounded Local Codex routing/behavior acceptance;
5. reconcile controls after local acceptance.

## Control identity

The formal release tag points to merge/source SHA `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`.

Later commits limited to `CURRENT_STATUS.md` / `CURRENT_TASK.md` are control-only movement and do not alter the released Plugin payload.
