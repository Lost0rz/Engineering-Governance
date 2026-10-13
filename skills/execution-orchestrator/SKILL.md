---
name: execution-orchestrator
description: Use when an already-authorized engineering task needs explicit decomposition, multiple execution roles/agents, parallel or sequential scheduling, model-tier selection, resumable multi-step execution, or controlled integration of independent work.
---

# Execution Orchestrator

Use this Skill only after Project Governance has established valid task authority. It controls **how authorized work is executed**, not what work is authorized.

Read [Execution contract](references/execution-contract.md) when orchestration is needed.

## Default posture

The lightest safe executor topology wins.

- One executor is preferred when one context can safely complete the task.
- Parallel readers/scouts/reviewers are preferred over parallel writers.
- Keep one writer for overlapping state/behavior authority.
- Multiple writers require proven-disjoint semantic write scopes/workspaces and a defined integration check.
- Do not dispatch a subagent merely because the capability exists.
- Do not add reviewer-per-task ceremony unless risk/independence justifies it.

## Core flow

1. Read the active task and accepted design/plan it links.
2. Split only where work units have independently checkable outcomes or materially useful context boundaries.
3. Choose topology: inline, sequential delegated, parallel read-only, or proven-disjoint parallel writers.
4. Assign one explicit role, write boundary, context package and model capability tier to each delegated unit.
5. Use `agent-handoff` whenever responsibility crosses an agent/session/machine/context boundary.
6. Integrate returned work under the original task/writer authority; do not trust an agent success message without repository/evidence confirmation.
7. Use an ephemeral recovery ledger only when resume/compaction risk makes it useful.
8. Return topology, actual model policy, integration evidence, unresolved conflicts and resume state to Project Governance.

## Hard rules

- **No silent model escalation or inheritance.** A delegated role must not silently inherit a materially higher controller/session tier.
- **No authority by delegation.** A subagent brief cannot expand scope beyond `CURRENT_TASK.md`.
- **No context dumping by default.** Send bounded authority references, relevant files/tests and fresh delta rather than full chat/control copies.
- **No overlapping concurrent writers without proof.** Branch/worktree separation alone does not prove semantic independence.
- **No blind trust in returned success.** Integration uses actual repository/evidence state.

## Output contract

Report:

- topology and work-unit boundaries;
- role/write authority per unit;
- model tier and fallback actually used;
- completed/failed/skipped work units;
- integration and verification evidence;
- unresolved conflicts/rulings;
- recovery ledger/resume point when incomplete.
