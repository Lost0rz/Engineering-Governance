# Mapping workflow

# Task-to-code mapping workflow

Route from the authorized work to the smallest useful source set:

`CURRENT_TASK -> affected Domain(s) -> DOMAIN_MAP -> candidate authorities / entry points / symbols / tests -> targeted search or optional Repo Map -> focused source reading -> confirmed route + unresolved gaps`

1. Read the current `CURRENT_TASK` and applicable project controls. Keep the navigation target within that task or an explicitly bounded mapping goal.
2. Identify the affected Domain(s) from the task and the project's `DOMAIN_MAP.md`.
3. Follow the relevant Domain entry to candidate authority sources, entry points, symbols, and tests. Verify that each source is current enough for this decision.
4. If a task-relevant entry is missing or insufficient, inspect only the smallest evidence set needed to route this work. Depending on the question, this may include applicable controls and accepted intent/docs, repository manifests and source entry points, relevant tests, imports or references found from those paths, and runtime/operational entry points when relevant.
5. Use targeted search or an optional Repo Map to choose candidate files or symbols when useful. Treat results as leads, then read the focused sources directly.
6. Report the confirmed route: which files to read and why, relevant symbols/tests, the authority for each needed fact class, and which relationships are directly observed. Keep unsupported ownership, missing paths, and conflicts explicitly unresolved.

Do not start with a whole-repository survey by default. Expand to whole-repository mapping only when the authorized task genuinely requires that scope; otherwise follow references outward only as needed to answer the routing question.
