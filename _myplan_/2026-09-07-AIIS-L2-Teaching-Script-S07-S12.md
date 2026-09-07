# AIIS_L2 — 詳細教學講稿 S07–S12
## Part B — DEFINE：把需求定義成可驗收的 Change

狀態：PART B — CANONICAL zh-TW REFINEMENT — 2026-09-07
課程位置：L2 / MANAGE

> **本段只做 DEFINE，不寫 Code。**

```text
DEFINE → BUILD → VERIFY → REMEMBER
  ↑
現在
```

每頁只回答一個問題：
```text
S07 從哪個 Problem 開始？
S08 這次工程工作如何被管理？
S09 WHY 是什麼？
S10 邊界在哪裡？
S11 系統應做到什麼？
S12 怎樣才算 Done？
```

---

# Slide 07 — 真實需求來了
## 從使用者 Problem 開始，不從 Code 開始

### 這頁在做什麼
把抽象 Spec 落到 Weather Security Center，第一次看到本課唯一代表性 Change。

### ON SLIDE
```text
使用者：
「我不知道現在看到的氣象資料
是剛更新的，還是一小時以前的。」
        ↓
NEED
知道資料最後更新時間
        ↓
CHANGE
add-weather-last-updated
```

> **PROBLEM → NEED → CHANGE**

### 視覺
Weather Security Center + 使用者對話泡泡；不要出現 Code。

### 煥哥角色
**需求接收者**，認真聽需求而不是急著敲鍵盤。

### 教師講稿
> 現在真的開始做一次 Change，但第一個動作不是叫 AI 寫 Code。

問：
> 使用者真正的問題是「缺一個文字欄位」，還是「無法判斷資料新鮮度」？

引導學生先看 Problem，再看解法。

### 學生只需帶走
> **工程 Change 從 Problem 與 Need 開始，不從 Implementation 開始。**

### 銜接 S08
> 我們替它取名 `add-weather-last-updated`。但 Change 不只是一個名稱。

建議時間：6–8 分鐘。

---

# Slide 08 — Change 是工程工作的管理單位
## 不只是 Prompt，也不只是某一個 File

### 這頁在做什麼
建立 Change 概念：把需求、邊界、實作、驗證與歷史視為同一件工程工作。

### ON SLIDE
中央大卡：
```text
add-weather-last-updated
```
周圍四個標籤：
```text
WHY
SCOPE
REQUIREMENTS
DONE
```

> **CHANGE = 可被定義、實作、驗證、保存的工程工作單位。**

### 視覺
一個大型 Change Folder；不要塞完整生命週期。

### 煥哥角色
**Change Owner（變更負責人）**。

### 教師講稿
> AI 寫 Code 可能只花五分鐘，但真正的 Change 還包括為什麼做、做到哪裡、怎麼知道做對，以及最後怎麼留下歷史。

```text
PROMPT ≠ CHANGE
FILE   ≠ CHANGE
CODE   ≠ CHANGE
```

### 學生只需帶走
> 我們管理的不是一段 Prompt，而是一個完整 Change。

### 銜接 S09
> Change 裡第一個要寫的不是 HOW，而是 WHY。

建議時間：6–7 分鐘。

---

# Slide 09 — WHY / NEED
## 先說為什麼，不要先決定怎麼寫

### 這頁在做什麼
建立 `WHY → WHAT → HOW` 順序，避免把實作方法誤寫成需求。

### ON SLIDE
```text
WHY
為什麼需要？
 ↓
WHAT
需要什麼行為？
 ↓
HOW
最後才決定怎麼做
```

❌ `在 index.html 加 timestamp div`

✓ `使用者無法判斷氣象資料的新鮮度`

> **先理解 Problem，再決定 Solution。**

### 煥哥角色
**Problem Framer（問題定義者）**。

### 教師講稿
> 第一個句子已經偷偷決定 HTML、div 和 timestamp，這是 HOW；第二句才描述真正 Problem。

本次 WHY：
```text
使用者目前無法從 Weather Dashboard
判斷氣象資料最後更新時間，
因此需要清楚的更新時間資訊。
```

### 快問
A 使用者不知道資料是否新鮮。
B 加 `<span>`。
C 使用 datetime。
D 修改 CSS。

哪一個是 WHY？→ A。

### 板書
```text
WHY ≠ IMPLEMENTATION
```

### 學生只需帶走
> **不要在 WHY 裡偷塞 HOW。**

### 銜接 S10
> 知道為什麼要改後，下一題是：這次到底允許改到哪裡？

建議時間：7–8 分鐘。

---

