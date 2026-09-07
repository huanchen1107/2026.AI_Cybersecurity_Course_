# AIIS_L2 — COMPLETE
## MANAGE：Spec-Driven AI Engineering
### OpenSpec × Antigravity × Git × GitHub

Date: 2026-09-07
Status: **PLANNING COMPLETE / CANONICAL**

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
>
> 規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。

---

# 1. L2 這堂課到底在做什麼？

L1 已經讓學生體驗：

```text
Prompt → AI → Working Software
```

L2 不再重做 Weather Security Center，而是回答下一個問題：

> **AI 可以很快修改程式，但我們如何管理 AI 產生的 Change？**

因此 L2 的唯一主線是：

```text
REQUEST
   ↓
DEFINE — OpenSpec
   ↓
BUILD — Antigravity
   ↓
VERIFY — Diff + Test + Acceptance Criteria + Human Review
   ↓
REMEMBER — Git + GitHub
```

整堂課只使用一個持續案例：

```text
add-weather-last-updated
```

不建立第二個 App，不額外開新工具支線。

---

# 2. L2 每一頁到底在做什麼？— Canonical Slide Purpose Map

這一節是製作 PPT、NotebookLM 分批生成與教師備課時的**第一層導航圖**。

原則：
> **一頁只承擔一個主要認知任務。**

詳細內容則放在各 Slide Teaching Script，不把所有教師講稿塞進投影片。

## Slide 00 — 課程定位 / Cover

### S00 — L2 MANAGE：從「做得出來」到「管得住改變」
**這頁在做什麼：** 把 L1 BUILD 接到 L2 MANAGE，告訴學生今天不是再做一個新網站，而是學會管理 AI 對既有專案做出的變更。

學生離開本頁只需記住：
> **L1 BUILD IT → L2 MANAGE IT**

---

# PART A — WHY MANAGE? — S01–S06
## 先讓學生感覺到「只靠 Prompt 不夠」

### S01 — AI Built It. What Happens Next?
**這頁在做什麼：** 重新打開 L1 Weather Security Center，製造第一個認知衝突：網站能跑，不代表工程變更已經可管理。

核心問題：
> 誰要求改？為什麼改？哪些不能改？怎樣算完成？

---

### S02 — One Sentence Can Change Many Files
**這頁在做什麼：** 用一句 `Add Last Updated` 讓學生看到：一個很小的 Request 也可能讓 AI 改很多檔案，因此需要 Change Control。

學生只需記住：
> **CAN CHANGE ≠ SHOULD CHANGE**
> 可以改，不代表應該改。

---

### S03 — The Vibe Coding Problem
**這頁在做什麼：** 肯定 Vibe Coding 在快速 Build 的價值，同時指出專案持續成長後，聊天式 Prompt 缺乏持久的 Scope、Decision、Done 與 History。

不是批評 Vibe Coding，而是完成角色升級：
```text
FAST CREATION → CONTROLLED EVOLUTION
```

---

### S04 — Prompt vs Spec
**這頁在做什麼：** 第一次清楚區分 Prompt 與 Spec：Prompt 是對 AI 的當下指令；Spec 是對 Change 的持久定義。

學生只需記住：
> **A PROMPT ASKS. A SPEC DEFINES.**

---

### S05 — Meet OpenSpec
**這頁在做什麼：** 正式介紹 OpenSpec，但不教繁瑣語法；讓學生知道重要 Requirements 不應只存在 Chat History，而應成為 Project 裡可保存的 Change。

核心：
> **Requirements must not live only in chat history.**

---

### S06 — Four Layers of AI Engineering
**這頁在做什麼：** 建立整堂 L2 的總地圖，讓後面所有操作都有位置。

```text
DEFINE   → OpenSpec
BUILD    → Antigravity
VERIFY   → Diff + Test + AC + Human
REMEMBER → Git + GitHub
```

這是 L2 的 Anchor Slide。

---

# PART B — DEFINE — S07–S12
## 真正建立第一個 OpenSpec Change

### S07 — A Real Request Arrives
**這頁在做什麼：** 從真實使用者問題出發：「我不知道氣象資料什麼時候更新」，先辨認 Problem / Need，而不是立刻寫 Code。

```text
PROBLEM → NEED → CHANGE
```

---

### S08 — Change = A Unit of Engineering Work
**這頁在做什麼：** 給這次工作一個正式身份：`add-weather-last-updated`，讓學生知道 Change 不是 Prompt、File 或 Code，而是一個可定義、實作、驗證、保存的工程單位。

---

### S09 — WHY / NEED
**這頁在做什麼：** 教學生先描述「為什麼需要改」，不要把 `edit index.html` 這種 HOW 誤寫成 Need。

核心順序：
```text
WHY → WHAT → HOW
```

---

### S10 — Scope / Out of Scope
**這頁在做什麼：** 替 Change 畫邊界，第一次正式教學生：Spec 不只說「要做什麼」，也要說「這次不要碰什麼」。

