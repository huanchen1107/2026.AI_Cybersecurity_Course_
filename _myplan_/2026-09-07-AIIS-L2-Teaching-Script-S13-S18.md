# AIIS_L2 — 教學講稿 S13–S18
## Part C — Antigravity 依照 Spec 實作

狀態：PART C TEACHING SCRIPT COMPLETE — 2026-09-07
課程位置：L2 / MANAGE
語言規則：繁體中文為主；必要資訊工程術語保留英文並搭配中文解釋。

前一段已完成 DEFINE：

```text
OpenSpec Change
→ WHY / NEED
→ SCOPE / OUT OF SCOPE
→ REQUIREMENTS
→ ACCEPTANCE CRITERIA
```

現在進入第二層：

```text
DEFINE → BUILD → VERIFY → REMEMBER
          ↑
        現在
```

Part C 的核心不是「叫 AI 寫 Code」，而是：

> **讓 AI 在明確 Spec 與人類控制下進行最小必要實作。**

---

# Slide 13 — Give AI the Project + Spec, Not Just a Prompt
## 不要只給 AI 一句 Prompt；要讓它讀 Project + Spec

### 本頁目的
讓學生理解 Spec-Driven AI Engineering 的第一個實務差異：AI 不再只接收一句自然語言指令，而是先讀既有專案與已核准的 Change。

### 主畫面

左側：
```text
PROMPT-DRIVEN

"Add Last Updated."
        ↓
       AI
        ↓
     ??? CODE
```

右側：
```text
SPEC-DRIVEN

Existing Project
      +
OpenSpec Change
      +
Scope / Constraints
      +
Acceptance Criteria
      ↓
      AI
      ↓
INSPECT → PLAN → IMPLEMENT
```

底部：

> **CONTEXT BEFORE CODE.**
> **先給正確脈絡，再要求寫程式。**

### 煥哥角色
角色：**AI 任務指揮者（AI Task Director）**。

不是直接按下「Generate Code」，而是把 Project 與 Spec 一起交給 Antigravity。

### 教師講稿
> 現在終於輪到 Antigravity。
>
> 但這一次，我們不再只說 `Add Last Updated`。

比較兩種方式。

方式 A：
```text
Add Last Updated to my website.
```

方式 B：
```text
Read the existing project.
Read the OpenSpec change:
add-weather-last-updated.

Inspect the repository first.
Do not modify files yet.
```

問：
> 哪一個方式讓 AI 比較知道「現在這個 Project 已經有什麼」以及「這次到底允許做什麼」？

### AI 需要的工程脈絡

```text
PROJECT CONTEXT
目前系統是什麼？

+

CHANGE CONTEXT
這次為什麼改？改什麼？不能改什麼？

+

DONE CRITERIA
怎樣才算完成？
```

教師：
> Prompt 還是會用，但 Prompt 現在主要是在告訴 Agent「如何執行工作」；Spec 則負責定義「這個 Change 到底是什麼」。

### Prompt 與 Spec 的合作

```text
SPEC
定義 Change
   ↓
PROMPT
指揮 Agent 執行下一步
   ↓
AI ACTION
```

不是 Prompt vs Spec 二選一。

### 本頁帶走
1. AI 應先讀既有 Project。
2. AI 應讀已定義的 Spec。
3. Prompt 負責指揮工作流程，Spec 負責定義工程邊界。

核心：
> **DON'T JUST PROMPT THE AI. GROUND THE AI.**
> **不要只下 Prompt，要先讓 AI 建立正確的專案脈絡。**

### 銜接 S14
> 那 AI 讀完 Project + Spec 後，第一件事是開始改嗎？不是。

下一頁：**INSPECT FIRST**

建議時間：7–9 分鐘。

---

# Slide 14 — INSPECT FIRST
## 先檢查，再修改

### 本頁目的
建立 Agentic Coding 最重要的操作習慣之一：AI 在修改前先閱讀 Repository、確認既有資料流與可能影響範圍。

### 核心句

