# Semantic authority, navigation projection, and Repo Map boundaries

Keep three roles distinct:

- **Semantic authorities:** accepted business, product, domain, capability, data, or runtime sources that may own project meaning or state. Their filename is irrelevant; ownership comes from verified project evidence.
- **Navigation projection:** an optional, durable, derived routing artifact such as the generic `DOMAIN_MAP.md` template. It links an agent from a task/Domain to relevant authorities, entry points, symbols, tests, dependencies, evidence, and freshness. It does not own the semantic truth it summarizes or links.
- **Repo Map:** an optional, dynamic, read-only relevance-selection aid. It may use file, symbol, syntax, or dependency relationships to rank candidate sources and help choose what to read next, especially under limited context or token budget.

A Repo Map may help select candidate files or symbols. It may not decide Domain ownership, decide business authority, authorize a task, automatically mutate semantic authorities or a navigation projection, replace direct source reading, or become central repository truth. Verify relevant claims against the project sources themselves.

No Repo Map program or executable helper is required by this Skill. A target repository may use an existing read-only relevance aid, but it remains optional and subordinate to direct source verification.
