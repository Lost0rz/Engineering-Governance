# CURRENT TASK — Global Routing and v0.4.0 Governance Corrective

Task ID: `EG-GLOBAL-ROUTING-V0.4.0-042`

State: `READY_FOR_INSTALLATION_ACCEPTANCE`

Mode: `GOVERNANCE_SKILL_EVOLUTION`

## Objective

Evolve the accepted Plugin v0.3.0 source into a v0.4.0 candidate that adds a durable global routing/adoption contract for the three existing Skills and folds verified pilot corrections back into Project Governance without adding a fourth Skill or an installer runtime.

## Start authority

- Accepted start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Task branch: `codex/global-routing-v0.4.0`.
- Published baseline: Plugin v0.3.0 remains the last released version until a separate release task is authorized and verified.
- Start revision role: exact task branch parent/current `main` at authorization, not a historical control-parent field.

## Implemented scope

1. Added a global request-to-Skill routing contract with `project-governance` as the normal route for project/repository engineering work, `domain-navigation` as conditional semantic/source routing, and `incident-doctor` as reactive evidence-gated diagnosis.
2. Added an agent-mediated adoption/upgrade contract and exact managed global `AGENTS.md` routing template. Installation completion requires both three-Skill availability and exactly one current routing block.
3. Kept the routable/adoption payload under `skills/**`; no fourth Skill or executable installer/runtime was added.
4. Added control identity semantics that distinguish transition/provenance parents, transition heads, current controls, explicit locked/execution heads, and remote freshness.
5. Expanded workspace lifecycle semantics to distinguish local branch, remote branch, worktree registration, filesystem path, HEAD, working-tree/unique-work state, write capability, and overlapping authority, with bounded lifecycle checkpoints during normal development rather than cleanup-only governance.
6. Refined verification policy so `V0`–`V3` remains the risk/scope dimension while construction/corrective/task/merge-release cadence is separate; effort follows change risk, not edit count.
7. Strengthened code-structure governance so responsibility/Domain/capability/authority/lifecycle/reason-to-change boundaries are checked while code is being designed and written. File length or edit size is not a split trigger; a materially new responsibility is.
8. Propagated the reusable semantics into project templates, root repository rules, README, and Plugin candidate metadata `0.4.0`.
9. Added maintainer design and implementation-plan records for this architectural change.

## Non-goals preserved

- No fourth Router Skill.
- No Bootstrap CLI, daemon, hook, MCP server, background service, automatic remediation, or automatic global-file mutation runtime.
- No automatic target-project modification by Plugin runtime.
- No full global `AGENTS.md` rewrite contract; only a marker-bounded managed routing block.
- No Plugin v0.4.0 publication or GitHub Release.
- No changes to target business repositories.

## Verification level, cadence, and rationale

Level: `V0 + multi-pass semantic/adversarial audit`.

Rationale: all reusable changes are Markdown contracts/templates plus Plugin metadata; no executable product runtime was changed.

Construction used focused source/path/semantic checks. The candidate then received multiple exact-source audit passes against the live PR/base and prior failure modes. No CI/runtime/build PASS is claimed because this repository has no applicable executable change or status check on the candidate HEAD.

## Multi-pass audit rounds

1. **Routing/adoption audit** — verified default Project Governance routing, conditional Domain Navigation, reactive Incident Doctor, managed-block idempotency, and the two-part installation completion contract.
2. **Domain/code-structure audit** — verified Domain means semantic capability/responsibility/authority rather than folder shape; file/module splits are responsibility-based rather than line-count based; structure checks now happen before a new responsibility is introduced and are re-run when implementation discoveries change the boundary.
3. **Workspace lifecycle audit** — verified local/remote branch, registration/path, HEAD, working-tree/unique-work, write capability, and overlapping authority are separate facts; added bounded lifecycle checkpoints at workspace selection, successor-writer decisions, retained-state transitions, terminal events, and before overlapping next tasks. Legacy archaeology remains a one-time recovery path rather than normal development.
4. **Historical failure regression audit** — replayed control-parent false drift, repeated full-regression overhead, duplicate authority/backend risk, incident-diagnostics overgrowth, stale-worktree accumulation, and Domain/source uncertainty against the final contracts.
5. **Anti-bypass/exact-head audit** — removed the remaining wording that could let a small edit bypass structure governance merely because it was not “substantial”; verified the final diff remains within authorized governance/plugin/maintainer paths and live `main` remains at the authorized base.

## Corrective findings resolved

Four material categories were found across implementation plus the multi-pass audit and corrected before installation acceptance:

