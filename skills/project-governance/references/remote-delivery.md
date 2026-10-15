# Remote repository delivery

## Purpose

A local Git commit proves local source state. It does **not** prove that repository-backed engineering work is remotely available to Web review, another machine, CI, PR creation, or later continuation.

For state-changing governed work, classify remote delivery separately from local commit creation before claiming successful repository delivery/closeout.

## Applicability gate

Apply this gate when the task produced or advanced Git commits.

Resolve only the facts needed for the current repository:

1. Is the workspace inside a Git repository?
2. Is there an applicable configured remote for the project/task delivery path?
3. Does project/task authority explicitly require local-only execution?
4. Which branch/ref is already authorized for remote publication?

Do not create a remote merely because none exists. Do not infer that `main`, `master`, or another default branch is the correct push target.

## Delivery classes

### `PUSHED_VERIFIED`

Use only when:

- an applicable remote exists;
- remote publication is not prohibited/local-only;
- the final delivered commit was pushed to the already-authorized task/project ref;
- fresh remote-ref evidence proves the delivered commit is remotely reachable/visible at the claimed ref.

A successful local `git commit` or clean working tree is not enough.

### `NOT_APPLICABLE_NO_REMOTE`

Use when no applicable configured remote exists.

This is a valid terminal delivery class for local-only repositories. Do not create a remote or repository solely to satisfy governance.

### `NOT_REQUIRED_LOCAL_ONLY`

Use only when accepted project/task authority explicitly defines the work as local-only or prohibits remote publication.

The mere absence of an upstream branch is not proof of local-only intent.

### `PENDING` / `FAILED`

Use when remote publication is applicable but cannot yet be completed or verified, including network, authentication, authorization, non-fast-forward, remote policy, ambiguous push target, or other delivery failures.

Preserve local commits and unique work. Do not report remotely available completion.

## Push safety

Normal successful closeout authorizes only publication already implied by the active repository/task delivery boundary. It does not authorize broader repository mutation.

Never, solely for closeout:

- force-push;
- bypass credentials/permissions;
- create or replace a remote;
- substitute another branch/ref when the authorized target fails;
- push directly to `main` merely because it exists;
- delete or rewrite remote history.

If the correct remote/ref is materially ambiguous, keep remote delivery unresolved and return to project/task authority rather than guessing.

## Verification

After push, verify the exact remote/ref relevant to the task. Evidence may be a freshly fetched remote-tracking ref, remote API/ref readback, or another authoritative repository-host observation.

Report separately:

```text
LOCAL_COMMIT: <sha | NONE>
REMOTE_DELIVERY: PUSHED_VERIFIED | NOT_APPLICABLE_NO_REMOTE | NOT_REQUIRED_LOCAL_ONLY | PENDING | FAILED
REMOTE_REF: <remote/ref | NONE | UNKNOWN>
REMOTE_COMMIT: <sha | NONE | UNKNOWN>
```

`REMOTE_COMMIT` may equal `LOCAL_COMMIT`, or may be a host-created merge/result identity when the task explicitly claims that later boundary. State which proposition is being verified.

## Closeout rule

For repository-backed state-changing work where remote publication is applicable, a final success claim such as `COMPLETE`, `DELIVERED`, `READY_FOR_REMOTE_REVIEW`, or equivalent must not rely only on local commit state.

If remote delivery is `PENDING` or `FAILED`, use a bounded state such as:

```text
LOCAL_COMPLETE_REMOTE_PENDING
STOP_REMOTE_DELIVERY
```

and report the blocking reason plus the preserved local identity.

Control reconciliation may still record that implementation is locally complete and remote publication is pending. It must not erase the distinction.

## Relationship to other boundaries

- Remote delivery proves remote availability of the claimed commit/ref. It does not prove CI, review, mergeability, merge, release, deployment, or acceptance.
- Repository-host gates remain separate live constraints.
- Workspace lifecycle remains separate: a pushed commit does not prove local cleanup, and local cleanup must not discard the only copy of required unpushed work.
- Read-only tasks do not gain push side effects from this contract.
