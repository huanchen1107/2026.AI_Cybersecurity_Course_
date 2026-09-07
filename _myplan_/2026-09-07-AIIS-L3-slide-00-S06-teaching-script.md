# AIIS_L3 — Slide-by-Slide Teaching Script
## Slide 00 + S01–S06

Date: 2026-09-07
Standard: AIIS Standard Slide-by-Slide Teaching Format
Lesson Mission: UNDERSTAND

---

# Slide 00 — AIIS_L3：UNDERSTAND

## 目的
把學生從 L1 BUILD、L2 MANAGE 帶到 L3 UNDERSTAND，明確告訴學生今天不是再叫 AI 多寫一個功能，而是第一次真正打開 Weather Security Center 看懂它。

## 投影片內容

**AIIS_L3 — UNDERSTAND**

### Python FastAPI Weather Security Center

```text
L1 BUILD      我們把它做出來
      ↓
L2 MANAGE     我們學會管理 AI 產生的改變
      ↓
L3 UNDERSTAND 我真的知道它怎麼運作嗎？
      ↓
L4 SECURE     我知道它怎麼運作後，才能問：安全嗎？
```

本課 Mission：

> Trace → Explain → Modify → Test → Evidence

## 視覺
中央是一台打開外殼的 Weather Security Center 機器。左邊學生原本只看到漂亮 Dashboard；右邊外殼打開後可以看到 Browser、HTTP、FastAPI、Python、SQLite、JSON 等齒輪與資料流。煥哥拿著放大鏡，表情由「會用了」變成「我要看懂裡面」。

## 煥哥
「AI 幫我寫好了……可是如果老師問我這一行為什麼在這裡，我答得出來嗎？」

## 老師講稿
前兩課我們已經開始使用 AI 做真正的工程工作。L1 的重點是 BUILD，我們體驗 AI-assisted development；L2 則開始學習不要讓 AI 隨便改，而要管理 change、review 與 evidence。

今天我們不急著再加新功能。

今天做一件對未來非常重要的事：把我們已經有的 Weather Security Center 打開來看。

很多人學 Vibe Coding 最容易遇到一個問題：程式真的跑起來了，但是如果問「Browser 按下去之後發生什麼？這個 endpoint 在哪裡？資料從哪裡來？為什麼最後會看到 JSON？」就說不清楚。

所以今天的目標不是背 FastAPI 語法，而是建立一張系統心智地圖。

到下課前，我希望每個人都能說：I can explain what my code does.

## 問
「一個程式能正常執行，是不是代表寫這個程式的人一定懂它？」

## 預期答案
不是。可能是複製、AI 生成、照教學完成，或者只是剛好能執行。

## 核心句
> Working code ≠ Understood code.

## Transition
「所以我們先看看，AI 時代為什麼『看懂程式』反而變得更重要。」

---

# Slide S01 — AI 寫好了，所以完成了嗎？

## 目的
建立本課的核心衝突：AI 可以快速生成 working code，但工程責任不能因此消失。

## 投影片內容

左：

```text
Prompt
  ↓
AI
  ↓
Code
  ↓
RUN ✓
```

右：五個問題

```text
它為什麼會跑？
Request 到哪裡？
哪個 function 被執行？
資料從哪裡來？
錯誤輸入會怎樣？
```

底部：

> RUN ✓ 只是開始，不是理解的證明。

## 視覺
煥哥高興地看到綠色 `RUN ✓`，下一秒旁邊冒出五個巨大問號。畫面形成「成功執行」與「真正理解」的反差。

## 煥哥
「它真的會跑！……等一下，它到底怎麼跑的？」

## 老師講稿
Vibe Coding 最大的優點是降低開始做軟體的門檻。以前可能要先學很多語法才能做出第一個 Web API，現在 AI 可以快速幫我們建立骨架。

但速度帶來新的責任。

如果 AI 一次產生 200 行程式，我們不能把「沒有紅色 error」當成唯一品質標準。

因為未來遇到 bug、安全問題、資料錯誤或功能修改時，你必須知道應該去哪裡找。

真正的工程能力不是「我可以叫 AI 產生 code」，而是「AI 產生之後，我能理解、驗證、修改它」。

## 問
「如果今天 Weather Security Center 顯示錯誤城市的溫度，你第一個會去哪裡找問題？」

