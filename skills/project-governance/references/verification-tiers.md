# Verification tiers and cadence

Choose the lightest verification that can safely establish the result for the change's scope and risk. **Verification effort follows change risk, not change count.** Do not use a numerical risk score and do not introduce a second competing risk taxonomy.

## Bind evidence to the identity it observes

When identity matters to a claim, name the relevant identity: literal Repository HEAD, Delivery / Semantic HEAD, PR head, merge commit or tree, build/package artifact, installed application/package, running runtime/process, deployed revision, or release artifact. Evidence proves the identity it actually observed; history or matching names alone do not transfer a result to another identity. For example, CI on implementation X does not prove a later implementation Y unless relevant semantic tree/content equivalence or sufficient provenance is established. Acceptance of installed build B applies to B; it applies to source A only when provenance or equivalence linking B to A is established.

Use [Control identity and freshness](control-identity.md) when repository revisions differ. A later Repository HEAD that differs only in `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` is `CONTROL_ONLY_DRIFT`: reuse implementation evidence when `SEMANTIC_TREE_EQUIVALENCE = PASS`, no implementation-relevant authority changed, and no task-owned requirement invalidates the tested implementation. Do not require CI, review, or audit to rerun solely because those two control records changed.

Reuse evidence without rerunning a check when the relevant equivalence is proven, such as semantic tree/content identity, an immutable artifact hash, or a sufficient provenance chain for the decision. Keep automated verification, human acceptance, and runtime/incident observation distinct and state what each proves; a task may require one or more of these evidence classes, not all of them. Apply identity checks in proportion to the claim and affected system rather than imposing build/runtime evidence on documentation-only or low-risk work.

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

#### Final PR-head freeze

When exact-head CI, independent audit, review, or another merge-gate check must bind to the final implementation, finish all intended implementation-relevant source/rule edits first, then designate the current **Delivery / Semantic HEAD** or equivalent semantic tree as the frozen implementation candidate. If the active task explicitly requires literal Repository HEAD equality, honor that stronger lock instead.

After the implementation candidate is frozen:

- CI, review, independent audit, mergeability, and repository-host checks are live external evidence for the implementation identity they actually observed.
- A later `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only commit may advance literal Repository HEAD while leaving Delivery / Semantic HEAD unchanged. When `SEMANTIC_TREE_EQUIVALENCE = PASS` and no task-owned condition invalidates the evidence, keep the existing CI/review/audit/merge-readiness evidence valid; do not restart the exact-head cycle merely because the control records moved.
- Do **not** create a status/task/handoff commit solely to record that external checks passed, failed, started, completed, or changed state. Such a write is unnecessary governance churn even though a control-only commit no longer changes delivery identity.
- Any source/config/test/workflow/schema/migration/dependency/runtime-relevant change, material `AGENTS.md` rule change, or mixed control+implementation change is `DELIVERY_HEAD_CHANGE`. If it affects the frozen implementation, obtain fresh evidence as required by the accepted verification contract.
- If external evidence reveals an actual implementation/control defect or materially changes scope, authorization, acceptance, or a stop condition, reconcile the task as required. A material task-content change remains authoritative even though its commit is excluded from delivery identity.
- If the frozen implementation passes its gates, merge the already verified implementation. Do not add a final “audit passed”, “CI passed”, “ready to merge”, or similar control commit as a prerequisite for merge.
- Post-merge CI may verify the merge commit or delivered tree. Treat that result as live evidence for the identity it observed; do not create another commit solely to write the post-merge result back into controls.

A control may state the durable rule or point to the external evidence authority, for example “the final Delivery / Semantic HEAD must have required CI success.” Transient run numbers and pass/fail observations may be reported in the audit/closure response without becoming a new commit unless the project has a separate, non-self-invalidating release record that explicitly owns those facts.

## Human acceptance loops

A normal low-risk acceptance loop should look like:

```text
related findings
-> one bounded corrective
-> focused verification after each material edit
-> targeted user/browser/runtime acceptance as needed
-> broader affected regression once the corrective stabilizes
-> freeze final Delivery / Semantic HEAD when exact implementation evidence is required
-> CI / independent audit on that implementation identity
-> merge the already verified implementation
-> post-merge verification as required, without evidence-only control churn
```

If an edit raises the actual risk tier—for example a visual fix becomes an API, persistence, security, lifecycle, or cross-Domain change—upgrade the tier immediately and add the checks that higher risk requires. If the higher risk also changes business scope or authorization, stop and reconcile the task before continuing.

## Recording the decision

Record the chosen `V0`–`V3` tier and a short rationale in `CURRENT_TASK.md`, plus any material cadence expectations such as checks deferred to corrective close, task close, or merge/release. Do not inherit a full historical suite solely because it exists. Report a check as passing only when current evidence supports that claim, and state material limits or checks not run. Once the final implementation identity is frozen for exact-head verification, report later CI/review/audit outcomes from live evidence rather than mutating controls merely to record those outcomes.
