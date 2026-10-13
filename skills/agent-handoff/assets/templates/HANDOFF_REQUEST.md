# Handoff Request

HANDOFF_ID: `<id>`
MODE: `EXECUTE | AUDIT | DIAGNOSE | REVIEW | VERIFY`

## TARGET

<Immediate requested outcome. This does not replace CURRENT_TASK authorization.>

## AUTHORITY

- `<AGENTS.md / CURRENT_STATUS.md / CURRENT_TASK.md / durable plan / repository or runtime authority>`

## DELTA

- `<Fresh fact/decision/focus not already represented safely in authority. Do not paste whole controls/rules here.>`

## BOUNDARY

- `<Read/write scope, selected workspace/identity when material, unique STOP conditions, external/destructive side-effect limits.>`

## RETURN_CONTRACT

- `<Mode-specific evidence required for the next decision.>`

### Mode hint

- `EXECUTE`: mutation result + changed paths + checks + lifecycle/alignment.
- `AUDIT`: target/range + findings/unknowns + verdict; read-only.
- `DIAGNOSE`: evidence/hypothesis/probe result + fix boundary.
- `REVIEW`: work-product findings + evidence; read-only.
- `VERIFY`: named claim + exact observation/identity + PASS/FAIL/UNKNOWN + proof boundary.
