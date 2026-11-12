# Portable CI routing

The installed `project-governance` Skill guides test selection and initial adoption. The bundled [ci-router.py](../scripts/ci-router.py) accepts any Git repository and creates a plan; an explicit local `run` or a released GitHub reusable workflow executes only selected tests. A Skill alone cannot register or control a GitHub Runner.

## First adoption without a bootstrap deadlock

1. Inspect existing workflows, product tests and Runner labels. Use `ci-router.py discover --repo-root PROJECT` as a **hint**, not an automatic command authority.
2. **Phase A:** add a minimal reviewed [ci-capabilities.json](../assets/examples/ci-capabilities.example.json) to the project's default branch while its existing CI is still operational. This file owns test commands, paths, optional `requires` dependencies, labels and relevant setup. New executable commands are not taken from a PR-supplied copy.
3. **Phase B:** after the config is accepted on the default branch, adopt the small [caller](../assets/examples/ci-caller.example.yml), and retire overlapping old heavy triggers in the same change. Keep genuine release/deployment jobs project-owned.
4. Check Ready scope, manual focused tests, true Runner labels, required-check identity and rollback. New/updated catalog commands are used by CI **only after acceptance into the trusted base**. When adding or changing a test lane, select `test_ci_router.py` in the Engineering Governance project's existing manual focused CI (or the applicable consumer test ID after adoption) rather than running full CI merely because the catalog was edited.

There is no per-Issue, writer handoff, comment or special approver requirement. Ordinary updates to the catalog use the same repository write permissions as other project files; CI syntax-checks the proposed catalog but executes **only accepted-base** commands. A config-only update is not blocked merely because the file changed.

## Local agent or desktop invocation

    python3 ci-router.py discover --repo-root PROJECT
    HEAD_SHA=$(git -C PROJECT rev-parse HEAD)
    python3 ci-router.py plan --repo-root PROJECT --base "$HEAD_SHA" --head "$HEAD_SHA" --worktree --config-source file --stage milestone
    python3 ci-router.py run --repo-root PROJECT --base "$HEAD_SHA" --head "$HEAD_SHA" --worktree --trusted-ref refs/remotes/origin/main --stage milestone
    python3 ci-router.py run --repo-root PROJECT --base BASE --head HEAD --trusted-ref refs/remotes/origin/main --stage focused --focused TEST_ID

`plan --worktree` includes staged, unstaged and untracked changes without committing; `run` includes them automatically so its scope matches the code actually executed. Worktree comparison is rejected in GitHub-output mode. `plan` never starts tests. For local `run`, select the accepted default branch with `--trusted-ref refs/remotes/origin/<default-branch>`; the router verifies it against `origin/HEAD`. If a checkout has no `origin/HEAD`, supply `--default-branch <default-branch>` from the host's repository settings (for example, `--default-branch main`). Do not use a task branch as a trusted test-command source. The router also checks the supplied HEAD equals the current checkout. Test logs go to stderr and one JSON result goes to stdout. `file` mode is planning only; actual host execution permission is still required.

## Remote test cadence

- **Draft:** defer remote heavy tests; no claim of successful test coverage.
- **Focused:** run a named test, including declared prerequisites, when needed.
- **Milestone:** run affected tests at a meaningful stable point.
- **Ready PR:** accumulate affected paths from the trusted base and run matching tests plus `requires` prerequisites. Unknown source dependencies are reported; tests remain unverified until their coverage is established.
- **Release:** execute the complete accepted test catalog, including any project release suites; an incomplete catalog cannot prove complete release acceptance.

V1/V2/V3 describe evidence depth, not permission. The current highest selected tier is reported; `requires` co-selects related suites but does **not** serialize GitHub matrix jobs. Tests needing execution order should use one project-owned command or setup step. Documentation exemptions apply only to descriptive text file types, ordinary Git file modes and **bounded** patterns (for example `docs/**`); `**` and ambiguous root-wide wildcard patterns are rejected.

Unmapped files stay visible as `PARTIAL_UNMAPPED`. `fallback_tests` selects a smoke lane but **does not automatically pass Ready**. Only an accepted-base `fallback_satisfies_ready: true` may establish `FALLBACK_COVERED`, and even then the result is not `FULL_SUITE_PASS`. Without credible coverage the Ready check fails rather than silently skipping tests.

## CI trust and host boundaries

For manual **focused/release** runs, the accepted catalog is taken from the target repo's current default branch, independent of comparison scope. The UI defaults to **none (plan only)**; choose `focused` and give the test ID to execute one lane, or deliberately choose `release` to execute the catalog. Manual **ready/milestone** runs require an explicit `comparison_base` SHA that is an ancestor of both the default branch and tested HEAD **and is different from the tested HEAD**. The router's `--config-ref` is the separate accepted test-catalog commit, never the historical comparison SHA. An empty HEAD-to-HEAD diff cannot be used as affected-scope proof.

The reusable workflow loads the approved test catalog from the target repo's **accepted config commit** and its own router from its published `v0.10.1` release. For PRs, scope is computed from original base and head, but the **test executor runs GitHub's PR merge revision** so integration mismatches are visible. The planner checkout fetches complete history (`fetch-depth: 0`); the executor checkout fetches the PR merge revision and its immediate parent (`fetch-depth: 2`) with no retained credential. Project-owned commands can read the accepted base catalog without an unauthenticated second `git fetch`, including in private repositories. The resulting plan includes base/head SHA, catalog digest, test IDs, real Runner labels and `NOT_RUN` until executed. A PR may propose a new catalog, but its commands are validated as data and not executed before acceptance.

The caller's workflow file itself can be changed in a PR. A centrally pinned router **cannot** stop that PR from removing or skipping the caller Job; the repository host must protect any required check/CI entrypoint through appropriate GitHub branch rules or workflow provenance. Do not claim tamper-proof required CI without such a host control. The PR-ready result and manual scoped result have different status names, avoiding confusing a manual no-test run with PR readiness. Fork PRs may run only lanes explicitly marked `fork_safe: true` with a GitHub-hosted Runner label. Other lanes (and unsafe dependencies) are withheld and reported; blocked Ready evidence cannot be counted as a pass. Never attach secrets to fork-safe lanes. Actual project test code still requires isolated Runner hosts.

GitHub-hosted Actions execute the routing and test plan, while local/self-hosted Runners retain project runtime setup. Web Skill planning does not by itself provide Workflow Dispatch; an authorized GitHub API or browser workflow action is needed to start a manual remote run. Reusable workflow usage requires this PR to be merged and an actual published immutable `v0.10.1` tag. Web plugin installation, GitHub deployment, Mac Runner availability and project onboarding are separate observable states.
