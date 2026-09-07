# AIIS_L2 — 詳細教學講稿 S24–S30
## Part E–F — REMEMBER × COMPLETE LAB × HANDOFF

狀態：L2 FINAL TEACHING SCRIPT COMPLETE — 2026-09-07
課程位置：L2 / MANAGE
語言：繁體中文為主；必要工程術語保留英文。

## 本段設計原則

每頁都必須足以支援實際授課，但**不把所有內容塞進投影片**。

採三層設計：
1. **ON SLIDE**：學生當下真正需要看的 3–5 個重點。
2. **TEACHER NOTES**：教師口頭補充、提問與案例。
3. **ACTIVITY / EVIDENCE**：需要學生操作時才加入。

> **高品質 ≠ 高密度。每一頁只承擔一個主要認知任務。**

前段已完成：
```text
DEFINE ✓ → BUILD ✓ → VERIFY ✓ → REMEMBER ← NOW
```

---

# Slide 24 — Software Needs Memory
## 軟體也需要記憶

### 本頁唯一任務
讓學生理解：驗證完成的 Change 如果沒有版本歷史，未來仍很難回答「改了什麼、為什麼改、哪個版本是好的」。

### ON SLIDE

左側：
```text
weather-final/
weather-final2/
weather-final-really-final/
weather-final-new/
```

右側：
```text
ENGINEERING MEMORY
What changed?
Why?
When?
Which version worked?
```

底部：
> **VERIFIED CHANGE NEEDS A MEMORY.**
> **驗證完成的變更，也需要留下記憶。**

### 視覺構圖
左側是凌亂資料夾堆；右側是一條乾淨的版本時間線。不要在本頁放 Git 指令。

### 煥哥角色
**PROJECT HISTORIAN（專案歷史管理者）**。看著 `final-final-v3` 一臉困惑，再轉向清楚的版本時間線。

### 教師講稿
> 假設今天 Last Updated 已經全部驗證 PASS。三個月後，網站突然壞掉。你還記得今天到底改了哪一版嗎？

> 很多人最自然的方法就是複製資料夾：final、final2、final-new。這其實是在人工製造一個很差的版本控制系統。

問：
> 如果我要知道「哪一次修改把系統弄壞」，這些資料夾名稱夠嗎？

### 板書
```text
WORKING NOW ≠ TRACEABLE LATER
```

### 常見誤解
「Git 只是備份工具。」

修正：Git 當然能幫助保存版本，但在本課更重要的是**保存工程變更歷史**。

### 本頁帶走
> 軟體工程不只要讓今天的版本能跑，也要讓未來的人能理解它怎麼變成今天這樣。

### 銜接
> 那怎麼把一個已經驗證完成的 Change 留成一個有名字的歷史節點？這就是 Commit。

建議時間：6–8 分鐘。

---

# Slide 25 — Commit = Named Checkpoint
## Commit：替一個已驗證的變更建立檢查點

### 本頁唯一任務
建立 Commit 的工程意義，不把本頁變成 Git 指令教學。

### ON SLIDE

```text
VERIFIED CHANGE
      ↓
    COMMIT
      ↓
NAMED CHECKPOINT
```

Bad：
```text
update
fix
new
```

Better：
```text
Add last-updated indicator to weather dashboard
```

底部：
> **COMMIT AFTER VERIFY.**
> **驗證後，再留下版本檢查點。**

### 視覺構圖
版本時間線：
```text
○ Initial Weather Center
│
● Add last-updated indicator
```
第二個節點標記 `VERIFIED ✓`。

### 煥哥角色
**CHECKPOINT KEEPER**，把「已驗證 Change」放到版本時間線上。

### 教師講稿
> Commit 可以先把它想成「有名字的工程檢查點」。

> 名字不是寫給 Git 看，是寫給未來的人看，包括未來的你自己。

比較：
```text
fix
```
和
```text
Add last-updated indicator to weather dashboard
```

問：
> 三個月後哪一個比較知道當時做了什麼？

### Traceability 輕量預告
```text
OpenSpec Change
      ↕
    Commit
      ↕
     Code
```

可在 commit message 或紀錄中引用：
```text
Implements: add-weather-last-updated
```

### 不要塞進本頁的內容
- branch internals
- merge strategy
- rebase
- Git object model
- 一整頁 command cheat sheet

這些都不是 L2 主線。

