# V074 Remote Delivery Acceptance

## Purpose

Validate the Project Governance correction that separates local Git commit creation from remote repository delivery.

## Required claims

A successful repository-backed state-changing closeout must satisfy the applicable delivery class below.

### A. Remote-backed delivery

Given:
- a Git repository;
- an applicable configured remote;
- a state-changing task that produced commits;
- no explicit local-only authority.

Require:
- the final delivered commit is pushed to the authorized task/project ref;
- the remote ref is re-read and proves the final delivered commit is remotely reachable/visible;
- a local commit SHA alone is insufficient;
- failure to push or verify remote delivery prevents a full `COMPLETE` repository-delivery claim.

### B. No remote

Given a Git repository with no applicable configured remote:

Require:

`REMOTE_DELIVERY: NOT_APPLICABLE_NO_REMOTE`

Do not create a remote solely to satisfy governance.

### C. Explicit local-only task

Given project/task authority that explicitly requires local-only execution:

Require:

`REMOTE_DELIVERY: NOT_REQUIRED_LOCAL_ONLY`

Do not invent publication side effects.

### D. Push failure

Given an applicable remote but network/auth/permission/non-fast-forward or another push failure:

Require:
- local commits/work are preserved;
- the failure is reported with the affected remote/ref;
- full remote delivery is not claimed;
- force-push, credential bypass, remote creation or branch substitution is not attempted unless separately authorized.

### E. Ref safety

Require:
- governance never chooses `main` merely because it exists;
- push target follows existing task/project ref authority;
- force push is never implied by normal closeout;
- read-only work remains non-mutating.

## Receipt contract

For repository-backed state-changing work, receipts distinguish:

```text
LOCAL_COMMIT: <sha | NONE>
REMOTE_DELIVERY: PUSHED_VERIFIED | NOT_APPLICABLE_NO_REMOTE | NOT_REQUIRED_LOCAL_ONLY | PENDING | FAILED
REMOTE_REF: <remote/ref | NONE | UNKNOWN>
REMOTE_COMMIT: <sha | NONE | UNKNOWN>
```

When `REMOTE_DELIVERY` is `PENDING` or `FAILED`, the outcome must not imply remotely available completion.

## Source acceptance

Source acceptance is PASS only when:
- Project Governance normal flow includes the remote-delivery gate;
- local commit creation is explicitly not sufficient evidence of remote repository delivery;
- Agent Handoff EXECUTE receipts can report remote-delivery evidence;
- the compact Project Governance receipt exposes remote-delivery state when applicable;
- Plugin version advances beyond the immutable `plugin-v0.7.2` release identity;
- focused validation confirms the required markers and nine-Skill package structure.

Runtime acceptance may later exercise representative remote/no-remote/push-failure cases in a disposable repository. Runtime tests must not force-push, bypass authentication or mutate production repositories.
