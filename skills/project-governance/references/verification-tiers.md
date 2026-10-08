# Verification tiers

Choose the lightest level that can safely establish the result for the change's scope and risk. Do not use a numerical risk score.

## Bind evidence to the identity it observes

When identity matters to a claim, name the relevant identity: source/commit HEAD, PR HEAD, merge commit or tree, build/package artifact, installed application/package, running runtime/process, deployed revision, or release artifact. Evidence proves the identity it actually observed; history or matching names alone do not transfer a result to another identity. For example, CI on PR HEAD X does not prove exact merge commit Y was tested unless relevant tree/content equivalence or sufficient provenance is established. Acceptance of installed build B applies to B; it applies to source A only when provenance or equivalence linking B to A is established.

Reuse evidence without rerunning a check when the relevant equivalence is proven, such as exact tree/content identity, an immutable artifact hash, or a sufficient provenance chain for the decision. Keep automated verification, human acceptance, and runtime/incident observation distinct and state what each proves; a task may require one or more of these evidence classes, not all of them. Apply identity checks in proportion to the claim and affected system rather than imposing build/runtime evidence on documentation-only or low-risk work.

- **V0 — documentation and repository structure:** documentation, controls, layout, links, frontmatter, and path/tree consistency. Inspect the diff and verify the affected content and scope.
- **V1 — localized behavior:** behavior with a narrow blast radius and no meaningful state or integration risk. Run focused tests and directly relevant lint or type checks.
- **V2 — domain behavior and integration boundaries:** domain-level behavior, persistence or state changes, external integration within one Domain, or a meaningful integration boundary. Run focused tests, affected-Domain checks, and required integration checks.
- **V3 — broad or high-consequence behavior:** cross-Domain changes, concurrency, security, system/runtime behavior, release-critical changes, or broad user-critical paths. Run relevant broad integration, build, runtime, and acceptance checks.

Record the chosen level and a short rationale in `CURRENT_TASK.md`, along with required checks and any material checks intentionally omitted. Do not inherit a full historical suite solely because it exists. Report a check as passing only when its current output supports that claim, and state material limits or checks not run.
