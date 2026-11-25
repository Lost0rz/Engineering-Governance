# Execution topology, intra-session handoffs, and cross-context cards

This reference governs how authorized `engineering-workflow` tasks split execution, hand off from planning to execution, or transfer across separate sessions/machines.

## 1. Execution topology and batching

| Mode | When to use | Coordination rule |
| --- | --- | --- |
| `Inline (batched)` | Default for cohesive single-stream tasks | Parallelize independent reads/searches/edits in one turn; chain verification with `&&` |
| `Sequential` | Dependent stages where step B needs step A's output | Carry verified file/symbol outputs forward directly |
| `Parallel read-only` | Independent codebase discovery or read-only checks | Share a safe read-only checkout; never mutate files |
| `Parallel disjoint writers` | Truly separate modules/files with zero shared state | Prove write scopes disjoint and verify integration once at merge |

Do not spawn Sub Agents merely to split sequential thinking or simulate progress. When a delegated unit fails, inspect its evidence and retry or fix only the failing boundary.

- **Delegated review & fix convergence:** specify the target's active `THREAT_PROFILE` (`SERVICE_OR_UNTRUSTED_INPUT` vs `SANDBOXED_APP`) in audit/roundtable/fix briefs (`Collateral impact first; BLOCKING/P0 or IMPORTANT/P1 requires reachable trigger path, observable impact, and frequency`), and terminate review/rework loops once two consecutive rounds surface only `MINOR` (`P2`) or `BACKLOG_NOTE` items.

## 2. Intra-session Plan-to-Execute handoff

When a higher-reasoning planning phase hands a plan to an execution phase in the same thread:

1. **Verified targets:** cite exact checked file paths, symbol names, and ordered edits—never guessed locations.
2. **Single-pass verification:** name the exact test/check command(s) and expected output that prove completion.
3. **Fail-fast `Re-plan if` triggers:** require handing back to planning if a verification fails twice, an assumed path/behavior differs, or scope/risk escalates to `G3`.

## 3. Host orchestration & model-routing precedence

Explicit user/host orchestration and model-routing rules (for example, global `AGENTS.md` / `GEMINI.md` delegation targets and provider settings) take **highest precedence** over generic plugin defaults.

Keep configured vs effective runtime identity distinct when reporting delegated work (`MODEL_SOURCE`, `MODEL_CONFIG`, `MODEL_EFFECTIVE`, `REASONING_EFFECTIVE`). Never report a configured setting as observed runtime identity unless the host actually exposes it.

## 4. Cross-context Handoff Cards (only when a link is insufficient)

An Issue/PR URL plus a concise 1-line delta is usually enough for cross-session continuation. Emit a structured Card only when the recipient otherwise lacks bounded scope or return expectations:

```text
TASK_ID: <task or Issue/PR ref>
MODE: <EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE>
TARGET: <repo / branch / PR / path>
AUTHORITY: <current user/host boundary; cards never grant write permission>
BOUNDARY: <bounded read/write scope and exclusions>
DELTA: <only fresh context not recoverable from linked sources>
RETURN_CONTRACT: <files changed, checks run, actual PR/CI state, blockers>
```

The receiver validates its own host permissions and applies the owning Skill directly. Machine browser/screenshot checks never replace pending `HUMAN_UI_ACCEPTANCE`.
