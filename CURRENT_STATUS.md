# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-18.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.7.3`.

Publication identity:

- release PR: `#36` — `MERGED`;
- publication source SHA: `25c7607de18a5ae70f9be48e2faca8b4723fed4c`;
- source feature merge: `998a8cae62546ed8a2551c1fb54aded037c62985`;
- source validation run: `38677775327` — `success`;
- release workflow run: `38678260676` — `success`;
- tag: `plugin-v0.7.3` -> `25c7607de18a5ae70f9be48e2faca8b4723fed4c`;
- release ID: `413399094`;
- asset: `engineering-governance-plugin.zip`;
- asset ID: `642580127`;
- asset size: `144317` bytes;
- asset SHA-256: `d5cee00ff2aacdbe1010f09d0ae706388ef7f62ec1935838da6f3d5f5e2597a6`;
- package entries: `63`;
- package contains only `plugin.json` and `skills/**`;
- included top-level Skills: exactly `9`.

The one-shot v0.7.3 release workflow was archived after publication at `3dd2aa94bb9f16097f606735f3aff4399adbd171`.

The prior `plugin-v0.7.2` release remains immutable historical evidence.

## v0.7.3 behavior

Project Governance distinguishes local commit creation from remote repository delivery.

For state-changing repository work that produced or advanced commits:

- applicable configured remote + not explicitly local-only -> push only the already-authorized task/project ref and verify fresh remote-ref evidence before claiming full repository delivery;
- local commit / clean working tree / local branch SHA alone does not establish remote delivery;
- no applicable remote -> `REMOTE_DELIVERY: NOT_APPLICABLE_NO_REMOTE`;
- explicit local-only authority -> `REMOTE_DELIVERY: NOT_REQUIRED_LOCAL_ONLY`;
- applicable remote but push/verification failure -> preserve local work and report `PENDING` / `FAILED`, not remotely delivered completion;
- normal closeout does not authorize remote creation, force-push, credential bypass, branch substitution, or implicit push to `main`.

Project Governance and EXECUTE Handoff receipts expose local and remote delivery evidence separately.

## Acceptance state

- v0.7.3 source validation: `PASS`;
- additional disposable Local runtime acceptance for v0.7.3: `WAIVED_BY_USER`;
- no runtime PASS claim is inferred from that waiver;
- prior Design acceptance: `PASS`;
- prior Air Local Sub Agent runtime acceptance: `PASS`;
- prior Air nine-Skill routing acceptance: `PASS_WITH_FOLLOWUPS` with no Skill-source corrective.

## Web Plugin

The existing private personal Web Plugin remains synchronized in place to `0.7.3`:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.3`;
- current Web release ID: `pluginrel_6ad04f006d348191928277d9a0e82c15`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root and platform manifests read back as `0.7.3`;
- v0.7.3 remote-delivery contract and Project Governance / Agent Handoff changes were read back;
- `skills/project-governance/references/remote-delivery.md` is present.

`WEB_PLUGIN_SYNC_073`: `PASS`.

## Distribution model

Source authority:

`Lost0rz/Engineering-Governance`

Intentional distribution projections:

1. persistent Local Git-backed Plugin installation, needed across account switches;
2. account-synced Web/remote Plugin projection.

These projections may coexist. Release/distribution correctness depends on source/version/content equivalence rather than forcing one physical runtime cache path.

## Active task

Task `EG-HUMAN-UI-ACCEPTANCE-089` is `ACTIVE` on branch `codex/human-ui-acceptance-boundary` from control parent `bb72d3aae0f98b312700dff3ee527301e9e55991`.

Draft PR `#37 — feat: make product UI acceptance human-owned` is `OPEN / DRAFT / UNMERGED`.

Current source objective:

- preserve Playwright/Cypress/E2E, accessibility, DOM/state, screenshot/visual-regression and other automated browser verification;
- allow AI browser/Computer Use inspection for debugging, evidence gathering, internal Design review, and corrective work;
- prevent AI browser/manual-style clicking or screenshot inspection from satisfying a required human UI/UX/product acceptance gate;
- keep `AUTOMATED_BROWSER_VERIFICATION`, `AI_RENDERED_INSPECTION`, `INTERNAL_VISUAL_REVIEW`, and `HUMAN_UI_ACCEPTANCE` distinct;
- preserve the human acceptance owner across cross-context Handoff cards/receipts.

No new Plugin release is authorized by Task 089. Published/runtime Plugin baseline remains `0.7.3` until a later explicit release decision.

## Repository lifecycle

- stale PR #21: `CLOSED / UNMERGED / SUPERSEDED`;
- v0.7.2 release PR #34: `MERGED`;
- v0.7.3 source PR #35: `MERGED`;
- v0.7.3 release PR #36: `MERGED`;
- Task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`: `COMPLETE`;
- Task `EG-HUMAN-UI-ACCEPTANCE-089`: `ACTIVE`;
- PR #37: `OPEN / DRAFT / UNMERGED`;
- open PR count: `1`.

## Downstream installation state

- private Web Plugin: `0.7.3`;
- Air Local Git-backed Plugin: user update to `0.7.3` pending observation;
- Mac mini Local Git-backed Plugin: user update to `0.7.3` pending observation;
- Local update should refresh the Git-backed marketplace, then start a new Codex/desktop session before verifying loaded version.
