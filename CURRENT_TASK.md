# CURRENT TASK — Project Governance Lifecycle, Identity & Workspace Integrity

Task ID: `EG-PROJECT-GOVERNANCE-LIFECYCLE-IDENTITY-WORKSPACE-037`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `REUSABLE_SKILL_ENHANCEMENT`

## Objective

Add three reusable Project Governance execution-integrity principles without creating new runtime/enforcement machinery or slowing ordinary business development:

1. task lifecycle must transition when reality changes so a completed/superseded task cannot remain active authority;
2. verification/acceptance evidence must stay bound to the exact source, artifact, build, runtime, or revision it actually proves unless equivalence/provenance is established;
3. state-changing work must identify the selected task workspace and its relationship to the authorized repository/ref/revision rather than trusting a project-looking directory by path alone.

These rules address repeated cross-project failure modes involving stale task controls after merges, evidence transferred across different HEAD/build/runtime identities, and old/symlink/worktree checkouts being mistaken for the active workspace.

## Authoritative baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted task 036 merge/main HEAD before this control transition: `11536eef2a76a18e8b197695d8936914133233dd`.
- Existing top-level Skills remain exactly: `project-governance`, `domain-navigation`, and `incident-doctor`.
- This task modifies only reusable `project-governance` guidance plus control handoff.

## Principle A — Task lifecycle integrity

The reusable contract must make the following semantics explicit:

- A task/control state is not indefinitely authoritative merely because its file still exists.
- Material lifecycle events such as merge, release, deployment, explicit human acceptance, abandonment, supersession, rollback, or a prerequisite invalidation must be reconciled into the active control state before further state-changing work that depends on the old phase.
- A task that has reached a terminal outcome must not continue to authorize implementation from an earlier phase such as `READY_FOR_MERGE`, `WAITING_FOR_ACCEPTANCE`, or `ACTIVE_IMPLEMENTATION`.
- Exact lifecycle state names are project-specific; do not impose a universal enum. What matters is that the current task contract accurately represents reality and does not silently remain in an obsolete phase.
- If the next action is a genuinely new objective/scope, open/reconcile the next task instead of stretching a completed task.
- Do not create churn for non-material status changes that do not affect authorization, prerequisites, acceptance, STOP conditions, side effects, or next action.

## Principle B — Exact identity and evidence binding

The reusable contract must distinguish identities such as, when relevant:

- source/commit HEAD;
- PR head;
- merge commit/tree;
- build/package artifact;
- installed application/package;
- running runtime/process;
- deployed revision;
- release artifact.

Required semantics:

- Evidence proves only the identity it actually observed or a different identity whose equivalence/provenance has been established.
- Do not silently transfer a CI/test result from PR HEAD X to merge commit Y, or runtime acceptance from installed build B to source HEAD A, merely because they are related by history or naming.
- Evidence may carry forward without rerunning when the relevant equivalence is actually proven, for example exact tree/content identity, immutable artifact hash identity, or an explicit provenance chain sufficient for the task decision. Do not require redundant reruns when equivalence is established.
- Automated verification, human acceptance, and runtime/incident observation are different evidence classes. Record what each proves; do not let one silently stand in for another when the task requires the missing class.
- Acceptance/closeout claims should name the exact revision/artifact/runtime being accepted when that identity matters to the decision.
- Do not turn every documentation-only or low-risk task into a build/runtime identity exercise; apply identity depth proportionally to the changed system and acceptance claim.

## Principle C — Selected task workspace identity

For source-controlled state-changing work:

