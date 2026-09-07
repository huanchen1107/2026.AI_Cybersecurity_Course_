# AIIS_L2 — 詳細教學講稿 S01–S06
## Part A — 從 Vibe Coding 走向 Spec-Driven AI Engineering

狀態：PART A TEACHING SCRIPT — CANONICAL zh-TW REVISION — 2026-09-07
課程位置：L2 / MANAGE

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**
>
> **規格定義需求，AI 負責實作，人類負責驗證，Git 保存歷史。**

## 本段設計原則
每頁只承擔一個主要認知任務；投影片保持精簡，詳細解釋放教師講稿。

```text
ONE SLIDE
= ONE MAIN QUESTION
+ ONE MAIN VISUAL
+ ONE MEMORY LINE
```

本段的故事不是先介紹工具，而是先讓學生感覺到：

```text
AI 很會 BUILD
        ↓
但是 Change 需要被 MANAGE
        ↓
Prompt alone 不夠
        ↓
需要 Spec + Workflow + Evidence + History
```

---

# Slide 01 — AI 做出來了，接下來呢？
## AI Built It. What Happens Next?

### 這頁在做什麼
從 L1 BUILD 正式進入 L2 MANAGE。製造第一個認知衝突：**系統能跑，不代表工程變更已經可管理。**

### ON SLIDE
左側：L1 Weather Security Center，標記：
```text
WORKING ✓
```

右側只放四個問題：
```text
WHY CHANGE?
WHAT SHOULD CHANGE?
WHAT SHOULD NOT CHANGE?
HOW DO WE KNOW IT IS DONE?
```

底部：
> **WORKING SOFTWARE ≠ MANAGED SOFTWARE**
> **能運作的軟體，不等於可管理的軟體。**

### 視覺
不要放流程圖。用「已完成的 Weather Security Center」對比右側四個巨大問號。

### 煥哥角色
**PROJECT LEAD（專案負責人）**。先看著能運作的網站微笑，再轉頭看 Change 問題露出思考表情。

### 教師講稿
> 上一堂課我們已經讓 AI 幫忙做出 Weather Security Center。它能 Run，資料也能顯示。
>
> 如果今天使用者說：「我想知道這些氣象資料最後是什麼時候更新的。」你會怎麼做？

學生多半回答：「叫 AI 加上去。」

教師：
> 沒錯，AI 很可能幾分鐘就做完。但是我要多問四件事：為什麼改？哪些應該改？哪些不能亂改？最後誰決定它真的 Done？

可短暫顯示一個故意模糊的 Prompt：
```text
Please improve my Weather Security Center.
```

問：
> `improve` 到底允許 AI 改多少？

### 板書
```text
L1 BUILD IT
 ↓
L2 MANAGE IT
```

### 學生只需帶走
> **AI 能 Build；現在要學的是如何管理 AI 產生的 Change。**

### 銜接 S02
> 而且別以為一句很短的 Request，只會改一小段 Code。

建議時間：6–8 分鐘。

---

# Slide 02 — 一句小需求，可能改很多地方
## One Sentence Can Change Many Files

### 這頁在做什麼
讓學生建立 **Change Surface（變更影響面）** 的直覺：Request 很短，不代表實際變更範圍很小。

### ON SLIDE
中央：
```text
"Add Last Updated"
```

向外只展開四張卡：
```text
UI
BACKEND?
DATA?
DEPENDENCY?
```

底部：
> **CAN CHANGE ≠ SHOULD CHANGE**
> **可以改，不代表應該改。**

### 視覺
一張很小的 Request 卡，後面展開多張 File / Component 卡。用問號強調「可能」，不是宣稱全部都要改。

### 煥哥角色
**CHANGE OBSERVER（變更觀察者）**。手上拿著小 Request，身後突然展開多個檔案。

### 教師講稿
> `Add Last Updated` 看起來只有四個字。但 AI 可能先想到 UI，再想到 Backend，再想到 Timestamp，再想到 CSS，甚至覺得需要一個新套件。

> 這些地方「可能」被影響，但可能被影響，不代表都應該修改。

簡單定義：
> **Change Surface = 一個需求可能影響到的程式、資料、設定與行為範圍。**

### 快速活動
學生只回答：
> 你預測這個 Change 最可能需要碰哪 1–3 個地方？為什麼？

不要追求正確檔名；重點是要求理由。

