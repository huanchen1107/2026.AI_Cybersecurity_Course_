# AIIS_L2 — 詳細教學講稿 S19–S23
## Part D — VERIFY：不要相信 Done，要驗證 Done

狀態：PART D DETAILED TEACHING SCRIPT COMPLETE — 2026-09-07
課程位置：L2 / MANAGE
語言：繁體中文為主；必要資訊工程術語保留英文。

> 本檔採「每一頁都可直接拿去做 PPT + 上課」的詳細規格，而不是只有大綱。

每頁固定包含：教學目的、學生先備認知、投影片文字、視覺構圖、煥哥角色、逐步揭露、教師講稿、示範資料、提問、學生互動、常見誤解、板書、核心句、帶走能力、前後頁銜接與建議時間。

前段：
```text
DEFINE → BUILD → VERIFY → REMEMBER
                  ↑
                現在
```

Part D 要回答五個問題：
```text
1. WHAT CHANGED?        改了什麼？
2. EXACTLY HOW?         到底怎麼改？
3. DOES IT WORK?        真的能運作嗎？
4. DOES IT MATCH SPEC?  符合規格嗎？
5. SHOULD WE ACCEPT?    人類應該接受嗎？
```

---

# Slide 19 — Changed Files
## AI 到底改了哪些檔案？

### 1. 教學目的
學生第一次從「AI 的完成摘要」轉向「實際變更事實」。本頁不深入 Git Diff 細節；先建立 Changed Files 是最便宜、最快速的第一層 Verification。

### 2. 學生先備認知
學生已在 S17 讓 AI 依核准 Plan 實作，S18 已知道：
> **AI CLAIM ≠ VERIFIED EVIDENCE**

### 3. 投影片主標題
**Changed Files — AI 到底改了哪些檔案？**

副標：
> **第一個驗證問題：WHAT ACTUALLY CHANGED?**

### 4. 主視覺
左右比較：

```text
EXPECTED FROM PLAN            ACTUAL CHANGE
預期                           實際

✓ templates/index.html        ✓ templates/index.html
? static/style.css            ✓ static/style.css
                              ! main.py
                              ! time_helper.py
                              ! requirements.txt
```

把三個非預期檔案用醒目警示符號呈現。

底部：
> **Unexpected file ≠ automatically wrong. It means: REVIEW ME.**
> **非預期檔案不一定錯，但一定值得審查。**

### 5. 煥哥角色
**CHANGE AUDITOR（變更稽核者）**。

煥哥拿著原本核准的 Plan，對照 AI 實際修改檔案清單；看到 `requirements.txt` 時眉頭微皺並標記 `WHY?`。

### 6. 逐步揭露
第一步只顯示：
```text
Expected:
index.html
style.css ?
```

問學生：
> 這是我們 S15 Plan 預期的範圍，還記得嗎？

第二步再顯示 Actual：
```text
index.html
style.css
main.py
time_helper.py
requirements.txt
```

停頓，不先評論。

第三步問：
> 第一眼你最想問哪一個檔案？為什麼？

### 7. 教師詳細講稿
> AI 剛剛說它已經完成 Last Updated。現在我們不先看它的 Summary，我們先看最基本的事實：它到底碰了哪些檔案。

> 我們原本核准的 Plan 預期主要修改 Dashboard Template，必要時調整一點 Style。如果實際結果突然多出 `main.py`、`time_helper.py`、`requirements.txt`，這是不是立刻代表 AI 做錯？

等待學生。

> 不一定。也許 Inspect 後真的發現 Backend 必須提供一個欄位。但工程上不能因為「也許有理由」就跳過 Review。我們要問：**每一個實際 Change，都能不能回到 Spec 或必要實作理由？**

### 8. Expected vs Actual 概念
```text
PLAN = 我們核准 AI 預計怎麼做
ACTUAL = AI 最後真的做了什麼
```

