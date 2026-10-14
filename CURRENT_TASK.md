# CURRENT TASK — Design Skill Anthropic Baseline Integration

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-ANTHROPIC-BASELINE-080`

Task class: `CAPABILITY_EXPANSION`

State: `COMPLETE`

## Objective

Add a routed top-level `design` capability to Engineering Governance and bundle Anthropic's `frontend-design` Skill as the first complete design-source module, so UI/frontend design work is selected through the existing Governance routing layer instead of requiring a separate external Plugin.

## Result

Completed.

The repository now has exactly nine top-level Skills, including stable external route `design`.

Design v0.6.8 currently provides:

- Anthropic `frontend-design` as the active internal visual-design baseline;
- preserved Apache-2.0 license and source provenance;
- explicit routing separation between UI/frontend visual design (`design`) and engineering architecture/state ownership (`solution-design`);
- Project Governance task/lifecycle authority preserved;
- Microsoft design-review/adaptation and UX heuristic/audit modules reserved as planned, not active.

## Source / release evidence

- PR #28: `MERGED`;
- merge/release source SHA: `7ac2d6262dd280df2b940fa75e9316db8a3615e7`;
- Plugin version: `0.6.8`;
- release workflow run: `38572736330` — `success`;
- tag: `plugin-v0.6.8`;
- GitHub Release ID: `412755933`;
- release asset size: `106408` bytes;
- release asset SHA-256: `79f19bfec117d6f6c914f72f1504949f7158bbddf888c223ed41b1bf92ccba39`;
- package entries: `52`;
- exact top-level Skills: `9`.

Anthropic upstream source identity:

- repository: `anthropics/skills`;
- path: `skills/frontend-design`;
- upstream `SKILL.md` blob: `a5333457c414d20d625f307df945842c0952ecc3`;
- local bundled `frontend-design.md` Git blob matches that source identity.

## Web Plugin synchronization

Existing private personal Plugin updated in place:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.8`;
- release ID: `pluginrel_6acf859bece081918fb21009caec1fa2`;
- scope/discoverability remains `USER / PRIVATE`;
- root and platform manifests read back as `0.6.8`;
- Design source module and Project Governance routing files read back from the installed release.

`WEB_PLUGIN_SYNC`: `PASS`.

## Verification

- exact nine-Skill capability model: `PASS`;
- Anthropic source body identity: `PASS`;
- Apache-2.0 license/provenance packaging: `PASS`;
- UI/frontend Design vs Solution Design routing separation: `PASS`;
- no separate Anthropic Plugin dependency: `PASS`;
- no premature Microsoft/Audit behavior claim: `PASS`;
- v0.6.7 Project Profile/Handoff release gates preserved: `PASS`;
- formal merged-source release/package validation: `PASS`;
- Web Plugin version/content readback: `PASS`;
- Local installed/runtime v0.6.8 behavior: `PENDING_USER_TRIAL`, not claimed.

## Terminal state

Task 080 terminal conditions are satisfied:

- source integration complete;
- PR merged;
- formal v0.6.8 release succeeded for the exact merged source;
- existing Web Plugin updated/read back at `0.6.8`;
- status/task controls reconciled;
- Local can consume the published version without manual cache mutation.

Future integration of Microsoft frontend design review/adaptation or UX heuristic/audit behavior should be authorized as a new follow-on task behind the existing stable `design` route.

Control Alignment:

- `PREDECESSOR_TASK`: `EG-HANDOFF-CARD-GENERATION-CORRECTIVE-079`
- `SOURCE_INTEGRATION`: `PASS`
- `FORMAL_RELEASE`: `PASS`
- `WEB_PLUGIN_SYNC`: `PASS`
- `LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`
- `LOCAL_CACHE_MUTATION`: `NONE`
- `LOCAL_068_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`
- `CONTROL_ALIGNMENT`: `PASS`
