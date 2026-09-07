# AIIS_L2 — 逐頁詳細教學稿 S24–S30
## Part E–F — REMEMBER × COMPLETE LAB × HANDOFF

狀態：CANONICAL — L1 STYLE — 2026-09-07

統一格式：**目的 → 投影片內容 → 視覺 → 煥哥 → 老師講稿 → 問答 → 核心句 → Transition**。

---

# Slide 24 — Software Needs Memory

## 目的
從 VERIFY 進入 REMEMBER。讓學生理解：一個已驗證的 Change，如果沒有留下可追溯歷史，仍然不是完整的工程流程。

## 投影片內容
左側：
```text
TODAY
Verified Change ✓
```
右側：
```text
NEXT WEEK
Why did we change this?
Who approved it?
What was tested?
Which version worked?
```
中央：
```text
?
```
底部巨大：
```text
VERIFIED CHANGE NEEDS A MEMORY.
```
繁中：**已驗證的變更，也需要工程記憶。**

## 視覺
左邊是一個今天清楚完整的 Change；經過時間軸到右邊後，資訊逐漸模糊。可用 `final.py / final2.py / final_really_final.py` 作為小型反例，但不要搶主畫面。

## 煥哥
表情：回想但找不到答案。
動作：站在一堆 `final_v2` 檔案前，手上拿著問號。
角色：FUTURE MAINTAINER。

## 老師講稿
假設今天所有 Acceptance Criteria 都 PASS，Human 也 ACCEPT。

今天大家都記得發生什麼。

但一個月後呢？

你可能只剩：
```text
weather-final
weather-final2
weather-final-ok
weather-final-really-ok
```

這些 File Name 沒辦法回答：為什麼改？當時驗證了什麼？哪個版本是核准的？

所以軟體工程除了要有 Working State，也需要 History。

## 問
如果程式現在能 Run，為什麼還要保存 History？

預期：未來追蹤、回復、交接、理解 Change、證明曾做過哪些驗證。

## 核心句
> **WORKING NOW ≠ TRACEABLE LATER.**
> **今天能運作，不代表未來可追溯。**

## Transition
> 那怎麼替一個已驗證的 Change 留下一個清楚的時間點？

下一頁：**Commit = Named Checkpoint。**

---

# Slide 25 — COMMIT = Named Checkpoint

## 目的
讓學生用工程概念理解 Commit，而不是把 Git 教成指令背誦課。

## 投影片內容
中央：
```text
VERIFIED CHANGE
      ↓
    COMMIT
      ↓
NAMED CHECKPOINT
```
下方範例：
```text
Add Last Updated indicator to weather dashboard
```
底部：
```text
COMMIT AFTER VERIFY.
```
繁中：**驗證之後，再建立有名稱的工程檢查點。**

## 視覺
一條 Project Timeline，在某一點插上一面旗子：`Last Updated ✓`。旗子旁顯示簡潔 Commit Message。

## 煥哥
表情：確認、保存。
動作：把 Verified Change 固定成 Timeline 上的一個 Checkpoint。
角色：VERSION HISTORIAN。

## 老師講稿
Commit 可以先把它想成：
> 一個有名字的工程檢查點。

不是「我今天按了幾次 Save」。

我們希望它代表一個有意義、已經 Review 與 Verify 的狀態。

例如：
```text
Add Last Updated indicator to weather dashboard
```

比：
```text
update
fix
final
123
```
更能告訴未來的你發生了什麼。

今天不需要背完整 Git Command。L2 要理解的是 Commit 在工程流程中的位置。

## 問
應該在 AI 一改完就 Commit，還是 Verify 後再 Commit？

預期：Verify 後。

## 核心句
> **A COMMIT IS A NAMED ENGINEERING CHECKPOINT.**
> **Commit 是有意義的工程檢查點，不只是存檔。**

## Transition
> Commit 講到這裡，學生最容易混淆的兩個名詞就出現了：Git 和 GitHub。

