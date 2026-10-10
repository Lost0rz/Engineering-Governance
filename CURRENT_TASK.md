# CURRENT TASK — Plugin v0.4.0 Runtime Cache Activation

Task ID: `EG-PLUGIN-V0.4.0-RUNTIME-CACHE-ACTIVATION-044`

State: `AUTHORIZED`

Mode: `LOCAL_PLUGIN_ACTIVATION_CORRECTIVE`

## Objective

Refresh the sole enabled Engineering Governance Codex plugin registration/runtime cache so the active runtime resolves to Plugin v0.4.0, without modifying repository source, Plugin payload semantics, or the already-verified global routing block.

## Accepted prior evidence

- Canonical source: `/Volumes/Jack-Dev/Projects/Engineering-Governance`.
- Source `main` was clean and matched `origin/main` at `221bcd597e1b45aceae73bf1088792ca6df6cfb4` in the latest local receipt.
- Official Plugin v0.4.0 release asset verified: size `54754`, SHA-256 `1d0d791acc167f47ff5d91b523528f53fed027f2bc9eac8d0b938983903a7922`.
- Installed plugin source path `/Users/ox_miles/.codex/plugins/engineering-governance` reports version `0.4.0` and exactly three Skills: `project-governance`, `domain-navigation`, `incident-doctor`.
- Previous `0.3.0` install backup is verified.
- Global managed routing block count is `1`; unrelated rules preserved; repeated adoption is idempotent.
- Read-only routing acceptance passed.
- Sole enabled registration still has stale cache metadata at `/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.3.0/plugin.json`.
- Root cause boundary is registration/runtime-cache activation, not source or routing content.

## Hard constraints

Do not:

- edit repository source or tests;
- rebuild or republish Plugin v0.4.0;
- edit the verified Plugin payload manually;
- rewrite the global routing block;
- delete plugin caches speculatively;
- delete or alter the verified 0.3.0 backup;
- touch unrelated plugins;
- touch Merloom, Gift, MemoX, InvestDesk, FloatTabs, DevBoard, RemoteOrbit, freqtrade, plineahome, or wedding-website;
- claim activation merely because the source install directory says `0.4.0`.

Use supported Codex/plugin marketplace refresh or reinstall mechanisms where available. If a client restart is required, record it explicitly.

## Gate 0 — fresh control and source identity

1. From `/Volumes/Jack-Dev/Projects/Engineering-Governance`, run `git fetch origin --prune`.
2. Require local `main` clean and ff-only synchronizable to fresh `origin/main`; sync ff-only if only behind.
3. Read fresh `AGENTS.md`, `CURRENT_STATUS.md`, and this task.
4. Require this Task ID exactly.
5. Record installed source plugin version and stale cache version before mutation.

## Gate 1 — identify the authoritative registration path

Inspect metadata only for the Engineering Governance registration:

- `~/.agents/plugins/marketplace.json` and any other marketplace file actually referenced by Codex;
- relevant non-secret plugin registration entries in `~/.codex/config.toml`;
- `codex plugin marketplace list` output if supported;
- the enabled registration name/source/path/version;
- the stale cache path and its `plugin.json` version.

Do not dump unrelated config values or secrets.

Prove which marketplace/registration owns `engineering-governance-personal/engineering-governance` before refreshing anything.

If the owner cannot be identified, STOP with the smallest next metadata probe.

## Gate 2 — supported refresh first

Use the supported Codex/plugin mechanism appropriate to the identified registration.

Preferred order:

1. refresh/upgrade the owning marketplace/source using supported `codex plugin marketplace ...` commands if applicable;
2. refresh/reinstall the Engineering Governance plugin registration through the supported local/plugin UI or CLI mechanism if required;
3. restart/reopen the relevant Codex/ChatGPT desktop client only if the supported install model requires restart to load the refreshed cached copy.

Do not manually `rm -rf` the cache as the first action.

If the current local registration mechanism has no supported refresh surface, STOP and report that fact before any direct cache surgery.

## Gate 3 — activation proof

After refresh/reinstall/restart as applicable, prove all of the following:

- exactly one enabled Engineering Governance registration remains;
- active/cached plugin version resolves to `0.4.0`;
- active payload contains exactly the three expected Skills;
- the loaded/cached copy corresponds to the verified v0.4.0 payload/source identity;
- no enabled `0.3.0` registration remains;
- global managed routing block count remains `1` and unrelated global content is unchanged;
- canonical repository remains clean and matches fresh `origin/main`.

If both 0.3.0 and 0.4.0 cache directories coexist, that alone is not failure. Failure is an enabled registration still resolving to 0.3.0. Do not delete historical cache entries unless the supported plugin mechanism does so or a later task authorizes cleanup.

## Gate 4 — representative runtime acceptance

Use a new supported Codex/ChatGPT session/context after activation if restart/new-session semantics apply.

Verify read-only/runtime routing from the active plugin:

- Project Governance available as default engineering route;
- Domain Navigation available conditionally;
- Incident Doctor available reactively;
- reported/loaded plugin version is v0.4.0 where the runtime exposes version identity.

No business repository mutation is allowed for this acceptance.

## Gate 5 — safe final state

Require:

```text
SOURCE_MODIFIED=NO
PLUGIN_PAYLOAD_MANUALLY_EDITED=NO
GLOBAL_ROUTING_REWRITTEN=NO
UNRELATED_PLUGINS_TOUCHED=NO
BUSINESS_PROJECTS_TOUCHED=NO
```

## Final receipt

```text
EG_PLUGIN_V040_RUNTIME_CACHE_ACTIVATION

CONTROL_HEAD:
LOCAL_HEAD:
SOURCE_CLEAN:

REGISTRATION:
  marketplace_or_source:
  registration_name:
  enabled:
  source_path:
  pre_cache_path:
  pre_cache_version:

REFRESH:
  mechanism:
  marketplace_refresh_performed:
  plugin_reinstall_or_refresh_performed:
  client_restart_required:
  client_restart_performed:

ACTIVE_RUNTIME:
  active_cache_path:
  active_version:
  expected_skills:
  enabled_0_3_registration_remaining:
  enabled_registration_count:

GLOBAL_ROUTING:
  managed_block_count:
  unrelated_rules_preserved:

RUNTIME_ACCEPTANCE:
  project_governance:
  domain_navigation:
  incident_doctor:
  v0_4_activation_proven:

SOURCE_MODIFIED: NO
PLUGIN_PAYLOAD_MANUALLY_EDITED: NO
GLOBAL_ROUTING_REWRITTEN: NO
UNRELATED_PLUGINS_TOUCHED: NO
BUSINESS_PROJECTS_TOUCHED: NO

FINAL_STATE:
EG_PLUGIN_V040_RUNTIME_ACTIVATION_PASS

or

STOP_<exact reason>
```
