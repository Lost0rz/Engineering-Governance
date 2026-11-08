<!-- Governance adoption template: declare CONTROL_MODE: FILE_CONTROL or ISSUE_CONTROL, ISSUE_APPROVERS and Issue permissions/cutover basis. ISSUE_WEB_SPEC_AUTHORING is a separate, optional Web Agent A authoring opt-in; default deny and keep it independent from approval. ISSUE_DELEGATED_APPROVAL: ENABLED is a separate explicit lower-assurance approval-proxy opt-in. Never enable either permission implicitly from Plugin installation or template copy. -->

# Project Agent Guidance

Record only durable **project-specific normative rules and boundaries** supported by verified evidence. Reusable Engineering Governance workflow belongs in the Plugin Skills, not here.

## Normative project rules
[Project-specific MUST/MUST-NOT rules, canonical writers/authority boundaries, safety/data constraints, and durable operating invariants. Omit descriptive background that belongs in the Project Profile.]

## Issue authoring and approval
ISSUE_WEB_SPEC_AUTHORING: DISABLED

[Keep disabled unless this project explicitly authorizes Web Agent A to create or revise Issue execution-spec drafts. Enabling this line grants only user-requested Issue-spec authoring; it does not approve a spec or grant source, branch, PR, merge, or release authority.]

## Authority exceptions / durable boundaries
[Only project-specific authority rules that materially constrain execution. Point to accepted domain/data/architecture authorities rather than copying their detail.]

## Environment / storage constraints
[Only durable project-specific execution, runtime, storage, LAN/device, or canonical-machine constraints. Do not record current machine-local model/tool defaults unless the project intentionally owns them as portable configuration.]

## Project-specific commands
[Only verified commands needed for safe work. Omit when none are established.]

## Project-specific stop conditions
[Only project-specific conditions beyond reusable Engineering Governance rules. Unknown unique work or conflicting authority should remain explicit rather than guessed.]

## Context pointers
[Optional pointers to `PROJECT_PROFILE.md`, Domain/navigation authority, durable planning authority, or other accepted project sources. These pointers do not copy their contents or create new authority.]
