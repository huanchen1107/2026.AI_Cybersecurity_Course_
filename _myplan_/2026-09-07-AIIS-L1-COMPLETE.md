# AIIS_L1 — COMPLETE
## AI 資安工程師的第一堂課 / Build Your First AI Weather Security Center

Date: 2026-09-07
Status: **PLANNING COMPLETE / CANONICAL**

> WORKING ≠ SECURE
>
> AI BUILDS. HUMAN VERIFIES.

---

## 1. Completion Decision

AIIS_L1 planning is complete. Do not reopen or expand the required L1 scope unless the course owner explicitly requests a revision.

Canonical L1 purpose:

1. Start with one structured prompt and a teacher-led Antigravity build.
2. Build a real CWA-based AI Weather Security Center.
3. Let students experience `Prompt → Working Software` first.
4. Turn the successful build into the security question `WORKING ✓ → SECURE ?`.
5. Teach Asset → Threat → Vulnerability → CIA → Risk.
6. Change AI role from Builder to Security Analyst.
7. Require evidence and human verification.
8. Leave automated scanning/remediation for the later secure-development sequence.

L1 must remain focused. Detailed Antigravity + GitHub workflow belongs to L2; Python/API internals belong to L3; Semgrep scan/remediation belongs to L4.

---

## 2. Canonical Teaching Flow

```text
ONE PROMPT
    ↓
ANTIGRAVITY
    ↓
CWA REAL DATA
    ↓
WEATHER WEBSITE
    ↓
WORKING ✓
    ↓
SECURE ?
    ↓
ASSET
    ↓
THREAT
    ↓
VULNERABILITY
    ↓
CIA TRIAD
    ↓
LIKELIHOOD + IMPACT
    ↓
RISK
    ↓
AI SECURITY REVIEW
    ↓
EVIDENCE
    ↓
HUMAN VERIFICATION
```

Future engineering loop:

```text
BUILD → SCAN → FIND → PROPOSE → REVIEW → FIX → TEST → RE-SCAN → VERIFY → REPORT
```

---

## 3. Canonical L1 Artifacts

### Main architecture
- `_myplan_/2026-09-07-AIIS-L1-Weather-Security-Center-Detailed-Lecture-Plan.md`

### Detailed 30-slide teaching scripts
- `_myplan_/2026-09-07-AIIS-L1-slide-01-06-teaching-script.md`
- `_myplan_/2026-09-07-AIIS-L1-slide-07-12-teaching-script.md`
- `_myplan_/2026-09-07-AIIS-L1-slide-13-20-teaching-script.md`
- `_myplan_/2026-09-07-AIIS-L1-slide-21-27-teaching-script.md`
- `_myplan_/2026-09-07-AIIS-L1-slide-28-30-teaching-script.md`

### Engineering prompt pack
- `_myplan_/2026-09-07-AIIS-L1-Build-Scan-Remediation-Prompt-Pack.md`

The prompt pack contains:
1. BUILD — create runnable CWA Weather Security Center.
2. SCAN — Semgrep evidence collection without modifying code.
3. REMEDIATION PROPOSAL — analyze findings and propose minimal fixes before implementation.
4. FIX / VERIFY — approved repair, regression tests, re-scan and evidence report.

---

## 4. 30-Slide Storyline

### BUILD FIRST — Slides 01–08
1. Build Your First AI Weather Security Center
2. One Prompt → One Real Website
3. What Are We Building?
4. Before AI, What Would We Need?
5. Meet Antigravity
6. The Build Prompt
7. Watch the Agent Work
8. It Runs!

### REAL DATA — Slides 09–12
9. Real Data, Not a Toy
10. Follow the Data
11. API + JSON in 5 Minutes
12. Advanced Showcase — LOOK, DON'T BUILD

### SECURITY TURN — Slides 13–20
13. WORKING ✓
14. SECURE ?
15. Security Starts with Assets
16. Asset Detective
17. What Can Go Wrong? — Threat
18. Why Could It Succeed? — Vulnerability
19. Threat ≠ Vulnerability
20. Weather Center Security Cases

