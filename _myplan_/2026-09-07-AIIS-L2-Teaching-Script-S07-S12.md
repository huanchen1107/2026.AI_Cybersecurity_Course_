# AIIS_L2 — 教學講稿 S07–S12
## Part B — 我們的第一個 OpenSpec Change

狀態：PART B TEACHING SCRIPT COMPLETE — 2026-09-07
課程位置：L2 / MANAGE
語言規則：**繁體中文為主；必要資訊工程術語保留英文，第一次出現時搭配中文解釋。**

本段延續 S01–S06：

```text
DEFINE → BUILD → VERIFY → REMEMBER
定義 → 建構 → 驗證 → 留存
```

Part B 專注第一層：

> **DEFINE — 用 OpenSpec 把需求變成可管理的工程變更。**

本段使用同一個 L1 Weather Security Center，不建立新 App。

---

# Slide 07 — A Real Request Arrives
## 真實需求來了

### 本頁目的
把前面抽象的「Spec」落到真實情境。學生從使用者需求出發，而不是從程式碼或 OpenSpec 語法出發。

### 投影片核心

```text
使用者：
「我不知道現在看到的氣象資料
是剛剛更新的，還是一個小時以前的。」

        ↓

需求：
Add Last Updated
加入「最後更新時間」
```

底部：

> **先定義 Change，再開始寫 Code。**

### 視覺設計
左側：Weather Security Center 畫面。
右側：使用者對話泡泡。
中央箭頭把「使用者問題」轉成「工程變更需求」。

不要一開始就顯示程式碼。

### 煥哥角色
角色：**需求接收者（Requirement Receiver）**。

表情：認真聽使用者需求；手上不是鍵盤，而是一張需求卡。

### 教師講稿
> 現在我們真的開始做一次 Change。
>
> 但這一次跟 L1 不一樣。L1 我們很快把想法交給 AI 去 Build；今天第一個動作不是叫 AI 寫 Code。

指向使用者：

> 使用者真正的問題是什麼？

讓學生回答。

引導到：

> 使用者無法判斷目前畫面上的氣象資料到底有多新。

接著問：

> 所以使用者真正需要的是「一個時間文字」，還是「能判斷資料新鮮度」？

重點：不要過早把 Need 等同某個 UI 解法。

### 從 Problem 到 Change
板書：

```text
PROBLEM
看不出資料新鮮度
     ↓
NEED
知道資料何時更新
     ↓
CHANGE
add-weather-last-updated
```

教師：

> 我們給這個工程工作一個名字：`add-weather-last-updated`。
>
> 從現在開始，它不是聊天裡的一句話，而是一個可以被追蹤的 Change。

### 小問題
問學生：

> 如果明天有人問「為什麼要加 Last Updated？」你希望答案在哪裡？

引導：不應只存在昨天的聊天紀錄。

### 本頁帶走
1. 工程變更從使用者問題開始。
2. 不要一收到需求就直接跳到 Code。
3. 有意義的變更需要一個可追蹤的 Change identity。

> **PROBLEM → NEED → CHANGE**

### 銜接 S08
> Change 只是檔案名稱嗎？不是。它其實是我們接下來整個工程工作的「容器」。

下一頁：**Change = A Unit of Engineering Work**

建議時間：6–8 分鐘。

---

# Slide 08 — Change = A Unit of Engineering Work
## Change 是一個完整的工程工作單位

### 本頁目的
讓學生理解 Change 不是「一個 Prompt」、不是「一次 AI 對話」、也不是「一個檔案」，而是從需求到驗證證據的一個可管理工作單位。

### 核心圖

```text
                add-weather-last-updated
                         │
       ┌─────────────────┼─────────────────┐
       ↓                 ↓                 ↓
      WHY              SCOPE          REQUIREMENTS
       │                                   │
       └──────────────┬────────────────────┘
                      ↓
             ACCEPTANCE CRITERIA
                      ↓
                IMPLEMENTATION
                      ↓
                  EVIDENCE
```

### 核心句

