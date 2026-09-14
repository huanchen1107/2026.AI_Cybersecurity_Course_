# AIIS_L0 — AI Revolution × Information Security

Course: **AIIS — AI and Information Security（人工智慧與資訊安全）**

AIIS_L0 是整門課的導論與世界觀建立課。這一課先建立「AI 時代背景 → AI 發展 → 資安 → 這學期要做什麼」的完整故事線，再進入後續 AIIS_L1–L16。

## Canonical Lecture Story

```text
4 INDUSTRIAL REVOLUTIONS
工業 → 能源 → 資訊 → AI
        ↓
AI REVOLUTION
        ↓
ANI → AGI → ASI
 │
 ├─ Discriminative AI
 ├─ Generative AI
 └─ Agentic AI
        ↓
AI CAN ANALYZE / GENERATE / ACT
        ↓
SECURITY MATTERS
        ↓
Asset → Threat → Vulnerability → Risk
        ↓
CIA Triad
        ↓
AI WEATHER SECURITY CENTER
        ↓
CWA Open Data
        ↓
AI Engineering Toolchain
        ↓
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

---

# Part 1 — Why This Course? AI × Information Security

先不急著講工具，而是先問學生：

> **我們正在經歷什麼樣的時代改變？**

AIIS 不把 AI 與 Information Security 拆成兩條無關的課。核心觀念是：

> **AI is the capability. Information Security is the discipline.**

現代 AI 系統同時包含 Software、API、Database、Identity、Cloud、Data、Models、Agents 與 Automation。AI 能力越強，安全責任越大。

---

# Part 2 — 四大工業革命 → AI 革命

## 2.1 Four Industrial Revolutions

```text
第一次工業革命
INDUSTRIAL REVOLUTION
機械化 / 蒸汽機
Machine Power
        ↓
第二次工業革命
ENERGY REVOLUTION
電力 / 石油 / 大量生產
Energy Power
        ↓
第三次工業革命
INFORMATION REVOLUTION
Computer / Internet / Software
Information Power
        ↓
第四次工業革命
AI REVOLUTION
Machine Intelligence
Intelligence Power
```

| Revolution | 核心資源 | 人類能力被放大 |
|---|---|---|
| Industrial | Machine | 體力 |
| Energy | Electricity | 能量 |
| Information | Computer + Internet | 資訊處理 |
| AI | Artificial Intelligence | **智慧 / 認知能力** |

課堂核心問題：

> 蒸汽機放大人的力量，電力放大能源使用，電腦放大資訊處理，那 AI 放大的是什麼？

答案：

> **Intelligence / Cognitive Capability**

## 2.2 AI Revolution 的 Three Phases

```text
AI REVOLUTION

Phase 1
ANI
Artificial Narrow Intelligence
        ↓
Phase 2
AGI
Artificial General Intelligence
        ↓
Phase 3
ASI
Artificial Superintelligence
```

### ANI — Artificial Narrow Intelligence

本課再用一個「教學發展框架」把 ANI 理解成三個 stages：

```text
ANI

Stage 1
Discriminative AI
辨識 / 分類 / 預測
        ↓
Stage 2
Generative AI
生成
        ↓
Stage 3
Agentic AI
規劃 / 使用工具 / 執行工作
```

> **重要說明：** ANI → Discriminative / Generative / Agentic 是 AIIS 採用的教學發展框架，不主張為學界唯一正式分類；AGI、ASI 的定義與實現時間也仍具有研究與社會討論空間。

### Stage 1 — Discriminative AI

```text
INPUT
  ↓
AI Model
  ↓
CLASS / SCORE / PREDICTION
```

Security examples：

```text
Email → Spam / Not Spam
URL → Phishing / Legitimate
Network Traffic → Normal / Attack
Security Event → Normal / Suspicious
```

這會連到後續 AIIS 的 Supervised ML / Deep Learning lessons。

### Stage 2 — Generative AI

從「這是什麼？」進入「幫我產生一個東西」。

```text
Prompt
  ↓
