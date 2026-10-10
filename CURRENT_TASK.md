# CURRENT TASK — Publish Engineering Governance Plugin v0.5.0

Task ID: `EG-PLUGIN-V0.5.0-RELEASE-050`

State: `CLOSED / PASS`

Mode: `RELEASED_VERIFIED`

Authoritative branch: `main`

## Release source

Exact accepted clean source revision:

`b288161c5a4b869ac9d95588c1501184229b2444`

The published tag `plugin-v0.5.0` was independently re-read after publication and points exactly to that commit.

## Published Release

- Release tag: `plugin-v0.5.0`
- Release title: `Engineering Governance Plugin v0.5.0`
- Source SHA: `b288161c5a4b869ac9d95588c1501184229b2444`
- Asset: `engineering-governance-plugin.zip`
- Asset size: `56882` bytes
- Asset SHA-256: `66a1b4b4eaf3b87eaf6e1addfe793cad578ceb4c35de3c0d681d02118f3250e0`
- Package file entries: `29`
- Included Skills:
  - `project-governance`
  - `domain-navigation`
  - `incident-doctor`
- Draft: `false`
- Prerelease: `false`

## Publisher evidence

One-shot publisher:

- trigger commit: `aa7273d7812e0f0ea96a4050eff0db7cd8ff302b`
- workflow run: `38018881361`
- conclusion: `success`

All publisher gates passed:

1. release/tag absent before publication;
2. exact source checkout matched `b288161c...`;
3. `plugin.json` version = `0.5.0`;
4. exactly three Skill directories verified;
5. no symlink in authorized payload;
6. deterministic portable ZIP built from `plugin.json + skills/**` only;
7. tag created at exact source;
8. Release + single asset published;
9. published Release metadata verified;
10. asset downloaded again and SHA-256 matched the locally built artifact;
11. one-shot publisher branch self-deleted.

## Release content

v0.5.0 includes the accepted integrated features:

- affected-only Navigation refresh with no-churn, unresolved, historical, and strict-read-only boundaries;
- lightweight evidence-backed non-blocking `CURRENT_STATUS.md / Follow-ups`, with explicit `CURRENT_TASK.md` authorization required before repair;
- Project Storage Affinity based on the canonical project storage authority by default, with project-local override;
- Engineering-Governance repository-specific remote/Web construction and local installed-runtime validation split.

Global routing remains selection-only and exactly three top-level Skills remain. No fourth Skill, Findings platform, storage runtime subsystem, daemon, service, database, installer, or automatic remediation was added.

## Final state

`EG_PLUGIN_V0.5.0_RELEASED_VERIFIED`

This release task no longer authorizes remote source or publication changes.

Next step: local reinstall of the published v0.5.0 Plugin followed by real installed/runtime behavior acceptance. Local validation must not repair reusable source; any reusable defect returns to a fresh Engineering-Governance Web/remote corrective task.