> **Change = 可以被定義、實作、驗證、保存的一個工程工作單位。**

### 煥哥角色
角色：**Change Owner（變更負責人）**。

手上拿著 `add-weather-last-updated` 資料夾，裡面不是只有 Code，而是 WHY、Scope、Requirements、Acceptance Criteria。

### 教師講稿
> 我們平常很容易把「改程式」想成打開檔案、修改幾行 Code。
>
> 但在 AI Engineering 裡，AI 寫 Code 反而可能是最快的一段。

問：

> 如果 AI 五分鐘就能改完，那工程工作是不是只剩五分鐘？

引導：不是，還有定義、審查、測試、驗證與歷史。

### 三個不要混淆

```text
PROMPT ≠ CHANGE
FILE   ≠ CHANGE
CODE   ≠ CHANGE
```

Prompt 是互動方式；File 是實作載體；Code 是實作結果。

Change 則描述「這一次工程工作」本身。

### Change 的生命週期預覽

```text
REQUEST
  ↓
DEFINE
  ↓
IMPLEMENT
  ↓
VERIFY
  ↓
ACCEPT
  ↓
REMEMBER
```

提醒：這只是預覽，S13 之後才進入實作與驗證。

### 學期中的重複使用
簡短展示：

```text
L2  Feature Change
L4  Security Fix Change
L13 Security Repair Change
L15–16 Final Project Change History
```

教師：

> 所以今天不是為了 Last Updated 學一套只用一次的方法，而是在學一個整學期會重複使用的工程習慣。

### 本頁帶走
> **CHANGE IS THE UNIT OF ENGINEERING WORK.**
>
> **Change 是工程工作的基本管理單位。**

### 銜接 S09
> 有了 Change 名稱，第一個真正要寫的內容不是 HOW，而是 WHY。

建議時間：6–8 分鐘。

---

# Slide 09 — WHY / NEED
## 先說為什麼，不要先說怎麼改

### 本頁目的
建立 `WHY → WHAT → HOW` 思考順序，防止學生把實作方案誤寫成需求。

### 主畫面

```text
WHY
為什麼需要改？

↓

WHAT
系統需要具備什麼行為？

↓

HOW
最後才決定怎麼實作
```

大字：

> **WHY → WHAT → HOW**

### 好與不好的 Need

❌ 不好：
```text
修改 index.html，加入一個 timestamp div。
```

✅ 較好：
```text
使用者目前無法判斷畫面上的氣象資料
何時更新，因此無法判斷資料的新鮮度。
```

### 教師講稿
> 這兩句哪一句比較像需求？

讓學生比較。

> 第一個已經偷偷決定 HOW：index.html、div、timestamp。
>
> 第二個描述的是使用者真正遇到的問題。

### 為什麼 WHY 很重要
如果一開始就寫 HOW：

```text
Need:
Add a timestamp div to index.html.
```

AI 可能不再檢查：
- 原本資料是否已經有 update time；
- 是否有更簡單的呈現方式；
- 這是不是正確的檔案；
- 是否需要 backend 改動。

教師：

> **太早決定 HOW，會限制我們理解真正的 Problem。**

### 本次 Change 的 WHY

```text
Change:
add-weather-last-updated

Need / Why:
使用者目前無法從 Weather Dashboard
判斷氣象資料最後更新的時間。

因此需要提供清楚、可讀的更新時間資訊，
讓使用者能判斷目前資料的新鮮度。
```

### 課堂快問快答
判斷哪個是 WHY：

A. 使用者不知道資料是否新鮮。
B. 在 HTML 加 `<span>`。
C. 使用 Python datetime。
D. 修改 CSS 成灰色字。

答案：A。

### 煥哥角色
角色：**Problem Framer（問題定義者）**。

指向使用者問題，而不是程式碼。

### 板書

```text
WHY ≠ IMPLEMENTATION
```

```text
Problem first.
Solution later.
```

可搭配繁中：

> **先理解問題，再決定解法。**

