---
name: execution-orchestrator
description: Choose inline, sequential or parallel execution only when delegation materially helps the current authorized engineering task.
---

# Execution Orchestrator

Use when decomposition, parallel research, specialist work or execution recovery would materially improve an existing task. `project-governance` keeps task authority and delivery; the host owns tools and model choices.

## Choose execution

1. Determine dependencies, shared mutable state and real capacity from current work.
2. Prefer **inline** for cohesive work; delegate only when independence, parallelism or isolation saves more effort than it costs.
3. For genuine delegation, choose sequential units, parallel read-only units or disjoint writing units with known integration points.
4. Give each unit its objective, relevant source/authority, affected files or state, dependencies and expected result.
5. Integrate only actual returned evidence; retry affected work or cancel stale units as needed.

No separate decision-record field is needed for an ordinary Sub Agent choice. Explain the reason only when unusual concurrency, cost or write conflicts materially affect the task.

## Boundaries

- A `WORKER` acts only within the current task and real receiving-host permissions; a `REVIEWER`, `VERIFIER` or `EXPLORER` gathers read-only evidence.
- Concurrent writes need distinct affected state or coordinated integration to protect actual work. Agent count does not grant additional ownership or permission.
- A new agent, session or execution unit does not imply a new Issue, PR, branch or worktree.
- Current host-authenticated bounded G1/G2 tasks can execute directly; legacy Issue tasks retain their selected approved scope. G3 decisions require actual owner authorization.
- The execution host chooses provider/model/reasoning and may impose its own isolation rules.

Read [execution-contract.md](references/execution-contract.md) only for a complex delegation or recovery decision; [subagent-execution.md](references/subagent-execution.md) for detailed worker boundaries; [environment-capabilities.md](references/environment-capabilities.md) when capabilities are uncertain.
