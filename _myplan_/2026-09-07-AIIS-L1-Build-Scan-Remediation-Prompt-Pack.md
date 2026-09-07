# AIIS_L1 — Build → Scan → Remediation Prompt Pack

Date: 2026-09-07
Status: Canonical classroom prompt pack
Scope: AI Weather Security Center only
Safety boundary: localhost, owned repository, teacher-provided code, or explicitly authorized lab only. Do not use these prompts against arbitrary public systems.

---

# 1. BUILD PROMPT — Create a Working Weather Security Center

Use this prompt in Antigravity to create the first working version of the project.

```text
PROJECT: AI Weather Security Center

GOAL
Create a complete, runnable Python project that fetches real Taiwan weather forecast data from the Taiwan Central Weather Administration (CWA) Open Data API, processes the data, saves normalized records to CSV, and presents an interactive Streamlit web application with a Taiwan map and regional weather table.

DATA SOURCE
Use the CWA Open Data API dataset:
F-A0010-001
(one-week agricultural weather forecast)

AUTHENTICATION
Use an environment variable named:
CWA_API_KEY

Do not hard-code any real API key.
Create a `.env.example` file that contains only a placeholder.
Do not commit secrets.

IF A REAL API KEY IS NOT AVAILABLE
Use a small local sample JSON fixture that matches the expected structure closely enough to validate parsing and UI behavior.
Do not invent or expose credentials.

FUNCTIONAL REQUIREMENTS
1. Fetch forecast data from CWA using Python `requests`.
2. Use a reasonable HTTP timeout.
3. Keep TLS certificate verification enabled.
4. Do not use `verify=False` as a default workaround.
5. Handle HTTP errors, timeouts, invalid JSON, missing fields, and temporary API failure gracefully.
6. Extract or derive teaching-region weather information for:
   - Northern
   - Central
   - Southern
   - Northeastern
   - Eastern
   - Southeastern Taiwan
7. Document the mapping from CWA locations to these teaching regions.
8. Extract at minimum:
   - date
   - region
   - min_temperature
   - max_temperature
   - average_temperature
   - weather_description
9. Save normalized data to:
   data/weather_data.csv
10. Build an interactive Streamlit web app.
11. Use a left-right layout:
   LEFT: Folium-based Taiwan map
   RIGHT: weather data table
12. Add a date selector that dynamically filters the displayed data.
13. Use approximate teaching coordinates for each region marker and document that they are representative rather than authoritative geographic centroids.
14. Color region circles by average temperature:
   - blue: <20°C
   - green: 20–<25°C
   - yellow: 25–<30°C
   - red: >=30°C
15. Each map popup should show:
   - region
   - date
   - minimum temperature
   - maximum temperature
   - average temperature
   - weather description

PROJECT STRUCTURE
Create a clean structure similar to:

weather-security-center/
    app.py
    cwa_client.py
    weather_parser.py
    weather_service.py
    config.py
    data/
        weather_data.csv
    tests/
        test_parser.py
        test_weather_service.py
    fixtures/
        sample_cwa_response.json
    .env.example
    .gitignore
    requirements.txt
    README.md

PACKAGES
Use only what is needed. Expected core packages:
- requests
- pandas
- streamlit
- folium
- streamlit-folium
- python-dotenv
- pytest

BASELINE SECURITY REQUIREMENTS
- no hard-coded secrets
- no committed credentials
- validate externally supplied response structures before using fields
- use network timeouts
- handle network exceptions
- keep TLS verification enabled
- no `eval()` or `exec()`
- no arbitrary command execution
- no unsafe file paths derived from external input
- no intentional backdoor
- no offensive or attack functionality
- avoid displaying unnecessary internal stack traces or secrets to end users

TESTS
Create tests for at least:
1. temperature parsing
2. average-temperature calculation
3. temperature color classification
4. missing-field handling
5. malformed/partial fixture handling
6. regional mapping logic

Where appropriate, mock API behavior rather than requiring a live CWA call during tests.

README
Document:
- what the project does
- architecture
- required environment variables
- setup
- virtual environment creation
- dependency installation
- how to fetch data
- how to run tests
- how to start Streamlit
- expected local URL
- known limitations
- security assumptions

EXECUTION WORKFLOW
STEP 1 — Inspect environment and propose a short implementation plan.
STEP 2 — Create the project structure.
STEP 3 — Implement the application.
STEP 4 — Install dependencies only if needed.
STEP 5 — Run tests.
STEP 6 — Start the app locally and verify that the website renders.
STEP 7 — Fix runtime or test failures until the baseline application works.
STEP 8 — Produce a BUILD REPORT.

BUILD REPORT
At the end, report:
1. files created
2. CWA integration status
3. whether real API or fixture data was used
4. tests run and results
5. local run result
6. known limitations
7. security assumptions
8. items that should later be reviewed by a security scanner

IMPORTANT
Do not claim success based only on code generation.
Success requires evidence from tests and local execution.

Target workflow:
PROMPT → PLAN → BUILD → RUN → TEST → WORKING WEATHER WEBSITE
```

