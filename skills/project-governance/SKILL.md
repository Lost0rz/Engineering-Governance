---
name: project-governance
description: Normal entry for governed software/repository tasks, including plain-language requests for construction or audit cards (给我施工卡/审计卡), approved GitHub Issue handoffs to Codex Desktop, task/control authorization, execution preflight, PR lifecycle, verification and receipts. Route actual cross-context cards through agent-handoff.
---

# Project Governance

Use this Skill as the normal engineering entry. It owns task/control authority, lifecycle, writer/workspace boundaries, proportional verification, repository delivery, and closeout. Keep clear work lightweight.
## Entry and capability boundaries

Route by the requested outcome, not by keywords. `references/global-routing.md` owns Skill selection; `agent-handoff` handles actual cross-context Cards, not ordinary continuation. **G0 status-only inquiries** (e.g. PR state and existing CI) use the smallest fresh read-only host evidence needed; they do not trigger full Issue/AGENTS preflight, formal Evidence Audit, V3 review or unrelated reference loading unless the question or project authority actually requires it.

For G0 read-only inspection, no Issue approval is required. For state-changing work, select the accepted **global CONTROL_POLICY_V1** mode and independently verified repository enrollment, then read the project `AGENTS.md` only for project-specific constraints and the selected FILE_CONTROL Task or ISSUE_CONTROL Issue. `references/issue-control.md` owns Web authoring, strict/delegated approval, the optional trusted G1/G2 grant and local receiver preflight. The unverified autonomy path is inactive; a Card is never authorization. Do not request repeated approval for a genuinely unchanged, already-authorized action.

Governance does not adopt external engineering frameworks as required Skills or runtime/model routers. `references/capability-composition.md` owns that boundary; the receiving environment owns its actual runtime tools.


## Task workspace creation boundary

Before creating any branch, Git worktree/checkout, or PR, apply the **reuse-first creation gate** in `references/workspace-lifecycle.md`. A command, same-task continuation, correction, control-only transition, new session, or delegated Sub Agent is not a reason to allocate a new physical worktree or PR. Branch, worktree, and PR are separate choices; preserve target-project requirements (including explicit fresh branch/Draft PR) and the unique-work/overlapping-writer safety gate. Read-only tasks normally need no new worktree/PR. Do not infer machine-local worktree state from GitHub evidence.

## Task-control mode selection

For **state-changing work and authority decisions**, use the installed versioned global CONTROL_POLICY_V1 and verified GitHub enrollment to select `FILE_CONTROL` (historical Task/Status) or `ISSUE_CONTROL` (approved Issue/revision). The project `AGENTS.md` cannot select or override the mode. Apply `issue-control.md` and `issue-execution-contract.md` only to the selected decision; `issue-control-migration.md` applies only to migration. Do not activate risk-scoped autonomy without actual accepted opt-in and independently verified host/credential trust. G0–G3 risks and V0–V3 verification remain separate. Unknown or stale authorization **never grants writes**; GitHub authorization failure stops the affected mutation. For a simple G0 status lookup, do not perform this write-authorization preflight.

## Control alignment versus standalone PR creation

Apply `references/control-plane.md` only for a relevant task-control or terminal transition, to distinguish FILE_CONTROL Task/Status alignment from ISSUE_CONTROL Issue evidence and PR state. It is not a universal per-edit final alignment gate. In FILE_CONTROL only, a verified merge can leave bounded `POST_MERGE_DRIFT`; report it without automatically opening a control-only PR, and use the next normally authorized development PR for the first control-only reconciliation/authorization commit when safe. Do not reuse a terminal/stale Task to write code or bypass PR rules. In ISSUE_CONTROL, read live host merge evidence and update only meaningful Issue receipt/state evidence; no Task/Status commit, no standalone PR just to mirror a merge. Missing or conflicting approved Issue authorization produces STOP before further mutation. Worktree creation remains governed by the size/isolation-based reuse-first gate, not by control file updates.

