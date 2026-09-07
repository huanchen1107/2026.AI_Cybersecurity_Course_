# AIIS_L2 — 逐頁詳細教學稿 S07–S12
## Part B — DEFINE：把需求定義成可驗收的 Change

狀態：CANONICAL — L1 STYLE — 2026-09-07

統一格式：**目的 → 投影片內容 → 視覺 → 煥哥 → 老師講稿 → 問答 → 核心句 → Transition**。

---

# Slide 07 — 真實需求來了

## 目的
讓學生從抽象的 Spec 概念回到一個真實 User Problem，建立 `PROBLEM → NEED → CHANGE`，避免一看到需求就直接跳 Code。

## 投影片內容
上方使用者泡泡：
```text
「我怎麼知道現在看到的
氣象資料是什麼時候更新的？」
```
中央：
```text
PROBLEM
資料新鮮度不清楚
      ↓
NEED
讓使用者看見更新時間
      ↓
CHANGE
add-weather-last-updated
```
底部：
```text
START WITH THE PROBLEM, NOT THE CODE.
```

## 視覺
左側是 Weather Security Center 畫面，使用者盯著氣象數字旁的問號。右側三張卡：Problem → Need → Change。此頁不出現程式碼。

## 煥哥
表情：傾聽、理解使用者。
動作：先指 User，再指 Change Card，而不是指 Code。
角色：PRODUCT / CHANGE OWNER。

## 老師講稿
現在真正的需求來了。

使用者不是來跟你說：
> 請在 HTML 某個 div 加一個 timestamp。

他真正的問題是：
> 我怎麼知道現在看到的資料是不是新的？

工程師第一件事不是猜 Implementation，而是把使用者問題整理成一個可以管理的 Change。

所以今天我們只做一個 Change：
```text
add-weather-last-updated
```

## 問
「資料不新鮮」和「使用者不知道資料什麼時候更新」是同一個問題嗎？

預期答案：不一定。現在的 Need 是可見性，不代表我們已證明資料來源本身有問題。

## 核心句
> **PROBLEM → NEED → CHANGE**
> **先理解問題，再定義變更。**

## Transition
> 有了 Change 名稱還不夠。接下來要把這次工程工作完整裝進一個可以追蹤的單位。

下一頁：**Change = A Unit of Engineering Work。**

---

# Slide 08 — Change = 一個工程工作單位

## 目的
讓學生理解 OpenSpec Change 不是單純 Prompt、File 或 Code，而是把 WHY、邊界、需求與 Done 綁在一起的工程管理單位。

## 投影片內容
中央巨大卡片：
```text
CHANGE
add-weather-last-updated
```
四個角落：
```text
WHY
SCOPE
REQUIREMENTS
DONE
```
底部：
```text
PROMPT ≠ CHANGE
FILE ≠ CHANGE
CODE ≠ CHANGE
```

## 視覺
一張 Change Folder / Engineering Work Card，四個資訊模組環繞。不要展示 OpenSpec 目錄語法。

## 煥哥
表情：整理、管理。
動作：把零散 Request、Notes、Criteria 收進同一個 Change Folder。
角色：CHANGE MANAGER。

## 老師講稿
為什麼不直接說「我要改 index.html」？

因為 File 只是實作的一部分。

一個 Change 應該回答：
- 為什麼要做？
- 做到哪裡？
- 系統應做到什麼？
- 怎樣才算完成？

未來可能一個 Change 只改一個 File，也可能合理地改三個 File。真正管理的是「工程意圖」，不是檔名。

## 問
如果 AI 改了三個 Files，這是三個 Change 嗎？

預期答案：不一定。同一個 Change 可以有多個必要的 File modifications。

## 核心句
> **MANAGE THE CHANGE, NOT JUST THE FILES.**
> **我們管理的是變更，不只是檔案。**

## Transition
> 那一個 Change 最先要寫什麼？不是 How，而是 WHY。

下一頁：**WHY / NEED。**

---

# Slide 09 — WHY：為什麼要改？

## 目的
教學生先保存 Engineering Intent，避免把 Implementation 當成 Need。

## 投影片內容
中央：
```text
WHY
↓
WHAT
↓
HOW
```
右側對比：
```text
✕ Add a timestamp div.

✓ Users should know when
  weather data was refreshed.
```
底部：
```text
WHY ≠ IMPLEMENTATION
```

## 視覺
WHY 位於流程最上方且最大；HOW 放最下面且較淡。Bad/Good 例子只各一個。

## 煥哥
表情：追問原因。
動作：拿著 WHY 放大鏡，不讓 AI 直接衝到 HOW。
角色：REQUIREMENT INVESTIGATOR。

## 老師講稿
很多工程文件第一句就開始寫：
> Add a timestamp div to index.html.

這其實已經在講 How。

但真正值得保存的是：
> Users should know when the displayed weather data was last refreshed.

因為未來 UI 改版、Framework 改變，How 可能變；但 WHY 還是可以幫助下一個工程師理解當初為什麼有這個 Change。

## 問
下面哪個比較像 WHY？

A. Add `last_updated()` function.

B. 使用者需要判斷畫面資料的新鮮度。

預期：B。

## 核心句
> **WHY → WHAT → HOW**
> **先保存意圖，再決定做法。**

## Transition
> WHY 清楚之後，下一個問題是：這次到底做到哪裡就停？

下一頁：**Scope / Out of Scope。**

---

# Slide 10 — SCOPE：這次做到哪裡？

## 目的
建立清楚的 Change Boundary，第一次正式讓學生看懂 Scope Creep。

## 投影片內容
中央一條邊界線。

