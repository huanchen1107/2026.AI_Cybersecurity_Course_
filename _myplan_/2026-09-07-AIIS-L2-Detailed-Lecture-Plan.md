# AIIS_L2 — Spec-Driven AI Engineering
## OpenSpec × Antigravity × Git × GitHub

Status: **PLANNING COMPLETE / CANONICAL / PPT-READY — 2026-09-07**

Master Curriculum Position: **L2 / MANAGE**

Canonical navigation document:
`_myplan_/2026-09-07-AIIS-L2-COMPLETE.md`

Detailed teaching scripts:
- `2026-09-07-AIIS-L2-slide-00-teaching-script.md`
- `2026-09-07-AIIS-L2-Teaching-Script-S01-S06.md`
- `2026-09-07-AIIS-L2-Teaching-Script-S07-S12.md`
- `2026-09-07-AIIS-L2-Teaching-Script-S13-S18.md`
- `2026-09-07-AIIS-L2-Teaching-Script-S19-S23.md`
- `2026-09-07-AIIS-L2-Teaching-Script-S24-S30.md`

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
>
> **規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。**

Core learning loop:

```text
DEFINE → BUILD → VERIFY → REMEMBER
```

Canonical engineering flow:

```text
REQUEST
→ OPENSPEC CHANGE
→ WHY / SCOPE / REQUIREMENTS / ACCEPTANCE CRITERIA
→ ANTIGRAVITY
→ INSPECT
→ PLAN
→ HUMAN PLAN REVIEW
→ MINIMAL IMPLEMENTATION
→ CHANGED FILES
→ DIFF
→ RUN / TEST
→ VERIFY AGAINST ACCEPTANCE CRITERIA
→ HUMAN DECISION
→ GIT COMMIT
→ GITHUB
→ HISTORY / EVIDENCE
```

## Curriculum Boundary

L2 使用 L1 建立的同一個 **AI Weather Security Center**，不重新建立 App。OpenSpec 是 L2 `MANAGE` 任務採用的工程方法，不是新增課程分支。

- Python / FastAPI / HTTP / API / JSON internals → L3
- Semgrep scanning / remediation / re-scan → L4
- Supervised ML → L5–L7
- Deep Learning → L9–L10
- Reinforcement Learning → **不列入正式 AIIS 課程**
- Red Team → L11–L12
- Blue Team → L13
- ISO 27001 / Risk Governance → L14
- Final Project → L15–L16

---

# Teaching Story — Slide 00 + S01–S30

## Slide 00 — COURSE POSITIONING
**這頁在做什麼：** 把 L1 BUILD 接到 L2 MANAGE；同一個 Weather Security Center，新的任務是管理一個 AI-generated Change。

```text
L1 BUILD IT → L2 MANAGE IT → L3 UNDERSTAND IT → L4 SECURE IT
```

---

## PART A — WHY MANAGE — S01–S06

### S01 — AI 做出來了，接下來呢？
**這頁在做什麼：** 建立 `Working Software ≠ Managed Software`。

### S02 — 一句小需求，可能改很多地方
**這頁在做什麼：** 建立 Change Surface 直覺；`CAN CHANGE ≠ SHOULD CHANGE`。

### S03 — Vibe Coding 很快，但專案要持續演化
**這頁在做什麼：** 從 Fast Creation 轉向 Controlled Evolution，而不是否定 Vibe Coding。

### S04 — Prompt 與 Spec 不一樣
**這頁在做什麼：** Prompt 負責當下互動；Spec 負責持久定義 Change。

### S05 — 認識 OpenSpec
**這頁在做什麼：** 把重要 Requirements 從 Chat History 搬進 Project。

### S06 — AI Engineering 四層地圖
**這頁在做什麼：** 建立全課 Anchor：`DEFINE → BUILD → VERIFY → REMEMBER`。

---

## PART B — DEFINE — S07–S12

### S07 — 真實需求來了
**這頁在做什麼：** `PROBLEM → NEED → CHANGE`；不從 Code 開始。

### S08 — Change 是工程工作的管理單位
**這頁在做什麼：** 建立 `add-weather-last-updated` 作為完整工程工作單位。

### S09 — WHY / NEED
**這頁在做什麼：** 建立 `WHY → WHAT → HOW`；不要在 WHY 偷塞 Implementation。

### S10 — Scope / Out of Scope
**這頁在做什麼：** 畫出 Change 邊界，降低 Scope Creep。

### S11 — Requirements
**這頁在做什麼：** `Request = 人想要什麼`；`Requirement = 系統應做到什麼`。

### S12 — Acceptance Criteria
**這頁在做什麼：** 在寫 Code 前先定義 Done；S22 再用 Evidence 回來驗證。

---

## PART C — BUILD — S13–S18

### S13 — Project + Spec 一起交給 AI
**這頁在做什麼：** `CONTEXT BEFORE CODE`；Prompt 指揮下一步，Spec 定義 Change。

### S14 — INSPECT FIRST
**這頁在做什麼：** 修改前先理解 Repository 與既有 Data Flow。

### S15 — PLAN BEFORE CODE
**這頁在做什麼：** 在低成本階段先審查 AI Implementation Plan。

### S16 — HUMAN PLAN REVIEW
**這頁在做什麼：** Human Gate：`APPROVE / REVISE / REJECT`。

