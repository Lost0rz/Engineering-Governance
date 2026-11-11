# Engineering-Governance Repository Rules

CONTROL_MODE: ISSUE_CONTROL
ISSUE_APPROVERS: Lost0rz
ISSUE_WEB_SPEC_AUTHORING: ENABLED

This repository's ISSUE_CONTROL cutover is bound to the **verified merge of migration PR #41**. Older accepted main revisions remain FILE_CONTROL. Bootstrap Issue #40 is migration provenance under the FILE_CONTROL Task 093 bridge, **not** perpetual post-cutover execution authorization. After acceptance/cutover, follow-on source mutations require a separately approved, selected Issue revision with an authenticated `SPEC_APPROVAL_V1` comment by the authorized GitHub approver.

## Purpose

This repository is the source for reusable Engineering Governance Skills, routing contracts, templates, and acceptance specifications. It is not a governance runtime, daemon, scheduler, database, installer service, or automatic remediation system.

## Repository authority

- `AGENTS.md` contains durable rules for maintaining this source repository.
- `CONTROL_MODE: ISSUE_CONTROL` takes effect only upon verified merge of the migration PR into `main`; before cutover accepted main remains FILE_CONTROL.
- In ISSUE_CONTROL, the selected approved GitHub Issue/spec revision is the only task authorization (Issue [#40](https://github.com/Lost0rz/Engineering-Governance/issues/40) documents the migration, not automatic future authority); Issue comments carry decision/receipt evidence, not new scope. A label/body assertion alone never proves approval.
- `CURRENT_TASK.md` and `CURRENT_STATUS.md` cease to be live controls after cutover and remain recoverable via Git history. PR/CI/merge truth belongs to the GitHub host.
- Reusable engineering workflow belongs in `skills/**`; do not duplicate Skill procedure here. Issue approval, execution, receipt and migration behavior belongs to `skills/project-governance/references/issue-*.md`.
- `documents/**` may preserve durable design rationale, but does not replace live controls.

## Capability model

Exactly nine top-level Skills are supported:

1. `project-governance`
2. `project-profile`
3. `solution-design`
4. `design`
5. `execution-orchestrator`
6. `agent-handoff`
7. `evidence-audit`
8. `domain-navigation`
9. `incident-doctor`

Global routing is policy, not another Skill. `design` owns bounded UI/UX and frontend visual-design capability while `solution-design` remains the owner for material engineering/architecture/state-ownership ambiguity. `project-profile` is derived context/navigation, not a replacement for `AGENTS.md`, Domain authority, the selected FILE_CONTROL Task/Status or ISSUE_CONTROL Issue, or durable planning.

## Environment boundary

Reusable source defines what environment capability must be resolved, not concrete machine/platform values. Runtime/model/tool/capacity facts remain owned by the current execution environment unless a project explicitly defines a portable configuration artifact.

## Source development rules

- Inspect actual repository/PR/source evidence before changing governance.
- Keep one canonical owner per semantic class; link instead of duplicating.
- Preserve unknown/unique work and existing project authorities.
- Keep changes proportional; no extra Skill/document/test ceremony without material value.
- Do not add runtime/daemon/database/model-router/automatic-enforcement behavior unless repository purpose explicitly changes.
- A routed capability must execute the bounded workflow it owns when materially triggered; merely reading a source/reference file is not sufficient evidence of capability use.
- Governed user-facing receipts must make the actual routing/Skill composition observable and must not claim Skills that were not actually used.
- No-op reconciliation means no write and no commit. Issue progress/receipts must not trigger status-only Git commits or PRs; migration is a single approved source transition.

## Release / acceptance boundary

Source construction, installed/runtime acceptance, merge and release are separate lifecycle steps. Do not claim CI, installed behavior or release readiness without evidence for the exact relevant identity.