下一頁：**Git ≠ GitHub。**

---

# Slide 26 — Git ≠ GitHub

## 目的
用最少資訊建立正確心智模型，不把 L2 變成 Git 指令課。

## 投影片內容
左側：
```text
GIT
Local Version Control

✓ Track changes
✓ Commit checkpoints
✓ History
```
右側：
```text
GITHUB
Remote Shared Repository

✓ Share
✓ Sync
✓ Collaborate
✓ Preserve remote history
```
中央巨大：
```text
GIT ≠ GITHUB
```
底部：
```text
LOCAL HISTORY ↔ SHARED HISTORY
```

## 視覺
左側是一台 Laptop，裡面有 Git Timeline；右側是 GitHub Repository。兩者用雙向箭頭連接。避免 Terminal 滿版。

## 煥哥
表情：清楚解釋差異。
動作：左右各指 Git 與 GitHub。
角色：ENGINEERING GUIDE。

## 老師講稿
Git 和 GitHub 很常一起出現，所以初學者容易以為它們是一樣的。

今天只記兩件事：
```text
Git    → Local Version Control
GitHub → Remote Shared Repository
```

Git 管理本機版本歷史；GitHub 讓 Repository 可以被遠端保存、分享與協作。

我們不需要在這頁教十個 Command。學生只要知道流程概念：
```text
VERIFY → COMMIT → SYNC / PUSH → GITHUB
```

## 問
沒有 GitHub，Git 能不能在本機做 Version Control？

預期答案：可以。

沒有 Git，只把 File 上傳 GitHub，是否等於理解完整 Version Control Workflow？

預期：不等於。

## 核心句
> **GIT TRACKS HISTORY. GITHUB SHARES HISTORY.**
> **Git 管版本；GitHub 讓工程歷史可共享。**

## Transition
> 那為什麼我們這堂 AI 課一定要 GitHub？因為我們要保存的不只是 Code。

下一頁：**Engineering Memory。**

---

# Slide 27 — GitHub = Engineering Memory

## 目的
把 GitHub 從「放程式的網站」提升成 AIIS 整學期的 Engineering Memory。

## 投影片內容
中央 Repository：
```text
GITHUB REPOSITORY
```
四條輸入：
```text
SPEC
CODE
TEST / EVIDENCE
HISTORY
```
合成：
```text
ENGINEERING STORY
```
底部：
```text
DON'T JUST SAVE CODE.
SAVE THE ENGINEERING STORY.
```
繁中：**不要只保存程式；保存工程故事。**

## 視覺
GitHub Repo 像一個 Engineering Memory Vault。四張卡 Spec / Code / Evidence / History 被放進去。旁邊有 Semester Timeline：L2 → L4 → L13 → Final。

## 煥哥
表情：從單次任務轉成長期專案視角。
動作：把 Change Evidence 放入 GitHub Vault。
角色：PROJECT MEMORY KEEPER。

## 老師講稿
如果 GitHub 只保存 Code，我們會失去很多重要資訊。

AIIS 希望最後能回答：
- 這個功能為什麼存在？
- 哪個 Change 加進來？
- AI 提了什麼 Plan？
- Human 怎麼 Review？
- Test 有沒有通過？
- Security Finding 後來怎麼修？

所以我們保存的是：
```text
SPEC + CODE + EVIDENCE + HISTORY
```

這套方法後面還會重複使用。

L4 發現 Security Finding，可以變成新的 OpenSpec Change。

L13 修補 Red-Team Finding，也要留下 Fix、Regression Test 與 Evidence。

最後期末展示不是只有一個網站，而是一整條 Engineering Story。

## 問
如果兩組最後網站看起來一樣，但 A 組只有 Final Code，B 組有 Spec、History、Tests、Evidence，哪一組更像 Engineering Project？

預期：B。

## 核心句
> **DON'T JUST SAVE CODE. SAVE THE ENGINEERING STORY.**

