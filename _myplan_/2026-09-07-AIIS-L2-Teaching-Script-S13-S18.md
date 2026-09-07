# AIIS_L2 — 詳細教學講稿 S13–S18
## Part C — BUILD：讓 Antigravity 在 Spec 與 Human Control 下實作

狀態：PART C — CANONICAL zh-TW REFINEMENT — 2026-09-07
課程位置：L2 / MANAGE

前一段已完成：
```text
DEFINE ✓ → BUILD → VERIFY → REMEMBER
            ↑
          現在
```

> **本段不是教「怎麼叫 AI 多寫 Code」，而是教「怎麼控制 AI 寫 Code 的過程」。**

每頁只回答一個問題：
```text
S13 AI 開始工作前需要什麼 Context？
S14 AI 第一件事應該做什麼？
S15 為什麼 Code 前先看 Plan？
S16 誰決定 Plan 可以執行？
S17 核准後應該改多少？
S18 AI 說 Done，為什麼還沒 Done？
```

---

# Slide 13 — 把 Project + Spec 一起交給 AI
## Context Before Code

### 這頁在做什麼
改變學生使用 Coding Agent 的方式：不再只丟一句 Prompt，而是讓 AI 先取得既有 Project 與已定義的 Change Context。

### ON SLIDE
左：
```text
"Add Last Updated"
       ↓
      AI
       ↓
      ???
```

右：
```text
PROJECT
   +
SPEC
   ↓
  AI
```

底部：
> **CONTEXT BEFORE CODE.**
> **先建立正確脈絡，再要求寫程式。**

### 視覺
左右對比即可。不要在本頁塞完整 Inspect / Plan / Implement 流程。

### 煥哥角色
**AI Task Director（AI 任務指揮者）**，把 Project 與 Spec 兩張卡交給 Antigravity。

### 教師講稿
> Prompt 還是會用。但現在 Prompt 主要告訴 Agent「下一步做什麼」；Spec 則告訴它「這個 Change 是什麼」。

比較：
```text
方式 A
Add Last Updated.
```

```text
方式 B
請閱讀目前 Project 與 OpenSpec Change：
add-weather-last-updated。
先不要修改檔案。
```

問：
> 哪一個 Agent 比較知道現有系統與這次 Change 的邊界？

### 板書
```text
SPEC = defines the change
PROMPT = directs the next action
```

### 學生只需帶走
> **不要只 Prompt AI；要先讓 AI Ground 在 Project + Spec。**

### 銜接 S14
> AI 有 Context 之後，第一件事是開始改嗎？不是。

建議時間：6–8 分鐘。

---

# Slide 14 — INSPECT FIRST
## 先檢查，再修改

### 這頁在做什麼
建立 Agentic Coding 的基本操作習慣：修改前先閱讀 Repository 與既有 Data Flow。

### ON SLIDE
```text
BAD
REQUEST → EDIT → HOPE

GOOD
REQUEST → INSPECT → UNDERSTAND
```

底部：
> **INSPECT BEFORE YOU EDIT.**
> **先檢查，再修改。**

### 視覺
兩條很短的流程。右側可搭配 Repository file tree + 放大鏡。

### 煥哥角色
**Repository Investigator（專案調查者）**，拿放大鏡查看檔案樹。

### 教師講稿
給 Antigravity：
```text
請閱讀目前專案與 OpenSpec Change：
add-weather-last-updated。

先 Inspect，不要修改任何檔案。
請確認：
1. 哪些元件與需求有關？
2. 哪些檔案可能需要修改？
3. 是否已有可重用的時間資料？
4. 有哪些假設或風險？
```

教師強調：
> 「不要修改任何檔案」很重要。Coding Agent 很積極，我們現在只要它理解現況。

Weather Center 要 Inspect 的重點只口頭說：UI、Data Flow、既有 Timestamp、相關 Files、Dependencies。

