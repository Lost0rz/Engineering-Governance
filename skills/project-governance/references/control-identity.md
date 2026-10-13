# Control identity and freshness

Use this contract when a task or status record names commits, parents, refs, control revisions, or when repository revisions must be compared for implementation freshness. Do not assume every recorded SHA has the same meaning, and do not confuse literal Git movement with delivery-identity movement.

## Repository HEAD vs Delivery / Semantic HEAD

**Repository HEAD** is the literal Git commit SHA. Every commit changes Repository HEAD.

**Delivery / Semantic HEAD** is the implementation identity used for source/delivery freshness after excluding exactly these repository-control paths by default:

- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`

For implementation freshness, exact-code-tree verification, CI/test identity, code-review identity, independent-audit identity, and accepted implementation-tree equivalence, reason about Delivery / Semantic HEAD unless an accepted task or project authority explicitly requires literal Repository HEAD equality.

The exclusion is identity-specific, not an authorization exception and not a repository-host bypass. `CURRENT_STATUS.md` and `CURRENT_TASK.md` remain authoritative for the semantics they own and should normally be read at governed task start. Repository-host gates that the host binds to the literal current PR/head/base remain live literal constraints even when Delivery / Semantic HEAD is unchanged.

## Change classifications

Classify revision differences before deciding that HEAD drift occurred:

- **`CONTROL_ONLY_CHANGE`** — the changed path set is non-empty and contains only `CURRENT_STATUS.md` and/or `CURRENT_TASK.md`.
- **`CONTROL_ONLY_DRIFT`** — Repository HEAD advanced, but the difference between the compared revisions is limited to those two control files, so Delivery / Semantic HEAD is unchanged.
- **`DELIVERY_HEAD_CHANGE`** — any implementation/governance-relevant path changed. A mixed commit that changes a control file plus any other path is a `DELIVERY_HEAD_CHANGE`.
- **`SEMANTIC_TREE_EQUIVALENCE = PASS`** — the compared repository trees are equivalent after excluding exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md`.

Do not claim that a control-only commit leaves Git `HEAD` unchanged. It changes Repository HEAD while leaving Delivery / Semantic HEAD unchanged.

The default exclusion does **not** apply to `AGENTS.md`, workflow files, tests, schemas, migrations, dependency manifests, runtime configuration, source code, or governance implementation. A material change to any of those remains implementation/governance-relevant unless a separate accepted project rule explicitly says otherwise.

## Identity classes

- **Control parent / transition parent** — provenance anchor for the revision immediately before a control transition. It proves ancestry or transition context; it is not automatically the required current HEAD.
- **Control transition head** — the Repository HEAD produced by a control transition when that transition itself matters to the task.
- **Current control head** — the currently verified Repository HEAD whose controls are being relied on for the active decision.
- **Locked / expected-current / exact-execution head** — an explicit equality constraint declared by the active task or project authority. The lock must make clear whether it binds Delivery / Semantic HEAD or literal Repository HEAD when ambiguity is possible.
- **Remote freshness evidence** — the live or otherwise accepted remote ref/revision evidence used to decide whether current repository/control state is stale enough to invalidate the task.
- **Repository-host gate identity** — the literal PR head, base, merge candidate, merge queue entry, review state, or other identity against which the repository host currently evaluates required checks, approvals, conflicts, rulesets, or mergeability.

Names may differ by project. Classify the semantic role from the owning control or repository host rather than from a field name alone.

## Recorded SHA rule

A SHA written in `CURRENT_STATUS.md` or `CURRENT_TASK.md` is a provenance/audit anchor by default. It is **not** automatically `CURRENT_HEAD_MUST_EQUAL_THIS_SHA`.

An equality lock exists only when the owning control explicitly declares semantics such as `EXPECTED_HEAD`, `REQUIRED_HEAD`, `MUST_EQUAL`, `FROZEN_IMPLEMENTATION_HEAD`, or another unambiguous equality contract.

When an equality lock exists, identify whether it locks:

- Delivery / Semantic HEAD; or
- literal Repository HEAD.

For implementation-oriented verification, default an otherwise unqualified lock to Delivery / Semantic HEAD. Require literal Repository HEAD equality only when the task or project authority explicitly requires literal repository identity.

This default does not rewrite repository-host rules. If the repository host requires a status check, approval, conflict-free state, merge queue condition, or another gate on the latest literal PR head/base, that host requirement remains literal even when the task's implementation lock is semantic.

## Relationship rule

Choose the comparison that matches the declared identity:

