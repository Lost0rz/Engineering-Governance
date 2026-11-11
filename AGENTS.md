# Engineering-Governance Repository Rules

CONTROL_MODE: ISSUE_CONTROL
ISSUE_APPROVERS: Lost0rz

## Repository purpose

Engineering-Governance is the source repository for portable Engineering Governance Skills, global routing policy, templates, acceptance specifications, and reference material. It is **not** a governance runtime, daemon, scheduler, database, installer service, central control plane, or automatic remediation platform.

## Repository-specific authority boundaries

- `AGENTS.md` contains this repository's durable, project-specific normative boundaries and explicit control/permission settings; it must not duplicate reusable Skill procedures.
- `skills/**` owns reusable Engineering Governance implementation, routing contracts, procedures, templates, and their tests. Global Skill routing is policy, not an additional Skill.
- `documents/**` owns durable capability architecture and design rationale; `references/**` owns shared engineering/reference and acceptance material. Neither is current task authorization.
- The GitHub host owns live refs, PR/CI/merge/release facts; historical control files are not current task authorization under the selected `ISSUE_CONTROL` mode.
- A target project's product/domain/data/runtime truths and repository-specific commands remain owned by that target project, not copied into shared Skills.

## Repository-specific safety and change constraints

- Do not introduce a runtime service, daemon, database, model router, installer/control plane, or automatic enforcement/remediation mechanism without an explicit change to this repository's purpose.
- Keep Skills portable across supported execution environments; do not make a specific local machine, model, account, runner, or session configuration a reusable policy requirement.
- Do not silently enable permission or approval opt-ins, weaken source/host trust boundaries, or migrate another repository merely by changing this source repository or its templates.
- Preserve historical acceptance evidence as history; do not reclassify it as proof of current installed/runtime/host state.

## Governance pointers (not duplicate workflow rules)

- Skill selection: `skills/project-governance/references/global-routing.md`.
- Task authorization and issue-writing opt-ins: `skills/project-governance/references/issue-control.md`.
- Risk/deviation bounds: `skills/project-governance/references/issue-execution-contract.md`.
- Verification and lifecycle: `skills/project-governance/references/verification-tiers.md` and `skills/project-governance/references/artifact-lifecycle.md`.
- Maintainer guidance: `references/SKILL_ENGINEERING.md`.