Generative AI
  ↓
Text / Code / Image / Audio / Video
```

ChatGPT、Gemini、Codex 等會在這裡第一次出現。

### Stage 3 — Agentic AI

Agentic AI 從「回答」進到「規劃並執行」。

```text
Goal
  ↓
AI Agent
  ↓
Plan
  ↓
Use Tools
  ↓
Read Files
  ↓
Write Code
  ↓
Run Tests
  ↓
Observe Result
  ↓
Fix
```

所以 Antigravity 不只是：

```text
Prompt → Answer
```

而更接近：

```text
Goal → Plan → Act → Observe → Correct → Complete
```

這正好帶出 Vibe Coding / Antigravity / Codex / Multi-Agent。

---

# Part 3 — AI 越強，Security 越重要

以前：

```text
Human
  ↓
Software
  ↓
Computer
```

現在：

```text
Human
  ↓
AI Agent
  ↓
Tools
  ↓
Code / API / Database / Cloud
```

AI 不只是「回答問題」，它開始可以 **Act**。

> **AI capability ↑ → Security responsibility ↑**

這是整門 AIIS 的核心句之一。

---

# Part 4 — 用「小偷偷東西」理解 Cybersecurity Risk

先問學生：

> 如果一個房間什麼值錢的東西都沒有，小偷為什麼要進去？

## ① Asset — 值錢的東西

```text
Asset
= 有價值、需要保護的東西
```

例如：現金、手機、電腦、珠寶。

沒有 Asset，就沒有「要保護什麼」。

## ② Threat — 小偷

```text
Threat
= 可能對 Asset 造成傷害的人、事件或力量
```

生活例：

```text
Threat = 小偷
```

資安例：

```text
Threat = Attacker / Threat Actor
```

## ③ Vulnerability — 錢沒有放好

例如：

```text
錢放在桌上
窗戶沒關
門沒有鎖
```

> **Vulnerability = 可以被 Threat 利用的 weakness。**

## ④ Risk — 最後可能造成的損失

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
東西被偷所造成的可能損失
```

例如：

```text
損失 NT$50,000
資料遺失
工作中斷
隱私外洩
```

映射到 Information Security：

| 小偷故事 | Information Security |
|---|---|
| 現金 / 珠寶 | Data / Account / API Key / Model |
| 小偷 | Attacker / Threat Actor |
| 錢沒收好 | Vulnerability / Weak Control |
| 被偷造成損失 | Risk / Impact |

後續 **AIIS_L13 — ISO 27001 × Risk Management** 再深入：

```text
Risk ≈ Likelihood × Impact
```

並加入 Control、Risk Treatment、Residual Risk。

---

# Part 5 — Information Security 保護什麼？

這時再介紹 CIA Triad：

```text
Confidentiality
誰可以看？

Integrity
誰可以改？資料是否被錯誤或惡意修改？

Availability
需要時能不能用？
```

三個目標會一路貫穿 AI Weather Security Center。

---

# Part 6 — 我們這學期要做什麼？

## AI Weather Security Center

AIIS 全學期不每週換一個 project，而是持續擴充同一個系統。

```text
中央氣象署 CWA Open Data
          ↓
       FastAPI
          ↓
   SQLite / SQLAlchemy
     ┌────┼────┐
     ↓    ↓    ↓
 Weather Users Security Events
          ↓
       Dashboard
          ↓
        ML / DL
          ↓
       Red Team
          ↓
       Blue Team
          ↓
    Risk Governance
```

第一堂只建立 Architecture Vision；後續每一課再增加真正功能與安全能力。

---

# Part 7 — Real Data：中央氣象署 CWA Open Data

課程正式使用 **中央氣象署 CWA Open Data** 作為真實資料來源之一。

```text
CWA Open Data
      ↓
Weather API / Dataset
      ↓
Python
      ↓
FastAPI
      ↓
Database
      ↓
Dashboard
      ↓
ML / Security Analysis
```

