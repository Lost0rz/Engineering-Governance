# Current Task

Task ID: [from the active authorization]

State: [current authorized, execution, retained-review, or terminal state]

Mode: [bounded execution, investigation, or other authorized mode]

## Objective

[One concrete outcome with an observable boundary. Do not combine unrelated objectives.]

## Planning context

[When this task implements part of durable design/planning, record `Related document`, bounded section/work package, revision/observation basis, and relationship to plan. The planning authority supplies durable rationale/design but is not a fourth control file and does not authorize execution.]

## Affected domains

[Use accepted product/domain/capability authorities and any useful navigation projection. State `unknown` when ownership cannot be verified; do not infer ownership from folder names.]

## Start baseline

[Actual repository/ref/revision/runtime identity needed for the task. Distinguish literal Repository HEAD from Delivery / Semantic HEAD when relevant and classify recorded Git identities as provenance/transition/current/explicit locks rather than treating every SHA as equality.]

## Workspace lifecycle

[If the project uses task branches/worktrees/multiple checkouts, record the selected workspace, task-relevant overlapping predecessor writers, write capability, unique-work risk, and expected retain/terminal disposition. Use `not applicable` when the project does not use this model.]

## In scope

- [Explicitly authorized work]

## Out of scope

- [Adjacent work not authorized by this task]

## Known evidence

[Relevant sources/identities/observations with freshness. Separate verified fact from inference.]

## Risk and rationale

[Concise blast radius/material risks; no numerical score.]

## Verification level, cadence, and rationale

[Choose `V0`–`V3`, required checks, intentionally deferred checks, and cadence. If a multi-part architecture/framework task defers integrated acceptance until architecture freeze, state that explicitly; construction sanity checks do not replace final acceptance.]

## Acceptance criteria

- [Observable evidence that establishes task completion; do not claim independent reviewer/user acceptance on their behalf.]

## Stop conditions

- [Authority/scope/evidence/baseline/workspace/safety conditions that require stopping. `CONTROL_ONLY_DRIFT` alone is not a delivery-identity stop, but material task-content changes remain authoritative.]

## Handoff / current stop point

[Task-owned lifecycle state: required evidence, next authorized milestone, recipient/review state, and workspace disposition where material. This section is **not** a transport handoff card. Do not paste a Web/local/subagent request here merely to move work between contexts. Use `agent-handoff` for the separate request/receipt envelope.]

Before a final successful state-changing handoff, run the Control Alignment Gate and report `RELATED_DOCUMENT`, `DOCUMENT_ALIGNMENT`, `CURRENT_STATUS_RECONCILIATION`, `CURRENT_TASK_RECONCILIATION`, and `CONTROL_ALIGNMENT`.

Routine CI/review/audit/mergeability observations do not require a task-file write unless they materially change task-owned semantics. A material objective/scope/authorization change requires task reconciliation before affected mutation.
