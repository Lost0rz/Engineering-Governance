# Cross-context Card and receipt

A Card transports *task references and the current action*, not repository permissions. The task owner remains `project-governance`. The receiving host verifies live identity, actual writer authority and affected scope when an action requires them.

## Card fields

| Field | Meaning |
| --- | --- |
| `TASK_ID` | Stable selected task |
| `MODE` | `EXECUTE`, `AUDIT`, `REVIEW`, `VERIFY` or `DIAGNOSE` |
| `TARGET` | Repo/ref/Issue/PR or artifact target |
| `AUTHORITY` | Current task/decision locator and trust source |
| `BOUNDARY` | Read/write limits, relevant risk/effects and exclusions |
| `DELTA` | Current request, verified findings or remaining action |
| `RETURN_CONTRACT` | Outcome and decisive evidence expected |

`CAPABILITY` (selected Skill) and `CARD_ID` are useful optional metadata, not authorization. No separate form is needed when the same context can continue directly.

## Selecting evidence

A legacy approved Issue task references its selected Issue/revision and relevant Work Package. A direct current USER-directed G1/G2 task references the current authenticated instruction and bounded effect; a different host needs its own fresh authorization. A formal audit uses read-only mode and declares what claim/identity requires a verdict.

A handoff may link code, source findings, PR/CI state, screenshots and logs, but it does not need to reproduce them. Actual human UI acceptance remains an independently observed human decision.

## Receipt

Report `TASK_ID`, `MODE`, `TARGET`, `OUTCOME` and decisive `EVIDENCE` or blocker, plus the next unresolved action when material. Do not claim an unobserved PASS, installation, merge or permission change. Runtime model/tool settings come from the receiver's host, not the Card.