後續可依實際 CWA dataset / API 使用：

```text
Temperature
Humidity
Rainfall
Wind
Pressure
Weather Observations
Timestamp
```

這些資料不是只拿來展示：

```text
CWA Data
   │
   ├─→ Dashboard
   ├─→ Database
   ├─→ Supervised ML
   ├─→ Deep Learning
   └─→ Anomaly / Security Scenario
```

因此 Weather Center 是一個真正的 **Data-driven Semester Project**。

---

# Part 8 — 2026 AI Engineer 的工具箱

AIIS_L0 只介紹工具「角色」，不深入操作細節。

```text
Idea
 ↓
Gemini / ChatGPT
思考、理解、規劃
 ↓
Prompt / YAML
把想法變工程規格
 ↓
Antigravity / Codex
Agentic Coding
 ↓
Multi-Agent
不同角色協作
 ↓
GitHub
Version + Memory + Evidence
 ↓
Vercel
Deploy
 ↓
Kali / TryHackMe / Local Cyber Range
Security Validation
```

### Gemini / ChatGPT
用來理解問題、brainstorm、設計、解釋。

### Vibe Coding
不是單一工具名稱，而是一種 AI-assisted development workflow。學生可以用自然語言描述需求，但 AIIS 強調仍必須有 Requirements、Review、Test 與 Security Validation。

### Antigravity
本課主要 Agentic Engineering 工具之一：

```text
Read Repo → Plan → Code → Run → Test → Fix
```

### Codex
另一個 coding agent / software engineering agent，讓學生理解工程任務不一定只能交給單一 AI。

### GitHub
GitHub 不只是放 Code，而是：

```text
Code
History
Evidence
Documentation
Collaboration
AI Context
```

### Multi-Agent

```text
Architect Agent
      ↓
Builder Agent
      ↓
Security Reviewer Agent
      ↓
Test Agent
```

未來不是「一個 Prompt 解決所有事情」，而是不同 Agent 分工，再由人做最終判斷。

### Vercel

```text
GitHub
  ↓
Deploy
  ↓
Web Application
```

但第一堂就建立安全界線：

```text
Vercel
= Secure Demo / Production

Local Docker / VM
= Cyber Range
```

公開可存取不等於授權攻擊。

---

# Part 9 — 第一個 Vibe Coding 體驗

第一個 Lab：**AIIS_L0_LAB01 — Security Event Analyzer**。

學生第一次完整走過：

```text
Human Idea
    ↓
YAML Prompt
    ↓
Antigravity
    ↓
Python
    ↓
Run
    ↓
Test
    ↓
GitHub
```

Synthetic input：

```text
login_success
login_failed
login_failed
login_failed
```

預期功能：

```text
Count events
      ↓
Detect repeated login failures
      ↓
Print simple warning
```

## Canonical Antigravity YAML — AIIS_L0_LAB01

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
  repository_behavior:
    - inspect the current repository before changing files
    - preserve existing course structure
    - keep implementation minimal and readable

learning_objectives:
  - understand that cybersecurity systems generate security events
  - understand the conceptual difference between normal and suspicious behavior
  - experience AI-assisted software development
  - practice Prompt to Plan to Code to Run to Test to Review workflow
  - understand that a detection rule is a human-defined assumption, not absolute truth

requirements:
  input_events:
    allowed_values:
      - login_success
      - login_failed
    example:
      - login_success
      - login_failed
      - login_failed
      - login_failed

  behavior:
    - count total events
    - count successful logins
    - count failed logins
    - print a warning when failed login count reaches 3 or more

  expected_output_fields:
    - total_events
    - login_success
    - login_failed
    - warning

security_requirements:
  - use only synthetic classroom data
  - never use real usernames
  - never use real passwords
  - do not connect to external systems
  - do not perform authentication attempts against real services
  - do not add offensive or scanning functionality

