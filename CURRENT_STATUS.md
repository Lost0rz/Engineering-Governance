# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.6.9`.

Release provenance:

- Task: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081`;
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

The released v0.6.9 Design capability has Anthropic `frontend-design` as its active internal source module and already enforces a bounded design-to-rendered-review loop, selective Skill routing, and observable route/used-Skill receipts.

## Published Web Plugin baseline

The existing private personal Web Plugin remains on the last verified v0.6.9 release until Task 082 release synchronization completes:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.9`;
- Web release ID: `pluginrel_6acf9be52a9c81919536fa9412ed1a67`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root `plugin.json`: `0.6.9` read back;
- platform `.codex-plugin/plugin.json`: `0.6.9` read back;
- v0.6.9 Design closed-loop / selective-routing / receipt changes: read back;
- bundled Anthropic source/license/provenance: present.

`WEB_PLUGIN_SYNC_069`: `PASS`.

## Local distribution state

The last directly observed Local Codex installation on Air remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

A newer marketplace/source version exists, but no fresh local runtime readback has been observed in this task. Do not promote the local installation state beyond the latest direct evidence.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Active task

Task `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082` is `ACTIVE` on branch `codex/design-multi-module-closed-loop-v070`.

Start main HEAD:

`366989b63e3c12707b3535eff89d306bf21b48c8`

Draft PR:

`#31 — feat: complete multi-module Design closed loop`

Current Design candidate is Plugin version `0.7.0` and keeps a single external `design` route with this internal sequence:

`Project Profile/context intake → actual interface audit → Anthropic reasoning → shadcn-admin pattern composition when applicable → awesome-design-md-informed DESIGN.md synthesis → implementation/prototype → Microsoft frontend-design-review final audit → corrective pass/re-review → rendered visual acceptance when supported`.

## Task 082 source result

Implemented source boundaries:

- existing Project Profile / Project Instructions may enter Design directly as compact **derived context / authority pointers**; reading them does not itself route through `project-profile`;
- underlying target-project authorities still outrank the Profile;
- Anthropic `frontend-design` remains the upstream design-reasoning / anti-template layer and its accepted source identity is preserved;
- `satnaing/shadcn-admin` informs a conditional admin/back-office page-pattern layer, not project visual authority;
- `VoltAgent/awesome-design-md` informs bounded visual-system / DESIGN.md synthesis, while external brands remain inspiration rather than authority;
- Microsoft `frontend-design-review` is adapted as the final downstream review only; its Creative Frontend Design mode does not compete with the upstream Design direction;
- Microsoft findings use `Blocking / Major / Minor`; open Blocking/Major findings require correction and re-review;
- Figma, Storybook, token, browser/render and accessibility evidence may not be fabricated;
- exactly nine top-level Skills remain;
- Plugin payload contract remains `plugin.json + skills/**` only.

New adapted Design modules preserve local provenance/license records for:

- Anthropic `frontend-design` — Apache-2.0 bundled source;
- `satnaing/shadcn-admin` — MIT-informed compact adaptation;
- `VoltAgent/awesome-design-md` — MIT-informed compact adaptation;
- Microsoft `frontend-design-review` — MIT-informed compact adaptation.

## Pre-merge acceptance

Latest semantic candidate HEAD:

`8ced8f3ddc455da1228887867c94e5c8c2f01cda`

PR pre-release workflow:

- workflow: `Release Plugin v0.7.0`;
- run: `38655255661`;
- run number: `3`;
- event: `pull_request`;
- conclusion: `success`.

This PR run executes source verification and exact Plugin payload construction but does **not** create a tag/release on the pull-request event.

Two earlier PR-run failures were release-gate assertion defects discovered during self-review and corrected before this accepted semantic candidate. They are not release evidence for the candidate.

`V070_PREMERGE_ACCEPTANCE`: `PASS`.

## Distribution state

`0.7.0` is **not yet published** at this point.

Published GitHub/Web baseline remains `0.6.9` until PR #31 is merged, the main-branch v0.7.0 release workflow succeeds, the immutable tag/release asset is verified, and the existing private Web Plugin is synchronized/read back.

## Control identity

Current released semantic Plugin identity remains:

`0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`

Task 082 control-only commits may move the branch/repository HEAD without changing the accepted semantic candidate identified above. A new released semantic identity is established only after the merged source passes the main release boundary.
