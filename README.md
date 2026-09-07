# AIIS — AI and Information Security

中文課名：**人工智慧與資訊安全**

Repository: `2026.AI_Cybersecurity_Course_`

## Canonical Course Identity

本課程正式使用：

```text
AIIS = AI and Information Security
```

`AIIS_L0` 是課程導論 / Orientation；`AIIS_L1–AIIS_L16` 為正式 16 課教學序列。

# MASTER CURRICULUM CONTRACT — 2026-09-07

> **16-Lesson Master Curriculum 是本專案最高層課程約束。**

任何單一 Lesson、Lab、投影片、工具或新技術的優化，都不得反過來改變 16 課總體架構。若內容超出該 Lesson 的責任邊界，應移至正確 Lesson，或標記為 `Further Exploration / Optional`，不得任意增加必修支線。

課程固定聚焦：

> **AI for Security / AI-assisted Security Engineering**

不擴張成獨立的 `Security for AI` 課程支線。

正式課程 **不安排 Reinforcement Learning (RL)**。RL 不屬於 AIIS_L1–L16 必修內容；若未來文件提及 RL，視為歷史規劃或 Optional/Further Exploration，不得占用正式 Lesson。

## Master Course Story

```text
AIIS_L0 — ORIENTATION
        ↓
BUILD → MANAGE → UNDERSTAND → SECURE
        ↓
LEARN (ML / DL)
        ↓
ATTACK
        ↓
DEFEND
        ↓
GOVERN
        ↓
DEMO
```

AI 是能力，Information Security 是主線。學生持續使用同一個 `AI Weather Security Center`，逐步完成 AI-assisted development、工程管理、程式理解、Secure SDLC、ML/DL、授權 Red Team、Blue Team remediation、Risk Governance 與成果展示。

# Canonical 16-Lesson Sequence

| ID | Canonical Theme | Phase |
|---|---|---|
| AIIS_L0 | AI Revolution × Information Security | ORIENTATION |
| **AIIS_L1** | **BUILD — Build Prompt → AI Weather Security Center → `WORKING ✓ → SECURE ?`** | BUILD |
| **AIIS_L2** | **MANAGE — Antigravity × Git × GitHub × AI-assisted Engineering Workflow** | MANAGE |
| **AIIS_L3** | **UNDERSTAND — Python × FastAPI × API × HTTP × JSON × Web App** | UNDERSTAND |
| **AIIS_L4** | **SECURE — `SCAN → FIND → PROPOSE → REVIEW → FIX → TEST → RE-SCAN → VERIFY`** | SECURE |
| AIIS_L5 | Supervised ML I — Classification Foundations | LEARN |
| AIIS_L6 | Supervised ML II — Tree Models | LEARN |
| AIIS_L7 | Supervised ML III — Security Evaluation | LEARN |
| AIIS_L8 | Midterm AI Security Engineering Review | REVIEW |
| AIIS_L9 | Deep Learning I — Neural Networks for Security | LEARN |
| AIIS_L10 | Deep Learning II — Security Sequence Analysis | LEARN |
| AIIS_L11 | AI Red Team I — Learn the Attack in TryHackMe / Authorized Range | ATTACK |
| AIIS_L12 | AI Red Team II — Prove It in Our Weather Cyber Range | ATTACK |
| AIIS_L13 | AI Blue Team — OWASP Secure Coding × Verified Repair | DEFEND |
| AIIS_L14 | ISO 27001 × Risk Management | GOVERN |
| AIIS_L15 | Final Project Demo I | FINAL |
| AIIS_L16 | Final Project Demo II & Course Closure | FINAL |

## L1–L4 Responsibility Boundary

The first four lessons form one continuous engineering spine using the same Weather Security Center.

```text
L1 BUILD
Build Prompt → Working Weather Security Center
WORKING ✓ → SECURE ?
        ↓
L2 MANAGE
Antigravity → Project → Files → Diff → Git → Commit → GitHub → History
        ↓
L3 UNDERSTAND
Python → FastAPI → HTTP/API → JSON → Frontend/Backend → Data Flow
        ↓
L4 SECURE
SCAN → FIND → PROPOSE → REVIEW → FIX → TEST → RE-SCAN → VERIFY
```

### AIIS_L1 owns
- first structured Build Prompt
- teacher-led Antigravity build experience
- first working Weather Security Center
- security mindset: Asset / Threat / Vulnerability / CIA / Risk
- `WORKING ≠ SECURE`
- AI Builder → AI Security Analyst
- evidence and human verification

L1 does **not** own detailed Git/GitHub workflow, Python internals, or formal automated scan/remediation.

### AIIS_L2 owns
- Antigravity engineering workflow
- project/workspace/files
- controlled AI change
- inspect changes / diff
- Git repository and history
- commit / meaningful commit message
- GitHub synchronization and engineering memory
- human review before recording AI changes

