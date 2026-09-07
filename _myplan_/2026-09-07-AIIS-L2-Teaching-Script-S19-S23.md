# AIIS_L2 — 逐頁詳細教學稿 S19–S23
## Part D — VERIFY：不要相信 Done，要驗證 Done

狀態：CANONICAL — L1 STYLE — 2026-09-07

統一格式：**目的 → 投影片內容 → 視覺 → 煥哥 → 老師講稿 → 問答 → 核心句 → Transition**。

本段唯一驗證主線：
```text
CHANGED FILES → DIFF → RUN / TEST → ACCEPTANCE CRITERIA → HUMAN DECISION
```

---

# Slide 19 — AI 到底改了哪些 Files？

## 目的
VERIFY 的第一步不是相信 AI Summary，而是確認實際 Change Surface。讓學生建立 Planned vs Actual 的比對習慣。

## 投影片內容
左側：
```text
EXPECTED
index.html
style.css ?
```
右側：
```text
ACTUAL
index.html ✓
style.css ✓
main.py ?
requirements.txt ?
```
中央：
```text
EXPECTED ≠ ACTUAL ?
```
底部：
```text
UNEXPECTED ≠ WRONG
UNEXPECTED = REVIEW SIGNAL
```
繁中：**沒預期到的修改不一定錯，但一定值得檢查。**

## 視覺
兩欄 File Cards。Expected 是 Human 核准 Plan 時的預期；Actual 是 AI 完成後真正 Changed Files。`main.py`、`requirements.txt` 用醒目的問號，不先判紅叉。

## 煥哥
表情：冷靜調查。
動作：拿著 Plan Checklist 對照 Changed Files。
視線：特別看 `requirements.txt ?`。
角色：CHANGE SURFACE REVIEWER。

## 老師講稿
上一頁我們說 AI 的 `Done` 只是 Claim。

第一個 Evidence 很簡單：
> 到底哪些 Files 被改了？

我們原本預期主要修改 Dashboard，可能需要少量 Style。

結果現在看到：
```text
index.html
style.css
main.py
requirements.txt
```

這時不要立刻說 AI 錯了。

Unexpected 不等於 Wrong。`main.py` 可能真的有合理原因。

但是 Unexpected 一定是一個 Review Signal：
> 為什麼要改？跟 Spec 有什麼關係？

## 問
如果 Plan 說只需要 Dashboard，但 Actual 多出 `requirements.txt`，第一個動作是什麼？

A. 立刻刪掉。
B. 不管它。
C. 檢查為什麼被修改。

預期答案：C。

## 老師補充
可以把 Changed Files 分成三類：
```text
EXPECTED
UNEXPECTED BUT JUSTIFIED
SUSPICIOUS / NEEDS REVIEW
```
不用要求學生現在判斷程式內容，先學會看到差異就停下來檢查。

## 核心句
> **FIRST VERIFY THE CHANGE SURFACE.**
> **先確認 AI 到底碰了哪些地方。**

## Transition
> 知道哪些 Files 被碰過，仍然不知道每個 File 裡面到底發生什麼。

下一頁：**看 Diff。**

---

# Slide 20 — DIFF：Before vs After

## 目的
讓學生理解 Diff 是檢查實際修改內容的核心 Evidence；不能只看最後 UI 看起來正常。

## 投影片內容
左側 BEFORE：
```html
<div class="weather">
  ...
</div>
```
右側 AFTER：
```html
<div class="weather">
  ...
</div>
<div class="last-updated">
  Last Updated: ...
</div>
```
右下角另外一張小卡：
```text
requirements.txt
- fastapi==...
+ fastapi==NEW_VERSION   ?
```
底部：
```text
A WORKING SCREEN CAN HIDE AN UNWANTED DIFF.
```
繁中：**畫面看起來正常，也可能藏著不需要的修改。**

## 視覺
主視覺就是 Before / After Diff。新增 Last Updated 是合理綠色區塊；Dependency 版本改動用問號標記。不要放完整真實大型 Diff。

