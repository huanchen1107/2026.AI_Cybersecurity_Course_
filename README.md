# 2026.AI_Cybersecurity_Course_

## Master Course Story

本課程採用 16 週一體化主線：

```text
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

AI 是能力，Cybersecurity 是主線。學生不是每週換一個工具，而是持續擴充同一個 `AI Weather Security Center`，最後完成從開發、機器學習、深度學習、授權紅隊、藍隊修補到 ISO 27001 風險治理的完整工程循環。

## Primary Technology Stack

- Python
- FastAPI
- SQLite（Local / Lab）
- SQLAlchemy
- pandas
- scikit-learn
- PyTorch
- pytest
- Git / GitHub
- Antigravity / AI Coding Agent
- Kali Linux
- TryHackMe / authorized cyber range
- Vercel（Secure production/demo deployment；不作公開攻擊靶場）

Production database 可依部署需求使用 managed PostgreSQL；課堂 Local / Cyber Range 優先使用 SQLite。

## 16-Session Curriculum

| Session | Theme |
|---|---|
| 1 | Course Introduction — AI × Cybersecurity |
| 2 | AI Security Engineer Toolbox — Prompt / Vibe Coding / Antigravity / GitHub |
| 3 | BUILD — Python FastAPI Weather Security Center |
| 4 | How to Build an AI Cybersecurity Project |
| 5 | Supervised ML I — Classification Foundations |
| 6 | Supervised ML II — Tree Models |
| 7 | Supervised ML III — Security Evaluation |
| 8 | Midterm AI Security Engineering Review |
| 9 | Deep Learning I — Neural Networks for Security |
| 10 | Deep Learning II — Security Sequence Analysis |
| 11 | AI Red Team I — Learn the Attack in TryHackMe |
| 12 | AI Red Team II — Prove it in Our Weather Cyber Range |
| 13 | AI Blue Team — Fix Our Code with OWASP Secure Coding |
| 14 | GOVERN — ISO 27001 × Risk Management |
| 15 | Final Project Demo I |
| 16 | Final Project Demo II |

## Shared Project

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

> Learn it in the Range. Prove it in our Lab. Fix it in our Code.

## Required Teaching Pattern

每一個 Lesson / Part 都必須依下列順序設計：

1. Concept — 先講清楚概念與 why
2. Security Meaning — 對資安的意義與風險
3. Practical Example / Lab — 可觀察、可驗證的實例
4. Antigravity YAML Prompt — 可直接交給 AI coding agent 實作
5. Test / Evidence — 測試、輸出、截圖、log、report 或 Git evidence
6. Reflection — 學生必須能解釋，而不是只複製 AI 結果

核心 AI workflow：

```text
Prompt → Plan → Code → Run → Test → Review → Fix
```

核心資安 workflow：

```text
Observe → Hypothesis → Authorized Test → Evidence → Root Cause → Fix → Regression Test
```

## Safety Boundary

Offensive security 僅限 localhost、自有 VM / Docker、教師指定靶機、TryHackMe / CTF 或其他明確授權環境。公開可存取不代表授權攻擊。Production / Vercel deployment 不作大量掃描、暴力嘗試、DoS 或自動化 exploitation target。

詳細新版規劃與知識追蹤請見 `_myplan_`。