# CURRENT TASK — Root Consistency and Freeze Handoff

Task ID: `EG-ROOT-CONSISTENCY-FREEZE-021`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `BOUNDED_ROOT_DOCS_FREEZE_AUDIT_HANDOFF`

## Objective

Hand off the completed root-document consistency correction for independent Web audit before merge and freeze. No reusable Skill-content change or target-project adoption is authorized.

## Authority and exact heads

- Pre-task main: `7ec0ffd574a0ec7e43c2990ebaf79633a6719e22`.
- Authorization/main head: `349adbe6011b77b6c5b921dc1f995ec881e2d36a`.
- Task branch: `control/root-consistency-freeze-auth`.
- Root-content implementation commit: `0062481f4bc7101fd3774472edf56be395763e69`.
- Historical `v0.1.0^{}` target: `738627a0caad330d277f60cfdaff5f153593135e`.
- Intended new stable version label after accepted closeout: `v0.2.0`.

## Changed durable files

- `README.md`
- `AGENTS.md`

The correction removes the obsolete universal requirement for a separate/literal Domain Map and aligns root guidance with the accepted Phase G Domain Navigation contract: discover existing semantic authorities first, reference rather than duplicate them, and add a separate derived navigation projection only when durable source/symbol/test/entry-point routing adds value.

## Audit contract

Verify:

1. branch is a clean linear descendant of authorization head;
2. durable-content changes are exactly `README.md` and `AGENTS.md`;
3. root wording matches the merged `domain-navigation` Skill contract;
4. `skills/**` is byte-unchanged from authorization;
5. exactly three top-level Skills remain;
6. no executable/runtime/dependency/workflow/tooling/new Skill was added;
7. historical `v0.1.0` is unchanged.

If all pass, merge to `main`, then close the task and freeze the resulting baseline by exact immutable commit SHA. If a `v0.2.0` Git tag can be written, it must point to that exact frozen SHA and never move.

## Forbidden actions

- any reusable Skill edit;
- any target-project mutation or adoption;
- any new architecture/tooling/runtime surface;
- moving/replacing historical `v0.1.0`.

## Current stop point

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`
