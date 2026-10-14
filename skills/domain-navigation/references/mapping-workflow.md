# Task-to-code mapping workflow

Route to the smallest source set sufficient for the current decision.

## Authority gate

For current-task navigation, identify the selected repository/checkout and verify the applicable task/control authority is current enough for this routing decision. If authority is unavailable/materially stale/contradictory, return `STOP_CURRENT_TASK_NAVIGATION` rather than guess.

For an explicitly named historical commit/branch/file/symbol, label the result `BOUNDED/HISTORICAL SNAPSHOT NAVIGATION` and do not present it as current task authority.

## Focused route

```text
verified task/target
-> affected Domain/capability
-> accepted semantic authority/navigation projection
-> candidate entry points/symbols/tests/runtime evidence
-> focused verification
-> confirmed route + unresolved gaps
```

Existing maps/search/indexes are leads, not proof. Direct focused source/runtime evidence verifies the route.

## Search escalation

Use the lightest method that answers the question:

1. known path -> direct read;
2. name/symbol -> targeted text search;
3. structural code question -> AST/structural search when available;
4. call/dependency/xref question -> indexed symbol/reference tool when available;
5. runtime ownership -> runtime/config/entry-point evidence.

Tool choice is environment-specific; this Skill defines the search progression, not a mandatory tool.

## Cross-repository route

When the governing task or explicit target spans repositories, route only through the named participants and shared contract authority. Report when material:

```text
OWNING_REPOSITORY
CONSUMER_REPOSITORY / DOWNSTREAM
UPSTREAM
CROSS_REPO_CONTRACT_AUTHORITY
RELEVANT_SOURCE_TEST_RUNTIME_ROUTE
```

Do not infer repository ownership from folder/name similarity or create a new cross-repo control artifact.

## Stop rule

Stop when the route is sufficient for the current decision. Expand one dependency/ownership hop only when a decision-relevant gap remains. Do not turn bounded navigation into whole-repository or whole-organization archaeology.

If an accepted navigation projection is verified stale and the active task authorizes refresh, update only the affected derived claim. Read-only work reports the correction candidate without mutation.
