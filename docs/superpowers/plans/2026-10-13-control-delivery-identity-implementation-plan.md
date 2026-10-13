# Control Delivery Identity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Project Governance distinguish control-only Repository HEAD movement from Delivery / Semantic HEAD changes so control records remain authoritative without causing CI/audit/merge/closeout churn.

**Architecture:** Keep the existing three-Skill architecture and modify only the declarative Project Governance contracts/templates plus this repository's dogfooding rule. `control-identity.md` becomes the semantic authority for Repository HEAD vs Delivery / Semantic HEAD and change classification; verification, control-plane, development-flow, workspace-lifecycle, and templates consume that distinction consistently. No new runtime, daemon, hook, database, installer, or fourth Skill is added.

**Tech Stack:** Markdown Agent Skills, Git/GitHub evidence, repository control files.

**Spec:** `docs/superpowers/specs/2026-10-13-control-delivery-identity-design.md`

## Global Constraints

- Exclude exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md` from Delivery / Semantic HEAD by default.
- Do not claim literal Git `HEAD` stays unchanged after a control-only commit.
- Preserve `CURRENT_TASK.md` as authoritative for scope and permission.
- A mixed commit containing any non-control path is `DELIVERY_HEAD_CHANGE`.
- `AGENTS.md` is not excluded.
- Real source/config/test/schema/workflow/dependency/migration/runtime-relevant changes still invalidate implementation evidence when appropriate.
- Do not add governance runtime machinery merely for this rule.
- Do not republish or mutate `plugin-v0.5.3` as part of this source task.

## Review Focus

1. **Mixed commit:** `CURRENT_STATUS.md` plus source/config/test/workflow change must classify as `DELIVERY_HEAD_CHANGE`, never control-only.
2. **Authorization mutation:** a material `CURRENT_TASK.md` scope/acceptance/STOP change must be obeyed before further mutation even though the commit is not application-code identity.
3. **Explicit literal lock:** a task that explicitly declares literal Repository HEAD equality must still enforce that lock; semantic equivalence must not silently override it.
4. **Exclusion creep:** `AGENTS.md`, workflow, tests, schemas, migrations, manifests, runtime config, source, and governance implementation must remain delivery/governance-relevant.
5. **Closeout reuse:** a task workspace already proven terminal/closed must not be reopened solely because main advanced via control-only records.

---

### Task 1: Lock the RED baseline and classification authority

**Files:**
- Read: `skills/project-governance/references/control-identity.md`
- Read: `skills/project-governance/references/verification-tiers.md`
- Read: `skills/project-governance/references/control-plane.md`
- Read: `skills/project-governance/references/workspace-lifecycle.md`
- Read: `skills/project-governance/references/development-flow.md`
- Reference: `docs/superpowers/specs/2026-10-13-control-delivery-identity-design.md`

**Interfaces:**
- Consumes: task baseline `1a450aacb301e7c5a25dd88d17749911536d989c` and the five required scenarios in the spec.
- Produces: explicit before-change RED evidence for A/B/C and preserved guard evidence for D/E; no reusable-source mutation yet.

- [ ] **Step 1: Re-read the exact task-branch source before implementation**

Verify the task branch still descends from `1a450aacb301e7c5a25dd88d17749911536d989c` and that no unplanned reusable-source edits are present.

- [ ] **Step 2: Demonstrate Scenario A is RED**

Confirm `verification-tiers.md` currently states that a post-freeze status/task/documentation commit changes the identity being verified. Record the finding as: `A=RED_CONTROL_ONLY_COMMIT_INVALIDATES_LITERAL_EXACT_HEAD`.

- [ ] **Step 3: Demonstrate Scenario B is missing/ambiguous**

Confirm `workspace-lifecycle.md` lacks an explicit rule that a later main advance limited to `CURRENT_STATUS.md` / `CURRENT_TASK.md` is non-blocking after verified closeout. Record: `B=RED_NO_CONTROL_ONLY_CLOSEOUT_GUARD`.

- [ ] **Step 4: Demonstrate Scenario C is overly eager**

Confirm `control-plane.md` / `development-flow.md` can require lifecycle reconciliation before the next state-changing task without allowing the safe single-transition pattern that both reconciles Task A and authorizes Task B. Record: `C=RED_INTERMEDIATE_CONTROL_TRANSITION_CAN_BE_REQUIRED`.

- [ ] **Step 5: Verify guard scenarios D/E already exist and must not regress**

Record that implementation-relevant drift remains invalidating and material `CURRENT_TASK.md` semantics remain authoritative.

- [ ] **Step 6: Do not commit reusable-source changes until Steps 2-5 are evidenced**

Expected result: at least A/B/C fail the desired contract for the expected reason; D/E are explicit regression guards.

---

### Task 2: Define Repository HEAD vs Delivery / Semantic HEAD once

**Files:**
- Modify: `skills/project-governance/references/control-identity.md`
- Modify: `skills/project-governance/SKILL.md`
- Modify: `AGENTS.md`
- Modify: `skills/project-governance/assets/templates/AGENTS.md`
- Modify: `skills/project-governance/assets/templates/CURRENT_STATUS.md`
- Modify: `skills/project-governance/assets/templates/CURRENT_TASK.md`

**Interfaces:**
- Consumes: RED evidence and design terminology.
- Produces: one canonical classification contract consumed by later verification/lifecycle references.

- [ ] **Step 1: Extend `control-identity.md` with the two-head model**

Add explicit definitions for `Repository HEAD` and `Delivery / Semantic HEAD`. State that semantic identity excludes exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md`.