例如：
- IN：Last Updated
- OUT：Authentication / DB schema / API redesign / unnecessary dependency

---

### S11 — Requirements
**這頁在做什麼：** 把口語 Request 轉成「系統應具備什麼行為」，建立 Request 與 Requirement 的差異。

```text
REQUEST = 人想要什麼
REQUIREMENT = 系統應做到什麼
```

---

### S12 — Acceptance Criteria = Definition of Done
**這頁在做什麼：** 在 AI 寫 Code 以前先定義 PASS / FAIL，讓學生知道 Done 不是 AI 自己宣布的。

核心：
> **AI DOES NOT DEFINE DONE. THE SPEC DEFINES DONE.**

到這頁結束，仍然沒有讓 AI 修改任何檔案。

---

# PART C — BUILD — S13–S18
## 讓 Antigravity 在 Spec 與 Human Control 下實作

### S13 — Give AI the Project + Spec
**這頁在做什麼：** 改變學生使用 AI Coding Agent 的方式：不再只丟一句 Prompt，而是讓 AI 同時讀 Existing Project + OpenSpec Change + Scope + Acceptance Criteria。

---

### S14 — Inspect First
**這頁在做什麼：** 教學生在 AI 修改前先讓 Agent 看懂 Repository、Data Flow 與既有能力。

核心：
> **INSPECT BEFORE YOU EDIT.**

---

### S15 — Plan Before Code
**這頁在做什麼：** 要求 AI 在寫 Code 前先提出 Implementation Plan，讓錯誤方向可以在低成本階段被發現。

```text
SPEC → INSPECT → PLAN → CODE
```

---

### S16 — Human Plan Review
**這頁在做什麼：** 把 Human-in-the-loop 變成真正的 Gate。學生根據 Spec 審查 AI Plan，做 APPROVE / REVISE / REJECT。

同時正式建立 Scope Creep 概念。

---

### S17 — Implement the Minimal Change
**這頁在做什麼：** Plan 通過後才允許 AI 實作，而且只做完成需求所需的最小必要變更。

核心：
> **MINIMAL = NECESSARY + SUFFICIENT**

---

### S18 — AI Summary Is Not Evidence
**這頁在做什麼：** 切斷「AI 說 Done → 人就相信」的習慣，正式從 BUILD 轉進 VERIFY。

核心：
> **AI CLAIM ≠ VERIFIED EVIDENCE**

---

# PART D — VERIFY — S19–S23
## 從 AI 的宣稱，走到可檢查的證據

### S19 — Changed Files
**這頁在做什麼：** 第一層 Verification：比較 Plan 預期檔案與實際 Changed Files，快速發現非預期 Change Surface。

```text
UNEXPECTED ≠ WRONG
UNEXPECTED = REVIEW SIGNAL
```

---

### S20 — Diff = Before vs After
**這頁在做什麼：** 從「哪些檔案被碰」進一步看到「每個檔案到底加了、刪了、改了什麼」。

核心：
> **不要只審最後畫面，要審實際變更。**

---

### S21 — Run / Test
**這頁在做什麼：** 讓學生真的把系統跑起來，確認新功能存在且原本 Weather 功能沒有被破壞。

核心：
> **LOOKS RIGHT ≠ WORKS RIGHT**

---

### S22 — Verify Against Acceptance Criteria
**這頁在做什麼：** 把 S12 寫好的 AC 拿回來，一條一條用 Evidence 判斷 PASS / FAIL，完成 DEFINE → VERIFY 閉環。

核心：
> **SPEC DEFINES DONE. EVIDENCE PROVES DONE.**

---

### S23 — Human Decision
**這頁在做什麼：** Evidence 都在桌上之後，由 Human 做 ACCEPT / REVISE / REJECT，而不是讓 AI 自己核准自己。

```text
EVIDENCE → HUMAN REVIEW → DECISION
```

---

# PART E — REMEMBER — S24–S27
## 把已驗證的 Change 變成工程記憶

### S24 — Software Needs Memory
**這頁在做什麼：** 用 `final / final2 / really-final` 的混亂讓學生理解：今天能跑還不夠，未來必須知道 What / Why / When / Which Version。

---

### S25 — Commit = Named Checkpoint
**這頁在做什麼：** 把 Commit 解釋成「有名字的已驗證工程檢查點」，而不是開始背 Git commands。

核心：
> **COMMIT AFTER VERIFY.**

---

### S26 — Git ≠ GitHub
**這頁在做什麼：** 一頁解決學生最常見混淆：Git 是本機版本控制；GitHub 是遠端共享 Repository。

不在這頁教 branch / merge / rebase。

---

### S27 — GitHub = Engineering Memory
**這頁在做什麼：** 把 GitHub 從「放 Code 的地方」提升成整學期保存 Spec + Code + Evidence + History 的 Engineering Memory。

並預告 L4、L13、L15–16 會重用同一方法。

---

