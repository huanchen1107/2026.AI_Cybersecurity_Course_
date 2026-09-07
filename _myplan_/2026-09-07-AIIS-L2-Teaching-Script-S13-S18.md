# AIIS_L2 — 逐頁詳細教學稿 S13–S18
## Part C — BUILD：讓 Antigravity 在 Spec 與 Human Control 下實作

狀態：CANONICAL — L1 STYLE — 2026-09-07

統一格式：**目的 → 投影片內容 → 視覺 → 煥哥 → 老師講稿 → 問答 → 核心句 → Transition**。

---

# Slide 13 — 把 Project + Spec 一起交給 AI

## 目的
改變學生使用 Coding Agent 的方式：不是只丟一句 Prompt，而是先讓 AI Ground 在既有 Project 與已核准的 Change Context。

## 投影片內容
左側：
```text
"Add Last Updated"
       ↓
      AI
       ↓
      ???
```
右側：
```text
PROJECT
   +
SPEC
   ↓
  AI
```
底部巨大：
```text
CONTEXT BEFORE CODE.
```
繁中：**先建立正確脈絡，再要求寫程式。**

## 視覺
左右對比。左邊只有一個漂浮 Prompt；右邊 AI 站在 Repository + OpenSpec Change 上。此頁不要提前塞 Inspect / Plan / Diff。

## 煥哥
表情：從 Requirement Owner 轉成 AI Task Director。
動作：把 `PROJECT` 與 `SPEC` 兩張卡一起交給 Antigravity。
視線：看著 AI 是否先取得 Context。

## 老師講稿
現在 DEFINE 已完成。

很多人下一步會直接打：
```text
Add Last Updated. Do it now.
```

我們今天換一種方式：
```text
請閱讀目前 Project 與 OpenSpec Change：
add-weather-last-updated。
先不要修改檔案。
```

Prompt 還是需要，但角色不同：
```text
SPEC   = defines the change
PROMPT = directs the next action
```

Spec 告訴 AI 這次 Change 是什麼；Prompt 告訴 AI 現在先做哪一步。

## 問
如果換另一個 Coding Agent，只給一句 `Add Last Updated`，和同時給它 Repository + Spec，哪一個比較不需要猜？

預期：Project + Spec。

## 核心句
> **CONTEXT BEFORE CODE.**
> **不要只 Prompt AI；先讓 AI Ground 在 Project + Spec。**

## Transition
> AI 有 Context 了。現在第一件事是不是立刻修改？

下一頁：**INSPECT FIRST。**

---

# Slide 14 — INSPECT FIRST

## 目的
建立 Agentic Coding 的基本習慣：修改前先理解 Repository、既有元件與 Data Flow。

## 投影片內容
上方：
```text
BAD
REQUEST → EDIT → HOPE
```
下方：
```text
GOOD
REQUEST → INSPECT → UNDERSTAND
```
中央大字：
```text
INSPECT BEFORE YOU EDIT.
```
繁中：**先檢查，再修改。**

## 視覺
兩條短流程。右側搭配 Repository File Tree 與放大鏡。任何檔案此時都保持未修改狀態。

## 煥哥
表情：專注調查。
動作：拿放大鏡查看 Repository。
角色：REPOSITORY INVESTIGATOR。

## 老師講稿
Coding Agent 很積極。你一說需求，它常常很想立刻 Edit。

但工程上我們希望它先回答：
- 哪些元件與需求有關？
- 哪些 Files 可能需要修改？
- 是否已有可重用的 Timestamp？
- 有哪些假設或風險？

給 Antigravity：
```text
請先 Inspect，不要修改任何檔案。
確認相關 Files、Data Flow、既有 Timestamp
以及可能的風險與假設。
```

注意「不要修改任何檔案」。Inspect 階段的產出是理解，不是 Code。

## 問
哪些是 Inspect？
- 搜尋 Timestamp 在哪裡處理 → ✓
- 新增 `time_helper.py` → ✕
- 找 Dashboard template → ✓
- 升級 FastAPI → ✕

## 核心句
> **INSPECT BEFORE YOU EDIT.**
> **REUSE BEFORE YOU ADD.**

## Transition
> Inspect 完後，我們知道可能要碰哪些地方。但仍然不要急著寫 Code。

