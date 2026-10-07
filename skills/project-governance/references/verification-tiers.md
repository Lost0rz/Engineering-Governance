# Verification tiers

Choose the lightest verification level that establishes safety for the change's risk and radius. Record both the level and its rationale in `CURRENT_TASK.md`.

- **V0 — documentation, controls, and layout:** inspect the diff and verify required paths, links, structure, and scope.
- **V1 — localized behavior:** run focused tests and directly relevant lint or type checks.
- **V2 — domain-level change:** run focused tests, the affected domain checks, and required integration checks.
- **V3 — cross-domain, high-risk, or release-critical change:** run the relevant broad integration, build, runtime, and acceptance checks.

Do not inherit a larger test burden solely because a historical suite exists. Do not report a check as passing unless its current output supports that claim; state material limits and checks not run.
