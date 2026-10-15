# CURRENT TASK — Remote Delivery Closeout

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-REMOTE-DELIVERY-CLOSEOUT-087`

Task class: `CAPABILITY_HARDENING`

State: `ACTIVE`

Target Plugin version: `0.7.3` candidate.

## Objective

Close a Project Governance delivery gap where local commits can be reported as completed engineering work even when a configured repository remote exists but the task branch/ref was never pushed, leaving the work unavailable to remote/Web audit.

Repository-backed engineering delivery must distinguish local commit creation from remote publication.

## Required behavior

For a state-changing task that produces Git commits:

- if the repository has an applicable configured remote and the task is not explicitly local-only, successful repository delivery requires pushing the authorized task branch/ref and verifying that the remote ref contains the final delivered commit;
- the rule must not imply pushing `main`; push only the already-authorized branch/ref or project-defined delivery ref;
- if no applicable remote exists, report `REMOTE_DELIVERY: NOT_APPLICABLE_NO_REMOTE` rather than inventing repository publication;
- if project/task authority explicitly defines the work as local-only, report `REMOTE_DELIVERY: NOT_REQUIRED_LOCAL_ONLY`;
- if a remote exists but push cannot be completed or verified, do not report full repository delivery/closeout as complete; preserve the local commit and report a remote-delivery pending/stop state with the blocking reason;
- a local commit SHA is evidence of local source state, not proof of remote delivery.

## Scope

Update only the reusable contracts needed to make remote publication part of repository-backed successful closeout:

- `project-governance` normal development/closeout behavior;
- workspace/local-vs-remote lifecycle evidence where relevant;
- Project Governance user receipt;
- cross-context EXECUTE Handoff Receipt;
- focused acceptance specification/validation;
- Plugin manifest/version as required for the new packaged behavior.

Do not add a daemon, background sync, auto-push service, repository creator, credential manager, or global enforcement runtime.

## Safety boundaries

- never create a remote merely because none exists;
- never guess credentials or bypass remote permissions;
- never force-push unless separately and explicitly authorized by project authority;
- never select `main` merely because it exists;
- preserve local/unique work when push fails;
- remote publication remains bounded by the task's existing write/ref authority;
- read-only tasks do not gain push side effects;
- repository-host merge/review/CI gates remain separate from proof that a commit is remotely visible.

## Acceptance

At minimum the contract must distinguish and correctly handle:

1. Git repo + configured remote + commit + authorized branch -> push and verify remote identity before `COMPLETE`;
2. Git repo + no configured remote -> `NOT_APPLICABLE_NO_REMOTE`;
3. explicit local-only task -> `NOT_REQUIRED_LOCAL_ONLY`;
4. configured remote + push/network/auth failure -> local work preserved, remote delivery not complete;
5. no implicit push to `main` or force push;
6. receipts distinguish `LOCAL_COMMIT` from `REMOTE_DELIVERY` / remote ref identity;
7. no change to read-only task behavior.

## Lifecycle

- formal `plugin-v0.7.2` remains immutable published baseline;
- this task creates the next source candidate rather than mutating v0.7.2 release identity;
- Web/local distribution update and formal v0.7.3 publication are later lifecycle decisions after source acceptance.
