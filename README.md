# AIIS — AI and Information Security

中文課名：**人工智慧與資訊安全**

Repository: `2026.AI_Cybersecurity_Course_`

## Canonical Course Identity

本課程正式使用：

```text
AIIS
= AI and Information Security
```

課程文件、Lab、YAML、投影片與 GitHub evidence 採一致識別規則：

```text
AIIS_L0
AIIS_L1
AIIS_L2
...
AIIS_L16
```

其中 **AIIS_L0 是課程導論 / Orientation**；AIIS_L1–AIIS_L16 為後續正式教學序列。

## Master Course Story

```text
AIIS_L0 — Understand the AI Revolution and Security Mission
        ↓
BUILD
        ↓
LEARN
        ↓
ATTACK
        ↓
DEFEND
        ↓
GOVERN
```

AI 是能力，Information Security 是主線。學生持續擴充同一個 `AI Weather Security Center`，完成從 AI-assisted development、ML/DL、授權 Red Team、Blue Team remediation 到 ISO 27001 / Risk Governance 的完整工程循環。

## AIIS_L0 — AI Revolution × Information Security

完整規劃見 [`Introduction/README.md`](Introduction/README.md)。

AIIS_L0 的故事線：

```text
Four Industrial Revolutions
工業 → 能源 → 資訊 → AI
          ↓
AI Revolution
          ↓
ANI → AGI → ASI
 │
 ├─ Discriminative AI
 ├─ Generative AI
 └─ Agentic AI
          ↓
AI Can Analyze / Generate / Act
          ↓
Information Security Matters
          ↓
Asset → Threat → Vulnerability → Risk
          ↓
AI Weather Security Center
          ↓
CWA Open Data
          ↓
AI Engineering Toolchain
```

Toolchain overview: GitHub、Antigravity、Vibe Coding、Gemini、Codex、Multi-Agent、Vercel、Kali、TryHackMe / Local Cyber Range。

## Primary Technology Stack

- Python / FastAPI
- SQLite（Local / Lab）/ SQLAlchemy
- pandas / scikit-learn
- PyTorch
- pytest
- Git / GitHub
- Antigravity / AI Coding Agent
- Gemini / Codex
- Multi-Agent workflow
- Kali Linux
- TryHackMe / authorized cyber range
- Vercel（Secure production/demo deployment；不作公開攻擊靶場）

## Canonical Course Sequence

| ID | Theme | Course Phase |
|---|---|---|
| [AIIS_L0](Introduction/) | AI Revolution × Information Security | ORIENTATION |
| [AIIS_L1](Lesson1/) | Course Foundations / AI Security Engineer Mindset | INTRO |
| [AIIS_L2](Lesson2/) | AI Security Engineer Toolbox — Prompt / Vibe Coding / Antigravity / GitHub | BUILD |
| [AIIS_L3](Lesson3/) | Python FastAPI Weather Security Center | BUILD |
| [AIIS_L4](Lesson4/) | How to Build an AI Cybersecurity Project | BUILD |
| [AIIS_L5](Lesson5/SESSION_05_SUPERVISED_ML_I.md) | Supervised ML I — Classification Foundations | LEARN |
| [AIIS_L6](Lesson6/) | Supervised ML II — Tree Models | LEARN |
| [AIIS_L7](Lesson7/) | Supervised ML III — Security Evaluation | LEARN |
| [AIIS_L8](Lesson8/) | Midterm AI Security Engineering Review | REVIEW |
| [AIIS_L9](Lesson9/) | Deep Learning I — Neural Networks for Security | LEARN |
| [AIIS_L10](Lesson10/) | Deep Learning II — Security Sequence Analysis | LEARN |
| [AIIS_L11](Lesson11/) | AI Red Team I — Learn the Attack in TryHackMe | ATTACK |
| [AIIS_L12](Lesson12/) | AI Red Team II — Prove it in Our Weather Cyber Range | ATTACK |
| [AIIS_L13](Lesson13/) | AI Blue Team — Fix Our Code with OWASP Secure Coding | DEFEND |
| [AIIS_L14](Lesson14/) | ISO 27001 × Risk Management | GOVERN |
| [AIIS_L15](Lesson15/) | Final Project Demo I | FINAL |
| [AIIS_L16](Lesson16/) | Final Project Demo II & Course Closure | FINAL |

## Shared Project — AI Weather Security Center

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

## Required Teaching Contract

Every AIIS Lesson / Part uses:

1. **Concept**
2. **Security Meaning**
3. **Practical Example / Lab**
4. **Antigravity YAML Prompt**
5. **Test / Evidence**
6. **Reflection**

YAML task IDs follow the same namespace, for example:

```text
AIIS_L0_LAB01
AIIS_L3_LAB02
AIIS_L12_LAB01
```

Core AI workflow:

```text
Prompt → Plan → Code → Run → Test → Review → Fix
```

Core security workflow:

```text
Observe → Hypothesis → Authorized Test → Evidence → Root Cause → Fix → Regression Test
```

## Knowledge Preservation Contract

原 Weather Web 課程的重要安全知識全部保留並重新分配到 AIIS spiral learning：Password Hashing、Authentication、Session Security、Authorization / RBAC / IDOR、Injection、XSS、CSRF、Input Validation、API Security、Dependency Risk、Logging、Safe Error Handling、Threat Modeling、OWASP Secure Coding、ISO 27001 / Risk。

```text
BUILD → ATTACK → DEFEND → GOVERN
```

## Safety Boundary

Offensive security 僅限 localhost、自有 VM / Docker、教師指定靶機、TryHackMe / CTF 或其他明確授權環境。公開可存取不代表授權攻擊。Vercel / production deployment 不作 classroom exploitation target。

Core statements:

> **AI is the capability. Information Security is the discipline.**

> **AI proposes. Human understands. Security validates.**

> **Learn it in the Range. Prove it in our Lab. Fix it in our Code.**
