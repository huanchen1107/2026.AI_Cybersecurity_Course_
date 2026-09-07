# AIIS COURSE DESIGN STANDARD
## 2026 AI × Information Security — Canonical Lesson Design Method

Version: 1.0
Date: 2026-09-07
Status: **CANONICAL COURSE-DESIGN STANDARD**
Applies to: **AIIS_L0–AIIS_L16 and future AIIS lessons**
Primary language: **繁體中文**

---

# 0. 本文件的目的

本文件定義 AIIS 課程的標準設計流程。

未來只要開始新的 AIIS Lesson，應先讀：

1. Root `README.md` — Master Curriculum Contract
2. 本文件 `AIIS-COURSE-DESIGN-STANDARD.md`
3. 該 Lesson 的 canonical `LessonX/README.md`
4. 相鄰 Lesson 的 Handoff / Boundary
5. 最新 `_myplan_` lesson planning files

然後才開始新增或修改課程內容。

目標不是讓每一課長得完全一樣，而是確保：

- 課程主線不漂移。
- 每課只有一個主要 Mission。
- 不因新工具而無限擴張。
- 每頁教學目的清楚。
- 學生看到的 Slide 簡潔。
- 老師擁有足夠詳細的講稿。
- Lab 有 Evidence。
- Lesson 之間有清楚 Handoff。
- 所有重要規劃同步保存到 GitHub。

---

# 1. 最高層約束：Master Curriculum First

AIIS 的 16-Lesson Master Curriculum 是最高層課程契約。

任何單課優化都必須服從 Master Curriculum，而不能反過來擠掉其他正式 Lesson。

正式主線：

```text
ORIENTATION
→ BUILD
→ MANAGE
→ UNDERSTAND
→ SECURE
→ LEARN (ML / DL)
→ ATTACK
→ DEFEND
→ GOVERN
→ DEMO
```

核心定位：

> **AI for Security / AI-assisted Security Engineering**

不是把課程無限擴張成所有 AI 與 Security 主題。

### Scope Control Rules

1. One Lesson = One Primary Mission。
2. 每課優先只實作一種代表性 Tool / Workflow。
3. 其他工具放入 `Further Exploration`，不能自動成為必修支線。
4. 新工具不能改變固定 Lesson allocation。
5. 優先沿用同一個 Weather Security Center / Persistent Lab。
6. 不為了介紹工具而建立不必要的新 Demo App。
7. Formal Curriculum 不包含 Reinforcement Learning (RL)。
8. Offensive Security 僅限授權、隔離、安全 Lab。

---

# 2. 課程設計總流程

每一個新 Lesson 都按照以下順序設計：

```text
MASTER CURRICULUM
       ↓
LESSON MISSION
       ↓
BOUNDARY
       ↓
PREREQUISITE / PREVIEW–TEACH–REUSE
       ↓
LESSON STORYLINE
       ↓
SLIDE PURPOSE MAP
       ↓
SLIDE 00
       ↓
L1-STYLE SLIDE-BY-SLIDE TEACHING SCRIPT
       ↓
LAB / ACTIVITY
       ↓
EVIDENCE
       ↓
HANDOFF TO NEXT LESSON
       ↓
GITHUB SYNC
       ↓
FINAL AUDIT
       ↓
FREEZE
```

這是 AIIS Lesson Design 的標準 Pipeline。

---

# 3. STEP 1 — 定義 Lesson Mission

開始一課前，先用一句話回答：

> **這一課學生完成後，最重要的新能力是什麼？**

Mission 必須足夠窄，不能一次承擔多個正式 Lesson。

例如：

```text
L1 BUILD
Build a working Weather Security Center with AI.

L2 MANAGE
Manage one AI-generated change with Spec, Review, Evidence and Git history.

L3 UNDERSTAND
Understand how the same Weather Security Center actually works.

L4 SECURE
Scan, evaluate, fix and re-verify source-code security findings.
```

如果一句 Mission 裡出現太多 `AND`，先檢查是否 Scope 過大。

