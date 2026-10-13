# CURRENT TASK — Plugin v0.5.5 Local Convergence

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.5.5-LOCAL-CONVERGENCE-060`

State: `MINI_PASS_AIR_AUTHORIZED`

Mode: bounded local Plugin convergence and global routing verification

## Objective

Converge Mac mini and MacBook Air from local Plugin `0.5.4` to `0.5.5`, preserving one active canonical Engineering Governance authority on each machine, then verify exactly one current managed Engineering Governance routing block in the authoritative global `AGENTS.md`.

## Planning context

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Relationship to plan: local distribution only; durable governance design is unchanged.

## Accepted baseline

- Formal release: `plugin-v0.5.5`.
- Frozen publication source: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- Current global routing template blob: `c54c84beb6ccfdb5ac1cbd3eb74d1c5e674f496e`.
- v0.5.4 and v0.5.5 global routing templates are byte-identical.

## Execution state

1. Mac mini — `PASS_LOCAL_PLUGIN_055`.
2. Mini receipt audit — `PASS`.
3. MacBook Air — authorized now.
4. Final dual-machine closeout — pending Air receipt.

## Accepted Mac mini result

- Plugin: `0.5.4 -> 0.5.5`.
- Active authority count: `1`.
- Active authority: `engineering-governance@engineering-governance-personal / 0.5.5`.
- Marketplace source: `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`.
- Installed payload matches frozen publication source.
- Exactly three top-level Skills.
- Planning-document linkage: `PASS`.
- Control Alignment Gate: `PASS`.
- `CONTROL_ONLY_DRIFT`: `PASS`.
- Delivery / Semantic HEAD: `PASS`.
- Repository-host gate boundary: `PASS`.
- Global agent authority: `/Users/ox_miles/.codex/AGENTS.md`.
- Managed routing markers: exactly one BEGIN and one END.
- Managed routing template match: `PASS`.
- Global routing reconciliation: `UNCHANGED`.
- Unrelated global rules preserved: `PASS`.
- Manual cache mutation: `NO`.
- Plugin source-directory mutation: `NO`.

## Current authorized scope — MacBook Air only

- Verify Air machine identity and Codex version.
- Verify canonical personal marketplace source and active authority before mutation.
- Upgrade through the supported Codex Plugin path only.
- Verify Plugin `0.5.5`, exactly three top-level Skills, planning-document linkage, Control Alignment Gate, control-only drift semantics, Delivery / Semantic HEAD semantics, and separate repository-host gates.
- Establish the authoritative global `AGENTS.md`.
- Verify exactly one current managed routing block.
- If the marker-bounded region already matches the current template, leave the global file unchanged.
- If one older compatible block exists, replace only that managed region and preserve unrelated global guidance.

## Out of scope

- Further Mini mutation unless later evidence requires explicit reconciliation.
- Copying full Project Governance procedures into global `AGENTS.md`.
- Editing project-local `AGENTS.md` solely for this local Plugin upgrade.
- Adding a fourth Skill.
- Manual active cache/source mutation.
- Removing the personal marketplace.
- Changing formal release or governance semantics.

## Stop conditions

Stop Air if machine identity, global guidance authority, Plugin authority, marketplace source, or routing-marker state is ambiguous; if multiple/conflicting routing blocks exist; if supported Plugin update requires manual cache/source mutation; or if the installed payload does not contain exactly the expected three Skills.

Do not stop merely because old 0.5.4 cache material disappears after the supported CLI update.

## Handoff / current stop point

Air is the only authorized local mutation target. After Air returns `PASS_LOCAL_PLUGIN_055`, perform final cross-machine audit and Control Alignment Gate.
