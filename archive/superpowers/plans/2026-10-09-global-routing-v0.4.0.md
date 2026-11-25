# Global Routing v0.4.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a v0.4.0 source candidate that adds a reusable global Skill-routing/adoption contract and incorporates pilot-proven control-identity, workspace-identity, and verification-cadence corrections without adding runtime infrastructure or a fourth Skill.

**Architecture:** Keep the existing three-Skill capability model. Put route selection and agent-mediated global-`AGENTS.md` adoption under Project Governance references/assets so it ships inside `skills/**`; keep detailed procedures in their owning Skills. Treat control identity and verification cadence as reusable Project Governance contracts rather than duplicating them into the managed global route block.

**Tech Stack:** Markdown Agent Skills, Agent Plugin metadata JSON, Git/GitHub source control.

**Spec:** `docs/superpowers/specs/2026-10-09-global-routing-v0.4.0-design.md`

## Global Constraints

- Keep exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`.
- No Router Skill, installer executable, daemon, hook, MCP server, background service, or automatic remediation.
- Global routing selects Skills only; it does not duplicate their detailed workflows.
- Project `AGENTS.md` remains repository-specific and does not copy the global routing block by default.
- Keep `V0`–`V3` as the single risk dimension; cadence is separate.
- `control_parent` is not an equality gate unless the task explicitly declares a locked/current/execution-head requirement.
- The Plugin package boundary remains `plugin.json` + `skills/**`.

## Review Focus

- Existing global `AGENTS.md` with unrelated rules must remain semantically intact during adoption.
- Multiple/conflicting managed route blocks must stop/reconcile rather than produce a third copy.
- Explicit locked-head semantics must not be weakened while fixing the historical-parent false positive.
- Routing must not cause Doctor to become the default path for ordinary bugs with sufficient evidence.
- Cadence guidance must not accidentally require full regression/CI for each small construction edit.

---

### Task 1: Add routing and adoption contracts

**Files:**
- Create: `skills/project-governance/references/global-routing.md`
- Create: `skills/project-governance/references/adoption.md`
- Create: `skills/project-governance/assets/templates/GLOBAL_AGENTS_ROUTING.md`
- Modify: `skills/project-governance/SKILL.md`

**Interfaces:**
- Consumes: existing three Skill names and boundaries.
- Produces: one default route, conditional route rules, managed-block markers, and idempotent agent-mediated adoption semantics.

- [ ] Add scenario-first routing contract with Project Governance default, Domain Navigation conditional, Incident Doctor reactive, and explicit return paths.
- [ ] Add adoption contract covering zero/one-current/one-old/multiple-conflicting managed-block states and preservation of unrelated global rules.
- [ ] Add concise managed block template with stable BEGIN/END markers and no duplicated workflow detail.
- [ ] Link all three from `project-governance/SKILL.md` and state that Project Governance is the normal Engineering Governance entry when global routing is adopted.
- [ ] Verify all links and exact managed markers by re-reading the branch files.

### Task 2: Correct control/workspace identity semantics

**Files:**
- Create: `skills/project-governance/references/control-identity.md`
- Modify: `skills/project-governance/references/control-plane.md`
- Modify: `skills/project-governance/references/development-flow.md`
- Modify: `skills/project-governance/references/workspace-lifecycle.md`

**Interfaces:**
- Consumes: task/control freshness and workspace lifecycle rules.
- Produces: typed identity semantics distinguishing provenance, current/locked heads, local/remote branch state, worktree registration/path state, write capability, and authority overlap.

- [ ] Define control-parent/transition/current/locked/freshness identities and the equality-vs-relationship decision rule.
- [ ] Add the verified historical-parent regression scenario and preserve explicit locked-head STOP behavior.
- [ ] Make workspace evidence dimensions explicit and prohibit inference between local branch, remote branch, worktree registration, filesystem path, HEAD, dirtiness, and write capability.
- [ ] Keep discovery bounded to task-relevant/overlapping writer scope.
- [ ] Re-read the modified references for contradictions with lifecycle and control ownership.

### Task 3: Add verification cadence without a second risk taxonomy

**Files:**
- Modify: `skills/project-governance/references/verification-tiers.md`
- Modify: `skills/project-governance/references/development-flow.md`
- Modify: `skills/project-governance/assets/templates/AGENTS.md`

**Interfaces:**
- Consumes: `V0`–`V3` risk/scope tiers.
- Produces: construction/corrective-close/task-close/merge-release cadence and the rule that effort follows risk, not edit count.

- [ ] Add cadence as an orthogonal dimension, preserving `V0`–`V3` meanings.
- [ ] Specify focused construction checks and broader closure checks only when justified.
- [ ] Add bounded-corrective guidance for multiple related human-acceptance findings.
- [ ] Add a short project-template placeholder for repository-specific validation cadence without copying the whole reusable policy.
- [ ] Verify no L1–L4 or competing risk taxonomy is introduced.

### Task 4: Align repository and package source

**Files:**
- Modify: `AGENTS.md`
- Modify: `README.md`
- Modify: `plugin.json`
- Modify: `CURRENT_STATUS.md`
- Modify: `CURRENT_TASK.md`

**Interfaces:**
- Consumes: completed reusable contracts from Tasks 1–3.
- Produces: coherent v0.4.0 source metadata and repository rules that permit agent-mediated adoption while still forbidding installer/runtime infrastructure.

- [ ] Update root repository rules to distinguish forbidden installer/runtime platforms from authorized agent-mediated adoption contracts.
- [ ] Update README to explain the global routing layer and adoption path.
- [ ] Bump package candidate version `0.3.0 -> 0.4.0` without claiming publication.
- [ ] Record implemented paths and verification state in controls; keep task open until exact-head audit is complete.
- [ ] Verify the package-visible routing/adoption files all live under `skills/**`.

### Task 5: Exact-head semantic audit and PR

**Files:**
- Read/audit all branch changes; corrective edits only if a material issue is found.

**Interfaces:**
- Consumes: exact final branch diff against start main.
- Produces: reviewable PR plus an audit verdict tied to exact head.

- [ ] Compare `b7e47e2de346fa229818013d4369ae60cee6e0fa...HEAD` and enumerate every changed path.
- [ ] Verify exactly three top-level Skill directories remain.
- [ ] Re-run all 12 acceptance scenarios against the exact branch content.
- [ ] Search for conflicting installer prohibitions, Router-Skill references, duplicate risk taxonomies, duplicate managed markers, and broken relative links.
- [ ] Perform a separate author self-review because no subagent review tool is available in this remote-only harness; classify findings Critical/Important/Minor.
- [ ] Fix any Critical/Important finding, then re-run the exact-head audit.
- [ ] Create a PR against `main` and leave it unmerged for the user's integration decision.
