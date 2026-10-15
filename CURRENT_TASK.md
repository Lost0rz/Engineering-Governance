# CURRENT TASK — Engineering Governance Plugin v0.7.3 Formal Release

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`

Task class: `RELEASE`

State: `ACTIVE — RELEASE_AUTHORIZED`

## Objective

Publish the accepted Engineering Governance Plugin `0.7.3` source as a formal GitHub release, synchronize the existing private Web Plugin in place to `0.7.3`, and leave Local Git-backed installation as a downstream user-executed update with explicit verification commands.

## Predecessor source result

Task `EG-REMOTE-DELIVERY-CLOSEOUT-087` source work is complete:

- PR `#35 — feat: require verified remote repository delivery at closeout` — `MERGED`;
- validated semantic/source head: `7a5c256b4bdf09768645d252df340870f8d8ef82`;
- `Validate Plugin v0.7.3 Candidate` run `38677775327` — `success`;
- merge commit: `998a8cae62546ed8a2551c1fb54aded037c62985`;
- root manifest: `0.7.3`;
- exactly nine top-level Skills retained;
- remote-delivery closeout contract is present in Project Governance and Agent Handoff receipts.

## Runtime-acceptance decision

The user explicitly waived an additional disposable Local runtime acceptance round for the bounded remote-delivery correction and authorized direct publication/distribution.

Therefore:

- `LOCAL_RUNTIME_ACCEPTANCE_073`: `WAIVED_BY_USER`;
- the waiver does not convert untested runtime behavior into observed PASS evidence;
- source validation remains `PASS`;
- release provenance must record the waiver rather than claim runtime acceptance.

## Release scope

1. create a one-shot `plugin-v0.7.3` release workflow;
2. verify manifest `0.7.3`, exactly nine Skills, and required remote-delivery contract markers;
3. build exact `plugin.json + skills/**` ZIP;
4. create immutable tag `plugin-v0.7.3` and GitHub release asset;
5. read back tag/release/asset provenance;
6. archive the one-shot release workflow after publication;
7. update the existing private Web Plugin in place to `0.7.3` and read back its version/content;
8. reconcile `CURRENT_STATUS.md` and `CURRENT_TASK.md` to the observed release/distribution result.

## Boundaries

- do not change Skill semantics during release;
- do not move or replace the immutable `plugin-v0.7.2` tag/release;
- do not claim Local runtime acceptance for v0.7.3;
- do not mutate user Local Codex installations from Web;
- Local Git-backed and account-synced distributions may coexist as projections of the repository source;
- Mac mini/Air Local installation is completed by the user with explicit CLI commands after formal release.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-REMOTE-DELIVERY-CLOSEOUT-087` (`SOURCE_MERGED`)
- `SOURCE_VERSION`: `0.7.3`
- `SOURCE_VALIDATION`: `PASS`
- `LOCAL_RUNTIME_ACCEPTANCE_073`: `WAIVED_BY_USER`
- `WEB_PLUGIN_UPDATE`: `PENDING`
- `FORMAL_GITHUB_RELEASE_073`: `PENDING`
- `TASK_STATE`: `ACTIVE — RELEASE_AUTHORIZED`
