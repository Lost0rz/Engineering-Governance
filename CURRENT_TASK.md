# CURRENT TASK — EG-095 (transitional FILE_CONTROL bridge)

Date: 2026-11-06
Repository: Lost0rz/Engineering-Governance
TASK_ID: EG-WEB-DELEGATED-ISSUE-AUTHORIZATION-095
MODE: SOURCE_ONLY / BOUNDED CORRECTIVE
AUTHORIZATION: explicit user request 2026-11-06 to optimize remote ChatGPT Web authorization to GitHub Issue approval; governance Issue #44 records scope and receipts.
CONTROL_BASIS: accepted main remains FILE_CONTROL until PR #41 is merged. This bridge exists only on the stacked feature branch; do not ship it in the final candidate tree.
BRANCH: codex/web-delegated-issue-approval-095
BASE: PR #43 branch codex/web-local-handoff-routing-094 at e0b0b7f1335786e90404b6f245e15c3baef6b33d
DEPENDENCIES: PR #41 (Issue Control) and PR #43 (Web-to-Codex handoff) both Draft/unmerged.

## Objective
Enable explicitly opted-in personal-project AI-proxy Issue approval after a **fresh, exact-spec user approval in Web chat**, with a dedicated lower-assurance delegated comment; stop redundant manual Issue comments, but never impersonate direct human GitHub approvals. Preserve strict default and source/host acceptance boundaries.

## Authorized changes
- skills/project-governance/references/issue-control.md
- skills/project-governance/references/issue-execution-contract.md
- skills/project-governance/scripts/issue-spec-check.py
- skills/project-governance/scripts/test_issue_spec_check.py
- skills/project-governance/SKILL.md (bounded pointer)
- skills/agent-handoff/references/handoff-contract.md (sender/receiver contract)
- references/V095_DELEGATED_ISSUE_APPROVAL_ACCEPTANCE.md (focused matrix)
- temporary CURRENT_TASK.md / CURRENT_STATUS.md bridge, removed from final PR tree.

## STOP
No merge, no main commit, no live plugin installation/release/version bump, no target repository AGENTS opt-in, no forged human proof, no automated approval absent an exact user decision, no new framework, runner, secret or broad CI. Do not broaden permission to PR merge or human UI acceptance. Keep final PR Draft with source test evidence and limitations.
