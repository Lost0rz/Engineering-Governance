# Repo Map boundary

# Domain Map and Repo Map boundaries

- **Domain Map:** the stable semantic routing layer. It describes capability, responsibility, ownership/authority boundaries, and evidence-backed routes to project sources.
- **Repo Map:** an optional, dynamic, read-only relevance-selection aid. It may use file, symbol, or dependency relationships to rank candidate sources and help choose what to read next, especially under limited context or token budget.

A Repo Map may help select candidate files or symbols. It may not decide Domain ownership, decide business authority, authorize a task, automatically mutate `DOMAIN_MAP.md`, replace direct source reading, or become central repository truth. Verify relevant claims against the project sources themselves.

Phase C implements no Repo Map program. No executable helper, index, service, or dependency is required.
