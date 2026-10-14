# Engineering-Governance Repository Rules

## Repository purpose

Engineering-Governance is the source repository for reusable AI engineering-governance Skills, templates, operating rules, routing/adoption contracts, and governance context. It is not a business-product repository, generic governance runtime, installer runtime, daemon, scheduler, database, or automatic enforcement/remediation service.

A target project is adapted by an AI agent after inspecting that project's real repository state. Templates define structure/required semantics; they are not copied blindly and do not replace project-specific facts.

## Core principles

1. **Three-file control plane.** `AGENTS.md` holds durable project/repository operating rules, `CURRENT_STATUS.md` is the concise verified current-state snapshot, and `CURRENT_TASK.md` is the single active execution authorization.
2. **Durable planning is linked, not duplicated control.** Long-lived design/large-PR/multi-task rationale may live in an accepted planning authority. Planning documents are not a fourth control file and do not own live progress or authorize execution.
3. **Seven-Skill capability model.** Top-level Skills are exactly `project-governance`, `solution-design`, `execution-orchestrator`, `agent-handoff`, `evidence-audit`, `domain-navigation`, and `incident-doctor`. Global routing policy is not an eighth Skill.
4. **Project Governance remains the normal entry/authority owner.** Narrow Skills own bounded capabilities and return to the caller; none creates a second task authority.
5. **Task purpose is independent from execution context.** A task owns one engineering objective/authorization. Sub Agent work units remain inside that task unless purpose/authority changes. Web/local/cloud/session/machine/agent are execution contexts, not reusable task classes.
6. **Business-first, specialist Skills on demand.** Clear work stays lightweight. Use Solution Design only for material design ambiguity, Execution Orchestrator when decomposition/parallelism/model/recovery policy adds value, Agent Handoff when responsibility crosses contexts, Evidence Audit for an explicit evidence/acceptance boundary, Domain Navigation when route/authority/source/test location is unclear, and Incident Doctor only after its blocking evidence-gap gate is met.
7. **Handoff is transport, not authority.** Cross-agent/session/machine cards preserve task authority and carry authority references + fresh delta + action boundary + return contract. Do not copy whole controls or durable Engineering Governance procedure into cards by default.
8. **Use safe agent parallelism deliberately.** Sub Agents are throughput/context-isolation capability, not something to minimize by policy. Exploit independent parallel units when useful. Overlapping writers require one authority; multiple writers require proven-disjoint semantic write scopes/workspaces plus integration evidence.
9. **Select model capability explicitly.** `LOW / STANDARD / HIGH` are portable capability tiers. HIGH is valid when judgment demand justifies it. Do not silently inherit/escalate model capability; map tiers to actual model/reasoning settings in the execution environment when material.
10. **Proportional verification.** `V0`–`V3` expresses change risk/scope; cadence is separate. Implementation self-check is verification, not automatically independent acceptance. Universal mandatory TDD is not a repository rule.
11. **Control records are not delivery identity.** `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement advances literal Repository HEAD but may be `CONTROL_ONLY_DRIFT` without changing Delivery / Semantic HEAD. Repository-host gates remain live constraints on the literal identity the host governs.
12. **Final control alignment is mandatory; writes are conditional.** Governed state-changing work rereads/compares current status/task and materially affected linked planning authority before a final successful handoff, updates only sources whose owned semantics changed, and reports alignment explicitly.

## Repository layout

- `skills/` contains reusable Skill modules. Each top-level module has one `SKILL.md` plus only needed `references/`, `assets/`, and `scripts/`.
- `documents/` contains durable planning/design authority for this repository when work spans bounded tasks or needs long-lived rationale/constraints. It is not live progress state.
- `references/` records upstream research, attribution/licensing notes, repository-wide maintainer contracts, and integrated acceptance specifications.
- `examples/` contains validated examples only.
- `docs/superpowers/` may preserve historical/tool-oriented maintainer planning; it is not reusable Plugin payload.
- Root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` govern this repository itself.

## Skill design rules

Follow `references/SKILL_ENGINEERING.md` for the maintainer quality contract.

