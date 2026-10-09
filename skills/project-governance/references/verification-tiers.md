# Verification tiers and cadence

Choose the lightest verification that can safely establish the result for the change's scope and risk. **Verification effort follows change risk, not change count.** Do not use a numerical risk score and do not introduce a second competing risk taxonomy.

## Bind evidence to the identity it observes

When identity matters to a claim, name the relevant identity: source/commit HEAD, PR HEAD, merge commit or tree, build/package artifact, installed application/package, running runtime/process, deployed revision, or release artifact. Evidence proves the identity it actually observed; history or matching names alone do not transfer a result to another identity. For example, CI on PR HEAD X does not prove exact merge commit Y was tested unless relevant tree/content equivalence or sufficient provenance is established. Acceptance of installed build B applies to B; it applies to source A only when provenance or equivalence linking B to A is established.

Reuse evidence without rerunning a check when the relevant equivalence is proven, such as exact tree/content identity, an immutable artifact hash, or a sufficient provenance chain for the decision. Keep automated verification, human acceptance, and runtime/incident observation distinct and state what each proves; a task may require one or more of these evidence classes, not all of them. Apply identity checks in proportion to the claim and affected system rather than imposing build/runtime evidence on documentation-only or low-risk work.

## Risk/scope tiers

- **V0 — documentation and repository structure:** documentation, controls, layout, links, frontmatter, and path/tree consistency. Inspect the diff and verify the affected content and scope.
- **V1 — localized behavior:** behavior with a narrow blast radius and no meaningful state or integration risk. Run focused tests and directly relevant lint or type checks.
- **V2 — domain behavior and integration boundaries:** domain-level behavior, persistence or state changes, external integration within one Domain, or a meaningful integration boundary. Run focused tests, affected-Domain checks, and required integration checks.
- **V3 — broad or high-consequence behavior:** cross-Domain changes, concurrency, security, system/runtime behavior, release-critical changes, or broad user-critical paths. Run relevant broad integration, build, runtime, and acceptance checks.

The tier describes **what risk must be covered**. It does not say that every check must be rerun after every small edit.

## Verification cadence

Select cadence separately from `V0`–`V3`:

### Construction

During implementation or an active human-acceptance correction loop, run the narrowest checks that can catch defects introduced by the current edit while still satisfying the current risk tier. Prefer focused tests, targeted type/lint checks, targeted browser/runtime acceptance, content/link checks, or other directly affected evidence.

Do not run unrelated full repository suites, builds, or remote CI after every CSS, copy, layout, button-position, or similarly bounded edit merely because a broader suite exists.

### Corrective close

When several related findings from one acceptance cycle share one objective and authority, group them into one bounded corrective where practical. After that corrective stabilizes, run the broader **affected** regression justified by its risk tier once. If the corrective spans only frontend presentation/interaction, that does not automatically justify an unrelated backend-wide suite.

### Task close

Before declaring the task complete or handing it off as complete, run every check required by the task's accepted verification contract and risk tier, including broader checks intentionally deferred during construction. Record material checks that remain intentionally omitted and why.

### Merge/release boundary

When integration or release consequences require it, add exact-head/provenance checks and the broad build, integration, runtime, packaging, browser, or remote CI evidence appropriate to the affected system. A merge/release boundary does not automatically require every historical suite in the repository; it requires enough evidence for the integration/release claim actually being made.

## Human acceptance loops

A normal low-risk acceptance loop should look like:

```text
related findings
-> one bounded corrective
-> focused verification after each material edit
-> targeted user/browser/runtime acceptance as needed
-> broader affected regression once the corrective stabilizes
-> task/merge closure verification at the justified boundary
```

If an edit raises the actual risk tier—for example a visual fix becomes an API, persistence, security, lifecycle, or cross-Domain change—upgrade the tier immediately and add the checks that higher risk requires. If the higher risk also changes business scope or authorization, stop and reconcile the task before continuing.

## Recording the decision

Record the chosen `V0`–`V3` tier and a short rationale in `CURRENT_TASK.md`, plus any material cadence expectations such as checks deferred to corrective close, task close, or merge/release. Do not inherit a full historical suite solely because it exists. Report a check as passing only when current evidence supports that claim, and state material limits or checks not run.