Verification 的第一個差異就是：
```text
EXPECTED ?= ACTUAL
```

### 9. 示範情境 A — 正常
```text
Expected:
- index.html

Actual:
- index.html
```

教師：
> 很乾淨，但仍然不能直接 Accept。下一頁還要看 Diff。

### 10. 示範情境 B — 合理但需解釋
```text
Expected:
- index.html

Actual:
- index.html
- main.py
```

AI 說明：現有 template 沒有取得 CWA `obsTime`，因此需將已存在資料傳入 template。

教師：
> 這可能合理，但我們要檢查是不是真的如此，而不是只聽 AI 解釋。

### 11. 示範情境 C — 高度可疑
```text
Actual:
- index.html
- main.py
- auth.py
- database.py
- requirements.txt
```

問：
> Last Updated 為什麼碰 Authentication 和 Database？

這就是 Scope Review 訊號。

### 12. 學生活動：三秒鐘 Change Triage
投影三組 Actual Changed Files，學生用手勢：
- 👍 合理
- 🤔 需要解釋
- ✋ 高度可疑

重點不是猜答案，而是養成「看到 Change Surface 先停一下」的習慣。

### 13. 常見誤解
**誤解 1：AI 多改檔案就是錯。**
修正：不是；但非預期修改必須有必要理由。

**誤解 2：檔案數少就安全。**
修正：一個檔案也可以改壞很多東西，所以 S20 還要看 Diff。

### 14. 板書
```text
PLAN
  ↓ compare
ACTUAL FILES
```

大字：
```text
UNEXPECTED ≠ WRONG
UNEXPECTED = REVIEW SIGNAL
```

### 15. 核心句
> **先問「改了哪些檔案」，再問「每個檔案改了什麼」。**

### 16. 本頁帶走能力
學生能：
1. 比較 Planned Files 與 Actual Changed Files。
2. 辨識非預期 Change Surface。
3. 不因 AI 解釋而跳過後續證據檢查。

### 17. 銜接 S20
> 知道改了五個檔案還不夠。下一個問題是：每一個檔案裡，到底刪了什麼、加了什麼？這就是 Diff。

建議時間：8–10 分鐘。

---

# Slide 20 — Diff = Before vs After
## 不要只看結果，要看「前後到底差在哪裡」

### 1. 教學目的
建立 Diff 的直覺。這不是 Git 指令課，而是 Change Review 課。學生要理解 Diff 是查看「實際變更」最直接的工程證據之一。

### 2. 投影片主標題
**Diff = Before vs After**

副標：
> **不要只看新增了什麼，要看所有改變。**

### 3. 主視覺
模擬 Diff：

```diff
 <div class="weather-info">
   <h2>臺中市</h2>
+  <p>最後更新：2026-09-07 18:30</p>
 </div>
```

旁邊另一段：

```diff
-fastapi==0.xx.x
+fastapi==0.yy.y
```

第一段標：`EXPECTED ✓`
第二段標：`WHY?`

### 4. 煥哥角色
**DIFF REVIEWER（差異審查者）**。

拿著 Before / After 透明片疊合，指出真正不同的位置。

### 5. 教師開場
> Changed Files 告訴我們「哪裡被碰過」，Diff 才告訴我們「到底怎麼碰」。

在黑板寫：
```text
Changed Files = WHERE
Diff          = WHAT EXACTLY
```

### 6. Diff 的簡單解釋
不用教 Git internals。

> Diff 就是把修改前與修改後做比較，讓我們看到哪些內容被新增、刪除或修改。

```text
- removed
+ added
```

### 7. 第一段示範：合理變更
展示加入 Last Updated 的 HTML。

問：
> 這段能不能對回 Requirement？

引導到 REQ-01 / AC-01。

建立 Traceability：
```text
SPEC
REQ-01
  ↓
DIFF
Last Updated UI
```

### 8. 第二段示範：隱藏的額外變更
再揭露 dependency upgrade。

