# AIIS_L0 — AI Revolution × Information Security

Course: **AIIS — AI and Information Security（人工智慧與資訊安全）**

AIIS_L0 是整門課的導論與世界觀建立課。這一課不急著深入 Python、FastAPI 或 ML 公式，而是先回答：我們正處在哪一波技術革命？AI 為什麼改變資訊安全？這門課接下來 16 個 Lessons 要怎麼串成一條完整工程主線？

## Course Story

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
          ↓
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

## Part 1 — Why AIIS?

AIIS 不把 AI 與 Information Security 分成兩條互不相干的課。

核心觀念：

> **AI is the capability. Information Security is the discipline.**

現代 AI 系統同時包含 Software、API、Database、Identity、Cloud、Data、Models、Agents 與 Automation，因此安全不能只看模型準確率，也要看帳號、資料、權限、輸入輸出、部署與治理。

## Part 2 — Four Industrial Revolutions

用四次革命建立技術演進的大圖：

| Revolution | 核心能力 | 代表性技術 |
|---|---|---|
| Industrial Revolution | 放大體力 / 機械能力 | Steam, Machinery |
| Energy Revolution | 放大能源使用 | Electricity, Oil, Mass Production |
| Information Revolution | 放大資訊處理 | Computer, Internet, Software |
| AI Revolution | 放大認知與智慧能力 | Machine Learning, Generative AI, AI Agents |

核心問題：

> 蒸汽機放大人的力量，電力放大能源使用，電腦放大資訊處理，那 AI 放大的是什麼？

答案：**Intelligence / Cognitive Capability**。

## Part 3 — AI Revolution: ANI → AGI → ASI

```text
Phase 1 — ANI
Artificial Narrow Intelligence
        ↓
Phase 2 — AGI
Artificial General Intelligence
        ↓
Phase 3 — ASI
Artificial Superintelligence
```

本課將 ANI 再用一個「教學發展框架」理解為三個 stages：

```text
ANI
├── Discriminative AI
├── Generative AI
└── Agentic AI
```

### Discriminative AI
輸入資料，輸出 classification / score / prediction。

Security examples:
- URL → Legitimate / Phishing
- Network Traffic → Normal / Attack
- Security Event → Normal / Suspicious

這會連到 AIIS 的 Supervised ML / DL lessons。

### Generative AI
Prompt → Text / Code / Image / Audio / Video。

課堂工具例如 Gemini、ChatGPT、Codex 等。

### Agentic AI
從「回答」走向「規劃並執行」。

```text
Goal
 ↓
Plan
 ↓
Use Tools
 ↓
Read / Write Code
 ↓
Run Tests
 ↓
Observe
 ↓
Fix
```

Antigravity 與 coding agents 在 AIIS 中主要放在這個位置。

> ANI → Discriminative / Generative / Agentic 是本課採用的教學框架，不主張為學界唯一正式分類。AGI / ASI 的定義與實現時間仍具有研究與社會討論空間。

## Part 4 — Why AI Makes Security More Important

```text
Traditional Software
Human → Software → Computer

Agentic AI
Human → AI Agent → Tools → Code / API / Database / Cloud
```

AI 從「分析」進到「生成」，再進到「執行」，能力越大，安全責任越大。

> **AI capability ↑ → Security responsibility ↑**

## Part 5 — Asset, Threat, Vulnerability, Risk：小偷故事

用生活例子先講清楚 risk language。

### Asset
可偷、而且有價值的東西：現金、手機、電腦、珠寶。

### Threat
可能造成傷害的來源：**小偷**。

### Vulnerability
弱點：錢沒收好、門沒鎖、窗戶沒關。

### Risk
Threat 利用 Vulnerability 影響 Asset 後，可能造成的損失。

```text
Asset
值錢的東西
   +
Threat
小偷
   +
Vulnerability
錢沒放好
   ↓
Risk
被偷造成的可能損失
```

再映射回 Information Security：

| 生活情境 | Information Security |
|---|---|
| 現金 / 珠寶 | Data / Account / API Key / Model |
| 小偷 | Attacker / Threat Actor |
| 錢沒放好 | Vulnerability / Weak Control |
| 被偷造成損失 | Risk / Impact |

