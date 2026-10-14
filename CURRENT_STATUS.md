# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.7.0`.

Release provenance:

- Task: `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082`;
- source / merge SHA: `8284f0f138427dd329cd50983046baf78ec110ce`;
- source PR: `#31 — feat: complete multi-module Design closed loop` — merged;
- pre-merge semantic candidate: `8ced8f3ddc455da1228887867c94e5c8c2f01cda`;
- pre-merge acceptance run: `38655255661` — `success`;
- main release workflow: `Release Plugin v0.7.0`;
- main release run: `38655371941` / run #6 — `success`;
- tag: `plugin-v0.7.0`;
- GitHub Release ID: `413275429`;
- release asset ID: `642031591`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `130963` bytes;
- asset SHA-256: `7cd695bc8b7f8302de06a8b36c1e5f5d8afabb8b874416a40ca42b6481fcf06b`;
- package entries: `61`;
- package scope: `plugin.json` + `skills/**` only;
- top-level Skills: exactly `9`.

`V070_PREMERGE_ACCEPTANCE`: `PASS`.
`V070_RELEASE_ACCEPTANCE`: `PASS`.

## Design capability now published

The single externally routed `design` capability now owns this internal closed loop for qualifying UI/UX/frontend design or redesign work:

`Project Profile/context intake → actual interface audit → Anthropic reasoning → shadcn-admin pattern composition when applicable → awesome-design-md-informed DESIGN.md synthesis → implementation/prototype → Microsoft frontend-design-review final audit → corrective pass/re-review → rendered visual acceptance when supported`.

Published boundaries:

- an existing Project Profile / Project Instructions may enter Design directly as compact **derived context / authority pointers**;
- consuming an existing Profile does not itself route through `project-profile`;
- target-project authorities still outrank the Profile and every generic Design module;
- Anthropic `frontend-design` remains the upstream design-reasoning / anti-template layer and its accepted bundled source identity is preserved;
- `satnaing/shadcn-admin` informs a conditional admin/back-office page-pattern layer, not project visual authority;
- `VoltAgent/awesome-design-md` informs bounded visual-system / DESIGN.md synthesis; external brands remain optional inspiration, not authority;
- Microsoft `frontend-design-review` is the downstream final review only; Creative Frontend Design does not compete with the upstream direction;
- Microsoft findings use `Blocking / Major / Minor`, with Blocking/Major requiring correction and re-review;
- Figma, Storybook, token, browser/render and accessibility evidence may not be fabricated;
- no new top-level Skill was added and no all-Skill pipeline was introduced.

Bundled/adapted Design source boundaries:

- Anthropic `frontend-design` — Apache-2.0 bundled source;
- `satnaing/shadcn-admin` — MIT-informed compact adaptation;
- `VoltAgent/awesome-design-md` — MIT-informed compact adaptation;
- Microsoft `frontend-design-review` — MIT-informed compact adaptation.

Each adapted Design module keeps adjacent provenance/license records inside `skills/design/references/**`.

## Published Web Plugin

The existing private personal Web Plugin has been updated **in place** to v0.7.0:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.0`;
- current Web release ID: `pluginrel_6ad01392fbec81919fb25c380af12954`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root `plugin.json`: `0.7.0` read back;
- platform `.codex-plugin/plugin.json`: `0.7.0` read back;
- `skills/design/SKILL.md`: multi-module closed loop read back;
- Design module map: Anthropic / shadcn-admin / awesome-design-md / Microsoft layers read back;
- shadcn-admin admin-pattern module and provenance: read back;
- awesome-design-md synthesis module and provenance: read back;
- Microsoft final-review module and provenance: read back;
- global routing rule allowing existing Project Profile context to enter Design directly as derived context: read back.

`WEB_PLUGIN_SYNC_070`: `PASS`.

## Local distribution state

The last directly observed Local Codex installation on Air remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

No fresh local runtime readback was produced in Task 082. Do not infer that Local Codex has already refreshed to v0.7.0 from GitHub/Web publication.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Task state

Task `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082`: `COMPLETE`.

Source PR #31 is merged, GitHub Plugin v0.7.0 is released, and the existing private Web Plugin has been synchronized/read back at v0.7.0.

The remaining local observation is a distribution/runtime freshness check, not an open source/release blocker for Task 082.

## Control identity

Released semantic Plugin identity:

`8284f0f138427dd329cd50983046baf78ec110ce`

Control-only STATUS/TASK closeout commits after this release may move `main` without changing the released v0.7.0 semantic source identity above.
