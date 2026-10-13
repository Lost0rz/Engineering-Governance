# Handoff Receipt

Use the profile matching `MODE`. Do not fill irrelevant fields merely for ceremony.

## State-changing / EXECUTE

HANDOFF_ID: `<id>`
MODE: `EXECUTE`
TASK_ID: `<task>`
SKILLS_USED: `<actual Skills used>`
OUTCOME: `PASS | PARTIAL | STOP`
START_IDENTITY: `<identity>`
FINAL_IDENTITY: `<identity>`
CHANGED_PATHS: `<paths | NONE>`
VERIFICATION: `<checks + results>`
LIFECYCLE: `<branch/PR/worktree effects | NONE>`
UNRESOLVED: `<NONE | evidence/blocker>`
RELATED_DOCUMENT: `<path | NONE>`
DOCUMENT_ALIGNMENT: `UPDATED | UNCHANGED | NOT_APPLICABLE`
CURRENT_STATUS_RECONCILIATION: `UPDATED | UNCHANGED`
CURRENT_TASK_RECONCILIATION: `UPDATED | UNCHANGED`
CONTROL_ALIGNMENT: `PASS | NEEDS_RECONCILIATION`
NEXT_SAFE_ACTION: `<next decision/action>`

## Read-only / AUDIT | REVIEW | VERIFY | DIAGNOSE

HANDOFF_ID: `<id>`
MODE: `<mode>`
TARGET: `<claim/work product/question>`
OBSERVED_IDENTITY: `<identity>`
EVIDENCE_RANGE: `<range/source>`
SKILLS_USED: `<actual Skills used>`
FINDINGS_OR_OBSERVATION: `<evidence-backed result>`
UNKNOWN_OR_UNVERIFIED: `<NONE | details>`
CI_TEST_HOST_EVIDENCE: `<relevant evidence | N/A>`
CONTROL_ALIGNMENT_OBSERVATION: `MATCH | STALE | UNKNOWN | NOT_APPLICABLE`
CONTROL_MUTATION: `NOT_AUTHORIZED_READ_ONLY`
VERDICT_OR_RESULT: `PASS | PASS_WITH_FOLLOWUPS | STOP | FAIL | UNKNOWN`
NEXT_SAFE_ACTION: `<next decision/action>`
