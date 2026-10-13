# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering Skills, templates, routing/adoption contracts, operating rules, and reference material. An agent reads the relevant capability, inspects the target repository, and adapts guidance to verified project facts.

## Capability model

Engineering Governance v0.6.0 has seven top-level Skills:

- **Project Governance** — normal project/repository entry; three-file control plane, task/scope authority, workspace/writer lifecycle, proportional verification selection, final control alignment, and closeout.
- **Solution Design** — conditional requirements/architecture/design resolution when implementation would otherwise require material guessing.
- **Execution Orchestrator** — conditional decomposition, role/subagent scheduling, parallelism, model-tier policy, recovery ledger, and integration strategy for already-authorized work.
- **Agent Handoff** — bounded cross-agent/session/machine request and receipt contracts using authority references + fresh delta rather than duplicated task/status/rules.
- **Evidence Audit** — independent implementation/code/PR/CI/release/merge-readiness evidence evaluation bound to explicit identities and ranges.
- **Domain Navigation** — conditional evidence-backed routing from task/domain authority to source, symbols, tests, dependencies, and runtime entry points.
- **Incident Doctor** — reactive evidence-gated investigation for a real blocking failure/unsafe ambiguity when current evidence is insufficient.

Global routing is policy, not an eighth Skill.

## Fixed authority model

- `AGENTS.md` owns durable project/repository operating rules.
- `CURRENT_STATUS.md` owns the concise verified current-state snapshot.
- `CURRENT_TASK.md` owns the single active execution authorization.
- Durable planning documents may be linked when they add cross-task value, but they are not a fourth control file.
- Handoff requests/receipts, execution ledgers, audit reports, review packages, and agent briefs do not override those authorities.

## Normal route

For software/project/repository work, enter through **Project Governance**. Use narrower Skills only when their trigger applies, then return to the governing workflow:

```text
project-governance
  -> solution-design (when design is materially unresolved)
  -> execution-orchestrator (when execution topology is non-trivial)
       -> agent-handoff (when responsibility crosses contexts)
  -> evidence-audit (when an independent acceptance/evidence verdict is needed)
  -> domain-navigation (when semantic/source/test routing is unclear)
  -> incident-doctor (only when a blocking evidence gap exists)
```

Clear low-risk work should remain clear and low-risk; installing this Plugin does not force extra design documents, worktrees, agents, TDD ceremonies, or broad audits.

## Handoff model

A handoff is not a second task contract.

```text
HANDOFF = authority references + fresh delta + action boundary + return contract
```

Use it for Web-to-local execution/audit cards, local-to-Web receipts, controller-to-worker briefs, and other cross-context transfers. Reference `AGENTS.md` / `CURRENT_STATUS.md` / `CURRENT_TASK.md` / accepted plans instead of copying their full contents by default.

## Execution and model policy

- Prefer one executor when one context can safely do the work.
- Prefer parallel readers over parallel writers.
- Keep one writer for overlapping semantic authority; multiple writers require proven-disjoint write scopes/workspaces and an integration check.
- Do not dispatch subagents merely because they are available.
- Do not silently escalate to a materially more capable/expensive model. Choose capability proportional to role/risk and state bounded fallbacks where material.
- Any execution ledger is ephemeral recovery state, not task/status authority.

## Evidence and audit

Evidence Audit binds findings to the target/range/identity it actually inspected. Semantic implementation evidence and live repository-host gates remain separate claims. A passing test/CI run on one identity does not automatically prove another identity; `CONTROL_ONLY_DRIFT` reuse remains allowed only under the existing semantic-equivalence/task conditions.

Read-only audit may report stale controls but must not mutate them merely to create a clean receipt.

## Doctor boundary

Incident Doctor remains on demand. A known bug with enough evidence for safe action stays in the normal authorized flow. Enter Doctor only when a real failure/unexplained unsafe ambiguity blocks progress and current evidence is insufficient for the next safe decision.

## Verification

`V0`–`V3` remains the single risk/scope dimension. Verification cadence is separate. Universal mandatory TDD is not an Engineering Governance rule; use regression-first/TDD when the accepted behavior/risk contract makes it the appropriate evidence method.

## Global routing adoption

Project Governance ships:

- `references/global-routing.md` — route-selection semantics;
- `references/adoption.md` — idempotent agent-mediated install/upgrade contract;
- `assets/templates/GLOBAL_AGENTS_ROUTING.md` — managed marker-bounded global routing block.

Adoption verifies all seven Skill identities and exactly one current managed routing block while preserving unrelated global guidance.

## What this repository is not

It is not a business product, installer runtime, generic enforcement engine, daemon, central database, scheduler, MCP server, or automatic remediation platform. External projects are conceptual references, not runtime dependencies.

## Maintainer notes

- `documents/` contains durable design/planning authority for this repository when justified.
- `docs/superpowers/` preserves historical/tool-oriented maintainer planning records; it is not Plugin payload.
- `references/UPSTREAMS.md` records conceptual influences and attribution.
- Formal release publication, local installed-Plugin acceptance, and reusable-source construction are separate lifecycle steps.