## 預期答案
學生可能回答 API、資料庫、程式、資料來源等。重點不是立即答對，而是讓大家發現需要 data flow 心智模型。

## 核心句
> AI can generate code. The engineer must build understanding.

## Transition
「那我們現在到底走到整個 AIIS Journey 的哪裡？」

---

# Slide S02 — BUILD → MANAGE → UNDERSTAND

## 目的
讓學生清楚知道 L3 不重做 L1/L2，而是能力向下一層深入。

## 投影片內容

```text
BUILD
Can AI help me build it?
       ↓
MANAGE
Can I control the change?
       ↓
UNDERSTAND  ← YOU ARE HERE
Can I explain how it works?
       ↓
SECURE
Can I find and fix security problems?
```

## 視覺
四層電梯／樓層圖。煥哥目前站在 UNDERSTAND 樓層，手上拿著 Weather Security Center 專案。下一層 SECURE 的門還沒打開，只露出盾牌與掃描符號作為 preview。

## 煥哥
「原來不是一直學新工具，而是把同一個系統一層一層看深。」

## 老師講稿
這是我們這門課很重要的設計。

我們不希望每一週換一個 Demo，最後每個工具都碰過，但是沒有任何一個系統真正做深。

所以 Weather Security Center 會一直留著。

L1 我們問：AI 能不能幫我做？
L2 我們問：AI 要修改時，我能不能管理這個 change？
今天 L3 問：這個系統我到底懂不懂？

而下一課才會正式問：既然我知道它怎麼運作，那它有沒有 security finding？

因此今天不要急著攻擊、掃描，也不要急著學 Semgrep。先建立理解。

## 核心句
> Same project. Deeper understanding.

## Transition
「可是整個 Web App 很大，我們怎麼開始理解？答案是：不要一次看全部。」

---

# Slide S03 — 今天只追一件事：一個 Request

## 目的
給學生一個降低認知負荷的方法：用一個 request 作為穿越整個系統的主線。

## 投影片內容

大字：

> FOLLOW ONE REQUEST.

```text
① Browser
   ↓
② HTTP Request
   ↓
③ FastAPI Route
   ↓
④ Python Function
   ↓
⑤ Data / SQLite
   ↓
⑥ JSON Response
   ↓
⑦ Browser
```

例：

```text
GET /weather?city=Hualien
```

## 視覺
一顆亮色資料球從 Browser 出發，沿著管線穿過 FastAPI、Python、Database，最後帶著 JSON 回到 Browser。全課後續頁面持續沿用同一顆資料球，形成視覺故事線。

## 煥哥
「我不用一次看懂整個專案，我先跟著這一個 request 走。」

## 老師講稿
看一個陌生 codebase 時，最容易犯的錯就是從第一個檔案第一行開始讀。

很快你就會迷路。

今天我們換一種工程師常用的方法：trace one flow。

假設 Browser 想取得花蓮天氣，它送出一個 request。我們就跟著這個 request 旅行。

它先經過 HTTP，再被 FastAPI 找到正確 route，執行 Python function，可能讀取資料來源或 database，最後組成 response 回來。

只要你能把這條路追清楚，你就開始擁有系統的 mental model。

## 老師補充 / 板書

```text
TRACE = 跟著一次真實執行路徑走
```

## 核心句
> Don’t read everything. Trace one real flow.

## Transition
「在開始旅行以前，我們先把 Weather Security Center 從一個黑盒子拆成幾層。」

---

# Slide S04 — Weather Security Center 裡到底有什麼？

## 目的
建立學生第一次完整但簡化的 application architecture mental model。

## 投影片內容

```text
┌─────────────────────┐
│ Browser / Frontend  │  看見畫面
└─────────┬───────────┘
          │ HTTP
┌─────────▼───────────┐
│ FastAPI             │  接住 Request
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ Python Logic        │  處理事情
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ Data / SQLite       │  保存／取得資料
└─────────┬───────────┘
          │
          └──→ Response / JSON
```

右下角：

> 今天不是背架構圖，而是讓一個 Request 親自走過它。

## 視覺
Weather Security Center 被畫成四層透明建築，每層有不同工作角色。資料球從上往下，再帶著 response 往上返回。

## 煥哥
「原來我看到的一個頁面，背後其實有不同層在合作。」

## 老師講稿
我們先暫時忽略很多真實系統的複雜細節。

