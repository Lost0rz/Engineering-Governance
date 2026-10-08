# CURRENT TASK — Domain Navigation Authority Gate Corrective

Task ID: `EG-DOMAIN-NAV-AUTHORITY-GATE-035`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `REUSABLE_SKILL_CORRECTIVE`

## Objective

Fix one repeated cross-project Domain Navigation defect: the Skill must not infer or treat an active/current task as authoritative when task/control freshness is materially unresolved.

Issue ID:

`DN-001 — do not route from stale or unverified task authority`

## Verified evidence basis

### RemoteOrbit reproduction

A read-only Domain Navigation trial could not verify the current project control authority from the local checkout, then inferred a current `non-seize HID audit / diagnostic monitor mode` task from a stale branch name and local source state. That inference was not the live remote task.

### FloatTabs reproduction

A second unprompted read-only Domain Navigation trial explicitly observed:

- local HEAD `0a3588bf6e4675d897aa02b336c1349ef090b692`;
- local cached upstream relation ahead 1 / behind 25;
- remote refs were not refreshed;
- local controls represented an older topology-probe phase.

Despite that unresolved freshness, it continued to route the old local topology-probe task to source, symbols, and tests. Independent live evidence showed remote `main` at `569e43783a98c8caca681ce8139ec87dd4fa276e`, PR #115 already merged, and the remote controls themselves lagging the completed merge state. The correct current-task navigation action was therefore to stop and return to Project Governance reconciliation.

These two independent project observations satisfy the repository rule for a repeated reusable Skill corrective.

## Authorized change scope

