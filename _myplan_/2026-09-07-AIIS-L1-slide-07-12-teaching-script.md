# AIIS_L1 — Slides 07–12 Detailed Teaching Script

Date: 2026-09-07
Status: Canonical detailed slide script
Parent plan: `_myplan_/2026-09-07-AIIS-L1-Weather-Security-Center-Detailed-Lecture-Plan.md`

---

## Slide 07 — WATCH THE AGENT WORK

**Purpose:** Shift students from passive amazement to engineering observation.

**On-slide:**
```text
PROMPT → PLAN → PROJECT STRUCTURE → WRITE CODE → INSTALL → RUN → TEST → ERROR? → FIX → EVIDENCE
```

Observation checklist:
- Did the agent plan first?
- What files were created?
- Were data and UI concerns separated?
- Did it actually run the program?
- Did it run tests?
- Did it encounter errors?
- What evidence proves success?

Bottom message: `AI CODING ≠ AI TYPING`

**Visual:** Agent workflow across center; reviewer checklist on right.

**煥哥:** focused reviewer expression; slightly leaning forward; one hand holding a clipboard/tablet, the other pointing to the workflow; gaze follows agent actions.

**Teacher talk:** Do not inspect every Python line yet. Watch the engineering behavior: plan, create files, execute, test, react to errors, and produce evidence. Emphasize: “It says Done” does not mean it is actually done.

**Ask:** What counts as evidence? Expected answers: tests pass, site opens, CWA response received, CSV generated, map displays.

**Live demo cue:** Pause briefly whenever Antigravity creates files, installs dependencies, runs tests, or repairs a runtime error. Do not teach implementation details yet.

**Transition:** “Now the most important moment: does the website actually run?”

---

## Slide 08 — IT RUNS!

**Purpose:** Deliver the first emotional payoff: prompt became working software.

**On-slide:**
- `IT RUNS!`
- `From Prompt to Working Software`
- ✓ CWA Data
- ✓ Temperature
- ✓ Taiwan Map
- ✓ Date Selector
- ✓ Data Table
- ✓ CSV
- ✓ Tests
- large: `WORKING ✓`

**Visual:** Large website screenshot/mockup centered.

**煥哥:** delighted/surprised success expression; one thumbs-up reserved specifically for this success moment; other hand points at the website; gaze toward product.

**Teacher talk:** We began with a requirement prompt. Now we have a real running application. Let students enjoy the “wow” moment before introducing security.

**Ask:** “So… is the project finished?”

**Transition:** Leave only `WORKING ✓` visible, then move on.

---

## Slide 09 — REAL DATA, NOT A TOY

**Purpose:** Show that the system is connected to the real world and therefore has meaningful engineering/security concerns.

**On-slide:**
```text
Taiwan Central Weather Administration
        ↓
Open Data API
        ↓
F-A0010-001
        ↓
JSON
        ↓
Python Program
        ↓
AI Weather Security Center
```

Key phrase: `EXTERNAL REAL-WORLD DATA → OUR SOFTWARE`

**Visual:** CWA/data source on left, our application on right, data arrow between them.

**煥哥:** serious professional expression; left hand points to CWA/data source, right hand points to the app; gaze follows the connecting arrow.

**Teacher talk:** Our program is no longer isolated. It accepts information from another system. When software begins trusting external input, security and validation become more important.

**Ask:** “When your program accepts external data, does security become more important?”

**Transition:** Follow the data through our system.

---

## Slide 10 — FOLLOW THE DATA

**Purpose:** Introduce data-flow thinking as a foundational security-engineering habit.

**On-slide:**
```text
CWA
 ↓
API
 ↓
JSON
 ↓
requests
 ↓
Python Parser
 ↓
DataFrame
 ├─────────────┐
 ↓             ↓
CSV         Streamlit
               ↓
           Taiwan Map
               ↓
              USER
```

Three questions:
1. INPUT — Where does data enter?
2. PROCESS — What does our software do?
3. OUTPUT — Where does it go?

**Visual:** Horizontal/vertical data pipeline with one highlighted “data packet” traveling through the system.

**煥哥:** explanatory/teaching expression; hand visually guides a data packet along the pipeline; gaze follows the flow.

**Teacher talk:** Security engineers learn to follow data. Ask where it enters, how it is transformed, where it is stored, and where it exits.

**Ask:** “If the CWA response format changes, where might the system break?” Follow with: “What if the external data is malformed or unexpected?”

**Key takeaway:** External data should not be trusted blindly.

**Transition:** Two names appear repeatedly in this flow: API and JSON.

---

## Slide 11 — API + JSON IN 5 MINUTES

**Purpose:** Give just enough vocabulary for L1 without stealing L3 content.

**On-slide left:**
```text
OUR PROGRAM
   │ Request
   ▼
  API
   │ Response
   ▼
OUR PROGRAM
```
`API = an interface used by software to communicate with another system.`

**On-slide right:**
```json
{
  "region": "Northern",
  "min_temp": 24,
  "max_temp": 30
}
```
`JSON = a common structured data format used by APIs.`

Bottom:
- `L1: understand the flow`
- `L3: open the code and learn the implementation`

**煥哥:** relaxed reassuring expression; one hand holds a Request card and the other a Response/JSON card; gaze toward students.

**Teacher talk:** Do not master APIs today. Just know our application asks another system for data, receives structured data, then parses it. L3 will open the code and explain requests, parsing, DataFrames, and application structure.

**Transition:** Before we turn to security, show how far a polished weather product could go—without changing our assignment.

---

## Slide 12 — ADVANCED SHOWCASE: LOOK, DON'T BUILD

**Purpose:** Provide inspiration without scope creep.

**On-slide:**
- `HOW FAR COULD THIS GO?`
- large: `LOOK, DON'T BUILD.`
- Advanced reference: `huanchen1107/taiwan-weather-map`

Comparison:
```text
OUR LAB                    ADVANCED SHOWCASE
Simple                     Polished
Understandable             More UI
Security-focused           More Features
```

Reference-only rules:
- ✗ No Clone
- ✗ No Install
- ✗ No Execution
- ✗ No Architecture Analysis
- ✗ No Extra Assignment

**Visual:** Simple L1 weather lab on left, advanced-site visual reference on right.

**煥哥:** appreciative but boundary-setting expression; one hand presents the advanced site, the other uses a natural open-palm stop gesture; gaze toward students.

**Teacher talk:** This repository is visual inspiration only. We are not cloning or running it because our learning goal is not front-end complexity. Explain the course principle: “Do not add features simply because AI makes adding features easy.”

**Core line:** We want one system that is simple enough to understand and rich enough to repeatedly practice security engineering.

**Transition:** Return to our own app. “It has real data. It runs. Antigravity says it is done.” Next slide: `WORKING ✓` — then ask `SECURE ?`.
