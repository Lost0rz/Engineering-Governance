# Workspace lifecycle

Use when a task actually needs a branch, checkout, worktree, or workspace cleanup. A task and its execution contexts are not the same as a Git branch, worktree or PR.

## Choose the smallest safe workspace

1. **Read-only or no change:** inspect from an existing safe checkout or the remote host.
2. **Same task:** reuse the valid branch, PR and checkout. Repair, another session, or another agent does not itself create a successor.
3. **New writing task:** use a safe existing checkout and a task branch when appropriate. Add a distinct worktree only for materially independent work, actual concurrent isolated writers, incompatible runtimes, or preservation of unique local work.
4. **Conflicting edits:** check the files and active work that actually overlap. Resolve those edits before touching them; unrelated work continues.
5. **Finish:** retain a workspace while review, testing or recovery needs it; otherwise clean up after checking for unique work and task-specific terminal conditions.

## Evidence that matters

- Before a risky switch or cleanup, inspect relevant `git status`, local branch/worktree identity, HEAD and uncommitted/untracked work. Remote branches and PRs cannot prove local worktree state.
- Preserve unique local commits, staged/unstaged files and untracked assets. Use non-destructive reconciliation before reset, overwrite or deletion.
- Keep durable task data under the canonical project storage authority unless a project-specific rule or host runtime requires otherwise.
- A merge, deployment or closure is a host event, not evidence that a local workspace is already clean or disposable.
- Record a reason and next disposition only for an additional durable worktree or an actual unresolved collision.

## Mode and authority

`FILE_CONTROL` reads the accepted Task for writing authority; `ISSUE_CONTROL` uses the selected approved Issue or host-authenticated current USER-directed bounded G1/G2 task. Neither mode grants permission to overwrite conflicting work. Project-specific checkout and branch rules still apply. Read [control-plane.md](control-plane.md) only for a material control transition.
