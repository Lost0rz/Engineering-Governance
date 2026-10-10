# CURRENT TASK — Publish Engineering Governance Plugin v0.5.0

Task ID: `EG-PLUGIN-V0.5.0-RELEASE-050`

State: `AUTHORIZED_REMOTE_PUBLICATION`

Mode: `EXACT_CLEAN_BASELINE_RELEASE`

Authoritative branch: `main`

## Release source

The exact accepted clean source revision is:

`RELEASE_SOURCE = b288161c5a4b869ac9d95588c1501184229b2444`

This source is the closed result of `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`.

Its reusable payload is exact-candidate-I1 equivalent; later task-control commits do not authorize or require any `plugin.json` or `skills/**` mutation.

## Release identity

- Plugin version: `0.5.0`
- Release tag: `plugin-v0.5.0`
- Release title: `Engineering Governance Plugin v0.5.0`
- Asset: `engineering-governance-plugin.zip`
- Package root: `engineering-governance/`
- Package payload: exactly root `plugin.json` plus complete `skills/**`

Fresh preflight confirmed that neither the GitHub Release nor tag `plugin-v0.5.0` exists before publication.

## Publication contract

Use a one-shot remote publisher transport that is never merged into `main` and self-deletes after successful publication.

Package only files from exact `RELEASE_SOURCE`.

The publisher must verify before release:

1. `plugin.json` parses and version is exactly `0.5.0`;
2. package has exactly one `engineering-governance/` root;
3. root contains `plugin.json` and `skills/` only;
4. exactly three top-level Skill directories exist:
   - `project-governance`
   - `domain-navigation`
   - `incident-doctor`
5. no symlink is included;
6. no root controls, docs, examples, `.github`, build artifacts, runtime cache, or business-project material enters the package;
7. record ZIP entry count, byte size, and SHA-256;
8. create tag `plugin-v0.5.0` pointing exactly to `RELEASE_SOURCE`;
9. publish the Release and upload exactly one asset named `engineering-governance-plugin.zip`;
10. download/verify published Release metadata and asset identity/hash when the available transport supports it;
11. self-delete the one-shot publisher branch after success.

## Release notes scope

Summarize only the accepted v0.5 changes:

- verified affected-only Navigation refresh and no-churn/read-only/historical boundaries;
- lightweight non-blocking `CURRENT_STATUS.md / Follow-ups` with Task authorization required before repair;
- Project Storage Affinity derived from canonical project location with project-local override;
- Engineering-Governance repository-specific Web construction/local runtime-validation workflow rule;
- exactly three Skills and unchanged selection-only Global Router.

Do not describe a new Findings platform, storage runtime, daemon, service, installer, or fourth Skill because none exists.

## STOP conditions

STOP without destructive correction if:

- live `main` changes reusable payload after `RELEASE_SOURCE`;
- tag or Release `plugin-v0.5.0` unexpectedly appears with another identity;
- package file list differs from the authorized payload;
- version/Skill topology is wrong;
- tag cannot be proven to target exact `RELEASE_SOURCE`;
- uploaded asset hash cannot be established;
- publication would require mutating installed local Plugin/cache/runtime.

## Out of scope

- local reinstall/runtime validation;
- target/business-project mutation;
- global installed `AGENTS.md` changes;
- reusable source fixes during publication.

## Final state

Success is:

`EG_PLUGIN_V0.5.0_RELEASED_VERIFIED`

After that, local AI may reinstall the published v0.5.0 package and run actual Plugin/runtime behavior acceptance under a separate local acceptance task.
