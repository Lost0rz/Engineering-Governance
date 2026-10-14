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

MacBook Air local Codex Plugin installation is now updated to `0.6.6` through the supported plugin remove/add mechanism using marketplace `engineering-governance-personal`.

Observed installation evidence supplied from the local terminal:

- installed Plugin: `engineering-governance@engineering-governance-personal`;
- version: `0.6.6`;
- enabled: `true`;
- source: `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`;
- installed path: `/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.6`;
- top-level Skill count: exactly `8`;
- Skills: `agent-handoff`, `domain-navigation`, `evidence-audit`, `execution-orchestrator`, `incident-doctor`, `project-governance`, `project-profile`, `solution-design`.

`LOCAL_PLUGIN_INSTALLATION`: `PASS`.

Remaining local acceptance is behavioral/routing acceptance, not distribution installation.

Do not claim full Web+Local integrated acceptance until the required local routing/continuation/handoff checks pass.

## Current task

Task: `EG-V066-RELEASE-078`

State: `LOCAL_INSTALL_PASS_ROUTING_ACCEPTANCE_PENDING`

Next:

1. verify the authoritative local global routing surface is singular/current where that environment uses it;
2. exercise bounded Local Codex routing/continuation/profile/handoff evidence from `references/V060_INTEGRATED_ACCEPTANCE.md`;
3. return the local receipt for Web audit;
4. reconcile controls and close Task 078 only if local acceptance passes.

## Control identity

The formal release tag points to merge/source SHA `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`.

Later commits limited to `CURRENT_STATUS.md` / `CURRENT_TASK.md` are control-only movement and do not alter the released Plugin payload.
