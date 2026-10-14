# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.6.7`.

Release provenance:

- PR #27: `MERGED`;
- merge/release source SHA: `53590bcec50c057d6c0fdd25b0e834133a808a93`;
- release workflow: `Release Plugin v0.6.7`;
- workflow run: `38552557416` — `success`;
- tag: `plugin-v0.6.7` -> `53590bcec50c057d6c0fdd25b0e834133a808a93`;
- GitHub Release ID: `412610677`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `94260` bytes;
- asset SHA-256: `082a332d08a526c59c392c073e301c7a78a9a05e47912e96ade2a5b59bdb7c6e`;
- package entries: `47`;
- package scope: `plugin.json` + `skills/**` only;
- package version: `0.6.7`;
- top-level Skills: exactly `8`.

The release workflow verified the exact eight-Skill set, Project Profile pre-return contract, mandatory cross-context Handoff routing, Handoff Card/Receipt pre-return gates, required Card/Receipt fields, valid MODE semantics, the Local global-routing template, the v0.6.7 regression acceptance markers, and exact Plugin package scope before publication.

## Web Plugin distribution

The existing private personal ChatGPT Web Plugin has been updated in place:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.7`;
- Web release: `pluginrel_6acf5f4fb8648191af081084ff326c44`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root `plugin.json`: `0.6.7` read back;
- platform `.codex-plugin/plugin.json`: `0.6.7` read back;
- corrected `agent-handoff`, Handoff request/receipt templates, Handoff contract, `project-governance`, and global routing template read back from the installed Web release.

`WEB_PLUGIN_SYNC`: `PASS`.

## Corrective result

The reproduced v0.6.6 Handoff generation defect is corrected at the reusable source-contract level.

The corrected contract now requires that a construction/execution/audit/review/verify/diagnose Card, instructions, or structured Receipt intended for another agent/session/machine/reviewer/execution context routes through `agent-handoff` before return.

The Handoff pre-return gate now rejects the reproduced legacy-card failure classes:

- task-purpose labels such as `CORRECTIVE` used as `MODE`;
- missing required Handoff core fields;
- rewriting `CURRENT_TASK.md`/plan content instead of authority references + fresh transfer delta;
- promoting sender-observed SHAs into execution locks without owning authority;
- boundaries that expand task authority;
- return contracts or Receipts that predeclare an unobserved successful outcome.

Regression authority: `references/V067_HANDOFF_CARD_ACCEPTANCE.md`.

## Local distribution state

No Local Codex cache/source was manually patched.

The supported source configured for the prior Local installation remains repository `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`, and `main` now publishes Plugin `0.6.7`. Local Codex can therefore update through its supported marketplace/plugin refresh mechanism.

The latest directly observed Local installed version remains the earlier `0.6.6` evidence until a fresh local readback is supplied. Do not claim Local installed/runtime `0.6.7` acceptance before that readback.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_CACHE_MUTATION`: `NONE`.
`LOCAL_067_INSTALL_READBACK`: `PENDING_USER_TRIAL`.

## Current task

Task: `EG-HANDOFF-CARD-GENERATION-CORRECTIVE-079`

State: `COMPLETE`

Source merge, formal release, Web Plugin synchronization/readback, and control reconciliation are complete. Local use of the published `0.6.7` release is the next observational trial, not an unfinished source-corrective step.

## Control identity

Released Delivery / Semantic Plugin identity:

`53590bcec50c057d6c0fdd25b0e834133a808a93`

Subsequent commits limited to `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` are control-only Repository HEAD movement and do not alter the released Plugin payload or its semantic release identity.