### 本頁帶走
1. Need / Why 描述問題與價值。
2. 不要在 WHY 裡偷塞實作方法。
3. AI 可以協助想 HOW，但人必須先確認 WHY。

### 銜接 S10
> 知道為什麼要改之後，下一個問題是：到底允許改到哪裡？

下一頁：**Scope / Out of Scope**

建議時間：7–9 分鐘。

---

# Slide 10 — SCOPE / OUT OF SCOPE
## 不只告訴 AI 要做什麼，也要告訴它不要做什麼

### 本頁目的
正式教 Scope（範圍）與 Out of Scope（排除範圍），建立 AI Change Control 與最小必要變更思維。

### 主畫面
中間是一個邊界框：

```text
┌────────────── IN SCOPE ──────────────┐
│ 顯示 Last Updated                    │
│ 使用既有時間資訊（若可用）          │
│ 保持資訊清楚可讀                     │
└──────────────────────────────────────┘

          OUT OF SCOPE
          ✕ Authentication
          ✕ Database schema
          ✕ API redesign
          ✕ New dependency
          ✕ Unrelated refactor
```

### 核心句

> **好的 Spec 不只告訴 AI 要做什麼，也告訴 AI 這次不要做什麼。**

### 教師講稿
> AI Agent 有一個很有趣的特性：你叫它改善一件事，它有時會順便幫你改善另外五件事。

問學生：

> 這叫貼心，還是風險？

答案：視情況；未經同意的額外變更就是需要審查的 Scope Creep（範圍蔓延）。

### 本次 Change 的 Scope

```text
Scope:
- 在 Dashboard 顯示 Last Updated。
- 優先重用現有氣象資料中的時間資訊。
- 顯示方式需清楚、可讀。
- 保持既有 Weather Display 正常運作。
```

### Out of Scope

```text
Out of Scope:
- 不修改 Authentication。
- 不修改 Database Schema。
- 不重新設計 API。
- 不新增不必要的 Dependency。
- 不做與需求無關的 Refactor。
```

### 為什麼 Out of Scope 對 AI 特別重要
傳統工程師通常會靠團隊背景理解邊界；AI Agent 可能會依自己的推理補足模糊處。

因此：

```text
AMBIGUITY
   ↓
AI ASSUMPTION
   ↓
UNEXPECTED CHANGE
```

Spec 的作用是降低不必要的猜測空間。

### 迷你判斷活動
需求：`Add Last Updated`

教師逐項念，學生回答 IN / OUT：
- 顯示更新時間 → IN
- 重用既有 timestamp → IN
- 把 FastAPI 升級最新版 → OUT
- 改登入流程 → OUT
- 重新設計整個 Dashboard → OUT
- 必要的小幅 CSS 調整 → 可能 IN，需有理由

這個「可能」很重要：Scope 不是機械式檔案白名單，而是與需求有合理關係的邊界。

### 煥哥角色
角色：**Boundary Keeper（範圍守門員）**。

站在 Scope 邊界旁，把「API redesign」「dependency upgrade」擋在外面。

### 板書

```text
IN SCOPE = 這次要完成
OUT OF SCOPE = 這次刻意不碰
```

```text
MORE CHANGES ≠ BETTER ENGINEERING
```

### 本頁帶走
1. Scope 定義這次 Change 的邊界。
2. Out of Scope 主動限制不必要的 AI 擴張。
3. 額外改動不是自動等於價值。

### 銜接 S11
> 有了 WHY 和邊界，現在要把「系統應該做到什麼」寫成更精確的 Requirements。

建議時間：8–10 分鐘。

---

# Slide 11 — REQUIREMENTS
## 把「我想要」變成「系統應該做到」

### 本頁目的
區分 Request（請求）與 Requirement（需求規格）。教學生以可理解、可檢查的系統行為描述需求，而不是堆技術細節。

### 主畫面

```text
REQUEST
「幫我加 Last Updated」
        ↓
REQUIREMENTS
REQ-01
REQ-02
REQ-03
```

### Request vs Requirement

