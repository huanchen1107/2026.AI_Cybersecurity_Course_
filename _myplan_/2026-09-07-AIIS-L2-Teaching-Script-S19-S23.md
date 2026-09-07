# AIIS_L2 — 詳細教學講稿 S19–S23
## Part D — VERIFY：不要相信 Done，要驗證 Done

狀態：PART D — CANONICAL zh-TW REFINEMENT — 2026-09-07
課程位置：L2 / MANAGE

前一段已完成：
```text
DEFINE ✓ → BUILD ✓ → VERIFY → REMEMBER
                    ↑
                  現在
```

> **BUILD 產生變更；VERIFY 建立信任。**

本段用一條固定的五步驗證漏斗：
```text
1. CHANGED FILES
      ↓
2. DIFF
      ↓
3. RUN / TEST
      ↓
4. ACCEPTANCE CRITERIA
      ↓
5. HUMAN DECISION
```

每頁只回答一個問題：
```text
S19 AI 到底碰了哪些檔案？
S20 每個檔案到底改了什麼？
S21 系統真的能正常運作嗎？
S22 是否真的符合先前定義的 Done？
S23 最後誰決定接受？
```

---

# Slide 19 — Changed Files
## AI 到底碰了哪些檔案？

### 這頁在做什麼
建立第一層 Verification：不要先相信 AI Summary，先看實際 Change Surface。

### ON SLIDE
左側：
```text
EXPECTED
index.html
style.css ?
```

右側：
```text
ACTUAL
index.html
style.css
main.py
requirements.txt
```

底部：
> **UNEXPECTED ≠ WRONG**
> **UNEXPECTED = REVIEW SIGNAL**
> **非預期變更不一定錯，但一定值得檢查。**

### 視覺
用 Expected vs Actual 兩欄 File cards。不要在這頁展示真正 Diff 內容。

### 煥哥角色
**Change Surface Reviewer（變更範圍審查者）**，拿著 Expected List 對照 Actual Files。

### 教師講稿
> VERIFY 第一個問題甚至不是「Code 對不對」，而是「AI 到底碰了哪些地方」。

回想 S15 Plan：如果當時預計只改 Dashboard template，現在卻出現 `requirements.txt`，就應該停下來問 WHY。

### 三類判斷
```text
EXPECTED
符合 Plan

UNEXPECTED BUT JUSTIFIED
原 Plan 沒想到，但有合理必要性

SUSPICIOUS
看不出和 Spec 有什麼關係
```

學生不用因為看到 Unexpected 就立刻判錯；要進下一層看 Diff。

### 快問
`add-weather-last-updated` 卻改到 Authentication file，第一反應應該是？

A. 一定是漏洞
B. 一定是錯
C. 需要 Review

答案：C。

### 學生只需帶走
> **先確認 Change Surface，再深入看內容。**

### 銜接 S20
> 知道哪些 Files 被改還不夠。下一步要看每一個 File 到底改了什麼。

建議時間：7–8 分鐘。

---

# Slide 20 — Diff = Before vs After
## 不看 AI 怎麼說，要看實際變更

### 這頁在做什麼
讓學生理解 Diff 是「實際變更證據」：看新增、刪除與修改，而不是只看最後 UI。

### ON SLIDE
左：BEFORE
```html
<div class="weather-card">
  ...
</div>
```

右：AFTER
```html
<div class="weather-card">
  ...
  <span>Last Updated: {{ updated_at }}</span>
</div>
```

下方再放一個小警訊：
```text
requirements.txt
fastapi==x → fastapi==newer-x   ?
```

底部：
> **A WORKING SCREEN CAN HIDE AN UNWANTED DIFF.**
> **畫面正常，也可能藏著不必要的變更。**

### 視覺
只展示一個正常 Diff + 一個可疑小 Diff。不要塞完整 Git patch。

### 煥哥角色
**Diff Reviewer（差異審查者）**，左右比對 Before / After。

### 教師講稿
> Changed Files 告訴我們「哪裡被碰」，Diff 才告訴我們「到底怎麼碰」。

學生此時還不用完全理解每一行 Python；那是 L3 的工作。但要先學會問四個工程問題：
```text
WHY    為什麼改？
SCOPE  在範圍內嗎？
RISK   有沒有副作用？
SPEC   和需求有關嗎？
```

### 快速判斷
如果畫面成功顯示 Last Updated，但 Diff 同時升級了 FastAPI，是否可以直接接受？

答案：不能，先理解原因並對照 Scope / AC。

### 學生只需帶走
> **不要只驗最後畫面，要驗實際變更。**

### 銜接 S21
> Diff 看起來合理，也還不代表系統真的能 Run。

建議時間：8–9 分鐘。

---

# Slide 21 — RUN / TEST
## 看起來對，不代表真的能運作

### 這頁在做什麼
從靜態變更證據進入執行證據：真的啟動 Weather Security Center，驗證新功能與既有功能。

### ON SLIDE
只放四個 Check：
```text
□ App starts
□ Weather data loads
□ Last Updated appears
□ Existing behavior still works
```

底部：
> **LOOKS RIGHT ≠ WORKS RIGHT**
> **看起來對，不代表真的能運作。**

### 視覺
Weather Security Center 正在執行的畫面 + 四個 Runtime Checks。

### 煥哥角色
**Runtime Tester（執行測試者）**，不是看 Code，而是在操作真正的 App。