## 煥哥
表情：像 Code Reviewer。
動作：拿放大鏡查看 `+` / `-`。
角色：DIFF REVIEWER。

## 老師講稿
Changed Files 告訴你「哪裡變了」。

Diff 才告訴你：
> **到底怎麼變。**

例如 Dashboard 新增 Last Updated，符合我們的 Spec。

但是同一個 Change 裡，`requirements.txt` 的 FastAPI Version 也被改了。

網站最後可能仍然正常，所以如果你只看畫面，很容易完全沒發現這件事。

現在我們不用深入理解 FastAPI 版本差異，那是另一個層次。L3 才會真正進入 Code 與 Data Flow。

今天只問四個工程問題：
```text
WHY?
IN SCOPE?
NECESSARY?
MATCHES SPEC?
```

## 問
如果網站看起來完全正常，還需要看 Diff 嗎？

預期答案：需要。

再問：為什麼？

預期：因為可能有不必要、無關或有風險的修改藏在背後。

## 核心句
> **DON'T ONLY VERIFY THE RESULT. VERIFY THE CHANGE.**
> **不要只看結果；也要檢查變更本身。**

## Transition
> Diff 看起來合理，只代表靜態修改看起來合理。系統真的能跑嗎？

下一頁：**RUN / TEST。**

---

# Slide 21 — RUN / TEST：真的能正常運作嗎？

## 目的
從 Static Evidence 進入 Runtime Evidence。讓學生理解「看起來對」和「實際能運作」不同。

## 投影片內容
中央四個檢查項目：
```text
□ App starts
□ Weather data loads
□ Last Updated appears
□ Existing behavior still works
```
下方巨大：
```text
LOOKS RIGHT ≠ WORKS RIGHT
```
繁中：**看起來正確，不等於實際運作正確。**

## 視覺
左側是 Code / Diff，箭頭進入 Running App，右側是四項 Runtime Checklist。這頁不展示測試框架或大量 Terminal 指令。

## 煥哥
表情：實際驗證。
動作：一手按 Run，一手拿 Runtime Checklist。
角色：TESTER。

## 老師講稿
到目前為止，我們做的主要是 Static Review。

現在真的把 App 跑起來。

至少確認：
- App 能不能啟動？
- Weather Data 還能不能載入？
- Last Updated 有沒有真的出現？
- 原本功能有沒有被我們弄壞？

最後一項就是很重要的 Regression 思維：
> 加入新功能時，不要破壞原本已經會工作的功能。

這堂課不是 Test Framework 課，所以不需要現在教 pytest 的完整語法。先建立「修改後一定要實際驗證」的習慣。

## 問
Last Updated 顯示正常，但 Weather Data 不再載入，這個 Change 算成功嗎？

預期答案：不算。

## 老師補充
如果 Test FAIL：
```text
FAIL
 ↓
INVESTIGATE
 ↓
REVISE
 ↓
TEST AGAIN
```
不是看到 Fail 就硬把它標成 Pass。

## 核心句
> **RUN IT. TEST IT. DON'T ASSUME IT.**
> **實際執行、實際測試，不要靠假設。**

## Transition
> 現在 App 能跑了，新功能也出現了。是不是終於可以說 Done？

還差最重要的一步：
> 回去看我們在 S12 先寫好的 Acceptance Criteria。

下一頁：**Verify against AC。**

---

# Slide 22 — 回到 Acceptance Criteria：真的符合 Done 嗎？

## 目的
完成 S12 的教學伏筆。讓學生看到 Spec → Evidence → Verification 的完整閉環，並刻意保留一項 FAIL，證明「功能會跑」仍不等於 Change 可接受。

## 投影片內容
把 S12 的五個 Checkbox 原樣帶回來，現在加入 Evidence 與 Result：
```text
AC-01 Last Updated visible     UI / Runtime       PASS ✓
AC-02 Time readable            UI                 PASS ✓
AC-03 Weather still works      Run / Test         PASS ✓
AC-04 API behavior unchanged   Diff / Review      PASS ✓
AC-05 No unnecessary dep.      requirements Diff  FAIL ✕
```
下方巨大：
```text
SPEC DEFINES DONE.
EVIDENCE PROVES DONE.
```
繁中：**Spec 定義完成；Evidence 證明完成。**

