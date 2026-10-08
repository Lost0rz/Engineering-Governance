# Code Structure and Canonical Authority

Use this reference when an authorized task adds or changes state ownership, writers, shared behavior, or module boundaries. It guides architecture decisions within the active task; it is not a style checker, a line-count policy, or authorization for unrelated refactoring.

## One canonical authority per fact or behavior class

For each fact, state, policy, mapping, lifecycle, business rule, or behavior contract, identify one canonical authority/owner. Apply this rule at the granularity of that fact or behavior class; it does not mean that the whole application has one authority.

Before introducing a backend, owner, or writer, find the existing authority for the affected class using the repository's accepted controls, semantic maps, interfaces, implementation, and relevant tests. If an authority already exists, reuse or extend it, or explicitly replace it with a defined transition. Do not silently establish a parallel source of truth.

Multiple consumers and surfaces are compatible with one authority. CLI and UI flows, adapters, projections, caches, read models, compatibility views, and diagnostics may exist, but they must derive from or delegate to the canonical authority. Persisting, copying, or displaying the same values does not make a cache, mirror, projection, UI state, or diagnostic view an authority.

Multiple clients may request writes through the same canonical owner. Two independent writers that can define or change the same state class are an architectural risk; reconcile ownership before extending that arrangement. Do not treat separate entry points as separate authorities when they delegate to one owner.

Temporary coexistence during migration is allowed only with an explicit boundary. Record all of the following and keep them unambiguous:

- `PRIMARY_AUTHORITY`: the owner that defines the accepted truth during coexistence;
- `SYNC_DIRECTION`: which representation or owner propagates state to which, including any planned direction change at cutover;
- `CUTOVER_CONDITION`: the observable condition that authorizes changing the primary authority;
- `RETIREMENT_BOUNDARY`: when and how the superseded writer or representation stops participating.

Migration coexistence is not open-ended permission for competing truth or unspecified bidirectional writes.

## Cohesive modules and responsibility-based structure

Keep modules and files cohesive around a clear Domain, capability, responsibility, and reason to change. When considering a split, identify the responsibility or ownership boundary the new module would establish; do not split mechanically to reduce line count.

Duplication is a signal to inspect existing semantics, not automatic proof that code should be shared. Prefer an accepted canonical implementation when the behavior and invariants are the same. Similar syntax alone is not enough: create a shared abstraction only when responsibility, lifecycle, invariants, and reason to change materially align. Avoid adding duplicate business behavior, authority, backends, parsers, adapters, or helpers when an implementation with the same semantics already exists.

File length alone does not make a module defective. Do not impose universal 500-, 800-, 1000-line, or other hard thresholds. A large generated, schema, or table-oriented file with one coherent responsibility is not an automatic split candidate.

Consider a structural split when a module or file:

- combines distinct Domains, capabilities, or authorities;
- has several independent reasons to change;
- mixes UI, persistence, orchestration, and infrastructure responsibilities; or
- materially impairs navigation, focused testing, review, or safe extension.

Split along responsibility and ownership boundaries. Refactor only as far as the authorized task requires for correctness, maintainability, safe extension, or ownership clarity. Report unrelated large files or duplicate-looking code as follow-up evidence; do not expand the active task into broad cleanup by default.

## Planning and review checks

For relevant source changes, be able to answer:

1. What fact, state, or behavior class is affected, and which existing authority owns it?
2. Do new or existing consumers delegate to that owner, or are there independent writers that require ownership reconciliation?
3. If authority must coexist during migration, are `PRIMARY_AUTHORITY`, `SYNC_DIRECTION`, `CUTOVER_CONDITION`, and `RETIREMENT_BOUNDARY` explicit?
4. If behavior is shared or a module is split, do the responsibilities, lifecycle, invariants, and reasons to change support that boundary?
5. Is the proposed change needed by the active task, and is the split based on responsibility rather than file length alone?

If these answers reveal competing owners, resolve the ownership decision before adding another writer. If they reveal only unrelated size or duplication, keep the current task bounded and record a follow-up when useful.