- **Template propagation:** reusable control-identity/cadence rules initially did not reach `CURRENT_TASK.md`/`CURRENT_STATUS.md` templates.
- **Installation/default routing:** initial adoption did not bind Skill availability + routing block into one completion gate, and early wording allowed simple repository engineering to bypass Project Governance.
- **Construction-time structure enforcement:** responsibility-based splitting existed, but the trigger could still be read as a review/final-cleanup concern. It now applies when a source edit introduces a new responsibility/authority boundary, independent of file length or edit size.
- **Workspace lifecycle prevention:** pre-task and terminal rules existed, but routine retained-state/successor checkpoints were not explicit enough. They are now explicit and bounded so healthy projects close lifecycle debt while evidence is fresh without repeated historical archaeology.

No remaining Critical or Important issue was found after the fifth pass.

## Acceptance scenario result

1. project/repository engineering -> Project Governance: PASS;
2. simple low-risk repository change -> Project Governance with lightweight procedure, no forced worktree/plan/full scan: PASS;
3. unclear Domain/capability/authority/source/test route -> Domain Navigation conditionally: PASS;
4. existing Domain/semantic map is sufficient -> reuse it without creating duplicate `DOMAIN_MAP.md`: PASS;
5. real blocking failure + insufficient evidence -> Incident Doctor: PASS;
6. bug with sufficient evidence -> remain in normal Project Governance flow: PASS;
7. incident with unclear source route -> Doctor -> Domain Navigation -> Doctor: PASS;
8. non-project/non-engineering request -> no forced Engineering Governance route: PASS;
9. no managed block -> insert exactly one: PASS by adoption contract;
10. one current block -> idempotent/no duplicate: PASS;
11. one older compatible block -> replace in place: PASS;
12. multiple/conflicting blocks -> STOP/reconcile: PASS;
13. historical control parent -> relationship check, no false equality drift: PASS;
14. explicit locked/current/execution head mismatch -> equality STOP retained: PASS;
15. several related small corrections -> focused construction verification plus justified closure regression: PASS;
16. large but cohesive file -> no automatic size-driven split: PASS;
17. small or large edit adds a second responsibility -> establish Domain/responsibility boundary during construction: PASS;
18. task enters PR/QA/frozen/terminal lifecycle state -> bounded workspace checkpoint: PASS;
19. unrelated old worktrees with no task relevance -> no routine full archaeology: PASS;
20. accumulated ambiguous historical workspaces -> explicit bounded legacy reconciliation path remains available: PASS.

## Exact source invariants

- base remains `b7e47e2de346fa229818013d4369ae60cee6e0fa` and live `main` had not drifted at the final pre-control audit;
- exactly three top-level Skill directories remain;
- `plugin.json` candidate version is `0.4.0` without a publication claim;
- all routing/adoption files required by install are under `skills/**`;
- managed routing template has one exact BEGIN/END pair and names all three Skills;
- Project Governance is the project/repository engineering default, Domain Navigation conditional, Incident Doctor reactive/evidence-gated;
- code structure uses semantic responsibility/authority boundaries rather than line count and applies during construction;
- workspace lifecycle uses bounded checkpoints during development and keeps full legacy archaeology exceptional;
- project `AGENTS.md` template avoids duplicating the global routing block;
- control identity preserves explicit locked-head equality while eliminating historical-parent category errors;
- verification policy contains `V0`–`V3` plus cadence and no competing L1–L4 taxonomy;
- diff contains only task-authorized governance/plugin/maintainer-control paths.

## Review-independence note

This multi-pass audit deliberately re-read the exact PR source and evaluated it adversarially rather than trusting implementation claims. However, the same ChatGPT conversation also authored corrective commits, so this task does **not** claim separate-actor or separate-model independence. If strict independent-review semantics require a different reviewer identity, that remains a separate optional merge gate. The user authorized this multi-pass audit as the pre-installation gate.

## Stop conditions

Stop merge/release or installation acceptance if final exact-head verification finds a material route conflict, broken/missing reusable link, extra top-level Skill, incomplete installation completion contract, weakened explicit equality gate, size-driven structure rule, cleanup-only workspace governance, duplicate risk taxonomy, unauthorized runtime/installer mechanism, unexpected diff path, or material `main` drift.

## Handoff / current stop point

Multi-pass audit and corrective work are complete. Perform one final read-only exact-head check after this control sync. If that passes, the candidate may proceed to **installation acceptance** while PR #14 remains Draft/unmerged. Plugin publication and merge remain separate decisions.
