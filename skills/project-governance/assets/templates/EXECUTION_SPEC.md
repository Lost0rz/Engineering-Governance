# EXECUTION_SPEC_V1 — GitHub Issue body template

> A form can capture fields; it cannot prove detailed plan quality or authorization. Replace all placeholders with verified, executable content. Keep DRAFT until approved for the exact revision.

CONTRACT: EXECUTION_SPEC_V1
REPOSITORY: <owner/repo>
ISSUE: <GitHub number assigned after creation>
TASK_ID: <stable-id>
SPEC_REVISION: 1
MODE: EXECUTE
PURPOSE: <bounded engineering purpose>
AUTHORIZATION: <explicit trusted approving actor + link + approved revision, or PENDING>
TASK_STATE: DESIGN_REVIEW

## Objective / accepted outcome
<one observable result, not 'improve X'>

## Verified baseline
<repository ref, code paths/symbols/API/data owners, inspected proof; UNKNOWN where not verified>

## Target state and acceptance claims
<positive cases and forbidden regression cases>

## Scope / side effects / non-goals
- IN_SCOPE:
- OUT_OF_SCOPE:
- ALLOWED_SIDE_EFFECTS:
- AUTHORITATIVE_DESIGN:

## Work Packages

### WP01 — <name>
- Preconditions:
- Verified target file(s) / function(s) / interface(s):
- Ordered implementation actions:
  1. 
  2. 
- Boundaries and permitted local discretion:
- Dependencies:
- Edge cases and failure handling:
- Focused verification (command/check, expected result):
- Done criteria:

## Dependency / integration order
<WP graph, disjoint units, integration owner>

## Deviation / STOP
- L0 CONTINUE only for proven nonsemantic adaptation:
- L1 LOCAL_CORRECT only within approved scope and risk limit:
- L2 PAUSE_AND_ASK when design/permission/API/side effects change:
- L3 TERMINATE on revoked authority/destructive/security/unsafe state:
- Additional STOP:

## Final verification / acceptance / receipt
- Proportional tests and host-bound evidence:
- HUMAN_UI_ACCEPTANCE: PENDING / NOT_REQUIRED with rationale
- PR/branch restrictions and existing refs:
- Issue receipt: EXECUTION_RECEIPT_V1 comment; PR links immutable code/CI evidence
- Close Issue only after all owning acceptance gates.

Read: skills/project-governance/references/issue-control.md and issue-execution-contract.md.
