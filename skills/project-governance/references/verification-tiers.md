# Verification tiers

Choose the lightest level that can safely establish the result for the change's scope and risk. Do not use a numerical risk score.

- **V0 — documentation and repository structure:** documentation, controls, layout, links, frontmatter, and path/tree consistency. Inspect the diff and verify the affected content and scope.
- **V1 — localized behavior:** behavior with a narrow blast radius and no meaningful state or integration risk. Run focused tests and directly relevant lint or type checks.
- **V2 — domain behavior and integration boundaries:** domain-level behavior, persistence or state changes, external integration within one Domain, or a meaningful integration boundary. Run focused tests, affected-Domain checks, and required integration checks.
- **V3 — broad or high-consequence behavior:** cross-Domain changes, concurrency, security, system/runtime behavior, release-critical changes, or broad user-critical paths. Run relevant broad integration, build, runtime, and acceptance checks.

Record the chosen level and a short rationale in `CURRENT_TASK.md`, along with required checks and any material checks intentionally omitted. Do not inherit a full historical suite solely because it exists. Report a check as passing only when its current output supports that claim, and state material limits or checks not run.