### 第二記憶句
> **REUSE BEFORE YOU ADD.**
> **先重用，再新增。**

如果已有 timestamp，優先重用，不要先造 helper/package/service。

### 快速判斷
哪些是 Inspect？
- 搜尋 timestamp 在哪裡處理 → ✓
- 新增 `time_helper.py` → ✕
- 找 Dashboard template → ✓
- 升級 FastAPI → ✕

### 學生只需帶走
> **Inspect 階段的成果是理解，不是修改。**

### 銜接 S15
> Inspect 後知道可能要碰哪些地方，但仍然先不要 Code。我們先看 Plan。

建議時間：8–9 分鐘。

---

# Slide 15 — PLAN BEFORE CODE
## 先看計畫，再讓 AI 寫 Code

### 這頁在做什麼
讓 AI Plan 成為第一個低成本、可被 Human Review 的控制點。

### ON SLIDE
```text
SPEC
 ↓
INSPECT
 ↓
PLAN  ← REVIEW HERE
 ↓
CODE
```

右側只放一個最小 Plan：
```text
1. Reuse existing timestamp
2. Update dashboard
3. Minimal style change if needed
4. Verify existing weather display
```

底部：
> **PLAN BEFORE CODE.**

### 視覺
Plan 位於 Spec 與 Code 中間，Human 放大鏡停在 Plan 上。

### 煥哥角色
**Plan Reviewer（計畫審查者）**，先看 Plan，不先看 Code。

### 教師講稿
> AI 的 Output 不只有 Code。AI 也可以先提出 Implementation Plan。

> 如果方向錯，現在改四行 Plan，比 Code 寫完、八個檔案都被改過後再重做便宜得多。

好 Plan 至少讓人知道：
- 要做哪幾步；
- 預計改哪些檔案；
- 為什麼；
- 有哪些風險或假設。

### 比較活動
Plan A：
```text
Reuse timestamp → update dashboard → verify
```

Plan B：
```text
Upgrade FastAPI → add package → rewrite service
→ redesign dashboard → add timestamp
```

問：
> 哪一個更符合 Spec？

### 核心句
> **越早發現方向錯誤，修正成本越低。**

### 學生只需帶走
> Plan 讓 Human 可以在 Code 產生以前先審方向與 Scope。

### 銜接 S16
> AI 提出 Plan 之後，誰有權決定可以執行？

建議時間：8–9 分鐘。

---

# Slide 16 — HUMAN PLAN REVIEW
## AI 提案，人類決定

### 這頁在做什麼
把 Human-in-the-loop 變成真正的 Gate，而不是最後形式上的 Approve 按鈕。

### ON SLIDE
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

底部：
> **AI PROPOSES. HUMAN DECIDES.**
> **AI 提案，人類決定。**

### 視覺
一個明確 Gate。這頁不要同時塞六個 Review 問題與完整 Scope Creep 圖。

### 煥哥角色
**Human Gatekeeper（人工審查關卡）**。

### 教師講稿
Human Review 口頭只抓四題：
```text
1. 符合 Spec 嗎？
2. 在 Scope 內嗎？
3. 每個修改都有必要嗎？
4. 有沒有不必要 Dependency / Refactor？
```

再顯示故意錯誤 Plan：
```text
Add Last Updated
+ Upgrade FastAPI
+ Replace CSS framework
+ Refactor weather service
```

問學生：
> APPROVE / REVISE / REJECT？為什麼？

引出：
> **Scope Creep（範圍蔓延）** = 未經明確同意，Change 逐漸加入原本沒有要求的工作。

不需要在畫面再列一大串定義。

### Human-in-the-loop 真正意思
```text
AI → proposes
HUMAN → reviews intent + scope + risk
HUMAN → authorizes next step
```

### 學生只需帶走
> **Human Review 是實作前的控制點，不是事後裝飾。**

### 銜接 S17
> Plan 核准後，AI 終於可以修改。但是「可以改」不等於「想改多少就改多少」。

