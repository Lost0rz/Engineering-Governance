# Current Task

Task ID: [from the active authorization]

Task class: [optional semantic purpose when useful: DESIGN | EXECUTION | AUDIT | VERIFY | DIAGNOSIS | CORRECTIVE | CLOSEOUT | project-equivalent]

State: [current authorized, executing, retained/waiting, stopped, or terminal state]

Mode: [bounded execution/investigation/review mode when it adds decision value]

## Objective

[One concrete authorized outcome with an observable boundary. Do not combine unrelated engineering purposes merely to avoid creating a later task.]

## Planning context

[When this task implements part of durable design/planning, record `Related document`, bounded section/work package, revision/observation basis, and relationship to plan. A written accepted solution is referenced here rather than re-derived by each executor. The planning authority supplies durable rationale/design but is not a fourth control file and does not authorize execution.]

## Task boundary

[When material, state whether this task is a continuation of an existing engineering purpose or a distinct purpose such as design, execution, independent audit/acceptance, corrective work, verification/diagnosis, or closeout. `Task class` is metadata owned by this file, not another authority. Subagent work units and Web/local/session/machine changes do not create new tasks by themselves.]

## Affected domains

[Use accepted product/domain/capability authorities and any useful navigation projection. State `unknown` when ownership cannot be verified; do not infer ownership from folder names.]

## Start baseline

[Actual repository/ref/revision/runtime identity needed for the task. Distinguish literal Repository HEAD from Delivery / Semantic HEAD when relevant and classify recorded Git identities as provenance/transition/current/explicit locks rather than treating every SHA as equality.]

## Workspace lifecycle

[If the project uses task branches/worktrees/multiple checkouts, record the selected workspace, task-relevant overlapping predecessor writers, write capability, unique-work risk, and expected retain/terminal disposition. Use `not applicable` when the project does not use this model. Execution context (Web/local/cloud/subagent/session) does not itself establish workspace or write authority.]

## In scope

- [Explicitly authorized work]

## Out of scope

- [Adjacent work not authorized by this task]

## Known evidence

[Relevant sources/identities/observations with freshness. Separate verified fact from inference.]

## Risk and rationale

[Concise blast radius/material risks; no numerical score.]

## Verification level, cadence, and rationale

[Choose `V0`–`V3`, required checks, intentionally deferred checks, and cadence. If a multi-part architecture/framework task defers integrated acceptance until architecture freeze, state that explicitly; construction sanity checks do not replace final acceptance. Implementation self-check/verification is not automatically an independent audit.]

## Acceptance criteria

- [Observable evidence that establishes this task's completion; do not claim independent reviewer/user acceptance on their behalf.]

## Stop conditions

- [Authority/scope/evidence/baseline/workspace/safety conditions that require stopping. `CONTROL_ONLY_DRIFT` alone is not a delivery-identity stop, but material task-content changes remain authoritative.]

## Handoff / current stop point

[Task-owned lifecycle state: required evidence, next authorized milestone, recipient/review state, and workspace disposition where material. This section is **not** a transport handoff card. The same task may continue across agents/sessions/machines through `agent-handoff` when objective/authorization is unchanged.]

Before a final successful state-changing handoff, run the Control Alignment Gate and report `RELATED_DOCUMENT`, `DOCUMENT_ALIGNMENT`, `CURRENT_STATUS_RECONCILIATION`, `CURRENT_TASK_RECONCILIATION`, and `CONTROL_ALIGNMENT`.

Routine CI/review/audit/mergeability observations do not require a task-file write unless they materially change task-owned semantics. A material objective/scope/authorization change requires task reconciliation before affected mutation. A new execution context alone does not.