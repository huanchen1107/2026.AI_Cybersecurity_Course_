# 2026.AI_Cybersecurity_Course_

## Master Course Story

本課程正式採用 **16 Lessons / 16 Sessions** 一體化主線：

```text
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

AI 是能力，Cybersecurity 是主線。學生不是每週換一個工具，而是持續擴充同一個 `AI Weather Security Center`，最後完成從開發、機器學習、深度學習、授權紅隊、藍隊修補到 ISO 27001 風險治理的完整工程循環。

## Primary Technology Stack

- Python / FastAPI
- SQLite（Local / Lab）/ SQLAlchemy
- pandas / scikit-learn
- PyTorch
- pytest
- Git / GitHub
- Antigravity / AI Coding Agent
- Kali Linux
- TryHackMe / authorized cyber range
- Vercel（Secure production/demo deployment；不作公開攻擊靶場）

Production database 可依部署需求使用 managed PostgreSQL；課堂 Local / Cyber Range 優先使用 SQLite。

## Canonical 16 Lessons

| Lesson | Theme | Course Phase |
|---|---|---|
| [Lesson 1](Lesson1/) | Course Introduction — AI × Cybersecurity | INTRO |
| [Lesson 2](Lesson2/) | AI Security Engineer Toolbox — Prompt / Vibe Coding / Antigravity / GitHub | BUILD |
| [Lesson 3](Lesson3/) | Python FastAPI Weather Security Center | BUILD |
| [Lesson 4](Lesson4/) | How to Build an AI Cybersecurity Project | BUILD |
| [Lesson 5](Lesson5/SESSION_05_SUPERVISED_ML_I.md) | Supervised ML I — Classification Foundations | LEARN |
| [Lesson 6](Lesson6/) | Supervised ML II — Tree Models | LEARN |
| [Lesson 7](Lesson7/) | Supervised ML III — Security Evaluation | LEARN |
| [Lesson 8](Lesson8/) | Midterm AI Security Engineering Review | REVIEW |
| [Lesson 9](Lesson9/) | Deep Learning I — Neural Networks for Security | LEARN |
| [Lesson 10](Lesson10/) | Deep Learning II — Security Sequence Analysis | LEARN |
| [Lesson 11](Lesson11/) | AI Red Team I — Learn the Attack in TryHackMe | ATTACK |
| [Lesson 12](Lesson12/) | AI Red Team II — Prove it in Our Weather Cyber Range | ATTACK |
| [Lesson 13](Lesson13/) | AI Blue Team — Fix Our Code with OWASP Secure Coding | DEFEND |
| [Lesson 14](Lesson14/) | ISO 27001 × Risk Management | GOVERN |
| [Lesson 15](Lesson15/) | Final Project Demo I | FINAL |
| [Lesson 16](Lesson16/) | Final Project Demo II & Course Closure | FINAL |

> Migration note: repository 原先以 Introduction + Lesson1–Lesson5 表示五個大型模組。舊知識內容保留作為 legacy/source material；新版 canonical 課程以 Lesson1–Lesson16 為準，詳見 `_myplan_/2026-09-05-lesson-directory-migration.md`。

## Shared Project — AI Weather Security Center

```text
Weather API / Fake Sensor
        ↓
     FastAPI
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

## Cyber Range Architecture

```text
GitHub
  ├── Secure Production App
  │       ↓
  │     Vercel
  │   Demo / non-destructive verification only
  │
  └── Local Cyber Range
          ↓
      Docker / VM
          ↓
      Lab-only vulnerable targets
```

TryHackMe / CTF 用於學習標準化、明確授權的攻擊技術；學生再將方法移轉到自己的 Local Weather Cyber Range：

> **Learn it in the Range. Prove it in our Lab. Fix it in our Code.**

## Required Teaching Contract

每一個 Lesson / Part 都必須依下列順序設計：

1. **Concept** — 先講清楚概念、why、與前後課的關係
2. **Security Meaning** — 對資安的意義、trust boundary 與風險
3. **Practical Example / Lab** — 可觀察、可驗證、可重現
4. **Antigravity YAML Prompt** — 可直接交給 AI coding agent 實作
5. **Test / Evidence** — tests、metrics、log、report、screenshots 或 Git evidence
6. **Reflection** — 學生必須能解釋結果，而不是只複製 AI

Antigravity YAML 至少包含：`task`、`context`、`learning_objectives`、`requirements`、`security_requirements`、`implementation_workflow`、`tests`、`deliverables`、`final_report`。

核心 AI workflow：

```text
Prompt → Plan → Code → Run → Test → Review → Fix
```

核心資安 workflow：

```text
Observe → Hypothesis → Authorized Test → Evidence → Root Cause → Fix → Regression Test
```

## Knowledge Preservation Contract

原 Weather Web 課程的重要知識不可因 Python migration 消失：Password Hashing、Authentication、Session Security、Authorization / RBAC / IDOR、SQL Injection、XSS、CSRF、Input Validation、API Security、Dependency Risk、Logging、Safe Error Handling、Threat Modeling、OWASP Secure Coding、ISO 27001 / Risk 全部保留，改採 Spiral Learning：

```text
BUILD：先理解與建立控制
   ↓
ATTACK：在授權 Lab 看見失效後果
   ↓
DEFEND：找到 Root Cause 並修補
   ↓
GOVERN：轉換成 Risk / Control / Residual Risk
```

## Safety Boundary

Offensive security 僅限 localhost、自有 VM / Docker、教師指定靶機、TryHackMe / CTF 或其他明確授權環境。公開可存取不代表授權攻擊。Production / Vercel deployment 不作大量掃描、暴力嘗試、DoS 或自動化 exploitation target。

詳細新版規劃、migration 與 knowledge traceability 請見 [`_myplan_`](_myplan_/)。