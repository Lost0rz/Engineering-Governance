# Engineering Governance v0.7.2 — Integrated Routing Acceptance

This acceptance records the completed Local Codex routing regression used before formal `plugin-v0.7.2` publication.

## Scope

The purpose was to verify selective routing across the nine top-level Skills after Design and Sub Agent hardening, without re-running already accepted Design/Sub Agent专项 coverage.

Test fixture: disposable Local Codex repository on MacBook Air.

Observed final fixture identity:

`1e4008896a06566f25720da4e0eb69166c96a0c0`

## Results

- Project Governance default route: PASS
- Solution Design positive route: PASS
- Solution Design negative route: PASS
- Evidence Audit advisory-negative route: PASS
- Evidence Audit formal-positive route: PASS; synthetic required UNKNOWN correctly returns STOP
- Agent Handoff generation: PASS
- Domain Navigation negative route: PASS
- Domain Navigation positive route: PASS
- Incident Doctor negative route: PASS
- Incident Doctor positive route: PASS; minimum probe designed, root cause left UNKNOWN
- Project Profile smoke: PASS
- Selective composition: `SELECTIVE_CAPABILITY_ROUTING`
- unnecessary Skill invocations: none
- missed required Skill invocations: none
- route-return failures: none

Overall Local result:

`NINE_SKILL_ROUTING_ACCEPTANCE: PASS_WITH_FOLLOWUPS`

## Non-blocking follow-up

The Local runtime did not expose which of two same-version cache/source paths supplied the active Skills. Both identified Engineering Governance `0.7.2`, and no relevant routing-content divergence was found.

This does not require collapsing to one physical distribution source. The user intentionally retains both:

1. a persistent Local Git-backed installation that survives account switching;
2. an account-synced Web/remote distribution projection.

Repository source remains the semantic authority. Distribution acceptance depends on version/content equivalence, not on forcing one cache path.

## Release disposition

No Skill-source corrective was required by this acceptance. Together with the v0.7.2 source validation, Design acceptances, Web Plugin readback and Local Sub Agent runtime acceptance, this result supports formal v0.7.2 publication.