```text
REQUEST
人想要什麼
通常自然、口語、可能模糊

REQUIREMENT
系統應該具備什麼行為
較明確、可追蹤、可驗證
```

### 本次 Requirements

```text
REQ-01
Weather Dashboard 應顯示
最新氣象資料的更新時間。

REQ-02
更新時間應顯示在
與氣象資訊容易建立關聯的位置。

REQ-03
加入更新時間後，
既有氣象資訊顯示功能仍應正常運作。
```

### 教師講稿
> Request 是：「我想要 Last Updated。」
>
> Requirement 則要回答：「完成之後，系統應該呈現什麼行為？」

強調 Requirement 不必寫成程式碼。

### Shall / 應
可以介紹工程文件常見語氣：

```text
The system shall...
系統應……
```

但不要把本課變成 Requirements Engineering 文法課。

### 好 Requirement 的三個簡單原則

```text
CLEAR      清楚
RELEVANT   與需求相關
CHECKABLE  可以檢查
```

### 壞例子

```text
REQ-X
Make the dashboard awesome.
讓 Dashboard 更棒。
```

問：怎麼判斷「更棒」？

另一個壞例子：

```text
REQ-X
Use package X version Y and rewrite the backend.
```

如果這不是必要 constraint，它可能只是過早指定 HOW。

### 小活動
把下面 Request 改寫成 Requirement：

> 「時間要讓我看得懂。」

可能答案：

> 更新時間應以使用者可讀的格式顯示。

不追求唯一答案，重點是從願望轉成可檢查的系統行為。

### 煥哥角色
角色：**Requirement Writer（需求規格撰寫者）**。

將一張口語 Request 卡整理成 REQ-01、REQ-02、REQ-03。

### 板書

```text
REQUEST = 人想要什麼
REQUIREMENT = 系統應做到什麼
```

### 本頁帶走
1. Request 可以模糊，Requirement 必須更精確。
2. Requirement 描述預期系統行為。
3. Requirement 要能在後面被驗證。

### 銜接 S12
> Requirement 寫好了，但最後還有一個很關鍵的問題：到底怎樣才算完成？

下一頁：**Acceptance Criteria = Definition of Done**

建議時間：7–9 分鐘。

---

# Slide 12 — ACCEPTANCE CRITERIA = DEFINITION OF DONE
## 驗收條件：在 AI 寫 Code 之前先定義「完成」

### 本頁目的
建立整個 L2 最重要的工程控制概念之一：完成標準必須在實作前定義，而且最後可以用 PASS / FAIL 檢查。

### 核心句

> **AI DOES NOT DEFINE DONE. THE SPEC DEFINES DONE.**
>
> **不是 AI 說 Done 就算完成；完成標準由 Spec 事先定義。**

### 主畫面

```text
AC-01  Dashboard 顯示 Last Updated       PASS / FAIL
AC-02  時間格式清楚可讀                  PASS / FAIL
AC-03  Weather Data 仍正常顯示           PASS / FAIL
AC-04  Existing API behavior 未刻意改變  PASS / FAIL
AC-05  沒有新增不必要 Dependency         PASS / FAIL
```

### 教師講稿
> AI 最常講的一句話是什麼？

可能學生回答：Done、Completed、Implemented。

教師：

> 那 AI 說 Done，我們就可以交作業嗎？

答案：不行。

> 因為「Done」不是 AI 的感覺，而是一組我們事先同意的驗收條件。

### Acceptance Criteria 是什麼

> **Acceptance Criteria（驗收條件）= 用來判斷這次 Change 是否達到要求的可檢查條件。**

每一條最好能回答：

```text
PASS ?
FAIL ?
```

### Requirement 與 Acceptance Criteria 的關係

```text
REQUIREMENT
系統應顯示更新時間
       ↓
ACCEPTANCE CRITERIA
畫面上可以實際看到 Last Updated → PASS/FAIL
```

Requirement 說「應該做到什麼」。
Acceptance Criteria 說「怎麼判斷真的做到了」。

