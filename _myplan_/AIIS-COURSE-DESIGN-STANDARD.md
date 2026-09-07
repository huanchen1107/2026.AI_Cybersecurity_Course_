# AIIS COURSE DESIGN STANDARD
## 2026 AI × Information Security — Canonical Lesson Design Method

Version: 1.1
Date: 2026-09-07
Status: **CANONICAL COURSE-DESIGN STANDARD**
Applies to: **AIIS_L0–AIIS_L16，以及未來所有依 AIIS 方法設計的新課程**
Primary language: **繁體中文**

---

# 0. 本文件的目的與來源

本文件定義 AIIS 的統一課程設計方法。

**重要：本 Standard 不是只規範 L3–L16。AIIS_L0、L1、L2、L3……L16 全部都屬於同一套設計標準。**

目前 L0–L2 是這套 Standard 的實際來源：

```text
L0 提供：整課故事線 / 世界觀 / Narrative Arc
        ↓
L1 提供：最清楚的逐頁教學設計格式
        ↓
L2 提供：把 L1 格式系統化並驗證可重複使用
        ↓
AIIS COURSE DESIGN STANDARD
        ↓
L0–L16 全部統一使用
```

因此，不應理解成「L0–L2 是舊格式，L3 才開始新標準」。

正確理解是：

> **我們從目前 L0 的故事線、L1 的逐頁教學品質，以及 L2 的系統化重構中，萃取出一套 AIIS_L0–L16 都適用的 Canonical Standard。**

如果回頭整理 L0、L1、L2，也應逐步對齊本 Standard；但對齊的目的不是破壞已經好的內容，而是統一文件結構、命名、Storyline、Slide Purpose Map、逐頁教學稿與 Audit 方法。

---

# 1. 新 Lesson / 新課程開始前必讀

未來只要開始或重構任何 AIIS Lesson（包含 L0），應先讀：

1. Root `README.md` — Master Curriculum Contract
2. 本文件 `AIIS-COURSE-DESIGN-STANDARD.md`
3. 該 Lesson 的 canonical `LessonX/README.md` 或 Introduction canonical file
4. 相鄰 Lesson 的 Handoff / Boundary
5. 最新 `_myplan_` lesson planning files
6. 如果是新的 AIIS 系列課程，先參考目前 L0 的 Storyline 建立該課程的 Narrative Arc

然後才開始新增或修改課程內容。

目標不是讓每一課長得完全一樣，而是確保：

- 整個 Course 有一條清楚 Storyline。
- 每課在 Storyline 中有明確位置。
- 每課只有一個 Primary Mission。
- 不因新工具而無限擴張。
- 每頁教學目的清楚。
- 學生看到的 Slide 簡潔。
- 老師擁有足夠詳細的講稿。
- Lab 有 Evidence。
- Lesson 之間有清楚 Handoff。
- 所有重要規劃同步保存到 GitHub。

---

# 2. L0 的特殊角色：先建立整門課的 Story

AIIS_L0 不是一般內容課，也不是可以略過的「第零課」。

L0 的主要設計責任是：

> **先讓學生看懂「我們為什麼要走完整個 AIIS Journey」。**

目前 L0 已建立的重要 Narrative：

```text
HUMAN TECHNOLOGY
Machine → Energy → Information → Intelligence
                         ↓
                   AI REVOLUTION
                         ↓
                 ANI → AGI → ASI
                         ↓
          Discriminate → Generate → Act
                                    ↓
                            AI CAN ACT
                                    ↓
                         SECURITY MATTERS
                                    ↓
             Asset → Threat → Vulnerability → Risk
                                    ↓
                              CIA TRIAD
                                    ↓
                    AI WEATHER SECURITY CENTER
                                    ↓
              AIIS LEARNING JOURNEY
                                    ↓
                        FIRST AI-ASSISTED LAB
                                    ↓
                   Rule ≠ Intelligence ≠ Truth
                                    ↓
                          NEXT: AIIS_L1
```

未來如果建立另一套新課程，不應直接複製 L0 的 AI Revolution 內容，而應複製它的**設計方法**：

```text
WHY THIS COURSE?
      ↓
BIG WORLD / HISTORICAL CONTEXT
      ↓
WHAT HAS CHANGED?
      ↓
WHY DOES IT MATTER TO STUDENTS?
      ↓
CORE PROBLEM / DISCIPLINE
      ↓
COURSE PROJECT / LEARNING VEHICLE
      ↓
SEMESTER JOURNEY
      ↓
FIRST EXPERIENCE
      ↓
HANDOFF TO LESSON 1
```

這稱為：

> **COURSE STORY FIRST. LESSONS SECOND. SLIDES THIRD.**

因此新的 Course Design 應先設計自己的「L0 型 Storyline」，再拆成 Lessons，而不是先列工具清單。

---

# 3. 最高層約束：Master Curriculum First

AIIS 的 L0–L16 Master Curriculum 是最高層課程契約。

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

# 4. 統一課程設計總流程

任何 AIIS Lesson，包括 L0，都按照以下設計精神：