後續 AIIS_L13 再進一步介紹 Likelihood、Impact、Control、Residual Risk。

## Part 6 — What Information Security Protects

CIA Triad：

- Confidentiality — 誰可以看？
- Integrity — 誰可以改？資料是否被錯誤或惡意修改？
- Availability — 需要時服務能不能使用？

這三個目標會貫穿 AI Weather Security Center。

## Part 7 — Semester Project: AI Weather Security Center

本課使用 **中央氣象署 CWA Open Data** 作為真實資料來源之一，建立一個從 Open Data 到 Web App、ML/DL、Red Team、Blue Team、Risk Governance 的共同專案。

```text
CWA Open Data
      ↓
Python / FastAPI
      ↓
SQLite / SQLAlchemy
      ↓
Dashboard + Users + Security Events
      ↓
Supervised ML / Deep Learning
      ↓
Authorized Security Validation
      ↓
Blue-Team Repair
      ↓
Risk Governance
```

可使用的 weather features 依實際 CWA dataset/API 而定，例如 temperature、humidity、rainfall、wind、pressure、timestamp 等。

## Part 8 — AIIS Toolchain Overview

Lesson 0 只介紹工具角色，不深入按鈕操作。

```text
Idea / Problem
   ↓
Gemini / ChatGPT
理解、討論、規劃
   ↓
Prompt / YAML
工程規格
   ↓
Antigravity / Codex
Agentic Coding
   ↓
Multi-Agent
Architect / Builder / Reviewer / Tester
   ↓
GitHub
Code + History + Evidence + Documentation
   ↓
Vercel
Secure Demo / Deployment
   ↓
Kali / TryHackMe / Local Cyber Range
Authorized Security Validation
```

### GitHub
不只是放程式碼，而是課程的工程記憶、版本、證據與可重現性中心。

### Antigravity
主要 AI coding agent 之一：Read Repo → Plan → Code → Run → Test → Fix。

### Vibe Coding
自然語言驅動的 AI-assisted development workflow；AIIS 強調 Vibe Coding 必須加上 Requirements、Tests、Review 與 Security Validation。

### Gemini Account
用於 AI explanation、brainstorming、planning、content / code assistance；實際可用功能依學生帳號與當期服務為準。

### Codex
用於 AI-assisted software engineering / coding-agent 類任務，與 Antigravity 一起讓學生理解 Agentic Coding。

### Multi-Agent
以角色分工理解 AI 工程：Architect → Builder → Security Reviewer → Tester。最終責任仍由人負責。

### Vercel
Secure production/demo deployment；不是公開攻擊靶場。

## Part 9 — First AI-assisted Lab

第一個 Lab 使用 synthetic security events，不碰真實帳號或外部系統。

```text
login_success
login_failed
login_failed
login_failed
        ↓
Python Security Event Analyzer
        ↓
Count / Rule / Warning
```

### Antigravity YAML Prompt

```yaml
course:
  id: AIIS
  name: AI and Information Security

lesson:
  id: AIIS_L0
  title: AI Revolution and Information Security

task:
  id: AIIS_L0_LAB01
  title: Build a minimal Python security event analyzer
  role: beginner_python_security_engineer

context:
  project: AI Weather Security Center
  language: Python
  environment: local_only

learning_objectives:
  - understand that security systems generate events
  - distinguish normal and suspicious behavior conceptually
  - experience AI-assisted software development
  - learn Prompt to Plan to Code to Test workflow

requirements:
  - accept synthetic login_success and login_failed events
  - count total events
  - count successful logins
  - count failed logins
  - print a warning when failed login count reaches 3 or more

security_requirements:
  - use only synthetic classroom data
  - do not use real usernames or passwords
  - do not connect to external systems

implementation_workflow:
  - inspect the repository first
  - state assumptions
  - create a minimal implementation plan
  - implement the smallest readable Python program
  - add simple tests
  - run the program
  - run tests
  - explain results
  - summarize limitations

tests:
  - one successful login produces no warning
  - two failed logins produce no warning
  - three failed logins produce a warning
  - five failed logins still produce a warning

deliverables:
  - security_event_analyzer.py
  - test_security_event_analyzer.py
  - README update

final_report:
  include:
    - files_created
    - assumptions
    - detection_logic
    - test_results
    - known_limitations
```