# PART F — COMPLETE LAB + HANDOFF — S28–S30
## 不再教新觀念，讓學生完成一次完整流程

### S28 — Student Mission: One Controlled Change
**這頁在做什麼：** 學生真正操作 `add-weather-last-updated`，完整走 DEFINE → BUILD → VERIFY → REMEMBER。

評量重點不是誰最快，而是：
> **誰能證明自己改對。**

---

### S29 — Evidence Package
**這頁在做什麼：** 把 Lab 的最小工程證據整理成 8 類，不要求學生寫冗長報告。

```text
Request / Spec / AI Plan / Human Review
Diff / Test / AC Verification / Git History
```

核心：
> **Evidence is part of engineering.**

---

### S30 — From MANAGE to UNDERSTAND
**這頁在做什麼：** 收束 L2，不再加入新工具；提出下一個問題：「我們知道 WHY、WHAT、PASS/FAIL、History，但真的看懂 Code 如何運作嗎？」自然交棒 L3。

```text
L1 BUILD IT
 ↓
L2 MANAGE IT ✓
 ↓
L3 UNDERSTAND IT ← NEXT
 ↓
L4 SECURE IT
```

---

# 3. 一眼看懂整個 L2 的故事

```text
S00  我們今天要從 BUILD 進入 MANAGE

S01  能跑，不代表可管理
S02  小 Request 也可能造成大 Change Surface
S03  Vibe Coding 很快，但持續工程需要控制
S04  所以 Prompt 不等於 Spec
S05  用 OpenSpec 保存 Change 定義
S06  建立 DEFINE / BUILD / VERIFY / REMEMBER 地圖

S07  真實需求來了
S08  給 Change 一個身份
S09  先定義 WHY
S10  再畫 Scope 邊界
S11  寫成 Requirements
S12  先定義 Done

S13  把 Project + Spec 交給 AI
S14  AI 先 Inspect
S15  AI 先 Plan
S16  Human 先 Review Plan
S17  才讓 AI Implement
S18  AI 說 Done 還不能信

S19  先看改了哪些 Files
S20  再看 Diff
S21  實際 Run / Test
S22  對回 Acceptance Criteria
S23  Human 決定 Accept / Revise / Reject

S24  已驗證 Change 還需要 Memory
S25  Commit 成為 Named Checkpoint
S26  分清 Git 與 GitHub
S27  GitHub 保存 Engineering Story

S28  學生完整做一次
S29  整理 Evidence
S30  L2 收束，進入 L3 UNDERSTAND
```

---

# 4. L2 課堂節奏

| 區段 | Slides | 主要問題 | 建議節奏 |
|---|---:|---|---:|
| Opening / Why | S00–S06 | 為什麼不能只一直 Prompt？ | 35–40 min |
| DEFINE | S07–S12 | 我們到底要改什麼？ | 35–40 min |
| BUILD | S13–S18 | 如何讓 AI 受控實作？ | 40–45 min |
| Break | — | — | 10 min |
| VERIFY | S19–S23 | 怎麼證明 AI 改對？ | 40–45 min |
| REMEMBER | S24–S27 | 怎麼保存工程歷史？ | 25–30 min |
| Lab / Closure | S28–S30 | 學生能否完整走一次？ | 35–50 min |

依實際課堂時數可壓縮講解，把更多時間留給 S28 Lab。

---

# 5. L2 投影片密度規則

每頁遵守：

```text
ONE SLIDE
=
ONE MAIN QUESTION
+
ONE MAIN VISUAL
+
ONE MEMORY LINE
```

詳細內容存在 Teaching Script，不代表全部放上投影片。

建議每頁 ON-SLIDE：
- 1 個主標題
- 1 個核心圖或對比
- 3–5 個短重點以內
- 1 個記憶句

教師講稿、例子、常見誤解、互動題目放 Speaker Notes / Teaching Script。

> **高品質 ≠ 高密度。**
>
> **詳細的是教學設計；簡潔的是學生看到的畫面。**

---

# 6. Canonical L2 Artifacts

- `Lesson2/README.md` — L2 canonical contract
- `_myplan_/2026-09-07-AIIS-L2-Detailed-Lecture-Plan.md` — detailed architecture
- `_myplan_/2026-09-07-AIIS-L2-Teaching-Script-S01-S06.md`
- `_myplan_/2026-09-07-AIIS-L2-Teaching-Script-S07-S12.md`
- `_myplan_/2026-09-07-AIIS-L2-Teaching-Script-S13-S18.md`
- `_myplan_/2026-09-07-AIIS-L2-Teaching-Script-S19-S23.md`
- `_myplan_/2026-09-07-AIIS-L2-Teaching-Script-S24-S30.md`

## Completion Decision

L2 planning is now complete at the architecture/story level and detailed teaching-script level.

Do not expand L2 with additional mandatory tools or topics unless the course owner explicitly changes the scope.

L2 remains:

> **MANAGE AI-GENERATED CHANGE.**
> **管理 AI 產生的工程變更。**
