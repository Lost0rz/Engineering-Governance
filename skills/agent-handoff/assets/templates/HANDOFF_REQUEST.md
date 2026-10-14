# Handoff Request

HANDOFF_ID: `<id>`
TASK_ID: `<same authorized task when purpose is unchanged>`
MODE: `EXECUTE | AUDIT | DIAGNOSE | REVIEW | VERIFY`

SOURCE_CONTEXT: `<optional: web/local/cloud/subagent/reviewer/session/machine>`
TARGET_CONTEXT: `<optional: web/local/cloud/subagent/reviewer/session/machine>`

## TARGET

<Immediate requested outcome. This does not replace CURRENT_TASK authorization.>

## AUTHORITY

- `<AGENTS.md / CURRENT_STATUS.md / CURRENT_TASK.md / accepted design/plan / repository or runtime authority>`

AUTHORITY_OBSERVED_BASIS: `<revision/observation/head | omit when immaterial>`

## DELTA

- `<Fresh fact/decision/focus not already represented safely in authority. Do not paste whole controls/rules here.>`

## BOUNDARY

- `<Read/write scope, selected workspace/identity when material, unique STOP conditions, external/destructive side-effect limits.>`

## RETURN_CONTRACT

- `<Mode-specific evidence required for the next decision.>`

### Mode hint

- `EXECUTE`: same-task mutation result + changed paths + checks + lifecycle/alignment.
- `AUDIT`: target/range + required claims + independence basis + findings/unknowns + verdict; read-only.
- `DIAGNOSE`: evidence/hypothesis/probe result + fix boundary under existing authorization.
- `REVIEW`: work-product findings + evidence; read-only.
- `VERIFY`: named claim + exact observation/identity + PASS/FAIL/UNKNOWN + proof boundary.

A change of Web/local/agent/session context alone does not require a new task. A materially different engineering purpose must be authorized/reconciled through Project Governance first.