建議時間：8–10 分鐘。

---

# Slide 17 — IMPLEMENT THE MINIMAL CHANGE
## 只做完成需求所需的最小必要變更

### 這頁在做什麼
建立 Minimal Change 思維：核准後的 Implementation 應忠於 Spec 與 Plan，而不是趁機重構整個 Project。

### ON SLIDE
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
> **MINIMAL = NECESSARY + SUFFICIENT**
> **最小變更 = 必要，而且足以完成需求。**

### 視覺
一條窄而清楚的 Change Path；旁邊一個被叉掉的巨大 Refactor cloud。

### 煥哥角色
**Implementation Controller（實作控制者）**。

### 教師講稿
> Minimal 不代表偷工減料。它的意思是：該做的做完，不該做的不順便做。

給 AI 的執行指令可為：
```text
Plan 已核准。
請依照 OpenSpec Change 與核准的 Plan
進行最小必要實作。

不要擴大 Scope。
不要新增不必要 Dependency。
不要進行無關 Refactor。
```

### 判斷例
- 重用既有 timestamp → 合理
- Dashboard 加顯示 → 合理
- 必要的小幅 CSS → 合理
- 順便換 CSS framework → 不合理
- 順便升級 FastAPI → 不合理

### 板書
```text
SMALLER CHANGE
→ easier to review
→ easier to test
→ easier to explain
```

這裡只做工程直覺，不提前進 L4 安全掃描。

### 學生只需帶走
> **AI 實作的目標不是改最多，而是精確完成 Spec。**

### 銜接 S18
> AI 修改完後通常會說：「Done。」現在可以 Commit 了嗎？

建議時間：7–9 分鐘。

---

# Slide 18 — AI 說 Done，不代表已經驗證
## AI Summary Is Not Evidence

### 這頁在做什麼
切斷最危險的習慣：把 AI 的自我報告當成驗證結果。正式從 BUILD 轉進 VERIFY。

### ON SLIDE
左：
```text
AI:
"Done! Everything works."
```

中央：
```text
≠
```

右：
```text
VERIFIED EVIDENCE
Changed Files
Diff
Run / Test
Acceptance Criteria
```

底部：
> **AI CLAIM ≠ VERIFIED EVIDENCE**
> **AI 的宣稱，不等於已驗證的證據。**

### 視覺
聊天泡泡 vs Evidence cards。這頁不要教 Diff 細節，S19–S22 會逐頁教。

### 煥哥角色
**Evidence Reviewer（證據審查者）**，不被綠色 Done 勾勾說服，轉頭查看 Evidence。

### 教師講稿
> Coding Agent 很常在最後說：Implemented successfully、All good、Done。

問：
> 它說 Done，我們就可以 Commit 嗎？

> 不行。因為這是產生變更的同一個 Agent 對自己工作的描述，不是獨立驗證。

### 三層觀念
```text
CLAIM
AI 說它完成
 ↓
EVIDENCE
我們看到實際變更與測試
 ↓
DECISION
Human 決定是否接受
```

### 快問
哪個比較像 Evidence？
- AI 說「I fixed it」 → Claim
- Diff 顯示實際修改 → Evidence
- App 實際 Run → Evidence
- AI 說「No issues」 → Claim

### 核心句
> **BUILD CREATES THE CHANGE. VERIFY EARNS TRUST.**
> **BUILD 產生變更；VERIFY 建立信任。**

### Part C 收束
```text
PROJECT + SPEC
      ↓
INSPECT
      ↓
PLAN
      ↓
HUMAN REVIEW
      ↓
MINIMAL IMPLEMENTATION
      ↓
AI SAYS DONE
      ↓
NOT DONE YET
```

### 銜接 S19
> VERIFY 第一個問題很簡單：AI 到底改了哪些 Files？

下一頁：**S19 — Changed Files**

建議時間：7–9 分鐘。
