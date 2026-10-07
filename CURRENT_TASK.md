# CURRENT TASK — Phase D Incident Doctor Enrichment

Task ID: `EG-INCIDENT-DOCTOR-ENRICH-IMPL-016`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `BOUNDED_IMPLEMENTATION`

## Objective

Enrich the existing `skills/incident-doctor/` module so an AI can investigate a real evidence-insufficient failure with a hard evidence gate, minimum decision-linked probes, fresh-incident capture, falsifiable hypotheses, minimum-fix boundaries, regression verification, and explicit probe retirement/promotion — without turning diagnosis into routine development or a permanent observability platform.

This is the bounded implementation of the user-approved Phase D design. Do not re-plan or expand scope.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Phase B accepted merge head: `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- Phase C accepted merge head: `1d28250717e4e72754655ccc3c69bc3664a70eae`.
- User-approved Phase D design baseline before authorization: `7511ec8ac29a58adc3cea5b587f664c8a2faf4ae`.
- Authorized branch: `codex/incident-doctor-enrichment`.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- The exact implementation start SHA is the Web authorization commit from which the authorized task branch is created; the local execution card supplies that SHA and any mismatch is a STOP.

## In scope

Only these six reusable Skill files may be enriched:

- `skills/incident-doctor/SKILL.md`
- `skills/incident-doctor/references/evidence-gate.md`
- `skills/incident-doctor/references/probe-design.md`
- `skills/incident-doctor/references/fresh-incident.md`
- `skills/incident-doctor/references/probe-lifecycle.md`
- `skills/incident-doctor/assets/templates/INCIDENT.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change only for task handoff/control-state recording.

## Required design behavior

### 1. Evidence gate is a hard gate

Before any new probe or diagnostic instrumentation:

1. state the blocked question;
2. identify the real failure, unexplained behavior, or unsafe ambiguity that makes the question relevant;
3. review existing task context, source, tests, runtime/build/configuration identity, state, logs, and other available evidence;
4. decide whether existing evidence is sufficient for the next safe decision.

If current evidence is sufficient, document that evidence and bypass new probe work. Do not add instrumentation merely to make diagnostics feel more complete.

If evidence is insufficient, name the exact missing fact and the decision it blocks before designing a probe.

### 2. Evidence categories must remain distinct

Guidance and template must keep these separate:

- user-reported symptom;
- direct observation;
- interpretation;
- hypothesis;
- falsification result;
- finding;
- root-cause claim.

Do not collapse a symptom or correlation into a causal conclusion. Root cause remains `UNKNOWN` until evidence supports a stronger claim.

### 3. Probe design must be minimum and decision-linked

A probe is justified only when it can close the named evidence gap or distinguish current plausible explanations.

For each probe record:

- the missing fact;
- competing explanations or hypotheses;
- the observation that would support or weaken each one;
- the next decision for each material result;
- why existing evidence cannot already answer the question.

Prefer canonical/read-only evidence. Do not change product behavior under the label of diagnosis. Do not add broad or permanent instrumentation without separate justification.

### 4. Fresh incident capture must preserve identity

After a new probe is introduced, important conclusions should come from a fresh, attributable incident or reproduction rather than mixing incompatible historical captures.

Record the smallest relevant observation window plus, when applicable:

- repository revision;
- build/application/runtime identity;
- process identity;
- configuration identity;
- request/data/session identity relevant to the incident;
- observation timestamps and required clock basis.

Keep user report, direct observation, and inference separate.

### 5. Hypotheses must be falsifiable

Each active hypothesis must state what observation would weaken or falsify it. Prioritize discriminating evidence over plausibility narratives. A hypothesis does not become root cause merely because it appears most likely.

If evidence remains insufficient after the available safe probes, preserve the unresolved state rather than inventing certainty.

### 6. Fix boundary must follow evidence

Incident Doctor does not authorize broad redesign.

Only after evidence supports a causal boundary may the task define the smallest authorized behavior change needed to address it. The fix must then receive risk-proportional regression verification under the normal project-governance verification policy.

If only correlation is established, keep the fix boundary unresolved unless separately authorized for another reason.

### 7. Probe lifecycle is explicit

Every diagnostic probe is classified as temporary or durable.

Temporary probes are retired/removed after their evidence is captured and verified unless a separate reason justifies retention.

Promotion to durable diagnostics requires:

- repeated evidence of continuing value;
- explicit owner;
- explicit scope;
- separate authorization.

A one-time incident must not silently create permanent observability work.

### 8. Incident template is an evidence chain, not a diary

`INCIDENT.md` must support at least:

- Incident ID;
- blocked question;
- root-cause status;
- user-reported symptom;
- verified runtime/context identity;
- existing evidence;
- evidence gap;
- hypotheses;
- falsification criteria/results;
- minimum probe, if needed;
- fresh reproduction/capture;
- findings with direct observations separated from inference;
- minimum fix boundary;
- regression verification;
- probe retirement/promotion decision;
- unresolved unknowns.

Keep the template concise enough for real use.

## Out of scope

Do not:

- modify reusable content under `skills/project-governance/` or `skills/domain-navigation/`;
- add a fourth Skill;
- add executable scripts/runtime code/package dependencies;
- build a diagnostic CLI, service, daemon, database, telemetry platform, background monitor, central log system, or automated remediation framework;
- add broad speculative observability or permanent instrumentation by default;
- modify product/business code;
- run a real-project incident adoption/validation exercise in this task;
- redefine project verification tiers;
- modify or move the historical `v0.1.0` tag;
- merge the task branch.

