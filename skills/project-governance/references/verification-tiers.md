# Verification tiers, cadence, evidence identity, and independent audit

Choose the lightest verification that safely establishes the requested result. **Verification effort follows change risk, not change count.** `V0`–`V3` is the single risk/scope dimension; cadence is separate.

## Evidence identity

When identity matters, name what a result observed: literal Repository HEAD, Delivery / Semantic HEAD, PR head/merge ref, merge commit/tree, build/package artifact, installed package/app, deployed revision, runtime/process or release artifact.

Evidence proves the identity it actually observed. Matching names or historical proximity do not transfer PASS to another identity without accepted semantic equivalence/provenance.

Use `control-identity.md` when repository revisions differ. Semantic test/CI/review/audit evidence may be reused across proven `CONTROL_ONLY_DRIFT` when `SEMANTIC_TREE_EQUIVALENCE = PASS`, no implementation-relevant authority changed and no task condition invalidates the evidence.

## Repository-host gates are separate

Required status checks, required reviews, conflicts/mergeability, merge queue, branch rules, latest-head/current-base requirements and similar host conditions are live facts for the literal identity the repository host governs.

Semantic equivalence does not make a current host gate pass. Re-read applicable host gates at the merge/release decision.

## Risk/scope tiers

- **V0 — documentation/control/layout:** diff/content/link/frontmatter/tree/scope consistency.
- **V1 — localized behavior:** focused tests plus directly relevant lint/type/runtime checks.
- **V2 — domain/integration boundary:** focused tests, affected-domain evidence and required integration checks.
- **V3 — broad/high-consequence/release:** broad relevant integration/build/runtime/security/concurrency/release evidence appropriate to the claim.

The tier describes what risk must be covered, not how often every check runs.

## Verification cadence

### Construction

Use the narrowest checks that catch defects introduced by current edits while remaining appropriate to the tier. Do not run unrelated broad suites after every small change.

For an explicitly authorized multi-part architecture/framework task, construction may use bounded static/sanity checks while deferring expensive **integrated installed/runtime acceptance** until the full architecture is frozen. This cadence is valid only when the task explicitly defines the later integrated acceptance boundary. It does not waive final evidence.

### Corrective close

Group related findings sharing one objective/authority into one bounded corrective where practical. After it stabilizes, run broader **affected** regression justified by risk once rather than repeating unrelated full validation per edit.

### Task close

Run every check required by the task's accepted verification contract and risk tier that was intentionally deferred during construction. State material checks still omitted and why.

### Merge/release boundary

Add exact-head/provenance, broad build/integration/runtime/packaging/remote CI evidence only as required by the integration/release claim. Do not inherit every historical suite automatically.

## Implementation verification vs independent audit

Keep task purpose and evidence role distinct:

- implementation/self-check establishes behavior evidence required by the active execution/corrective task;
- calling `evidence-audit` from the same implementation context does not automatically create independence;
- when formal independent acceptance/readiness is a distinct engineering boundary, Project Governance authorizes the appropriate AUDIT/VERIFY task purpose and its required independence level;
- not every V0/V1 change needs an independent audit;
- V2 often benefits from independent audit at the integrated task/PR boundary rather than after every unit;
- V3 requires explicit independent evidence/review appropriate to the high-consequence boundary.

When independence matters, report one of:

```text
AUDIT_INDEPENDENCE: SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN
```

`SELF_CHECK` is useful verification but is not independent acceptance.

Evidence Audit profiles include `CODE_DIFF`, `PR_MERGE`, `CI`, `RELEASE_PROVENANCE`, and `POST_CHANGE`. A PASS for one profile does not automatically prove another.

## Required-claim coverage

For a material audit/acceptance boundary, identify the claims that must be established before verdict:

```text
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

A required claim without adequate evidence remains `UNKNOWN` and cannot be silently omitted from the verdict.

## Final implementation freeze

When exact-head semantic evidence is required:

1. finish intended implementation-relevant source/rule/design edits;
2. designate the Delivery / Semantic HEAD/tree (or explicit literal Repository HEAD lock when required) as the frozen candidate;
3. run required semantic verification and independent audit on that candidate;
4. allow later `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only control reconciliation without rerunning semantic checks when equivalence/task conditions permit;
5. re-read current repository-host gates for the literal identity at merge/release.

Any mixed control+implementation commit, material `AGENTS.md` rule change, durable planning/design change, source/config/test/workflow/schema/migration/dependency/runtime change is a new delivery/governance change and must be assessed for fresh evidence.

Do not create final `CI PASS`, `audit PASS` or `ready to merge` control commits solely to memorialize external evidence.

## Human/integrated acceptance loop

A healthy loop is:

```text
complete bounded architecture/implementation
-> focused construction evidence
-> freeze semantic candidate when ready
-> required integrated verification
-> independent audit/acceptance task where required
-> read current host gates
-> bounded corrective task if findings create a distinct objective
-> rerun affected integrated scenarios/evidence
-> merge/release only when semantic evidence + live host gates satisfy the boundary
```

For multi-Skill architecture work, prefer testing composition and positive/negative routing behavior on the frozen architecture rather than proving only that each Skill file loads independently.

## Recording the decision

`CURRENT_TASK.md` records the chosen V0–V3 tier, short rationale, required checks and material cadence/deferred evidence. Report semantic checks as passing only from evidence for the relevant identity, and host gates as passing only from current host evidence. `no status` or missing evidence is `UNKNOWN`/none, not `PASS`.
