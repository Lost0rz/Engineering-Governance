# CURRENT TASK — Repository Branch Hygiene

Task ID: `EG-REPO-BRANCH-HYGIENE-027`

State: `AUTHORIZED_FOR_LOCAL_EXECUTION`

Mode: `REMOTE_BRANCH_CLEANUP_ONLY`

## Objective

Remove only obsolete remote task/control branches that have been independently verified as fully contained in the accepted post-audit `main`, leaving a clean remote baseline before adoption.

## Authority and baseline

- Accepted post-audit reusable/content baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Control commit that authorizes this cleanup is the live `origin/main` when execution begins; fetch it fresh and use that live SHA as cleanup authority.
- No open PRs existed at the final Web audit.

## Exact remote branches authorized for deletion

- `codex/cross-project-corrective`
- `codex/domain-navigation-audit-corrective`
- `codex/domain-navigation-enrichment`
- `codex/final-root-cross-skill-corrective`
- `codex/incident-doctor-audit-corrective`
- `codex/incident-doctor-enrichment`
- `codex/project-governance-audit-corrective`
- `codex/project-governance-enrichment`
- `codex/skill-repository-skeleton-reset`
- `control/root-consistency-freeze-auth`

## Required pre-delete verification

After `git fetch origin --prune`:

1. verify the repository is `Lost0rz/Engineering-Governance`;
2. read current `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` from `origin/main` and confirm this Task ID/mode;
3. for each listed remote branch, verify its tip is an ancestor of `origin/main` (`git merge-base --is-ancestor <remote-ref> origin/main` must succeed);
4. verify there are no open PRs targeting or sourced from a listed branch if local GitHub tooling can establish that; if this cannot be checked, report it but do not substitute guesswork for the already established Web evidence;
5. do not delete any branch not in the exact list.

If any listed branch is not contained in `origin/main`, STOP before deleting anything and return the branch/ref/SHA evidence.

## Authorized action

Delete the exact listed remote branches with normal non-force remote deletion. No repository file modification, commit, reset, rebase, merge, tag mutation, force-push, local-work destruction, or target-project action is authorized.

Local branches/worktrees are not part of this task. Do not delete them merely because the corresponding remote branch is removed; preserve any unknown local state for a separate evidence-backed cleanup if needed.

## Verification after cleanup

- `git fetch origin --prune`;
- list remote branches and confirm only the intended active baseline remains (`origin/main`, excluding symbolic `origin/HEAD` if present);
- confirm `origin/main` did not move during deletion;
- confirm historical tags remain unchanged, especially `v0.1.0`;
- working tree remains unchanged/clean relative to its pre-task state.

## Stop conditions

- authority/control mismatch;
- `origin/main` changes materially during cleanup;
- any authorized deletion target is not fully contained in `origin/main`;
- deletion would require force;
- any unique remote work is discovered;
- any repository file would need modification.

## Final receipt

Return only:

- `TASK_ID`
- `ORIGIN_MAIN_BEFORE`
- `ORIGIN_MAIN_AFTER`
- `DELETED_REMOTE_BRANCHES`
- `REMOTE_BRANCHES_FINAL`
- `ALL_DELETED_BRANCHES_WERE_ANCESTORS`
- `OPEN_PR_CHECK`
- `TAG_CHECK`
- `WORKTREE_MUTATED`
- `FINAL_STATE`

## Current stop point

`AUTHORIZED_FOR_LOCAL_EXECUTION`
