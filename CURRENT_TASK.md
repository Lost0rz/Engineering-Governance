# CURRENT TASK — Capability Architecture Hardening v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ARCHITECTURE-HARDENING-063`

State: `ACTIVE`

Mode: remote reusable-source architecture hardening before consolidated installed Plugin/runtime acceptance

## Objective

Refine the frozen v0.6.0 seven-Skill architecture so task semantics, Sub Agent orchestration, model selection, cross-context handoff, and independent audit behavior match the intended operating model before integrated acceptance.

The goal is **not** to suppress Sub Agents or high-capability models. The goal is to use them deliberately and effectively: parallelize independent work when useful, select stronger models when judgment demand justifies them, keep execution authority explicit, and separate engineering task purpose from the Web/Local/agent context in which the work happens.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: Task 062 froze a complete architecture candidate; Task 063 reopens source architecture only for bounded semantic hardening accepted after the seven-Skill audit.

## Accepted baseline

- Task start literal branch HEAD: `177c685e867747eb8346edcef31272e03df405ea`.
- Prior frozen Architecture Delivery / Semantic HEAD: `26fdc590b4c4ef1e25781f7065626fc87fc349cf`.
- Branch: `codex/capability-model-v0.6.0`.
- PR #26: OPEN / DRAFT / UNMERGED.
- Published/installed Plugin baseline remains `0.5.5`.
- Installed v0.6.0 integrated acceptance has not run.

## User-decided architecture corrections

1. **Sub Agents are a throughput capability, not a behavior to minimize.** When authorized work decomposes into genuinely independent units, the orchestrator should use available safe parallelism. The constraint is dependency/writer/integration safety, not an arbitrary preference for fewer agents.
2. **HIGH-capability models are allowed and should be selected when justified.** The prohibited behavior is silent/unreasoned inheritance or escalation, not intentional use of strong models.
3. **Web and Local are execution contexts, not engineering task classes.** The same execution task may cross contexts without becoming a new task merely because another machine/session/agent continues it.
4. **Task boundaries follow engineering purpose/authorization.** Design, execution, independent audit/acceptance, corrective work, verification, diagnosis, and closeout may be distinct tasks when their objective/authority boundary is distinct. Subagent work units inside one authorized execution remain the same task.
5. **A written/accepted solution is execution authority context, not something every executor re-derives.** An execution task should implement the accepted design/plan; a later independent audit/acceptance task evaluates the result from its own evidence boundary.

## In scope

1. Add a lightweight task-purpose / task-class contract under Project Governance, including same-task vs new-task rules.
2. Make Execution Orchestrator positively exploit safe parallel Sub Agent capacity when decomposition is beneficial, while preserving dependency and writer-authority gates.
3. Add explicit environment model-tier mapping semantics for actual model + reasoning effort, including intentional HIGH selection and explicit escalation/fallback behavior.
4. Make handoff context-neutral: source/target contexts may be Web, local, cloud, subagent, reviewer, or another execution surface without defining task purpose.
5. Bind same-task cross-context continuation to the same task authority and fresh authority basis rather than duplicated interpretation.
6. Clarify that formal independent audit/acceptance is a distinct task-purpose boundary when independence is required; implementation self-check remains verification rather than independent acceptance.
7. Update the integrated acceptance specification for positive Sub Agent use, intentional HIGH-model use, task-purpose/context separation, and cross-context same-task continuity.
8. Re-audit the hardened source and freeze a new v0.6.0 Architecture Delivery / Semantic HEAD candidate.

## Out of scope

- Running installed Plugin/Web/Codex integrated acceptance under this task.
- Adding an eighth top-level Skill.
- Hardcoding one universal provider/model name into reusable governance.
- Adding a model-router executable, daemon, scheduler, database, automatic enforcement runtime, or fourth project control file.
- Merging PR #26 or publishing v0.6.0.

## Verification level, cadence, and rationale

`V2` source-architecture hardening.

During construction use bounded source/reference consistency checks only. After all hardening changes are integrated, run one remote source-architecture audit and freeze a new semantic head. Installed Plugin/Web/Codex acceptance remains one later consolidated pass against that frozen identity.

## Acceptance criteria

- Project Governance distinguishes engineering task purpose from execution context and from subagent work units.
- The same authorized task can continue across contexts without artificial task duplication.
- Independent audit/acceptance can be represented as a distinct task-purpose boundary rather than implementer self-review masquerading as independence.
- Execution Orchestrator treats safe parallelism as useful capacity and can actively dispatch independent units when beneficial.
- Model selection can intentionally choose LOW / STANDARD / HIGH and bind those tiers to actual environment model/reasoning settings when material.
- HIGH use is not prohibited; silent/unjustified inheritance/escalation remains prohibited.
- Handoff references the same task authority for continuation and records enough authority basis to detect incompatible drift.
- Integrated acceptance scenarios cover these semantics.
- No new task/status/control authority is introduced.
- PR #26 remains Draft.

## Stop conditions

- A proposed rule makes Web/Local a reusable task-authority distinction.
- A proposed rule suppresses useful parallel agents or HIGH models solely for conservatism rather than dependency/risk/cost constraints.
- A proposed task class becomes a second task authority instead of metadata owned by `CURRENT_TASK.md`.
- The branch acquires unrelated runtime/release implementation.

## Handoff / current stop point

Task 063 is authorized for remote source hardening. The next terminal boundary is a **new hardened architecture semantic freeze**, followed later by the existing consolidated integrated acceptance process.