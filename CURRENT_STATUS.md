# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.7.1`.

Release provenance:

- Task: `EG-DESIGN-ROUTING-HARDENING-083`;
- source / merge SHA: `208279e5f3b7974c13a3446a3db2e8f27de7b688`;
- source PR: `#32 — feat: harden Design routing composition` — merged;
- pre-merge semantic candidate: `f0f1ebf6a9c7c49c106955cfb84940a645635dc4`;
- pre-merge acceptance run: `38658235439` — success;
- main release workflow: `Release Plugin v0.7.1`;
- main release run: `38658367623` / run #5 — success;
- tag: `plugin-v0.7.1`;
- GitHub Release ID: `413290156`;
- release asset ID: `642098498`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `134882` bytes;
- asset SHA-256: `8a2482eb4c0e28c642b5d27ffe34c0e64c0b8d64afbf9c51c6b83325013055db`;
- package entries: `61`;
- package scope: `plugin.json` + `skills/**` only;
- top-level Skills: exactly `9`.

`V071_PREMERGE_ACCEPTANCE`: `PASS`.
`V071_RELEASE_ACCEPTANCE`: `PASS`.

## Design routing hardening now published

The external route remains the single top-level `design` Skill, but Design is no longer treated as an isolated silo.

Published routing behavior:

- Design remains primary owner of bounded UI/UX/frontend interaction and visual-design work after entry;
- cross-Skill composition is allowed only for a concrete unresolved dependency that can materially change the current decision;
- each bounded call identifies the unresolved dependency, decision/Design impact, smallest owning capability, bounded expected return and explicit resume owner/stage;
- bounded results return to the originating capability/stage instead of restarting the full routing tree;
- `domain-navigation` is explicitly valid when a needed backend/product authority/source/symbol/state-owner/runtime/test route is genuinely unclear;
- `solution-design` is explicitly valid when the route is known but material business/state/API/data-flow ownership remains ambiguous;
- other Skills remain available only on their real triggers;
- no Skill is invoked merely for general enrichment, completeness, a generic second opinion or because it is installed.

Frontend workflow ownership is explicit:

- interaction workflow — how users see, understand, navigate, edit, act and receive feedback -> `design`;
- business/state workflow — canonical state transitions, data/state ownership, API/data-flow responsibility, persistence semantics and implementation boundaries -> `solution-design` when materially ambiguous.

Design supports four purpose-specific modes:

- `AUDIT_ONLY`;
- `DESIGN_SPEC`;
- `DESIGN_IMPLEMENT`;
- `FINAL_REVIEW`.

For full implementation with rendered evidence support, the published sequence is:

`context/audit → Anthropic reasoning → admin pattern when applicable → bounded design spec → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`.

Anthropic, shadcn-admin, awesome-design-md and Microsoft remain internal Design modules; their existing provenance/license boundaries remain preserved.

## Published Web Plugin

The existing private personal Web Plugin has been updated **in place** to v0.7.1:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.1`;
- current Web release ID: `pluginrel_6ad01a9215e88191829245c5571fd160`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root `plugin.json`: `0.7.1` read back;
- platform `.codex-plugin/plugin.json`: `0.7.1` read back;
- `skills/design/SKILL.md`: four Design modes, evidence-triggered cross-Skill composition and return-to-Design contract read back;
- Design module map: mode-aware pipeline and nested composition read back;
- Microsoft final review: rendered evidence before review and re-render/re-review correction gate read back;
- Project Governance/global routing/capability composition/global routing template/adoption: evidence-triggered composition and interaction-vs-business workflow discriminator read back.

`WEB_PLUGIN_SYNC_071`: `PASS`.

## Local distribution state

The last directly observed Local Codex installation on Air remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

No local v0.7.x runtime freshness is inferred without a fresh local readback.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Task state

Task `EG-DESIGN-ROUTING-HARDENING-083`: `COMPLETE`.

Source PR #32 is merged, GitHub Plugin v0.7.1 is released, and the existing private Web Plugin has been synchronized/read back at v0.7.1.

The remaining local observation is a distribution/runtime freshness check, not an open source/release blocker for Task 083.

## Control identity

Released semantic Plugin identity:

`208279e5f3b7974c13a3446a3db2e8f27de7b688`

Control-only STATUS/TASK closeout commits after this release may move `main` without changing the released v0.7.1 semantic source identity above.