### CIA + RISK — Slides 21–27
21. CIA Triad
22. Confidentiality
23. Integrity
24. Availability
25. One System, Three Questions
26. From Vulnerability to Risk
27. Risk Ranking / BUG ≠ VULNERABILITY ≠ RISK

### AI REVIEW + EVIDENCE — Slides 28–30
28. AI Changes Role: Builder → Security Analyst
29. AI Security Risk Detective — Student Mini Lab
30. Today We Built It. Next, We Learn to Trust It.

---

## 5. 煥哥 Character Narrative

煥哥 is the teaching spokesperson and must support the lesson narrative rather than serve as repeated decoration.

Character progression:

```text
HOST
 ↓
BUILDER
 ↓
OBSERVER
 ↓
CELEBRATOR
 ↓
SKEPTIC
 ↓
DETECTIVE
 ↓
TEACHER
 ↓
SECURITY ANALYST
 ↓
COACH
 ↓
GUIDE
```

Each slide script specifies expression, pose/action and gaze. Avoid identical poses across consecutive slides. The most important emotional transition is:

`IT RUNS! / WORKING ✓` → skeptical `SECURE ?`

---

## 6. Required Student Evidence

Every student/team must produce an AI Security Risk Detective artifact containing:

| Field | Required |
|---|---|
| Asset | Yes |
| Threat | Yes |
| Vulnerability | Yes |
| CIA impact | Yes |
| Likelihood | Yes |
| Impact | Yes |
| Risk | Yes |
| Recommended control | Yes |
| Evidence | Yes |
| AI suggestion | Yes |
| Human review | Yes |

Mandatory reflection:

> AI suggested _______. I accepted / rejected / marked it NEEDS VERIFICATION because _______.

Teacher's recurring review questions:
- Where is your evidence?
- Is this a fact or an assumption?
- Why did you rank this risk High?

---

## 7. AI / Scanner Epistemic Rules

Students must learn these distinctions:

```text
AI FINDING ≠ CONFIRMED FINDING
SCANNER FINDING ≠ CONFIRMED VULNERABILITY
BUG ≠ VULNERABILITY ≠ RISK
```

Finding status vocabulary:
- CONFIRMED
- LIKELY TRUE POSITIVE
- LIKELY FALSE POSITIVE
- NEEDS VERIFICATION

Remediation decision vocabulary:
- FIX NOW
- VERIFY FIRST
- ACCEPT RISK
- FALSE POSITIVE / NO CHANGE

---

## 8. Safety / Authorization Boundary

L1 and the related prompt pack are for:
- localhost
- student-owned code
- teacher-provided code
- owned isolated VM/container
- explicitly authorized classroom targets

Do not scan or test arbitrary third-party live systems.

The advanced `huanchen1107/taiwan-weather-map` project remains reference/showcase only in L1:
- LOOK, DON'T BUILD
- no clone
- no install
- no execution
- no architecture analysis
- no additional assignment

---

## 9. Exit Ticket

Students answer three questions:

1. What is one Asset in our Weather Security Center?
2. Explain the difference between Threat and Vulnerability.
3. Complete: `AI __________. Human __________.`

Expected final concept:

> AI assists/builds. Human verifies.

---

## 10. Handoff to Next Lessons

```text
AIIS_L1
Build real system + security mindset
        ↓
AIIS_L2
Antigravity + GitHub engineering workflow
        ↓
AIIS_L3
Python + API + JSON + application internals
        ↓
AIIS_L4
Semgrep: SCAN → FIND → PROPOSE → FIX → TEST → RE-SCAN → VERIFY
```

No additional required technology should be inserted into L1 merely because it is interesting. New ideas should normally be routed to the appropriate later lesson or Further Exploration.

---

# AIIS_L1 PLANNING STATUS: COMPLETE ✓

Canonical closing messages:

# WORKING ≠ SECURE
# AI BUILDS. HUMAN VERIFIES.
# BUILD → THINK → VERIFY