# Slide 10 — Scope / Out of Scope
## 不只定義要做什麼，也定義這次不做什麼

### 這頁在做什麼
教 Change Control 的邊界概念，避免 Scope Creep。

### ON SLIDE
```text
IN SCOPE
✓ 顯示 Last Updated
✓ 優先重用既有時間資訊
✓ 保持原 Weather Display 正常

OUT OF SCOPE
✕ Authentication
✕ Database redesign
✕ API redesign
✕ Unnecessary dependency
✕ Unrelated refactor
```

> **清楚邊界，降低 AI 不必要的猜測。**

### 視覺
一個 Scope 邊界框；框內 3 項、框外 4–5 項。

### 煥哥角色
**Boundary Keeper（範圍守門員）**。

### 教師講稿
> AI 有時很積極。你叫它改善一件事，它可能順便 Refactor、Upgrade、Redesign。

問：
> 這是貼心，還是風險？

引出 Scope Creep：未經同意逐漸加入原本沒要求的工作。

### 快速活動
- 顯示更新時間 → IN
- 必要小幅 CSS → IN
- 升級 FastAPI → OUT
- 改登入 → OUT
- 重設 Dashboard → OUT

### 核心句
> **好的 Spec 不只說要做什麼，也說這次不要做什麼。**

### 銜接 S11
> 邊界畫好了，現在把 Need 寫成系統應具備的行為。

建議時間：8–9 分鐘。

---

# Slide 11 — Requirements
## 把 Need 轉成系統應具備的行為

### 這頁在做什麼
區分 Request 與 Requirement，讓口語願望變成可實作、可檢查的系統行為。

### ON SLIDE
```text
REQUEST
「我想知道資料什麼時候更新。」
       ↓
REQUIREMENTS
REQ-01 顯示最後更新時間
REQ-02 顯示位置清楚可見
REQ-03 保持既有氣象資訊正常
```

> **REQUEST = 人想要什麼**
> **REQUIREMENT = 系統應做到什麼**

### 視覺
一個使用者泡泡轉成三張 REQ 卡。

### 煥哥角色
**Requirement Writer（需求撰寫者）**。

### 教師講稿
> 使用者通常只會說：「我想知道資料是不是新的。」我們把它轉成系統應具備的行為，但不要過度指定實作。

比較：
```text
不好：Use Python datetime and add a gray span.
較好：Dashboard shall display a readable last-updated time.
```

### Requirement 三檢查
```text
CLEAR      清楚
RELEVANT   與 Need 有關
CHECKABLE  可以檢查
```

### 學生只需帶走
> Requirement 定義「系統應做到什麼」，不是指定 AI 一定怎麼寫。

### 銜接 S12
> Requirements 說明應做到什麼，但做到什麼程度才算完成？

建議時間：7–9 分鐘。

---

# Slide 12 — Acceptance Criteria
## 在寫 Code 前，先定義 Done

### 這頁在做什麼
完成 DEFINE。Acceptance Criteria（驗收條件）在實作前先定義，S22 再逐條回來驗證。

### ON SLIDE
```text
AC-01 看得到 Last Updated
AC-02 時間清楚可讀
AC-03 Weather Data 仍正常
AC-04 Existing API behavior 未刻意改變
AC-05 無不必要 Dependency
```

> **WHO DEFINES DONE? → THE SPEC.**
> **誰定義完成？→ Spec。**

### 視覺
五個空白 Checkbox。此刻不要打勾，因為還沒實作。

### 煥哥角色
**Acceptance Designer（驗收設計者）**。

### 教師講稿
> 現在一行 Code 都還沒有改，我們就先把 Done 寫下來。如果等 AI 寫完，再由 AI 自己告訴我們什麼叫完成，它同時成了選手和裁判。

認知衝突：
```text
Last Updated ✓
Weather Data ✓
但新增不必要 Dependency ✕
```

問：
> Feature 能跑，算 Done 嗎？

答案：還不能接受，AC-05 沒通過。

### DONE 簡版
```text
DONE
= Required behavior works
+ Acceptance Criteria pass
+ No unacceptable side effects
```

### 核心句
> **AI DOES NOT DEFINE DONE. THE SPEC DEFINES DONE.**
> **AI 不自行宣布完成；Spec 先定義完成。**

### Part B 收束
```text
PROBLEM → CHANGE → WHY → SCOPE → REQUIREMENTS → AC
```

> **DEFINE BEFORE YOU BUILD.**
> **先定義，再建構。**

### 銜接 S13
> DEFINE 完成。現在才把 Project + Spec 交給 Antigravity，進入 BUILD。

建議時間：9–10 分鐘。
