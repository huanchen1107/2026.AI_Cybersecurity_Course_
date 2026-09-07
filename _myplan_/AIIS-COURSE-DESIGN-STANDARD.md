# AIIS COURSE DESIGN STANDARD
## 2026 AI × Information Security — Canonical Lesson Design Method

Version: 1.2
Date: 2026-09-07
Status: **CANONICAL COURSE-DESIGN STANDARD**
Applies to: **AIIS_L0–AIIS_L16，以及未來所有依 AIIS 方法設計的新課程**
Primary language: **繁體中文**

---

# 0. 本文件的目的與來源

本文件定義 AIIS 的統一課程設計方法。

**重要：本 Standard 不是只規範 L3–L16。AIIS_L0、L1、L2、L3……L16 全部都屬於同一套設計標準。**

目前 L0–L5 的實作共同萃取出這套 Standard：

```text
L0 提供：整課故事線 / 世界觀 / Narrative Arc
L1 提供：最清楚的逐頁教學設計格式
L2 提供：把 L1 格式系統化並驗證可重複使用
L1–L5 Visual Audit 提供：Content → Visual → Character Interaction 規則
        ↓
AIIS COURSE DESIGN STANDARD
        ↓
L0–L16 全部統一使用
```

> **COURSE STORY FIRST. LESSONS SECOND. SLIDES THIRD.**

---

# 1. 新 Lesson / 新課程開始前必讀

開始或重構任何 AIIS Lesson 前，先讀：
1. Root `README.md` — Master Curriculum Contract
2. 本文件
3. 該 Lesson canonical README
4. 相鄰 Lesson Handoff / Boundary
5. 最新 `_myplan_` lesson planning files
6. 相關 Content-Driven Visual Audit（若已存在）

目標：Course Story 清楚、One Primary Mission、Scope 不發散、每頁目的清楚、Student Slide 簡潔、Teacher Script 詳細、Lab 有 Evidence、Lesson 有 Handoff、GitHub 是 Source of Truth。

---

# 2. L0 的特殊角色：COURSE STORY FIRST

L0 主要責任是讓學生先看懂「為什麼要走完整個 AIIS Journey」。新課程應複製 L0 的設計方法而非內容：

```text
WHY THIS COURSE?
→ BIG WORLD / CONTEXT
→ WHAT HAS CHANGED?
→ WHY IT MATTERS
→ CORE PROBLEM
→ PERSISTENT PROJECT
→ SEMESTER JOURNEY
→ FIRST EXPERIENCE
→ HANDOFF TO L1
```

---

# 3. Master Curriculum First

正式主線：

```text
ORIENTATION → BUILD → MANAGE → UNDERSTAND → SECURE
→ LEARN (ML / DL) → ATTACK → DEFEND → GOVERN → DEMO
```

核心定位：**AI for Security / AI-assisted Security Engineering**。

Scope Rules:
1. One Lesson = One Primary Mission.
2. 每課優先只實作一種代表性 Tool / Workflow.
3. 其他工具放 `Further Exploration`.
4. 新工具不能改變固定 Lesson allocation.
5. 優先沿用 Weather Security Center.
6. 不為工具建立不必要 Toy App.
7. Formal Curriculum 不包含 RL.
8. Offensive Security 僅限授權、隔離、安全 Lab.

---

# 4. 統一課程設計流程

```text
COURSE STORY / MASTER CURRICULUM
→ LESSON POSITION
→ LESSON MISSION
→ BOUNDARY
→ PREVIEW–TEACH–REUSE
→ LESSON STORYLINE
→ SLIDE PURPOSE MAP
→ SLIDE 00
→ L1-STYLE SLIDE-BY-SLIDE TEACHING SCRIPT
→ CONTENT-DRIVEN VISUAL DESIGN
→ LAB / ACTIVITY
→ EVIDENCE
→ HANDOFF
→ GITHUB SYNC
→ FINAL CONTENT + VISUAL AUDIT
→ FREEZE
```

---

# 5. Lesson Mission

一句話回答：**這一課學生完成後，最重要的新能力是什麼？**
Mission 足夠窄；若有太多 AND，檢查 Scope。

Examples:
- L0 ORIENTATION — understand why AI capability makes information-security discipline necessary.
- L1 BUILD — build a working Weather Security Center with AI.
- L2 MANAGE — manage one AI-generated change with Spec, Review, Evidence and Git history.
- L3 UNDERSTAND — understand how the same Weather Security Center works.
- L4 SECURE — scan, evaluate, fix and re-verify source-code security findings.
- L5 LEARN — use CRISP-DM to frame and build a first security-classification workflow.

