# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.6.8`.

Release provenance:

- PR #28: `MERGED`;
- merge/release source SHA: `7ac2d6262dd280df2b940fa75e9316db8a3615e7`;
- release workflow: `Release Plugin v0.6.8`;
- workflow run: `38572736330` — `success`;
- tag: `plugin-v0.6.8`;
- GitHub Release ID: `412755933`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `106408` bytes;
- asset SHA-256: `79f19bfec117d6f6c914f72f1504949f7158bbddf888c223ed41b1bf92ccba39`;
- package entries: `52`;
- package scope: `plugin.json` + `skills/**` only;
- package version: `0.6.8`;
- top-level Skills: exactly `9`.

The ninth Skill is `design`. Its active baseline bundles Anthropic `frontend-design` internally, with Apache-2.0 license/provenance preserved. Microsoft design-review/adaptation and UX heuristic/audit modules remain planned and inactive.

## Routing result

Current routed boundaries:

- `project-governance` — task/control authority, lifecycle, verification and closeout;
- `solution-design` — material engineering requirements/architecture/state-ownership/API/data-flow/implementation-boundary ambiguity;
- `design` — bounded UI/UX/frontend visual design and redesign, including aesthetic direction, typography, layout, hierarchy, density, composition, interface copy and visual critique.

A keyword alone does not select Design. Project Governance remains task/lifecycle owner when a governed implementation composes Solution Design and Design.

## Web Plugin distribution

The existing private personal ChatGPT Web Plugin was updated in place:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.8`;
- Web release: `pluginrel_6acf859bece081918fb21009caec1fa2`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root `plugin.json`: `0.6.8` read back;
- platform `.codex-plugin/plugin.json`: `0.6.8` read back;
- `skills/design/**`: present and readable;
- Project Governance Design routing: read back from the installed Web release.

`WEB_PLUGIN_SYNC`: `PASS`.

## Regression preservation

The v0.6.8 release gate preserves the previously accepted v0.6.7 Project Profile and Agent Handoff checks in addition to the new Design checks.

- Project Profile pre-return gate: `PASS`;
- Handoff pre-return/request/receipt gates: `PASS`;
- v0.6.7 Handoff regression markers: `PASS`;
- Design source/routing/package checks: `PASS`.

## Local distribution state

No Local Codex cache/source was manually patched.

The supported marketplace source remains this repository `main`, which now publishes `0.6.8`. A fresh Local installed/runtime `0.6.8` readback is still observational follow-up and is not claimed here.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_CACHE_MUTATION`: `NONE`.
`LOCAL_068_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Current task

Task `EG-DESIGN-ANTHROPIC-BASELINE-080` is `COMPLETE`.

Source integration, merge, formal release, Web Plugin update/readback, and control reconciliation are complete. Future Microsoft review/adaptation or UX-audit integration should be authorized as a separate follow-on task behind the stable `design` route.

## Control identity

Released Delivery / Semantic Plugin identity:

`7ac2d6262dd280df2b940fa75e9316db8a3615e7`

Any subsequent commit limited to `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` is control-only Repository HEAD movement and does not alter the released Plugin payload or semantic release identity.
