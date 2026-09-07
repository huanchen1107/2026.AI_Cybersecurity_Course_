# AIIS_L2 — 詳細教學講稿 S24–S30
## Part E–F — REMEMBER × COMPLETE LAB × HANDOFF

狀態：L2 FINAL TEACHING SCRIPT — CANONICAL zh-TW REFINEMENT — 2026-09-07
課程位置：L2 / MANAGE
語言：繁體中文為主；必要工程術語保留英文。

前面已完成：
```text
DEFINE ✓ → BUILD ✓ → VERIFY ✓ → REMEMBER
                               ↑
                             現在
```

> **本段不是 Git 指令課。**
> Git / GitHub 在 L2 的角色只有一個：**把已驗證的 Change 保存成可追蹤的工程記憶。**

每頁只回答一個問題：
```text
S24 為什麼已驗證的 Change 還需要 Memory？
S25 Commit 到底代表什麼？
S26 Git 與 GitHub 有什麼不同？
S27 為什麼 GitHub 不只是放 Code？
S28 學生如何完整做一次？
S29 要留下哪些最小 Evidence？
S30 L2 完成後，下一個問題是什麼？
```

---

# Slide 24 — 軟體也需要記憶
## Software Needs Memory

### 這頁在做什麼
讓學生理解：今天能 Run、今天驗證通過，仍不代表未來能知道「為什麼這樣改」與「哪個版本是對的」。

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
> **已驗證的變更，也需要被記住。**

### 視覺
左側是混亂資料夾；右側是一條乾淨的版本時間線。

### 煥哥角色
**History Keeper（歷史保存者）**，從一堆 final folders 走向清楚的版本歷史。

### 教師講稿
> 很多人第一次做 Project 都會有 `final`、`final2`、`really-final`。問題不是檔名醜，而是你不知道：哪次改了什麼？為什麼？哪一版真的驗證過？

板書：
```text
WORKING NOW ≠ TRACEABLE LATER
```

> Git 的核心價值，不只是備份，而是保存 Change History。

### 學生只需帶走
> **驗證完成只是「現在可信」；版本歷史讓它「未來可追蹤」。**

### 銜接 S25
> 那要怎麼在歷史裡留下「這次驗證過的 Change」？先認識 Commit。

建議時間：6–7 分鐘。

---

# Slide 25 — Commit = 有名字的工程檢查點
## Named Checkpoint

### 這頁在做什麼
讓學生理解 Commit 的工程意義，不開始背 Git commands。

### ON SLIDE
```text
VERIFIED CHANGE
       ↓
     COMMIT
       ↓
NAMED CHECKPOINT
```

下面只比較兩種訊息：
```text
BAD
update
fix
new

BETTER
Add last-updated indicator to weather dashboard
```

底部：
> **COMMIT AFTER VERIFY.**
> **驗證後，再形成 Commit。**

### 視覺
一條時間線上放一個清楚的 checkpoint。

### 煥哥角色
**Checkpoint Owner（檢查點負責人）**。

### 教師講稿
> Commit 可以先把它想成「一個有名字的版本檢查點」。

> 它最好能回答：這次 Change 做了什麼？

連回本課案例：
```text
OpenSpec Change
add-weather-last-updated
        ↕
Commit
Add last-updated indicator to weather dashboard
```

提醒：
> 我們今天不是教 Git object model，也不是 branch / merge / rebase 課。

### 學生只需帶走
> **Commit 應該代表一個已經過驗證、可以說得清楚的 Change。**

### 銜接 S26
> Commit 在哪裡？這就要先分清楚 Git 與 GitHub。

建議時間：6–7 分鐘。

---

# Slide 26 — Git ≠ GitHub
## 一個在本機管理版本，一個讓歷史能被遠端共享

### 這頁在做什麼
一次解決學生最常見的混淆，不延伸成 Git 操作大全。

### ON SLIDE
```text
GIT
Local Version Control
本機版本歷史
        ↓
   PUSH / SYNC
        ↓
GITHUB
Remote Shared Repository
遠端共享工程空間
```

底部：
> **Git remembers locally. GitHub shares the history.**
> **Git 在本機保存版本；GitHub 讓工程歷史可以共享。**

### 視覺
左邊 Laptop，右邊 GitHub cloud，中間一個 Push/Sync 箭頭。

### 煥哥角色
**System Explainer（系統解說者）**，一手指本機，一手指遠端 Repository。

