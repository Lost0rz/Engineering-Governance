# Artifact ownership and refresh

Each fact has one working owner. Update the owner when the underlying meaning changes, and refresh derived views only if they would otherwise mislead readers.

| Artifact | Role |
| --- | --- |
| Source/code/schema/API | Implemented behavior and source-owned contracts |
| Accepted design / domain docs | Product and architecture decisions |
| Global plugin Skills | Shared engineering workflow and methods |
| Project `AGENTS.md` | Project-specific enduring constraints |
| Legacy Task/Status | Selected FILE_CONTROL task and progress projection |
| GitHub Issue/PR/CI | Issue-backed task, remote change and observed host results |
| Project Profile / maps / receipts | Derived navigation or evidence, not additional write grants |

## Reconciliation

1. Identify the changed semantic fact and its owner.
2. Update that owner, with just the dependent pointers/projections whose meaning became stale.
3. Leave unrelated artifacts unchanged. A no-op observation needs no new commit.
4. Keep delivery/provenance and actual host state distinct from documentation claims.

Task/Issue authority and product semantic state can evolve on different schedules. Project history remains discoverable through Git and GitHub rather than copied into routine handoff documents.