今天只需要四層。

第一層是 Browser 或 frontend，是使用者看到的地方。
第二層是 FastAPI，它負責接住 Web request，判斷這個 request 應該交給誰。
第三層是 Python logic，真正執行我們寫的處理邏輯。
第四層是 data，可能是外部 Weather data，也可能是 SQLite 中保存的資料。

這不是所有 Web Architecture 的完整版本，但它是一張足夠讓我們開始 debug、理解與修改的地圖。

## 問
「如果資料庫裡的資料完全正確，但 Browser 顯示錯誤，問題一定在 Database 嗎？」

## 預期答案
不一定。可能發生在 Python logic、API response、frontend 等其他層。

## 核心句
> A working screen is the result of multiple layers cooperating.

## Transition
「如果我們不知道這些層，就只會看到一個黑箱。」

---

# Slide S05 — 黑箱 vs 透明系統

## 目的
把「理解」具體定義成能指出輸入、處理、資料與輸出的路徑，而不是要求學生背全部 source code。

## 投影片內容

### BLACK BOX

```text
Prompt → AI → ??? → Web App ✓
```

我只知道：
- 它能跑
- 我敢按按鈕
- 壞了就再問 AI

### TRANSPARENT SYSTEM

```text
Request
→ Route
→ Function
→ Data
→ Response
```

我可以：
- Trace
- Explain
- Modify
- Test

底部：

> 理解 ≠ 背程式碼
> 理解 = 能解釋因果與資料流

## 視覺
左邊是一個封閉黑箱，煥哥只敢按綠色 Run；右邊是透明機器，可以看到資料球的完整路徑，煥哥手上拿著路線圖。

## 煥哥
「所以老師不是要我背 300 行 code，而是要我知道事情為什麼會發生。」

## 老師講稿
這一點非常重要。

我說「看懂 AI 產生的程式」，不是叫大家把所有 code 背起來。

真正的理解是因果關係。

當 `/weather` 被呼叫時，哪個 route 接到？哪個 function 執行？輸入從哪裡來？資料從哪裡取得？最後 return 什麼？

如果錯了，我可以根據這張地圖逐層找，而不是只把 error 丟給 AI 說「fix it」。

AI 還是可以幫我們。但是現在 AI 是 navigator，不是替我們遮住系統的黑布。

## 核心句
> Understanding means explaining the flow, not memorizing the code.

## Transition
「現在我們正式跟著 request 出發。第一站，就是大家每天都在使用的 Browser。」

---

# Slide S06 — Browser 做了什麼？

## 目的
從學生熟悉的 Browser 行為建立 client → server request 心智模型，為 HTTP 教學鋪路。

## 投影片內容

使用者：

```text
我想看 Hualien weather
```

Browser / Client：

```text
GET /weather?city=Hualien
```

Server：

```text
收到 request
→ 找 route
→ 執行程式
→ 回 response
```

底部：

> Browser 不會直接「讀 Python」。它透過 HTTP 跟 Server 說話。

## 視覺
左側學生在 Browser 輸入 Hualien；中間 Browser 把人的意圖包成一個 HTTP request 信封；右側 FastAPI Server 收到信封。延續 S03 的資料球視覺。

## 煥哥
「我只是按了一下按鈕，原來 Browser 已經幫我送出一個 Request。」

## 老師講稿
我們平常用網站時，很容易覺得 Browser 好像什麼都知道。

其實 Browser 與 Server 是兩個不同角色。

Browser 不會自己跑我們 Server 裡面的 Python function。它要用雙方都同意的溝通方式送訊息，這個溝通規則就是 HTTP。

例如我們想看花蓮的天氣，前端可能最後形成一個像 `GET /weather?city=Hualien` 的 request。

這個 request 送到 Server 後，FastAPI 才開始工作。

下一頁我們就要把這個 request 信封拆開來看。

## 問
「Browser 知不知道 Server 裡面那個 Python function 的名字？」

## 預期答案
通常不需要知道。Browser 透過 HTTP method/path/API contract 與 Server 溝通。

## 老師補充 / 板書

```text
CLIENT ≠ SERVER
HTTP = communication contract
```

## 核心句
> The browser talks to the server through HTTP, not by directly calling our Python code.

## Transition
「那這封 HTTP Request 裡面，到底裝了什麼？」