- Identify the selected task workspace/check-out/worktree and establish its relationship to the authorized repository/ref/revision before mutation.
- A directory containing project files is not automatically the authoritative workspace.
- Branch name, folder name, symlink path, archived copy, old worktree, detached checkout, or local clone location does not by itself establish task authority.
- A non-main task worktree is valid when it is the intentionally selected authorized workspace; `main` is not automatically the only valid place to work.
- Preserve unknown staged/unstaged/untracked/local-only work in other or selected workspaces. Do not reset/stash/clean/delete merely to force alignment.
- Do not scan every disk path, worktree, clone, or remote by default. Expand workspace discovery only when ambiguity, lifecycle cleanup, unique work, or the task decision materially requires it.
- If workspace identity/relationship is materially unresolved for the requested mutation, stop and reconcile rather than proceeding from an inferred checkout.

## Evidence-class distinction

Where acceptance depends on behavior, keep the following concepts separate:

- automated verification: evidence about the checked source/tree/artifact and tested assertions;
- human acceptance: evidence about the user-visible behavior actually observed;
- runtime/incident evidence: evidence about the specific running execution observed.

A task may need one or more classes. The Skill must not require all three universally.

## Intended placement

Prefer the smallest coherent Project Governance update. Suitable locations include:

- `skills/project-governance/references/control-plane.md` for lifecycle reconciliation;
- `skills/project-governance/references/development-flow.md` for selected workspace and execution flow;
- `skills/project-governance/references/verification-tiers.md` for identity/evidence binding;
- `skills/project-governance/SKILL.md` only for minimal entry/reference wording if needed.

A new focused reference such as `references/execution-integrity.md` is allowed only if it materially reduces duplication and keeps the above contracts clearer than scattering them across existing references. Do not create a new file merely for symmetry.

Do not modify templates merely for consistency unless a concrete reusable semantic gap remains after the primary references are updated.

## Not authorized

Do not:

- modify `domain-navigation` or `incident-doctor` Skill content;
- create a fourth Skill;
- add runtime identity collectors, telemetry, daemons, databases, scanners, background monitors, automatic worktree cleanup, automatic remediation, or enforcement hooks;
- require scanning every worktree/clone/remote for ordinary tasks;
- require rebuilding/retesting merely because a commit SHA differs when relevant tree/artifact equivalence is already established;
- mutate any business repository;
- bump `plugin.json` version;
- create a Git tag, GitHub Release, release ZIP, or merge the task branch.

## Verification

Use `V0 + focused contract review`.

Required checks:

1. exact changed-path scope is minimal;
2. `git diff --check` PASS;
3. completed/superseded lifecycle states cannot silently remain active authority;
4. lifecycle reconciliation does not create meaningless control churn;
5. evidence is bound to exact source/artifact/runtime identity unless equivalence/provenance is established;
6. proven equivalence can avoid redundant reruns;
7. automated, human, and runtime evidence classes are distinguished without universally requiring all three;
8. selected task workspace identity is established before state-changing work when relevant;
9. non-main authorized worktrees remain valid;
10. no full-disk/full-worktree/full-remote scan is required by default;
11. unknown local work remains preserved;
12. `domain-navigation` and `incident-doctor` trees are unchanged;
13. `plugin.json` remains version `0.1.0`;
14. no business repository is modified.

## Focused scenarios

Review at least these cases:

### Case A — stale task after merge

A task says `READY_FOR_MERGE`, but the PR has already merged and main advanced.

Expected: reconcile/close/supersede the obsolete lifecycle phase before using it to authorize further state-changing work. Do not continue as if merge were still pending.

### Case B — superseded or abandoned task

A newer accepted task replaces an older task, or the old task is explicitly abandoned.

Expected: the old task no longer authorizes execution; preserve history without keeping it active.

### Case C — CI on PR head vs merge commit

CI passed exact PR HEAD X; merge commit Y now exists.

Expected: do not claim exact-head CI for Y unless relevant equivalence/provenance is established. If Y has the same accepted tree/content for the claim, evidence may carry without a redundant rerun.

### Case D — source vs installed/running build

Source HEAD A is current, but human/runtime acceptance observed installed build B.

Expected: acceptance applies to B and may apply to A only if build/provenance identity is established. Do not silently transfer the claim.

