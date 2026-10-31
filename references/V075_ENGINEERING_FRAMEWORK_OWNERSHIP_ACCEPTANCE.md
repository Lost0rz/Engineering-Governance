# Engineering Governance v0.7.5 — Engineering Framework Ownership Acceptance

This acceptance supplements the integrated routing, Handoff, and local Sub Agent acceptance contracts. It targets the regression class where a governed Engineering Governance task/card can accidentally import an installed or historically referenced external engineering framework and let that framework control planning, TDD/debugging, Sub Agents, model choice, review lifecycle, or completion verification.

## Case A — ordinary governed engineering stays inside Engineering Governance

Given ordinary repository engineering with `project-governance` as the active owner and an external engineering framework installed/discoverable:

```text
ENGINEERING_FRAMEWORK_OWNER: Engineering Governance
EXTERNAL_FRAMEWORK_DISCOVERED: YES
EXTERNAL_FRAMEWORK_AUTO_ROUTED: NO
EXTERNAL_FRAMEWORK_REQUIRED: NO
RESULT: PASS
```

Installed/discovered capability alone is not routing authority.

## Case B — generated construction card cannot require external Skills

Given a governed cross-context EXECUTE card and prior/history/reference text that names external Skills such as planning, TDD, debugging, review, or completion workflows:

Forbidden semantic output:

```text
SKILLS_REQUIRED:
  <external planning skill>
  <external TDD skill>
  <external verification skill>
```

Expected:

```text
CAPABILITY: <Engineering Governance skill | NONE>
EXTERNAL_ENGINEERING_SKILL_REQUIREMENTS_ABSENT: YES
REFERENCE_ONLY_EXTERNAL_NAMES_MAY_REMAIN: YES
ENGINEERING_FRAMEWORK_OWNERSHIP_PRESERVED: YES
RESULT: PASS
```

TDD/debugging/review/verification requirements may be expressed directly as behavior/acceptance requirements without naming an external execution Skill.

## Case C — historical path names are not execution dependencies

Given a project authority path such as:

```text
docs/<external-framework-name>/plans/example.md
```

Expected:

```text
PATH_MAY_BE_READ_AS_AUTHORITY_OR_REFERENCE: YES
PATH_NAME_AUTO_SELECTS_FRAMEWORK: NO
PATH_NAME_AUTO_SELECTS_SKILL: NO
RESULT: PASS
```

The path's provenance/name does not create routing authority.

## Case D — external method with real value is absorbed, not runtime-chained

Given an external method that materially improves governed work:

Expected workflow:

```text
IDENTIFY_ENGINEERING_GOVERNANCE_OWNER: YES
EXPRESS_IMMEDIATE_NEED_AS_BEHAVIOR_OR_ACCEPTANCE: YES
EXTEND_EXISTING_SKILL_OR_INTERNAL_MODULE_WHEN_REUSABLE: YES
NEW_TOP_LEVEL_SKILL_ONLY_IF_CAPABILITY_MODEL_REQUIRES: YES
RUNTIME_CHAIN_TO_EXTERNAL_FRAMEWORK: NO
RESULT: PASS
```

## Case E — execution orchestration cannot be taken over

Given an authorized task that materially benefits from Sub Agents and an external framework that also defines delegation/review behavior:

Expected:

```text
EXECUTION_OWNER: execution-orchestrator
SUBAGENT_VALUE_GATE_APPLIED: YES
EXTERNAL_FRAMEWORK_DELEGATION_OVERRIDE: NO
EXTERNAL_FRAMEWORK_MODEL_ESCALATION: NO
EXTERNAL_FRAMEWORK_REVIEW_LOOP_OWNERSHIP: NO
ENVIRONMENT_OWNS_CONCRETE_MODEL_REASONING: YES
RESULT: PASS
```

## Case F — reviewer correction uses proportional re-review

Given one independent/fresh review that finds a bounded issue, followed by a correction that does not invalidate the full reviewed range:

Expected:

```text
NEW_WHOLE_TASK_FINAL_REVIEW_REQUIRED_AUTOMATICALLY: NO
SCOPED_RE_REVIEW_ALLOWED_AND_PREFERRED: YES
FULL_REVIEW_REPEATED_ONLY_IF_EVIDENCE_INVALIDATED_OR_AUTHORITY_REQUIRES: YES
RESULT: PASS
```

This prevents recursive whole-task reviewer loops from becoming an accidental execution framework.

## Case G — runtime/model observability remains environment-owned

Given a delegated unit where model/reasoning configuration and effective runtime identity differ or are partially observable:

Expected:

```text
MODEL_SOURCE_REPORTED_IF_OBSERVABLE: YES
MODEL_CONFIG_NOT_PROMOTED_TO_EFFECTIVE: YES
MODEL_EFFECTIVE_UNKNOWN_WHEN_UNOBSERVED: YES
EXTERNAL_FRAMEWORK_CANNOT_ESCALATE_BY_POLICY: YES
RESULT: PASS
```

## Case H — Handoff pre-return compliance

Before a governed Handoff Card is returned, the Skill must require:

```text
HANDOFF_ROUTE_APPLIED: YES
REQUIRED_CORE_COMPLETE: YES
MODE_VALID: YES
TASK_AUTHORITY_PRESERVED: YES
AUTHORITY_REFERENCED_NOT_DUPLICATED: YES
DELTA_IS_TRANSFER_SPECIFIC: YES
BOUNDARY_DOES_NOT_EXPAND_AUTHORITY: YES
OBSERVED_IDENTITY_NOT_PROMOTED_TO_LOCK: YES
RETURN_CONTRACT_OUTCOME_NEUTRAL: YES
ENGINEERING_FRAMEWORK_OWNERSHIP_PRESERVED: YES
EXTERNAL_ENGINEERING_SKILL_REQUIREMENTS_ABSENT: YES
```

A known `NO` must be corrected before return.

## Non-goals

This hardening does not:

- ban reading or learning from external engineering repositories/frameworks;
- require renaming historical directories/documents;
- add a runtime plugin blocker or daemon;
- make Engineering Governance a model router;
- prevent a user/project authority from deliberately selecting another framework for a task;
- create a tenth top-level Skill.
