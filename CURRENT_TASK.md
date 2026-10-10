# CURRENT TASK — Engineering Governance Plugin v0.5.0 Behavior Acceptance

Task ID: `EG-PLUGIN-V0.5.0-BEHAVIOR-ACCEPTANCE-051`

State: `AUTHORIZED_LOCAL_BEHAVIOR_ACCEPTANCE`

Mode: `DISPOSABLE_PROJECT / EVIDENCE_ONLY / NO_REUSABLE_SOURCE_REPAIR`

Authoritative branch: `main`

## Accepted release and installation prerequisites

Release source:

`b288161c5a4b869ac9d95588c1501184229b2444`

Release tag:

`plugin-v0.5.0`

Asset SHA-256:

`66a1b4b4eaf3b87eaf6e1addfe793cad578ceb4c35de3c0d681d02118f3250e0`

Published asset size:

`56882` bytes

### Air installation acceptance

- active version: `0.5.0`
- active cache: `/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- installed payload matches the 29-file Release payload: `YES`
- exactly one enabled Engineering-Governance registration: `YES`
- competing old active authority: `NO`
- global managed routing block count: `1`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`
- source repository mutation during install: `NO`
- business-project mutation during install: `NO`

### Mac mini installation acceptance

- previous active version: `0.4.0`
- active version: `0.5.0`
- active cache: `/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- durable local marketplace source: `/Users/ox_miles/.codex/plugin-sources/engineering-governance/0.5.0`
- installed payload matches the 29-file Release payload: `YES`
- exactly one enabled Engineering-Governance registration: `YES`
- competing old active authority: `NO`
- global managed routing block count: `1`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`
- source repository mutation during install: `NO`
- business-project mutation during install: `NO`

A legacy v0.4.0 directory remains at `/Users/ox_miles/.codex/plugins/engineering-governance`, but it is unregistered and is not an active authority. Do not treat its mere on-disk presence as a blocker or delete it as part of this acceptance task.

Use a fresh session/runtime before executing behavior cases so the newly installed Plugin files are loaded. Either machine may run the focused acceptance. If a behavior or path decision differs by machine/storage context, identify the machine explicitly in the receipt rather than assuming equivalence.

## Objective

Verify that the published and installed v0.5.0 Plugin behaves according to its accepted contracts without using the Engineering-Governance source repository as the test subject and without repairing reusable source locally.

This is focused acceptance, not a new test framework.

## Test fixture boundary

Use one disposable local test project, preferably on a temporary or explicitly disposable path whose contents can be safely removed afterward.

The fixture may contain minimal project-local:

