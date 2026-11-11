# Repository identity and freshness

Identity checks exist to avoid applying evidence to the wrong code or host event. Use only the identities material to the selected task.

## Distinguish identities

- **Repository HEAD:** literal Git commit on the selected ref.
- **Delivery/semantic identity:** implementation tree and relevant behavior. In legacy FILE_CONTROL, a diff limited to `CURRENT_STATUS.md` and `CURRENT_TASK.md` is `CONTROL_ONLY_DRIFT`; a mixed source/control diff is not.
- **Task authority:** current approved Issue material revision, authenticated direct USER request, or accepted FILE_CONTROL Task, depending on mode.
- **Host gate:** literal PR head/base, check run, review, merge or release identity. Host gates must be checked against their current ref even when semantic evidence can be reused.

## Reconcile only material changes

1. Verify compared refs and the changed path set before classifying an identity mismatch.
2. Reuse implementation/test evidence across a proved control-only drift when its dependencies and task conditions remain equivalent.
3. Honor an explicit **literal HEAD lock** when the selected task genuinely requires exact equality; otherwise distinguish current repository HEAD from delivery semantics.
4. Recheck live host-required status/reviews for the exact merge/release target. A local PASS cannot substitute for a host gate.
5. If task authority or unique work has actually changed, resolve the affected action; do not create status-only commits just to make identical-looking SHAs.

For meaningful conflicts, return the expected vs observed identity, material changed paths and precise consequence. Issue comments and labels are host metadata rather than Git revisions.