### 教師講稿
快速問三題：
> 沒網路可以 Git commit 嗎？→ 可以。
>
> GitHub 暫時不能連，Git 歷史就消失嗎？→ 不會。
>
> Push 前 Commit 可以先存在本機嗎？→ 可以。

今天只記：
```text
CHANGE
 ↓
VERIFY
 ↓
COMMIT   ← Git
 ↓
PUSH / SYNC
 ↓
GITHUB
```

### 本頁刻意不教
- branch
- merge
- rebase
- cherry-pick
- Git internals
- 大量 command cheat sheet

### 學生只需帶走
> **Git 與 GitHub 有關，但不是同一個東西。**

### 銜接 S27
> 如果 GitHub 不只是「放 Code 的地方」，那它在 AIIS 整學期扮演什麼角色？

建議時間：6–8 分鐘。

---

# Slide 27 — GitHub = Engineering Memory
## 不只保存 Code，也保存工程故事

### 這頁在做什麼
把 GitHub 放進整個 AIIS 學期主線：它是 Spec、Code、Evidence、History 的持續工程記憶。

### ON SLIDE
```text
SPEC
 +
CODE
 +
EVIDENCE
 +
HISTORY
   ↓
ENGINEERING MEMORY
```

下方小型學期線：
```text
L2 Feature Change
   ↓
L4 Security Fix
   ↓
L13 Verified Repair
   ↓
L15–16 Final Evidence
```

底部：
> **DON'T JUST SAVE CODE. SAVE THE ENGINEERING STORY.**
> **不要只保存程式碼，也要保存工程故事。**

### 視覺
一個 GitHub Repository 內有四層：Spec / Code / Evidence / History。

### 煥哥角色
**Engineering Archivist（工程記憶管理者）**。

### 教師講稿
> 如果 GitHub 裡只有最後版本 Code，我們只知道「現在長什麼樣」。

> 如果裡面還有 Change、Commit、驗證證據，我們就能回答「為什麼變成這樣」。

完整工程故事：
```text
REQUEST
 ↓
SPEC
 ↓
PLAN
 ↓
CODE
 ↓
TEST / EVIDENCE
 ↓
HUMAN ACCEPT
 ↓
COMMIT / HISTORY
```

這條線不必全部顯示在投影片，可逐步揭露或口頭回顧。

### 學生只需帶走
> **GitHub 是本學期的 Engineering Memory，不只是 Code Storage。**

### 銜接 S28
> 四層都學完了。現在不再教新概念，學生自己完整走一次。

建議時間：7–8 分鐘。

---

# Slide 28 — Student Mission
## 完整做一次 Controlled Change

### 這頁在做什麼
把 S07–S27 的方法真正做一次。這是 L2 最重要的實作頁，不新增理論。

### ON SLIDE
四個大站：
```text
① DEFINE
OpenSpec Change

② BUILD
Inspect → Plan → Human Review → Implement

③ VERIFY
Files → Diff → Run/Test → AC → Decision

④ REMEMBER
Commit → GitHub
```

中央：
```text
MISSION
add-weather-last-updated
```

底部：
> **不是比誰最快改完，而是比誰能證明自己改對。**

### 視覺
像四站式 Mission Map。學生現在只需要看流程，不要再看理論文字。

### 煥哥角色
**Mission Commander（任務指揮者）**，把任務交給學生。

### 學生實作 Prompt
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

### 教師巡堂只看四件事
1. 是否先有 Spec？
2. AI 是否先 Inspect？
3. Student 是否真的 Review Plan？
4. 有沒有 Scope Creep？

### Lab 建議節奏
```text
5–8 min   DEFINE review
5–8 min   INSPECT + PLAN
3–5 min   HUMAN PLAN REVIEW
8–12 min  IMPLEMENT
8–12 min  VERIFY
3–5 min   COMMIT / GITHUB
```

可依課堂長度壓縮，但不要犧牲 VERIFY。

### 學生只需帶走
> **AI 做得快不是重點；能控制、驗證、留下證據才是工程能力。**

建議時間：25–40 分鐘。

---

# Slide 29 — Evidence Package
## 不交厚報告，只交最小可驗證證據

### 這頁在做什麼
定義 Lab 最小交付物。目標是養成 Evidence Habit，而不是增加文書負擔。

### ON SLIDE
八張 Evidence Card：
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