- [ ] **Step 2: Add change classifications to `control-identity.md`**

Define `CONTROL_ONLY_CHANGE`, `CONTROL_ONLY_DRIFT`, `DELIVERY_HEAD_CHANGE`, and `SEMANTIC_TREE_EQUIVALENCE`. State that any mixed commit containing a non-control path is `DELIVERY_HEAD_CHANGE`.

- [ ] **Step 3: Refine SHA/equality semantics**

State that SHAs recorded in status/task are provenance/audit anchors by default. Equality locks must be explicit and identify whether they lock semantic implementation identity or literal Repository HEAD; default implementation locks to semantic identity unless literal equality is explicitly required.

- [ ] **Step 4: Preserve authorization authority**

State that control-only classification never weakens `CURRENT_TASK.md` content authority. A material task-content change must be read and obeyed before further mutation.

- [ ] **Step 5: Update `SKILL.md` to consume the classification**

Replace wording that treats every control commit as an exact-head identity change. Route implementation freshness and exact-head decisions through `control-identity.md` semantic equivalence while preserving material task reconciliation.

- [ ] **Step 6: Dogfood the rule in root `AGENTS.md`**

Add the durable repository rule that status/task-only drift is non-blocking for delivery identity while `AGENTS.md` itself remains governance-relevant. Do not add `AGENTS.md` to the excluded set.

- [ ] **Step 7: Update templates**

Make `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` templates avoid implying that recorded control SHAs are current implementation equality locks. Add concise guidance for semantic-vs-literal locks where useful; do not duplicate the full reference contract.

- [ ] **Step 8: Focused consistency check**

Verify all preferred terms are used consistently and no file claims control-only commits leave literal Git HEAD unchanged.

- [ ] **Step 9: Commit the identity authority slice**

Commit message: `feat: separate control records from delivery identity`

---

### Task 3: Make exact-head, CI, review, and merge evidence semantic-tree aware

**Files:**
- Modify: `skills/project-governance/references/verification-tiers.md`
- Modify: `skills/project-governance/references/control-plane.md`

**Interfaces:**
- Consumes: `control-identity.md` classifications from Task 2.
- Produces: verification and merge-readiness behavior that reuses evidence across control-only Repository HEAD advances.

- [ ] **Step 1: Change final-head freeze semantics in `verification-tiers.md`**

Define the frozen implementation candidate using Delivery / Semantic HEAD or semantic-tree equivalence unless the task explicitly requires literal Repository HEAD equality.

- [ ] **Step 2: Preserve evidence across control-only advances**

State that CI/review/audit/mergeability evidence remains valid when only status/task changed later, semantic tree equivalence passes, no implementation-relevant authority changed, and no task requirement invalidates the tested implementation.

- [ ] **Step 3: Keep real drift invalidating**

Explicitly state that source/config/test/workflow/schema/migration/dependency/runtime-relevant changes are `DELIVERY_HEAD_CHANGE` and require fresh evidence when the existing verification contract says so.

- [ ] **Step 4: Remove evidence-only control-loop implications**

Retain the prohibition on commits created solely to write `CI PASS`, `audit PASS`, `ready to merge`, or equivalent evidence states, but stop describing all status/task commits as necessarily invalidating the implementation identity.

- [ ] **Step 5: Update `control-plane.md` ownership/cadence**

State that controls remain authoritative for owned semantics but external evidence does not require immediate writeback. Add lazy/batched post-merge reconciliation and the safe next-task single-transition pattern.

- [ ] **Step 6: Focused scenario check**

A must now classify as `CONTROL_ONLY_DRIFT`; D must still classify as `DELIVERY_HEAD_CHANGE`; E must still require reading/obeying changed authorization.

- [ ] **Step 7: Commit the verification slice**

Commit message: `feat: preserve verification across control-only drift`

---

### Task 4: Prevent lifecycle and task-start loops

**Files:**
- Modify: `skills/project-governance/references/workspace-lifecycle.md`
- Modify: `skills/project-governance/references/development-flow.md`