左側：
```text
IN SCOPE ✓
Show Last Updated
Reuse existing time data
Keep weather display working
```
右側：
```text
OUT OF SCOPE ✕
Authentication
Database redesign
API redesign
New unnecessary dependency
```
底部：
```text
A GOOD CHANGE HAS BOUNDARIES.
```

## 視覺
像一道清楚的圍牆／邊界。需求內的卡片在框內，額外工作在框外。可有一個 `Scope Creep` 小怪獸試圖把額外卡片推進框內。

## 煥哥
表情：堅定。
動作：站在 Scope Gate 前，一手放行 Last Updated，一手擋住 unrelated refactor。
角色：SCOPE GATEKEEPER。

## 老師講稿
Scope 不只是「要做什麼」。

Out of Scope 一樣重要，因為它明確告訴 AI：
> 這些事情今天不要順便做。

例如 Authentication 很重要嗎？重要。

API redesign 有沒有可能未來需要？有。

但今天的 Change 是 `add-weather-last-updated`，所以它們不是這次的工作。

這就是控制 Scope Creep。

## 問
如果 AI 說：「為了程式更乾淨，我順便重構整個 Weather Service。」

要立刻接受嗎？

預期：不。先看它是否必要且在核准 Scope 內。

## 核心句
> **OUT OF SCOPE DOES NOT MEAN UNIMPORTANT. IT MEANS NOT THIS CHANGE.**
> **Out of Scope 不是不重要，而是不是這一次。**

## Transition
> 邊界畫好後，我們要把使用者的 Request 轉成系統真正應做到的事情。

下一頁：**Requirements。**

---

# Slide 11 — REQUIREMENTS：系統應做到什麼？

## 目的
區分自然語言 Request 與可檢查的 System Requirements。

## 投影片內容
左側：
```text
REQUEST
「讓我知道資料什麼時候更新」
```
箭頭到右側三張卡：
```text
REQ-01
Dashboard 顯示 Last Updated

REQ-02
時間資訊清楚可讀

REQ-03
既有 Weather Display 保持運作
```
底部：
```text
REQUEST = 人想要什麼
REQUIREMENT = 系統應做到什麼
```

## 視覺
一個使用者對話泡泡，經過「Translate」漏斗，變成三張結構化 Requirement Cards。

## 煥哥
表情：分析、翻譯需求。
動作：把 User Request 轉換成 Requirement Cards。
角色：REQUIREMENT TRANSLATOR。

## 老師講稿
使用者通常不會替我們寫完整 Requirement。

他只會說：「我想知道資料什麼時候更新。」

工程師要把它翻成系統可理解、可檢查的要求。

好的 Requirement 至少要做到三件事：
```text
CLEAR
RELEVANT
CHECKABLE
```
這三個字可口頭說，不必全部擠進投影片。

注意 REQ-03：新功能不能把原本 Weather Display 弄壞。這就是我們開始建立 Regression 思維，但詳細測試留到 VERIFY。

## 問
「Make the dashboard better」是不是好 Requirement？

預期答案：不是，太模糊，不容易驗證。

## 核心句
> **TURN REQUESTS INTO CHECKABLE REQUIREMENTS.**
> **把人說的需求，轉成系統可檢查的要求。**

## Transition
> Requirement 告訴我們系統應做到什麼；但還缺最後一件事：到底怎樣才算 Done？

下一頁：**Acceptance Criteria。**

---

# Slide 12 — ACCEPTANCE CRITERIA：誰定義 Done？

## 目的
完成 DEFINE 階段。讓學生在 AI 寫 Code 之前，就先看到一份清楚的 Definition of Done。

## 投影片內容
中央五個**尚未打勾**的 Checkbox：
```text
□ AC-01  Dashboard 顯示 Last Updated
□ AC-02  時間資訊清楚可讀
□ AC-03  Weather Display 仍正常
□ AC-04  Existing API behavior 未被刻意改變
□ AC-05  沒有新增不必要 Dependency
```
中央下方巨大：
```text
WHO DEFINES DONE?
THE SPEC.
```
底部：
```text
AI DOES NOT DEFINE DONE.
THE SPEC DEFINES DONE.
```

## 視覺
這頁就是一張乾淨的 Acceptance Checklist。所有 Checkbox 故意保持空白。右下角小字標示：`We will return here in S22.`

## 煥哥
表情：正式、明確。
動作：拿著尚未勾選的 Checklist，另一手阻止 AI 提前打綠色 Done。
角色：ACCEPTANCE OWNER。

## 老師講稿
這頁非常重要。

注意：現在 AI 還沒有開始寫 Code，但我們已經先決定什麼叫完成。

如果沒有 Acceptance Criteria，最後就會變成：
> AI 覺得完成了。
> 我看起來好像可以。
> 那就算 Done 吧。

這不是工程驗收。

今天這五個 Checkbox 現在一個都不要打勾。

等到 S22，我們會拿真正的 Evidence 回來，一條一條決定能不能勾。

這形成一個很重要的閉環：
```text
DEFINE DONE FIRST
        ↓
BUILD
        ↓
VERIFY DONE LATER
```

## 問
如果 Last Updated 已經顯示，但 AI 順便新增一個不必要 Package，算不算完成？

預期：不能直接算，因為 AC-05 可能 FAIL。

## 核心句
> **DEFINE DONE BEFORE YOU BUILD.**
> **先定義完成，再開始建構。**

## Transition
> 到這裡 DEFINE 完成。

```text
WHY ✓
SCOPE ✓
REQUIREMENTS ✓
ACCEPTANCE CRITERIA ✓
```

接下來才進 BUILD。

下一頁：**Slide 13 — 把 Project + Spec 一起交給 AI。**