## 視覺
與 S12 使用同一張 Acceptance Checklist，形成學生明顯可辨識的視覺回憶。S12 五格全空；S22 四綠一紅。AC-05 的 FAIL 成為全頁焦點。

## 煥哥
表情：原本準備打勾，看到最後一項後停住。
動作：手拿筆停在 `AC-05 FAIL`。
角色：ACCEPTANCE VERIFIER。

## 老師講稿
大家還記得 S12 嗎？

那時候五個 Checkbox 全部是空的，因為 AI 還沒有開始 Build。

現在我們終於有 Evidence，可以一條一條驗證。

前四條都 PASS。

但 AC-05：
> No unnecessary dependency is added.

我們剛才 Diff 發現 `requirements.txt` 有一個沒有充分理由的版本修改。

所以即使畫面漂亮、App 會 Run，我們仍然不能把所有 Criteria 打勾。

這就是為什麼 Done 必須在 Build 前先定義。

## 問
現在功能已經能正常使用，這個 Change 是 Done 嗎？

預期答案：還不是，至少 AC-05 沒有通過。

再問：那應該怎麼做？

合理答案：要求 AI 移除不必要修改／說明必要性 → Review → Run/Test → 再驗證 AC。

## 老師補充
這裡可以第一次簡單畫出 Traceability：
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
不必深入講 Traceability Matrix。

## 核心句
> **DONE MUST BE PROVEN, NOT ANNOUNCED.**
> **完成必須被證明，不是被宣布。**

## Transition
> Evidence 已經擺在桌上。最後還有一個角色不能消失：Human。

下一頁：**ACCEPT / REVISE / REJECT。**

---

# Slide 23 — HUMAN DECISION：接受、修正、還是拒絕？

## 目的
完成 VERIFY 階段，讓學生理解 Human-in-the-loop 的第二個 Gate：不是憑感覺，而是根據 Evidence 做 Engineering Decision。

## 投影片內容
中央：
```text
          EVIDENCE
             ↓
        HUMAN REVIEW
             ↓
    ┌────────┼────────┐
    ↓        ↓        ↓
 ACCEPT    REVISE   REJECT
 接受       修正      拒絕
```
底部：
```text
AI PROPOSES.
TOOLS PROVIDE EVIDENCE.
HUMAN DECIDES.
```

## 視覺
與 S16 Human Plan Review 使用相同 Gate 視覺，形成鏡像：
```text
S16 BEFORE CODE → HUMAN PLAN GATE
S23 AFTER CODE  → HUMAN EVIDENCE GATE
```

## 煥哥
表情：負責任、做決策。
動作：桌面上放著 Spec、Diff、Test、AC Evidence，手放在三個 Decision Buttons 前。
角色：ENGINEERING APPROVER。

## 老師講稿
大家有沒有發現 Human 出現了兩次？

第一次是 S16：
> Code 還沒寫之前，Human Review Plan。

第二次是現在：
> Code 寫完之後，Human Review Evidence。

所以 Human-in-the-loop 不是最後按一下 OK。

我們來看三種情況。

Case A：只做需求內修改，所有 AC PASS。
> ACCEPT。

Case B：功能正常，但多了一個不必要 Dependency。
> REVISE。

Case C：一個小需求卻造成 DB redesign、API redesign、Framework upgrade，而且沒有核准。
> REJECT，或要求大幅重新規劃。

## 問
如果 AI 很有自信，但 Evidence 有 FAIL，應該相信哪一個？

預期答案：Evidence。

## 板書
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

## 核心句
> **AI PROPOSES. TOOLS PROVIDE EVIDENCE. HUMAN DECIDES.**
> **AI 提案，工具提供證據，人類做最後決定。**

## Transition
> 假設我們已經修正 AC-05、重新 Test，最後全部 PASS，Human 也 ACCEPT。

現在這個 Change 已經 Verified。

但如果明天全部忘記了呢？

下一頁：**Software Needs Memory。**
