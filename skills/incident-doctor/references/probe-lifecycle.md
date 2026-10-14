# Probe lifecycle

Classify every state-changing probe as `TEMPORARY` or `DURABLE`.

## TEMPORARY — default

Before deployment record, when material:

```text
OWNER
SCOPE
REMOVE_WHEN
ROLLBACK_METHOD
```

After evidence is captured, preserve the needed incident evidence and remove/disable the probe at the declared condition. If removal cannot occur, report the blocker explicitly.

## DURABLE — exceptional

Promotion requires repeated evidence of continuing value, explicit owner/scope, accepted safety/privacy/operability impact, and separate authorization. A single incident does not justify permanent observability.

Diagnostic value alone never authorizes a durable probe.
