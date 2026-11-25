# Minimal probes, fresh captures & diagnostic techniques

Load only after `incident-doctor`'s inline hard evidence gate concludes `INSUFFICIENT` and names concrete `MISSING_FACT` + `BLOCKED_DECISION`.

## 1. Minimum decision-linked probe design

Add the least intrusive probe (preferring read-only runtime/canonical queries first) whose possible outcomes change the blocked decision. Record:

- `MISSING_FACT` & `BLOCKED_DECISION`;
- `COMPETING_EXPLANATIONS` & `DISCRIMINATING_OBSERVATION` (which outcome supports/falsifies each);
- `RESULT_TO_DECISION` (if every plausible outcome leads to the same action, do not add the probe);
- If the probe can alter timing, load, state, or privacy exposure, also record `OBSERVER_EFFECT_RISK`, `SAFETY_PRIVACY_IMPACT`, and `CLEANUP_PLAN`.

## 2. Fresh, attributable incident capture

Base causal claims only on captures taken **after** the probe became active, binding applicable identities (`unknown` if unavailable, never inferred):

- `REPOSITORY_REVISION`, `BUILD_IDENTITY`, `APP_RUNTIME_IDENTITY`, `CONFIGURATION_IDENTITY`;
- `PROCESS_ID` / `PROCESS_START`, relevant `SESSION_ID` / `REQUEST_ID` / `DATA_ID`, `OBSERVATION_WINDOW`, and `CLOCK_BASIS`.

Keep user reports (`USER_REPORTED_SYMPTOM`), `DIRECT_OBSERVATION`, `INTERPRETATION`, falsifiable `HYPOTHESIS`, and verified `ROOT_CAUSE_CLAIM` strictly separate; never merge captures from different commits, processes, or clock bases into one causal chain.

## 3. Systematic isolation techniques (apply only as needed)

- **Recent-change comparison:** diff task-relevant code/config/environment changes against the last known working state.
- **Working-vs-broken comparison:** compare the failing input/environment against the nearest working path before assuming any difference is harmless.
- **Backward data-flow tracing:** trace bad values upstream to their earliest causal producer instead of patching downstream symptoms.
- **Single-hypothesis minimum test:** state falsification criteria up front and vary one material condition at a time.
- **Condition-based waiting:** observe real state transitions/events instead of guessing with arbitrary sleeps.

## 4. Probe lifecycle (`TEMPORARY` default vs `DURABLE`)

- **TEMPORARY (default):** assign `OWNER`, `REMOVE_WHEN`, and `ROLLBACK_METHOD`; remove/disable the probe once evidence is captured and fix verification passes.
- **DURABLE (exceptional):** requires repeated proven value, explicit owner/safety/privacy review, and task authorization; diagnosis never auto-authorizes permanent telemetry.
