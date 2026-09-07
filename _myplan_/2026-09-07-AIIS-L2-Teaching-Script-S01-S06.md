# AIIS_L2 — 逐頁詳細教學稿 S01–S06
## Part A — 從 Vibe Coding 走向 Spec-Driven AI Engineering

狀態：CANONICAL — L1 STYLE — 2026-09-07

統一格式：**目的 → 投影片內容 → 視覺 → 煥哥 → 老師講稿 → 問答 → 核心句 → Transition**。

---

# Slide 01 — AI 做出來了，接下來呢？

## 目的
從 L1 BUILD 正式進入 L2 MANAGE。建立第一個認知衝突：**系統能跑，不代表這次變更已經被妥善管理。**

## 投影片內容
左側巨大：
```text
WORKING ✓
```
右側：
```text
WHY CHANGE?
WHAT SHOULD CHANGE?
WHAT SHOULD NOT CHANGE?
HOW DO WE KNOW IT IS DONE?
```
底部：
```text
WORKING SOFTWARE ≠ MANAGED SOFTWARE
```
繁中：**能運作的軟體，不等於可管理的軟體。**

## 視覺
左邊是 L1 已完成的 Weather Security Center，亮綠色 `WORKING ✓`。右邊是四個工程問號，中間是一條尚未完成的管理橋樑。

## 煥哥
表情：從 L1 完成作品的開心，轉為思考。
動作：一手指著網站，一手指向四個問號。
角色：PROJECT LEAD。

## 老師講稿
上一堂課，我們已經讓 AI 幫忙做出 Weather Security Center。它可以 Run，資料也可以顯示。

現在使用者提出一個很小的需求：
> 我想知道這些氣象資料最後是什麼時候更新的。

很多人的第一個反應是：叫 AI 加上去。

這沒有錯。但我要多問四件事：為什麼改？哪些地方應該改？哪些地方不應該亂改？最後誰決定它真的完成？

## 問
如果 Prompt 只有：
```text
Please improve my Weather Security Center.
```
`improve` 到底允許 AI 改多少？

預期：學生開始發現邊界不清楚。

## 核心句
> **AI CAN BUILD. NOW WE LEARN TO MANAGE CHANGE.**
> **AI 能幫我們建構；現在我們要學會管理改變。**

## Transition
> 而且別以為一句很短的 Request，只會改一小段 Code。

下一頁：**一句小需求，可能改很多地方。**

---

# Slide 02 — 一句小需求，可能改很多地方

## 目的
建立 **Change Surface（變更影響面）** 的直覺：Request 很短，不代表實際影響範圍很小。

## 投影片內容
中央巨大：
```text
"Add Last Updated"
```
向外展開：
```text
UI
BACKEND?
DATA?
DEPENDENCY?
```
底部：
```text
CAN CHANGE ≠ SHOULD CHANGE
```
繁中：**可以改，不代表應該改。**

## 視覺
中央是一張很小的 Request 卡，向外展開多個 File / Component 卡。每張卡使用問號，表示「可能影響」，不是「一定要改」。

## 煥哥
表情：驚訝。
動作：手拿小 Request，身後卻展開很多檔案。
角色：CHANGE OBSERVER。

## 老師講稿
`Add Last Updated` 看起來只是很小的要求。

但 AI 可能想到 UI、Backend、Timestamp、CSS，甚至覺得應該新增 Package。

這些地方可能被影響，但「可能被影響」不代表「全部都應該修改」。

簡單記住：
> Change Surface 就是一個需求可能影響到的程式、資料、設定與行為範圍。

## 問
如果 AI 提議：
```text
Add Last Updated
+ Upgrade FastAPI
+ Refactor weather service
+ Replace CSS framework
```
它做得更多，代表工程品質更好嗎？

預期答案：不一定。

## 核心句
> **MORE CHANGES ≠ BETTER ENGINEERING.**
> **改得更多，不代表工程做得更好。**

## Transition
> 如果每次都只靠一句 Prompt，讓 AI 自己決定 Scope，專案改十次之後會發生什麼？

下一頁：**Vibe Coding 很快，但專案要持續演化。**

---

# Slide 03 — Vibe Coding 很快，但專案要持續演化

## 目的
肯定 L1 Vibe Coding 的價值，同時讓學生理解：快速開始之後，持續專案需要控制與工程記憶。

## 投影片內容
左：
```text
IDEA → PROMPT → AI → WORKING ✓
```
右：
```text
CHANGE #1
CHANGE #2
CHANGE #3
CHANGE #4
...
```
中央：
```text
FAST CREATION
      ↓
CONTROLLED EVOLUTION
```

## 視覺
左側有速度感，一次完成作品；右側逐漸堆疊多張 Change Cards。不要把 Spec 名詞提前塞滿畫面。

## 煥哥
左側：快速 Vibe Coding、開心。
右側：轉為 Engineering Lead，開始看變更與歷史。

## 老師講稿
L1 的 Vibe Coding 有沒有用？非常有用。

它讓我們很快從 Idea 走到 Working Software。

但 Weather Security Center 不是今天做完就丟掉。後面還會增加功能、理解程式、做安全檢查、修正問題，最後成為期末作品。

所以真正困難的不是第一次 Build，而是第十次 Change 之後，你還知不知道：為什麼改、改了什麼、誰決定的？

Chat 很適合互動與思考，但重要工程決策不能只存在某一次聊天裡。

## 問
到第十次修改時，你還記得第二次跟 AI 說了什麼嗎？

預期：很難。

## 核心句
> **VIBE CODING GETS US STARTED. ENGINEERING KEEPS US UNDER CONTROL.**
> **Vibe Coding 讓我們快速開始；Engineering 讓專案持續可控。**

