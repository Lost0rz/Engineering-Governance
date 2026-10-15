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
- asset SHA-256 `7cd695bc8b7f8302de06a8b36c1e5f5d8afabb8b874416a40ca42b6481fcf06b`;
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

PR:

`#32 — feat: harden Design routing composition` — Draft / Unmerged

## v0.7.1 candidate result

Accepted semantic candidate:

`f0f1ebf6a9c7c49c106955cfb84940a645635dc4`

Pre-merge workflow:

- workflow: `Release Plugin v0.7.1`;
- run: `38658235439` / run #2;
- event: `pull_request`;
- conclusion: `success`;
- `Verify release source`: PASS;
- `Build exact Plugin payload`: PASS;
- publication: skipped on PR as intended.

An earlier run `38658175876` failed only because the release gate required the literal wording `resume at the declared stage`; the contract was made explicit and run #2 passed. It is not acceptance evidence for the candidate.

`V071_PREMERGE_ACCEPTANCE`: `PASS`.

## Design routing hardening now in candidate

The candidate changes Design from hard anti-cross-Skill isolation to **evidence-triggered composition**:

- Design remains the primary bounded owner after entry;
- a cross-Skill call requires a concrete unresolved dependency, material decision impact, smallest owning capability, bounded expected return and explicit resume stage;
- `domain-navigation` is explicitly valid when a needed backend/product authority/source/symbol/state-owner/runtime/test route is genuinely unclear;
- `solution-design` is explicitly valid when that route is known but material business/state/API/data-flow ownership remains ambiguous;
- other Skills remain available only on their real trigger;
- no Skill is called for general enrichment, completeness, generic second opinion or because it is installed;
- the bounded result returns to the originating capability/stage rather than restarting the routing tree.

Frontend workflow ownership is now explicit:

- interaction workflow -> `design`;
- business/state workflow -> `solution-design` when materially ambiguous.

Design now has four modes:

- `AUDIT_ONLY`;
- `DESIGN_SPEC`;
- `DESIGN_IMPLEMENT`;
- `FINAL_REVIEW`.

For full implementation with rendering support, the candidate sequence is:

`context/audit → Anthropic → admin pattern when applicable → bounded design spec → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`.

The nine-Skill architecture, existing Design source modules, Project Profile boundary, source provenance/licenses, receipt/handoff rules and Plugin payload boundary remain preserved.

## Release state

`0.7.1` is **not yet published**. Published GitHub/Web baseline remains `0.7.0` until PR #32 is merged, the main v0.7.1 release workflow succeeds, the release asset is verified, and the existing private Web Plugin is updated/read back.

## Local distribution state

The last directly observed Local Codex installation on Air remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

No local v0.7.x runtime freshness is inferred without a fresh local readback.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Control identity

Current released semantic identity remains v0.7.0:

`8284f0f138427dd329cd50983046baf78ec110ce`

Task 083 control-only STATUS/TASK commits may move the branch HEAD without changing the accepted v0.7.1 semantic candidate above.
