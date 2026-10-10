# CURRENT TASK — Project Storage Affinity Rule

Task ID: `EG-PROJECT-STORAGE-AFFINITY-045`

State: `AUTHORIZED`

Mode: `BOUNDED_REUSABLE_RULE_CHANGE`

Authoritative branch: `main`

Implementation branch: `codex/project-storage-affinity-v1`

## Objective

Update Engineering Governance so Project Governance derives project-controlled development storage from the canonical project's actual storage location rather than from a universal host path or external-volume default.

This is a bounded reusable-rule change. Do not add a new Skill, storage daemon, installer, global filesystem redirect, or machine-wide `TMPDIR` policy.

## Owner-approved semantics

The accepted rule is:

> Development storage follows the canonical project location.

Required behavior:

1. Resolve the canonical project root before selecting project-controlled worktree/staging/diagnostic/archive paths.
2. If the canonical project root is on external storage, project-controlled durable development assets should stay on that same storage authority.
3. If the canonical project root is on local host storage, project-controlled durable development assets should stay local.
4. Explicit project-specific path/authority rules override the derived same-storage default.
5. Do not hard-code `/Volumes/Jack-Dev`, the Mac mini, or any one host as a universal development-storage target.
6. Do not place durable or unique project state in unrelated convenience locations such as `/private/tmp`, `/tmp`, Desktop, Downloads, or arbitrary home-directory paths.
7. OS/tool-required ephemeral scratch may use system temporary locations, but any unique/durable project evidence or state must be moved/retained under the project's storage authority before task closure.
8. Machine-operational state is separate: CI runner runtime, LaunchAgents, Homebrew/package-manager services, host caches, system temp, and other host runtime state may remain machine-local unless the project explicitly owns them as portable data.
9. The global managed routing block remains concise and unchanged unless inspection proves a minimal routing reference is strictly required. Do not duplicate the storage procedure into global routing.

Examples are illustrative only, not hard-coded policy:

- canonical project under `/Volumes/Jack-Dev/Projects/MemoX` => project-controlled durable worktrees/diagnostics/archives remain on that external storage authority;
- canonical project under `/Users/.../Merloom` => project-controlled durable development state remains on local storage;
- CI runner state may remain under the host CI runtime location even when the governed project's source authority is external.

## Gate 0 — fresh baseline

1. From `/Volumes/Jack-Dev/Projects/Engineering-Governance`, run `git fetch origin --prune`.
2. Require local `main` clean and ff-only synchronizable to fresh `origin/main`.
3. Sync ff-only.
4. Read fresh root `AGENTS.md`, `CURRENT_STATUS.md`, this task, `skills/project-governance/SKILL.md`, `skills/project-governance/references/development-flow.md`, and `skills/project-governance/references/workspace-lifecycle.md`.
5. Inspect relevant assets/templates/tests/packaging checks before editing so the rule extends the existing authority/workspace model rather than creating a parallel model.
6. STOP on unexpected dirty source or overlapping active writer.

## Gate 1 — prove current gap

Before editing, identify where current reusable guidance selects/permits worktree, temporary task state, diagnostic evidence, or archive locations.

Record concise evidence for:

- whether storage-location affinity is currently absent or ambiguous;
- whether any current reusable text encourages `/private/tmp`, arbitrary home paths, or fixed external-volume paths;
- which existing Project Governance files are the minimum authoritative surfaces for the rule.

Do not perform a broad rewrite.

## Gate 2 — minimal implementation

Create branch:

`codex/project-storage-affinity-v1`

Implement the rule in the smallest coherent existing authority surfaces.

Expected primary surfaces to inspect/use:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/references/workspace-lifecycle.md`

Update root `AGENTS.md`, README, templates, or other references only if needed for semantic consistency or existing verification contracts.

Requirements:

- one canonical concept, not repeated divergent rules;
- no mandatory per-project storage manifest for ordinary projects;
- canonical project location is the default routing signal;
- explicit project-local authority/path rules can override it;
- distinguish durable project-controlled assets from machine/runtime state;
- distinguish durable evidence/state from ephemeral OS/tool scratch;
- avoid absolute host/user paths in reusable normative text except as clearly non-normative examples;
- do not change Skill count or routing model;
- do not bump/release/install Plugin version in this task.

## Gate 3 — focused verification

This is `V0` reusable documentation/Skill behavior, but because it ships in the Plugin payload, verify at least:

1. focused text/structure consistency across changed Project Governance files;
2. no contradictory storage guidance remains in reusable Project Governance payload;
3. no new universal Jack-Dev/Mac-mini path rule exists;
4. exactly three top-level Skills remain;
5. existing package/payload validation relevant to changed files passes;
6. changed paths are limited to the bounded rule/control surfaces;
7. root/global routing managed block contract is not duplicated or broadened accidentally.

If existing automated tests cover Skill/package structure, run the focused applicable set. Do not invent a broad product test suite for a documentation rule.

## Gate 4 — handoff

Commit and push the implementation branch.

Do not merge.
Do not publish a Plugin release.
Do not modify the installed v0.4.0 Plugin/runtime.
Do not modify business projects.

Return evidence for independent Web audit.

## Final receipt

```text
EG_PROJECT_STORAGE_AFFINITY_045

CONTROL_HEAD:
BASELINE_MAIN:
IMPLEMENTATION_BRANCH:
FINAL_BRANCH_HEAD:
REMOTE_BRANCH_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:

CURRENT_GAP:
  storage_affinity_missing_or_ambiguous:
  conflicting_or_fixed_path_guidance_found:
  authoritative_surfaces_selected:

IMPLEMENTATION:
  changed_paths:
  canonical_rule_summary:
  explicit_project_override_preserved:
  machine_runtime_exception_preserved:
  ephemeral_temp_boundary_preserved:
  hardcoded_jack_dev_rule_added: NO
  new_skill_added: NO
  global_routing_rewritten: NO
  plugin_version_changed: NO

VERIFICATION:
  focused_checks:
  package_or_structure_checks:
  exactly_three_top_level_skills:
  contradictory_storage_guidance_remaining:
  scope_check:

SOURCE_MODIFIED: YES
INSTALLED_PLUGIN_MODIFIED: NO
PLUGIN_RUNTIME_MODIFIED: NO
BUSINESS_PROJECTS_TOUCHED: NO

FINAL_STATE:
EG_PROJECT_STORAGE_AFFINITY_READY_FOR_AUDIT

or

STOP_<exact reason>
```