```text
COURSE STORY / MASTER CURRICULUM
       ↓
LESSON POSITION
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

### L0 的流程差異

L0 在 `LESSON POSITION` 之前多一個責任：

```text
DEFINE THE COURSE STORY
```

因為 L0 本身就是整門課的入口與世界觀。

---

# 5. STEP 1 — 定義 Lesson Mission

開始一課前，先用一句話回答：

> **這一課學生完成後，最重要的新能力是什麼？**

Mission 必須足夠窄，不能一次承擔多個正式 Lesson。

例如：

```text
L0 ORIENTATION
Understand why AI capability makes information-security discipline necessary and see the semester journey.

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

# 6. STEP 2 — 明確定義 Boundary

每課必須寫：

```text
THIS LESSON OWNS
THIS LESSON DOES NOT OWN
```

Boundary 的目的不是限制創意，而是防止一課把後面五課都教完。

L0 也要有 Boundary：L0 建立世界觀與課程 Journey，但不提前完整教授 L1–L16 的正式技能。

---

# 7. STEP 3 — PREVIEW → TEACH → REUSE

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

L0 特別適合 Preview 整學期的重要 Vocabulary 與 Journey，但不能因此把後續 Lesson 提前教完。

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

# 8. STEP 4 — 建立 Lesson Storyline

在寫逐頁內容之前，先建立整課 Narrative Arc。

每個 Part 都回答一個大問題。

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

L0 可使用更大的 Story Arc：

```text
WORLD
→ CHANGE
→ CONSEQUENCE
→ PROBLEM
→ DISCIPLINE
→ COURSE JOURNEY
→ FIRST EXPERIENCE
→ L1
```

避免：

```text
Tool A
Tool B
Tool C
Tool D
```

---

# 9. STEP 5 — Slide Purpose Map

正式寫 Slide 前，先建立每頁「這頁在做什麼」。

Purpose Map 用來檢查：

- 是否有重複頁？
- 是否跳太快？
- 是否一頁承擔太多認知任務？
- 是否缺少必要 Transition？
- 是否侵入下一課？

L0 同樣必須建立 Purpose Map，確保 30+ 頁不是資訊堆疊，而是一條 Story。

---

# 10. STEP 6 — Slide 00 規則

每一個正式 AIIS Lesson，**包含 L0**，都有：

```text
Slide 00
```

Slide 00 是封面 + Course Positioning，不消耗 S01、S02…正式內容頁碼。

一般 Lesson 的 Slide 00 回答：

1. 上一課在哪裡？
2. 今天是哪個 Mission？
3. 今天沿用哪個 Persistent Project / Context？
4. 今天主要解決什麼問題？
5. 下一課大致往哪裡走？

L0 沒有上一課，因此改回答：

1. 這門課是什麼？
2. 為什麼現在需要這門課？
3. AI 與 Information Security 的關係是什麼？
4. 整學期會走哪條 Journey？
5. 今天 L0 要建立什麼世界觀？

Slide 00 不應提前把整課內容全部教完。

---

# 11. STEP 7 — L1 式逐頁詳細教學稿

這是 **AIIS_L0–L16 全部正式採用** 的逐頁教學稿標準。

名稱雖稱「L1 式」，只是因為這個格式在 L1 最先被清楚定型；它不是只屬於 L1。

未來可把它理解成：

> **AIIS Standard Slide-by-Slide Teaching Format**

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

不需要為了格式而硬塞每一欄；如果某頁不需要問答 / 板書，可以省略。

但是以下核心項目原則上都要存在：

- 目的
- 投影片內容
- 視覺
- 老師講稿
- 核心句
- Transition

---

# 12. 投影片最重要的品質規則

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

# 13. 視覺設計規則

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

# 14. 「煥哥」角色規則

煥哥不是每頁固定貼圖，而是教學 Narrative Guide。

每頁可定義：

```text
表情
動作
視線
角色
```

Avatar 的動作應服務該頁 Concept。

避免每頁都使用相同表情與姿勢。

---

# 15. 老師講稿規則

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

# 16. Question / Expected Answer

適合互動的頁面加入：

```text
問
預期答案
老師補充
```

問題優先使用 Concept Check，而不是死背。

---

# 17. Transition 規則

每頁最好有自然 Transition。

Transition 應回答：

> **為什麼下一頁現在必須出現？**

好的 Lesson 是一個 Story，不是 30 張獨立海報。

---

# 18. Persistent Project Rule

AIIS 優先沿用同一個 Persistent Project：

> **AI Weather Security Center**

目標是讓學生看到同一個系統如何逐步經歷：

```text
ORIENT
→ BUILD
→ MANAGE
→ UNDERSTAND
→ SECURE
→ LEARN
→ ATTACK
→ DEFEND
→ GOVERN
→ DEMO
```

如果可以在既有 Project 完成教學，就不要為每課建立新的 Toy Project。

---

# 19. Lab 設計規則

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

# 20. Evidence Culture

AIIS 不把 AI 的文字宣稱當作完成證據。

核心原則：

> **AI CLAIM ≠ VERIFIED EVIDENCE**

