# Fresh incident capture

# Fresh, attributable incident capture

When a new probe is introduced, base key conclusions on a fresh incident or reproduction captured after that probe is active. Capture the smallest reproduction and observation window sufficient to answer the blocked question.

Record the following identities when applicable and available; mark missing values `unknown` rather than inferring them:

- `REPOSITORY_REVISION`;
- `BUILD_IDENTITY`;
- `APP_RUNTIME_IDENTITY`;
- `PROCESS_ID` and `PROCESS_START`;
- `CONFIGURATION_IDENTITY`;
- relevant `SESSION_ID`, `REQUEST_ID`, or `DATA_ID`;
- `OBSERVATION_WINDOW`;
- timestamps and `CLOCK_BASIS`.

Do not combine captures into one causal chain when they differ in app version, commit, process, configuration, runtime, or clock basis. Keep historical captures separate unless their identities and relationship are verified. Preserve a user report as a report, direct observations as observations, and inference as interpretation; record unresolved identity or timing gaps explicitly.
