# AIIS_L1 — Build Your First AI Weather Security Center
## Detailed Lecture Architecture

Date: 2026-09-07
Status: Canonical detailed L1 teaching plan
Course: AIIS — AI and Information Security（人工智慧與資訊安全）
Position: Lesson 1 / first hands-on AI-assisted security engineering experience

> WORKING ≠ SECURE
>
> AI BUILDS. HUMAN VERIFIES.

---

## 1. Canonical Teaching Story

AIIS_L1 begins with a real build, not a long sequence of definitions.

```text
ONE PROMPT
    ↓
ANTIGRAVITY
    ↓
CWA REAL WEATHER DATA
    ↓
WORKING WEATHER WEBSITE
    ↓
WORKING ✓  BUT SECURE ?
    ↓
ASSET
    ↓
THREAT
    ↓
VULNERABILITY
    ↓
CIA TRIAD
    ↓
RISK
    ↓
AI-ASSISTED RISK REVIEW
    ↓
HUMAN VERIFICATION
    ↓
FUTURE: SCAN → FIND → FIX → TEST → RE-SCAN → VERIFY
```

The website is not a disposable demo. It becomes the shared AI Weather Security Center used and improved across later lessons.

---

## 2. Scope Boundary

L1 intentionally uses Antigravity as a teacher-led live build so students immediately experience Prompt → Working Software. Detailed Antigravity/GitHub engineering workflow belongs to L2. Python/API/Web internals belong to L3. Semgrep source scanning belongs to L4.

L1 therefore does NOT attempt to teach every Antigravity feature, FastAPI/Streamlit implementation detail, SAST tool, offensive technique, or ML algorithm.

### L1 core learning outcomes
Students should be able to:
1. Explain why working software is not automatically secure software.
2. Identify important Assets in a real web/data application.
3. Distinguish Threat from Vulnerability.
4. Apply Confidentiality, Integrity and Availability to the Weather Security Center.
5. Make a basic Likelihood × Impact risk judgment.
6. Use AI as an assistant for risk analysis while separating evidence from assumptions.
7. Explain why human verification remains necessary.

---

## 3. Core Build — Real CWA Weather Website

Teacher uses Antigravity to build a real Python weather-data web application from a single structured prompt.

Required direction:
- Taiwan Central Weather Administration (CWA) Open Data
- F-A0010-001 agricultural 7-day weather forecast dataset
- requests + pandas
- Streamlit web application
- Folium / streamlit-folium Taiwan map
- date selector
- regional temperature table
- normalized CSV output
- environment variable for CWA API key
- tests for parsing/calculation logic
- local execution

Security baseline:
- no hard-coded real API secret
- no intentional backdoor
- no attack scripts
- request timeout and error handling
- do not solve SSL issues by silently disabling certificate verification
- external response validation
- local classroom execution

The purpose is to create a realistic system that can later be scanned, reviewed, repaired and verified.

---

## 4. Advanced Showcase Reference — LOOK, DON'T BUILD

Reference repository:
https://github.com/huanchen1107/taiwan-weather-map

Purpose: show students what a more polished Taiwan weather-map experience can look like and provide optional visual/UI inspiration.

Rules:
- reference only
- do NOT clone in L1
- do NOT install
- do NOT execute
- do NOT analyze its architecture as part of L1
- do NOT add its features to required work
- do NOT allow front-end/UI complexity to distract from AI × Cybersecurity objectives

Message to students:

> LOOK, DON'T BUILD.
>
> Our goal is not to reproduce a sophisticated weather product. Our goal is to build one understandable system and repeatedly learn how to make it more trustworthy and secure.

---

## 5. Three-Hour Lesson Rhythm

| Time | Part | Focus | Evidence/Interaction |
|---|---|---|---|
| 0–15 min | P1 | Welcome / mission | course question |
| 15–35 min | P2 | One Prompt → One Website | Antigravity live demo |
| 35–55 min | P3 | Real CWA Data | data-flow understanding |
| 55–75 min | P4 | Asset | Asset Map |
| 75–95 min | P5 | Threat vs Vulnerability | classification exercise |
| 95–105 min | Break | — | — |
| 105–125 min | P6 | CIA Triad | CIA mapping |
| 125–150 min | P7 | Risk | risk ranking |
| 150–170 min | P8 | AI Security Analyst | AI-assisted review |
| 170–180 min | P9 | Course preview | SCAN → FIX → VERIFY |

