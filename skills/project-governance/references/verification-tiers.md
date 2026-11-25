# Verification: evidence follows impact

Choose tests that support the changed behavior and actual consequences. **G0–G3** describes permission/risk; **V0–V3** describes evidence depth. Neither determines the other.

| Tier | Use | Evidence |
| --- | --- | --- |
| V0 | Non-normative documentation/history/formatting | Diff, links, syntax and scope checks |
| V1 | Local behavior or isolated contracts | Focused tests, applicable lint/types |
| V2 | Shared behavior, Skill/workflow contracts or affected integration | Focused and dependent contract/integration checks |
| V3 | Trusted execution code, unknown executable dependencies, consequential security/data changes or release claims | Relevant broad security, integration or build evidence |

A file path is a routing hint, **not** a risk verdict. For a normative Markdown change start with affected contracts, and expand review/tests if the actual diff changes authorization semantics or other consequential behavior. Do not promote a whole directory to high risk merely because one rule is sensitive.

## CI selection

`EG_CI_CAPABILITIES_V1` / `EG_CI_PLAN_V1` is implemented by [ci-router.py](../scripts/ci-router.py) and configured in `.github/ci-capabilities.json`. CI evaluates the tested PR merge revision against the trusted **base**, loading both the router script and capability catalog from that accepted base rather than PR-supplied edits. The plan lists source identities, selected lanes, `unmapped_paths`, and `NOT_RUN` until executed. Untrusted, unmapped, or unverifiable selections fall back safely; skipped work is never reported as PASS.

For this repository, `archive/**` and `examples/**` descriptive files can use V0; Skill/contract/template prose uses V1 (`workflow-contracts`); packaging/manifest/reference updates add V2 (`packaging-contracts` / `router-contracts`); router scripts, workflows, policy JSON, and tests use V3 (`full-governance-suite`). The chosen tier does **not** authorize writes, packaging or merge.

**Build preview** is an independently requested `workflow_dispatch.package_preview` action using `scripts/package-plugin.py`; publishing/installing/releasing requires its own observable evidence.

## Cadence and acceptance

Run focused tests during implementation, then affected integration at a meaningful stable point. After a correction, rerun invalidated evidence; broader tests when coverage or high-consequence claims justify them. Reuse still-valid checks across proven semantic equivalence.

A green scope check only proves selected checks ran. Track untested claims and actual CI status; independent audit is appropriate at a real acceptance boundary, not after every edit.

Playwright and comparable automated browser tests are valid machine evidence. Final product-interface acceptance belongs to the human when the project requires it; machine screenshots or AI clicks cannot substitute for that decision.