教師：
> 如果我們只打開網站看畫面，會看到這一行嗎？

答案：不會。

> 所以「畫面看起來正常」不能取代 Diff Review。

### 9. Diff Review 四問
每看到一段重要 Diff，都問：

```text
1. WHY — 為什麼需要這個改動？
2. SCOPE — 它在這次範圍內嗎？
3. RISK — 它可能影響什麼？
4. SPEC — 它能對回哪個 Requirement / AC？
```

### 10. 「新增」與「刪除」都要看
教師：
> 很多人只看 AI 新增的漂亮 Code，但刪掉的東西有時更危險。

示例：
```diff
- if weather_data is None:
-     return error_response
```

問：
> Last Updated 為什麼把 Error Handling 刪掉？

### 11. 學生活動：Spot the Unrelated Change
給一個小型 Diff，包含：
- 正常加入 timestamp；
- 改標題字體；
- 移除錯誤處理；
- 升級 dependency。

學生圈：
```text
NEEDED
QUESTIONABLE
OUT OF SCOPE
```

### 12. 常見誤解
**「我不會寫這段 Code，所以不能 Review Diff。」**

教師修正：
> L2 不要求你完全理解每個 Python 細節；那是 L3 要加強的能力。今天至少要能問：這段 Change 為什麼存在？跟 Spec 有沒有關係？

這也自然銜接 L3 UNDERSTAND。

### 13. 板書
```text
FILES = WHERE?
DIFF  = WHAT EXACTLY?
```

```text
DON'T REVIEW ONLY THE OUTPUT.
REVIEW THE CHANGE.
```

繁中：
> **不要只審最後畫面，要審實際變更。**

### 14. 本頁帶走能力
學生能：
1. 說明 Diff 的用途。
2. 用 Scope / Requirement 來看 Diff。
3. 注意新增與刪除兩種變化。
4. 辨識與需求無關的修改。

### 15. 銜接 S21
> Diff 看起來合理，代表程式一定能跑嗎？不代表。下一步我們要讓系統真的執行。

建議時間：10–12 分鐘。

---

# Slide 21 — Run / Test
## Code 看起來對，不代表真的能運作

### 1. 教學目的
讓學生建立最基本的動態驗證觀念：靜態看 Code/Diff 與實際執行是兩種不同證據。本頁不深入 pytest 或測試框架，那屬於後續課程與實作細節。

### 2. 主標題
**RUN / TEST — 真的跑一次**

副標：
> **LOOKS RIGHT ≠ WORKS RIGHT**
> **看起來正確 ≠ 實際運作正確**

### 3. 主視覺

```text
CODE / DIFF
看起來合理
     ↓
RUN APPLICATION
     ↓
CHECK BEHAVIOR
     ↓
EVIDENCE
```

右側 Checklist：
```text
□ Application starts
□ Weather data loads
□ Last Updated appears
□ Time is readable
□ Existing page still works
```

### 4. 煥哥角色
**TEST OPERATOR（測試操作員）**。

一手看 Browser，一手看 Terminal；不是只看 AI 對話視窗。

### 5. 教師開場
> 我們已經知道 AI 改了哪些檔案，也看了 Diff。現在是不是可以 Accept？

停頓。

> 還不行。因為 Code 可以「看起來很合理」，但真正 Run 時才出現 Error。

### 6. 最小 Run Checklist
本次 Lab 不需要複雜 Test Framework：

```text
TEST-01 App 能啟動嗎？
TEST-02 Weather Data 能載入嗎？
TEST-03 Last Updated 有出現嗎？
TEST-04 時間看得懂嗎？
TEST-05 原本功能仍正常嗎？
```

### 7. 示範失敗案例 A
AI 加了：
```text
Last Updated: None
```

問：
> AC-01「有顯示」算 PASS 嗎？

引導：形式上有文字，但資訊沒有意義，需看 AC-02 可讀性/有效性。