底部：
> **WHY → CHANGE → EVIDENCE → TRUST**

### 視覺
八張小卡，依流程排成兩列，不放評分細節。

### 煥哥角色
**Evidence Collector（證據整理者）**。

### 教師講稿
> Evidence 不等於寫十頁報告。它只是讓另一個人可以理解：你為什麼改、AI 怎麼提案、你怎麼審、最後憑什麼接受。

建議評量：
```text
OpenSpec Change                  20%
Scope + Acceptance Criteria      15%
AI Plan + Human Review           15%
Diff Review                      15%
Run / Test                       10%
AC Verification                  10%
Git / GitHub History             10%
Reflection                        5%
```

### Reflection 只問一題
> 如果沒有 Spec，AI 在這次 Last Updated Change 中最可能做出哪一種不必要修改？

### 核心句
> **NO EVIDENCE, NO TRUST.**
> **沒有證據，就沒有足夠理由相信。**

### 學生只需帶走
> **Evidence 是工程工作的一部分，不是事後補作業。**

### 銜接 S30
> 現在我們會管理 Change 了。但還有一個更根本的問題。

建議時間：8–10 分鐘。

---

# Slide 30 — From MANAGE to UNDERSTAND
## 我們會管理改變了，但真的看懂系統嗎？

### 這頁在做什麼
收束 L2，明確交棒 L3。不要再加入任何新工具。

### ON SLIDE
上半：
```text
L1 — BUILD
Prompt → AI → Working Software

L2 — MANAGE
Request → Spec → Plan → Implement
→ Verify → Commit → History
```

中央大問題：
> **But do you understand HOW the code actually works?**
> **但是，你真的知道這套系統怎麼運作嗎？**

下半：
```text
L3 — UNDERSTAND
Python → HTTP → API → JSON → FastAPI → Web App
```

底部：
```text
L1 BUILD IT
    ↓
L2 MANAGE IT ✓
    ↓
L3 UNDERSTAND IT ← NEXT
    ↓
L4 SECURE IT
```

### 視覺
一座四階樓梯。L2 亮起 ✓，L3 標記 NEXT。

### 煥哥角色
**Course Guide（課程引導者）**，站在 L2 與 L3 階梯之間。

### 教師講稿
> L2 到這裡，我們已經可以回答：WHY、WHAT、Scope、Done、What Changed、Evidence、History。

> 但如果我打開 `main.py`，你看得懂嗎？如果 Browser 發 Request 到 FastAPI，你知道資料怎麼走嗎？如果 CWA API 回 JSON，你知道 Python 怎麼處理嗎？

只做 L3 Preview：
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

不要在本頁正式解釋 HTTP status code、route syntax 或 JSON parsing，這些留給 L3。

### L2 四層最後回顧
```text
DEFINE   — OpenSpec
BUILD    — Antigravity
VERIFY   — Diff + Test + AC + Human
REMEMBER — Git + GitHub
```

### Exit Ticket
1. Prompt 與 Spec 最大差別是什麼？
2. 為什麼 AI 說 Done 不能直接接受？
3. Git 在這個 Workflow 裡負責什麼？

### 最後三句
> **L1：讓 AI 幫我們做出來。**
>
> **L2：學會管理 AI 做出的改變。**
>
> **L3：開始真正看懂這個系統。**

建議時間：8–10 分鐘。

---

# L2 最終教學故事

```text
S00      從 BUILD 進入 MANAGE

S01–06   為什麼需要管理 AI Change？
           ↓
S07–12   DEFINE
           ↓
S13–18   BUILD
           ↓
S19–23   VERIFY
           ↓
S24–27   REMEMBER
           ↓
S28      COMPLETE LAB
           ↓
S29      EVIDENCE PACKAGE
           ↓
S30      → L3 UNDERSTAND
```

# L2 兩張核心 Anchor Diagram

## Anchor A — 整堂課
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

## Anchor B — VERIFY 五步
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

# 最終範圍防呆
L2 不再增加 Mandatory Topic：
- 不擴充成 Git command 課。
- 不教 branch / merge / rebase。
- 不深入 Python / FastAPI / HTTP / JSON，留給 L3。
- 不進行 Semgrep 掃描，留給 L4。
- 不建立第二個 App。
- 不新增第二個 Mandatory AI Coding Tool。

> **高品質 ≠ 高密度。**
> **詳細的是教學設計；簡潔的是學生看到的畫面。**