### 特別強調 AC-05

```text
AC-05
沒有新增不必要 Dependency
```

教師：

> 假設 Last Updated 正常出現，但是 AI 順便加了三個根本不需要的套件。功能有沒有成功？可能有。
>
> Change 有沒有通過？不一定，因為它違反我們的完成標準。

建立：

```text
FEATURE WORKS
     ≠
CHANGE ACCEPTED
```

### Definition of Done

```text
DONE
=
Requirements satisfied
+
Acceptance Criteria passed
+
No unacceptable side effects
+
Human reviewed evidence
```

這裡只建立概念；S19–S23 才詳細教 Evidence 與 Human Decision。

### 迷你活動：哪一個是真的 Done？

A：AI 說 Done，但沒 Run。

B：畫面有 Last Updated，但 Weather Data 壞掉。

C：功能正常、所有 AC PASS、沒有非預期變更、Human Review 通過。

答案：C。

### 煥哥角色
角色：**Acceptance Judge（驗收判定者）**。

手持 PASS / FAIL Checklist，不接受 AI 單純遞來一張 `DONE!` 卡片。

### 板書

```text
AI says DONE ≠ DONE
```

```text
SPEC defines DONE
EVIDENCE proves DONE
HUMAN accepts DONE
```

第三句在後面 VERIFY Part 再深入。

### 本頁帶走
1. Acceptance Criteria 必須在實作前定義。
2. 每一條應盡量可判斷 PASS / FAIL。
3. 功能看起來能用，不等於 Change 已被接受。
4. AI 不能自行決定自己的工作已經完成。

### Part B 收束

```text
USER REQUEST
     ↓
OPENSPEC CHANGE
     ↓
WHY / NEED
     ↓
SCOPE / OUT OF SCOPE
     ↓
REQUIREMENTS
     ↓
ACCEPTANCE CRITERIA
     ↓
DEFINITION OF DONE
```

教師：

> 注意，到現在為止我們還沒有叫 AI 修改任何一個檔案。
>
> 但是我們已經把「想做什麼、為什麼做、不能亂動什麼、系統應該做到什麼、怎樣才算完成」全部定義清楚了。

最後揭示：

> **DEFINE BEFORE YOU BUILD.**
>
> **先定義，再建構。**

### 銜接 Part C / Slide 13
> 現在 Spec 已經準備好了。下一步才輪到 Antigravity。但這一次，我們不會只丟一句 Prompt 給 AI。

下一頁：

**Slide 13 — Give AI the Project + Spec, Not Just a Prompt**

建議時間：9–12 分鐘。

---

# Part B 完成檢查

```text
S07 真實使用者問題
 ↓
S08 建立 Change 工作單位
 ↓
S09 WHY / NEED
 ↓
S10 SCOPE / OUT OF SCOPE
 ↓
S11 REQUIREMENTS
 ↓
S12 ACCEPTANCE CRITERIA / DONE
```

Part B 完成後，學生應已能建立第一個最小 OpenSpec Change：

```text
Change: add-weather-last-updated

Need / Why:
使用者需要知道目前氣象資料最後更新的時間，
以判斷資料的新鮮度。

Scope:
- 顯示 Last Updated。
- 優先重用既有時間資訊。
- 保持既有 Weather Display 正常。

Out of Scope:
- Authentication
- Database Schema
- API redesign
- unnecessary dependency
- unrelated refactor

Requirements:
REQ-01 顯示最新資料更新時間。
REQ-02 更新時間清楚且容易與氣象資訊建立關聯。
REQ-03 既有氣象顯示功能維持正常。

Acceptance Criteria:
AC-01 Last Updated 可見。
AC-02 時間格式可讀。
AC-03 Weather Data 正常顯示。
AC-04 Existing API behavior 未被刻意改變。
AC-05 無不必要 Dependency。
```

下一個 Part 必須進入 BUILD，不再增加新的 DEFINE 概念：

```text
Part C — Antigravity Implements the Spec
S13–S18
```
