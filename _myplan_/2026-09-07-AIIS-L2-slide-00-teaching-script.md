# AIIS_L2 — Slide 00 教學講稿
## MANAGE：從「AI 做得出來」到「我們管得住改變」

Date: 2026-09-07
Status: CANONICAL SLIDE 00
Language: 繁體中文為主

> Slide 00 是課程定位／封面頁，不占用原本 S01–S30 的正式教學頁碼。

## 這頁在做什麼？

把 L1 的 BUILD 自然接到 L2 的 MANAGE。學生一開始就要知道：**今天不再建立另一個 App，也不是單純學 Git 指令，而是學習如何管理 AI 對既有專案產生的 Change。**

## ON SLIDE

主標題：

# AIIS_L2 — MANAGE
## Spec-Driven AI Engineering
### OpenSpec × Antigravity × Git × GitHub

中央主線：

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

底部核心句：

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
>
> **規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。**

## 視覺構圖

畫面不要塞流程細節。

- 左／後方：L1 已完成的 Weather Security Center，標示 `WORKING ✓`。
- 中央：一張 Change 卡 `add-weather-last-updated`。
- 右／前方：四個簡潔節點 `DEFINE → BUILD → VERIFY → REMEMBER`。
- 煥哥站在 Change 卡旁，從「Builder」角色轉為「Engineering Lead」。

表情：專注、準備管理工程變更，不需要誇張。

## 教師開場講稿

> 上一堂課，我們完成了一件很重要的事：讓 AI 幫我們把一個想法變成真的可以運作的 Weather Security Center。

> 但是從今天開始，問題變了。

停一下，指向已完成系統：

> 如果我現在只對 AI 說一句：「幫我加一個 Last Updated」，AI 很可能幾分鐘就改好了。

接著問學生：

> 可是它到底改了哪些檔案？
>
> 為什麼這樣改？
>
> 有沒有順便改了我們沒叫它改的東西？
>
> 它說 Done，我們怎麼知道真的 Done？
>
> 三個月以後，我們還找得到今天為什麼這樣改嗎？

揭示：

```text
BUILDING SOFTWARE
        ↓
MANAGING CHANGE
```

> 所以 L2 不是再教你「怎麼讓 AI 多寫一些 Code」。今天要學的是：**怎麼把 AI Coding 從一次性的 Prompt，提升成可以管理、可以驗證、可以留下歷史的 Engineering Workflow。**

## 今天只做一件事

```text
Request:
「使用者需要知道氣象資料最後更新時間。」

Change:
add-weather-last-updated
```

> 整堂課就追蹤這一個 Change。我們不建立第二個 App，也不開新的工具支線。

## 四層只 Preview，不在 S00 解釋

```text
DEFINE
BUILD
VERIFY
REMEMBER
```

教師：

> 現在不用記每一層怎麼做。到 S06 我們會正式建立完整地圖。今天開場只要知道：我們要把一個 Change 從需求一路管理到可信的工程歷史。

## 學生本頁只需帶走

1. L1 是 BUILD；L2 是 MANAGE。
2. 今天沿用同一個 Weather Security Center。
3. 今天只管理一個代表性 Change：`add-weather-last-updated`。
4. AI 能修改 Code，不代表 Change 已經被管理。

## 核心記憶句

> **AI CAN BUILD. NOW WE LEARN TO MANAGE CHANGE.**
>
> **AI 能幫我們建構；現在我們要學會管理改變。**

## 銜接 S01

> 那第一個問題就來了：我們的 Weather Security Center 已經能跑了。既然能跑，為什麼還需要 L2？

下一頁：

**S01 — AI Built It. What Happens Next?**

建議時間：4–6 分鐘。

## 單頁品質檢查

- One Main Question：L1 做出來之後，接下來怎麼管理 AI Change？
- One Main Visual：L1 BUILD → L2 MANAGE → L3 UNDERSTAND → L4 SECURE
- One Memory Line：AI CAN BUILD. NOW WE LEARN TO MANAGE CHANGE.
- 不教 Git command。
- 不教 OpenSpec syntax。
- 不重講 L1 Security concepts。
- 不搶 L3 Python/API 或 L4 Semgrep。
