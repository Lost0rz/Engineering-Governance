# Portable CI routing

The `ci-governance` Skill guides test selection and onboarding. The bundled [ci-router.py](../scripts/ci-router.py) accepts any Git repository to discover manifests, scaffold a starter catalog, validate path hygiene, plan affected lanes, or execute local accepted-base tests.

## First adoption without a bootstrap deadlock

1. **Discover & scaffold:** inspect existing workflows and test commands, then run:
   - `python3 skills/ci-governance/scripts/ci-router.py discover --repo-root PROJECT`
   - `python3 skills/ci-governance/scripts/ci-router.py scaffold --repo-root PROJECT > .github/ci-capabilities.json` (review and customize every generated command and Runner label before committing).
2. **Phase A (Catalog on default branch):** commit reviewed `.github/ci-capabilities.json` (see [example](../assets/examples/ci-capabilities.example.json)) and validate it with `ci-router.py check-catalog --repo-root PROJECT --require-complete-mapping` so zero dead globs, unmapped source files, or doc-masquerading symlinks exist.
3. **Phase B (Caller workflow):** adopt [ci-caller.example.yml](../assets/examples/ci-caller.example.yml), which pins the released workflow tag (`@v0.10.3`) and enables PR `concurrency` cancellation so redundant pushes never queue stale self-hosted runs. Retire overlapping heavy CI triggers in the same change.
4. **Trust rule:** PRs may edit `.github/ci-capabilities.json` and have the new JSON validated as data, but CI executes **only commands from the accepted baseline**. Note that edits to `tests/**` or `.github/**` inside a PR still run on the PR code tree, so enforce human / `CODEOWNERS` review on test and workflow edits.

## Local agent and developer invocation

    python3 ci-router.py discover --repo-root PROJECT
    python3 ci-router.py scaffold --repo-root PROJECT
    python3 ci-router.py check-catalog --repo-root PROJECT --require-complete-mapping
    HEAD_SHA=$(git -C PROJECT rev-parse HEAD)
    python3 ci-router.py plan --repo-root PROJECT --base "$HEAD_SHA" --head "$HEAD_SHA" --worktree --config-source file --stage milestone
    python3 ci-router.py run --repo-root PROJECT --base "$HEAD_SHA" --head "$HEAD_SHA" --worktree --trusted-ref refs/remotes/origin/main --stage milestone --keep-going

- `--worktree` diffs working-tree changes directly against `merge-base(base, head)` plus untracked files, eliminating false positives when edits are reverted before running.
- Local `run` executes lanes in topological order (`requires` prerequisites and lighter tiers `V1 -> V2 -> V3` first), records `duration_ms` per lane, and supports `--keep-going` to continue independent lanes while marking dependent lanes `DEPENDENCY_FAILED`.
- For local `run`, `--trusted-ref refs/remotes/origin/<default-branch>` is verified against `origin/HEAD` (or `--default-branch` when `origin/HEAD` is unset); task branches are never trusted command sources.

## Stage tiering, `supersedes`, and catalog schema

Each entry in `tests` supports:

- `id`, `tier` (`V1` | `V2` | `V3`), `paths`, `runner`, `command`, optional `setup`, `cwd`, `timeout_minutes`, `fork_safe`, `requires`.
- **`stages` (optional):** subset of `["milestone", "ready", "release"]`. When omitted, `V1`/`V2` lanes default to `["milestone", "ready", "release"]`, while heavy `V3` lanes default to `["ready", "release"]` so `milestone` stays fast. Files covered only by `release`-only lanes still flag `PARTIAL_UNMAPPED` on `ready` if no `ready` lane covers them.
- **`supersedes` (optional):** lower-or-equal tier test IDs fully covered by this broader lane (for example, a full `unittest` suite superseding single-file suites). When the superset lane runs in `milestone`/`ready`/`release`, redundant subset lanes not required by other remaining lanes are dropped and recorded in `superseded_test_ids`.
- **`exclude_paths` / `include_docs`:** `documentation_paths` exemptions (`archive/**`, `docs/**`, etc.) are evaluated **before** module wildcards (`apps/web/**`) for regular descriptive text files unless a lane explicitly sets `"include_docs": true`. Paths excluded by `exclude_paths` and covered by no other lane fail closed as `unmapped_paths`.

## Optional Python `import_only_alternatives` & specialist evidence

- A trusted `V2`/`V3` lane may declare `"import_only_alternatives": ["import-contracts"]` backed by real import/contract tests. When an in-place Python edit changes only top-level import targets while preserving bindings and remaining AST, `ready`/`milestone` plans substitute the lighter lane.
- **Security invariant:** `import_only_alternatives` only applies when `source_trust == "internal"`. External **fork PRs** never substitute away `fork_safe: false` lanes (`fork_blocked_tests` and `review_required: true` remain enforced).
- For separate Browser or cross-repo workflows, `ci-router.py import-only --repo-root PROJECT --base BASE_SHA --head HEAD_SHA` outputs read-only `changed_paths` and `import_only_paths` without loading or running commands.

## Reusable GitHub Actions trust boundaries

- The reusable workflow in `v0.10.3` (`.github/workflows/ci-router-reusable.yml`) inspects `${{ github.workflow_ref }}` to resolve its own pinned immutable tag (`vX.Y.Z`) or 40-char commit SHA—never checking out a mutable branch or hardcoding a mismatched version tag.
- On `pull_request`, the router verifies `HEAD^2 == github.event.pull_request.head.sha`, binds `BASE_SHA` and `CONFIG_REF` to the tested merge commit's parent 1 (`HEAD^1`), and runs selected tests on the merged revision (`${{ github.sha }}`) with `persist-credentials: false`.
- Optional `control_runner` JSON labels move `route` and `result` control jobs onto a self-hosted runner for internal PRs while forcing `ubuntu-latest` for fork PRs. Fork PRs may execute only `fork_safe: true` lanes on GitHub-hosted runner labels and fail closed if any non-fork-safe lane is needed.
- Protect required check entrypoints (such as `EG Ready verification`) via GitHub branch protection rules, because a PR can propose edits to its own caller workflow.