> **INSPECT BEFORE YOU EDIT.**
> **先檢查，再修改。**

### 主畫面

```text
BAD FLOW
REQUEST → EDIT → HOPE

GOOD FLOW
REQUEST → INSPECT → UNDERSTAND → PLAN → EDIT
```

### 建議給 Antigravity 的 Prompt

```text
請先閱讀目前專案，以及 OpenSpec Change：
add-weather-last-updated。

先檢查 Repository，不要修改任何檔案。

請確認：
1. 哪些既有元件與此需求有關？
2. 哪些檔案可能需要修改？
3. 是否可以重用既有的時間資料？
4. 有哪些假設或風險？

目前只做 Inspect，不要開始實作。
```

### 教師講稿
> 注意最後一句：**不要修改任何檔案。**
>
> 為什麼要特別寫？因為 Coding Agent 很積極。你問它怎麼做，它有時候會直接幫你做完。

### Inspect 要找什麼

以 Weather Security Center 為例：

```text
UI
Last Updated 要顯示在哪？

DATA FLOW
時間資訊從哪裡來？

EXISTING CODE
目前是否已經取得 timestamp？

FILES
哪些檔案真的相關？

DEPENDENCIES
是否根本不需要新套件？
```

### 重要觀念：Reuse Before Add

如果現有 API 或資料結構已經包含更新時間：

```text
EXISTING DATA
     ↓
   REUSE ✓
```

而不是：

```text
EXISTING DATA
     ↓
IGNORE
     ↓
NEW PACKAGE
NEW HELPER
NEW SERVICE
```

核心：
> **REUSE BEFORE YOU ADD.**
> **先重用，再新增。**

### 學生判斷活動
問：下面哪些是 Inspect？

A. 搜尋目前 timestamp 在哪裡被處理。
B. 直接新增 `time_helper.py`。
C. 找出 Dashboard template。
D. 升級 FastAPI。
E. 檢查 CWA response 是否已有更新時間。

答案：A、C、E。

### 煥哥角色
角色：**Repository Investigator（專案調查者）**。

拿放大鏡查看檔案樹與資料流，不拿鐵鎚直接修改。

### 板書

```text
INSPECT ≠ IMPLEMENT
```

```text
READ → UNDERSTAND → PLAN
```

### 本頁帶走
1. Agent 修改前必須先理解現況。
2. Inspect 階段不應偷偷變成 Implement。
3. 優先重用現有能力，降低 Change Surface。

### 銜接 S15
> Inspect 完之後，我們已經知道可能要碰哪些地方。但還是不能直接 Code。下一步要先把做法寫成 Plan。

建議時間：8–10 分鐘。

---

# Slide 15 — PLAN BEFORE CODE
## 先看計畫，再讓 AI 寫 Code

### 本頁目的
把 AI 的 Plan 變成人類可以在低成本階段審查的中間產物。讓學生理解「先審 Plan」比「Code 寫完再發現方向錯」便宜很多。

### 主畫面

```text
SPEC
 ↓
INSPECT
 ↓
PLAN       ← HUMAN CAN REVIEW HERE
 ↓
CODE
```

核心：

> **PLAN BEFORE CODE.**
> **先計畫，再寫程式。**

### 範例 Implementation Plan

```text
Implementation Plan

1. 檢查目前 Weather Data Flow。
2. 重用既有 Update Timestamp。
3. 在 Dashboard 顯示 Last Updated。
4. 必要時做最小幅度的樣式調整。

預期修改：
- templates/index.html

可能修改：
- static/style.css

預期不需要：
- Database change
- New dependency
- API redesign
```

### 教師講稿
> AI 很會寫 Code，但今天我們先利用 AI 的另一種能力：**先提出 Plan。**

強調：

```text
AI OUTPUT ≠ ONLY CODE
```

AI 也可以產生：

```text
SPEC
PLAN
CODE
TEST
REVIEW
REPORT
```

### 好 Plan 應回答

1. 準備做哪幾步？
2. 預計修改哪些檔案？
3. 每個檔案為什麼需要修改？
4. 哪些部分刻意不碰？
5. 有什麼假設或風險？