---

# 6. Boundary

每課必須寫：
```text
THIS LESSON OWNS
THIS LESSON DOES NOT OWN
```
防止一課把後面五課教完。

---

# 7. PREVIEW → TEACH → REUSE

跨 Lesson 概念採：
```text
PREVIEW → TEACH → REUSE
```
需要前置知識時，先決定在哪一課 Preview、哪一課正式 Teach、後續如何 Reuse；不要直接新增必修 Lesson。

---

# 8. Lesson Storyline

逐頁之前先建立因果 Narrative：
```text
Problem → Need → Concept → Method → Practice → Evidence → Handoff
```
不是 Tool A → Tool B → Tool C。

---

# 9. Slide Purpose Map

正式寫 Slide 前先寫每頁 Purpose，用來檢查重複、跳躍、認知負荷、Transition、Boundary。

---

# 10. Slide 00

每個正式 Lesson（含 L0）都有 Slide 00，作封面 + Course Positioning，不消耗 S01。
一般 Lesson 回答：上一課在哪、今天 Mission、Persistent Project、今日問題、下一步。
L0 改回答 Course Purpose / Why Now / AI × Security / Semester Journey / Worldview。

---

# 11. AIIS Standard Slide-by-Slide Teaching Format

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

核心必備：目的、投影片內容、視覺、老師講稿、核心句、Transition。

---

# 12. Slide Quality

> **高品質 ≠ 高密度。**
> **詳細的是教學設計；簡潔的是學生看到的畫面。**
> **ONE SLIDE = ONE MAIN QUESTION + ONE MAIN VISUAL + ONE MEMORY LINE**

Student-facing 通常：1 Title、1 Main Visual/Contrast、3–5 短重點、1 Memory Line。

---

# 13. Content-Driven Visual Design — 強制規則（v1.2 新增）

視覺不是完成文字後再貼裝飾圖，而必須從該頁 Concept 推導：

```text
SLIDE PURPOSE / CONCEPT
      ↓
WHAT MUST STUDENT SEE?
      ↓
VISUAL METAPHOR / SYSTEM OBJECT
      ↓
HUANGE ROLE
      ↓
EXPRESSION
      ↓
ACTION
      ↓
PROP
      ↓
DIRECT CONTENT INTERACTION
      ↓
PLACEMENT / SCALE
```

每頁在 PPT production 前都必須能回答：
1. 這頁真正教什麼？
2. 最重要的視覺隱喻或物件是什麼？
3. 煥哥在這頁扮演什麼教學角色？
4. 他的表情為何符合概念？
5. 他正在做什麼，而不是只站著？
6. 他拿什麼與核心內容互動？
7. 他的眼神/手勢實際指向哪個內容？
8. 學生不讀完整文字時，是否仍可由圖猜到這頁概念？

優先 Main Visual：Contrast / Flow / Before-After / Layer / Checklist / Timeline / Pipeline / Architecture / Decision Gate / Evidence Card。

---

# 14. 「煥哥」Content-Reactive Character Standard

煥哥是 **Narrative Guide + Teaching Actor**，不是品牌貼圖。

每頁 `## 煥哥` 原則上要定義：
```text
Role / Costume
Expression
Pose / Action
Prop
Content Interaction
Speech / Memory Line（適合時）
Placement / Scale
```

角色臉部與核心身份全課一致；可依任務使用輕量角色配件，例如 Builder / Reviewer / Security Engineer / Data Detective / ML Engineer / Analyst。

### 強制要求
- 人物要指、拿、檢查、比較、操作、阻擋、交付或追蹤該頁核心教學物件。
- 表情由概念決定，不是每頁微笑。
- 相鄰頁原則上避免相同 Pose，除非是刻意 Visual Callback。
- 一般人物約占 15–30%，不得遮住 Main Visual。
- Speech Bubble 不能取代 Action。

### 明確禁止
- 每頁同一張站立人物，只換一句話。
- 只有「煥哥：一句話」，沒有 Role/Action/Interaction。
- Generic thumbs-up / generic pointing 與內容無關。
- 人物只是裝飾。
- 資安頁一律套 hooded hacker / terminal。
- AI/ML 頁一律套 generic glowing brain。

如果移除人物後完全不影響該頁的視覺教學邏輯，應重新檢查人物是否只是裝飾。

---

# 15. Cross-Slide Visual Callback

好的 Lesson 不是 30 張獨立海報。重要概念應刻意重用同一視覺物件，讓學生看到狀態變化。