### 板書
```text
COMMIT = NAMED CHECKPOINT
```

### 本頁帶走
學生知道 Commit 的目的，是把一個有意義、已驗證的工程狀態保存成可理解的歷史節點。

### 銜接
> Commit 在我的電腦裡，那 GitHub 又是什麼？Git 和 GitHub 不是同一件事。

建議時間：7–8 分鐘。

---

# Slide 26 — Git ≠ GitHub
## Git 與 GitHub，不是同一件事

### 本頁唯一任務
用最簡單的模型消除學生最常見的混淆。

### ON SLIDE

```text
GIT
Local Version Control
本機版本歷史

        PUSH / SYNC →

GITHUB
Remote Shared Repository
遠端共享工程空間
```

大字：
> **Git ≠ GitHub**

### 視覺構圖
左：學生 Laptop + Git history。
右：GitHub repository + team/cloud icon。
中間只有一條 Push/Sync 箭頭。

### 煥哥角色
**CONNECTOR**，站在 Local 與 Remote 中間，把已驗證 Commit 推向共享 Repository。

### 教師講稿
> 很多人第一次學 Git，會把 Git 和 GitHub 當成同一個東西。

> 今天只要先記住：Git 管理你本機的版本歷史；GitHub 讓這些專案與歷史可以放到遠端、共享、查看與協作。

### 快問快答
- 沒網路，Git 還能不能 Commit？→ 可以。
- GitHub 掛掉，Git 就不存在嗎？→ 不是。
- Push 前的 Commit 是否已經存在本機？→ 是。

### 最小工作流
```text
CHANGE
 ↓
VERIFY
 ↓
COMMIT (Git)
 ↓
PUSH / SYNC
 ↓
GITHUB
```

### 本頁刻意不教
不在這裡塞 `clone/add/status/log/branch/merge/rebase` 全套指令。實際操作時只示範完成 Lab 所需最少步驟。

### 核心句
> **Git remembers locally. GitHub shares the history.**
> **Git 在本機保存歷史；GitHub 讓歷史可以共享與追蹤。**

### 銜接
> 當 Spec、Code、Commit 與驗證證據都逐漸留在同一個 Project 裡，GitHub 就不只是「放 Code 的地方」。

建議時間：6–8 分鐘。

---

# Slide 27 — GitHub = Engineering Memory
## GitHub：整個學期的工程記憶

### 本頁唯一任務
把 GitHub 放回 AIIS 整學期主線，讓學生看到 L2 的方法會被 L3–L16 重複使用。

### ON SLIDE

```text
SPEC
 +
CODE
 +
TEST / EVIDENCE
 +
HISTORY
      ↓
ENGINEERING MEMORY
```

下方只放一條學期線：
```text
L2 Feature
→ L4 Security Fix
→ L13 Verified Repair
→ L15–16 Final Evidence
```

### 視覺構圖
中央 GitHub Repository；四周只有四張卡：Spec / Code / Evidence / History。底部是一條學期成長時間線。

### 煥哥角色
**ENGINEERING MEMORY CURATOR**，把不同證據整理進同一個 Project history。

### 教師講稿
> 我不希望你們把 GitHub 理解成「交作業網站」。

> 到學期末，我們希望看到的不只是 Final Code，而是這個系統一路怎麼被 Build、Understand、Secure、Attack、Defend、Improve。

### Engineering Evidence Chain
逐步顯示，不要一次塞滿：
```text
REQUEST
→ SPEC
→ PLAN
→ CODE
→ TEST
→ ACCEPT
→ COMMIT
→ HISTORY
```

教師：
> 這就是為什麼 L2 很重要。它不是獨立的一堂 Git 課，而是在替後面所有 AI Security Engineering 建立「怎麼留下可信工程歷史」的方法。

### PREVIEW → TEACH → REUSE
只口頭說：
- L2 正式 TEACH OpenSpec workflow。
- L4 Security Fix 直接 REUSE。
- L13 Verified Repair 再 REUSE。
- Final Project 用整段 history 當 Evidence。

### 核心句
> **DON'T JUST SAVE CODE. SAVE THE ENGINEERING STORY.**
> **不要只保存程式碼，也要保存工程決策與證據。**

### 銜接
> 現在四層都齊了。接下來不再增加新觀念，直接讓你完整走一次。

建議時間：7–9 分鐘。

---