### Case E — stale/symlink/archived workspace

A directory contains the project but is an old branch/worktree, archived copy, symlinked checkout, or detached state whose relation to the authorized task is unresolved.

Expected: stop mutation until selected workspace identity and relation to the authorized repo/ref/revision are established.

### Case F — valid non-main task worktree

A dedicated task worktree is intentionally authorized while canonical main has unrelated preserved untracked output.

Expected: task worktree is valid; preserve unrelated work; do not force work onto main or clean other workspaces.

### Case G — ordinary unambiguous task

The selected workspace and task revision are already sufficiently established and no material ambiguity exists.

Expected: proceed without scanning every clone/worktree/remote or adding unnecessary verification burden.

## Branch/workspace

Use a dedicated branch such as:

`codex/project-governance-lifecycle-identity-workspace-v1`

Before modification:

1. fetch canonical remote;
2. require local base to safely reconcile/fast-forward to live `origin/main` containing this task;
3. preserve unknown staged/unstaged/untracked/local-only work;
4. STOP rather than reset/stash/delete/overwrite unknown work.

## Acceptance

PASS only if the three principles are reusable, proportional, and prevent stale control/evidence/workspace identity errors without creating a heavyweight universal preflight.

## Execution handoff — 2026-10-08

- Implemented only `skills/project-governance/SKILL.md` and its `control-plane.md`, `development-flow.md`, and `verification-tiers.md` references.
- V0: `git diff --check` passed; the three reference links resolve; `plugin.json` remains `0.1.0`; the Domain Navigation and Incident Doctor trees are unchanged; no business repository was modified.
- Focused contract review: Cases A–G pass. Material lifecycle changes invalidate stale phases while non-material status updates avoid churn; terminal tasks remain historical but inactive; evidence stays bound to observed identities with proven-equivalence reuse; automated, human, and runtime evidence remain distinct; unresolved workspace identity stops mutation; authorized non-main worktrees remain valid; discovery stays task-bounded; unknown work remains preserved.
- No product tests or runtime checks were run; this documentation-only change uses the task's V0 validation level.
- Handoff state: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`. No merge, tag, release, or ZIP publication is authorized.

Stop at:

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Return:

```text
TASK_ID: EG-PROJECT-GOVERNANCE-LIFECYCLE-IDENTITY-WORKSPACE-037
REMOTE_CONTROL_HEAD:
LOCAL_BASELINE_AFTER_SYNC:
TASK_BRANCH:
FINAL_BRANCH_HEAD:
REMOTE_BRANCH_HEAD:
LOCAL_REMOTE_MATCH:
CHANGED_PATHS:
LIFECYCLE_INTEGRITY_RULE: PASS/STOP
TERMINAL_TASK_NOT_ACTIVE_RULE: PASS/STOP
NO_MEANINGLESS_CONTROL_CHURN: PASS/STOP
EXACT_IDENTITY_BINDING_RULE: PASS/STOP
PROVEN_EQUIVALENCE_REUSE_RULE: PASS/STOP
EVIDENCE_CLASS_DISTINCTION: PASS/STOP
SELECTED_WORKSPACE_IDENTITY_RULE: PASS/STOP
NON_MAIN_WORKTREE_ALLOWED: PASS/STOP
NO_GLOBAL_SCAN_DEFAULT: PASS/STOP
UNKNOWN_WORK_PRESERVED: YES/NO
PROJECT_GOVERNANCE_SCOPE_ONLY: PASS/STOP
DOMAIN_NAVIGATION_UNCHANGED: YES/NO
INCIDENT_DOCTOR_UNCHANGED: YES/NO
PLUGIN_VERSION: 0.1.0
BUSINESS_REPO_MUTATED: NO
DIFF_CHECK: PASS/STOP
WORKING_TREE:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_AUDIT / STOP
```

Do not merge or publish under this task.
