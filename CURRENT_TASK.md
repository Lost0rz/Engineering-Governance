# CURRENT TASK — Global Routing and v0.4.0 Governance Corrective

Task ID: `EG-GLOBAL-ROUTING-V0.4.0-042`

State: `ACTIVE`

Mode: `GOVERNANCE_SKILL_EVOLUTION`

## Objective

Evolve the accepted Plugin v0.3.0 source into a v0.4.0 candidate that adds a durable global routing/adoption contract for the three existing Skills and folds verified pilot corrections back into Project Governance without adding a fourth Skill or an installer runtime.

## Start authority

- Accepted start `main`: `b7e47e2de346fa229818013d4369ae60cee6e0fa`.
- Task branch: `codex/global-routing-v0.4.0`.
- Published baseline: Plugin v0.3.0 remains the last released version until a separate release task is authorized and verified.

## Authorized scope

1. Add a global request-to-Skill routing contract with `project-governance` as the normal engineering entry point, `domain-navigation` as conditional semantic/source routing, and `incident-doctor` as reactive evidence-gated diagnosis.
2. Add an agent-mediated adoption/upgrade contract that can install exactly one managed Engineering Governance routing block into a user's global `AGENTS.md`, preserve unrelated global rules, and update the block idempotently.
3. Keep the routable payload inside `skills/**` so the existing Plugin packaging boundary can ship it.
4. Correct Project Governance semantics proven by v0.3.0 application:
   - distinguish control provenance/transition anchors from required current/locked heads;
   - distinguish local branch, remote branch, registered worktree, filesystem path, HEAD, working-tree state, write capability, and overlapping authority;
   - keep workspace discovery task-bounded rather than turning normal work into historical archaeology.
5. Refine verification policy so effort follows change risk, not change count, and separate risk tier (`V0`–`V3`) from execution cadence (construction, corrective close, task close, merge/release boundary).
6. Update package/source documentation and version metadata consistently for the v0.4.0 candidate.
7. Add scenario-based routing/adoption/identity verification material sufficient for a V0 semantic audit.

## Non-goals

- No fourth Router Skill.
- No Bootstrap CLI, daemon, hook, MCP server, background service, automatic remediation, or global-file mutation runtime.
- No automatic target-project modification by Plugin runtime.
- No rewriting an entire global `AGENTS.md`; only the managed routing block contract is defined.
- No Plugin v0.4.0 publication or GitHub Release in this task.
- No changes to target business repositories.

## Design constraints

- Global routing decides **which Skill to load**; it must not duplicate the detailed workflow owned by the Skills.
- Project-local `AGENTS.md` remains project-specific and must not receive a duplicate copy of the global routing policy by default.
- Installation/adoption is performed by an AI agent after inspecting the existing global file; unrelated user rules are preserved.
- Managed-block upgrade is idempotent: zero blocks becomes one block; one compatible/older block becomes one updated block; multiple/conflicting blocks are an ambiguity that must be reconciled rather than blindly appended.
- Existing v0.3.0 business-first and Doctor-on-demand boundaries remain intact.

## Verification

Level: `V0 + semantic scenario audit`.

Rationale: this task changes reusable Markdown contracts, templates, and package metadata but introduces no executable runtime. Verification must establish path/layout integrity, frontmatter/link consistency, package-payload reachability, non-duplication of authority, scenario routing correctness, idempotent managed-block semantics, and exact diff scope.

Required scenarios:

- normal feature/refactor -> Project Governance;
- unclear Domain/capability/authority/source/test route -> Domain Navigation within governed work;
- real blocking failure + insufficient evidence -> Incident Doctor;
- incident with unclear source route -> Incident Doctor may use Domain Navigation only for locating evidence;
- simple non-project/non-engineering request -> no forced Engineering Governance route;
- existing managed route -> replace/update rather than append;
- multiple/conflicting managed route blocks -> stop/reconcile;
- historical `control_parent` that is a verified transition ancestor -> no false `HEAD != parent` drift stop;
- explicitly locked current/execution head -> equality gate remains valid;
- multiple small acceptance corrections -> focused verification during construction, broader verification once at the appropriate closure boundary.

## Acceptance

- The Plugin candidate still contains exactly three top-level Skills.
- A packaged `skills/**` payload contains the routing/adoption contract and managed-block template.
- The routing contract has one clear default entry and no circular Router-Skill dependency.
- Project/global routing ownership is explicit and nonduplicative.
- Control identity semantics prevent the verified v0.3.0 false-positive parent/current-head interpretation without weakening explicit locked-head gates.
- Verification semantics preserve `V0`–`V3` as the risk dimension and add cadence without a competing second risk taxonomy.
- Root repository rules no longer describe agent-mediated adoption as forbidden while continuing to forbid an installer/runtime platform.
- Exact branch diff contains only files authorized above.
- A detailed remote audit of the exact final branch head finds no material correctness or governance-ownership issue.

## Stop conditions

Stop state-changing work if `main` moves in a way that materially invalidates this task's start authority or creates overlapping changes to the same governance authorities; if a change requires an executable installer/runtime; if routing requires duplicating full Skill workflows into global rules; or if exact semantics cannot be kept backward-compatible with the three-Skill capability model.

## Current point

Authorized for remote-only implementation on `codex/global-routing-v0.4.0`. The user explicitly selected direct inline construction followed by detailed audit. Do not merge or publish from this task without a separate integration decision.
