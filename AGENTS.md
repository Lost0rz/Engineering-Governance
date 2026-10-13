# Engineering-Governance Repository Rules

## Repository purpose

Engineering-Governance is the source repository for reusable AI engineering-governance Skills, templates, operating rules, routing/adoption contracts, and governance context. It is not a business-product repository, generic governance runtime, installer runtime, daemon, scheduler, database, or automatic enforcement/remediation service.

A target project is adapted by an AI agent after inspecting that project's real repository state. Templates define structure/required semantics; they are not copied blindly and do not replace project-specific facts.

## Core principles

1. **Three-file control plane.** `AGENTS.md` holds durable project/repository operating rules, `CURRENT_STATUS.md` is the concise verified current-state snapshot, and `CURRENT_TASK.md` is the single active execution authorization.
2. **Durable planning is linked, not duplicated control.** Long-lived design/large-PR/multi-task rationale may live in an accepted planning authority. Planning documents are not a fourth control file and do not own live progress or authorize execution.
3. **Seven-Skill capability model.** Top-level Skills are exactly `project-governance`, `solution-design`, `execution-orchestrator`, `agent-handoff`, `evidence-audit`, `domain-navigation`, and `incident-doctor`. Global routing policy is not an eighth Skill.
4. **Project Governance remains the normal entry/authority owner.** Narrow Skills own bounded capabilities and return to the caller; none creates a second task authority.
5. **Business-first, design/orchestration/audit on demand.** Clear product/business work stays lightweight. Use Solution Design only for material design ambiguity, Execution Orchestrator only for non-trivial execution topology, Evidence Audit when an independent evidence verdict is needed, Domain Navigation when route/authority/source/test location is unclear, and Incident Doctor only after its blocking evidence-gap gate is met.
6. **Handoff is transport, not authority.** Cross-agent/session/machine cards reference authoritative controls plus fresh delta/action boundary/return contract. Do not copy whole controls or durable Engineering Governance procedure into cards by default.
7. **Controlled agent/model topology.** Prefer one executor and parallel readers. Overlapping writers require one authority; multiple writers require proven-disjoint write scopes/workspaces plus integration evidence. No silent model escalation.
8. **Proportional verification.** `V0`–`V3` expresses change risk/scope; cadence is separate. Universal mandatory TDD is not a repository rule. Use the lightest evidence that safely proves the accepted behavior/risk boundary.
9. **Control records are not delivery identity.** `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement advances literal Repository HEAD but may be `CONTROL_ONLY_DRIFT` without changing Delivery / Semantic HEAD. Repository-host gates remain live constraints on the literal identity the host governs.
10. **Final control alignment is mandatory; writes are conditional.** Governed state-changing work rereads/compares current status/task and materially affected linked planning authority before a final successful handoff, updates only sources whose owned semantics changed, and reports alignment explicitly.

## Repository layout

- `skills/` contains reusable Skill modules. Each top-level module has one `SKILL.md` plus only needed `references/`, `assets/`, and `scripts/`.
- `documents/` contains durable planning/design authority for this repository when work spans bounded tasks or needs long-lived rationale/constraints. It is not live progress state.
- `references/` records upstream research, attribution/licensing notes, and repository-wide reference material.
- `examples/` contains validated examples only.
- `docs/superpowers/` may preserve historical/tool-oriented maintainer planning; it is not reusable Plugin payload.
- Root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` govern this repository itself.

## Skill design rules

- Use the Agent Skills shape: `SKILL.md` plus optional supporting directories.
- A Skill must have a distinct trigger, ownership boundary, and output/return contract. Do not create a Skill merely because a topic exists.
- Keep frontmatter `description` focused on **when to use** the Skill rather than summarizing its full workflow; put procedure in the Skill body/references.
- Keep frequently selected Skill bodies focused; move detailed contracts/examples into references for progressive disclosure.
- Do not duplicate authority across Skills. Project Governance owns task/control/workspace lifecycle; Solution Design owns design resolution; Execution Orchestrator owns execution topology/model/parallel/recovery policy; Agent Handoff owns transfer envelopes; Evidence Audit owns independent evidence verdicts; Domain Navigation owns semantic/source routing; Incident Doctor owns evidence-gated diagnosis.
- Scripts are optional and must be justified. Do not add daemons, background services, databases, installer executables, automatic remediation, or silent global-file mutation.

## Evidence and adaptation

- Inspect a target repository before generating/updating governance files.
- Separate verified facts, user/project decisions, agent assumptions, and agent-made choices. Unsupported facts remain unknown.
- Prefer concrete paths, symbols, manifests, tests, runtime entry points, Git identities, CI jobs/runs, and host-gate evidence.
- Discover accepted semantic/domain/architecture authorities before creating derived maps or documents; reference them rather than duplicate product truth.
- External projects are references, not hidden dependencies. Record conceptual influence and licensing posture before copying code/text. Prefer adaptation of ideas over verbatim process import.
- When revisions are named, classify their semantic role before comparing them. Provenance/transition bases are not implicit current-head equality locks.
- Audit claims bind to the identity/range they inspected. Preserve semantic-evidence vs repository-host-gate separation.

## Delivery workflow

- Keep one active task in `CURRENT_TASK.md`.
- Link a durable planning section/work package when the task implements part of a cross-task design; standalone tasks may have no related document.
- On material objective/scope/authorization change, reconcile the control plane before affected implementation.
- Prefer small independently reviewable slices without forcing artificial task fragmentation.
- Use Agent Handoff for Web-to-local/local-to-Web or other cross-context transfer. The card carries authority references + fresh delta + bounded target/return evidence; it must not restate generic governance rules or become a second task file.
- Use Execution Orchestrator only when decomposition/agents/parallelism/model choice/recovery actually need policy. One executor is a valid and preferred topology for many tasks.
- **Repository-specific execution split:** Web/remote session owns reusable source construction, remote GitHub mutation, integration, source audit, and release preparation for this repository. Local AI is primarily for installed Plugin/runtime/behavior acceptance and must not repair reusable source during that acceptance; reusable defects return to the Web/remote source flow.
- Preserve unknown staged/unstaged/untracked/local-only work. Do not reset/stash/delete/force-clean merely to satisfy a card.
- Before final successful state-changing handoff, run the Control Alignment Gate and report document/status/task alignment.

## Verification levels

- **V0 — control/documentation/layout:** path/tree/content/link/frontmatter/scope consistency.
- **V1 — localized behavior:** targeted tests plus relevant lint/type checks.
- **V2 — domain/cross-capability change:** targeted checks plus affected-domain/integration evidence.
- **V3 — cross-domain/high-risk/release:** broad relevant integration/build/runtime/release evidence.

Verification effort follows change risk, not change count. At merge/release boundaries, semantic implementation evidence and live repository-host gate state are separate claims and both must satisfy the accepted contract.

## Incident Doctor boundary

Incident Doctor is not a parallel product track. Enter only when a real failure/unexplained unsafe ambiguity blocks safe progress **and** current evidence cannot answer the needed decision. Use existing evidence first, then the minimum probe/hypothesis test required. Diagnosis does not itself authorize a behavior change.

## Legacy preservation

Historical plans/governance experiments remain recoverable through Git history/tags. Do not keep obsolete runtime trees in the active repository merely as archives.
