# Engineering-Governance Repository Rules

## Repository purpose

Engineering-Governance is the source repository for reusable AI engineering-governance Skills, templates, operating rules, routing/adoption contracts, and governance context. It is not a business-product repository, not a generic governance runtime, and not an installer runtime.

A target project is adapted by an AI agent after inspecting that project's real repository state. Templates in this repository define structure and required semantics; they are not copied blindly and they do not replace project-specific facts. Cross-project Skill routing may be adopted into an authoritative global `AGENTS.md` through the managed-block contract shipped under `skills/**`; that agent-mediated adoption is configuration guidance, not an installer executable or runtime service.

## Core v1 principles

1. **Three-file control plane.** Every governed project should have clear project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` roles. `AGENTS.md` holds durable operating rules, `CURRENT_STATUS.md` is the concise verified current-state snapshot, and `CURRENT_TASK.md` is the single active execution contract.
2. **Durable planning is linked, not duplicated control.** Long-lived design, large-PR planning, multi-task sequencing, rationale, and durable work-package structure may live in an accepted planning authority; `documents/**` is the default pattern when a project has no better existing authority. Planning documents are not a fourth control file, do not authorize execution, and do not own live progress. `CURRENT_TASK.md` links to the relevant planning section/work package when needed; `CURRENT_STATUS.md` summarizes only the current planning position.
3. **Domain navigation.** Every project needs an evidence-backed semantic route from the active task to the responsible domain/capability, authority, entry points, dependencies, relevant tests, and evidence before broad source reading. Discover and reuse accepted business/product/domain/capability maps already present regardless of filename. A separate navigation projection is optional and should exist only when it adds durable routing value; it must not duplicate or replace semantic truth.
4. **Business-first, Doctor-on-demand.** Normal product/business delivery is the default. Incident Doctor work is entered only after a real problem appears and existing evidence is insufficient. Add the minimum probe needed to answer the blocked question, then return to delivery.
5. **Proportional verification.** Verification depth follows change risk and scope, while verification cadence follows the construction/corrective/task/integration boundary. Documentation/control changes do not inherit the same test burden as cross-domain, persistence, concurrency, security, or release-critical changes, and repeated small edits do not each require the broadest suite.
6. **Global routing is selection, not duplicated procedure.** When Engineering Governance is adopted globally, `project-governance` is the normal engineering entry, `domain-navigation` is conditional for unclear semantic/source routes, and `incident-doctor` is reactive and evidence-gated. The global managed block must stay concise and point to Skills rather than copy their workflows.
7. **Control records are not delivery identity.** `CURRENT_STATUS.md` and `CURRENT_TASK.md` remain authoritative controls, but commits limited to those two paths advance literal Repository HEAD without changing Delivery / Semantic HEAD. They do not by themselves invalidate semantic implementation evidence or closed workspace lifecycle. They also do not bypass repository-host gates: required checks/reviews, current mergeability/conflicts, merge queue, latest-head/current-base requirements, and similar host rules remain live constraints for the literal identity the host governs. `AGENTS.md` and durable planning documents are not part of the delivery-identity exclusion; material durable-rule/plan changes remain governance-relevant.
8. **Final control alignment is mandatory; control writes are conditional.** Governed state-changing work must reread and compare current `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and any materially affected linked planning document before a final successful handoff. Update only sources whose owned semantics changed, but always report whether document/status/task were `UPDATED`, `UNCHANGED`, or not applicable. Routine external evidence does not force a write when no owned semantic changed.

## Repository layout contract

- `skills/` contains reusable Skill modules. Each module has one `SKILL.md` and only the references/assets/scripts needed by that Skill.
- `documents/` contains durable planning/design authority for this repository when work spans multiple bounded tasks or otherwise needs long-lived rationale, sequencing, constraints, and work-package structure. It is not a live task-progress log and not part of the three-file control plane.
- `references/` contains upstream research, attribution, licensing notes, and repository-wide reference material. It is not a dumping ground for project history.
- `examples/` contains only examples that have been validated against real target projects. Hypothetical examples must not be presented as proven patterns.
- `docs/superpowers/` may contain historical or tool-oriented maintainer design/implementation planning records for this repository. These files are not part of the reusable Skill payload and need not be bulk-migrated merely because new durable planning uses `documents/`.
- Root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` govern this repository itself. Template versions live under the relevant Skill assets and must not be confused with the root controls.

## Skill design rules

- Use the Agent Skills shape: `SKILL.md` plus optional `references/`, `assets/`, and `scripts/`.
- Keep `SKILL.md` focused on trigger conditions, workflow, decision rules, and what supporting material to load. Move detail into references for progressive disclosure.
- Do not create a new Skill merely because a topic exists. A Skill should represent a repeatable agent capability with a distinct trigger and output contract.
- The capability model has exactly three top-level Skills: `project-governance`, `domain-navigation`, and `incident-doctor`. Global routing policy is not a fourth Skill.
- Scripts are optional. Any initial Domain Navigation script must be read-only and justified by a demonstrated navigation need. Do not add daemons, background services, databases, enforcement systems, installer executables, Bootstrap CLIs, or automatic remediation.
- Agent-mediated adoption is allowed only as a documented, idempotent configuration procedure: inspect the authoritative global guidance, add or replace exactly one marker-bounded routing block, preserve unrelated user rules, and stop on ambiguity. Do not implement automatic global-file mutation as a Plugin runtime.

## Evidence and adaptation

- Inspect the target repository before generating or updating its governance files.
- Separate verified facts from intent. Unsupported facts remain unknown; do not fill template sections with guesses.
- Prefer concrete source paths, symbols, manifests, tests, runtime entry points, and Git evidence.
- Discover accepted semantic maps before creating navigation artifacts. Existing business/product/domain/capability maps may own project meaning and must be referenced rather than duplicated.
- Discover an accepted durable architecture/product/design planning authority before creating `documents/**`. Reuse it when it already owns long-lived planning; create a new durable planning document only when it adds real cross-task value. Keep live progress and task authorization out of the planning document.
- Any separate navigation projection follows capability/ownership/authority rather than folder names alone; it is derived routing evidence, not product/domain truth, and a literal `DOMAIN_MAP.md` filename is not required.
- A Repo Map is an optional dynamic code-navigation aid; it does not replace semantic authorities, direct source verification, or a durable navigation projection when one is justified.
- External projects are references, not hidden dependencies. Record what is borrowed conceptually and check licensing before copying code or text.
- When controls or planning links name Git revisions, distinguish provenance/transition/planning revision bases from current or explicitly locked heads. Test the declared relationship; do not convert every recorded SHA into an equality gate. For implementation freshness, distinguish literal Repository HEAD from Delivery / Semantic HEAD under `skills/project-governance/references/control-identity.md`; only `CURRENT_STATUS.md` / `CURRENT_TASK.md` are excluded by default. Keep repository-host gate identity separate from semantic implementation identity.

## Delivery workflow

- Keep one active task in `CURRENT_TASK.md`.
- When the task implements part of a durable plan, record the linked document, bounded section/work package, revision basis, and relationship to the plan. A standalone task may explicitly declare no related document.
- On a material scope change, update the root control plane before implementation. If a durable-plan change materially alters active task authorization, reconcile/re-authorize the task before further affected mutation.
- Prefer small, independently reviewable slices. Establish the repository skeleton first, then enrich one Skill module at a time.
- **Engineering-Governance repository-specific execution split:** the Web/remote session owns reusable source construction, remote GitHub mutation, integration, source audit, and release preparation for this repository. Local AI is used primarily for installed Plugin/runtime/behavior validation and must not repair reusable source during acceptance; any reusable defect found locally returns to the Web/remote Engineering-Governance flow for correction and renewed source audit. This rule is specific to this repository and does not define the execution split for other projects.
- If the verified remote baseline, active task, or authorized branch differs from the execution card, classify the difference before stopping. A `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only difference is `CONTROL_ONLY_DRIFT` and is non-blocking for delivery identity unless the changed control content alters authorization or another task-owned condition. A historical control parent or planning revision basis that is correctly related to a later authorized transition is not, by itself, current-head drift. Real delivery/governance drift or a failed explicit literal/semantic head lock remains blocking. Current repository-host gates still follow the literal identity the host governs.
- Do not expand a task into adjacent governance work merely because an improvement is visible.
- When a source-controlled project uses task branches or worktrees, classify the task-relevant non-canonical workspaces needed for the active decision; unrelated historical workspaces do not require routine full classification unless they create ambiguity, collision, unique-work risk, require lifecycle cleanup, or are explicitly in a legacy-reconciliation task. Before creating a successor writer, reconcile any predecessor that can write the same overlapping state/behavior authority; a retained predecessor that can still resume writes remains a writer until it is terminal, superseded, explicitly frozen/read-only, or otherwise unable to write without new authorization. When the project/task defines a lifecycle event as terminal, close obsolete workspace/branch state promptly or explicitly retain it with a verified reason and release condition; preserve unknown or unique local work and stop rather than force-cleaning it.
- Before a final successful **state-changing** handoff, run the Control Alignment Gate: obtain fresh outcome evidence; reread `CURRENT_STATUS.md` and `CURRENT_TASK.md`; reread the linked planning document when the outcome could affect durable design assumptions; update only sources whose owned semantics are materially stale; and report `RELATED_DOCUMENT`, `DOCUMENT_ALIGNMENT`, `CURRENT_STATUS_RECONCILIATION`, `CURRENT_TASK_RECONCILIATION`, and `CONTROL_ALIGNMENT`. Strict read-only work reports stale alignment without mutating controls.

## Verification levels and cadence

Use the lightest verification that can establish the task safely. `V0`–`V3` remains the single risk/scope dimension:

- **V0 — control/documentation/layout:** path/tree checks, content/link/frontmatter consistency, and scope verification.
- **V1 — localized behavior:** targeted tests plus relevant lint/type checks.
- **V2 — domain change:** targeted tests, the affected domain suite, and required integration tests.
- **V3 — cross-domain/high-risk/release:** broad relevant integration/build/runtime acceptance appropriate to the changed system.

Choose cadence separately. During construction use focused checks appropriate to the tier; group related acceptance findings into a bounded corrective where practical; run broader affected regression when that corrective stabilizes; and run task/merge/release closure evidence at the boundary whose claim it proves. **Verification effort follows change risk, not change count.** The active task must state the chosen level and why. Do not run a full historical test suite merely because one exists if the accepted task removes the runtime it tested. At merge/release boundaries, semantic implementation evidence and live repository-host gate state are separate claims; both must satisfy the accepted contract before a merge-ready assertion.

## Incident Doctor boundary

Incident Doctor is not a parallel product track. Enter it only when a real failure or unexplained behavior blocks safe progress and current evidence cannot answer the needed question. The sequence is: classify the problem, assess evidence sufficiency, analyze existing evidence, add the minimum probe if needed, capture a fresh incident, test/falsify hypotheses, and define the minimum evidence-supported fix boundary. That diagnosis does not itself authorize a behavior change: if the active task does not authorize the fix and required side effects, return to Project Governance for reconciliation/re-authorization before changing behavior. After an authorized fix, verify regression, then retire or explicitly promote the probe.

## Legacy preservation

Historical code, plans, and governance experiments remain recoverable through Git history and stable tags. Do not keep obsolete runtime trees in the active repository merely as an archive. If current scope retires a subsystem, remove it from the live tree after the retirement task is explicitly authorized and verified.