---

# 2. SECURITY SCAN PROMPT — Code-First Review with Semgrep

Use this only on the local/owned Weather Security Center repository.

```text
TASK: Security Scan — AI Weather Security Center

SCOPE
Review only this local/owned repository.
Do not scan arbitrary public targets.
Do not perform exploitation.
Do not modify code yet.

PRIMARY TOOL
Use Semgrep as the representative SAST tool.

GOAL
Produce a reproducible before-remediation security report that separates:
- scanner findings
- confirmed evidence
- likely false positives
- assumptions that still need verification

WORKFLOW
1. Inspect the project structure.
2. Identify the application entry points and externally controlled inputs.
3. Run the existing test suite first and record baseline results.
4. Run Semgrep using an appropriate maintained ruleset for Python/web/security code.
5. Preserve the raw scan result where practical.
6. Review each relevant finding in source context.
7. Do NOT automatically treat every Semgrep match as a confirmed vulnerability.
8. Do NOT modify code in this phase.

FOR EACH FINDING REPORT
- Finding ID
- Tool / rule
- Severity
- File
- Line or code location
- Relevant code snippet or concise description
- Asset affected
- Threat
- Vulnerability / weakness
- CIA impact
- Likelihood: Low / Medium / High
- Impact: Low / Medium / High
- Initial risk: Low / Medium / High / Critical
- Evidence
- Classification:
  - CONFIRMED
  - LIKELY TRUE POSITIVE
  - LIKELY FALSE POSITIVE
  - NEEDS VERIFICATION
- Why this classification was chosen
- Recommended control

MANUAL REVIEW CHECKLIST
In addition to Semgrep output, inspect the code for these teaching concerns:
- hard-coded secrets or credential handling
- accidental secret exposure in logs/UI
- missing request timeout
- disabled TLS verification
- weak validation of external API response structure
- `eval()` / `exec()` or unsafe dynamic execution
- unsafe subprocess / shell invocation
- unsafe path construction
- overly broad exception handling hiding security-relevant failures
- debug information exposed to users
- unsafe temporary-file handling if present
- insecure deserialization if present
- dependency/configuration concerns that can be established from repository evidence

Do not invent findings for categories that are not present.

OUTPUT FILES
Create:

security_reports/semgrep_before.md
security_reports/scan_summary.md

If raw machine-readable output can be generated safely, also create:
security_reports/semgrep_before.json

`semgrep_before.md` should contain the detailed findings.
`scan_summary.md` should contain:
- baseline test result
- number of findings by classification
- top risks
- items needing verification
- findings likely to be false positives

STOP CONDITION
Do not fix code in this phase.
End by proposing the next remediation-analysis step.

Target workflow:
BASELINE TEST → SAST SCAN → REVIEW EVIDENCE → CLASSIFY → REPORT
```

---

# 3. REMEDIATION PROPOSAL PROMPT — Analyze Before Changing Code

Use this after the scan report exists. This phase creates a proposal only.

```text
TASK: Create a Security Remediation Proposal

INPUT
Review:
- security_reports/semgrep_before.md
- security_reports/scan_summary.md
- relevant source files
- existing tests

GOAL
Create a remediation proposal for confirmed or well-supported findings before modifying code.

DO NOT MODIFY SOURCE CODE YET.

PRINCIPLES
1. Fix root causes, not only scanner symptoms.
2. Prefer the smallest safe change.
3. Preserve existing functionality.
4. Do not fix findings that are classified as likely false positives unless new evidence changes that classification.
5. Items marked NEEDS VERIFICATION must first receive a verification plan.
6. Every accepted fix must have a verification method.
7. Where practical, add a regression test that would fail before the fix or protect the corrected behavior afterward.

FOR EACH FINDING CREATE
- Finding ID
- Current classification
- Root cause
- Security consequence
- Affected Asset
- CIA impact
- Proposed change
- Files expected to change
- Why this is the minimum safe fix
- Possible compatibility / regression risk
- Test to add or update
- How to verify after implementation
- Expected post-fix scanner result
- Decision:
  - FIX NOW
  - VERIFY FIRST
  - ACCEPT RISK
  - FALSE POSITIVE / NO CHANGE

PRIORITIZATION
Order the work by practical risk:
1. confirmed High/Critical risk
2. confirmed Medium risk
3. verification items with potentially high impact
4. Low-risk hardening
5. false positives / no-change explanations

OUTPUT
Create:
security_reports/remediation_proposal.md

At the top include a short executive summary:
- what should be fixed first
- what should not be changed
- what still needs evidence

At the end include an implementation checklist in dependency-safe order.

Do not implement the proposal yet.
```

---

# 4. FIX PROMPT — Implement Approved Remediation

Use this only after reviewing the remediation proposal.