### 8. 示範失敗案例 B
Last Updated 正常，但 Weather Data 不再顯示。

```text
Last Updated ✓
Weather Data ✗
```

教師：
> 新功能成功，但 Regression（既有功能退化）發生了。

簡單定義：
> **Regression = 修改後，原本正常的功能變壞。**

不深入自動化 regression testing。

### 9. 示範失敗案例 C
本機能跑，但啟動 Terminal 出現新 dependency 缺失。

問：
> 這跟 AC-05 有沒有關係？

讓學生開始把 Test Evidence 與 Acceptance Criteria 連起來。

### 10. Evidence 要記錄什麼
簡單表：

| Test | Result | Evidence |
|---|---|---|
| App starts | PASS | Terminal / browser |
| Weather loads | PASS | Dashboard |
| Last Updated | PASS | Dashboard |
| Existing behavior | PASS | Manual check |

教師：
> 「我有測」比不上「我可以說明測了什麼、結果是什麼」。

### 11. 學生活動
學生實際 Run Weather Security Center，完成 5 項 Checklist。若失敗，不要求假裝 PASS，必須記錄 FAIL。

### 12. 重要文化
> **FAIL 不是丟臉；假的 PASS 才是工程問題。**

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

### 13. 常見誤解
- Browser 打得開 ≠ 所有功能正常。
- 沒看到 Error ≠ Acceptance Criteria 全部 PASS。
- AI 說已測試 ≠ 學生已取得自己的驗證證據。

### 14. 板書
```text
STATIC REVIEW → Diff
DYNAMIC CHECK → Run/Test
```

大字：
> **LOOKS RIGHT ≠ WORKS RIGHT**

### 15. 本頁帶走能力
學生能：
1. 實際執行變更後系統。
2. 檢查新功能與既有功能。
3. 記錄 PASS / FAIL，而不是只說「好像可以」。

### 16. 銜接 S22
> 現在功能真的跑了。但「能跑」是不是等於「符合我們一開始的 Spec」？還差最後一個逐條對照。

建議時間：10–15 分鐘（含實作）。

---

# Slide 22 — Verify Against Acceptance Criteria
## 回到最開始的 Spec，一條一條驗收

### 1. 教學目的
完成 DEFINE → BUILD → VERIFY 的閉環。學生理解 Acceptance Criteria 不是寫完就放著，而是最後必須逐條拿回來驗證。

### 2. 主標題
**VERIFY AGAINST THE SPEC**

副標：
> **Spec 定義 Done；Evidence 證明 Done。**

### 3. 主視覺
完整 Verification Matrix：

| AC | 驗收條件 | Evidence | 結果 |
|---|---|---|---|
| AC-01 | Dashboard 顯示 Last Updated | Browser | PASS |
| AC-02 | 時間格式清楚可讀 | Browser | PASS |
| AC-03 | Weather Data 正常顯示 | Run/Test | PASS |
| AC-04 | Existing API behavior 未刻意改變 | Diff + Test | PASS |
| AC-05 | 無不必要 Dependency | Diff / files | PASS |

### 4. 煥哥角色
**ACCEPTANCE REVIEWER（驗收審查者）**。

手拿 S12 當時寫好的 Acceptance Criteria，逐條對照現在 Evidence；形成視覺上的「回到原點」。

### 5. 教師開場
> 還記得 S12 嗎？那時候 Code 一行都還沒有改，我們就先寫好了五條 Acceptance Criteria。

> 現在它們終於派上用場。

把 S12 → S22 畫成回環：
```text
DEFINE AC
   ↓
BUILD
   ↓
TEST
   ↓
VERIFY AC
```

### 6. 一條 AC 需要對應 Evidence
教師逐項示範：

**AC-01**：不是 AI 說「我加了」，而是 Browser 實際可見。

**AC-03**：不是 Last Updated 自己正常就好，Weather Data 仍需正常。

