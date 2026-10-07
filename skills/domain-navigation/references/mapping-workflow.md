# Mapping workflow

# Task-to-code mapping workflow

Route from the authorized work to the smallest useful source set:

`CURRENT_TASK -> affected Domain(s) -> existing semantic authorities and/or navigation projection -> candidate authorities / entry points / symbols / tests -> targeted search or optional Repo Map -> focused source reading -> confirmed route + unresolved gaps`

1. Read the current `CURRENT_TASK` and applicable project controls. Keep the navigation target within that task or an explicitly bounded mapping goal.
2. Discover accepted business, product, domain, and capability maps already present in the target repository, regardless of filename. Determine which semantic facts they actually own; do not assume a file named `DOMAIN_MAP.md` must exist or that a similarly named document is authoritative without evidence.
3. Identify the affected Domain(s) from the task and those accepted semantic authorities. If a current navigation projection exists, follow it to candidate authority sources, entry points, symbols, and tests and verify that each source is current enough for this decision.
4. If no navigation projection exists, or the existing one is missing or insufficient, route from the accepted semantic authorities and inspect only the smallest evidence set needed for this work. Depending on the question, this may include applicable controls and accepted intent/docs, repository manifests and source entry points, relevant tests, imports or references found from those paths, and runtime/operational entry points when relevant. Create or refresh a separate navigation projection only when durable source/symbol/test routing adds value beyond the existing semantic authorities; do not duplicate their business/domain truth.
5. Use targeted search or an optional Repo Map to choose candidate files or symbols when useful. Treat results as leads, then read the focused sources directly.
6. Report the confirmed route: which files to read and why, relevant symbols/tests, the authority for each needed fact class, and which relationships are directly observed. Keep unsupported ownership, missing paths, and conflicts explicitly unresolved.

Do not start with a whole-repository survey by default. Expand to whole-repository mapping only when the authorized task genuinely requires that scope; otherwise follow references outward only as needed to answer the routing question.
