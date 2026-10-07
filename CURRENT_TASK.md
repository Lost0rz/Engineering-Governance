# CURRENT TASK — Doctor CLI Productization

Task ID: `EG-V01-DOCTOR-CLI-005`

State: `WAITING_FOR_MERGE_AUTHORIZATION`

Mode: `INDEPENDENT_WEB_AUDIT_ACCEPTED`

## Objective

The bounded Doctor CLI implementation is complete and has passed independent Web review. The only authorized next action is an explicit user decision on merging Draft PR #5. Do not add product code, expand diagnostics, start Bootstrap/Audit/AI work, or perform lifecycle cleanup before merge authorization.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Live `main` / PR base during independent review: `f1fba7f9591047f6e2f40e677f79048227d67d8e`.
- Authorized task branch: `codex/eg-v01-doctor-cli`.
- Implementation commit: `40cedb3ab21130ca773ec20519d1b8d669b24422`.
- Executor handoff head independently reviewed: `26404b234fb720dd5de3ac05ee3889f1b0cc4a06`.
- PR: #5, OPEN / DRAFT / UNMERGED, targeting `main`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.
- Stable tag `v0.1.0` must remain at `738627a0caad330d277f60cfdaff5f153593135e`.

## Accepted implementation

Supported path:

`PYTHONPATH=src python3.11 -m engineering_governance doctor <target>`

The implementation is intentionally thin:

- `src/engineering_governance/__main__.py` uses standard-library `argparse`;
- the `doctor` command delegates to existing `run_doctor()`;
- it supplies existing `run_git_readonly`, `Path.read_bytes`, stdout/stderr, and a timezone-aware UTC clock;
- it does not duplicate Doctor report construction or Git probing;
- usage errors are rejected before Doctor execution;
- default operation remains local/offline/read-only.

Product/test/documentation paths in the implementation commit are exactly:

- `README.md`
- `src/engineering_governance/__main__.py`
- `tests/test_cli.py`

No dependency file, packaging framework, remote-query path, new Doctor check, Bootstrap, deeper Audit, AI runtime, MCP, enforcement, remediation, migration, or unrelated refactor is included.

## Executor evidence

- Baseline Python 3.11 suite: 52 tests, 0 failures.
- Focused RED command: `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_cli.py' -v`.
- RED result: 4 expected failures because `engineering_governance.__main__` was absent.
- Focused GREEN: 4/4.
- Final Python 3.11 suite: 56 tests, 0 failures.
- Valid target: exit 0 with one existing JSON report.
- Non-repository target: Doctor STOP exit 2 with no JSON report.
- Missing target / unsupported command: nonzero usage error without calling Doctor.
- Dirty-target read-only snapshot: file and Git metadata unchanged before/after CLI execution.
- Executor worktree was reported clean and local task HEAD matched remote handoff head.

## Independent Web audit — 2026-10-07

Result: `PASS` — no Critical or Important findings.

Verified against GitHub and independent reconstruction:

1. PR #5 is open, draft, unmerged, mergeable, targets `main`, and its reviewed handoff head is `26404b234fb720dd5de3ac05ee3889f1b0cc4a06`.
2. Live `main` remained exactly `f1fba7f9591047f6e2f40e677f79048227d67d8e`; no base drift occurred during review.
3. `f1fba7f... -> 40cedb3...` is one implementation commit touching only README, `__main__.py`, and `test_cli.py`; `40cedb3... -> 26404b2...` is the executor control/evidence handoff.
4. The CLI implementation delegates to the existing Doctor path and pre-existing local Git allowlist. The allowlist contains only `rev-parse --show-toplevel`, `rev-parse --git-common-dir`, `rev-parse --verify HEAD`, and `symbolic-ref --quiet --short HEAD`; no fetch/pull/ref mutation or network operation is introduced.
5. The new tests directly exercise the required valid-target, STOP, usage-rejection, and dirty-target mutation behaviors.
6. Web independently reconstructed the changed CLI slice from the reviewed remote sources. With `__main__.py` removed, the four focused CLI tests failed as expected; restoring the PR implementation produced 4/4 PASS. The reconstruction used Linux/Python 3.13, so it verifies the changed behavior and RED/GREEN semantics but is not represented as an independent Python 3.11 full-suite rerun.
7. The executor's exact Python 3.11 full-suite evidence remains 56/56. GitHub exposes no CI status checks for the PR head; absence of CI is not counted as PASS.
8. The annotated `v0.1.0` tag independently dereferences to `738627a0caad330d277f60cfdaff5f153593135e`.
9. README accurately states that the first local Doctor CLI slice exists while Bootstrap and Audit remain unimplemented.

## Merge authorization gate

Do not merge without explicit user authorization.

After authorization, Web must freshly verify:

1. live `main` is still the expected base or reconcile any legitimate advance;
2. PR #5 remains OPEN and unmerged;
3. the exact PR head is the expected audited lineage (implementation commit `40cedb3...`, executor handoff `26404b2...`, plus only this Web audit control update);
4. no new product/test paths or review blockers appeared;
5. `v0.1.0` remains unchanged.

If those checks pass, merge PR #5 with exact-head protection. After merge, authorize a separate local closeout gate to fast-forward canonical `main`, rerun the full Python 3.11 suite on merged `main`, prove the retained task worktree/branch has no unique work, and clean it up without force.

## Current stop point

`WAITING_FOR_MERGE_AUTHORIZATION`

No merge, release, lifecycle cleanup, Bootstrap, deeper Audit, AI runtime, or next feature is authorized yet.