Examples from canonical audits:
- L2 S12 empty Acceptance Checklist → S22 same checklist with Evidence.
- L2 S16 Human Plan Gate → S23 Human Evidence Gate.
- L3 simplified Request Journey → later complete end-to-end Journey.
- L4 first Scan → same Scanner Re-scan after Fix.
- L5 sealed TEST set → remains sealed during `.fit()`.
- L5 UNTRAINED → TRAINED → PREDICTION.

Callback 必須有教學理由；不是為了重複版型。

---

# 16. Teacher Script / Question / Transition

Teacher Script 要比 Slide 詳細，包含開場、重要性、例子、常見誤解、Concept Check、整理、下一頁銜接。
Transition 回答：**為什麼下一頁現在必須出現？**

---

# 17. Persistent Project Rule

優先沿用 **AI Weather Security Center**：
```text
ORIENT → BUILD → MANAGE → UNDERSTAND → SECURE → LEARN → ATTACK → DEFEND → GOVERN → DEMO
```
能在既有 Project 教，就不要建立 Toy Project。

---

# 18. Lab / Evidence

重要 Lab：
```text
MISSION / INPUT / STEPS / EXPECTED OUTPUT / TEST-VERIFY / EVIDENCE / REFLECTION
```
AI-assisted：
```text
AI proposes → Human reviews → Tool/Runtime verifies → Human decides
```

> **AI CLAIM ≠ VERIFIED EVIDENCE**
> **NO EVIDENCE, NO TRUST.**

---

# 19. AI-assisted Engineering Workflow

```text
PROMPT / REQUEST → PLAN → HUMAN REVIEW → CODE/ACTION → RUN/TEST → REVIEW → FIX → EVIDENCE
```
Spec-driven：
```text
DEFINE → BUILD → VERIFY → REMEMBER
```
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

---

# 20. Security Rules

```text
AI FINDING ≠ CONFIRMED FINDING
SCANNER FINDING ≠ CONFIRMED VULNERABILITY
BUG ≠ VULNERABILITY ≠ RISK
```
Secure loop：
```text
BUILD → SCAN → FIND → UNDERSTAND/PROPOSE → REVIEW → FIX → TEST → RE-SCAN → VERIFY → REPORT
```
Visual 也必須保留這些區別；不能因插圖把 Finding 畫成已確認 Attack。

---

# 21. Offensive Security Safety Boundary

僅使用 localhost、student-owned code、teacher-provided target、VM/Docker isolated lab、TryHackMe、CTF、deliberately vulnerable lab、explicitly authorized range。

> **Publicly accessible ≠ authorized.**

---

# 22. Antigravity Prompt / YAML

實作 Lesson 應提供可重用 Prompt/YAML：ROLE / CONTEXT / MISSION / SCOPE / OUT OF SCOPE / CONSTRAINTS / STEPS / HUMAN REVIEW GATES / ACCEPTANCE CRITERIA / EVIDENCE。

---

# 23. Lesson Handoff

每課最後回答：
```text
WHAT WE NOW KNOW
WHAT WE STILL DO NOT KNOW
WHY NEXT LESSON IS NECESSARY
```
Handoff Visual 優先直接把同一 Persistent Project / Evidence / Object 交到下一課，而非 generic victory pose。

---

# 24. GitHub Sync Rule

Meaningful Design Batch 應同步 GitHub，通常約 5–6 頁，必要時最多約 10 頁。每批：更新 Teaching Script → Boundary/Transition check → GitHub → progress report。不要等使用者再次提醒。

---

# 25. Final Content + Visual Audit（v1.2 強化）

一課完成後，至少檢查：

### Curriculum / Story
- [ ] Mission 符合 Master Curriculum？
- [ ] 沒侵入其他 Lesson / 新增不必要支線？
- [ ] Slide 00 定位完成？
- [ ] Storyline 有因果？
- [ ] 每頁 Purpose 不重複？
- [ ] Transition 自然？

### Slide Quality
- [ ] One Main Question？
- [ ] One Main Visual？
- [ ] One Memory Line？
- [ ] Student-facing 不擁擠？
- [ ] Teacher Script 足夠？

### Content-Driven Visual — 每頁都要過
- [ ] Visual 是否由當頁 Concept 推導？
- [ ] 煥哥是否有 page-specific Role？
- [ ] Expression 是否符合 Concept？
- [ ] 是否有明確 Action，而不是站立說話？
- [ ] 是否有 Concept-matched Prop？
- [ ] 是否直接與核心內容互動？
- [ ] 是否避免與前後頁無理由重複 Pose？
- [ ] 是否有值得保留的 Cross-Slide Callback？
- [ ] 圖像是否可能造成概念誤解？

