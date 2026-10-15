# CURRENT TASK — Remote Delivery Closeout

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-REMOTE-DELIVERY-CLOSEOUT-087`

Task class: `CAPABILITY_HARDENING`

State: `SOURCE_MERGED — RUNTIME_ACCEPTANCE_PENDING`

Target Plugin version: `0.7.3` candidate.

## Objective

Close a Project Governance delivery gap where local commits can be reported as completed engineering work even when a configured repository remote exists but the task branch/ref was never pushed, leaving the work unavailable to remote/Web audit.

Repository-backed engineering delivery now distinguishes local commit creation from remote publication.

## Delivered source behavior

For state-changing work that produces or advances Git commits:

- applicable configured remote + not explicitly local-only -> push only the already-authorized task/project ref and verify fresh remote-ref evidence before reporting full repository delivery;
- local commit SHA / clean working tree / local branch SHA alone is not remote-delivery evidence;
- no applicable remote -> `REMOTE_DELIVERY: NOT_APPLICABLE_NO_REMOTE`;
- explicit local-only authority -> `REMOTE_DELIVERY: NOT_REQUIRED_LOCAL_ONLY`;
- applicable remote but push or remote verification failure -> preserve local work and report `PENDING` / `FAILED` rather than full remotely available completion;
- normal closeout does not authorize remote creation, force-push, credential bypass, ref substitution, or implicit push to `main`.

Receipts now distinguish, when applicable:

```text
LOCAL_COMMIT
REMOTE_DELIVERY
REMOTE_REF
REMOTE_COMMIT
```

## Source delivery

- PR `#35 — feat: require verified remote repository delivery at closeout` — `MERGED`;
- candidate branch: `codex/remote-delivery-closeout-v073`;
- validated semantic/source head: `7a5c256b4bdf09768645d252df340870f8d8ef82`;
- `Validate Plugin v0.7.3 Candidate` run `38677775327` — `success`;
- current PR head added only archive of the obsolete v0.7.2 validator after the validated semantic head;
- merge commit: `998a8cae62546ed8a2551c1fb54aded037c62985`;
- Plugin manifest on `main`: `0.7.3` candidate;
- formal published GitHub release remains immutable `plugin-v0.7.2`.

## Source surfaces

- `skills/project-governance/SKILL.md`;
- `skills/project-governance/references/development-flow.md`;
- `skills/project-governance/references/remote-delivery.md`;
- `skills/agent-handoff/references/handoff-contract.md`;
- `references/V074_REMOTE_DELIVERY_ACCEPTANCE.md`;
- `.github/workflows/validate-plugin-v0.7.3.yml`;
- archived obsolete `.github/workflows/validate-plugin-v0.7.2.yml`;
- `plugin.json` -> `0.7.3`.

## Runtime acceptance still required

Before Task 087 is fully complete, exercise the new behavior in disposable Local repositories without production mutation:

1. Git repo + configured disposable remote -> final authorized task ref is pushed and remote identity verified before completion;
2. Git repo + no remote -> `NOT_APPLICABLE_NO_REMOTE` with no remote creation;
3. explicit local-only case -> `NOT_REQUIRED_LOCAL_ONLY`;
4. remote/push failure case -> local work preserved and full remote-delivery completion refused;
5. confirm no implicit `main`/force push;
6. confirm receipt exposes local vs remote delivery separately.

## Safety boundaries

- never create a remote merely because none exists;
- never guess credentials or bypass remote permissions;
- never force-push unless separately and explicitly authorized by project authority;
- never select `main` merely because it exists;
- preserve local/unique work when push fails;
- read-only tasks do not gain push side effects;
- repository-host merge/review/CI gates remain separate from proof that a commit is remotely visible.

## Lifecycle

- source construction/merge: complete;
- Local runtime acceptance: pending;
- Web Plugin 0.7.3 synchronization: not yet performed;
- Local Git-backed 0.7.3 distribution/update: not yet accepted;
- formal GitHub `plugin-v0.7.3` release: not authorized/performed.

## Control Alignment

- `PREDECESSOR_RELEASE`: `plugin-v0.7.2` (`PUBLISHED / IMMUTABLE`)
- `PR`: `#35` (`MERGED`)
- `MERGE_COMMIT`: `998a8cae62546ed8a2551c1fb54aded037c62985`
- `TARGET_VERSION`: `0.7.3`
- `SOURCE_VALIDATION`: `PASS`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`
- `WEB_PLUGIN_UPDATE`: `NOT_PERFORMED`
- `FORMAL_GITHUB_RELEASE_073`: `NOT_PERFORMED`
- `TASK_STATE`: `SOURCE_MERGED — RUNTIME_ACCEPTANCE_PENDING`
