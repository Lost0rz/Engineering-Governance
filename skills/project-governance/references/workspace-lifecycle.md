# Workspaces: reuse first, protect real work

Use a safe existing checkout/branch/PR for an ongoing task. Read-only inspection ordinarily needs no new branch or worktree. Add a separate worktree only when actual isolation, independent long-lived work or concurrent disjoint writes justify its cost.

Before switching, merging or cleaning up, inspect the **relevant** branch/ref, local dirty state, untracked/unique work and actual overlapping writers when those facts can affect the action. A historical branch or theoretical writer is not a lock. Preserve real unique work.

A new Issue, Card, agent, session, test command or correction does not itself imply a new workspace or PR. Use the existing PR for the same objective.

Clean up only when the project no longer needs the workspace and its unique work is accounted for. A remote merge proves neither a local clean checkout nor a safe deletion. Project-specific branch/worktree rules and true host permissions still apply.