- Use the Agent Skills shape: `SKILL.md` plus optional supporting directories.
- A Skill must have a distinct trigger, ownership boundary, return contract, and negative/near-miss trigger guidance. A topic alone is not a Skill.
- Keep frontmatter `description` focused on **when to use** the Skill rather than summarizing its full workflow; put procedure in the Skill body/references.
- Keep frequently selected Skill bodies focused; move detailed contracts/examples into references for progressive disclosure.
- Do not duplicate authority across Skills. Project Governance owns task/control/workspace lifecycle; Solution Design owns design resolution; Execution Orchestrator owns execution topology/model/parallel/recovery policy; Agent Handoff owns transfer envelopes; Evidence Audit owns evidence verdicts; Domain Navigation owns semantic/source routing; Incident Doctor owns evidence-gated diagnosis.
- Over-triggering and systematic under-use are both defects: do not invoke a Skill just because it is installed, but do not suppress a materially useful bounded capability merely for conservatism.
- Scripts are optional and must be justified. Do not add daemons, background services, databases, installer executables, automatic remediation, or silent global-file mutation.

## Evidence and adaptation

- Inspect a target repository before generating/updating governance files.
- Separate verified facts, user/project decisions, agent assumptions, and agent-made choices. Unsupported facts remain unknown.
- Prefer concrete paths, symbols, manifests, tests, runtime entry points, Git identities, CI jobs/runs, and host-gate evidence.
- Discover accepted semantic/domain/architecture authorities before creating derived maps or documents; reference them rather than duplicate product truth.
- External projects are references, not hidden dependencies. Record conceptual influence and licensing posture before copying code/text. Prefer adaptation of ideas over verbatim process import.
- When revisions are named, classify their semantic role before comparing them. Provenance/transition bases are not implicit current-head equality locks.
- Audit claims bind to the identity/range and required claims they inspected. Preserve semantic-evidence vs repository-host-gate separation.

## Delivery workflow

- Keep one active task in `CURRENT_TASK.md`.
- Use optional `TASK_CLASS` only when engineering-purpose distinction helps (for example DESIGN / EXECUTION / AUDIT / VERIFY / DIAGNOSIS / CORRECTIVE / CLOSEOUT). It is task metadata, not another authority.
- Link a durable planning section/work package when the task implements part of a cross-task design; standalone tasks may have no related document.
- On material objective/scope/authorization/task-purpose change, reconcile the control plane before affected implementation.
- Do not create a new task merely because work crosses Web/local/session/machine/agent context or is decomposed into Sub Agent units.
- Prefer small independently reviewable slices without forcing artificial task fragmentation.
- Use Agent Handoff for cross-context transfer. Same-purpose continuation keeps the same task authority; the card carries authority references + fresh delta + bounded target/return evidence.
- Use Execution Orchestrator when decomposition/agents/parallelism/model choice/recovery adds material value. Use safe available parallelism deliberately; one executor remains correct when delegation has no material benefit or dependencies/shared state dominate.
- HIGH model capability is allowed and should be chosen deliberately when reasoning demand justifies it. The failure mode is silent/unjustified selection, not strong-model use itself.
- Use Evidence Audit for explicit acceptance/readiness judgments. Implementation self-check is not automatically independent; formal independent acceptance should declare its task purpose and independence basis when required.
- **Repository-specific execution convention:** for this source repository today, Web/remote sessions commonly own reusable-source construction/remote GitHub mutation/source audit while local AI is commonly used for installed Plugin/runtime acceptance. This is an operational convention of this repository, not the reusable meaning of DESIGN/EXECUTION/AUDIT tasks and not a rule that Web or Local inherently owns a capability.
- Preserve unknown staged/unstaged/untracked/local-only work. Do not reset/stash/delete/force-clean merely to satisfy a card.
- Before final successful state-changing handoff, run the Control Alignment Gate and report document/status/task alignment.

## Verification levels and cadence

- **V0 — control/documentation/layout:** path/tree/content/link/frontmatter/scope consistency.
- **V1 — localized behavior:** targeted tests plus relevant lint/type checks.
- **V2 — domain/cross-capability change:** targeted checks plus affected-domain/integration evidence.
- **V3 — cross-domain/high-risk/release:** broad relevant integration/build/runtime/release evidence.

Verification effort follows change risk, not change count. Cadence may deliberately separate construction sanity checks from expensive integrated acceptance. At merge/release boundaries, semantic implementation evidence and live repository-host gate state are separate claims and both must satisfy the accepted contract.

## Incident Doctor boundary

Incident Doctor is not a parallel product track. Enter only when a real failure/unexplained unsafe ambiguity blocks safe progress **and** current evidence cannot answer the needed decision. Use existing evidence first, then the minimum probe/hypothesis test required. Diagnosis does not itself authorize a behavior change.

## Legacy preservation

Historical plans/governance experiments remain recoverable through Git history/tags. Do not keep obsolete runtime trees in the active repository merely as archives.