## Part 10 — Reflection

老師不只問「程式跑了嗎」，而要追問：

1. 為什麼 3 failed logins 被判 suspicious？— 因為目前是人定義的 Rule。
2. 正常使用者連續打錯三次會怎樣？— 可能形成 False Positive。
3. 攻擊者慢慢嘗試會怎樣？— 單純計數 rule 可能失效，引出 time window、feature engineering、ML 與 sequence analysis。

## Part 11 — AIIS Teaching Figure / PPT Visual System

AIIS 投影片與教學圖不採「任意生成一張圖」的方式，而是先理解 lecture content，再判斷其所屬 Lesson、抽取教學概念、選擇 visualization，再套用 AIIS 視覺語言與教師角色。

```text
Lecture Content
      ↓
Understand Meaning
      ↓
Detect AIIS Lesson
      ↓
Extract Teaching Concepts
      ↓
Choose Visualization Type
      ↓
Choose 煥哥 Expression / Teaching Pose
      ↓
Generate AIIS Figure / Slide
```

### AIIS PPT / Figure Style

- 16:9 landscape
- warm ivory / off-white background
- deep teal / navy / cyan 為主色
- orange / coral red 作重點與警示
- rounded cards、流程箭頭、簡化圖示、架構圖與教學資訊圖表
- medium-high information density，但保留可讀性與留白
- Traditional Chinese 為主，必要時保留 English technical terms
- 避免 dark cyberpunk、過度 neon、無意義 Matrix code、過多裝飾

### Instructor Character — 煥哥

以指定教師參考照片作為固定角色身份，但**不能每頁只貼相同靜態頭像**。應依內容重畫成相同人物特徵，並調整表情與專業教學動作：

| Teaching Context | Pose / Expression |
|---|---|
| Introduction | 歡迎、open palm |
| Explanation | 指向圖表 / 白板 |
| Important Concept | 舉食指、focused |
| Comparison | 左右兩側比較 |
| Warning / Security | 嚴肅提醒、caution gesture |
| Coding | 筆電旁示範 code |
| Investigation | 分析 evidence / magnifier |
| Red Team | 專業 security analyst |
| Blue Team | Code review / shield / checklist |
| Governance | Executive risk review |
| Reflection | 思考姿勢 / question mark |
| Closing | Wave / thumbs-up |

### Lecture-aware Figure Generator YAML

完整 reusable YAML 規格放在：

[`AIIS_L0_FIGURE_GENERATOR.yaml`](AIIS_L0_FIGURE_GENERATOR.yaml)

這份 YAML 會：

1. 讀取 `lecture_content`
2. 自動判斷 primary / secondary AIIS Lesson
3. 抽取 3–7 個 key concepts
4. 在 concept map / process flow / comparison / architecture / timeline / risk model / lab workflow 等類型中選擇最適合的 visual form
5. 根據 lecture semantic context 選擇「煥哥」的表情與教學動作
6. 套用 AIIS 的固定 visual style
7. 執行 conceptual / visual / safety quality checks

這份 YAML 後續可直接給 Antigravity、Gemini、Codex 或其他 AI Agent 作為 figure / slide generation 的 canonical prompt contract。

## AIIS Course Direction

```text
AIIS_L0
Understand the Revolution and Mission
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

Core statements:

> **AI is the capability. Information Security is the discipline.**

> **AI proposes. Human understands. Security validates.**

> **Learn it in the Range. Prove it in our Lab. Fix it in our Code.**

## Required Teaching Contract

後續每一個 AIIS Lesson / Part 都採：

1. Concept
2. Security Meaning
3. Practical Example / Lab
4. Antigravity YAML Prompt
5. Test / Evidence
6. Reflection

Offensive security 僅限 localhost、自有 VM / Docker、教師指定系統、TryHackMe / CTF 或其他明確授權環境。