核心句：

> **NO EVIDENCE, NO TRUST.**

---

# 21. AI-assisted Engineering Workflow

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

# 22. Security Lesson 的額外規則

Security Finding 必須區分：

```text
AI FINDING ≠ CONFIRMED FINDING
SCANNER FINDING ≠ CONFIRMED VULNERABILITY
BUG ≠ VULNERABILITY ≠ RISK
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

# 23. Offensive Security Safety Boundary

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

---

# 24. Antigravity Prompt / YAML

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

---

# 25. Lesson Handoff

每一課最後必須明確回答：

```text
WHAT WE NOW KNOW
WHAT WE STILL DO NOT KNOW
WHY NEXT LESSON IS NECESSARY
```

L0 的 Handoff 特別重要：它必須把「Course Worldview」交給 L1 的第一個實際 BUILD Mission。

---

# 26. GitHub Sync Rule

課程設計不是只存在 Chat History。

每一個 Meaningful Design Batch 應同步到 GitHub。

推薦批次通常一次約 5–6 頁，必要時最多約 10 頁。

每批完成後：

1. 更新對應 Teaching Script。
2. 保持繁體中文。
3. 檢查 Lesson Boundary。
4. 檢查前後 Slide Transition。
5. 寫入 GitHub。
6. 回報進度。

不要等使用者再次提醒「寫入 GitHub」。

---

# 27. Final Audit

一課全部設計完成後，至少做以下 Audit：

### Curriculum
- [ ] Mission 是否符合 Master Curriculum？
- [ ] 是否侵入其他 Lesson？
- [ ] 是否新增不必要必修支線？

### Course Story
- [ ] 本 Lesson 在 Course Story 中的位置是否清楚？
- [ ] 如果是 L0 / 新課程入口，是否先建立完整 Narrative Arc？

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

# 28. Freeze Rule

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

# 29. AIIS 標準 Lesson Artifact Set

每課建議保留：

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

L0 / Course Introduction 的 COMPLETE 文件另外要保存：

- Course Worldview
- Course Narrative Arc
- Semester Journey
- Why this course now?
- L0 → L1 Handoff

---

# 30. 新 Lesson / 新 Course 啟動 SOP

## A. AIIS 既有課程內開始任何 Lesson（L0–L16）

使用者只要說：

> **開始 AIIS_L3**

或：

> **重整 L0**

應自動執行：

```text
1. Read Master Curriculum
2. Read AIIS Course Design Standard
3. Read Lesson canonical files
4. Read previous / next lesson boundaries
5. Confirm Course Story position
6. Confirm Mission and Boundary
7. Build / audit Lesson Storyline
8. Build Slide Purpose Map
9. Create / audit Slide 00
10. Write AIIS Standard slide-by-slide scripts in batches
11. Sync each meaningful batch to GitHub
12. Build Lab + Evidence where appropriate
13. Complete Handoff
14. Run Final Audit
15. Mark CANONICAL FINAL / PPT-READY
```

## B. 建立全新的課程

不要直接從 Lesson 1 或工具清單開始。

先使用 L0 的設計方法：

```text
1. DEFINE COURSE PURPOSE
2. BUILD COURSE STORY / NARRATIVE ARC
3. DEFINE STUDENT JOURNEY
4. DEFINE PERSISTENT PROJECT / LEARNING VEHICLE
5. SPLIT STORY INTO LESSON MISSIONS
6. DEFINE BOUNDARIES
7. DESIGN COURSE-ENTRY / L0 EXPERIENCE
8. THEN DESIGN EACH LESSON
9. USE STANDARD SLIDE-BY-SLIDE FORMAT
10. AUDIT THE WHOLE COURSE
```

---

# 31. 使用者不需要再提醒的預設規則

未來不需要反覆提醒：

- 「L0–L16 都要同一標準」
- 「要先梳理故事線」
- 「要像 L1」
- 「要有老師講稿」
- 「要寫視覺」
- 「要有煥哥」
- 「要有 Transition」
- 「記得寫 GitHub」
- 「不要一直發散」

以上全部是本 Standard 的預設行為。

---

# 32. AIIS 課程設計核心口訣

## Course 層級

> **COURSE STORY FIRST. LESSONS SECOND. SLIDES THIRD.**
>
> **先建立整門課的故事，再拆 Lesson，最後才寫 Slide。**

## Curriculum 層級

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

## Evidence 層級

> **NO EVIDENCE, NO TRUST.**

---

# 33. 最終原則

AIIS 不以「介紹最多 AI 工具」為目標。

AIIS 要建立的是一條學生能真正反覆使用的能力鏈。

課程設計順序永遠是：

```text
COURSE STORY
→ LESSON JOURNEY
→ LESSON MISSION
→ SLIDE STORY
→ PRACTICE
→ EVIDENCE
→ HANDOFF
```

因此未來每一個 Course / Lesson / Slide 都應回到同一個問題：

> **它是否真的推進這門課的故事與學生能力？**

如果答案不是明確的「是」，就應刪除、延後，或移到 `Further Exploration`。
