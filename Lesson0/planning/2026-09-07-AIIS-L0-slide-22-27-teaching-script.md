# AIIS_L0 — Slides 22–27 Detailed Teaching Script

Date: 2026-09-07
Parent plan: `2026-09-07-AIIS-L0-32-slide-detailed-lecture-plan.md`
Status: Detailed lecture script

## Story

```text
REAL DATA — CWA
      ↓
REAL SYSTEM — AI Weather Security Center
      ↓
SEMESTER JOURNEY
BUILD → LEARN → ATTACK → DEFEND → GOVERN
      ↓
AI-ASSISTED ENGINEERING
Think → Specify → Build → Verify
      ↓
TOOLS HAVE ROLES
      ↓
AGENTIC ENGINEERING LOOP
      ↓
NOW BUILD SOMETHING
```

# Slide 22 — AI Weather Security Center

## Core
**One System. One Semester. Keep Building.**

Start with a small Weather App, then reveal growth:

```text
Weather App
    ↓
+ Database
    ↓
+ Users
    ↓
+ Security Events
    ↓
+ Machine Learning
    ↓
+ Security Testing
    ↓
+ Defense
    ↓
+ Governance
```

Architecture preview:

```text
CWA DATA
   ↓
FastAPI
   ↓
Database + Security Events
   ↓
Dashboard
   ↓
ML / DL
   ↓
Security Analysis
```

Presenter: 煥哥 welcoming/presenting the semester project.

Teacher message: Do not throw away a mini-project every week. The project grows as knowledge grows. Reuse code, data, failures, fixes and evidence across lessons.

Ask why a semester-long system is better than unrelated weekly exercises. Lead to lifecycle, accumulated code/data and visible improvement.

Core slogan:
> **The project grows as your knowledge grows.**
>
> **Secure software is built over time.**

# Slide 23 — Real Data: CWA Open Data

## Core
**Real Data → Real Engineering Problems**

Architecture:

```text
中央氣象署 CWA Open Data
          ↓
      Weather API
          ↓
        Python
          ↓
       FastAPI
          ↓
       Database
          ↓
       Dashboard
```

Potential fields: Temperature / Humidity / Rainfall / Wind / Pressure / Timestamp.

Data lifecycle:

```text
CWA → COLLECT → STORE → PROCESS → DISPLAY → LEARN → PROTECT
```

Teacher message: Weather data is real-world data suitable for API, database, time-series, visualization and ML exercises while avoiding starting the course with highly sensitive personal/medical/financial data.

Reuse the same data:
- BUILD: display it
- LEARN: model patterns
- DEFEND: protect integrity
- GOVERN: treat data/service as assets

Retrieval question: If 25°C is maliciously changed to 250°C, no data was stolen. Is it still a security problem? Yes: Integrity.

Accuracy guard: verify current CWA datasets, endpoints, licensing and authentication requirements at implementation time; do not hard-code guessed API details in L0.

# Slide 24 — BUILD → LEARN → ATTACK → DEFEND → GOVERN

This is the canonical AIIS semester roadmap.

```text
BUILD ─→ LEARN ─→ ATTACK ─→ DEFEND ─→ GOVERN
 App      ML/DL     Authorized   Fix/Test    Risk
 API      Detection Validation   Evidence    Control
 DB                                          Policy
```

## BUILD
Build Python + FastAPI + Database + Weather Dashboard.
Core: `能跑 ≠ 安全`.

## LEARN
Use supervised ML / deep learning for security intelligence and pattern recognition.
Core: AI saying “suspicious” does not automatically mean correct.

## ATTACK
Always frame as **Authorized Security Validation**.

```text
AUTHORIZED LAB ONLY
✓ Localhost
✓ Own VM / Docker
✓ Teacher-designated Lab
✓ TryHackMe / CTF
✗ Random public websites
✗ Public production targets without authorization
```

Goal is to validate systems we own/are authorized to test, not attack arbitrary sites.

## DEFEND

```text
Finding → Reproduce → Root Cause → Fix → Test → Evidence
```

Finding a vulnerability is not the end. Fix it and prove the fix.

## GOVERN

```text
Asset → Risk → Control → Evidence → Decision
```

Introduce risk management, controls, policy, ISO 27001 and evidence later.

Key teacher statement:
> BUILD teaches us what the system does. ATTACK shows us where it fails. DEFEND teaches us how to fix it. GOVERN teaches us how to manage it.

LEARN adds AI pattern recognition where simple hand-written rules are insufficient.

# Slide 25 — From Idea to Working System

## Core
AI-assisted engineering changes where students spend effort.

```text
IDEA → THINK → SPECIFY → BUILD → VERIFY → REMEMBER → DEPLOY → VALIDATE
```

AIIS policy:

```text
Understand → Generate → Review → Execute → Verify
```

Explicitly reject:
> ❌ “AI wrote it. I don't know.”

Core:
> **AI-assisted ≠ AI-unverified**

Ask: If AI writes 200 lines in 10 seconds, what should the saved time be used for? Understanding, testing, debugging, review and security.

Teaching statement:
> Move time from typing to thinking, testing and reviewing — not from learning to not learning.

# Slide 26 — Who Does What?

Teach roles, not a logo wall.

```text
THINK
ChatGPT / Gemini
理解、討論、設計
        ↓
SPECIFY
Prompt / YAML
需求、限制、測試
        ↓
BUILD
Antigravity / Codex
Read Repo / Code / Run
        ↓
REMEMBER + VERIFY
GitHub
Code / History / Evidence
        ↓
DEPLOY
Vercel
Secure Demo
        ↓
VALIDATE
Authorized Lab
Security Validation
```

Human remains across the whole pipeline:

```text
HUMAN
├── Understand
├── Decide
└── Verify
```

Role explanations:
- ChatGPT/Gemini: Think with AI
- Prompt/YAML: Specify clearly
- Antigravity/Codex: Build with AI
- GitHub: Code + History + Documentation + Evidence + Collaboration + AI Context
- Vercel: deploy secure demo
- Authorized Lab: security validation

Guard: Public deployment is not an authorized attack target.

Core:
> Tool names may change. Engineering roles and responsibilities matter more than buttons.
>
> **Human understands. Human decides. Human verifies.**

# Slide 27 — Agentic Engineering Loop

Canonical loop:

```text
READ REPO
   ↓
PLAN
   ↓
CODE
   ↓
RUN
   ↓
TEST
   ↓
REVIEW
   ↓
FIX ─────────→ TEST
```

Outer contract:

```text
REQUIREMENT → AI AGENT LOOP → EVIDENCE → HUMAN REVIEW
```

Reject one-shot workflow:

```text
Prompt → Generate 500 lines → Done
```

Teach:
1. Read Repo first — understand architecture, relevant files and boundaries.
2. Plan before Code.
3. Code → Run → Test → Review → Fix.
4. Produce evidence.

Multi-Agent is mentioned only briefly, not expanded into a separate topic:
`Architect Agent → Builder Agent → Security Reviewer → Test Agent`.

Core is separation of responsibility + evidence, not number of agents.

Final three AIIS engineering principles:
> **1. AI proposes.**
>
> **2. Tests verify behavior.**
>
> **3. Human accepts responsibility.**

Transition:
> 講到這裡還全部是投影片。現在我們第一次真的讓 Agent 幫我們做一件事情。

→ **AIIS_L0_LAB01 — Security Event Analyzer**