L2 does **not** become a deep Python lesson or security scanning lesson.

### AIIS_L3 owns
- Python foundations needed by the project
- FastAPI structure
- HTTP / API / JSON
- frontend ↔ backend
- request / response / data flow
- understanding the Weather Security Center code students already manage

L3 does **not** become the Red Team lesson.

### AIIS_L4 owns
- source-code-oriented security scanning
- representative scanner workflow (Semgrep as primary teaching tool)
- finding triage
- AI-assisted remediation proposal
- human review
- minimal fix
- tests
- re-scan and verification

Core epistemic rules remain:

```text
AI FINDING ≠ CONFIRMED FINDING
SCANNER FINDING ≠ CONFIRMED VULNERABILITY
BUG ≠ VULNERABILITY ≠ RISK
```

# Shared Project — AI Weather Security Center

The Weather Security Center is **not a one-lesson demo**. It is the persistent semester lab.

```text
L1   Build it
 ↓
L2   Manage it
 ↓
L3   Understand it
 ↓
L4   Secure it
 ↓
L5–L7   Learn ML with security-relevant data
 ↓
L9–L10  Learn DL for security analysis
 ↓
L11      Learn offensive techniques in authorized range
 ↓
L12      Validate concepts in our isolated Weather Cyber Range
 ↓
L13      Repair verified weaknesses and regression-test
 ↓
L14      Translate technical findings into risk governance
 ↓
L15–L16  Demonstrate the complete AI Security Engineering project
```

Representative architecture:

```text
CWA Open Data / Fake Sensor when needed
        ↓
Python + FastAPI
        ↓
SQLite / SQLAlchemy
        ↓
Dashboard + Users + Security Events
        ↓
ML / DL Security Analysis
        ↓
Authorized Red-Team Validation
        ↓
Blue-Team Repair + Regression Test
        ↓
Risk Governance
```

# Scope-Control Rule

To prevent curriculum expansion:

1. Each Lesson has one primary teaching mission.
2. Prefer one representative implementation/tool rather than many competing implementations.
3. Alternatives may be mentioned as `Further Exploration`.
4. A new tool must not create a new mandatory curriculum branch.
5. L1–L4 must not consume the time reserved for ML, DL, Red Team, Blue Team, Governance or Final Project.
6. Supervised ML remains three lessons: L5–L7.
7. Deep Learning remains two lessons: L9–L10.
8. Reinforcement Learning is explicitly excluded from the formal curriculum.
9. L11–L12 remain authorized Red Team lessons.
10. L13 remains Blue Team repair; L14 remains governance; L15–L16 remain final demos.

# Required Teaching Contract

Every AIIS Lesson / Part uses:

1. **Concept**
2. **Security Meaning**
3. **Practical Example / Lab**
4. **Antigravity YAML Prompt**
5. **Test / Evidence**
6. **Reflection**

Core AI workflow:

```text
Prompt → Plan → Code → Run → Test → Review → Fix
```

Core Secure SDLC progression introduced in L1 and formally practiced in L4:

```text
BUILD → SCAN → FIND → PROPOSE → REVIEW → FIX → TEST → RE-SCAN → VERIFY → REPORT
```

Core authorized security workflow:

```text
Observe → Hypothesis → Authorized Test → Evidence → Root Cause → Fix → Regression Test
```

# Knowledge Preservation Contract

重要安全知識採 spiral learning，不因 L1–L4 重新分工而刪除：Password Hashing、Authentication、Session Security、Authorization / RBAC / IDOR、Injection、XSS、CSRF、Input Validation、API Security、Dependency Risk、Logging、Safe Error Handling、Threat Modeling、OWASP Secure Coding、ISO 27001 / Risk。

它們依課程階段逐步深化，而不是全部塞入前四課。

# Safety Boundary

Offensive security 僅限 localhost、自有 VM / Docker、教師指定靶機、TryHackMe / CTF 或其他明確授權環境。公開可存取不代表授權攻擊。Vercel / production deployment 不作 classroom exploitation target。

# Canonical Statements

> **AI is the capability. Information Security is the discipline.**

> **AI BUILDS. HUMAN VERIFIES.**

> **AI changes. Git remembers. Human decides.**

> **AI proposes. Human understands. Security validates.**

> **Learn it in the Range. Prove it in our Lab. Fix it in our Code.**

---

## Consistency Note — 2026-09-07

Older Lesson1–Lesson4 README files may describe earlier allocations such as toolbox content in L1, full Weather App construction in L2, Red Team in L3, or Blue Team in L4. Those allocations are **superseded by this Master Curriculum and the latest canonical `_myplan_` documents**.

Until each older Lesson README is rewritten, use this priority order:

```text
1. Root README — Master Curriculum Contract
2. Latest canonical _myplan_ document for the Lesson
3. LessonX/README.md
4. Historical planning documents
```

Any conflict must be resolved in favor of the higher-priority source.