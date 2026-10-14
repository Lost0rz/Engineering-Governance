---
name: evidence-audit
description: Use when the requested outcome is a read-only evidence, acceptance, or readiness verdict for implementation/code/PR/CI/release/post-change state, separate from corrective implementation. Do not use merely because code, PR, CI, or release is mentioned while the requested outcome is fixing or continuing work.
---

# Evidence Audit

Use for an explicit evidence/acceptance/readiness boundary. It evaluates evidence; it does not authorize corrective mutation. Read `references/audit-contract.md` for profile-specific evidence rules.

Calling this Skill from an implementation context does not make the result independent. When independence matters, report the actual basis: `SELF_CHECK`, `FRESH_CONTEXT`, `SEPARATE_AGENT`, or `HUMAN`.

## Profiles

- `CODE_DIFF`
- `PR_MERGE`
- `CI`
- `RELEASE_PROVENANCE`
- `POST_CHANGE`

## Before verdict

Bind target/range/identity, requirement/design authority, evidence freshness, live host identity when relevant, and the claims that must be established:

```text
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

A required unsupported claim remains `UNKNOWN`.

## Findings and verdict

- `BLOCKING` -> `STOP`.
- `IMPORTANT` -> `STOP` when required before the requested boundary; follow-up only when responsible authority explicitly accepts deferral.
- `MINOR` -> may allow `PASS_WITH_FOLLOWUPS`.
- required `UNKNOWN` -> `STOP`.

Verdict: `PASS | PASS_WITH_FOLLOWUPS | STOP`.

Do not transfer PASS between identities without accepted equivalence/provenance. Reviewer suggestions are evidence to verify, not mutation instructions.