### 教師講稿
> 到現在我們有 Static Evidence：Files、Diff。接下來需要 Runtime Evidence。

學生至少測：
1. App 能正常啟動。
2. Weather Data 正常顯示。
3. Last Updated 出現且可讀。
4. 原有重要行為沒有明顯被破壞。

簡單引入 Regression：
> **Regression（回歸問題）** = 新修改讓原本正常功能壞掉。

不在本頁深入 unit test framework 或 Python internals，避免侵入 L3。

### 如果 Test Fail
```text
FAIL
 ↓
INVESTIGATE
 ↓
REVISE
 ↓
TEST AGAIN
```

### 學生只需帶走
> **沒有 Run/Test，只有「看起來應該可以」。**

### 銜接 S22
> App 能跑只是其中一種 Evidence。現在要把 S12 寫好的 Acceptance Criteria 拿回來。

建議時間：8–10 分鐘。

---

# Slide 22 — Verify Against Acceptance Criteria
## 回到 S12：逐條證明 Done

### 這頁在做什麼
完成 DEFINE → VERIFY 閉環。不是憑感覺說「差不多完成」，而是逐條將 AC 與 Evidence 配對。

### ON SLIDE
```text
AC                    EVIDENCE              RESULT
-------------------------------------------------
AC-01 Last Updated    UI / runtime          PASS
AC-02 readable        UI                    PASS
AC-03 weather works   run/test              PASS
AC-04 API unchanged   diff/review           PASS
AC-05 no extra dep    requirements diff     FAIL
```

底部：
> **SPEC DEFINES DONE. EVIDENCE PROVES DONE.**
> **Spec 定義完成；Evidence 證明完成。**

### 視覺
一個極簡 Verification Matrix。這頁是 S12 五個空 Checkbox 的回收頁。

### 煥哥角色
**Acceptance Verifier（驗收驗證者）**，逐條把 Evidence 放到 AC 旁邊。

### 教師講稿
提醒學生 S12：
> 我們在一行 Code 都還沒改以前，就先寫了 AC。現在它們終於派上用場。

故意留下 AC-05 FAIL：
> 即使畫面很好看、功能能跑，只要無必要 Dependency 這條沒通過，就還不能說 Change 已經 Accepted。

### Traceability 簡化展示
```text
WHY
 ↓
REQUIREMENT
 ↓
AC
 ↓
IMPLEMENTATION
 ↓
EVIDENCE
```

不用講更複雜的需求工程術語，只讓學生知道每一個 Evidence 應該能回到一個要求。

### DONE 定義
```text
DONE
= Requirements satisfied
+ Acceptance Criteria passed
+ No unacceptable side effects
+ Human reviewed the evidence
```

### 學生只需帶走
> **Done 必須能被證明，不是被宣布。**

### 銜接 S23
> Evidence 都在桌上了。最後誰來做決定？

建議時間：9–10 分鐘。

---

# Slide 23 — HUMAN DECISION
## ACCEPT / REVISE / REJECT

### 這頁在做什麼
收束 VERIFY：工具提供 Evidence，AI 提供建議，但最後由 Human 做接受決策。

### ON SLIDE
```text
             EVIDENCE
                 ↓
          HUMAN REVIEW
                 ↓
     ┌───────────┼───────────┐
     ↓           ↓           ↓
  ACCEPT       REVISE      REJECT
   接受         修正         拒絕
```

底部：
> **AI PROPOSES. TOOLS PROVIDE EVIDENCE. HUMAN DECIDES.**
> **AI 提案，工具提供證據，人類做決定。**

### 視覺
與 S16 Human Plan Review 呼應，但這次 Gate 位於實作與 Evidence 之後。

### 煥哥角色
**Final Reviewer（最終審查者）**，面前是 Spec、Diff、Test、AC Evidence。

### 教師講稿
給三個案例：

**Case A**
```text
Only requested change
All AC PASS
No suspicious side effect
```
→ ACCEPT

**Case B**
```text
Feature works
But unnecessary package added
```
→ REVISE

**Case C**
```text
Small request
But DB/API redesigned + framework upgraded
```
→ REJECT 或重大 REVISE

### Human 的真正責任
```text
DEFINE INTENT
CONTROL SCOPE
REVIEW PLAN
INTERPRET EVIDENCE
MAKE DECISION
```

### 五步驗證 Anchor
整段最後完整顯示：
```text
WHAT CHANGED?
Changed Files
      ↓
EXACTLY HOW?
Diff
      ↓
DOES IT WORK?
Run / Test
      ↓
DOES IT MATCH SPEC?
Acceptance Criteria
      ↓
SHOULD WE ACCEPT IT?
Human Decision
```

### 學生只需帶走
> **驗證的終點不是「測試跑完」，而是 Human 根據 Evidence 做 Decision。**

### Part D 收束
```text
AI SAYS DONE
     ↓
CHANGED FILES
     ↓
DIFF
     ↓
RUN / TEST
     ↓
AC VERIFICATION
     ↓
HUMAN DECISION
     ↓
VERIFIED CHANGE ✓
```

### 銜接 S24
> Change 已經被驗證並接受。下一個問題是：三個月後，我們還記得今天改了什麼、為什麼改嗎？

下一頁進入：**REMEMBER — Git + GitHub**

建議時間：9–10 分鐘。
