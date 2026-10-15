# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.7.0` while Task `EG-DESIGN-ROUTING-HARDENING-083` is active.

Released semantic Plugin identity:

`8284f0f138427dd329cd50983046baf78ec110ce`

Published v0.7.0 evidence remains valid:

- source PR #31 — merged;
- pre-merge acceptance run `38655255661` — success;
- main release run `38655371941` — success;
- tag `plugin-v0.7.0`;
- GitHub Release ID `413275429`;
- asset `engineering-governance-plugin.zip`;
- asset SHA-256 `7cd695bc8b7f8302de06a8b36c1e5f5d8afabb8b874416a40ca42b6481fcf06b`;
- package entries `61`;
- package scope `plugin.json + skills/**` only;
- top-level Skills exactly `9`.

## Published Web Plugin baseline

The existing private personal Web Plugin is currently v0.7.0:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web release ID: `pluginrel_6ad01392fbec81919fb25c380af12954`;
- scope/discoverability: `USER / PRIVATE`;
- v0.7.0 root/platform manifests and Design multi-module files were read back successfully.

`WEB_PLUGIN_SYNC_070`: `PASS`.

## Active task

Task `EG-DESIGN-ROUTING-HARDENING-083` is `ACTIVE` on branch:

`codex/design-routing-hardening-v071`

Start main HEAD:

`06301c8ff5c074ea16e26a4e01a0755d52d43e24`

Target Plugin version:

`0.7.1`

The task hardens Design composition after the v0.7.0 routing audit. It does **not** add new top-level Skills or new external Design source modules.

Target changes:

- replace hard anti-cross-Skill wording with evidence-triggered composition;
- keep Design as primary bounded owner while allowing necessary calls to `domain-navigation`, `solution-design`, `agent-handoff`, `evidence-audit`, `execution-orchestrator` or `incident-doctor` when their real trigger exists;
- require a concrete unresolved dependency, material Design impact, smallest capability, bounded expected return and explicit resume stage for each cross-Skill call;
- distinguish interaction workflow (`design`) from business/state workflow (`solution-design` when materially ambiguous);
- add Design modes: `AUDIT_ONLY`, `DESIGN_SPEC`, `DESIGN_IMPLEMENT`, `FINAL_REVIEW`;
- make rendered evidence available before Microsoft final review when supported, then re-render/re-review material corrections before final visual acceptance;
- preserve existing Project Profile authority boundary, source provenance/licenses, receipts, top-level Skill count and payload scope.

## Local distribution state

The last directly observed Local Codex installation on Air remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

No local v0.7.x runtime freshness is inferred without a fresh local readback.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Control identity

Current released semantic identity remains v0.7.0:

`8284f0f138427dd329cd50983046baf78ec110ce`

Task 083 branch/control commits do not become published Plugin identity until the v0.7.1 release boundary succeeds.