### Plan 的價值

比較：

```text
錯誤 PLAN
→ 人看 30 秒發現
→ REVISE
```

與：

```text
錯誤 PLAN
→ 直接寫 300 行 Code
→ 改 8 個檔案
→ 測試失敗
→ 才發現方向錯
```

教師：
> **越早發現錯誤，修正成本通常越低。**

### 煥哥角色
角色：**Plan Reviewer 準備者**。

AI 把 Plan 放到桌上，煥哥先看 Plan，而不是直接看一堆 Code。

### 小活動
給兩個 Plan：

Plan A：
```text
1. Reuse existing timestamp.
2. Update dashboard template.
3. Verify weather display remains functional.
```

Plan B：
```text
1. Upgrade FastAPI.
2. Add a datetime package.
3. Rewrite weather service.
4. Redesign dashboard.
5. Add Last Updated.
```

問：哪一個更符合 Spec？為什麼？

### 板書

```text
SPEC → PLAN → CODE
```

> **PLAN 是 AI 與 Human Review 之間的第一個控制點。**

### 本頁帶走
1. AI 應先提出可審查的實作計畫。
2. Plan 必須能對應 Scope 與 Requirements。
3. 先審 Plan 可以提早發現 Scope Creep。

### 銜接 S16
> Plan 有了，現在輪到誰？不是 AI。輪到 Human。

下一頁：**HUMAN PLAN REVIEW**

建議時間：8–10 分鐘。

---

# Slide 16 — HUMAN PLAN REVIEW
## AI 提案，人類決定

### 本頁目的
建立 Human-in-the-loop 的具體責任。人類不是最後按「Approve」的裝飾，而是在實作前審查 AI 是否理解需求與邊界。

### 主畫面

```text
AI PLAN
   ↓
HUMAN REVIEW
   ↓
┌─────────┬─────────┬─────────┐
│ APPROVE │ REVISE  │ REJECT  │
│ 核准    │ 修正    │ 拒絕    │
└─────────┴─────────┴─────────┘
```

### 核心句

> **AI PROPOSES. HUMAN DECIDES.**
> **AI 提案，人類決定。**

### 六個 Plan Review 問題

```text
1. 這是 Spec 要求的嗎？
2. 在 Scope 裡嗎？
3. 有沒有碰 Out of Scope？
4. 每個預計修改的檔案都有必要嗎？
5. AI 是否新增了不必要 Dependency？
6. Plan 是否涵蓋 Acceptance Criteria？
```

### 紅黃綠燈

```text
🟢 APPROVE
方向正確、範圍合理，可以實作。

🟡 REVISE
方向大致正確，但需要縮小或修改 Plan。

🔴 REJECT
違反 Spec、方向錯誤或風險不可接受。
```

### 故意給錯誤 Plan

```text
1. Add Last Updated.
2. Upgrade FastAPI.
3. Replace CSS framework.
4. Refactor weather service.
5. Change API response format.
```

問學生：

> APPROVE、REVISE 還是 REJECT？

引導：至少需要 REVISE；若核心方向嚴重偏離可 REJECT。

### 正式介紹 Scope Creep

> **Scope Creep（範圍蔓延）= Change 在沒有明確同意下逐漸加入原本沒有要求的工作。**

```text
ORIGINAL CHANGE
      ↓
+ one extra thing
+ another extra thing
+ refactor
+ upgrade
      ↓
UNCONTROLLED CHANGE
```

### AI Change Control

把本課的人類角色講清楚：

```text
AI can suggest.
AI can explain.
AI can implement.

HUMAN controls:
- intent
- scope
- acceptance
```

### 煥哥角色
角色：**Change Gatekeeper（變更守門員）**。

站在 Plan → Code 之間的 Gate，手上有 APPROVE / REVISE / REJECT 三張卡。

### 小活動
每組拿一份 AI Plan，圈出：
- 必要項目
- 可疑項目
- Out-of-Scope 項目