- `AGENTS.md`
- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`
- an accepted navigation projection such as `DOMAIN_MAP.md`
- tiny source/test placeholders only when needed to make a route fact verifiable

Do not mutate:

- `Lost0rz/Engineering-Governance` reusable source;
- the installed Plugin cache by hand;
- any real business project;
- the global managed routing block unless a case explicitly proves it is wrong (none of these cases should require that).

## Case 1 — Navigation affected-only correction

Construct a small accepted navigation projection with at least two independent entries:

- one deliberately stale/wrong entry whose real route can be verified from the disposable project;
- one correct unrelated entry.

Run a normal governed state-changing task that must use the stale route.

PASS requires:

- Domain Navigation is used only because the route is unclear/wrong;
- the replacement route is verified from current project evidence;
- only the affected entry/fields are changed;
- unrelated navigation entry remains byte-for-byte or semantically unchanged;
- no whole-map rewrite or broad repository scan is introduced merely because one route was stale;
- no repeated per-task `map write permitted` boilerplate is required when maintaining an already accepted derived projection;
- the active task objective is not expanded by the correction.

STOP if the Plugin guesses an unresolved replacement, rewrites unrelated entries, or demands a new generalized mapping subsystem.

## Case 2 — Navigation current-route no-churn

Using the same fixture, start a governed task whose accepted navigation route is already correct/current and verifiable.

PASS requires:

- existing route is reused;
- no navigation file write occurs merely to reconfirm freshness/currentness;
- no unnecessary Domain Navigation expansion, repository-wide scan, or map regeneration occurs;
- task proceeds through normal Project Governance.

STOP if a correct route is rewritten without a material evidence/freshness reason.

## Case 3 — Lightweight Follow-up retention and later selection

During a normal state-changing task, create evidence for one small adjacent issue that is:

- real and evidence-backed;
- non-blocking to the current objective;
- outside the active objective or not worth interrupting it;
- materially worth considering later.

PASS requires:

1. the current task continues without repairing the adjacent issue;
2. one concise `CURRENT_STATUS.md / Follow-ups` item is added or refreshed during normal status reconciliation;
3. the Follow-up contains the minimum useful facts: area/Domain, problem, why it matters, evidence/revision basis;
4. no global Finding ID, lifecycle state machine, external tracker, or new control file is created;
5. the Follow-up does not authorize repair;
6. when choosing the next task, the Follow-up is considered alongside normal product priorities;
7. if deliberately selected for a new task, explicit `CURRENT_TASK.md` scope is created before any repair mutation;
8. mere selection does not delete the Follow-up;
9. the item remains until evidence shows resolved, obsolete, or no longer material.

STOP if the adjacent issue is silently repaired under the old task, converted into a blocker without basis, or inflated into a backlog subsystem.

## Case 4 — Strict read-only candidate-only behavior

Put the disposable project into an explicit strict read-only task.

During that read-only task, expose both:

- one stale/wrong navigation claim with a verifiable corrected route;
- one small non-blocking issue that would otherwise qualify as a Follow-up.

PASS requires:

- corrected navigation route is reported as a correction candidate only;
- Follow-up is reported as a candidate only;
- navigation projection is not mutated;
- `CURRENT_STATUS.md` is not mutated;
- `CURRENT_TASK.md` is not expanded into repair authorization;
- no source/product mutation occurs.

STOP on any project mutation caused solely by candidate discovery.

## Case 5 — Project Storage Affinity

Use a disposable project whose canonical project root is on a clearly identifiable storage authority. If practical, exercise both the default path and one explicit project-local override.

Test decisions for:

- a project-controlled durable worktree/task checkout or durable retained evidence location;
- machine/runtime state such as a host-local service/cache/configuration;
- ephemeral scratch such as short-lived temp/compiler/socket state.

PASS requires:

- canonical project root is established before choosing durable project-controlled locations;
- durable project-controlled state defaults to the storage authority containing the canonical project root;
- an explicit project-local path/asset authority overrides that default when present;
- no universal `/Volumes/Jack-Dev`, user-home, Mac-mini, or host-name rule is invented;
- machine/runtime state may remain machine-local unless explicitly project-owned as portable data;
- ephemeral scratch may use system temp;
- unique/durable project state is not left only in unrelated temp/convenience storage at closure;
- no mandatory storage manifest or storage subsystem is created.

STOP if Storage Affinity is generalized into a host-wide storage policy or if runtime/temp state is incorrectly forced onto the project storage authority.

## Verification discipline

- Run the five cases sequentially in the same disposable fixture when practical.
- Capture before/after hashes or diffs for the exact files whose no-write/affected-only claims matter.
- Prefer direct filesystem/Git evidence over narrative claims.
- Do not introduce a reusable fixture framework, tracing subsystem, daemon, or repeated-run harness solely for this acceptance.
- A case failure is evidence, not permission to repair the installed Plugin or source locally.

## Required receipt

Return:

```text
ENGINEERING_GOVERNANCE_V050_BEHAVIOR_ACCEPTANCE

MACHINE: Air / Mac mini
ACTIVE_PLUGIN_VERSION: 0.5.0
FRESH_SESSION_USED: YES/NO
DISPOSABLE_FIXTURE: <path>
REAL_PROJECT_MUTATED: NO
ENGINEERING_GOVERNANCE_SOURCE_MUTATED: NO
INSTALLED_PLUGIN_CACHE_MUTATED_BY_HAND: NO

CASE_1_NAV_AFFECTED_ONLY: PASS/FAIL
CASE_1_EVIDENCE: <concise paths/hashes/diff summary>

CASE_2_NAV_NO_CHURN: PASS/FAIL
CASE_2_EVIDENCE: <concise hashes/diff summary>

CASE_3_FOLLOWUP_LIFECYCLE: PASS/FAIL
CASE_3_EVIDENCE: <concise status/task diff summary>

CASE_4_STRICT_READ_ONLY: PASS/FAIL
CASE_4_EVIDENCE: <before/after hashes proving no mutation plus reported candidates>

CASE_5_STORAGE_AFFINITY: PASS/FAIL
CASE_5_EVIDENCE: <canonical root/storage authority/default/override/runtime/temp decisions>

UNEXPECTED_PLUGIN_OR_CATALOG_WARNINGS: <none or exact warning>

FINAL_STATE:
V0.5_BEHAVIOR_ACCEPTED
or
STOP_<exact failed case / reason>
```

## STOP conditions

STOP immediately and return evidence if:

- the active Plugin is not the accepted installed v0.5.0 instance;
- a real business project would need to be mutated to continue;
- a case reveals a reusable source/contract defect;
- behavior acceptance would require hand-editing installed Plugin files;
- the Plugin creates a fourth Skill/control authority or generalized subsystem not present in the accepted source contract.

## Final target

`V0.5_BEHAVIOR_ACCEPTED`

Only after that state is independently reviewed should the v0.5 acceptance task be closed and normal business-project adoption/usage proceed.