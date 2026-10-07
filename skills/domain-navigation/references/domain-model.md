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

`DOMAIN_MAP.md` is a navigation projection: it helps an agent locate and verify project sources. It is not a product authority, domain-truth authority, data authority, or runtime authority, and it does not replace the sources it links to. Keep entries concise. Create a detailed `DOMAIN.md` only when the Domain's complexity or navigation needs justify the extra detail.