## Transition
> 那一句 Prompt，和一份可以保存的工程規格，到底差在哪裡？

下一頁：**Prompt vs Spec。**

---

# Slide 04 — Prompt 與 Spec 不一樣

## 目的
第一次清楚區分 Prompt 與 Spec 的角色。

## 投影片內容
兩欄：
```text
PROMPT                  SPEC
"Add Last Updated"     WHY
                        SCOPE
                        REQUIREMENTS
                        DONE
```
底部：
```text
A PROMPT ASKS. A SPEC DEFINES.
```
繁中：**Prompt 提出指令；Spec 定義變更。**

## 視覺
左側是一個聊天泡泡；右側是一張結構化 Change Card。兩者之間不是紅叉，而是不同角色的對比。

## 煥哥
表情：理解差異。
動作：左手拿 Prompt bubble，右手拿 Spec card。
角色：SPEC THINKER。

## 老師講稿
`Add Last Updated` 這句話錯嗎？沒有。

它很適合開始與 AI 互動。

但它沒有完整回答：為什麼？範圍到哪裡？系統必須做到什麼？怎樣算 Done？

所以：
```text
PROMPT = 如何與 AI 互動
SPEC   = 如何持久定義 Change
```

Prompt 和 Spec 不是敵人。後面我們仍然會 Prompt AI，但 AI 的工作邊界來自 Spec。

## 問
如果明天換另一個 AI Agent，只有昨天的聊天內容與有一份 Spec，哪一個比較容易接手？

預期：Spec。

## 核心句
> **A PROMPT ASKS. A SPEC DEFINES.**
> **重要 Change 不能只靠聊天中的一句 Prompt 定義。**

## Transition
> 那我們怎麼把 Spec 真正放進 Project，而不是再做一個散落的文字檔？

下一頁：**Meet OpenSpec。**

---

# Slide 05 — 認識 OpenSpec

## 目的
正式介紹 OpenSpec 作為 AIIS 的代表性 Spec-Driven Development 方法；不進入複雜語法。

## 投影片內容
```text
USER REQUEST
     ↓
┌───────────────────┐
│  OPENSPEC CHANGE  │
│ WHY               │
│ SCOPE             │
│ REQUIREMENTS      │
│ ACCEPTANCE        │
└─────────┬─────────┘
          ↓
     AI ENGINEERING
```
底部：
> **重要 Requirements 不應只存在 Chat History。**

## 視覺
OpenSpec Change 明確畫在 Project / Repository 裡，而不是漂浮在聊天視窗。

## 煥哥
表情：開始有掌控感。
動作：把使用者 Request 放進 Project，變成 OpenSpec Change。
角色：CHANGE OWNER。

## 老師講稿
現在我們需要的不是更多 Prompt 技巧，而是一個方法，把重要需求從聊天搬進專案。

AIIS 選 OpenSpec 作為代表性方法。不是說全世界只有 OpenSpec，而是我們整班需要一套一致、可以重複使用的 Change Workflow。

今天唯一的 Change 名稱：
```text
add-weather-last-updated
```

下星期就算換另一個 Agent，我們也可以叫它先讀這個 Change，而不是問它還記不記得上次聊天。

這堂課不教完整 OpenSpec 語法，也不比較十種 Spec 工具，避免主線發散。

## 問
OpenSpec 的角色是替 AI 寫 Code 嗎？

預期答案：不是，是 DEFINE THE CHANGE。

## 核心句
> **REQUIREMENTS MUST NOT LIVE ONLY IN CHAT HISTORY.**
> **重要需求必須進入可保存的工程脈絡。**

## Transition
> OpenSpec 只是其中一層。完整 AI Engineering 還需要 Build、Verify 和 Remember。

下一頁：**四層地圖。**

---

# Slide 06 — AI Engineering 的四層地圖

## 目的
建立 L2 最重要的 Anchor Slide。後面 S07–S30 全部回到這四層。

## 投影片內容
```text
① DEFINE
OpenSpec
定義要改什麼

② BUILD
Antigravity
依 Spec 實作

③ VERIFY
Diff + Test + Human
證明真的做對

④ REMEMBER
Git + GitHub
保存歷史與證據
```
底部巨大：
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

## 視覺
四個大型模組橫向排列。上方一條 Human 線：
```text
HUMAN: DEFINE → REVIEW → VERIFY → ACCEPT
```
不要放完整 15-step workflow。

## 煥哥
表情：清楚、自信。
動作：站在四層流程上方，指向整張工程地圖。
角色：ENGINEERING LEAD。

## 老師講稿
今天工具名稱很多：OpenSpec、Antigravity、Git、GitHub。

如果只記工具，很快就亂掉。

所以只記四個動詞。

DEFINE：先定義這次 Change。

BUILD：再讓 AI 依 Spec 實作。

VERIFY：AI 說完成還不夠，要看 Diff、Run/Test、Acceptance Criteria 與 Human Review。

REMEMBER：驗證後，把工程歷史保存下來。

Human-in-the-loop 不是最後按一下 Approve。Human 從一開始就在控制 Intent、Scope 與 Acceptance。

## 問
教師快速念四件事，學生回答屬於哪一層：
- 寫 Acceptance Criteria → DEFINE
- AI 修改 Dashboard → BUILD
- 看 Diff → VERIFY
- Commit → REMEMBER

## 核心句
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
> **規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。**

## Transition
> 地圖有了。現在我們用一個真正的 Request，從 DEFINE 開始完整走一次。

下一頁：**Slide 07 — 真實需求來了。**