### 教師故意給錯誤 AI 建議
```text
Add Last Updated
+ Upgrade FastAPI
+ Refactor weather service
+ Replace CSS framework
```

問：
> AI 做得更多，是不是代表工程品質更好？

揭示：
> **MORE CHANGES ≠ BETTER ENGINEERING**

### 學生只需帶走
> 小 Request 可能造成大的 Change Surface，因此 AI 的變更需要邊界與控制。

### 銜接 S03
> 如果每一次都只靠一句 Prompt，再讓 AI 自己決定 Scope，專案改十次之後會發生什麼？

建議時間：7–9 分鐘。

---

# Slide 03 — Vibe Coding 很快，但專案要能持續演化
## From Fast Creation to Controlled Evolution

### 這頁在做什麼
不否定 Vibe Coding；先肯定它在 L1 的價值，再說明持續專案需要比聊天 Prompt 更多的控制與記憶。

### ON SLIDE
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

底部：
> **Vibe Coding gets us started. Engineering keeps us under control.**

### 視覺
左側速度感、右側逐漸堆疊的 Change cards。不要在畫面塞 Intent/Scope/Constraints 等六個名詞。

### 煥哥角色
**VIBE CODER → ENGINEERING LEAD**。左側快速建立，右側開始審查變更與歷史。

### 教師講稿
> L1 的 Vibe Coding 有沒有用？非常有用。否則我們可能還在設定環境，網站已經被 AI 幫我們做出來了。

> 問題不是第一次 Build，而是這個 Project 要活整個學期。

口頭快速帶過：
```text
Week 1 Build
Week 2 Add feature
Week 4 Security fix
Later ML / DL / Red Team / Blue Team
```

問：
> 到第十次修改時，你還記得第二次跟 AI 說了什麼嗎？

教師：
> Chat 很適合互動與思考，但重要工程決策不能只存在某一次聊天裡。

### 板書
```text
CHAT = conversation
PROJECT = durable engineering memory
```

### 常見誤解
「所以 Vibe Coding 不好？」

修正：
> 不是。它非常適合快速開始；我們現在只是替它加上持續工程所需要的管理層。

### 學生只需帶走
> **快速做出來之後，還要能持續、可控地改下去。**

### 銜接 S04
> 那麼，一句 Prompt 和一個真正可保存的工程規格，差在哪裡？

建議時間：7–8 分鐘。

---

# Slide 04 — Prompt 與 Spec 不一樣
## Prompt vs Spec

### 這頁在做什麼
第一次清楚區分：Prompt 是與 AI 的當下互動；Spec 是對 Change 的持久定義。

### ON SLIDE
兩欄即可：

```text
PROMPT                     SPEC
"Add Last Updated"        WHY
                           SCOPE
                           REQUIREMENTS
                           DONE
```

底部：
> **A PROMPT ASKS. A SPEC DEFINES.**
> **Prompt 提出指令；Spec 定義變更。**

### 視覺
左邊是一張聊天泡泡；右邊是一張結構化 Change Card。避免把完整 Acceptance Criteria 塞進本頁。

### 煥哥角色
**SPEC THINKER（規格思考者）**，把一句 Prompt 轉換成一張結構化 Change Card。

### 教師講稿
顯示：
```text
Add Last Updated.
```

問：
> 這句話錯嗎？

教師：
> 沒錯，它很適合開始互動。但它沒有完整回答：為什麼？範圍到哪裡？系統必須做到什麼？怎樣算 Done？

建立：
```text
PROMPT = 如何與 AI 互動
SPEC   = 如何持久定義 Change
```

### 一個重要澄清
Prompt 與 Spec 不是敵人，也不是二選一。

後面仍然會 Prompt AI：
```text
請讀取 Spec，先 Inspect，再提出 Plan。
```

但 AI 的工作邊界來自 Spec。

### 板書
```text
PROMPT = ASK / INSTRUCT
SPEC   = DEFINE
```

### 學生只需帶走
> **重要 Change 不能只靠聊天中的一句 Prompt 定義。**

### 銜接 S05
> 那我們怎麼把 Spec 真正放進 Project，而不是再做一個散落的文字檔？

建議時間：7–9 分鐘。

---

# Slide 05 — 認識 OpenSpec
## 把重要需求從 Chat 搬進 Project

### 這頁在做什麼
正式介紹 OpenSpec 作為 AIIS 的代表性 Spec-Driven Development 方法，但**不教 OpenSpec 語法細節**。