下一頁：**PLAN BEFORE CODE。**

---

# Slide 15 — PLAN BEFORE CODE

## 目的
讓 AI Implementation Plan 成為第一個低成本、可以被 Human Review 的控制點。

## 投影片內容
中央流程：
```text
SPEC
 ↓
INSPECT
 ↓
PLAN  ← REVIEW HERE
 ↓
CODE
```
右側小 Plan Card：
```text
1. Reuse existing timestamp
2. Update dashboard
3. Minimal style change if needed
4. Verify existing weather display
```
底部：
```text
PLAN BEFORE CODE.
```

## 視覺
Plan 位於 Spec 與 Code 中間。Human 放大鏡停在 PLAN，而 Code 區域仍鎖住。

## 煥哥
表情：審慎。
動作：拿著 AI Plan，另一手示意 Code 暫停。
角色：PLAN REVIEWER。

## 老師講稿
AI 的 Output 不只有 Code。

我們可以要求 AI 先提出 Implementation Plan。

如果方向錯，現在改四行 Plan，成本非常低；如果讓 AI 先改完八個 Files 才發現方向錯，成本就高很多。

一個好 Plan 至少應該讓 Human 看懂：要做哪些步驟、預計改哪些 Files、為什麼，以及有沒有風險或假設。

## 問
Plan A：
```text
Reuse timestamp → update dashboard → verify
```
Plan B：
```text
Upgrade FastAPI → add package → rewrite service
→ redesign dashboard → add timestamp
```
哪個更符合目前 Spec？

預期：A。

## 核心句
> **PLAN BEFORE CODE.**
> **越早發現方向錯誤，修正成本越低。**

## Transition
> AI 提出 Plan，不代表 AI 自己可以核准 Plan。

下一頁：**HUMAN PLAN REVIEW。**

---

# Slide 16 — HUMAN PLAN REVIEW

## 目的
把 Human-in-the-loop 變成真正的工程 Gate：AI 提案，人類決定是否可以進入 Implementation。

## 投影片內容
中央：
```text
          AI PLAN
             ↓
        HUMAN REVIEW
             ↓
    ┌────────┼────────┐
    ↓        ↓        ↓
 APPROVE   REVISE   REJECT
 核准      修正      拒絕
```
底部巨大：
```text
AI PROPOSES. HUMAN DECIDES.
```
繁中：**AI 提案，人類決定。**

## 視覺
一個清楚的 Human Gate。AI Plan 在 Gate 左邊，Code 在 Gate 右邊；只有 APPROVE 才能通過。

## 煥哥
表情：嚴謹、負責。
動作：站在 Gate 前，手上三個按鈕 APPROVE / REVISE / REJECT。
角色：HUMAN GATEKEEPER。

## 老師講稿
Human Review 不是看 AI 的 Plan 漂不漂亮。

只抓四個問題：
```text
1. 符合 Spec 嗎？
2. 在 Scope 內嗎？
3. 每個修改都有必要嗎？
4. 有沒有不必要 Dependency / Refactor？
```

例如 AI 提案：
```text
Add Last Updated
+ Upgrade FastAPI
+ Replace CSS framework
+ Refactor weather service
```

這時不要因為 AI 解釋得很有道理就直接 APPROVE。

這些額外工作可能是 Scope Creep。

## 問
上面的 Plan 應該 APPROVE / REVISE / REJECT？

合理答案：至少 REVISE，要求回到 Spec 與最小必要 Scope；如果核心方向完全錯，也可 REJECT。

## 核心句
> **AI PROPOSES. HUMAN DECIDES.**
> **Human Review 是實作前的控制點，不是事後裝飾。**

## Transition
> Plan 核准了，AI 終於可以開始修改。但「可以改」不代表「想改多少就改多少」。

下一頁：**Minimal Change。**

---

# Slide 17 — IMPLEMENT THE MINIMAL CHANGE

## 目的
建立 Minimal Change 思維：Implementation 必須忠於 Spec 與已核准 Plan，而不是趁機重構整個 Project。

