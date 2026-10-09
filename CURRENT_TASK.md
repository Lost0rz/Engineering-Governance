# CURRENT TASK — Workspace Lifecycle Corrective

Task ID: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-CORRECTIVE-040`

State: `ACTIVE`

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
- Prior 039 branch is terminal, fully merged, and retained only because current connector capability does not expose branch-ref deletion; it is not an active writer and does not block this corrective.
- Retain current 040 branch until merge or another explicit terminal disposition.
- This is a remote-only task; no local worktree-cleanliness claim is authorized.

## In scope

1. Narrow root durable wording from all non-canonical workspaces to task-relevant non-canonical workspaces, with unrelated historical workspaces requiring expansion only when they create ambiguity, collision, unique-work risk, lifecycle cleanup, or are explicitly under legacy reconciliation.
2. Replace broad same-capability writer gating with overlapping write-authority/state/behavior-class semantics, consistent with `code-structure.md` canonical-authority granularity.
3. Make retained predecessors that remain write-capable count as writers; a successor writer for the overlapping authority is blocked until the predecessor is terminal, superseded, explicitly frozen/read-only, or otherwise cannot resume writes without new authorization.
4. Clarify that merge, release, acceptance, abandonment, supersession, rollback, or similar events end a task/phase only when project/task controls define them as terminal or when the event materially changes authorization; merge alone does not universally imply terminal closeout.
5. Update only the minimal Skill/reference/template/root-control surfaces needed for internal consistency.

## Out of scope

- New Skill, CLI, daemon, database, hook, scanner, installer, automation, or enforcement runtime.
- Plugin version bump, package build, tag, release, or publication.
- Changes to `domain-navigation` or `incident-doctor` behavior.
- Any target-project worktree cleanup.
- Broader refactoring of the three-file control plane or verification tiers unless required to resolve an actual contradiction found during audit.

## Known evidence

- Full audit after task 039 found the root `AGENTS.md` wording broader than the canonical lifecycle reference (`every non-canonical` versus `task-relevant`).
- `code-structure.md` defines canonical ownership at fact/state/policy/behavior-class granularity, so capability alone is too coarse as a mandatory writer lock.
- A retained non-terminal workspace can be fully classified yet still be able to resume writes after review/QA feedback; classification alone therefore does not eliminate a parallel-writer risk.
- `control-plane.md` already distinguishes material lifecycle events from the project-defined terminal outcome, while `workspace-lifecycle.md` currently phrases several events too categorically.

## Risk and rationale

This is documentation/Skill semantics only, but an imprecise rule can materially slow development or recreate parallel-writer ambiguity across every governed project. Keep the corrective narrow and align all summaries to one canonical detailed lifecycle authority rather than adding another policy layer.

## Verification level and rationale

`V0` — documentation/control semantics only.

Required checks:

- exact base/head and final diff scope;
- whole `project-governance` consistency across `SKILL.md`, all references, templates, and root `AGENTS.md`;
- consistency with `code-structure.md` authority granularity and `control-plane.md` lifecycle semantics;
- boundary review against `domain-navigation` and `incident-doctor` to ensure no trigger/authority leakage;
- confirmation normal startup remains bounded and legacy reconciliation remains the only broad historical inventory path;
- confirmation no plugin-release/runtime/automation surface changes;
- post-merge exact-main/tree/content verification.

## Acceptance criteria

- Root and Skill wording consistently limits routine classification to task-relevant workspaces.
- Writer exclusion is based on overlapping write authority/state/behavior class, not capability name alone.
- A retained predecessor that can still resume writes blocks a successor writer for the overlapping authority until it is frozen/read-only, superseded, terminal, or otherwise cannot write without new authorization.
- Merge/release/etc. are not universally treated as terminal; project/task lifecycle authority determines whether the event ends authorization or moves phases.
- Multi-worktree coexistence for disjoint writers/readers remains permitted.
- Unknown/unique work preservation and remote/local evidence boundaries remain intact.
- No new top-level capability, runtime, automation, or Plugin publication is added.
- Final whole-Skill audit finds no material contradiction, duplicate authority, over-constraint, broken link, or scope leak.

## Stop conditions

- `main` or authorized branch moves incompatibly with the reviewed baseline.
- A separate canonical lifecycle authority is discovered that changes the correction design.
- The correction requires new runtime/enforcement behavior or Plugin publication.
- Any ambiguity would require destructive or unsupported cleanup action.

## Handoff / current stop point

Authorized to implement the four bounded semantic corrections on `codex/project-governance-workspace-lifecycle-corrective-v1`, perform a whole-Skill V0 audit, create and merge a PR only if the exact reviewed branch remains aligned, then close task 040 after post-merge verification.
