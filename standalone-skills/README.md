# Standalone Skills

Skills in this directory are **independent source packages**, hosted in the Engineering-Governance repository for convenience only.

They are not part of the Engineering Governance plugin. In particular, do not move them into the root `skills/` or `references/` trees: the existing Web preview builder collects those trees for the Governance plugin.

- [Wiki Knowledge Builder](wiki-knowledge-builder/README.md): evidence-aware, value-first knowledge-note production for subsequent LLM Wiki ingestion.

Each standalone package owns its instructions, references, examples and acceptance cases. Installing or publishing the Governance plugin does not install or enable these packages. Any standalone installation must be separately selected by the user and supported by the target host.

## Multi-package source testing

The standalone CI runner discovers every package directory under `standalone-skills/` that has a `SKILL.md`; any new package without `tests/test_*.py` cases **fails closed** rather than reporting green. A discovered suite must execute at least one unskipped test; zero discovered or all-skipped cases are explicitly BLOCKED. Per-package optional `tests/requirements.txt` installs test dependencies only during verification, not during Agent installation.

## Independent verification boundary

This directory is temporary source staging only. The previous standalone GitHub
Actions workflow was removed when all Engineering Governance files were restored
to their original baseline. **No active CI workflow validates the latest PR HEAD.**

The repo-only tests no longer reference the Governance plugin, its preview
builder, or a host-specific CI workflow. Use `standalone-skills/tests/` as the
independent test harness until it moves into a dedicated Wiki Knowledge Builder
repository with its own CI. Do not merge this staging PR into Governance.

## Deterministic standalone package preflight (no release)

`standalone-skills/tests/build_wiki_packages.py` creates two **distinct** ZIP formats
under an **explicit output directory**, only from files whose actual bytes match Git HEAD:

- `wiki-knowledge-builder-agent-skill-v0.2.0-<sha>.zip` with `wiki-knowledge-builder/SKILL.md`.
- `wiki-knowledge-builder-chatgpt-private-v0.2.0-<sha>.zip` with independent
  `plugin.json`, `.codex-plugin/plugin.json` and `skills/wiki-knowledge-builder/SKILL.md`.

The preflight verifies ZIP CRCs, exact paths and bytes, version and Git source SHA.
An independent CI runner can invoke this through isolated temporary-directory tests;
it never uploads, publishes, installs, or updates the private ChatGPT plugin.
Neither archive contains Engineering Governance's root `skills/` tree.

The package builder supports a repository-root `SKILL.md`, a `wiki-knowledge-builder/` source subdirectory, and this temporary `standalone-skills/wiki-knowledge-builder/` layout. It does not read or require Engineering Governance manifests, code, test policies, or workflows. Its ZIP payload is allowlisted and verified against pinned Git blob hashes.
