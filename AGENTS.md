# Engineering-Governance Repository Rules

## Repository purpose

Engineering-Governance is the source repository for reusable AI engineering-governance Skills, templates, operating rules, and governance context. It is not a business-product repository, not a generic governance runtime, and not an installer.

A target project is adapted by an AI agent after inspecting that project's real repository state. Templates in this repository define structure and required semantics; they are not copied blindly and they do not replace project-specific facts.

## Core v1 principles

1. **Three-file control plane.** Every governed project should have clear project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` roles. `AGENTS.md` holds durable operating rules, `CURRENT_STATUS.md` is the concise verified current-state snapshot, and `CURRENT_TASK.md` is the single active execution contract.
2. **Domain navigation.** Every project needs an evidence-backed semantic route from the active task to the responsible domain/capability, authority, entry points, dependencies, relevant tests, and evidence before broad source reading. Discover and reuse accepted business/product/domain/capability maps already present regardless of filename. A separate navigation projection is optional and should exist only when it adds durable routing value; it must not duplicate or replace semantic truth.
3. **Business-first, Doctor-on-demand.** Normal product/business delivery is the default. Incident Doctor work is entered only after a real problem appears and existing evidence is insufficient. Add the minimum probe needed to answer the blocked question, then return to delivery.
4. **Proportional verification.** Verification depth follows change risk and scope. Documentation/control changes do not inherit the same test burden as cross-domain, persistence, concurrency, security, or release-critical changes.

## Repository layout contract

- `skills/` contains reusable Skill modules. Each module has one `SKILL.md` and only the references/assets/scripts needed by that Skill.
- `references/` contains upstream research, attribution, licensing notes, and repository-wide reference material. It is not a dumping ground for project history.
- `examples/` contains only examples that have been validated against real target projects. Hypothetical examples must not be presented as proven patterns.
- `docs/superpowers/` may contain temporary maintainer design/implementation planning records for this repository. These files are not part of the reusable Skill payload.
- Root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` govern this repository itself. Template versions live under the relevant Skill assets and must not be confused with the root controls.

## Skill design rules

- Use the Agent Skills shape: `SKILL.md` plus optional `references/`, `assets/`, and `scripts/`.
- Keep `SKILL.md` focused on trigger conditions, workflow, decision rules, and what supporting material to load. Move detail into references for progressive disclosure.
- Do not create a new Skill merely because a topic exists. A Skill should represent a repeatable agent capability with a distinct trigger and output contract.
- v1 has three top-level capabilities: `project-governance`, `domain-navigation`, and `incident-doctor`.
- Scripts are optional. Any initial Domain Navigation script must be read-only and justified by a demonstrated navigation need. Do not add daemons, background services, databases, enforcement systems, or automatic remediation.
- Do not build an installer or Bootstrap CLI. Adoption is performed by an AI agent that reads these Skills and adapts the templates to the target project.

## Evidence and adaptation

- Inspect the target repository before generating or updating its governance files.
- Separate verified facts from intent. Unsupported facts remain unknown; do not fill template sections with guesses.
- Prefer concrete source paths, symbols, manifests, tests, runtime entry points, and Git evidence.
- Discover accepted semantic maps before creating navigation artifacts. Existing business/product/domain/capability maps may own project meaning and must be referenced rather than duplicated.
- Any separate navigation projection follows capability/ownership/authority rather than folder names alone; it is derived routing evidence, not product/domain truth, and a literal `DOMAIN_MAP.md` filename is not required.
- A Repo Map is an optional dynamic code-navigation aid; it does not replace semantic authorities, direct source verification, or a durable navigation projection when one is justified.
- External projects are references, not hidden dependencies. Record what is borrowed conceptually and check licensing before copying code or text.

## Delivery workflow

- Keep one active task in `CURRENT_TASK.md`.
- On a material scope change, update the root control plane before local implementation.
- Prefer small, independently reviewable slices. Establish the repository skeleton first, then enrich one Skill module at a time.
- The Web/remote planning side defines and audits the accepted task contract. Local AI execution follows that contract and returns evidence for independent review.
- If the verified remote baseline, active task, or authorized branch differs from the execution card, stop rather than improvising.
- Do not expand a task into adjacent governance work merely because an improvement is visible.

## Verification levels

Use the lightest verification that can establish the task safely:

- **V0 — control/documentation/layout:** path/tree checks, content/link/frontmatter consistency, and scope verification.
- **V1 — localized behavior:** targeted tests plus relevant lint/type checks.
- **V2 — domain change:** targeted tests, the affected domain suite, and required integration tests.
- **V3 — cross-domain/high-risk/release:** broad relevant integration/build/runtime acceptance appropriate to the changed system.

The active task must state the chosen level and why. Do not run a full historical test suite merely because one exists if the accepted task removes the runtime it tested.

## Incident Doctor boundary

Incident Doctor is not a parallel product track. Enter it only when a real failure or unexplained behavior blocks safe progress and current evidence cannot answer the needed question. The sequence is: classify the problem, assess evidence sufficiency, analyze existing evidence, add the minimum probe if needed, capture a fresh incident, test/falsify hypotheses, and define the minimum evidence-supported fix boundary. That diagnosis does not itself authorize a behavior change: if the active task does not authorize the fix and required side effects, return to Project Governance for reconciliation/re-authorization before changing behavior. After an authorized fix, verify regression, then retire or explicitly promote the probe.

## Legacy preservation

Historical code, plans, and governance experiments remain recoverable through Git history and stable tags. Do not keep obsolete runtime trees in the active repository merely as an archive. If current scope retires a subsystem, remove it from the live tree after the retirement task is explicitly authorized and verified.
