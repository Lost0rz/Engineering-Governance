# CURRENT TASK — Global Routing and v0.4.0 Governance Corrective

Task ID: `EG-GLOBAL-ROUTING-V0.4.0-042`

State: `READY_FOR_MERGE`

Mode: `GOVERNANCE_SKILL_EVOLUTION`

## Objective

Evolve the accepted Plugin v0.3.0 source into a v0.4.0 candidate that adds durable global routing/adoption for the three existing Skills and folds verified pilot corrections into Project Governance without adding a fourth Skill or installer runtime.

## Start authority

- Accepted start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Task branch: `codex/global-routing-v0.4.0`.
- Published baseline: Plugin v0.3.0 remains the last released version until the separate release task completes.
- Final audited reusable source before release-handoff control updates: `0a00ebf1a5ebe17163431fa099249b8e2fc70a22`.

## Accepted implemented scope

1. Global request-to-Skill routing with `project-governance` as the normal project/repository engineering route, `domain-navigation` conditional for unclear semantic/source routing, and `incident-doctor` reactive/evidence-gated.
2. Agent-mediated adoption/upgrade with one marker-bounded global routing block; installation completion requires both three-Skill availability and exactly one current routing block.
3. Control identity semantics separating provenance/transition parents, transition heads, current controls, explicit locked/execution heads, and remote freshness.
4. Workspace lifecycle semantics separating local branch, remote branch, worktree registration/path, HEAD, working-tree/unique-work state, write capability, and overlapping authority, with bounded lifecycle checkpoints during normal development.
5. Construction-time code-structure governance based on Domain/capability/responsibility/authority/lifecycle/dependency/invariants/reason-to-change rather than line count or edit size.
6. Single canonical authority per fact/state/behavior class, with explicit migration boundaries for temporary coexistence.
7. `V0`–`V3` as the single risk/scope taxonomy plus separate construction/corrective/task/merge-release cadence.
8. Reuse of accepted semantic maps; optional Domain navigation projection remains derived routing evidence rather than product/domain truth.
9. Project templates and root guidance updated without copying the full global routing contract into each project.

## Non-goals preserved

- No fourth Router Skill.
- No Bootstrap CLI, installer executable, daemon, hook, MCP server, background service, automatic remediation, or automatic global-file mutation runtime.
- No automatic target-project modification by Plugin runtime.
- No full global `AGENTS.md` rewrite contract; only a marker-bounded managed routing block.
- No Plugin v0.4.0 publication inside this task; publication belongs to the separate release task after merge.
- No changes to target business repositories.

## Verification level and cadence

Level: `V0 + multi-pass semantic/adversarial audit`.

Audit passes covered:

1. routing precedence, route composition, and return paths;
2. adoption/idempotency and partial-install rejection;
3. Domain/semantic navigation and existing-map reuse;
4. canonical authority and responsibility-based code structure;
5. proactive worktree lifecycle checkpoints versus legacy archaeology;
6. control-parent/current-head false-stop regression;
7. verification-risk/cadence separation;
8. package boundary and exact-source publication transport;
9. anti-bypass wording and exact-head re-read.

## Findings resolved

- Template propagation gap for control identity/cadence.
- Installation completion/default-route ambiguity.
- Structure governance initially did not make construction-time responsibility checks explicit enough.
- Workspace lifecycle initially lacked explicit PR/QA/freeze/terminal/successor checkpoints.
- Final release-preflight found one residual wording loophole: a checklist item said `Before writing substantial new code`, which could let a small responsibility-changing edit skip the structure guard. Corrected at `0a00ebf1a5ebe17163431fa099249b8e2fc70a22` so responsibility change, not edit size, is the trigger.

No Critical or Important issue remained after the final exact reusable-source audit.

## Release-relevant invariants

- live `main` remained `b7e47e2de346fa229818013d4369ae60cee6e0fa` through the reusable-source audit;
- exactly three top-level Skill directories remain;
- `plugin.json` version is exactly `0.4.0`;
- routing/adoption artifacts required for installation are under `skills/**` and therefore inside the established Plugin payload boundary;
- managed routing template contains one BEGIN/END marker pair and names all three Skills;
- Project Governance is the default engineering entry; Domain Navigation is conditional; Incident Doctor is reactive/evidence-gated;
- code-structure decisions are responsibility-driven and construction-time;
- workspace governance uses bounded lifecycle checkpoints and keeps full legacy archaeology exceptional;
- explicit locked-head equality remains hard while historical control-parent inequality alone is not drift;
- no competing L1–L4 taxonomy exists;
- no unauthorized runtime/installer mechanism was added.

## Package/release handoff

This task may merge the audited source into `main`. Publication itself requires a new release task after the exact merged source SHA is known.

The release task must:

- verify the merged source contains the same Plugin payload as audited reusable source `0a00ebf1a5ebe17163431fa099249b8e2fc70a22` except permitted control-only merge/source bookkeeping;
- verify `plugin-v0.4.0` Release/tag identity is unused;
- package exactly one `engineering-governance/` root containing only `plugin.json` and `skills/**`;
- verify exactly three top-level Skills and reject symlinks/extra repository files;
- record package size and SHA-256 before upload;
- publish Release `plugin-v0.4.0` targeting the exact accepted merged release-source SHA;
- verify GitHub Release tag target, non-draft/non-prerelease state, asset name/size/digest, and absence of publisher workflow/transport files from `main` and tagged source.

## Stop conditions

Stop merge or release handoff if the final control-only seal contains any Skill/plugin payload change, if `main` drifts before merge, if the PR head is not the exact verified head, or if any routing/Skill/package invariant above is contradicted.

## Handoff / current stop point

User changed the accepted sequence to: **final audit -> publish -> local reinstall -> real acceptance**. Perform one final control-only exact-head comparison after this update. If the delta from reusable source `0a00ebf1a5ebe17163431fa099249b8e2fc70a22` is control-only and `main` is unchanged, merge PR #14 with expected-head protection. Then start the separate Plugin v0.4.0 release task from the exact merged source.
