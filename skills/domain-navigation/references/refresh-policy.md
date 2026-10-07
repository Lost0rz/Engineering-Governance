# Refresh policy

# Incremental Domain Map refresh

Refresh navigation evidence when a trigger affects the current task or a mapped area:

- the task-relevant Domain entry is absent or insufficient;
- a source path moved or was removed;
- an important symbol moved, was renamed, or was removed;
- an authority or ownership boundary changed;
- a dependency or consumer relationship materially changed;
- a relevant test changed;
- a runtime or operational entry point changed;
- a verified source contradicts the map;
- the recorded evidence or freshness basis is too stale for the current decision.

Refresh only the affected Domain entry and affected fields. Re-read enough current evidence to verify the changed claim, preserve evidence that remains valid, and record the new revision/observation basis for the fields actually checked.

Do not mark an entire `DOMAIN_MAP.md` freshly verified because one Domain changed. Untouched entries retain their previous freshness; unchecked areas remain `stale` or `unknown` as appropriate. Do not rewrite unrelated Domains or imply they were rechecked.
