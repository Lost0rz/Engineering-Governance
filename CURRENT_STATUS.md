# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.6.9`.

Release provenance:

- Task: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081`;
- PR #29: `MERGED` — Design closed-loop / selective routing / receipt enforcement;
- PR #30: `MERGED` — corrective release trigger inside the same Task 081;
- released source SHA: `0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`;
- release workflow: `Release Plugin v0.6.9`;
- workflow run: `38586843709` — `success`;
- tag: `plugin-v0.6.9`;
- GitHub Release ID: `412857747`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `110866` bytes;
- asset SHA-256: `d157790b0c41eb3a9fd254c31319b9efe6936e357346eca9d20e19a373c857ff`;
- package entries: `52`;
- package scope: `plugin.json` + `skills/**` only;
- top-level Skills: exactly `9`.

Anthropic `frontend-design` remains the only active internal Design source module. Its bundled source identity/provenance/license are preserved. Microsoft design-review/adaptation and UX heuristic/audit remain planned and inactive.

## Design corrective result

The v0.6.9 Design contract now requires a qualifying design/redesign task to execute a bounded closed loop rather than merely read the Anthropic reference:

`understand / diagnose → explicit Design deliverable → pre-build brief/genericity review → implementation → rendered visual critique / corrective pass when supported`.

The Design deliverable explicitly covers design intent, page composition, hierarchy, visual-system decisions, interaction/state treatment, and protected business/data/lifecycle authority.

Functional browser regression is no longer equivalent to visual acceptance. When rendered evidence is available, Design must inspect the implemented surface and correct material visual issues before completion; when unavailable, that limitation must be reported rather than fabricated.

## Routing / composition result

Capability composition is now selective rather than cumulative:

- ordinary engineering still enters `project-governance`;
- narrow Skills are selected only for distinct material triggers;
- an already-understood frontend redesign may remain `project-governance → design` through Design's own closed loop;
- known project context does not by itself trigger `domain-navigation`;
- Design's own rendered critique does not by itself trigger `evidence-audit`;
- `solution-design` composes with Design only when a separate material engineering architecture/state-ownership ambiguity actually exists.

The goal is capability depth, not maximum Skill count.

## Receipt observability

Project Governance now has a mandatory pre-return receipt compliance gate.

Every governed user-facing receipt must expose:

- actual `Governance route`;
- actual `Skills used`;
- optional `Capability modules` when a used Skill materially applies a named internal source module;
- task state, outcome, changes, control alignment, PR/workspace and next action as applicable.

Installed/discovered/mentioned Skills that did not materially govern the work must not be reported as used.

## Web Plugin distribution

The existing private personal Web Plugin was updated in place:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.9`;
- Web release ID: `pluginrel_6acf9be52a9c81919536fa9412ed1a67`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root `plugin.json`: `0.6.9` read back;
- platform `.codex-plugin/plugin.json`: `0.6.9` read back;
- updated Design closed-loop Skill: read back;
- updated Project Governance receipt gate: read back;
- updated selective routing/composition: read back;
- bundled Anthropic source/license/provenance remain present.

`WEB_PLUGIN_SYNC`: `PASS`.

## Local distribution state

The last directly observed Local Codex installation on Air is still `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

The supported marketplace source now publishes `0.6.9`. Local `0.6.9` installation/runtime acceptance is not claimed until a fresh local update/readback is observed.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_069_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Current task

Task `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081` is complete at the source/release/Web-distribution boundary. Local `0.6.9` runtime trial remains observational follow-up and does not change the released source identity.

## Control identity

Released Delivery / Semantic Plugin identity:

`0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`

Any subsequent commit limited to `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` is control-only Repository HEAD movement and does not alter the released Plugin payload or semantic release identity.
