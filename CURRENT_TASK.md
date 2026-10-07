# CURRENT TASK — Project Governance Audit Corrective

Task ID: `EG-PROJECT-GOVERNANCE-AUDIT-CORRECTIVE-023`

State: `AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

Mode: `BOUNDED_DOCUMENTATION_CORRECTIVE`

## Objective

Correct only the Project Governance issues established by `EG-FULL-SKILL-AUDIT-022`, without expanding the three-Skill architecture or adding new governance infrastructure.

## Authority and baseline

- Audit control head before this authorization: `67062a389ea6b26c86e91435612169f60240346a`.
- Frozen reusable comparison baseline: `4bc63eadbf1e1166ef8d9106c7f387a8ebb42c18`.
- Planned branch: `codex/project-governance-audit-corrective`.

## Authorized reusable files

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/assets/templates/AGENTS.md`
- `skills/project-governance/assets/templates/CURRENT_TASK.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change only for handoff/closeout.

## Required corrective A — optional semantic-navigation integration

Remove assumptions that every target repository already has or must create a separate Domain Map. Project Governance should route through existing accepted business/product/domain/capability authorities and/or an optional derived navigation projection. When Domain/authority/code location is unclear, call Domain Navigation.

Do not duplicate the Domain Navigation contract or create a new map requirement.

## Required corrective B — non-destructive execution baseline

For source-controlled projects, make the normal workflow state clearly that an executor verifies the task-relevant repository/ref/revision and current workspace state before state-changing work; unknown staged/unstaged/untracked work or local-only commits must not be reset, stashed, deleted, overwritten, or force-cleaned merely to match an execution card. If authoritative baseline/control drift materially affects the task, stop and reconcile rather than improvising.

Keep this conditional and lightweight; do not prescribe Git/worktrees to projects that do not use them.

## Out of scope

- changes to `domain-navigation` or `incident-doctor`;
- new files or new Skill;
- scripts/runtime/dependencies;
- target-project adoption;
- broad branch-management framework;
- changing verification tiers or the three-file ownership model.

## Verification

`V0` only:

- changed reusable paths exactly the four files above;
- frontmatter and relative links remain valid;
- no new mandatory Domain Map wording remains in those files;
- non-destructive workspace/baseline rule is conditional on the target's source-control workflow and does not create a new tool dependency;
- sibling Skills unchanged;
- `git diff --check` equivalent content hygiene;
- final branch ready for independent re-audit before merge.

## Current stop point

`AUTHORIZED_FOR_BOUNDED_CORRECTIVE`