---

## 6. Planned Slide Architecture — 30 Slides

### Part A — Opening / Build First
01. AIIS_L1 — Build Your First AI Weather Security Center
02. Today: One Prompt → One Real Website
03. What Are We Actually Building?
04. Before AI: How Many Things Would We Need to Learn?
05. Meet Antigravity — AI Coding Agent
06. The Build Prompt
07. Watch the Agent Work: Prompt → Plan → Files → Code → Run
08. It Runs! The Weather Website Is Alive

### Part B — Real Data / System View
09. This Is Real Data, Not a Toy
10. CWA → API → JSON → Python → CSV → Web App
11. What Is an API? What Is JSON?
12. Advanced Showcase: LOOK, DON'T BUILD

### Part C — Security Turn
13. WORKING ✓
14. SECURE ?
15. Security Starts with: What Are We Protecting?
16. Asset Detective — Find the Assets
17. What Can Go Wrong? — Threat
18. Why Could It Succeed? — Vulnerability
19. Threat ≠ Vulnerability
20. Weather Center Security Cases

### Part D — CIA / Risk
21. CIA Triad
22. Confidentiality — Keep Secrets Secret
23. Integrity — Can We Trust the Weather Data?
24. Availability — What If the Service Stops?
25. From Asset to Risk
26. Likelihood × Impact
27. Not Every Bug Is a Security Vulnerability

### Part E — AI Review / Lab / Closure
28. AI Changes Role: Builder → Security Analyst
29. AI Security Risk Detective — Student Lab
30. BUILD Today → SCAN / FIX / VERIFY Next

---

## 7. Student Evidence Artifact

Each student/team completes one AI Security Risk Report containing:
- Asset
- Threat
- Vulnerability
- CIA impact
- Likelihood
- Impact
- Risk level
- Recommended control
- Evidence
- AI suggestion
- Human review: accept/reject/needs verification and reason

Required reflection:

> AI suggested _______. I accepted / rejected / marked it for verification because _______.

---

## 8. Semester Continuity

```text
L1  Build a real CWA Weather Website + Security Mindset
 ↓
L2  Learn Antigravity + GitHub engineering workflow
 ↓
L3  Understand and extend Python / API / Weather application
 ↓
L4  Semgrep: SCAN → FIND → FIX → RE-SCAN
 ↓
L5–L10  ML / DL security learning
 ↓
L11–L12  Authorized security validation
 ↓
L13  DEFEND / repair / verify
 ↓
L14  GOVERN / risk treatment
 ↓
L15–L16  Integrated final evidence
```

The Weather Security Center remains the common course system whenever practical.

---

## 9. Slide Character Direction — 煥哥

Every slide may use the established AIIS spokesperson/avatar **煥哥** where useful. The character must support the teaching message rather than become decoration.

For every detailed slide script specify:
- expression
- body pose / hand gesture
- gaze direction
- relationship to diagrams or key text

Suggested expression vocabulary:
- welcoming / confident smile
- curious / thinking
- surprised / impressed
- skeptical / questioning
- alert / serious
- detective / examining
- teaching / pointing
- reassuring / guiding
- celebratory / thumbs-up

Avoid repetitive identical poses. Match the character's emotion to the slide narrative, especially the dramatic transition from `WORKING ✓` to `SECURE ?`.

---

## 10. Next Authoring Step

Expand Slides 01–30 into detailed slide scripts. Each slide must contain:
1. Purpose
2. On-slide content
3. Visual composition
4. 煥哥 expression/action/gaze
5. Teacher talk
6. Student question/interaction where useful
7. Transition to next slide
8. Demo/prompt instructions where applicable

This document is the canonical L1 lecture architecture. Detailed slide-script files may be split into manageable groups while preserving this 30-slide order.