---

# 4. STEP 2 — 明確定義 Boundary

每課必須寫：

```text
THIS LESSON OWNS
THIS LESSON DOES NOT OWN
```

例如 L2：

```text
OWNS
OpenSpec
AI implementation planning
Human review
Diff
Acceptance Criteria verification
Git / GitHub engineering memory

DOES NOT OWN
Python internals → L3
Semgrep remediation → L4
ML → L5–L7
DL → L9–L10
Red Team → L11–L12
Blue Team → L13
Governance → L14
```

Boundary 的目的不是限制創意，而是防止一課把後面五課都教完。

---

# 5. STEP 3 — PREVIEW → TEACH → REUSE

跨 Lesson 的重要概念採：

```text
PREVIEW
   ↓
TEACH
   ↓
REUSE
```

### PREVIEW
只建立認知，不深入教。

### TEACH
在正式擁有該概念的 Lesson 完整教授。

### REUSE
後續直接使用，不重教完整內容。

例如 OpenSpec：

```text
L0 / L1 → PREVIEW
L2      → TEACH
L3–L16  → REUSE when useful
```

如果設計後面 Lesson 時發現學生需要前置知識，應主動檢查：

1. 是否需要在前一課 Preview？
2. 哪一課正式 Teach？
3. 後續如何 Reuse？

不要直接新增一個新的必修 Lesson。

---

# 6. STEP 4 — 建立 Lesson Storyline

在寫逐頁內容之前，先建立整課 Narrative Arc。

每個 Part 都回答一個大問題。

例如 L2：

```text
A. WHY MANAGE?
B. DEFINE
C. BUILD
D. VERIFY
E. REMEMBER
F. COMPLETE LAB + HANDOFF
```

Storyline 應該像一條因果鏈，而不是 Topic List。

好的 Storyline：

```text
Problem
→ Need
→ Concept
→ Method
→ Practice
→ Evidence
→ Reflection / Handoff
```

避免：

```text
Tool A
Tool B
Tool C
Tool D
```

---

# 7. STEP 5 — Slide Purpose Map

正式寫 Slide 前，先建立每頁「這頁在做什麼」。

例如：

```text
S01 能跑，不代表可管理
S02 小 Request 也可能造成大 Change Surface
S03 Vibe Coding 很快，但持續工程需要控制
S04 Prompt 不等於 Spec
S05 用 OpenSpec 保存 Change 定義
S06 建立完整 Engineering Map
```

Purpose Map 用來檢查：

- 是否有重複頁？
- 是否跳太快？
- 是否一頁承擔太多認知任務？
- 是否缺少必要 Transition？
- 是否侵入下一課？

---

# 8. STEP 6 — Slide 00 規則

每一個正式 AIIS Lesson 都有：

```text
Slide 00
```

Slide 00 是封面 + Course Positioning，不消耗 S01、S02…正式內容頁碼。

Slide 00 必須回答：

1. 上一課在哪裡？
2. 今天是哪個 Mission？
3. 今天沿用哪個 Persistent Project / Context？
4. 今天主要解決什麼問題？
5. 下一課大致往哪裡走？

Slide 00 不應提前把整課內容全部教完。

---

# 9. STEP 7 — L1 式逐頁詳細教學稿

這是 AIIS 正式的逐頁教學稿標準。

每一張 Slide 使用以下結構：

```text
# Slide XX — 標題

## 目的

## 投影片內容

## 視覺

## 煥哥

## 老師講稿

## 問

## 預期答案

## 老師補充 / 板書（需要時）

## 核心句

## Transition
```

不需要為了格式而硬塞每一欄；如果某頁不需要 Activity / 板書，可以省略。

但是以下核心項目原則上都要存在：

- 目的
- 投影片內容
- 視覺
- 老師講稿
- 核心句
- Transition

---

# 10. 投影片最重要的品質規則

> **高品質 ≠ 高密度。**
>
> **詳細的是教學設計；簡潔的是學生看到的畫面。**

