# Execution choices

This reference governs **how to divide actual work**, not whether a task is authorized. Use the active task scope and verified design/source facts.

| Mode | When useful |
| --- | --- |
| Inline (batched) | One cohesive work stream; batch independent reads/searches/edits per turn and verify at milestones |
| Sequential | Dependent units whose outcomes inform later work |
| Parallel read-only | Independent analysis, discovery, or verification |
| Parallel disjoint writers | Demonstrably separate state/files with a clear integration point |

Keep units small enough to have observable completion, but avoid artificial Work Packages. Choose `EXPLORER`, `WORKER`, `VERIFIER`, or `REVIEWER` by actual duty, not by model tier. Chain dependent local verification commands with `&&` in one pass rather than polling or re-running passing suites without new edits.

## Intra-session Plan-to-Execute contract

When a planning turn hands off to an execution turn within the same thread:

1. **Concrete targets**: cite verified paths, symbols, and intended behavior rather than abstract goals.
2. **Single-pass verification**: provide the exact command(s) and expected output that prove completion.
3. **Fail-fast escalation**: define `Re-plan if` triggers so unexpected codebase drift or repeated verification failures return to planning rather than guessing.

## Execution and recovery

A worker receives objective, task authority reference, relevant repository/ref, bounded read/write scope, and expected evidence. Receiving host verifies any source write. Preserve exact local/remote work; reconcile only actual overlapping writes.

If a unit fails, first recover using its existing evidence and rerun the affected unit. Replan material architecture or obtain a user decision only when the active task/risk envelope cannot safely cover the needed change. Do not multiply agents, worktrees, or tests to simulate progress.

Explicit host/user orchestration rules and platform defaults own provider/model/delegation settings; separate contexts do not inherit runtime or persistent permission merely from a Card.