### Practice / Evidence
- [ ] Representative Lab / Example？
- [ ] Human Review？
- [ ] Test / Verification？
- [ ] Evidence？

### Continuity / Repository
- [ ] Persistent Project？
- [ ] PREVIEW → TEACH → REUSE？
- [ ] Next Lesson Handoff？
- [ ] Canonical README / `_myplan_` 一致？

---

# 26. Freeze Rule

只有 Content Audit + Visual Audit 都通過，才可標：
```text
CANONICAL FINAL / PPT-READY
```

若任一正式內容頁只有 generic avatar、speech-only avatar、或人物與核心內容無互動，**不得 Freeze**。

Freeze 後主要限 factual correction、Traditional Chinese refinement、visual-production refinement、teacher feedback、lab bug fix、safety correction；不要因新工具重新增加 Mandatory Branch。

---

# 27. Standard Lesson Artifact Set

```text
LessonX/README.md
_myplan_/
  AIIS-LX-COMPLETE.md
  AIIS-LX-Detailed-Lecture-Plan.md
  AIIS-LX-slide-00-teaching-script.md
  AIIS-LX-Teaching-Script-S01-S06.md
  AIIS-LX-Teaching-Script-S07-S12.md
  ...
  AIIS-LX-Content-Driven-Visual-Audit-*.md
```

`COMPLETE.md` 保存 Mission / Boundary / Storyline / Purpose Map / Timing / Lab / Evidence / Handoff / Freeze Status。

---

# 28. New Lesson SOP

使用者說「開始 AIIS_Lx」時自動：
```text
1 Read Master Curriculum
2 Read Course Design Standard
3 Read Lesson canonical files
4 Read adjacent boundaries
5 Confirm Story position / Mission / Boundary
6 Build Storyline
7 Build Slide Purpose Map
8 Create Slide 00
9 Write slide-by-slide scripts in batches
10 Design page-specific Content-Driven Visual while writing each slide
11 Sync each meaningful batch to GitHub
12 Build Lab + Evidence
13 Complete Handoff
14 Run Final Content + Visual Audit
15 Mark CANONICAL FINAL / PPT-READY only if both pass
```

**重要：Visual 不應等到整課文字完成才補。從 L6 起，逐頁 Teaching Script 第一次寫入時就必須同時完成 Content-Driven Visual。**

---

# 29. 新 Course SOP

```text
DEFINE COURSE PURPOSE → BUILD COURSE STORY → DEFINE STUDENT JOURNEY
→ DEFINE PERSISTENT PROJECT → SPLIT INTO LESSON MISSIONS → BOUNDARIES
→ DESIGN L0 EXPERIENCE → DESIGN EACH LESSON → SLIDE-BY-SLIDE + VISUAL
→ AUDIT WHOLE COURSE
```

---

# 30. 使用者不需要再提醒的預設規則

未來不需要再提醒：L0–L16 同一標準、先梳理 Storyline、像 L1、老師講稿、每頁視覺、煥哥必須依內容做不同表情/動作/道具/互動、Cross-Slide Callback、Transition、GitHub Sync、不要發散。

以上全部是預設行為。

---

# 31. Core Mnemonics

> **COURSE STORY FIRST. LESSONS SECOND. SLIDES THIRD.**
> **MASTER FIRST. LESSON SECOND. TOOL THIRD.**
> **ONE SLIDE = ONE MAIN QUESTION + ONE MAIN VISUAL + ONE MEMORY LINE.**
> **CONTENT DEFINES THE VISUAL. THE CHARACTER TEACHES THROUGH ACTION.**
> **詳細的是教學設計；簡潔的是學生看到的畫面。**
> **AI BUILDS. HUMAN VERIFIES.**
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
> **NO EVIDENCE, NO TRUST.**

---

# 32. 最終原則

AIIS 不以介紹最多 AI 工具為目標，而是建立學生可反覆使用的能力鏈。

```text
COURSE STORY → LESSON JOURNEY → LESSON MISSION → SLIDE STORY
→ CONTENT-DRIVEN VISUAL → PRACTICE → EVIDENCE → HANDOFF
```

每個 Course / Lesson / Slide 都問兩件事：
1. **它是否真的推進課程故事與學生能力？**
2. **它的 Visual 是否真的在教這一頁，而不只是裝飾？**

若答案不是明確的「是」，就刪除、重設計、延後或移到 `Further Exploration`。