每一頁遵守：

> **ONE SLIDE = ONE MAIN QUESTION + ONE MAIN VISUAL + ONE MEMORY LINE**

### ON SLIDE 建議

通常只需要：

- 1 個 Title
- 1 個 Main Visual / Contrast
- 3–5 個短重點
- 1 個 Memory Line

不要把 Teacher Script 全放到 Slide。

---

# 11. 視覺設計規則

視覺不是裝飾，而是認知工具。

優先使用：

```text
Contrast
Flow
Before / After
Layer
Checklist
Timeline
Pipeline
Architecture
Decision Gate
Evidence Card
```

每頁盡量只有一個 Main Visual。

如果同一頁需要三張複雜 Diagram，通常代表應拆頁。

---

# 12. 「煥哥」角色規則

煥哥不是每頁固定貼圖，而是教學 Narrative Guide。

每頁可定義：

```text
表情
動作
視線
角色
```

角色可隨 Story 改變，例如：

```text
BUILDER
PROJECT LEAD
REQUIREMENT INVESTIGATOR
PLAN REVIEWER
ENGINEERING REVIEWER
TESTER
EVIDENCE REVIEWER
SYSTEM EXPLORER
```

Avatar 的動作應服務該頁 Concept。

避免每頁都使用相同表情與姿勢。

---

# 13. 老師講稿規則

Teacher Script 要比 Slide 詳細。

應包含：

- 這頁如何開場。
- 為什麼重要。
- 具體例子。
- 學生可能誤解什麼。
- 怎麼問學生。
- 怎麼整理答案。
- 如何接下一頁。

老師講稿不是把 Slide 文字重新念一次。

---

# 14. Question / Expected Answer

適合互動的頁面加入：

```text
問
預期答案
老師補充
```

問題優先使用 Concept Check，而不是死背。

例如：

```text
AI 說 Done，算 Evidence 嗎？
```

比：

```text
請背出 Verification 的定義。
```

更符合 AIIS。

---

# 15. Transition 規則

每頁最好有自然 Transition。

Transition 應回答：

> **為什麼下一頁現在必須出現？**

例如：

```text
AI 說 Done。
→ 但 Claim 不是 Evidence。
→ 所以下一頁先看 Changed Files。
```

好的 Lesson 是一個 Story，不是 30 張獨立海報。

---

# 16. Persistent Project Rule

AIIS 優先沿用同一個 Persistent Project：

> **AI Weather Security Center**

目標是讓學生看到同一個系統如何逐步經歷：

```text
BUILD
→ MANAGE
→ UNDERSTAND
→ SECURE
→ ATTACK
→ DEFEND
→ GOVERN
→ DEMO
```

如果可以在既有 Project 完成教學，就不要為每課建立新的 Toy Project。

---

# 17. Lab 設計規則

Lab 不是只要求「做出結果」。

每個重要 Lab 應回答：

```text
MISSION
INPUT
STEPS
EXPECTED OUTPUT
TEST / VERIFY
EVIDENCE
REFLECTION
```

AI-assisted Lab 應保留 Human Control：

```text
AI proposes
→ Human reviews
→ Tool / Runtime verifies
→ Human decides
```

---

# 18. Evidence Culture

AIIS 不把 AI 的文字宣稱當作完成證據。

核心原則：

> **AI CLAIM ≠ VERIFIED EVIDENCE**

依 Lesson 不同，可保存：

```text
Prompt / Request
Spec
Plan
Human Review
Code / Diff
Run Result
Test Result
Scanner Result
Acceptance Criteria
Security Finding
Fix
Re-scan
Regression Test
Git Commit
GitHub History
Report
```

核心句：

> **NO EVIDENCE, NO TRUST.**

---

# 19. AI-assisted Engineering Workflow

課程中的 AI 使用不採「一句 Prompt → 接受答案」模式。

基本 Workflow：

```text
PROMPT / REQUEST
      ↓
PLAN
      ↓
HUMAN REVIEW
      ↓
CODE / ACTION
      ↓
RUN / TEST
      ↓
REVIEW
      ↓
FIX
      ↓
EVIDENCE
```

