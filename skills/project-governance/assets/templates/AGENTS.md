<!-- Governance adoption template: declare CONTROL_MODE: FILE_CONTROL or ISSUE_CONTROL, ISSUE_APPROVERS and Issue permissions/cutover basis. ISSUE_WEB_SPEC_AUTHORING is a separate, optional Web Agent A authoring opt-in; default deny and keep it independent from approval. ISSUE_DELEGATED_APPROVAL: ENABLED is a separate explicit lower-assurance approval-proxy opt-in. RISK_SCOPED_AUTONOMY: ENABLED is a separate opt-in and remains inactive until trusted host and credential-separation evidence is independently verified. Never enable a permission implicitly from Plugin installation or template copy. -->

# Project Agent Guidance

Record only durable **project-specific normative rules and boundaries** supported by verified evidence. Reusable Engineering Governance workflow belongs in the Plugin Skills, not here.

## Normative project rules
[Project-specific MUST/MUST-NOT rules, canonical writers/authority boundaries, safety/data constraints, and durable operating invariants. Omit descriptive background that belongs in the Project Profile.]

## Issue authoring and approval
ISSUE_WEB_SPEC_AUTHORING: DISABLED

[Keep disabled unless this project explicitly authorizes Web Agent A to create or revise Issue execution-spec drafts. Enabling this line grants only user-requested Issue-spec authoring; it does not approve a spec or grant source, branch, PR, merge, or release authority.]

## Risk-scoped autonomy
RISK_SCOPED_AUTONOMY: DISABLED

[Keep disabled unless an accepted policy change explicitly opts in and the actual GitHub host, protected grant workflow, current grant/revocation state, target binding, and grant/executor credential separation are independently verified. A local JSON snapshot or actor login alone is not proof. This opt-in does not authorize G3 work, merge/release/deployment, protected-main writes, privileged install, credentials, destructive data overwrite, another repository, or human UI acceptance.]

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