**AC-05**：不是 UI 能跑就算；還要看 Changed Files / Diff 是否出現不必要 dependency。

### 7. 最重要案例：Feature Works but Change Fails
情境：
```text
AC-01 PASS
AC-02 PASS
AC-03 PASS
AC-04 PASS
AC-05 FAIL
```

原因：AI 新增一個不必要的日期套件。

問學生：
> 4/5 PASS，而且畫面正常，可以交嗎？

課程答案：
> **還不能直接 ACCEPT。**

因為 Change 沒有符合我們事先定義的完整 Done。

### 8. 建立 DONE 公式

```text
DONE
=
REQUIREMENTS SATISFIED
+
ACCEPTANCE CRITERIA PASSED
+
NO UNACCEPTABLE SIDE EFFECTS
+
HUMAN REVIEWED EVIDENCE
```

### 9. Traceability 概念
不深入工具，只建立鏈：

```text
WHY
 ↓
REQUIREMENT
 ↓
ACCEPTANCE CRITERION
 ↓
IMPLEMENTATION
 ↓
EVIDENCE
```

教師：
> 如果一個 Change 可以從「為什麼」一路追到「證據」，它就比一句 `Done!` 可靠得多。

### 10. 學生活動
每組拿自己的 Lab Evidence，完成 Verification Matrix。禁止只填 PASS；Evidence 欄必須說明依據。

### 11. 常見誤解
**AC 是老師打分表。**
修正：AC 首先是工程團隊在實作前定義的 Done。

**所有 AC 都 PASS 就完全沒有風險。**
修正：AC 只能驗證已定義條件；所以 DEFINE 品質本身也很重要。

### 12. 板書
```text
SPEC DEFINES DONE.
EVIDENCE PROVES DONE.
```

繁中：
> **規格定義完成；證據證明完成。**

### 13. 本頁帶走能力
學生能：
1. 為每個 AC 找對應 Evidence。
2. 不把 Feature Works 當作 Change Accepted。
3. 建立基本 Traceability 思維。

### 14. 銜接 S23
> 現在 Evidence 都在桌上。最後一個問題不是 AI 回答，而是人類回答：我們要不要接受這個 Change？

建議時間：10–12 分鐘。

---

# Slide 23 — Human Decision
## ACCEPT / REVISE / REJECT

### 1. 教學目的
完成 Human-in-the-loop 閉環。學生學會工程決策不是二元的「成功/失敗」，而是根據 Evidence 做 ACCEPT、REVISE、REJECT。

### 2. 主標題
**HUMAN DECISION**

副標：
> **AI 可以實作與提出證據，人類負責最後的接受決策。**

### 3. 主視覺

```text
             EVIDENCE
                ↓
          HUMAN REVIEW
                ↓
     ┌──────────┼──────────┐
     ↓          ↓          ↓
   ACCEPT     REVISE     REJECT
   接受       修正        拒絕
```

### 4. 三種決策定義

**ACCEPT**
```text
Spec satisfied
AC passed
Evidence sufficient
No unacceptable change
```

**REVISE**
```text
方向正確
但仍有可修正問題
→ 回到 Plan / Implement / Verify
```

**REJECT**
```text
方向錯誤
重大 Scope violation
或 Change 不應被保留
```

### 5. 煥哥角色
**FINAL CHANGE APPROVER（最終變更核准者）**。

桌面上有 Spec、Diff、Test、AC Matrix；不是憑感覺按 Approve。

### 6. 教師講稿
> Human Review 不是「我覺得不錯」。我們的判斷必須建立在前面蒐集的 Evidence 上。

> 所以 Human-in-the-loop 不是把人放在流程最後當橡皮圖章，而是讓人真正掌握 Intent、Scope 與 Acceptance。

### 7. 三個案例

#### Case A — ACCEPT
```text
Only required files changed
All AC PASS
No unnecessary dependency
Existing behavior works
```

答案：ACCEPT。

