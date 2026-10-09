# CURRENT TASK — Global Routing and v0.4.0 Governance Corrective

Task ID: `EG-GLOBAL-ROUTING-V0.4.0-042`

State: `WAITING_FOR_INDEPENDENT_AUDIT`

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
2. Added an agent-mediated adoption/upgrade contract and exact managed global `AGENTS.md` routing template. Installation completion now requires both three-Skill availability and exactly one current routing block.
3. Kept the routable/adoption payload under `skills/**`; no fourth Skill or executable installer/runtime was added.
4. Added control identity semantics that distinguish transition/provenance parents, transition heads, current controls, explicit locked/execution heads, and remote freshness.
5. Expanded workspace lifecycle semantics to distinguish local branch, remote branch, worktree registration, filesystem path, HEAD, working-tree/unique-work state, write capability, and overlapping authority.
6. Refined verification policy so `V0`–`V3` remains the risk/scope dimension while construction/corrective/task/merge-release cadence is separate; effort follows change risk, not edit count.
7. Propagated the new semantics into reusable project templates, root repository rules, README, and Plugin candidate metadata `0.4.0`.
8. Added maintainer design and implementation-plan records for this architectural change.

## Non-goals preserved

- No fourth Router Skill.
- No Bootstrap CLI, daemon, hook, MCP server, background service, automatic remediation, or automatic global-file mutation runtime.
- No automatic target-project modification by Plugin runtime.
- No full global `AGENTS.md` rewrite contract; only a marker-bounded managed routing block.
- No Plugin v0.4.0 publication or GitHub Release.
- No changes to target business repositories.

## Verification level, cadence, and rationale

Level: `V0 + semantic scenario audit`.

Rationale: all reusable changes are Markdown contracts/templates plus Plugin metadata; no executable product runtime was changed.

Construction used focused source/path/semantic checks. At corrective close, the complete branch diff was compared with the authorized start revision and the key routing/adoption/control/verification authorities were re-read from exact branch HEAD. Final PR-head verification remains required after this control handoff commit.

## Acceptance scenario result

Author self-audit result before final control sync:

1. project/repository engineering -> Project Governance: PASS;
2. unclear Domain/capability/authority/source/test route -> Domain Navigation conditionally: PASS;
3. real blocking failure + insufficient evidence -> Incident Doctor: PASS;
4. incident with unclear source route -> Doctor -> Domain Navigation -> Doctor: PASS;
5. non-project/non-engineering request -> no forced Engineering Governance route: PASS;
6. no managed block -> insert exactly one: PASS by adoption contract;
7. one current block -> idempotent/no duplicate: PASS;
8. one older compatible block -> replace in place: PASS;
9. multiple/conflicting blocks -> STOP/reconcile: PASS;
10. verified historical control parent -> relationship check, no false equality drift: PASS;
11. explicit locked/current/execution head mismatch -> equality STOP retained: PASS;
12. related small acceptance corrections -> focused construction verification plus justified closure regression: PASS.

## Author self-audit findings and corrective actions

Two Important findings were discovered and fixed before handoff:

- **Template propagation:** initial reusable identity/cadence changes did not yet reach `CURRENT_TASK.md`/`CURRENT_STATUS.md` templates. Corrected.
- **Installation/default routing:** initial adoption did not define Skill availability + routing block as one completion gate, and initial wording allowed simple repository engineering to bypass Project Governance. Corrected so project/repository engineering routes through Project Governance while the Skill itself scales process down for low-risk work.

No remaining Critical or Important issue was found in the author self-audit. This statement is explicitly an author self-review, not independent reviewer evidence.

## Exact source invariants to verify on PR head

- base remains `b7e47e2de346fa229818013d4369ae60cee6e0fa` and live `main` has not materially drifted;
- exactly three top-level Skill directories remain;
- `plugin.json` candidate version is `0.4.0` without a publication claim;
- all routing/adoption files required by install are under `skills/**`;
- managed routing template has one exact BEGIN/END pair and names all three Skills;
- Project Governance is the project/repository engineering default, Domain Navigation conditional, Incident Doctor reactive/evidence-gated;
- project `AGENTS.md` template explicitly avoids duplicating the global routing block;
- control identity preserves explicit locked-head equality while eliminating historical-parent category errors;
- verification policy contains `V0`–`V3` plus cadence and no competing L1–L4 taxonomy;
- diff contains only task-authorized governance/plugin/maintainer-control paths.

## Stop conditions

Stop merge/release if final PR-head verification finds a material route conflict, broken/missing reusable link, extra top-level Skill, incomplete installation completion contract, weakened explicit equality gate, duplicate risk taxonomy, unauthorized runtime/installer mechanism, unexpected diff path, or material `main` drift.

## Handoff / current stop point

Implementation and author self-audit are complete. Open a PR against `main`, verify the exact PR head after this control sync, and leave the PR unmerged. A fresh independent reviewer is still required if the project wants independent-review semantics; the author self-audit must not be represented as that independent review. Plugin publication and target-environment installation are separate future tasks.
