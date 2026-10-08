# CURRENT TASK — Codex Plugin Packaging and Local Install Test

Task ID: `EG-CODEX-PLUGIN-PACKAGING-033`

State: `AUTHORIZED_FOR_LOCAL_PACKAGING_AND_INSTALL_TEST`

Mode: `CODEX_PLUGIN_PACKAGING`

## Objective

Package the existing Engineering-Governance repository as one local Codex plugin named `engineering-governance`, containing the existing three Skills unchanged, then install and validate it through a personal local marketplace.

## Authoritative start baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Remote start HEAD before this control transition: `32ad185bbe5f5f058ff8c40d7a0ee0cffe1c8c2b`.
- Local executor previously reported a clean but stale checkout at `e4e3ed975b46617c29b9bf83346a835bf0be8420`.
- The executor must fetch the verified canonical remote and fast-forward clean local `main` to the live remote `main` containing this task before doing any packaging work.

## Existing payload — must remain unchanged

Reuse exactly these existing Skill directories:

- `skills/project-governance/`
- `skills/domain-navigation/`
- `skills/incident-doctor/`

Do not rewrite, copy, rename, or semantically modify their `SKILL.md`, references, assets, or scripts as part of packaging.

## Authorized repository change

Add only the minimum plugin packaging metadata required by the current supported OpenAI/Codex plugin format.

Preferred repository change:

- root `plugin.json` portable manifest.

A `.codex-plugin/plugin.json` compatibility manifest is allowed only if current official OpenAI documentation or actual local-host validation shows it is required for this local test. Do not add it by default merely for redundancy.

The plugin is Skills-only. Do not add MCP configuration, apps, hooks, commands, daemons, databases, runtimes, enforcement, analytics, telemetry, installers, or bootstrap CLIs.

## Authorized local user changes

For this test only, the executor may create/update user-local Codex plugin/marketplace state described by current official OpenAI documentation, including:

- a personal local plugin copy under the user's Codex plugin area;
- `~/.agents/plugins/marketplace.json` or the equivalent currently documented personal marketplace path;
- installation/enabled state needed for the local plugin test.

Preserve any pre-existing personal marketplace entries. Do not replace unrelated plugin configuration. Back up the prior marketplace file before editing if one exists.

Do not add plugin files or marketplace configuration to RemoteOrbit, InvestDesk, Merloom, MemoX, FloatTabs, or any other business repository.

## Plugin identity

- package name: `engineering-governance`
- display name: `Engineering Governance`
- description: concise statement that the plugin supplies reusable project governance, domain navigation, and evidence-gated incident investigation Skills.
- package version: choose an explicit initial plugin package version and report it. Do not imply that the package version is an existing Git tag unless that Git tag actually exists.

## Installation validation

After packaging and local installation, start a fresh supported Codex/ChatGPT desktop Codex session and validate:

1. the local marketplace recognizes `engineering-governance`;
2. the plugin can be installed/enabled without MCP or authentication requirements;
3. all three Skills are discoverable from the installed plugin;
4. direct invocation of `project-governance` in RemoteOrbit can read the target controls and summarize the current task/authority read-only;
5. direct invocation of `domain-navigation` can route the current RemoteOrbit task to focused source/test boundaries without creating a new Domain Map;
6. direct invocation or trigger-decision test of `incident-doctor` correctly evaluates whether a qualifying incident exists without adding probes or mutating the target.

The RemoteOrbit validation is read-only. No RemoteOrbit source, control, branch, PR, worktree, runtime, settings, diagnostic behavior, or installed app may be changed by this packaging task.

## Verification level

`V0 + local plugin discovery/install acceptance`.

Reason: repository changes are packaging metadata only, but successful local discovery/install cannot be established by file inspection alone.

Required repository verification:

- exact changed paths;
- JSON parse/schema sanity for plugin manifest(s);
- prove the three Skill trees are byte-for-byte unchanged relative to the authorized baseline;
- `git diff --check`;
- clean final task branch/worktree;
- pushed branch HEAD matches remote branch HEAD.

Required local-install evidence:

- plugin source/copy path;
- personal marketplace path;
- plugin entry identity/version;
- install/enabled result;
- fresh-session discovery result for all three Skills;
- read-only RemoteOrbit smoke-test results.

## Branch/workspace

Use a dedicated task branch such as:

`codex/engineering-governance-plugin-packaging-v1`

Create it only after local `main` is fast-forwarded to the live authoritative remote task. A separate clean worktree is optional, not mandatory, because the reported local checkout is clean; do not invent a worktree if it provides no safety value.

## Acceptance criteria

PASS only if:

- local baseline is reconciled to the live remote control plane before work;
- the repository packaging change is minimal and contains no Skill semantic change;
- the personal local marketplace/install preserves unrelated existing configuration;
- the plugin is actually visible/installable in a supported local Codex surface;
- the installed plugin exposes all three intended Skills;
- the RemoteOrbit smoke tests are read-only and route correctly;
- no MCP server, hook, runtime, daemon, database, installer, bootstrap CLI, or business-repository mutation is introduced.

## STOP conditions

STOP and report without destructive correction if:

- local `main` cannot fast-forward to the authoritative remote because of unique local work or divergence;
- current official OpenAI documentation contradicts the assumed portable/local-marketplace format in a way that changes scope materially;
- packaging appears to require changing Skill contents;
- an existing personal marketplace cannot be safely preserved;
- the local host cannot discover the plugin without introducing MCP/runtime machinery outside this task;
- RemoteOrbit validation would require target mutation.

## Handoff

Return exactly enough evidence for independent review:

```text
TASK_ID: EG-CODEX-PLUGIN-PACKAGING-033
REMOTE_CONTROL_HEAD:
LOCAL_BASELINE_AFTER_SYNC:
TASK_BRANCH:
FINAL_BRANCH_HEAD:
REMOTE_BRANCH_HEAD:
LOCAL_REMOTE_MATCH:
REPO_CHANGED_PATHS:
PLUGIN_MANIFEST_PATH:
PLUGIN_NAME:
PLUGIN_VERSION:
SKILL_CONTENT_UNCHANGED: YES/NO
MCP_ADDED: NO
HOOKS_ADDED: NO
RUNTIME_ADDED: NO
PERSONAL_PLUGIN_PATH:
PERSONAL_MARKETPLACE_PATH:
PREEXISTING_MARKETPLACE_PRESERVED: YES/NO/NOT_APPLICABLE
PLUGIN_DISCOVERED: PASS/STOP
PLUGIN_INSTALLED_ENABLED: PASS/STOP
PROJECT_GOVERNANCE_DISCOVERY: PASS/STOP
DOMAIN_NAVIGATION_DISCOVERY: PASS/STOP
INCIDENT_DOCTOR_TRIGGER_TEST: PASS/STOP
REMOTEORBIT_MUTATED: NO
DIFF_CHECK:
WORKING_TREE:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_AUDIT / STOP
```

Do not merge the packaging branch under this task. Stop at independent Web audit.