## Transition
> 四個 Layer 都學完了。現在不要再看老師做，我們自己完整走一次。

下一頁：**Student Mission。**

---

# Slide 28 — STUDENT MISSION：完整走一次

## 目的
L2 最重要的 Hands-on Integration。學生使用同一個 Weather Security Center 與同一個 Change，完整走一次 DEFINE → BUILD → VERIFY → REMEMBER。

## 投影片內容
中央四站：
```text
① DEFINE
OpenSpec Change

② BUILD
Antigravity

③ VERIFY
Diff + Run/Test + AC

④ REMEMBER
Commit + GitHub
```
上方 Mission：
```text
add-weather-last-updated
```
底部巨大：
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

## 視覺
四個大型 Station，學生 Avatar 從左走到右。每站完成後取得一個 Evidence Token。最後四個 Token 合成 `VERIFIED CHANGE ✓`。

## 煥哥
表情：教練模式。
動作：站在流程旁，不替學生操作，只指引下一站。
角色：ENGINEERING COACH。

## 老師講稿
現在開始今天真正的 Lab。

不是另外做一個新 Demo，也不是重新建立一個 App。

就是使用 L1 的 Weather Security Center，完成今天唯一的 Change：
```text
add-weather-last-updated
```

學生任務：
```text
DEFINE
→ Review OpenSpec Change
→ WHY / Scope / Requirements / AC

BUILD
→ Ask Antigravity to inspect
→ Review AI Plan
→ Approve / Revise
→ Implement minimal change

VERIFY
→ Changed Files
→ Diff
→ Run / Test
→ Check every AC
→ Human decision

REMEMBER
→ Commit
→ Sync GitHub
```

建議實作時間 25–40 分鐘。老師巡堂時不要只問「做完了嗎」，而是問「你現在在哪一層？你的 Evidence 是什麼？」

### 建議 Antigravity Prompt
```text
請閱讀目前 Weather Security Center Repository
與 OpenSpec Change: add-weather-last-updated。

先不要修改任何檔案。
先 Inspect 相關程式與資料流，提出最小實作 Plan，
列出預計修改的 Files、理由、風險與驗證方式。
等待 Human Review 後再進行實作。
```

## 問
老師巡堂固定問：
1. 你的 Spec 在哪裡？
2. AI 的 Plan 是什麼？
3. 你核准了什麼？
4. 你的 Diff 看過了嗎？
5. 哪個 Evidence 證明 AC PASS？

## 核心句
> **DO THE WHOLE LOOP, NOT JUST THE CODE.**
> **完成整個工程閉環，不只是把 Code 寫出來。**

## Transition
> Lab 做完後，不是舉手說「老師，我完成了」。

下一頁：**Show me the Evidence。**

---

# Slide 29 — EVIDENCE PACKAGE：怎麼證明你真的完成？

## 目的
把 L2 學習成果從「作品」提升為「可驗證工程證據」。同時為後續 L4、L13、期末專題建立共同 Evidence Culture。

## 投影片內容
中央 Evidence Folder：
```text
L2 EVIDENCE PACKAGE
```
周圍八張卡：
```text
1 REQUEST
2 SPEC
3 AI PLAN
4 HUMAN REVIEW
5 DIFF
6 TEST
7 AC VERIFICATION
8 GIT HISTORY
```
底部巨大：
```text
NO EVIDENCE, NO TRUST.
```
繁中：**沒有證據，就沒有足夠的工程信任。**

## 視覺
八張 Evidence Cards 收進同一個資料夾。不要把完整 14 項 Rubric 全擠到投影片；詳細評分留在 Teacher Notes / LMS。

## 煥哥
表情：像 Reviewer 收件。
動作：檢查 Evidence Folder，而不是只看漂亮 UI。
角色：EVIDENCE REVIEWER。

## 老師講稿
如果學生只交一張「Last Updated 已經出現」的 Screenshot，我只能知道結果看起來存在。