在 Spec-driven Lesson 中：

```text
DEFINE
→ BUILD
→ VERIFY
→ REMEMBER
```

核心句：

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

---

# 20. Security Lesson 的額外規則

Security Finding 必須區分：

```text
AI FINDING ≠ CONFIRMED FINDING
SCANNER FINDING ≠ CONFIRMED VULNERABILITY
BUG ≠ VULNERABILITY ≠ RISK
```

Finding 可標示：

```text
CONFIRMED
LIKELY TRUE POSITIVE
LIKELY FALSE POSITIVE
NEEDS VERIFICATION
```

Remediation Decision：

```text
FIX NOW
VERIFY FIRST
ACCEPT RISK
FALSE POSITIVE / NO CHANGE
```

Secure SDLC 主線：

```text
BUILD
→ SCAN
→ FIND
→ PROPOSE
→ REVIEW
→ FIX
→ TEST
→ RE-SCAN
→ VERIFY
→ REPORT
```

---

# 21. Offensive Security Safety Boundary

任何 Red Team / Offensive Security 實作只能使用：

- localhost
- student-owned code
- teacher-provided target
- VM / Docker isolated lab
- TryHackMe
- CTF
- deliberately vulnerable lab
- explicitly authorized range

核心規則：

> **Publicly accessible ≠ authorized.**

課程避免要求學生對未授權 Public Website 執行攻擊或掃描。

---

# 22. Antigravity Prompt / YAML

適合實作的 Lesson 應提供可重複使用的 Antigravity Prompt 或 YAML。

Prompt 應包含：

```text
ROLE
CONTEXT
MISSION
SCOPE
OUT OF SCOPE
CONSTRAINTS
STEPS
HUMAN REVIEW GATES
ACCEPTANCE CRITERIA
EVIDENCE
```

不要只寫：

```text
Build this for me.
```

---

# 23. Lesson Handoff

每一課最後必須明確回答：

```text
WHAT WE NOW KNOW
WHAT WE STILL DO NOT KNOW
WHY NEXT LESSON IS NECESSARY
```

例如 L2 → L3：

```text
We know WHY the change exists.
We know WHAT changed.
We know WHETHER it met AC.
We know WHERE history is recorded.

But:
HOW does the code actually work?

→ L3 UNDERSTAND
```

Handoff 是下一課 Story 的起點。

---

# 24. GitHub Sync Rule

課程設計不是只存在 Chat History。

每一個 Meaningful Design Batch 應同步到 GitHub。

推薦批次：

```text
Slide 00
S01–S06
S07–S12
S13–S18
S19–S24
S25–S30
```

實際頁數依內容可調整，通常一次約 5–6 頁，必要時最多約 10 頁。

每批完成後：

1. 更新對應 Teaching Script。
2. 保持繁體中文。
3. 檢查 Lesson Boundary。
4. 檢查前後 Slide Transition。
5. 寫入 GitHub。
6. 回報進度。

不要等使用者再次提醒「寫入 GitHub」。

---

# 25. Final Audit

一課全部設計完成後，至少做以下 Audit：

### Curriculum
- [ ] Mission 是否符合 Master Curriculum？
- [ ] 是否侵入其他 Lesson？
- [ ] 是否新增不必要必修支線？

### Story
- [ ] Slide 00 是否完成定位？
- [ ] Storyline 是否有清楚因果？
- [ ] 每頁 Purpose 是否不同？
- [ ] Transition 是否自然？

### Slide Quality
- [ ] One Main Question？
- [ ] One Main Visual？
- [ ] One Memory Line？
- [ ] Student-facing Slide 是否過度擁擠？
- [ ] Teacher Script 是否足夠詳細？

### Practice
- [ ] 是否有代表性 Lab / Example？
- [ ] 是否有 Human Review？
- [ ] 是否有 Test / Verification？
- [ ] 是否有 Evidence？

