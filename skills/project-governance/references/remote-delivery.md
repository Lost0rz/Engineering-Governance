# Remote delivery and PR state

Use when a task includes publication of source or another observable remote action. Local edits or commits by themselves do not prove remote delivery.

## Flow

1. Confirm intended repository, base, task branch, current HEAD and actual GitHub writer capability.
2. Reuse the existing authorized branch/PR for same-task fixes when safe.
3. Commit the bounded change, push to the selected remote ref, then read back actual remote SHA and PR state.
4. Report what GitHub observed: pushed, open Draft/ready, CI pending/passed/failed, merged or blocked; do not infer later states.
5. Before a requested merge/release, read live host-required checks, reviews, mergeability and exact head/base identity. Execution permission does not itself approve merge or release.

## Result language

- `PUSHED_VERIFIED`: remote ref readback matches intended commit.
- `NOT_REQUIRED_LOCAL_ONLY` or `NOT_APPLICABLE_NO_REMOTE`: publication not part of task.
- `PENDING` / `FAILED`: no verified remote acceptance.

Preserve remote data and unique local work when a push is rejected or branch histories differ. Report the affected mismatch rather than silently force-pushing or creating another PR. Deployment and installed-runtime verification are separate delivery boundaries.