但我不知道：
- Requirement 是什麼？
- AI 有沒有亂改 Scope？
- Human 有沒有 Review？
- Test 有沒有做？
- AC 是否真的逐條驗證？

所以 L2 的成果不是一張 Screenshot，而是一個 Evidence Package。

老師可以依課堂時間要求學生提交其中核心證據；完整版本可保存：Original Request、OpenSpec Change、Need、Scope、AC、AI Plan、Human Review、Changed Files、Diff、Run/Test、AC Verification、Human Decision、Commit Message、GitHub History。

## 問
如果畫面成功，但沒有 Diff、Test、AC Evidence，可以給「工程流程完整」嗎？

預期答案：不行。

## 核心句
> **NO EVIDENCE, NO TRUST.**
> **工程品質不只要做出來，也要能證明。**

## Transition
> 現在我們知道 WHY、WHAT、DONE、EVIDENCE、HISTORY。

但還有一個問題我們刻意沒有深入回答：
> **這個 Weather Security Center 到底是怎麼運作的？**

下一頁：**From MANAGE to UNDERSTAND。**

---

# Slide 30 — From MANAGE to UNDERSTAND

## 目的
收束 L2 並精準交棒 L3。讓學生知道 L2 已解決哪些問題，以及下一課為什麼必須理解 Python / FastAPI / HTTP / API / JSON / Frontend ↔ Backend Data Flow。

## 投影片內容
左側完成：
```text
L1 — BUILD ✓
Can we make it work?

L2 — MANAGE ✓
Can we control the change?
```
右側下一站巨大：
```text
L3 — UNDERSTAND ?
HOW DOES IT ACTUALLY WORK?
```
下方階梯：
```text
BUILD
  ↓
MANAGE
  ↓
UNDERSTAND ← NEXT
  ↓
SECURE
```
底部：
```text
DON'T JUST RUN THE CODE.
UNDERSTAND THE FLOW.
```
繁中：**不要只讓程式能跑；要理解它如何流動。**

## 視覺
同一個 Weather Security Center。L1 看外觀與 Working；L2 外圍出現 Spec / AI / Evidence / Git History；L3 開始把 App 畫成 X-Ray：Frontend → HTTP → FastAPI → API → JSON → Weather Data。

## 煥哥
表情：完成 L2，但開始對系統內部產生好奇。
動作：一手拿著 L2 Evidence Package，另一手用 X-Ray / 放大鏡看 Weather Security Center 內部。
角色：從 ENGINEERING LEAD 轉成 SYSTEM EXPLORER。

## 老師講稿
今天我們沒有深入教 Python Syntax，也沒有深入解 FastAPI Route。

這是刻意的。

L2 解決的是：
```text
WHY does this change exist?
WHAT should change?
WHAT should not change?
WHEN is it done?
WHAT evidence proves it?
WHERE is the history?
```

現在我們已經能管理 AI 做的 Change。

但是如果我問：
> Browser 按下 Refresh 後，資料怎麼一路走到畫面？

你可能還說不清楚。

所以下一堂 L3 不重新 Build 新網站。

我們把同一個 Weather Security Center 打開來看它的內部：
```text
PYTHON
→ FUNCTION / VARIABLE / DATA
→ HTTP REQUEST / RESPONSE
→ API
→ JSON
→ FASTAPI ROUTE
→ FRONTEND ↔ BACKEND
→ WEATHER DATA FLOW
```

## Exit Ticket
請學生用一句話回答三題：
1. Prompt 和 Spec 最大差異是什麼？
2. AI 說 Done 為什麼還不算 Done？
3. Git / GitHub 在今天流程中保存了什麼？

## 核心句
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

接續下一課：
> **DON'T JUST RUN THE CODE. UNDERSTAND THE FLOW.**
> **不要只讓程式能跑；要理解資料與程式如何流動。**

## Transition
L2 結束。

下一課：
# **AIIS_L3 — UNDERSTAND**
## Python × FastAPI × HTTP × API × JSON × Web App
