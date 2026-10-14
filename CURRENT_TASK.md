# CURRENT TASK — Design Anthropic Closed-Loop + Receipt Enforcement

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081`

Task class: `CAPABILITY_CORRECTIVE`

State: `COMPLETE`

## Objective

Strengthen the routed `design` capability so Anthropic `frontend-design` executes as a bounded design workflow rather than merely being read as reference material, while making governed Skill routing selective and making the actual route / used Skills explicit in every governed user-facing receipt.

## Result

Completed.

Design v0.6.9 now requires qualifying design/redesign work to perform:

`understand / diagnose → explicit Design deliverable → pre-build self-review → implementation → rendered visual critique / corrective pass when supported`.

The Design deliverable covers:

- Design intent;
- page composition;
- information / CTA hierarchy;
- relevant visual-system decisions;
- interaction and state treatment;
- protected business/data/lifecycle authority.

Design does not silently redefine canonical state, API/schema, persistence ownership or lifecycle semantics.

## Routing correction

Skill composition is selective, not a linear all-Skill pipeline.

- Project Governance remains task/lifecycle authority.
- A bounded Design problem stays in Design through its own closed loop unless a separate material trigger exists.
- Domain Navigation is not added merely to read already-known project authorities.
- Evidence Audit is not added merely for Design's own rendered critique.
- Solution Design composes only when a separate material architecture/state-ownership/API/data-flow ambiguity exists.

## Receipt correction

The compact governed receipt now requires:

- actual `Governance route`;
- actual `Skills used`;
- optional internal `Capability modules`;
- task/outcome/change/control/workspace/next fields as applicable.

A mandatory pre-return gate rejects receipts that omit route/Skills, report theoretical instead of actual routing, or list installed/discovered Skills that did not materially govern the work.

## Release evidence

- PR #29: `MERGED`;
- PR #30: `MERGED` — release-trigger correction inside the same Task 081;
- released source SHA: `0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`;
- Plugin version: `0.6.9`;
- release workflow: `Release Plugin v0.6.9`;
- workflow run: `38586843709` — `success`;
- tag: `plugin-v0.6.9`;
- GitHub Release ID: `412857747`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `110866` bytes;
- asset SHA-256: `d157790b0c41eb3a9fd254c31319b9efe6936e357346eca9d20e19a373c857ff`;
- package entries: `52`;
- top-level Skills: exactly `9`.

Release verification preserves the bundled Anthropic source identity `a5333457c414d20d625f307df945842c0952ecc3`, its Apache-2.0 provenance/license, and the previously accepted Project Profile and Agent Handoff gates.

## Web Plugin synchronization

The existing private personal Web Plugin was updated in place:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.9`;
- release ID: `pluginrel_6acf9be52a9c81919536fa9412ed1a67`;
- scope/discoverability remains `USER / PRIVATE`;
- root/platform manifests, Design closed-loop Skill, Project Governance receipt gate, and selective routing/composition were read back successfully;
- Anthropic source/license/provenance remain present.

`WEB_PLUGIN_SYNC`: `PASS`.

## Out of scope / preserved

- Microsoft frontend design review/adaptation: `PLANNED / INACTIVE`;
- UX heuristic/audit module: `PLANNED / INACTIVE`;
- separate Anthropic Plugin dependency: `NONE`.

## Local follow-up

The last observed Air installation is `0.6.8`. The marketplace source now publishes `0.6.9`.

Local `0.6.9` update/readback and a fresh Merloom redesign trial remain observational acceptance follow-up; they do not block Task 081 source/release/Web closeout.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ANTHROPIC-BASELINE-080` (`COMPLETE`)
- `RELEASED_SEMANTIC_SHA`: `0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`
- `FORMAL_RELEASE`: `PASS`
- `WEB_PLUGIN_SYNC`: `PASS`
- `MICROSOFT_MODULE`: `OUT_OF_SCOPE / INACTIVE`
- `UX_AUDIT_MODULE`: `OUT_OF_SCOPE / INACTIVE`
- `LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`
- `LOCAL_069_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`
- `CONTROL_ALIGNMENT`: `PASS`
