---
name: ci-governance
description: >-
  Portable CI test routing, local affected/focused execution, catalog hygiene
  checks, starter config scaffolding, and GitHub Actions reusable workflow
  governance (ci-router.py, .github/ci-capabilities.json). Do not load for
  ordinary code fixes (engineering-workflow) or formal PR/release verdicts
  (evidence-audit).
---

# CI Governance

Route only tests warranted by actual Git diffs while keeping command execution bound to the accepted baseline.

## Fast route

| Task need | Mode | Next reading |
| --- | --- | --- |
| Select or run affected/focused checks (`plan` / `run`) | `SELECT_AND_RUN` | **NONE (this file)** |
| Audit dead globs, symlinks, or unmapped files (`check-catalog`) | `VALIDATE_CATALOG` | **NONE (this file)** |
| Onboard repo (`scaffold`), tune `stages`/`supersedes`, or wire Actions | `ONBOARD_OR_CONFIGURE` | [ci-routing.md](references/ci-routing.md) |

## Inline CLI & stage matrix (`V0`–`V3`)

`<SKILL_DIR>` means this Skill's directory; in an external project repo do not assume `skills/ci-governance` lives in `PROJECT`.

- `python3 <SKILL_DIR>/scripts/ci-router.py discover --repo-root PROJECT` — detect languages, manifests, workflows.
- `python3 <SKILL_DIR>/scripts/ci-router.py check-catalog --repo-root PROJECT --require-complete-mapping` — reject dead `paths`/`exclude_paths`/`documentation_paths`, symlinks masquerading as docs, and unmapped/release-only-blind files.
- `python3 <SKILL_DIR>/scripts/ci-router.py plan --repo-root PROJECT --worktree --config-source file --stage milestone` — dry-run test selection (auto-resolves `merge-base(origin/HEAD, HEAD)` + dirty worktree).
- `python3 <SKILL_DIR>/scripts/ci-router.py run --repo-root PROJECT --trusted-ref auto --stage milestone --keep-going` — run accepted-base commands topologically (`V1` -> `V2` -> `V3`; add `--jobs 2` for parallel waves).

| Stage | Behavior | Default tiers run |
| --- | --- | --- |
| `draft` / `none` | Defer execution (`coverage: DEFERRED`) | None |
| `focused` | Run `--focused ID` + `requires` | Selected lane only |
| `milestone` | Fast local/milestone feedback; skips heavy `V3` by default | `V1`, `V2` (or explicit `stages`) |
| `ready` | PR merge readiness; applies `supersedes` & flags unmapped/fork-blocked paths | `V1`–`V3` (excludes `release`-only) |
| `release` | Complete catalog run before release | All lanes (`V1`–`V3` + `release`) |

`import_only_alternatives` applies **only** to `source_trust=internal`; fork PRs never downgrade `fork_safe: false` gates.