最後投票 APPROVE / REVISE / REJECT。

### 板書

```text
AI PLAN ≠ APPROVED PLAN
```

```text
PLAN
 ↓
HUMAN GATE
 ↓
CODE
```

### 本頁帶走
1. AI 的 Plan 是提案，不是命令。
2. Human Review 在寫 Code 前就開始。
3. Scope Creep 必須被主動識別與控制。

### 銜接 S17
> Plan 通過 Human Gate 之後，現在才真正允許 AI 修改程式。

建議時間：9–12 分鐘。

---

# Slide 17 — IMPLEMENT THE MINIMAL CHANGE
## 實作最小必要變更

### 本頁目的
建立 Minimal Change（最小必要變更）原則：AI 只實作已核准 Plan 所需要的內容，不趁機重構、升級或擴張。

### 核心句

> **MAKE THE MINIMUM NECESSARY CHANGE.**
> **只做完成需求所需的最小必要變更。**

### 主畫面

```text
APPROVED PLAN
      ↓
MINIMAL IMPLEMENTATION
      ↓
EXPECTED FILES ONLY
```

旁邊放一個禁止擴張區：

```text
✕ unrelated refactor
✕ dependency upgrade
✕ API redesign
✕ "while I'm here..."
```

### 給 Antigravity 的實作 Prompt

```text
請依照已核准的 OpenSpec Change
add-weather-last-updated
與已審查通過的 Implementation Plan 進行實作。

要求：
- 嚴格維持在已定義的 Scope 內；
- 只做完成需求所需的最小必要修改；
- 不做無關 Refactor；
- 不新增不必要 Dependency；
- 保留既有行為。

完成修改後，請列出實際修改的檔案。

在 Acceptance Criteria 尚未驗證以前，
不要宣稱 Change 已完成。
```

### 教師講稿
> 現在終於可以 Code。
>
> 注意我們花了多少時間在 Code 以前：Need、Scope、Requirement、Acceptance Criteria、Inspect、Plan、Human Review。

問：
> 這是不是浪費時間？

引導：對小 Demo 可能顯得多，但對持續演化、多人/多 Agent、資安相關系統，這是在降低返工與非預期變更。

### Minimal Change 的原因

```text
SMALLER CHANGE
→ easier to understand
→ easier to review
→ easier to test
→ easier to revert
```

繁中：

```text
變更越聚焦
→ 越容易理解
→ 越容易審查
→ 越容易測試
→ 出問題越容易回復
```

### 不等於「程式碼越少越好」
重要澄清：Minimal Change 不是硬追求最少行數。

> 它的意思是：**不要做超出需求與必要工程品質之外的額外工作。**

必要的測試、錯誤處理、清楚實作仍然可以是必要變更。

### 煥哥角色
角色：**Minimalist Builder（最小變更建構者）**。

用精準工具只修改指定區域，而不是拿大鐵鎚拆整個系統。

### 板書

```text
APPROVED PLAN → IMPLEMENT
```

```text
MINIMAL ≠ CARELESS
MINIMAL = NECESSARY + SUFFICIENT
```

繁中：
> **最小變更不是草率，而是必要且足夠。**

### 本頁帶走
1. AI 依已核准 Plan 實作。
2. 變更應保持聚焦。
3. Minimal Change 降低 Review 與 Verification 成本。

### 銜接 S18
> AI 修改完之後，它通常會很開心地告訴我們：「Done！」現在可以相信嗎？

下一頁：**AI SUMMARY IS NOT EVIDENCE**

建議時間：8–10 分鐘。

---

# Slide 18 — AI SUMMARY IS NOT EVIDENCE
## AI 的完成報告，不等於驗證證據

### 本頁目的
在 BUILD 與 VERIFY 之間建立清楚界線。學生不能把 Agent 的自我報告當成客觀驗證結果。

### 主畫面

左側 AI 對話泡泡：

```text
Done! ✓

✓ Added Last Updated
✓ Existing functionality preserved
✓ No dependencies added
✓ Everything works
```

