---
name: project-governance
description: Normal engineering entry. Keep task authority and workflow clear; perform bounded work, verify affected behavior, and report real evidence.
---

# Project Governance

The default loop is **understand → locate → implement → verify → deliver**. Use the smallest relevant Skill; optional specialist methods are not required stages.

## Task authority

- **G0/read-only:** inspect the necessary evidence directly.
- **Authenticated current USER-directed G1/bounded G2:** the current request plus actual host/tool permissions is sufficient initial task authority. Stay within the intended objective, effects and real project constraints; correct ordinary defects without repeated approval or a first Issue.
- **Existing legacy task:** use the selected approved Issue/revision or accepted FILE_CONTROL Task where that mode actually applies.
- **G3/changed scope:** obtain an explicit decision for actual new privilege, credential/security-trust expansion, destructive or irreversible production/data effects; live merge/release gates remain separate.

`CONTROL_POLICY_V1` is the installed mode source. Project `AGENTS.md` owns project-specific facts, not workflow grants. Policy helper outputs are not host writer credentials. Cross-session/unattended autonomous grants require independent host trust and are inactive in this release.

## Perform the work

1. Recover only relevant repository/ref, task and source facts; reuse a safe workspace.
2. Choose the existing code owner. Use design/navigation/incident diagnosis only for unresolved questions.
3. Implement within the current task; handle L0/L1 directly, resolve L2 uncertainty inside scope where possible.
4. Choose V0–V3 evidence from actual affected behavior. Prefer focused/affected tests; preserve meaningful security and integration checks.
5. Confirm observed remote PR/CI/merge state when needed; keep human product UI acceptance separate from automated browser tests.

Delegate only when it meaningfully helps; the receiving host chooses tools/models. A real cross-context transfer uses a concise `agent-handoff` Card with references and delta. Return the actual change, decisive evidence, and unresolved decision if any.

## References, only when relevant

- [global-routing](references/global-routing.md): specialist selection.
- [issue-control](references/issue-control.md) and [issue-execution](references/issue-execution-contract.md): selected legacy Issue or disputed authorization.
- [verification](references/verification-tiers.md): test scope and evidence.
- [workspace](references/workspace-lifecycle.md) and [code ownership](references/code-structure.md): actual workspace or state-owner questions.
- [remote delivery](references/remote-delivery.md): PR/merge/release.
- [development flow](references/development-flow.md), [control plane](references/control-plane.md), [identity](references/control-identity.md): exceptional lifecycle transitions.
- [artifact lifecycle](references/artifact-lifecycle.md), [planning](references/planning-documents.md), [migration](references/issue-control-migration.md), [adoption](references/adoption.md), [composition](references/capability-composition.md): only when those operations are requested.
