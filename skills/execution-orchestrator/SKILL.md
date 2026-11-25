---
name: execution-orchestrator
description: >-
  Choose inline, sequential, or parallel execution, batch independent tool I/O,
  and structure intra-session plan-to-execute handoffs or Sub Agents when
  delegation beats inline execution. Do not use for cohesive single-stream work
  or to override explicit host/user model or delegation rules.
---

# Execution Orchestrator

Use when decomposition, parallel research, intra-session plan/execute handoff, specialist work, or execution recovery materially improves the current task. Host permissions and explicit host orchestration settings govern tools, delegation targets, and model choices.

## Choose execution

1. Determine dependencies, shared mutable state, and real capacity from current work.
2. **Batch first, prefer inline for cohesive work**: parallelize independent searches, file reads, and disjoint edits within one turn before spawning Sub Agents. Delegate only when independence, parallelism, or context isolation saves more effort than coordination costs.
3. For genuine delegation, choose sequential units, parallel read-only units, or disjoint writing units with known integration points.
4. Give each unit its objective, relevant source/authority, exact file/symbol scope, dependencies, verification command, and expected result.
5. Integrate only actual returned evidence; retry affected work or cancel stale units as needed.

## Intra-session Plan-to-Execute handoff

When handing a plan from a higher-reasoning planning phase to an execution phase in the same session, keep the handoff concrete and self-contained:

- list exact verified file paths, symbols, and ordered changes (no guessed locations);
- specify exact verification commands and expected pass criteria;
- name explicit **Re-plan if** stop conditions (missing target, conflicting behavior, twice-failed verification, or scope/risk escalation) instead of letting the executor improvise past the plan.

## Boundaries

- **Host orchestration precedence**: explicit user/host Sub Agent and model-routing rules (for example, global `AGENTS.md` / `GEMINI.md` delegation policies) are authoritative host configuration and are never overridden by plugin defaults.
- A `WORKER` acts only within the current task and real receiving-host permissions; a `REVIEWER`, `VERIFIER`, or `EXPLORER` gathers read-only evidence.
- Concurrent writes need distinct affected state or coordinated integration to protect actual work. Agent count does not grant additional ownership or permission.
- A new agent, session, or execution unit does not imply a new Issue, PR, branch, or worktree.
- Current host-authenticated bounded G1/G2 tasks execute directly; G3 decisions require actual owner authorization.

Read [execution-contract.md](references/execution-contract.md) only for complex delegation, batching, or recovery decisions; [subagent-execution.md](references/subagent-execution.md) for detailed worker boundaries; [environment-capabilities.md](references/environment-capabilities.md) when capabilities are uncertain.