implementation_workflow:
  - inspect the repository first
  - state assumptions before coding
  - create a minimal implementation plan
  - identify the smallest files that must change
  - implement the smallest readable Python program
  - add automated tests
  - run the program
  - run all related tests
  - review the implementation for unnecessary complexity
  - explain what the rule detects
  - explain what the rule cannot detect
  - summarize security limitations

tests:
  required_cases:
    - name: successful_login_only
      input:
        - login_success
      expected_warning: false

    - name: two_failed_logins
      input:
        - login_failed
        - login_failed
      expected_warning: false

    - name: three_failed_logins
      input:
        - login_failed
        - login_failed
        - login_failed
      expected_warning: true

    - name: five_failed_logins
      input:
        - login_failed
        - login_failed
        - login_failed
        - login_failed
        - login_failed
      expected_warning: true

deliverables:
  - security_event_analyzer.py
  - test_security_event_analyzer.py
  - README update describing how to run the lab

acceptance_criteria:
  - all required tests pass
  - no external network access is required
  - code is understandable by beginning Python students
  - warning threshold behavior is explicitly documented
  - limitations are documented

final_report:
  include:
    - assumptions
    - files_created_or_changed
    - implementation_summary
    - detection_logic
    - commands_run
    - test_results
    - known_limitations
    - possible_next_features
```

## Reflection after Lab

老師不只問「程式跑了嗎？」而要追問：

1. 為什麼 3 failed logins 被判定 suspicious？
   - 因為這是目前由人設定的 Rule。
2. 如果正常使用者真的打錯 3 次密碼？
   - 可能產生 **False Positive**。
3. 如果攻擊者每 10 分鐘只試一次？
   - 單純 count rule 可能失效。
4. 接下來需要什麼？
   - Time Window、Feature Engineering、ML、Sequence Analysis。

這些問題會自然銜接到後面的 AIIS ML / DL lessons。

---

# Part 10 — AIIS_L0 最後收斂

最後用一張總圖收斂：

```text
4 INDUSTRIAL REVOLUTIONS
        ↓
     AI REVOLUTION
        ↓
   ANI → AGI → ASI
    │
    ├─ Discriminative AI
    ├─ Generative AI
    └─ Agentic AI
             ↓
        AI CAN ACT
             ↓
     SECURITY MATTERS
             ↓
   AI WEATHER SECURITY CENTER
             ↓
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

核心句：

> **AI is the capability. Information Security is the discipline.**

> **AI proposes. Human understands. Security validates.**

> **Learn it in the Range. Prove it in our Lab. Fix it in our Code.**

AIIS_L0 的故事不是從 AI 定義開始，而是從：

> **人類工業革命 → AI 革命 → Agentic AI → 新的 Security 問題 → 親手建立一個系統來學習這件事**

下一課正式進入：

> **AIIS_L1 — AI Tools × Prompt × Vibe Coding × Antigravity × GitHub**

---

# AIIS Teaching Figure / PPT Visual System

AIIS 的 Figure / PPT 採 Lecture-aware generation：

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

固定 visual language：16:9、warm ivory / off-white、deep teal / navy / cyan、orange / coral highlight、rounded cards、流程箭頭、資訊圖表、Traditional Chinese 為主。

教師角色「煥哥」使用指定參考照片維持人物身份，但應依 lecture semantic context 改變表情與專業上課動作，不應每頁只貼同一張靜態頭像。

完整 reusable Figure Generator YAML：

[`AIIS_L0_FIGURE_GENERATOR.yaml`](AIIS_L0_FIGURE_GENERATOR.yaml)

---

# Required Teaching Contract

後續每一個 AIIS Lesson / Part 都採：

1. Concept
2. Security Meaning
3. Practical Example / Lab
4. Antigravity YAML Prompt
5. Test / Evidence
6. Reflection

核心工程 workflow：

```text
Understand → Generate → Review → Execute → Verify
```

Offensive security 僅限 localhost、自有 VM / Docker、教師指定系統、TryHackMe / CTF 或其他明確授權環境。