### Continuity
- [ ] 是否沿用 Persistent Project？
- [ ] 是否遵守 PREVIEW → TEACH → REUSE？
- [ ] 是否有清楚 Next Lesson Handoff？

### Repository
- [ ] Canonical Lesson README 是否一致？
- [ ] `_myplan_` 是否同步？
- [ ] 是否避免互相矛盾的 Canonical 文件？

---

# 26. Freeze Rule

完成 Final Audit 後，Lesson 可標示：

```text
CANONICAL FINAL / PPT-READY
```

Freeze 後，除非 Master Curriculum 改變，後續修改應主要限於：

- factual correction
- Traditional Chinese wording refinement
- visual-production refinement
- teacher-feedback improvement
- lab bug fix
- safety correction

不要因為看到新工具，就重新打開已完成 Lesson 並新增 Mandatory Branch。

---

# 27. AIIS 標準 Lesson Artifact Set

建議每課至少保留：

```text
LessonX/README.md

_myplan_/
  AIIS-LX-COMPLETE.md
  AIIS-LX-Detailed-Lecture-Plan.md
  AIIS-LX-slide-00-teaching-script.md
  AIIS-LX-Teaching-Script-S01-S06.md
  AIIS-LX-Teaching-Script-S07-S12.md
  ...
```

頁數依 Lesson 調整，不要求硬切 30 頁。

`COMPLETE.md` 應保存：

- Lesson Mission
- Boundary
- Storyline
- Slide Purpose Map
- Timing
- Lab
- Evidence
- Handoff
- Freeze Status

---

# 28. 新 Lesson 啟動 SOP

未來使用者只要說：

> **開始 AIIS_L3**

或：

> **開始下一課**

應自動執行：

```text
1. Read Master Curriculum
2. Read AIIS Course Design Standard
3. Read LessonX README
4. Read previous / next lesson boundaries
5. Confirm Mission internally
6. Build / audit Lesson Storyline
7. Build Slide Purpose Map
8. Create Slide 00
9. Write L1-style detailed scripts in batches
10. Sync each meaningful batch to GitHub
11. Build Lab + Evidence
12. Complete Handoff
13. Run Final Audit
14. Mark CANONICAL FINAL / PPT-READY
```

使用者不需要反覆提醒：

- 「要像 L1」
- 「要有老師講稿」
- 「要寫視覺」
- 「要有煥哥」
- 「要有 Transition」
- 「記得寫 GitHub」
- 「不要一直發散」

這些已經是本 Standard 的預設行為。

---

# 29. AIIS 課程設計核心口訣

## 課程層級

> **MASTER FIRST. LESSON SECOND. TOOL THIRD.**
>
> **先守住總課程，再設計單課，最後才選工具。**

## 投影片層級

> **ONE SLIDE = ONE MAIN QUESTION + ONE MAIN VISUAL + ONE MEMORY LINE**

## 教學設計層級

> **詳細的是教學設計；簡潔的是學生看到的畫面。**

## AI Engineering 層級

> **AI BUILDS. HUMAN VERIFIES.**

## Spec-driven Engineering 層級

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

## Security 層級

> **AI proposes. Human understands. Security validates.**

## Evidence 層級

> **NO EVIDENCE, NO TRUST.**

---

# 30. 最終原則

AIIS 不以「介紹最多 AI 工具」為目標。

AIIS 要建立的是一條學生能真正反覆使用的能力鏈：

```text
看懂問題
→ 定義需求
→ 使用 AI 建構
→ 人類審查
→ 實際驗證
→ 保存證據
→ 理解系統
→ 找出安全問題
→ 修補與再驗證
→ 管理風險
→ 展示完整工程故事
```

因此，未來每一個 Lesson 的設計都應回到同一個問題：

> **這一頁、這個 Lab、這個 Tool，是否真的讓學生更接近 AI-assisted Security Engineering 的完整能力？**

如果答案不是明確的「是」，就應該刪除、延後，或移到 `Further Exploration`。
