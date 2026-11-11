# Task authority and project control

Select the active mode using the installed `CONTROL_POLICY_V1` and verified repository enrollment. Project `AGENTS.md` holds product-specific constraints, not the global workflow switch.

| Mode | Owner of active task | Progress evidence |
| --- | --- | --- |
| `ISSUE_CONTROL` | Selected approved Issue **or** current host-authenticated bounded USER-directed G1/G2 request | Issue/PR/commit/CI evidence when relevant; direct tasks need no first Issue |
| `FILE_CONTROL` (legacy, unenrolled) | `CURRENT_TASK.md` | `CURRENT_STATUS.md` as a verified projection |

## FILE_CONTROL only

- `AGENTS.md` describes stable project architecture/product/runtime constraints; `CURRENT_TASK.md` defines current task intent and authorization; `CURRENT_STATUS.md` summarizes observed progress.
- Design plans and Domain maps own their domain meaning; they are not additional approval records.
- Refresh Task/Status only on actual changes to task authority, material results, or terminal state. Read-only inspections report outdated facts without modifying them.
- Control-only commits can move repository HEAD without changing implementation semantics; verify changed paths before deciding that code evidence is stale.
- After an externally verified merge, record bounded `POST_MERGE_DRIFT` and reconcile at the next authorized write when safe. Do not reuse a terminated task for new source changes.

## ISSUE_CONTROL

An Issue write is not a Git commit and does not move repository HEAD. A direct current-session user task needs no Issue or progress-document synchronization. For Issue-backed work, bind the relevant approved revision and material decisions; ordinary PR/CI evidence need not be copied into another file.

Use [control-identity.md](control-identity.md) only when an actual identity/freshness conflict affects the decision. Host merge/release gates remain separate from task execution.