中央大字：

```text
AI CLAIM
   ≠
VERIFIED EVIDENCE
```

右側：

```text
NEED TO CHECK:
Changed Files
Diff
Run / Test
Acceptance Criteria
Human Review
```

### 核心句

> **AI CLAIM ≠ VERIFIED EVIDENCE**
> **AI 的宣稱，不等於已驗證的證據。**

### 教師講稿
> AI 很可能會給你一份看起來非常完整的 Summary。

讀出：
> Added Last Updated、preserved functionality、no dependency、everything works。

然後問：

> 它說「沒有新增 Dependency」，我們真的看過 `requirements.txt` 了嗎？
>
> 它說「Existing functionality preserved」，我們真的 Run 過嗎？
>
> 它說「Everything works」，誰定義 Everything？

### Self-Report 問題

AI 同時是實作者又是報告者：

```text
AI IMPLEMENTS
     +
AI REPORTS ABOUT ITSELF
```

因此不能只靠自我宣稱完成 Verification。

用學生熟悉的比喻：
> 寫完考卷的人自己說「我全部答對」，不能直接當成滿分證據。

### 從 BUILD 進入 VERIFY

```text
DEFINE ✓
BUILD  ✓
VERIFY ← NEXT
REMEMBER
```

下一階段需要回答：

```text
WHAT ACTUALLY CHANGED?
DOES IT RUN?
DOES IT MATCH THE SPEC?
SHOULD HUMAN ACCEPT IT?
```

### Evidence Preview
只預告，不深入：

```text
Changed Files
Diff
Run / Test
Acceptance Criteria
Human Decision
```

S19–S23 再逐一教。

### 煥哥角色
角色：**Evidence Skeptic（證據審查者）**。

AI 遞來一張大大的 `DONE ✓`，煥哥沒有直接接受，而是拿出 Verification Checklist。

表情：冷靜、專業，不是不信任 AI，而是依流程驗證。

### 板書

```text
AI SAYS DONE
      ≠
ENGINEERING DONE
```

再寫：

```text
CLAIM → CHECK → EVIDENCE → DECISION
```

### 本頁帶走
1. AI Summary 是有用的線索，但不是最終證據。
2. 實作者的自我宣稱必須經過獨立檢查。
3. BUILD 結束不代表 Change 完成。
4. 下一步是 VERIFY。

### Part C 收束

```text
PROJECT + SPEC
      ↓
INSPECT
      ↓
PLAN
      ↓
HUMAN PLAN REVIEW
      ↓
APPROVE / REVISE / REJECT
      ↓
MINIMAL IMPLEMENTATION
      ↓
AI SUMMARY
      ↓
NOT DONE YET
```

教師收尾：

> 到這裡 AI 已經完成實作，但我們還沒有接受這個 Change。
>
> 下一個 Part，我們要從「AI 說它做對了」進入「我們有證據證明它做對了」。

最後揭示：

> **BUILD CREATES THE CHANGE. VERIFY EARNS TRUST.**
> **建構產生變更，驗證建立可信度。**

### 銜接 Part D / Slide 19

下一頁：

**Slide 19 — Changed Files：AI 到底改了哪些檔案？**

建議時間：8–10 分鐘。

---

# Part C 完成檢查

```text
S13 Project + Spec，不只 Prompt
 ↓
S14 INSPECT FIRST
 ↓
S15 PLAN BEFORE CODE
 ↓
S16 HUMAN PLAN REVIEW
 ↓
S17 MINIMAL IMPLEMENTATION
 ↓
S18 AI CLAIM ≠ VERIFIED EVIDENCE
```

學生此時應能說出完整 BUILD 控制流程：

```text
SPEC
 ↓
INSPECT
 ↓
PLAN
 ↓
HUMAN REVIEW
 ↓
IMPLEMENT
 ↓
VERIFY NEXT
```

下一段固定進入：

```text
Part D — VERIFY
S19–S23
```

不得在此加入新的 Build 工具或新 App，以維持 L2 單一工程主線。