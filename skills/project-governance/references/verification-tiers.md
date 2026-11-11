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

`VERIFICATION_PLAN_V1` is implemented by `scripts/verification-plan.py`. CI obtains the complete base/head diff, including rename origins, and runs the selector from the trusted **base**, not PR-supplied policy. The plan lists the source identities, selected/skipped suites, reasons and `TESTS_PENDING`. Untrusted or unverifiable selection receives conservative testing; skipped work is reported as skipped, never PASS.

For this repository, descriptive history can use V0; README/notes use V1; active Skill/contract Markdown uses affected V2 suites; trusted executable policy, CI/selector and unknown executable owners use V3. The chosen tier does **not** authorize writes, packaging or merge.

**Build preview** is an independently requested `workflow_dispatch.package_preview` action; publishing/installing/releasing requires its own observable evidence.

## Cadence and acceptance

Run focused tests during implementation, then affected integration at a meaningful stable point. After a correction, rerun invalidated evidence; broader tests when coverage or high-consequence claims justify them. Reuse still-valid checks across proven semantic equivalence.

A green scope check only proves selected checks ran. Track untested claims and actual CI status; independent audit is appropriate at a real acceptance boundary, not after every edit.

Playwright and comparable automated browser tests are valid machine evidence. Final product-interface acceptance belongs to the human when the project requires it; machine screenshots or AI clicks cannot substitute for that decision.
