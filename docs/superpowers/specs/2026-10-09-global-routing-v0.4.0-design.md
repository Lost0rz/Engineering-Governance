# Engineering Governance Global Routing v0.4.0 Design

## Intent

Plugin v0.3.0 proved the three reusable capabilities but left the selection problem outside the reusable payload: each Skill knows when it applies only after an agent has already chosen to read it. v0.4.0 adds a small global routing/adoption contract that can be installed into a user's global `AGENTS.md` and folds pilot-proven corrections back into Project Governance.

The design keeps the existing three-Skill architecture. Routing is policy, not a fourth capability.

## Authority split

### Global `AGENTS.md`

Owns only stable cross-project routing rules. Its Engineering Governance managed block decides which Skill to load and when to hand off between Skills. It does not copy task workflow, repository facts, workspace procedures, verification details, or incident procedures.

### Project `AGENTS.md`

Owns durable repository-specific rules and pointers. It does not duplicate the global Engineering Governance routing block by default.

### Skills

Own reusable procedure detail:

- `project-governance`: normal governed engineering entry, task/control/workspace/verification lifecycle;
- `domain-navigation`: conditional semantic and source routing when Domain/capability/authority/code/test location is unclear;
- `incident-doctor`: reactive evidence-gated diagnosis for a real blocking problem with insufficient evidence.

## Routing model

Default engineering route:

`engineering/project request -> project-governance`

Conditional routes:

- If the responsible Domain/capability, semantic authority, code location, symbol, runtime entry, or relevant test cannot be established safely, `project-governance -> domain-navigation -> project-governance`.
- If a real failure/unexplained behavior/unsafe ambiguity blocks safe progress and current evidence is insufficient, `project-governance -> incident-doctor`.
- Incident Doctor may call Domain Navigation only to locate/verify candidate evidence. Diagnosis stays owned by Incident Doctor.
- If diagnosis supports a behavior change that the active task does not authorize, return to Project Governance for reconciliation before mutation.
- Simple non-project/non-engineering requests do not force an Engineering Governance route.

The router selects a Skill; it does not execute that Skill's full workflow itself.

## Managed global block

The reusable payload ships a concise block bounded by stable markers:

`<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->`

`<!-- END ENGINEERING-GOVERNANCE ROUTING -->`

Adoption behavior:

- no block -> insert exactly one managed block at an appropriate durable location;
- exactly one older/compatible block -> replace that block in place;
- exactly one current block -> leave it unchanged;
- multiple/conflicting managed blocks -> stop and reconcile; do not append another block;
- preserve all unrelated global rules byte-for-byte where practical and semantically intact in every case.

The managed block contains only route/dispatch semantics and a pointer to the installed Skills. It does not contain the full Project Governance, Domain Navigation, or Incident Doctor procedures.

## Adoption boundary

Adoption is agent-mediated. The Plugin does not ship or require a Bootstrap CLI, daemon, hook, MCP server, background service, or automatic file-mutating runtime. An authorized AI agent inspects the existing global `AGENTS.md`, applies the managed-block contract, and verifies the result.

The routing template and adoption contract must live under `skills/**` so the existing package rule (`plugin.json` + `skills/**`) ships them.

## Control identity correction

Project Governance must distinguish these identities instead of treating every recorded SHA as the same kind of gate:

- `control_parent` / transition parent: provenance anchor for the commit or transition that established a control state;
- `control_transition_head`: the revision produced by that transition when relevant;
- `current_control_head`: the currently verified revision whose controls are being relied on;
- `locked_head` / `expected_current_head` / `exact_execution_head`: an explicit equality requirement when the task actually declares one;
- remote freshness evidence: live or accepted remote state used to decide whether the current control is stale.

A historical parent mismatch alone is not control drift. If the declared parent is verified as the expected ancestor/parent of a control-only transition and no task field requires current HEAD equality, continue using the verified current control state. Explicit locked-head requirements still use equality and still stop on mismatch.

## Workspace identity correction

When workspace lifecycle matters, establish separately:

- local branch identity;
- remote branch identity;
- worktree registration;
- filesystem path existence/identity;
- HEAD/revision;
- staged/unstaged/untracked/local-only state;
- write capability;
- overlapping authority.

Do not infer one from another. A missing remote branch does not mean a local task branch/worktree is absent; a registered worktree does not prove its path exists; a path does not prove Git registration; a merged PR does not prove local cleanliness or non-writing disposition.

Keep normal checks bounded to task-relevant workspaces and overlapping writers. Historical full-repository archaeology remains a separate reconciliation activity.

## Verification model

Keep `V0`–`V3` as the single risk/scope dimension. Do not add a competing L1–L4 taxonomy.

Add verification cadence as a separate dimension:

- **Construction:** run the narrowest checks that can catch defects introduced by the current edit and support fast iteration.
- **Corrective close:** after a bounded set of related acceptance corrections stabilizes, run the broader affected regression justified by the risk tier once.
- **Task close:** run all checks required by the task acceptance and its risk tier, including any intentionally deferred broader checks.
- **Merge/release boundary:** when integration/release consequence warrants it, verify exact-head/provenance and the broad build/integration/runtime/CI evidence required by the affected system.

Principle: **verification effort follows change risk, not change count**. Multiple small findings from one acceptance cycle should normally be grouped into one bounded corrective when they share an objective and authority. Do not run unrelated full suites after each CSS/copy/small interaction edit. Escalate the risk tier or cadence when the change itself or closure boundary justifies it.

## Source changes

Expected reusable-source changes:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/global-routing.md` (new)
- `skills/project-governance/references/adoption.md` (new)
- `skills/project-governance/references/control-identity.md` (new)
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/references/workspace-lifecycle.md`
- `skills/project-governance/assets/templates/GLOBAL_AGENTS_ROUTING.md` (new)
- `skills/project-governance/assets/templates/AGENTS.md`
- optional focused edits to the other two Skill entry files only where cross-route wording needs alignment.

Repository/source metadata:

- root `AGENTS.md`
- `README.md`
- `plugin.json`
- root `CURRENT_STATUS.md` / `CURRENT_TASK.md`
- maintainer spec/plan files.

## Acceptance scenarios

1. Feature/refactor request routes to Project Governance.
2. Unknown Domain/authority/source/test location invokes Domain Navigation conditionally.
3. Real blocking incident with insufficient evidence invokes Incident Doctor.
4. Incident with unclear source location uses Domain Navigation only for locating evidence, then returns to Doctor.
5. Non-engineering request does not force any Engineering Governance Skill.
6. Adoption into a global file with no block produces one block.
7. Re-adoption with one current block is idempotent.
8. Upgrade with one older block replaces it rather than appending.
9. Multiple/conflicting blocks stop for reconciliation.
10. Verified historical control parent plus later control transition does not trigger false current-head drift.
11. Explicit locked current/execution head mismatch still stops.
12. Multiple small acceptance corrections use focused construction checks and one justified closure regression rather than repeated broad suites.

## Non-goals

No fourth Router Skill, installer executable, runtime service, automatic project mutation, project-level duplication of global routing, release publication, or target-repository migration is part of this task.
