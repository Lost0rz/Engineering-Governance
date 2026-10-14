# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5` until Task `EG-V066-RELEASE-078` publishes `plugin-v0.6.6`.

Previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`; Local Codex acceptance for `0.6.6` is intentionally deferred until installation from the formal release asset.

## v0.6.6 accepted Web candidate

The eight-Skill architecture remains accepted.

Current Delivery / Semantic candidate:

`edf20c44a5ec32b49d2494b7a1c9511af8ca32cd`

Current personal Web Plugin candidate:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.6`;
- Web release: `pluginrel_6acf45f2c8208191937f142f6c7198a8`;
- scope/discoverability: `USER / PRIVATE`;
- root/platform manifests read back as `0.6.6`;
- Task-077 Skill/template/contract installed readback: PASS;
- Task-077 overlay ZIP SHA-256: `bc714a64fde1b273e346db6632728b338329ef1953bffb404360b5a078a1af64`;
- packaged Git-blob identities matched repository source for the corrected Profile files before Web upload.

## Web acceptance

Parent Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is closed for the Web boundary.

Project Profile regressions:

- Gift: PASS;
- Merloom: PASS;
- MemoX: PASS;
- FloatTabs: PASS.

The previously blocking Profile classes no longer reproduce:

- Memory/history backfill into Profile facts;
- old Profile self-bootstrap;
- current-stage/runtime detail promoted into durable identity;
- temporary endpoint leakage;
- Domain ownership mini-map under `Authority map`;
- source/code map in `Environment`;
- expanded per-Skill Engineering Governance routing.

Previously established Web routing/discovery acceptance remains valid. Later Tasks 072–077 were bounded Project Profile correctives except Task 071's Handoff template correction and did not introduce a new material routing failure. Current Web use continues to route ordinary engineering through Project Governance, Profile work through Project Profile, and formal release/readiness audit through Evidence Audit.

Minor compression observations in generated Profiles remain non-blocking.

## Current release task

Task: `EG-V066-RELEASE-078`

State: `ACTIVE`

Authorized next actions:

1. add and audit a dedicated `0.6.6` release workflow;
2. make PR #26 ready and merge only after release-readiness PASS;
3. verify the main-triggered `plugin-v0.6.6` tag/release/package provenance;
4. provide Local Codex update commands for installation from the formal release asset;
5. run Local Codex integrated acceptance after update.

## PR / host state before release workflow change

- PR #26: OPEN / DRAFT / UNMERGED / mergeable at last fresh read;
- base `main`: `3b8d99c3dba13ca01098abade5c6e696454ddd10`;
- no required branch-protection status checks are configured on `main`;
- no PR workflow/check result is being claimed as PASS where none exists.

## Release boundary

The formal GitHub Plugin asset must contain only:

- `plugin.json`;
- `skills/**`.

Release version/tag:

`0.6.6` / `plugin-v0.6.6`

Local Codex is updated **after** publication from this immutable asset. Full Web+Local integrated acceptance remains pending until the local installation and acceptance succeed.
