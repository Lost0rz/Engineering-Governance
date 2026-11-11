### CONTRACT

EXECUTION_SPEC_V1

### TASK_ID

<Stable task identity, preserve across contexts>

### SPEC_REVISION

1

### MODE

EXECUTE

### PURPOSE

<Specific engineering task purpose, e.g. BOUNDED_CORRECTIVE>

### OBJECTIVE

<One observable engineering outcome>

### VERIFIED_BASELINE

<Actual inspected main/ref, file/symbol/API evidence; UNKNOWN means cannot execute>

### TARGET_BEHAVIOR

<Positive and negative observable acceptance claims>

### IN_SCOPE

<Explicit allowed components and semantics>

### OUT_OF_SCOPE

<Explicit exclusions>

### ALLOWED_SIDE_EFFECTS

<Permitted source, workspace, API or data mutations>

### CANONICAL_AUTHORITIES

<Accepted design, API, schema and AGENTS pointers>

### WORK_PACKAGES

#### WP01 — scoped code change
Targets: <verified path/function/interface>
Preconditions: <verified entry preconditions>
Actions: <ordered concrete actions>
Dependencies: <NONE or WP dependency>
Edge cases: <bounded edge cases>
Verification: <command and expected output>
Done: <checkable done criterion>

### VERIFICATION_PLAN

<Governance authority/effects ceiling G0-G3, separately from verification tier V0-V3; list focused checks, cadence, and final live host gates as applicable>

### HUMAN_UI_ACCEPTANCE

PENDING

### DEVIATION_POLICY

<L0 CONTINUE, L1 LOCAL_CORRECT, L2 PAUSE_AND_ASK, L3 TERMINATE inside the fixed objective/risk/effect envelope. THIS IS AN ISSUE-BACKED TEMPLATE ONLY: host-verified current top-level USER-directed bounded G1/G2 tasks need no first Issue or GitHub approval comment. Unattended durable autonomy still requires independent protected global host grant and separated executor credentials.>

### STOP_AND_SAFETY

<Specific unapproved/destructive/permission/dependency stop criteria>

### RETURN_CONTRACT

<Expected issue receipt content and PR/CI evidence>

### AUTHORIZATION_BASIS

PENDING — awaiting authenticated SPEC_APPROVAL_V1 comment