#### Case B — REVISE
```text
Feature works
But unnecessary package added
AC-05 FAIL
```

答案：REVISE。

要求 AI 移除不必要 dependency，再 Run/Test/Verify。

#### Case C — REJECT
```text
Dashboard redesigned
API changed
Database changed
FastAPI upgraded
Original request was only Last Updated
```

答案：REJECT，因為 Change 已嚴重偏離 Spec。

### 8. Verification Loop
正式畫出：

```text
SPEC
 ↓
PLAN
 ↓
IMPLEMENT
 ↓
VERIFY
 ↓
HUMAN DECISION
 ↓
ACCEPT ─────────→ REMEMBER
 ↓
REVISE
 ↓
PLAN / IMPLEMENT / VERIFY AGAIN
```

Reject 可回到重新定義或放棄 Change。

### 9. 關鍵觀念：人類不是一定要手寫 Code
教師：
> 在 AI-assisted Engineering 裡，人類價值不只等於「自己敲多少行 Code」。

人類責任：
```text
DEFINE INTENT
CONTROL SCOPE
REVIEW PLAN
INTERPRET EVIDENCE
MAKE DECISION
```

這是 L2 很重要的 AI 時代工程角色轉變。

### 10. 小組決策活動
教師給 3 張 Change Evidence Card。每組必須：
1. 選 ACCEPT / REVISE / REJECT。
2. 指出至少兩項 Evidence。
3. 說明理由。

禁止答案只有「我覺得」。

### 11. Verification Checklist 收束

```text
1. WHAT CHANGED?
   → Changed Files

2. EXACTLY HOW?
   → Diff

3. DOES IT WORK?
   → Run / Test

4. DOES IT MATCH SPEC?
   → Acceptance Criteria

5. SHOULD WE ACCEPT?
   → Human Decision
```

### 12. 常見誤解
**Human Review = 人一定比 AI 懂所有 Code。**
修正：不是。Human Review 的核心是責任與決策；必要時也可用更多工具取得證據。

**REVISE = AI 失敗。**
修正：不是。Iterative revision 本來就是工程流程。

### 13. 板書
```text
NO EVIDENCE → NO ACCEPT
```

```text
AI PROPOSES.
TOOLS PROVIDE EVIDENCE.
HUMAN DECIDES.
```

繁中：
> **AI 提案，工具提供證據，人類做決策。**

### 14. 本頁帶走能力
學生能：
1. 依 Evidence 做 ACCEPT / REVISE / REJECT。
2. 說明 Human-in-the-loop 的真正角色。
3. 理解 Verification 是可重複循環，不是一次性的 Done。

### 15. Part D 收尾講稿
> 到現在，我們終於可以說：這個 Change 不只是「AI 寫完了」，而是「我們驗證過了」。

> 但是還有一個問題：如果今天驗證完成，下星期我們還記得嗎？如果三個月後想知道為什麼改這一段，去哪裡找？

揭示下一層：

```text
DEFINE ✓
BUILD  ✓
VERIFY ✓
REMEMBER ← NEXT
```

### 16. 銜接 Slide 24
下一頁：
**Software Needs Memory — 軟體需要記憶**

建議時間：10–12 分鐘。

---

# Part D 完成檢查

完整 VERIFY 流程：

```text
AI SUMMARY
    ↓
CHANGED FILES
    ↓
DIFF
    ↓
RUN / TEST
    ↓
ACCEPTANCE CRITERIA
    ↓
HUMAN DECISION
    ↓
ACCEPT / REVISE / REJECT
```

學生應能完整說明：

> **AI 的 Done 是 Claim；工程上的 Done 需要 Evidence。**

以及：

> **SPEC DEFINES DONE. EVIDENCE PROVES DONE. HUMAN ACCEPTS DONE.**
>
> **規格定義完成，證據證明完成，人類決定接受。**

下一段：
```text
Part E — REMEMBER
S24–S27
Git + GitHub = Engineering Memory
```
