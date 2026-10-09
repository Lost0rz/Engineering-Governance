# Control identity and freshness

Use this contract when a task or status record names commits, parents, refs, or control revisions. Do not assume every recorded SHA has the same meaning.

## Identity classes

- **Control parent / transition parent** — provenance anchor for the revision immediately before a control transition. It proves ancestry or transition context; it is not automatically the required current HEAD.
- **Control transition head** — the revision produced by a control transition when that transition itself matters to the task.
- **Current control head** — the currently verified revision whose controls are being relied on for the active decision.
- **Locked / expected-current / exact-execution head** — an explicit equality constraint declared by the active task or project authority. This identity is a hard gate when present.
- **Remote freshness evidence** — the live or otherwise accepted remote ref/revision evidence used to decide whether a local/current control state is stale enough to invalidate the task.

Names may differ by project. Classify the semantic role from the owning control rather than from a field name alone.

## Relationship rule

Choose the comparison that matches the declared identity:

- provenance/transition parent -> verify the required ancestry or direct-parent/transition relationship;
- transition head -> verify the transition revision and its intended control diff when material;
- current control head -> verify that the controls being used are read from the current accepted revision for the decision;
- locked/expected-current/exact-execution head -> require equality;
- remote freshness -> compare against the remote authority/freshness basis the project actually declares.

Do not convert a relationship constraint into an equality constraint merely because both sides are Git SHAs.

## False-positive drift guard

A historical control parent differing from current HEAD is not by itself `CONTROL_HEAD_DRIFT`.

For example, if task metadata records `P` as the parent used to publish a control transition and current HEAD `C` is verified as the expected child/descendant containing only that authorized control transition, then `C != P` is expected. Continue if current controls remain authoritative and no task field declares `P` as a locked current/execution head.

Stop when any material identity relationship actually fails: the declared parent is not in the required relationship, the transition content is not what the control contract permits, the current controls are stale/contradictory for the task, or an explicit locked/expected head differs.

## Evidence and reporting

When a stop or pass depends on control identity, report the semantic class and the tested relationship, not only two SHAs. Prefer statements such as:

```text
CONTROL_PARENT_ROLE: transition provenance
EXPECTED_RELATIONSHIP: direct parent of current control transition
RELATIONSHIP_VERIFIED: YES
CURRENT_CONTROL_HEAD: <sha>
LOCKED_HEAD_REQUIRED: NO
```

or:

```text
LOCKED_HEAD_REQUIRED: YES
EXPECTED_LOCKED_HEAD: <sha>
OBSERVED_HEAD: <sha>
EQUALITY_VERIFIED: NO
FINAL_STATE: STOP_CONTROL_HEAD_DRIFT
```

This makes a later auditor able to distinguish a genuine equality failure from a parent/current-head category error.

## Interaction with task reconciliation

A freshly verified status/control revision does not silently rewrite task authorization. If the newly established current control state invalidates a task prerequisite, acceptance criterion, STOP condition, allowed side effect, or explicit head lock, return to the control-plane reconciliation rules before state-changing work. If it only establishes that the historical parent relationship was interpreted correctly and the active contract remains valid, no new task is required.
