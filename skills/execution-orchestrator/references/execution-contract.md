# Execution choices

This reference governs **how to divide actual work**, not whether a task is authorized. Use the selected `project-governance` task and existing design/source facts.

| Mode | When useful |
| --- | --- |
| Inline | One cohesive work stream; lowest coordination cost |
| Sequential | Dependent units whose outcomes inform later work |
| Parallel read-only | Independent analysis, discovery or verification |
| Parallel disjoint writers | Demonstrably separate state/files with a clear integration point |

Keep units small enough to have observable completion, but avoid artificial Work Packages. Choose `EXPLORER`, `WORKER`, `VERIFIER` or `REVIEWER` by actual duty, not by model tier.

## Execution and recovery

A worker receives objective, task authority reference, relevant repository/ref, bounded read/write scope and expected evidence. Receiving host verifies any source write. Preserve exact local/remote work; reconcile only actual overlapping writes.

If a unit fails, first recover using its existing evidence and rerun the affected unit. Replan material architecture or obtain a user decision only when the active task/risk envelope cannot safely cover the needed change. Do not multiply agents, worktrees or tests to simulate progress.

The host owns model/provider defaults and availability; separate contexts do not inherit runtime or persistent permission merely from a Card.
