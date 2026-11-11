# Canonical code ownership

Give each behavior or durable state fact one clear source of truth. The goal is coherent software, not a global file-count or module-size limit.

## Change method

1. Locate the existing function, data owner, service or public API responsible for the behavior.
2. Reuse or extend that owner where cohesive; split/replace it when a real responsibility or dependency boundary requires it.
3. If adding a writer/consumer, define data ownership and any consequential interface/persistence compatibility before implementation.
4. Validate affected callers, tests, schema/migrations and runtime behavior rather than only the new file.
5. Update durable design/API documentation when the actual canonical contract changes.

An architectural **canonical writer** is not the same as a Git agent that currently edits files. Actual concurrent edits are handled by workspace conflict evidence, not architecture ownership labels.

Favor understandable modules and explicit API boundaries. Avoid duplicate authoritative state or multiple services racing to mutate the same fact. File length by itself is not a stop condition.
