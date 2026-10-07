# Domain model

A Domain is a semantic capability and responsibility boundary shaped by ownership, state, and authority. A Domain is not a folder: directory layout may suggest where to look, but cannot establish ownership on its own.

For each affected Domain, record only fields supported by evidence. A useful entry can identify:

- responsibility and what the Domain does not own;
- state and authority owners by relevant fact class;
- primary entry points and important symbols;
- upstream dependencies and downstream consumers;
- relevant tests and the behavior or boundary each test covers;
- data/control flow when it helps route the task;
- runtime or operational entry points when applicable;
- invariants and their accepted sources;
- evidence paths and a freshness basis;
- known unknowns, stale claims, or unresolved conflicts.

Before creating a navigation projection, discover accepted business, product, domain, or capability maps already present in the target repository, regardless of filename. Such documents may own semantic truth that this Skill must reference rather than restate. Their existence does not make them navigation artifacts, and a navigation artifact must not compete with them.

`DOMAIN_MAP.md` is a generic template name for an optional navigation projection: it helps an agent locate and verify project sources when a separate durable routing layer adds value. A target repository is not required to create a file with that exact name. If existing authoritative maps plus bounded source/symbol/test pointers already provide sufficient routing, keep using those authorities and do not create duplicate semantic content merely to satisfy the template. When a separate navigation projection is useful, link back to semantic authorities and keep only navigation-specific ownership, source, symbol, test, evidence, and freshness pointers.

A navigation projection is not a product authority, domain-truth authority, data authority, or runtime authority, and it does not replace the sources it links to. Keep entries concise. Create a detailed `DOMAIN.md` only when the Domain's complexity or navigation needs justify the extra detail.