# Slide 28 — Student Mission
## 完整 Lab：Add Last Updated

### 本頁唯一任務
讓學生把 L2 全流程真正做一次。此頁是任務頁，不再講新理論。

### ON SLIDE

**MISSION**
> 在 L1 Weather Security Center 加入 `Last Updated`，但必須使用完整受控 Change Workflow。

四區：
```text
1 DEFINE
OpenSpec Change

2 BUILD
Inspect → Plan → Human Review → Implement

3 VERIFY
Files → Diff → Run/Test → AC → Decision

4 REMEMBER
Commit → GitHub
```

底部：
> **不是比誰最快改完，而是比誰能證明自己改對。**

### 視覺構圖
四站式 Mission Map，每站一個 icon；Weather Security Center 位於中央。不要把全部 Prompt 放在投影片上，Prompt 放講義/Lab Sheet。

### 煥哥角色
**MISSION COACH**，站在四站路線旁提醒學生不要跳關。

### 教師講稿
> 現在你們真的開始做。注意，這個 Lab 最常見的錯誤不是 Code 寫錯，而是學生直接跳過 DEFINE，跑去叫 AI 修改。

> 今天只要你跳過任何一站，你的工程 Evidence 就是不完整的。

### Lab 最小規格
**DEFINE**
- Change：`add-weather-last-updated`
- Need / Why
- Scope / Out of Scope
- Requirements
- Acceptance Criteria

**BUILD**
- AI 先 Inspect，不改檔案
- AI 提 Plan
- Human：Approve / Revise / Reject
- 才 Implement

**VERIFY**
- Changed Files
- Diff
- Run/Test
- AC Matrix
- Human Decision

**REMEMBER**
- Meaningful Commit
- Push / Sync GitHub

### 建議 Antigravity Prompt
```text
請閱讀目前專案與 OpenSpec Change：
add-weather-last-updated。

先 Inspect，不要修改任何檔案。

請提出完成此 Change 所需的最小 Implementation Plan，列出：
1. 預計修改的檔案；
2. 每個修改的理由；
3. 主要假設；
4. 可能風險。

請維持在 Spec Scope 內。
```

### 教師巡堂重點
不要先幫學生 Debug Code；先檢查：
1. 有沒有 Spec？
2. AI 是否先 Inspect？
3. Plan 有沒有經 Human Review？
4. 是否出現 Scope Creep？

### 建議時間
25–40 分鐘，依課程總時數調整。

### 銜接
> 做完不是結束。你要把「我是怎麼知道它做對的」整理成 Evidence Package。

---

# Slide 29 — Evidence Package
## 不只交成果，也交「為什麼可信」

### 本頁唯一任務
定義學生最後要保存的證據，不把作業變成大量文書。

### ON SLIDE

**8 個 Evidence Items**
```text
E1 Request
E2 Spec
E3 AI Plan
E4 Human Review
E5 Diff
E6 Test
E7 AC Verification
E8 Git History
```

中央箭頭：
```text
WHY → CHANGE → EVIDENCE → TRUST
```

底部：
> **Evidence is part of engineering.**
> **證據不是事後補文件，而是工程的一部分。**

### 視覺構圖
8 張小卡即可，每張只放名稱，不塞說明。教師口頭解釋。

### 煥哥角色
**EVIDENCE CURATOR**，把 8 張證據卡整理成一個簡潔 Portfolio。

### 教師講稿
> 我不要你們寫一份二十頁報告。我要的是最少但足以回答工程問題的 Evidence。

逐一快速說：
- E1：原始需求是什麼？
- E2：最後定義的 Change 是什麼？
- E3：AI 原本打算怎麼做？
- E4：人類有沒有審 Plan？
- E5：實際改了什麼？
- E6：真的跑過嗎？
- E7：每個 AC 是否通過？
- E8：最後版本在哪裡？

### 建議評量
```text
OpenSpec Change              20%
Scope + Acceptance Criteria  15%
AI Plan + Human Review       15%
Diff Review                  15%
Run / Test                   10%
AC Verification              10%
Git / GitHub History         10%
Reflection                    5%
```

### Reflection 只問一題
> **這次如果沒有 Spec，你認為 AI 最可能做出哪一種不必要變更？**

避免增加大量心得文。

### 核心句
> **NO EVIDENCE, NO TRUST.**
> **沒有證據，就不能只靠宣稱建立信任。**

