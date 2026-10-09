# CURRENT TASK — Workspace Lifecycle Corrective

Task ID: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-CORRECTIVE-040`

State: `READY_FOR_MERGE`

Mode: `BOUNDED_GOVERNANCE_CORRECTIVE`

## Objective

Correct four semantic edge cases in the accepted workspace/worktree lifecycle contract so routine task startup remains bounded, writer conflicts are scoped by overlapping authority rather than broad capability labels, retained write-capable predecessors cannot create parallel writers, and merge/release events are terminal only when the project/task defines them as terminal or they otherwise change authorization.

## Affected domains

- Root repository governance rule: `AGENTS.md`
- Reusable Skill: `skills/project-governance/`

No new top-level Skill or runtime component is authorized.

## Start baseline

- Repository: `Lost0rz/Engineering-Governance`
- Canonical branch: `main`
- Verified start HEAD: `1e80848880b902ccf56ffcd70e22b19788b7b8d4`
- Authorized task branch: `codex/project-governance-workspace-lifecycle-corrective-v1`
- Prior lifecycle task 039: `CLOSED / MERGED_VERIFIED`
- Published Plugin v0.2.0 remains unchanged and does not include tasks 039/040.

## Workspace lifecycle

- Selected task workspace: remote branch `codex/project-governance-workspace-lifecycle-corrective-v1`.
- Prior 039 branch is terminal, fully merged, and retained only because current connector capability does not expose branch-ref deletion; it is not write-capable under a current task authorization and does not block this corrective.
- Retain current 040 branch until merge or another explicit terminal disposition.
- This is a remote-only task; no local worktree-cleanliness claim is authorized.

## Accepted corrective scope

1. Root and reusable rules now classify only task-relevant workspaces for routine decisions; unrelated historical workspaces expand into scope only for ambiguity, collision, unique-work risk, lifecycle cleanup, or explicit legacy reconciliation.
2. Writer conflict is defined at overlapping fact/state/policy/behavior authority. Domain/capability labels are routing hints and do not create automatic mutual exclusion.
3. A retained predecessor that can still resume writes under its current authorization remains a writer and blocks a successor for overlapping authority until a verified non-writing boundary exists, such as terminal state, supersession, explicit freeze/read-only disposition, or equivalent project rule.
4. Merge, release, deployment, acceptance, abandonment, supersession, rollback, and similar lifecycle events are not terminal by name alone; project/task controls determine whether the event ends the task/phase, advances authorization, or is non-terminal.

## Out of scope

- New Skill, CLI, daemon, database, hook, scanner, installer, automation, or enforcement runtime.
- Plugin version bump, package build, tag, release, or publication.
- Changes to `domain-navigation` or `incident-doctor` behavior.
- Any target-project worktree cleanup.
- Broader refactoring of the three-file control plane or verification tiers.

## Verification

`V0` whole-Skill audit — PASS on reviewed corrective HEAD `1e1affa284d7d3e3bfacfb44f19ee58d5f3778b9`, tree `b5e818ea93359ba98ef680d55d9e5796927b6fa7`.

Fresh evidence established:

- exact baseline `main` remained `1e80848880b902ccf56ffcd70e22b19788b7b8d4` during implementation audit;
- branch is ahead 10, behind 0 from that exact baseline;
- changed paths are limited to root `AGENTS.md`, root controls, `project-governance` entry/reference/template Markdown files;
- `plugin.json` remains version `0.2.0` and is unchanged;
- `verification-tiers.md`, `code-structure.md`, `domain-navigation/SKILL.md`, and `incident-doctor/SKILL.md` remain outside the diff;
- `code-structure.md` canonical authority remains fact/state/policy/behavior-class granular and the corrected lifecycle contract now uses compatible overlapping-authority semantics;
- `domain-navigation` still only routes evidence and does not authorize tasks; `incident-doctor` remains evidence-gated diagnosis and returns authorization changes to `project-governance`;
- project-governance reference paths exist on the exact branch, including `workspace-lifecycle.md`, `code-structure.md`, `control-plane.md`, `development-flow.md`, and `verification-tiers.md`;
- normal startup remains bounded; broad historical inventory remains isolated to explicit legacy reconciliation or task-relevant ambiguity/collision/unique-work/lifecycle needs;
- audit-found wording ambiguity in the writer invariant was corrected before merge review.

## Acceptance criteria

- Routine classification is task-relevant rather than repository-global. — PASS
- Writer exclusion uses overlapping authority rather than capability name alone. — PASS
- Retained write-capable predecessors still block overlapping successor writers. — PASS
- Lifecycle event names do not automatically imply terminal status. — PASS
- Multi-worktree coexistence for disjoint writers/readers remains permitted. — PASS
- Unknown/unique work preservation and remote/local evidence boundaries remain intact. — PASS
- Control-plane, code-structure, Domain Navigation, and Incident Doctor boundaries remain internally consistent. — PASS
- No new runtime/automation/top-level Skill or Plugin publication is present. — PASS
- V0 audit found no remaining material contradiction, duplicate authority, broken referenced path, or scope leak. — PASS

## Stop conditions

- `main` or the task branch changes incompatibly before merge.
- PR diff differs materially from this exact reviewed branch.
- Mergeability/status evidence reveals a blocker.
- A separate canonical lifecycle authority is discovered before merge.

## Handoff / current stop point

Ready to create a PR from exact reviewed HEAD `1e1affa284d7d3e3bfacfb44f19ee58d5f3778b9`. Before merge, independently inspect the PR diff, base/head identity, mergeability, and available status/workflow evidence. Merge only with expected-head protection. After merge, verify exact `main` tree/content equivalence and reconcile this task to a terminal closed state. Plugin publication remains separate.
