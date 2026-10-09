# Current Task

Task ID: [from the active authorization]

State: [current authorized, execution, or handoff state]

Mode: [bounded execution, investigation, or other authorized mode]

## Objective

[One concrete outcome with an observable boundary. Do not combine unrelated objectives.]

## Affected domains

[Use accepted business/product/domain/capability authorities and any useful derived navigation projection. State `unknown` or `not established` when ownership cannot be verified. Do not require a literal `DOMAIN_MAP.md`.]

## Start baseline

[Actual verified repository identity, branch/ref, revision, and relevant remote or runtime identity. For source-controlled work, include the task-relevant workspace/unique-work state when it affects safe execution. Do not use an assumed baseline.]

## Workspace lifecycle

[When the project uses task branches, worktrees, multiple checkouts, or an equivalent workspace model, record the selected workspace identity, any task-relevant predecessor whose write authority materially overlaps this task, whether a retained predecessor can still resume writes, the expected terminal/non-terminal disposition, and any explicit retain-until condition. Use `not applicable` when the project does not use task workspaces. Do not treat a broad Domain/capability label as an automatic writer lock, and keep unrelated global workspace history out of this task file unless this task explicitly performs legacy reconciliation.]

## In scope

- [Explicitly authorized work]

## Out of scope

- [Adjacent work not authorized by this task]

## Known evidence

[Relevant sources, identities/revisions, observations, and freshness basis. Keep inference separate from verified facts.]

## Risk and rationale

[Concise change radius, material risks, and why the chosen verification depth is suitable. Do not calculate a numerical risk score.]

## Verification level and rationale

[Chosen `V0`–`V3` level, short rationale, required checks, and material checks intentionally omitted. Choose the lightest level that can safely establish the result.]

## Acceptance criteria

- [Observable evidence that establishes completion; do not claim independent reviewer or user acceptance on their behalf.]

## Stop conditions

- [Baseline, evidence, authority, scope, workspace, or safety conditions that halt this task. In source-controlled projects, include task-relevant baseline/control drift, a predecessor that remains able to write an overlapping authority, and unknown unique work when they cannot be resolved without destructive assumptions or parallel writers.]

## Handoff / current stop point

[Required evidence, recipient or review state, next authorized milestone, and—when workspace lifecycle is material—the actual workspace disposition, current write capability if retained, explicit retention reason/release condition, and whether the latest lifecycle event is terminal for this task/phase. A merge or similarly named event does not itself prove terminal status or local closeout. A handoff does not itself mean independent review accepted the work.]

Ordinary evidence discovery within the accepted objective does not expand scope or create a new task. A material objective or scope change requires updated task authorization before the affected work continues.
