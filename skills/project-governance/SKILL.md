---
name: project-governance
description: Default entry for repository engineering: select task authority, do the smallest safe work, verify the affected behavior, and report actual delivery. Use agent-handoff only for real cross-context handoffs.
---

# Project Governance

**Goal:** help the agent complete real engineering work with minimum ceremony. Define the workflow, not a universal checklist. Read only what the current action requires.

## Working loop

1. **Understand:** identify the requested outcome, repository, task boundary and current evidence. For G0 status-only inquiries, inspect only relevant live facts; do not require an Issue, full preflight or formal audit.
2. **Route:** use the smallest capable Skill. Clear defects go straight to implementation; use design, domain navigation, incident diagnosis, orchestration or formal audit only for a real unresolved dependency.
3. **Execute:** reuse existing valid work, keep changes inside the objective and actual host permissions, and resolve ordinary defects and interface adjustments autonomously.
4. **Verify:** choose focused tests from the changed semantics and dependencies, not from file count, commit count or a default full suite. Reuse still-valid evidence.
5. **Deliver:** report what changed, decisive evidence and remaining decisions. Never claim unrun tests, unmerged PRs or automated UI inspection as human acceptance.

A normal continuation does not create another Issue, branch, worktree, approval, Handoff Card or review cycle. Do not run a prescribed list of all Skills.

## Authority: check once, escalate only real changes

For **state-changing work and authority decisions**, select the globally installed `CONTROL_POLICY_V1` and the independently verified repository enrollment. Project `AGENTS.md` provides *project-specific* business/runtime constraints; it cannot override global task-control mode, grant writes or set universal approval flags.

- **G0:** read-only status, inspection or advisory analysis needs no write authorization.
- **Current top-level user request (G1/bounded G2):** when the host actually authenticates the live USER request, selected repository, intended scope/effects and the real write tool permits the operation, the request is first task authorization. No initial 19-field Issue, digest or GitHub approval comment. Keep in-envelope fixes in the same task. The host, not an assistant claim or a helper's caller-provided booleans, verifies permission.
- **Issue-backed / legacy:** when the selected task depends on an approved Issue, verify that Issue's actual current revision, approval and task scope. The older 19-field contract is for this path, not for every request. FILE_CONTROL applies only to independently verified unenrolled repositories.
- **G3 or changed authority:** explicit human decision is required for new privilege/identity/credential scope, material security boundary, destructive or irreversible production/data actions. A host merge, deployment or release gate remains separate from task authorization.

`source_write_gate()` is intentionally **not a permission oracle**: it has no trusted USER-role or host writer channel and always declines to mint a write grant. Do not treat its advisory stop as a second approval requirement for a host-authorized direct task. Never replace actual host checks with a self-attestation. Unattended or transferred grants require independent durable trust; the shipped risk-scoped automation remains disabled.

L0/L1 corrections continue inside scope. For L2 uncertainty, **resolve within the current envelope first**; escalate only a genuine new decision, risk, owner or effect. Pause only the affected unsafe mutation. A real overlapping writer or unique uncommitted work is a conflict; an old branch or hypothetical writer is not. Preserve unknown local work.

## Workspace, quality and delivery

Reuse a safe checkout and task branch/PR when possible. Create a distinct durable worktree only for justified independent work or actual isolation needs; never create worktrees for read-only inspection or routine handoff. Consult workspace rules only if selection, collision or cleanup is material.

G0–G3 describe consequences/authority; V0–V3 describe *verification evidence*, not permissions. Documentation/Skill prose normally needs static or affected-contract checks; changed executable authorization/CI trust, unknown executable owners, or high-consequence effects can require broader tests. **Packaging and publishing are separate explicit operations, not automatic V3 side effects.** The accepted-base CI selector decides checks; PR text cannot waive them. Applicable human product-UI acceptance remains human-owned, while deterministic browser tests are valid machine evidence.

Use the receiving environment's actual tool/model/workspace capabilities. Sub Agents, separate independent reviews and long receipts are optional unless the task/risk truly needs them. Repo delivery requires observed remote commit/PR state; a local commit is not proof of push.

For material outcomes, return a concise status: change, evidence or blocker, next safe action. Do not emit a compulsory multi-field receipt for routine work. A genuine cross-context transfer uses `agent-handoff`; it carries current authority *references + delta*, not duplicated history or authorization.

## References — optional pointers, not a startup reading list

Read only the owner selected by an actual question:
- `references/global-routing.md` — Skill selection.
- `references/issue-control.md` — Issue approval, legacy execution or authorization ambiguity.
- `references/issue-execution-contract.md` — legacy Issue Work Packages, deviations and receipts.
- `references/verification-tiers.md` — affected tests, evidence and cadence.
- `references/workspace-lifecycle.md` — real workspace, writer or cleanup decisions.
- `references/code-structure.md` — ownership and architectural writer changes.
- `references/remote-delivery.md` — push/PR/merge/release boundaries.
- `references/control-plane.md` — material task/terminal control transitions.
- `references/artifact-lifecycle.md` — authority/projection refresh on meaningful changes.
- `references/control-identity.md` — disputed revision or provenance evidence.
- `references/development-flow.md` — full lifecycle only when needed.
- `references/issue-control-migration.md` — migration only.
- `references/planning-documents.md` — durable design decisions only.
- `references/adoption.md` — environment installation/routing only.
