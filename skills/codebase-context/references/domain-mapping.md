# Domain mapping & incremental refresh

Load when creating or incrementally updating a durable `DOMAIN_MAP.md` (or multi-repo route) under `codebase-context`. Simple source lookups run inline from [SKILL.md](../SKILL.md) without creating any map file.

## 1. Authority hierarchy (do not duplicate semantic truth)

Keep three artifacts strictly distinct:

- **Semantic authorities:** canonical business/product/API/schema/runtime specs or code that own project truth.
- **Navigation projection (`DOMAIN_MAP.md`):** an optional derived index mapping Domains -> responsibilities, canonical state owners, entry symbols, upstream/downstream links, relevant tests, and evidence freshness. Create/update only when existing docs lack reliable routing and durable navigation adds real value.
- **Dynamic Repo Map:** optional read-only relevance ranking aids; leads only, never ownership authority.

A Domain is a semantic capability/ownership boundary, not merely a directory name.

## 2. Evidence & freshness rules

- Ground every route claim in concrete paths, manifests, symbols, tests, or runtime config observed at a specific revision/time.
- Separate **Direct observation** (what code/test actually does) from **Interpretation** (inferred capability boundary).
- Mark unverified claims `unknown` and outdated claims `stale` until re-checked; never invent numeric confidence scores or infer absence from missing grep hits.

## 3. Cross-repository routing

When a task spans repositories, verify participation from explicit task/contract authority rather than folder-name similarity, and report: `OWNING_REPOSITORY`, `CONSUMER_REPOSITORY`, `UPSTREAM`, `CROSS_REPO_CONTRACT_AUTHORITY`, and `RELEVANT_SOURCE_TEST_RUNTIME_ROUTE`.

## 4. Incremental refresh policy

When authorized work verifies that a derived `DOMAIN_MAP.md` claim is stale (moved path/symbol, changed owner, updated test):

- Refresh **only** the affected Domain entry and its freshness/revision basis;
- Leave untouched entries with their existing freshness state (never mark the whole map freshly verified when only one Domain was checked);
- Under read-only tasks, report the correction candidate without mutating files.