## Governed development

1. Select the current authority once. Continue the same task directly when purpose and permission remain valid; context transfer, test rerun or correction alone does not create a task.
2. Check only relevant repository, writer, workspace, dependency and host facts. Preserve unique work; use `references/workspace-lifecycle.md` for actual conflicts.
3. Stay within the authorized task/risk/effect envelope. `references/issue-execution-contract.md` owns G0–G3 and L0–L3; L2 first resolves affected uncertainty in-envelope and requests an external decision only when necessary.
4. Use narrower Skills only for material dependencies; Sub Agents and extra worktrees are never default workflow steps.
5. Implement the smallest safe change and verify proportionally under `references/verification-tiers.md`. Human UI acceptance remains a distinct human decision.
   For material verification plans, use the machine-readable `VERIFICATION_PLAN_V1` contract in `references/verification-tiers.md`; its `scripts/verification-plan.py` adapter is source policy consumed only from a trusted base by the target repository's own CI. Never treat an untrusted PR's own plan as permission to skip required tests.
6. For repository delivery, use `references/remote-delivery.md`; local commits alone do not prove remote push. At merge/release, check actual host gates.
7. Reconcile only the semantic owners changed by a material task/terminal event under `references/artifact-lifecycle.md`; no status-only commit on a no-op.


## Cross-repository coordination

A multi-repository objective may record only decision-relevant coordination facts: primary task authority, participating repositories, per-repo write authority, shared contract authority, integration order, acceptance owner. A task never automatically grants writes in another governed repository.

## Mutually exclusive task authority

- `AGENTS.md` is always durable project-specific policy; global CONTROL_POLICY_V1 and verified host enrollment select the mode.
- FILE_CONTROL: `CURRENT_STATUS.md` is the concise snapshot; `CURRENT_TASK.md` alone authorizes work.
- ISSUE_CONTROL: an approved, uniquely selected GitHub Issue/spec revision alone authorizes work; Issue comments hold bounded decision/receipt evidence. Retired Task/Status files are historical only.

Project Profile, durable planning, Domain maps, handoffs, audits and CI/test/PR/runtime observations never become a second task authority.

## Compact Engineering Status Receipt

For a material engineering action, return a short, truthful outcome: what changed, the decisive evidence or blocker, and the next safe action. Mention the actual Governance route/Skills when materially used, but **do not emit a compulsory multi-field receipt or checklist for routine status, advice, G0 inspection or an ordinary same-task continuation**. A real cross-context Card, mandated project record, G3 decision or release gate keeps its own required provenance.

Report actual PR/commit/CI identity when claiming delivery, and do not label an unrun test, absent permission, machine-driven UI inspection or unmerged Draft as PASS. Subagent model/reasoning details are relevant only when actual delegation materially affected the task. No documentation-only or no-op activity requires a status-only commit or Issue comment.
## Supporting contracts

These are **optional pointers, not a startup reading list**. Open a reference only after a concrete question or safety gate selects its owner:

- `references/control-plane.md` — mode-aware authority and alignment;
- `references/issue-control.md` — approved Issue authority and provenance;
- `references/issue-execution-contract.md` — deterministic plan, deviations and receipts;
- `references/issue-control-migration.md` — safe migration/cutover;
- `references/artifact-lifecycle.md` — authority/projection refresh lifecycle;
- `references/control-identity.md` — HEAD/provenance/control-only drift;
- `references/development-flow.md` — full governed flow;
- `references/remote-delivery.md` — local commit vs remote repository delivery gate;
- `references/code-structure.md` — canonical writer/authority;
- `references/workspace-lifecycle.md` — workspace/branch closeout;
- `references/verification-tiers.md` — proportional verification;
- `references/planning-documents.md` — durable design/work-package linkage;
- `references/adoption.md` — environment-aware routing adoption.