## 投影片內容
中央：
```text
SPEC ✓
PLAN ✓
HUMAN APPROVAL ✓
        ↓
MINIMAL IMPLEMENTATION
```
右側：
```text
NECESSARY ✓
SUFFICIENT ✓
UNRELATED ✕
```
底部：
```text
MINIMAL = NECESSARY + SUFFICIENT
```
繁中：**最小變更 = 必要，而且足以完成需求。**

## 視覺
一條窄而清楚的 Change Path 通往 `Last Updated ✓`。旁邊有一團巨大 Refactor Cloud 被紅叉擋住。

## 煥哥
表情：專注控制範圍。
動作：引導 AI 沿著核准的窄路實作，不讓它走向大型 Refactor。
角色：IMPLEMENTATION CONTROLLER。

## 老師講稿
Minimal 不代表偷工減料。

它的意思是：
> 該做的做完，不該做的不順便做。

可以給 AI：
```text
Plan 已核准。
請依照 OpenSpec Change 與核准的 Plan
進行最小必要實作。
不要擴大 Scope。
不要新增不必要 Dependency。
不要進行無關 Refactor。
```

例如：重用既有 Timestamp 合理；Dashboard 加顯示合理；必要的小幅 Style 合理。

但順便換 CSS Framework 或升級 FastAPI，除非 Spec/Plan 有充分理由，否則不是今天的工作。

## 問
「改越少」一定越好嗎？

預期答案：不是。Minimal 是 Necessary + Sufficient；如果少到 Requirement 沒完成，也不合格。

## 核心句
> **AI 的目標不是改最多，而是精確完成 Spec。**

## Transition
> 現在 AI 修改完了，而且很開心地告訴你：Done！

下一頁：**它說 Done，真的 Done 了嗎？**

---

# Slide 18 — AI 說 Done，真的 Done 了嗎？

## 目的
這是 L2 從 **BUILD → VERIFY** 最重要的觀念轉折。切斷把 AI 自我報告當成驗證結果的習慣。

## 投影片內容
左側巨大對話泡泡：
```text
AI:
"Done!
Everything works. ✓"
```
中央巨大：
```text
≠
```
右側：
```text
VERIFIED ?

□ Changed Files
□ Diff
□ Run / Test
□ Acceptance Criteria
```
底部：
```text
AI CLAIM ≠ VERIFIED EVIDENCE
```
繁中：**AI 的宣稱，不等於已驗證的證據。**

## 視覺
左邊是一個漂亮、自信、亮綠色的 `DONE ✓`。右邊是尚未打勾的 Evidence Checklist。中間用巨大 `≠` 隔開。

右側所有 Checkbox 此時都不能打勾。

## 煥哥
表情：從滿意轉成冷靜審查。
動作：左手指 AI 的 Done，右手拿 Evidence Checklist。
視線：不看 AI，而是看 Evidence。
角色：ENGINEERING REVIEWER。

## 老師講稿
現在 Antigravity 告訴你：
> Done! Everything works.

很多人在使用 AI Coding 時，到這裡就 Commit、Push、結束。

但我要問：它說 Done，誰說它真的 Done？

再問：剛才修改 Code 的是誰？學生：AI。

現在告訴你「我全部改好了」的又是誰？學生：還是 AI。

所以現在等於：
```text
AI 寫答案
+
AI 自己批改答案
+
AI 告訴你 100 分
```

這樣可以嗎？

這就是為什麼 `AI SUMMARY` 不能直接當 `VERIFICATION`。

## 問
如果 Antigravity 說：
> I implemented Last Updated successfully.

這算 Evidence 嗎？

預期答案：不算，這是 Claim。

再問：什麼比較像 Evidence？

學生可能回答：看程式、看 Diff、實際 Run、Test、看修改 Files。都可以接受。

老師整理成：
```text
Changed Files
Diff
Run / Test
Acceptance Criteria
```

## 板書
```text
CLAIM
  ↓
EVIDENCE
  ↓
HUMAN DECISION
```

## 核心句
> **BUILD CREATES THE CHANGE. VERIFY EARNS TRUST.**
> **BUILD 產生變更；VERIFY 建立信任。**

## Transition
> VERIFY 第一個問題不是重新問 AI：「Are you sure?」

而是自己看：
> **AI 到底改了哪些 Files？**

下一頁：**Slide 19 — What Files Did AI Change?**
