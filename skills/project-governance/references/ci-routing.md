# Portable CI routing

The installed `project-governance` Skill guides test selection and initial adoption. The bundled [ci-router.py](../scripts/ci-router.py) accepts any Git repository and creates a plan; an explicit local `run` or a released GitHub reusable workflow executes only selected tests. A Skill alone cannot register or control a GitHub Runner.

## First adoption without a bootstrap deadlock

1. Inspect existing workflows, product tests and Runner labels. Use `ci-router.py discover --repo-root PROJECT` as a **hint**, not an automatic command authority.
2. **Phase A:** add a minimal reviewed [ci-capabilities.json](../assets/examples/ci-capabilities.example.json) to the project's default branch while its existing CI is still operational. This file owns test commands, paths, optional `requires` dependencies, labels and relevant setup. New executable commands are not taken from a PR-supplied copy.
3. **Phase B:** after the config is accepted on the default branch, adopt the small [caller](../assets/examples/ci-caller.example.yml), and retire overlapping old heavy triggers in the same change. Keep genuine release/deployment jobs project-owned.
4. Check Ready scope, manual focused tests, true Runner labels, required-check identity and rollback. New/updated catalog commands are used by CI **only after acceptance into the trusted base**.

There is no per-Issue, writer handoff, comment or special approver requirement. Ordinary updates to the catalog use the same repository write permissions as other project files; CI syntax-checks the proposed catalog but executes **only accepted-base** commands. A config-only update is not blocked merely because the file changed.

## Local agent or desktop invocation

    python3 ci-router.py discover --repo-root PROJECT
    python3 ci-router.py plan --repo-root PROJECT --base BASE --head HEAD --config-source file --stage milestone
    python3 ci-router.py run --repo-root PROJECT --base BASE --head HEAD --config-source base --stage focused --focused TEST_ID

`plan` never starts a test. `run` explicitly executes selected commands from the accepted Git base and returns actual PASS/FAILED; `file` mode is planning only. The host must have real machine/runtime permission. Local testing may occur throughout Draft work without generating expensive GitHub Actions runs.

## Remote test cadence

- **Draft:** defer remote heavy tests; no claim of successful test coverage.
- **Focused:** run a named test, including declared prerequisites, when needed.
- **Milestone:** run affected tests at a meaningful stable point.
- **Ready PR:** accumulate affected paths from the trusted base and run matching tests plus `requires` prerequisites. Unknown source dependencies are reported; tests remain unverified until their coverage is established.
- **Release:** execute the complete accepted test catalog, including any project release suites; an incomplete catalog cannot prove complete release acceptance.

V1/V2/V3 describe evidence depth, not permission. The current highest selected tier is reported; tests declare explicit path matches and dependencies. Documentation exemptions apply only to descriptive text file types and **bounded** patterns (for example `docs/**`); `**` and ambiguous root-wide wildcard patterns are rejected.

## CI trust and host boundaries

The reusable workflow loads the approved test catalog from the target repo's **base commit** and its own router from its published `v0.10.0` release. The resulting plan includes base/head SHA, catalog digest, test IDs, real Runner labels and `NOT_RUN` until executed. A PR may propose a new catalog, but its commands are validated as data and not executed before acceptance.

The caller's workflow file itself can be changed in a PR. A centrally pinned router **cannot** stop that PR from removing or skipping the caller Job; the repository host must protect any required check/CI entrypoint through appropriate GitHub branch rules or workflow provenance. Do not claim tamper-proof required CI without such a host control. The PR-ready result and manual scoped result have different status names, avoiding confusing a manual no-test run with PR readiness. Fork PRs are not dispatched onto self-hosted Runner labels by this workflow; real project test code still requires trusted, isolated Runner hosts.

GitHub-hosted Actions execute the routing and test plan, while local/self-hosted Runners retain project runtime setup. Reusable workflow usage requires this PR to be merged and an actual published immutable `v0.10.0` tag. Web plugin installation, GitHub deployment, Mac Runner availability and project onboarding are separate observable states.
