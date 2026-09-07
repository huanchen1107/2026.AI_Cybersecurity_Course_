# AIIS_L2 — L1 式逐頁詳細教學稿
# Slide 00 — MANAGE：從「AI 做得出來」到「我們管得住改變」

狀態：CANONICAL FINAL — L1 STYLE — 2026-09-07
語言：繁體中文為主

> Slide 00 是課程定位／封面頁，不占用 S01–S30 正式教學頁碼。

---

## 目的

把 L1 的 **BUILD** 自然接到 L2 的 **MANAGE**。

學生一開始就要知道：今天不建立另一個 App，也不是單純學 Git 指令，而是學習如何管理 AI 對既有 Weather Security Center 產生的一次真實 Change。

這頁只做課程定位；`DEFINE → BUILD → VERIFY → REMEMBER` 只 Preview，S06 才正式教。

---

## 投影片內容

主標題：
```text
AIIS_L2 — MANAGE
Spec-Driven AI Engineering
OpenSpec × Antigravity × Git × GitHub
```

中央階梯：
```text
L1 — BUILD IT ✓
       ↓
L2 — MANAGE IT ← TODAY
       ↓
L3 — UNDERSTAND IT
       ↓
L4 — SECURE IT
```

本課 Mission：
> **管理 AI 對既有 Weather Security Center 產生的一次真實變更。**

Change：
```text
add-weather-last-updated
```

右側只 Preview：
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

底部核心句：
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
>
> **規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。**

---

## 視覺

畫面不要塞流程細節。

左／後方：L1 已完成的 Weather Security Center，標示：
```text
WORKING ✓
```

中央：一張代表本課唯一任務的 Change Card：
```text
add-weather-last-updated
```

右／前方：四個簡潔節點：
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

整體視覺要讓學生一眼看懂：
```text
L1 做出系統
     ↓
L2 管理一次真實變更
```

四層流程不要在封面展開子步驟。

---

## 煥哥

表情：專注、自信，從 L1 Builder 轉成 Engineering Lead。

動作：一手指向 L1 已完成的 `WORKING ✓` 系統，另一手拿著 `add-weather-last-updated` Change Card。

視線：看向 Change Card，而不是只看完成的網站。

角色轉換：
```text
L1 BUILDER
    ↓
L2 ENGINEERING LEAD
```

---

## 老師講稿

上一堂課，我們完成了一件很重要的事。

我們讓 AI 幫忙把一個想法，變成真的可以運作的 Weather Security Center。

指向左邊：
```text
WORKING ✓
```

但是從今天開始，問題變了。

假設我現在只對 AI 說一句：
> 幫我加一個 Last Updated。

AI 很可能幾分鐘就改好了。

但我要問大家：

> 它到底改了哪些檔案？

> 為什麼這樣改？

> 有沒有順便改了我們沒有叫它改的東西？

> 它說 Done，我們怎麼知道真的 Done？

> 三個月以後，我們還找得到今天為什麼這樣改嗎？

停一下。

中央揭示：
```text
BUILDING SOFTWARE
        ↓
MANAGING CHANGE
```

所以 L2 不是再教大家「怎麼讓 AI 多寫一些 Code」。

今天真正要學的是：
> **怎麼把一次性的 AI Coding Prompt，提升成可以管理、可以驗證、可以留下歷史的 Engineering Workflow。**

而且今天整堂課只做一件事。

使用者的 Request：
> 使用者需要知道氣象資料最後更新時間。

我們把它變成一個正式 Change：
```text
add-weather-last-updated
```

整堂課就追蹤這一個 Change。

不建立第二個 App。
不換另一套 Demo。
也不開新的工具支線。

我們會讓它依序走過四個階段：
```text
DEFINE
BUILD
VERIFY
REMEMBER
```

現在不用急著記每一層怎麼做。

到 Slide 06，我們會正式建立這張 Engineering Map。

今天開場只需要知道：
> **我們要把一個 Change，從需求一路管理到可信、可追溯的工程歷史。**

---

## 問

上一堂課 Weather Security Center 已經能 Run。

那為什麼還需要 L2？

學生可能回答：
- 要保存版本。
- 要知道 AI 改了什麼。
- 要確認有沒有改錯。
- 要留下紀錄。
- 要管理 GitHub。

老師不用急著判斷完整與否。

回應：
> 很好。今天就是把這些零散想法整理成一套可以重複使用的 Engineering Workflow。

---

## 核心句

> **AI CAN BUILD. NOW WE LEARN TO MANAGE CHANGE.**
>
> **AI 能幫我們建構；現在我們要學會管理改變。**

---

## Transition

老師指向 `WORKING ✓`：

> 第一個問題就來了。
>
> Weather Security Center 已經能跑了。
>
> 既然能跑，為什麼還需要管理？

下一頁：
# **Slide 01 — AI 做出來了，接下來呢？**

---

## 建議時間

4–6 分鐘。

## 單頁品質檢查

```text
ONE MAIN QUESTION
L1 做出來之後，接下來怎麼管理 AI Change？

ONE MAIN VISUAL
L1 BUILD → L2 MANAGE → L3 UNDERSTAND → L4 SECURE

ONE MEMORY LINE
AI CAN BUILD. NOW WE LEARN TO MANAGE CHANGE.
```

邊界：
- 不教 Git commands。
- 不教 OpenSpec advanced syntax。
- 不重講 L1 Security concepts。
- 不搶 L3 Python / FastAPI / API / JSON。
- 不搶 L4 Semgrep / Security Remediation。