### S17 — IMPLEMENT THE MINIMAL CHANGE
**這頁在做什麼：** 只做 Necessary + Sufficient 的最小必要變更。

### S18 — AI Summary Is Not Evidence
**這頁在做什麼：** `AI CLAIM ≠ VERIFIED EVIDENCE`；正式從 BUILD 轉入 VERIFY。

---

## PART D — VERIFY — S19–S23

本段 Anchor：

```text
CHANGED FILES
      ↓
DIFF
      ↓
RUN / TEST
      ↓
ACCEPTANCE CRITERIA
      ↓
HUMAN DECISION
```

### S19 — Changed Files
**這頁在做什麼：** 比對 Planned Files 與 Actual Files；Unexpected 是 Review Signal。

### S20 — Diff
**這頁在做什麼：** 看 Before vs After，不能只看最後畫面。

### S21 — Run / Test
**這頁在做什麼：** 驗證新功能能運作，既有行為沒有被破壞。

### S22 — Verify Against Acceptance Criteria
**這頁在做什麼：** 用 Evidence 回答 S12 預先定義的每一條 AC。

### S23 — Human Decision
**這頁在做什麼：** 根據 Evidence 做 `ACCEPT / REVISE / REJECT`。

---

## PART E — REMEMBER — S24–S27

### S24 — Software Needs Memory
**這頁在做什麼：** 從 `final/final2/really-final` 混亂建立版本歷史需求。

### S25 — Commit = Named Checkpoint
**這頁在做什麼：** Commit 是已驗證 Change 的命名檢查點；不是 Git command lesson。

### S26 — Git ≠ GitHub
**這頁在做什麼：** Git = Local Version Control；GitHub = Remote Shared Repository。

### S27 — GitHub = Engineering Memory
**這頁在做什麼：** 保存 `SPEC + CODE + EVIDENCE + HISTORY`，供後續 L4、L13、L15–16 重用。

---

## PART F — COMPLETE LAB + HANDOFF — S28–S30

### S28 — Student Mission
**這頁在做什麼：** 學生完整執行一次 `DEFINE → BUILD → VERIFY → REMEMBER`，不再增加新理論。

### S29 — Evidence Package
**這頁在做什麼：** 整理最小工程證據包：Request / Spec / AI Plan / Human Review / Diff / Test / AC / Git History。

### S30 — From MANAGE to UNDERSTAND
**這頁在做什麼：** 收束 L2，提出下一個問題：「我們會管理 Change 了，但真的看懂 Code 與 Data Flow 嗎？」自然交棒 L3。

```text
L1 — BUILD IT
L2 — MANAGE IT
L3 — UNDERSTAND IT
L4 — SECURE IT
```

---

# Canonical Lab

唯一正式案例：

```text
Change: add-weather-last-updated

Need:
使用者需要知道目前顯示的氣象資料最後更新時間。

Scope:
在既有 Weather Dashboard 顯示 Last Updated。

Out of Scope:
- database schema changes
- authentication changes
- API redesign
- unnecessary dependencies
- unrelated refactor

Acceptance Criteria:
1. Dashboard visibly shows Last Updated.
2. Time is readable.
3. Existing weather display still works.
4. Existing API behavior is not intentionally changed.
5. No unnecessary dependency is added.
```

學生完整工作流：

```text
Create / Review OpenSpec Change
→ Antigravity Inspect
→ AI Implementation Plan
→ Human Plan Review
→ Minimal Implementation
→ Changed Files
→ Diff
→ Run / Test
→ Acceptance Criteria Verification
→ Human Decision
→ Commit
→ GitHub
```

---

# PPT Production Rule

```text
ONE SLIDE
= ONE MAIN QUESTION
+ ONE MAIN VISUAL
+ ONE MEMORY LINE
```

每頁 ON SLIDE 原則：
- 1 個清楚標題；
- 1 個主要視覺或對比；
- 約 3–5 個核心資訊；
- 1 句 Memory Line。

詳細說明、例子、常見誤解、活動與教師提問放 Teaching Script，不全部塞進投影片。

> **高品質 ≠ 高密度。**
> **詳細的是教學設計；簡潔的是學生看到的畫面。**

---

# Final Freeze Check

- [x] Slide 00 exists and does not renumber S01–S30.
- [x] S01–S30 each has one primary cognitive task.
- [x] Traditional Chinese is the primary teaching language.
- [x] English is retained only where useful for technical terms / memory lines.
- [x] Same Weather Security Center is reused; no second App.
- [x] OpenSpec remains a method inside L2 MANAGE, not a new lesson.
- [x] Antigravity is used as the representative AI engineering agent.
- [x] Human Review is present before and after implementation.
- [x] Verification is evidence-based, not AI self-report based.
- [x] Git/GitHub is taught as engineering memory, not a command-heavy Git course.
- [x] L3 Python/FastAPI internals are not taught early.
- [x] L4 Semgrep/security remediation is not taught early.
- [x] RL is excluded from the formal curriculum.
- [x] S28 Lab is the main hands-on integration point.
- [x] S30 explicitly hands off to L3 UNDERSTAND.

## Final Status

> **AIIS_L2 = CANONICAL FINAL / PPT-READY**

Unless the Master Curriculum changes, future edits to L2 should be corrections, visual-production refinements, or teaching-feedback revisions—not new mandatory branches or additional tools.