```text
TASK: Implement Approved Security Remediation

INPUT
Use:
- security_reports/semgrep_before.md
- security_reports/scan_summary.md
- security_reports/remediation_proposal.md

SCOPE
Modify only this local/owned Weather Security Center repository.
Do not add offensive functionality.

GOAL
Implement only findings marked `FIX NOW` in the remediation proposal, plus any explicitly approved verification-driven fix that becomes confirmed during implementation.

WORKFLOW FOR EACH FIX
1. Re-open the original finding and relevant code.
2. Confirm the root cause still exists.
3. Make the smallest safe code change.
4. Preserve existing behavior unless the behavior itself is insecure.
5. Add or update a regression/security test where practical.
6. Run the relevant focused tests.
7. Run the full test suite.
8. Run Semgrep again.
9. Compare before and after results.
10. Document unresolved findings instead of hiding them.

DO NOT
- silence Semgrep merely by adding ignore comments unless there is documented false-positive justification
- remove tests to make the build pass
- weaken TLS verification
- hard-code secrets
- introduce broad exception swallowing
- claim a vulnerability is fixed without verification evidence
- make unrelated refactors

OUTPUT FILES
Create or update:

security_reports/remediation.md
security_reports/semgrep_after.md
security_reports/verification_summary.md

If practical, also save:
security_reports/semgrep_after.json

REMEDIATION REPORT FORMAT
For every implemented finding show:

BEFORE
→ ROOT CAUSE
→ FIX
→ TEST
→ RE-SCAN
→ AFTER

Include:
- files changed
- exact rationale
- tests added/updated
- test results
- scanner result before
- scanner result after
- residual risk

VERIFICATION SUMMARY
Summarize findings under:
- FIXED AND VERIFIED
- IMPROVED BUT RESIDUAL RISK REMAINS
- UNRESOLVED
- FALSE POSITIVE / ACCEPTED
- NEEDS FURTHER VERIFICATION

FINAL RULE
A scanner becoming quiet is not, by itself, proof that the system is secure.
Verification requires code evidence, tests, and review.

Target workflow:
FINDING → ROOT CAUSE → FIX → TEST → RE-SCAN → VERIFY
```

---

# 5. OPTIONAL END-TO-END ORCHESTRATION PROMPT

For a teacher-led demonstration, this prompt can coordinate all phases while preserving explicit phase gates.

```text
Run a controlled Secure Vibe Coding workflow on this local/owned AI Weather Security Center.

PHASE 1 — BUILD
Create or validate a working baseline application.
Run tests and record evidence.
STOP and summarize.

PHASE 2 — SCAN
Run Semgrep and perform evidence-based manual review.
Create `security_reports/semgrep_before.md` and `scan_summary.md`.
Do not modify code.
STOP and summarize.

PHASE 3 — PROPOSE
Create `security_reports/remediation_proposal.md`.
Do not modify code.
Clearly separate FIX NOW, VERIFY FIRST, ACCEPT RISK, and FALSE POSITIVE.
STOP and summarize.

PHASE 4 — FIX
Implement only approved/justified fixes.
Add regression tests.
Run tests.
Re-run Semgrep.
Create remediation and verification reports.
STOP and summarize.

At all phases:
- operate only on this repository / localhost
- preserve evidence
- separate facts from assumptions
- do not invent vulnerabilities
- do not exploit anything
- do not hide unresolved findings
- AI assists; human review remains required

Overall workflow:
BUILD
→ TEST
→ SCAN
→ CLASSIFY
→ PROPOSE
→ FIX
→ TEST
→ RE-SCAN
→ VERIFY
→ REPORT
```

---

# 6. Teaching Placement

Recommended placement across the canonical 16-lesson plan:

- L1: use Build Prompt; introduce AI review concept only
- L2: use the Build Prompt again as part of disciplined Antigravity/GitHub workflow
- L3: inspect/extend the generated Python/API/data code
- L4: use Security Scan Prompt → Remediation Proposal Prompt → Fix Prompt
- L13: revisit the same remediation/verification pattern for Blue Team engineering

Do not compress all four phases into L1. L1 should end with the question `SECURE ?`; L4 is where the representative SAST implementation becomes the formal lab.

---

# 7. Canonical Engineering Loop

```text
PROMPT
  ↓
BUILD
  ↓
RUN
  ↓
TEST
  ↓
WORKING ✓
  ↓
SECURITY REVIEW
  ↓
SCAN
  ↓
FINDING
  ↓
EVIDENCE / CLASSIFICATION
  ↓
REMEDIATION PROPOSAL
  ↓
HUMAN REVIEW
  ↓
FIX
  ↓
REGRESSION TEST
  ↓
RE-SCAN
  ↓
VERIFY
  ↓
REPORT
```

Core message:

> WORKING ≠ SECURE
>
> AI BUILDS. AI ASSISTS REVIEW. HUMAN VERIFIES.