## Verification level

`V0 — Skill/documentation contract enrichment`.

Required verification:

- reusable changes are limited to the six authorized `incident-doctor` files;
- root-control changes are handoff-only;
- `SKILL.md` frontmatter remains valid and the reactive trigger/boundary is explicit;
- all relative Markdown links resolve;
- evidence-gate, probe-design, fresh-incident, probe-lifecycle, and template semantics are internally consistent;
- `skills/project-governance/` and `skills/domain-navigation/` remain byte-for-byte unchanged from task start;
- no executable source, dependency manifest, diagnostic runtime/platform, database, daemon, or generated binary is introduced;
- exactly three top-level Skills remain;
- task branch is clean and local/remote matched at handoff.

Do not run a historical runtime test suite; Phase D changes no runtime behavior.

## Acceptance criteria

A fresh AI reading the target repository plus `incident-doctor` should be able to determine, without inventing facts:

- whether Doctor should trigger at all;
- whether existing evidence is already sufficient;
- what precise fact is missing when evidence is insufficient;
- how to design the minimum discriminating probe;
- how to capture a fresh attributable incident;
- how to keep symptom, observation, interpretation, hypothesis, finding, and root-cause claim separate;
- how to falsify hypotheses rather than accumulate plausible narratives;
- when a minimum behavior fix is evidence-supported;
- how to verify that fix proportionally;
- when a probe must be retired versus separately promoted.

The result must improve incident reasoning without creating a standing diagnostics program.

## STOP conditions

STOP and return evidence without improvising if:

- live `origin/main` or the authorized branch start SHA differs from the execution card;
- the local canonical checkout or chosen worktree contains unpreserved unique work;
- completing the approved design requires changing a reusable file outside the six authorized `incident-doctor` paths;
- any change to `project-governance` or `domain-navigation` appears necessary;
- implementation would require executable code, dependencies, a diagnostic runtime/platform, or real-project adoption work;
- a material requirement is ambiguous enough that proceeding would invent policy outside the approved design;
- the stable tag target changes;
- remote/control authority drifts during execution in a way that changes task scope.

## Handoff requirements

Before returning to Web:

- set state to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`;
- record `START_HEAD`, `FINAL_HEAD`, `REMOTE_HEAD`, and local/remote match;
- record exact reusable changed paths and root-control changed paths;
- record `V0` checks and intentionally omitted checks;
- confirm sibling reusable Skills unchanged;
- confirm no executable/runtime/dependency/diagnostic-platform surface added;
- confirm exactly three top-level Skills remain;
- confirm stable tag target unchanged;
- leave the task worktree clean;
- push only `codex/incident-doctor-enrichment`;
- do not merge.

## Execution evidence

- `START_HEAD`: `ae56617dbb3dca6815ccdaaee8b3b7dd0213e4ee`.
- `FINAL_HEAD`: this handoff-control commit; its exact SHA is recorded in the verified post-push executor receipt because a commit cannot contain its own SHA.
- `REMOTE_HEAD`: verified equal to `FINAL_HEAD` after push; exact SHA is in the post-push executor receipt.
- `LOCAL_REMOTE_MATCH`: `YES` after final push verification.
- `WORKING_TREE`: `CLEAN` after final push verification.
- `REMOTE_MAIN`: `ae56617dbb3dca6815ccdaaee8b3b7dd0213e4ee` at final pre-push fetch.
- `REUSABLE_CHANGED_PATHS`:
  - `skills/incident-doctor/SKILL.md`
  - `skills/incident-doctor/references/evidence-gate.md`
  - `skills/incident-doctor/references/probe-design.md`
  - `skills/incident-doctor/references/fresh-incident.md`
  - `skills/incident-doctor/references/probe-lifecycle.md`
  - `skills/incident-doctor/assets/templates/INCIDENT.md`
- `ROOT_CONTROL_CHANGED_PATHS`: `CURRENT_STATUS.md`, `CURRENT_TASK.md` (handoff only).
- `PROJECT_GOVERNANCE_CHANGED`: `NO`.
- `DOMAIN_NAVIGATION_CHANGED`: `NO`.
- `TOP_LEVEL_SKILL_COUNT`: `3`.
- `EXECUTABLE_RUNTIME_ADDED`: `NO`.
- `DEPENDENCY_ADDED`: `NO`.
- `DIAGNOSTIC_PLATFORM_ADDED`: `NO`.
- `AUTOMATIC_REMEDIATION_ADDED`: `NO`.
- `STABLE_TAG_TARGET`: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- `V0_CHECK_RESULTS`: `PASS` — exact six-file reusable allowlist plus two handoff-only root controls; no added/deleted/renamed paths; `git diff --check` clean; sibling Skills diff exit 0; frontmatter and all five required `SKILL.md` links valid; all six module links resolve; evidence taxonomy and required INCIDENT fields/context identities checked; exactly three top-level Skills; no executable, dependency, diagnostic platform, database, daemon, or generated-binary path added. Historical runtime suite and real-project incident adoption not run because this documentation-only task is authorized at V0.
- `SCOPE_EXPANSION`: `NO`.
- `FINAL_STATE`: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Current stop point

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`