### ON SLIDE

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

### 視覺
一定要把 OpenSpec Change 畫在 Project / Repository 裡，而不是浮在聊天視窗中。

### 煥哥角色
**CHANGE OWNER（變更負責人）**。把一張使用者 Request 放入 Project 裡標記為 OpenSpec Change。

### 教師講稿
> 我們現在需要的不是更多 Prompt 技巧，而是一個方法，把重要需求從聊天搬進專案。

> AIIS 選擇 OpenSpec 作為代表性的實作方法。不是說全世界只有這一種方法，而是整班需要一套一致、可重複的 Change Workflow。

示範名稱：
```text
add-weather-last-updated
```

教師：
> 下星期就算換另一個 AI Agent，我們也可以叫它先讀這個 Change，而不是問它「還記不記得上次聊天」。

### 不在本頁教
- OpenSpec 完整語法
- 目錄細節
- 進階 template
- 多種 Spec 工具比較

這些都會讓 L2 主線發散。

### 核心句
> **REQUIREMENTS MUST NOT LIVE ONLY IN CHAT HISTORY.**
> **重要需求必須進入可保存的工程脈絡。**

### 學生只需帶走
> OpenSpec 的角色是 **DEFINE THE CHANGE**，不是替 AI 寫 Code。

### 銜接 S06
> 到這裡 OpenSpec 只是其中一層。完整的 AI Engineering 還需要 Build、Verify 和 Remember。

建議時間：7–9 分鐘。

---

# Slide 06 — AI Engineering 的四層地圖
## DEFINE → BUILD → VERIFY → REMEMBER

### 這頁在做什麼
建立 L2 最重要的 Anchor Slide。後面 S07–S30 所有內容都必須能回到這四層之一。

### ON SLIDE
只放四格：

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

底部：
> **DEFINE → BUILD → VERIFY → REMEMBER**

### 視覺
四個大型模組橫向排列。每格只放一個代表工具與一句中文，不要放完整 15-step workflow。

### 煥哥角色
**ENGINEERING LEAD（工程負責人）**。站在四層流程上方，代表 Human 責任橫跨全部階段。

### 教師講稿
> 今天工具名稱很多：OpenSpec、Antigravity、Git、GitHub。如果我們只記工具，很快就亂掉。

> 所以只記四個動詞。

逐格揭露：

**DEFINE**
> 先定義這次 Change 是什麼。

**BUILD**
> 再讓 AI 依照定義去實作。

**VERIFY**
> AI 說完成還不夠，我們要用 Diff、Run/Test、Acceptance Criteria 和 Human Review 驗證。

**REMEMBER**
> 驗證後，把工程歷史保存下來。

### Human 橫跨四層
在四格上方畫一條細線：
```text
HUMAN: DEFINE → REVIEW → VERIFY → ACCEPT
```

教師：
> Human-in-the-loop 不是最後按一下 Approve；Human 從一開始就在控制 Intent、Scope 和 Acceptance。

### 快速分類活動
教師念四件事，學生回答哪一層：
- 寫 Acceptance Criteria → DEFINE
- AI 修改 HTML → BUILD
- 看 Diff → VERIFY
- Commit → REMEMBER

### 核心句
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

### 學生只需帶走
如果今天只記得一張圖，就是：
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

### 銜接 S07
> 地圖有了。現在我們用一個真正的 Request，從 DEFINE 開始完整走一次。

下一頁：
**S07 — 真實需求來了：Add Last Updated**

建議時間：8–10 分鐘。

---

# Part A 教學節奏檢查

```text
S01  為什麼需要 MANAGE？
 ↓
S02  因為小 Request 也可能造成大 Change Surface
 ↓
S03  Vibe Coding 適合快速開始，但持續專案需要控制
 ↓
S04  Prompt 與 Spec 的角色不同
 ↓
S05  OpenSpec 把 Change 定義留在 Project
 ↓
S06  四層總地圖：DEFINE → BUILD → VERIFY → REMEMBER
```

## Part A 刻意沒有做的事
- 不建立第二個 App。
- 不教 Git command 細節。
- 不教 OpenSpec 複雜語法。
- 不教 Python / FastAPI internals。
- 不進行 Semgrep Scan。
- 不提前教 L3/L4 的正式內容。

Part A 結束後直接進入同一個案例：
```text
add-weather-last-updated
```
