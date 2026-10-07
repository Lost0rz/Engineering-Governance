# CURRENT TASK — Doctor Foundation Implementation Plan Corrective

Task ID: `EG-V01-DOCTOR-FOUNDATION-PLAN-003`

State: `ACTIVE — PLAN CORRECTIVE AFTER WEB REVIEW`

Mode: `PLAN_CORRECTIVE_ONLY`

## Objective

Correct the Doctor foundation implementation plan after independent Web review. Preserve the accepted first-slice scope and tooling design. This task remains planning-only and does not authorize executable implementation.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Branch: `codex/eg-v01-doctor-foundation-plan`.
- Stacked PR: #3, OPEN / DRAFT / UNMERGED, base `codex/eg-v01-tooling-design`.
- Executor plan handoff reviewed by Web: `781428ccaea258cbe3f4723ab1aeb82a208eda1e`.
- Accepted design control head: `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`.
- Accepted design spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.

## Required corrective

### MAJOR 1 — TDD sequencing must permit genuine RED → GREEN

The current plan makes Task 2 implement the Git command allowlist, then Task 5 asks for new prohibited-command tests (`fetch` / `remote` / `ls-remote`) to fail first. If Task 2 is implemented correctly, those Task 5 tests should already pass.

Correct the task ordering so every implementation task that claims TDD has a behavior that is genuinely absent before its RED step. Acceptable approaches include:

- move the prohibited-command negative tests into Task 2 before allowlist implementation, and make the final no-mutation phase a separate acceptance/verification gate rather than a fake implementation RED; or
- move the end-to-end no-mutation acceptance tests into the Doctor orchestration task before `run_doctor` exists, then keep a final verification-only gate with no implementation commit.

Do not invent an artificial defect merely to manufacture RED. The final structure may have fewer implementation commits if that is the cleaner truthful plan.

### MAJOR 2 — Freeze exact test names and key assertions

The plan currently says "write tests for ..." but does not identify the exact test functions/methods and the assertions that define success.

For each implementation task, add a concise named test matrix or equivalent step detail containing:

- exact `test_*` names;
- the key input/setup;
- the key assertions/result values that pin the contract;
- the focused RED command and expected reason for failure;
- the same GREEN command after minimal implementation.

Do not transcribe full production code. Keep the plan proportional, but make it executable by a fresh implementer without inventing the test surface.

### MAJOR 3 — Define deterministic task-ID reference matching

Replace the ambiguous phrase "the exact parsed task ID must occur as a whole token in the status text" with one exact matching rule.

The rule must define what counts as a boundary around task IDs containing characters such as letters, digits, hyphens, underscores, dots, or slashes as applicable, and must include tests for at least:

- exact intended reference → match;
- same ID inside backticks or ordinary prose → match if intended by the rule;
- prefix/suffix collision such as `TASK-1` versus `TASK-10` → no match;
- embedded alphanumeric/identifier text → no false match;
- missing exact reference → deterministic consistency `FAIL`, not command STOP.

Keep this a narrow deterministic text rule; do not introduce a Markdown parser or machine-readable schema.

## Preserved scope

Keep unchanged unless directly needed to resolve the three findings:

- first slice only: shared local reader/model + local read-only Doctor;
- macOS Apple silicon, Python 3.11+, standard library only;
- offline/local default;
- no third-party runtime dependencies;
- immutable/versioned Doctor base report;
- exit `0` truthful report / `2` classified fatal STOP / `3` internal fatal failure;
- no Bootstrap, deeper Audit, AI runtime/composition, remote query, MCP, daemon, enforcement, migration/remediation, pilot changes, packaging, CLI, or schema implementation.

Do not change the accepted tooling spec or `EngineeringGovernanceStandard 0.1.0` unless a direct contradiction is discovered; if so, STOP and report it instead.

## Allowed changes

Only:

- `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`
- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`

No source, tests, fixtures, manifests, schemas, skills, templates, check registries, or executable implementation may be created in this corrective.

## Validation and handoff

After correcting the plan:

1. re-run the writing-plans self-review for spec coverage, step granularity, interface/type consistency, Review Focus coverage, and proportion;
2. explicitly verify every implementation task has a truthful RED condition before its implementation step;
3. verify every planned test has an exact name and key assertion surface;
4. verify the task-ID matching rule is deterministic and has boundary/false-positive tests;
5. update `CURRENT_STATUS.md` and set this task back to `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`;
6. commit/push the same plan branch;
7. keep PR #3 Draft/unmerged and verify local/remote HEAD equality plus clean worktree;
8. return the receipt below.

Required receipt:

```text
TASK_ID:
CONTROL_START_HEAD:
FINAL_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:

MAJOR_1_TDD_SEQUENCE_RESOLVED:
MAJOR_2_EXACT_TEST_SURFACE_RESOLVED:
MAJOR_3_TASK_ID_MATCH_RULE_RESOLVED:
IMPLEMENTATION_TASK_COUNT:
VERIFICATION_ONLY_GATE_PRESENT:
ALL_IMPLEMENTATION_TASKS_HAVE_GENUINE_RED:
TEST_NAMES_AND_KEY_ASSERTIONS_FROZEN:
TASK_ID_BOUNDARY_TESTS_DEFINED:

FIRST_SLICE_ONLY: YES
THIRD_PARTY_DEPENDENCIES_PLANNED: NO
IMPLEMENTATION_STARTED: NO
ACCEPTED_SPEC_CHANGED: NO
STANDARD_CHANGED: NO

CHANGED_PATHS:
PR_STATE:
FINAL_STATE: WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW | STOP
STOP_REASON:
```

STOP on unexpected remote-head drift, unknown local work, third-party dependency need, scope expansion, executable implementation, or any newly discovered contradiction with the accepted spec/standard.