**Interfaces:**
- Consumes: semantic identity and verification contracts from Tasks 2-3.
- Produces: lifecycle/startup behavior that does not reopen closed work or demand intermediate closeout commits.

- [ ] **Step 1: Add the closeout non-reopen rule**

In `workspace-lifecycle.md`, state that a later main advance limited to control records is non-blocking after terminal workspace closeout and must not require a second cleanup cycle.

- [ ] **Step 2: Keep unique-work and writer safeguards unchanged**

Ensure the new rule does not bypass dirty/local-only work preservation, unresolved predecessor writers, storage authority, or other existing local evidence requirements.

- [ ] **Step 3: Update task-start flow**

In `development-flow.md`, require reading controls and fresh repository evidence, then classify any revision difference with `control-identity.md`. A control-only difference does not trigger HEAD-drift STOP or a fresh construction branch by itself.

- [ ] **Step 4: Add lazy next-task reconciliation**

Allow one control transition at the next meaningful planning boundary to reconcile the prior accepted task and authorize the next task when live evidence supports both.

- [ ] **Step 5: Preserve material authorization changes**

State that if the content of `CURRENT_TASK.md` materially changes the active contract, the new authorization must be obeyed even though semantic implementation identity is unchanged.

- [ ] **Step 6: Focused scenario check**

B must keep lifecycle closed; C must allow one next-task reconciliation; D/E must remain safe.

- [ ] **Step 7: Commit the lifecycle slice**

Commit message: `feat: avoid lifecycle loops from control-only commits`

---

### Task 5: Cross-contract acceptance and handoff

**Files:**
- Review all files modified in Tasks 2-4.
- Update root `CURRENT_STATUS.md` / `CURRENT_TASK.md` only if their owned semantics materially require a pre-freeze task handoff update; do not write external CI/audit outcomes merely to record them.

**Interfaces:**
- Consumes: completed semantic, verification, and lifecycle slices.
- Produces: one internally consistent source candidate ready for independent Web audit and later release authorization.

- [ ] **Step 1: Run the five scenario audit end-to-end**

Expected outcomes:

```text
A: CONTROL_ONLY_DRIFT -> no CI/audit restart
B: LIFECYCLE_STATE remains closed -> no second cleanup
C: prior-task reconciliation + next-task authorization may be one control transition
D: DELIVERY_HEAD_CHANGE -> exact-head evidence invalidated when appropriate
E: changed task content remains authoritative -> read/obey before mutation
```

- [ ] **Step 2: Audit the exact exclusion boundary**

Verify only `CURRENT_STATUS.md` and `CURRENT_TASK.md` receive the default delivery-identity exclusion. Confirm `AGENTS.md`, workflows, tests, schemas, migrations, dependency manifests, runtime config, source, and governance implementation are not excluded.

- [ ] **Step 3: Audit mixed commits and explicit locks**

Confirm mixed control+implementation commits are delivery changes and explicit literal Repository HEAD locks remain enforceable.

- [ ] **Step 4: Audit terminology**

Confirm the reusable source consistently uses the preferred terms: `Repository HEAD`, `Delivery / Semantic HEAD`, `CONTROL_ONLY_CHANGE`, `CONTROL_ONLY_DRIFT`, `DELIVERY_HEAD_CHANGE`, `SEMANTIC_TREE_EQUIVALENCE`.

- [ ] **Step 5: Inspect the complete diff**

Ensure there is no fourth Skill, runtime service, hook, daemon, database, installer, remediation mechanism, or unrelated governance expansion.

- [ ] **Step 6: Reconcile controls before exact-head freeze only if materially required**

If task-owned semantics need a final pre-freeze update, make it before choosing the final implementation candidate. Do not create a later commit merely to memorialize CI/review/audit results.

- [ ] **Step 7: Freeze the implementation candidate and open/update a Draft PR**

The PR must identify the exact implementation candidate and summarize RED evidence, changed contracts, acceptance scenarios, and any remaining limits. External CI/review/audit evidence should bind to the semantic implementation candidate; later control-only Repository HEAD movement must be classified rather than automatically invalidating it.

- [ ] **Step 8: Stop for independent Web audit before merge/release**

No new Plugin release is authorized by this task. Release publication requires separate authorization after source acceptance.

## Self-review result

- Spec coverage: all 12 source-rule sections and five required scenarios are mapped to Tasks 1-5.
- Step scan: each task produces one reviewable semantic slice; no new runtime subsystem is introduced.
- Type/term consistency: the plan uses one classification vocabulary throughout.
- Review focus: mixed commits, material task changes, literal locks, exclusion creep, and lifecycle closeout are each explicitly checked.
- Proportion: source changes remain limited to existing Project Governance contracts/templates plus root dogfooding controls.