Primary files:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/mapping-workflow.md`

`skills/domain-navigation/references/evidence-rules.md` may be changed only if one concise supporting rule is necessary to make the entry gate unambiguous. Do not expand other Domain Navigation material merely for consistency prose.

After the corrective behavior is independently validated on the task branch, `plugin.json` may be bumped from package version `0.1.0` to `0.1.1` as release metadata preparation. Do not create a Release or tag under this task.

Do not modify:

- `project-governance` Skill content;
- `incident-doctor` Skill content;
- business repositories;
- runtime, MCP, hooks, telemetry, indexing, Repo Map machinery, daemons, databases, installers, or diagnostics.

## Required semantic rule

For **current-task navigation**:

1. Establish the task/control authority needed for the requested routing decision before treating any task as current.
2. A local `CURRENT_TASK.md` or similar control file is not automatically current authority when repository freshness is materially unresolved.
3. Do not infer current active task or executable authority from:
   - branch names;
   - dirty/staged/untracked files;
   - local code shape;
   - stale or conflicting control files;
   - historical documents;
   - chat context or memory.
4. If current task/control authority is unavailable, materially stale, contradictory, or cannot be verified enough for the requested current-task route, stop current-task navigation and hand back to Project Governance reconciliation. Do not continue source/symbol/test routing under a guessed task.
5. This is not a generic requirement to fetch every remote or force perfect freshness. The gate applies only when unresolved freshness/authority is material to the requested navigation decision.

## Explicit bounded-navigation exception

The corrective must preserve useful read-only navigation when the user explicitly scopes a historical or fixed snapshot, for example:

- “analyze commit X”;
- “map this historical branch”;
- “locate the domain for this file/symbol without claiming it is the current task.”

In that case, navigation may proceed against the specified snapshot, but the output must clearly classify it as bounded/historical snapshot navigation and must not present it as current task authority or authorization.

## Regression acceptance

Validate four cases with the smallest sufficient evidence. Do not create new telemetry or a test harness merely for this corrective.

### Case A — RemoteOrbit stale/unavailable current authority

Expected:

`STOP_CURRENT_TASK_NAVIGATION`

The Skill must not infer the current task from the historical branch/source state.

### Case B — FloatTabs stale checkout

Given the reproduced stale-local condition and unresolved remote/control drift, expected:

`STOP_CURRENT_TASK_NAVIGATION`

The Skill must not route the old topology-probe work as the current task.

### Case C — fresh verified current task

Given a project/snapshot where the current task authority is sufficiently verified, navigation must continue normally:

`task -> affected capability -> semantic authority -> source -> key symbols -> focused tests`

The new gate must not create a blanket STOP or require unnecessary repository-wide freshness work.

### Case D — explicit historical snapshot

Given an explicit bounded request to navigate a named historical commit/branch/file without claiming current-task authority, navigation must proceed and clearly mark the result as historical/bounded snapshot navigation.

## Verification level

`V0 + focused Skill behavior regression`.

Reason: the change is reusable Skill contract text and routing behavior, not product/runtime code. Verify exact diff/scope plus fresh-session behavior for the four cases above. Do not run unrelated business-project test suites.

## Branch/workspace

Use a dedicated branch such as:

`codex/domain-navigation-authority-gate-v1`

Before modification:

1. fetch canonical remote;
2. require local base to safely fast-forward/reconcile to live `origin/main` containing this task;
3. preserve unknown local work;
4. STOP rather than reset/stash/delete unknown work or improvise around baseline divergence.

## Acceptance criteria

PASS only if:

- the change is minimal and limited to the Domain Navigation authority-entry defect;
- Cases A and B stop current-task navigation without guessing;
- Case C continues normal fresh navigation without false STOP;
- Case D continues explicit historical/snapshot navigation without pretending it is current authority;
- Project Governance and Incident Doctor Skill trees are unchanged;
- no new runtime/infrastructure/diagnostic machinery is introduced;
- any package version bump is only `0.1.0 -> 0.1.1` and no tag/release is created;
- final task branch is clean and pushed at an exact remote-matching HEAD.

## STOP conditions

STOP without destructive correction if:

- local unique/unknown work prevents safe baseline reconciliation;
- the corrective appears to require broad Project Governance or Incident Doctor changes;
- the proposed gate causes blanket current-task STOPs where authority is already sufficiently verified;
- the historical/snapshot exception cannot remain clearly separated from current-task authority;
- validation requires mutating RemoteOrbit, FloatTabs, or another business project.

## Handoff

Stop at:

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Return:

```text
TASK_ID: EG-DOMAIN-NAV-AUTHORITY-GATE-035
REMOTE_CONTROL_HEAD:
LOCAL_BASELINE_AFTER_SYNC:
TASK_BRANCH:
FINAL_BRANCH_HEAD:
REMOTE_BRANCH_HEAD:
LOCAL_REMOTE_MATCH:
CHANGED_PATHS:
DN001_RULE_ADDED: YES/NO
CURRENT_TASK_AUTHORITY_GATE: PASS/STOP
REMOTEORBIT_REGRESSION: PASS/STOP
FLOATTABS_REGRESSION: PASS/STOP
FRESH_AUTHORITY_CASE: PASS/STOP
HISTORICAL_SNAPSHOT_CASE: PASS/STOP
PROJECT_GOVERNANCE_UNCHANGED: YES/NO
INCIDENT_DOCTOR_UNCHANGED: YES/NO
PLUGIN_VERSION:
RELEASE_CREATED: NO
DIFF_CHECK:
WORKING_TREE:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_AUDIT / STOP
```

Do not merge or publish Plugin v0.1.1 under this task.

## Executor handoff

- Remote control head and local baseline after sync: `0aee551e4ce2fbe843221f070dafaac490a33bb9`.
- Task branch: `codex/domain-navigation-authority-gate-v1`.
- Changed Domain Navigation contract files: `skills/domain-navigation/SKILL.md` and `skills/domain-navigation/references/mapping-workflow.md`.
- Focused contract review: RemoteOrbit and FloatTabs resolve to `STOP_CURRENT_TASK_NAVIGATION`; sufficiently verified fresh authority continues through normal routing; an explicitly named historical/bounded target proceeds with the `BOUNDED/HISTORICAL SNAPSHOT NAVIGATION` label.
- Review type: four-case contract-level scenario replay after rereading the changed Skill text. No business repository was modified, and no test harness was added.
- `project-governance` and `incident-doctor` content was not changed. `plugin.json` remains `0.1.0`; no release, tag, or merge was created.
- Next action: independent Web audit of the exact pushed branch head.
