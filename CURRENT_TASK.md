# CURRENT TASK — Contract Corrective v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-CONTRACT-CORRECTIVE-069`

Task class: `CORRECTIVE`

State: `COMPLETE`

## Objective

Tighten the remaining v0.6.0 contract gaps around Project Profile mutation/surface ownership, Card/Receipt schema, capability-vs-mode semantics, artifact lifecycle taxonomy, compact status receipts, advisory-vs-formal audit boundaries, context recovery and acceptance coverage without adding new Skills or control files.

## Completed

- required compatible Project Governance / `CURRENT_TASK.md` authorization before repository/project-managed Profile mutation;
- defined one current Profile projection surface or one primary + derived mirror;
- separated Handoff `CAPABILITY` from `MODE` and made Card/Receipt required-core fields explicit;
- added `PURPOSE` and other conditional transfer fields without bloating the core schema;
- clarified that Handoff modes do not replace Skill routing;
- separated `IMPLEMENTATION_AUTHORITY` from `OBSERVED_EVIDENCE` in artifact lifecycle;
- made one compact human Engineering Status Receipt the normal required ending for governed engineering/status/audit/CI/PR/merge responses;
- distinguished advisory read-only inspection from formal Evidence Audit verdict boundaries;
- aligned optional Profile landing-page recovery wording;
- slimmed Domain Navigation top-level Skill for progressive disclosure;
- updated integrated acceptance, durable design authority, README and global routing template to the Task 069 semantics.

## Architecture freeze

Frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`7be11aae70c42b075034eb4613a7dc66b242bb80`

## Verification

`V2 remote source-architecture audit: PASS`.

`AUDIT_INDEPENDENCE: SELF_CHECK`.

- exact eight top-level Skill directories;
- Plugin metadata remains `0.6.0`;
- no competing task/control authority or duplicate Profile/Domain authority;
- Project Profile mutation/surface ownership rules are explicit;
- Card/Receipt schema is internally consistent and side-effect-safe;
- `CAPABILITY` and `MODE` are independent dimensions;
- artifact taxonomy cleanly separates semantic owners from observed evidence;
- advisory inspection vs formal audit routing is explicit;
- durable design and routing surfaces align with current source;
- source changes remain governance/Skill/design/acceptance Markdown/control only;
- no runtime/daemon/database/model-router/automatic enforcement implementation added;
- PR #26 OPEN / DRAFT / UNMERGED and mergeable at final audit time;
- no commit/check status on semantic head, so CI PASS is not claimed.

## Terminal state

Task 069 is complete. Next milestone is one consolidated installed Plugin/Web/Codex acceptance against the frozen semantic identity (or a proven semantic-tree-equivalent control-only descendant).

Control Alignment:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-hardening-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UPDATED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