### 銜接
> L2 到這裡已經完成。但下一堂我們會遇到一個新的問題：你可以 Review Change，卻不一定真正看懂 Code 為什麼這樣跑。

建議時間：8–10 分鐘。

---

# Slide 30 — From MANAGE to UNDERSTAND
## 我們會管理 AI 的 Change 了；下一步，要真正看懂它

### 本頁唯一任務
收束 L2 並自然交棒 L3，不在結尾加入新工具。

### ON SLIDE

上半部：
```text
L1 — BUILD
Prompt → AI → Working Software

L2 — MANAGE
Request → Spec → Plan → Implement
→ Verify → Commit → History
```

下半部大問題：
> **But do you understand HOW the code actually works?**
> **但是，你真的知道這些 Code 是怎麼運作的嗎？**

下一站：
```text
L3 — UNDERSTAND
Python → HTTP → API → JSON → FastAPI → Web App
```

### 視覺構圖
樓梯式：
```text
L4 SECURE IT
      ↑
L3 UNDERSTAND IT ← NEXT
      ↑
L2 MANAGE IT ✓
      ↑
L1 BUILD IT ✓
```

### 煥哥角色
**GUIDE**。背後是已完成的 Weather Security Center 與 GitHub history；前方打開程式碼與 API data-flow 地圖。

### 教師收尾講稿
> L1 我們學會一件很震撼的事：即使還沒有完全掌握所有技術細節，AI 也能協助我們 Build 一個真的可以跑的系統。

> L2 我們補上第二個能力：不能只是一直 Prompt、一直改。我們需要 Spec、Plan、Human Review、Evidence 和 History，才能管理 AI 產生的 Change。

停一下，再問：

> 可是如果我現在打開 `main.py`，你知道每一段在做什麼嗎？
>
> Browser 按下 Refresh 後，Request 去哪裡？FastAPI 做什麼？CWA API 回來的是什麼？JSON 又怎麼變成畫面？

> 這就是 L3。

### L2 四層最後回顧
```text
DEFINE    OpenSpec
BUILD     Antigravity
VERIFY    Diff + Test + AC + Human
REMEMBER  Git + GitHub
```

全班最後念一次：
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
>
> **規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。**

### Exit Ticket
只問三題：
1. Prompt 和 Spec 最大差別是什麼？
2. AI 說 Done 為什麼還不能直接 Accept？
3. Git 在這個 Workflow 裡負責什麼？

### L3 預告圖
```text
Browser
  ↓ HTTP Request
FastAPI Route
  ↓
Python
  ↓
CWA API
  ↓ JSON
Python
  ↓ HTTP Response
Browser
```

只 Preview，不在 L2 解釋。

### 最後一句
> **L1：讓 AI 幫我們做出來。**
>
> **L2：學會管理 AI 做出的改變。**
>
> **L3：開始真正看懂這個系統。**

建議時間：8–10 分鐘。

---

# AIIS_L2 完整教學故事完成

```text
S00  Lesson Positioning

S01–S06
WHY MANAGE?
Vibe Coding → Prompt vs Spec → OpenSpec → Four Layers

S07–S12
DEFINE
Request → Change → Why → Scope → Requirements → AC

S13–S18
BUILD
Project + Spec → Inspect → Plan → Human Review → Minimal Implement

S19–S23
VERIFY
Changed Files → Diff → Run/Test → AC → Human Decision

S24–S27
REMEMBER
Software Memory → Commit → Git vs GitHub → Engineering Memory

S28–S29
COMPLETE LAB
Mission → Evidence Package

S30
HANDOFF
MANAGE → UNDERSTAND
```

## L2 最終核心模型

```text
REQUEST
   ↓
DEFINE — OpenSpec
   ↓
BUILD — Antigravity
   ↓
VERIFY — Diff + Test + AC + Human Review
   ↓
REMEMBER — Git + GitHub
```

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

## 範圍檢查
L2 到此停止，不擴張：
- Python / FastAPI / HTTP / API / JSON 細節 → L3
- Semgrep / Security Scan → L4
- ML → L5–L7
- DL → L9–L10
- Red Team → L11–L12
- Blue Team → L13
- ISO 27001 / Risk → L14
- Final Demo → L15–L16

因此 L2 維持單一任務：

> **MANAGE AI-GENERATED CHANGE.**
> **管理 AI 產生的工程變更。**