- provenance/transition parent -> verify the required ancestry or direct-parent/transition relationship;
- transition head -> verify the transition revision and its intended control diff when material;
- current control head -> verify that the controls being used are read from the current accepted revision for the decision;
- semantic implementation lock -> require Delivery / Semantic HEAD equality or semantic-tree equivalence;
- literal repository lock -> require literal Repository HEAD equality;
- remote freshness -> compare against the remote authority/freshness basis the project actually declares;
- repository-host gate -> query the current host state for the literal identity that the host says the gate applies to.

Do not convert a relationship constraint into an equality constraint merely because both sides are Git SHAs. Likewise, do not convert semantic-tree equivalence into repository-host gate satisfaction.

## False-positive drift guard

A historical control parent differing from current Repository HEAD is not by itself `CONTROL_HEAD_DRIFT`.

Likewise, when the only difference between an accepted implementation revision and a later repository revision is `CURRENT_STATUS.md` and/or `CURRENT_TASK.md`, classify the difference as `CONTROL_ONLY_DRIFT`. That difference must not by itself cause `STOP_HEAD_DRIFT`, a task restart, a fresh construction branch, semantic CI/test restart, independent-audit restart, semantic exact-head invalidation, source re-verification, or a lifecycle-closeout loop.

It also must not be used to claim that current repository-host gates automatically remain satisfied. If the host keys required checks, approvals, mergeability, merge queue, conflicts, current-base, or latest-head conditions to the later literal identity, re-read those gates live and satisfy them as the host requires.

When relevant, report:

```text
Repository HEAD advanced by control-only records; delivery identity unchanged.
```

Continue using fresh repository evidence unless another task-owned condition or current repository-host gate independently requires a stop.

Stop when a material identity relationship actually fails: the declared parent is not in the required relationship, implementation-relevant content changed unexpectedly, the current controls are stale/contradictory for the task, an explicit semantic/literal equality lock fails, or a required live repository-host gate is not satisfied for the identity it governs.

## Repository-host gate boundary

Semantic implementation evidence and repository-host gate state are separate evidence classes.

Examples of semantic evidence that may be reused across proven `CONTROL_ONLY_DRIFT` include:

- test/CI conclusions about the unchanged implementation tree;
- code-review conclusions about unchanged implementation content;
- independent-audit conclusions about unchanged implementation content.

Examples of repository-host gates that must be read from current live host state when applicable include:

- required status/check suites attached to the current PR/head;
- required reviews or approval freshness rules;
- mergeability/conflict state against the current base;
- merge queue eligibility/state;
- ruleset/branch-protection requirements;
- current-base or latest-head requirements.

`SEMANTIC_TREE_EQUIVALENCE = PASS` can justify reuse of semantic implementation evidence. It cannot, by itself, produce `HOST_GATE_PASS`.

## Authorization remains authoritative

Control-only classification never weakens `CURRENT_TASK.md` as the task authorization authority.

If `CURRENT_TASK.md` materially changes objective, scope, allowed mutation, prerequisites, acceptance criteria, stop conditions, authority boundaries, or another task-owned decision, read and obey the new authorization before further state-changing work. That content change can change what work is authorized or which evidence is sufficient even though the control commit is not application-code identity.

A stale or conflicting authorization may therefore require reconciliation. A SHA mismatch caused only by control-record commits does not by itself constitute implementation drift.

## Evidence and reporting

When a stop or pass depends on control or delivery identity, report the semantic class and tested relationship, not only two SHAs. Prefer statements such as:

```text
CHANGE_CLASS: CONTROL_ONLY_DRIFT
REPOSITORY_HEAD: <sha>
DELIVERY_IDENTITY_CHANGED: NO
SEMANTIC_TREE_EQUIVALENCE: PASS
LOCKED_REPOSITORY_HEAD_REQUIRED: NO
HOST_GATE_STATE: <live current state or NOT_APPLICABLE>
```

or:

```text
LOCKED_HEAD_REQUIRED: YES
LOCK_TYPE: literal Repository HEAD
EXPECTED_LOCKED_HEAD: <sha>
OBSERVED_REPOSITORY_HEAD: <sha>
EQUALITY_VERIFIED: NO
FINAL_STATE: STOP_CONTROL_HEAD_DRIFT
```

This makes a later auditor able to distinguish genuine implementation drift, an explicit literal equality failure, harmless control-only Repository HEAD movement, and an independently failing current repository-host gate.

## Interaction with task reconciliation

A freshly verified status/control revision does not silently rewrite task authorization. If newly read control content invalidates a task prerequisite, acceptance criterion, STOP condition, allowed side effect, authority boundary, or explicit head lock, return to the control-plane reconciliation rules before state-changing work.

If the difference is only `CONTROL_ONLY_DRIFT` and the active task-owned semantics remain valid, no new task, fresh semantic CI/test run, fresh independent audit, or lifecycle reopen is required merely because Repository HEAD advanced. Repository-host gates still follow the host's current literal requirements and must be checked separately before a merge/release claim.
