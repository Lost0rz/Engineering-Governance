# Handoff Receipt

A Receipt reports the actual result/evidence of one Card. It is transport/evidence, not project authority.

## Required core

Every structured Receipt starts with:

```text
CARD_ID: <source card id>
TASK_ID: <authorized task id>
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
CAPABILITY: <Engineering Governance Skill actually requested | NONE>
TARGET: <card target>
OUTCOME: <mode-appropriate result>
```

Then add only mode-relevant evidence. Do not restate the full task contract.

## EXECUTE

```text
START_IDENTITY: <identity>
FINAL_IDENTITY: <identity>
CHANGED_PATHS: <paths | NONE>
VERIFICATION: <checks + results>
LIFECYCLE: <branch/PR/workspace effects | NONE>
UNRESOLVED: <NONE | evidence/blocker>
CONTROL_ALIGNMENT: <PASS | NEEDS_RECONCILIATION | NOT_APPLICABLE>
NEXT_SAFE_ACTION: <next decision/action>
```

`EXECUTE` does not permit mutation beyond the Card/task authority. Legitimate no-change execution should report `CHANGED_PATHS: NONE` explicitly.

## AUDIT / REVIEW

```text
OBSERVED_IDENTITY_OR_RANGE: <identity/range>
EVIDENCE_OR_FINDINGS: <evidence-backed result>
UNKNOWN: <NONE | unverified claim/gap>
VERDICT: <PASS | PASS_WITH_FOLLOWUPS | STOP | UNKNOWN as applicable>
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION: <next decision/action>
```

If formal Evidence Audit was requested, `CAPABILITY` should identify `evidence-audit`. `MODE: AUDIT` alone is only the read-only action class.

## VERIFY

```text
CLAIM: <named proposition/check>
OBSERVED_IDENTITY: <identity>
RESULT: PASS | FAIL | UNKNOWN
EVIDENCE: <what was observed>
PROVES: <supported boundary>
DOES_NOT_PROVE: <important non-covered boundary>
NEXT_SAFE_ACTION: <next decision/action>
```

## DIAGNOSE

Keep diagnosis read-only unless the Card used `MODE: EXECUTE` for an authorized probe. Report only decision-linked evidence, for example:

```text
OBSERVED_IDENTITY: <identity/runtime>
MISSING_FACT_OR_QUESTION: <fact/question>
EVIDENCE_OR_HYPOTHESIS: <result>
UNKNOWN: <NONE | unresolved gap>
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION: <next decision/action>
```

Changing execution context does not imply a task change. Report a different `TASK_ID` only when Project Governance actually authorized/reconciled a distinct engineering purpose.
