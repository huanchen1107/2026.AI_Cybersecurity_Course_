# AIIS_L3 — Slide-by-Slide Teaching Script
## S25–S30 — Security Preview → Trace → Explain → Modify → Test → Evidence

Date: 2026-09-07
Lesson Mission: UNDERSTAND

---

# Slide S25 — Validation 也是 Security 的入口

## 目的
把 L3 的 input/validation 理解自然銜接到 L4 security，但只建立問題意識，不提前教授 Semgrep/SAST。

## 投影片內容

```text
OUTSIDE WORLD
     ↓
   INPUT
     ↓
 VALIDATION
     ↓
APPLICATION LOGIC
     ↓
    DATA
```

今天我們問：

> 「這個 input 符合我們的 contract 嗎？」

下一課會再問：

> 「這段 code 有沒有 security weakness？」

```text
L3 UNDERSTAND → L4 SECURE
```

## 視覺
Weather Security Center 的入口閘門。外部資料先經 Validation Gate。遠方下一站有盾牌與 code scan 圖示，但不出現具體攻擊 payload。

## 煥哥
「原來要談 Security，第一步是先知道資料到底怎麼進系統。」

## 老師講稿
這一頁是 L3 與 L4 的邊界。

今天我們學 validation，主要是為了理解 application 如何處理 input。

但是大家應該已經開始感覺到，這件事情和 security 很接近。

因為 application 的外部邊界，就是資料進入系統的地方之一。

不過我們今天不要跳到 vulnerability scanning，也不要開始背安全規則。

先把 L3 的責任做好：我能不能指出 input 從哪裡進來？在哪裡 validation？哪個 function 接到？資料最後去哪裡？

如果連 flow 都不知道，下一課看到 scanner finding 時，很容易又變成「AI 說有問題所以我就改」。

真正的 secure engineering 必須建立在 understanding 上。

## 核心句
> You cannot secure a flow you do not understand.

## Transition
「概念學完了。現在不再只是看老師的 flow，我們自己選一個 endpoint，開始 TRACE。」

---

# Slide S26 — LAB 1：TRACE IT

## 目的
讓學生實際使用既有 Weather Security Center 找出一條 endpoint execution/data path，將整堂課概念轉成可觀察 evidence。

## 投影片內容

### Mission 1 — TRACE

選一個既有 endpoint：

```text
① 找到 Method + Path
② 在 /docs 執行一次
③ 找到 source route
④ 找到 Python function
⑤ 找出 input
⑥ 找出 data source / database interaction
⑦ 找出 response
```

交付一張：

```text
REQUEST → ROUTE → FUNCTION → DATA → RESPONSE
```

## 視覺
煥哥拿著偵探板，將 `/docs`、source code、data/database、JSON response 用紅線連成一條 evidence chain。不是攻擊偵查，而是 code trace。

## 煥哥
「先不要改 code。我先證明我知道現在的 code 怎麼跑。」

## 老師講稿
Lab 第一階段有一個很重要的限制：先不要修改。

請從目前 Weather Security Center 選一個老師指定或允許的 endpoint。

第一步到 `/docs` 看它的 API contract，執行一個正常 request，保存 response。

第二步回 source code 找到對應 route 與 function。

第三步繼續追 input 往哪裡走，是否讀 external data、local data 或 SQLite。

最後畫出一條最簡單的 request-to-response flow。

如果中途看不懂，可以問 AI。但 AI 給你的答案不能直接當 evidence，你要回 source 和 runtime 驗證。

## 問
「這個階段為什麼故意不讓大家先改 code？」

## 預期答案
要先建立 baseline 與理解，否則修改後不知道行為差異從哪裡來。

## 老師補充 / 板書

```text
BASELINE BEFORE CHANGE
```

## 核心句
> Trace the current behavior before changing it.

## Transition
「Trace 出路線還不夠。下一步，你要能不用 AI 替你回答，自己說出這條 flow。」

---

# Slide S27 — LAB 2：EXPLAIN IT

## 目的
把學生從 AI explanation consumer 轉成 verifier，要求以自己的話解釋 endpoint 並用 source/runtime evidence 支持。

## 投影片內容

### Mission 2 — EXPLAIN

可以問 AI：

```text
Explain this endpoint step by step.
Identify:
- request input
- route
- function
- data source
- response
```

但是你必須完成：

```text
AI says...
    ↓
Check source
    ↓
Check /docs
    ↓
Run request
    ↓
My verified explanation
```

學生一句話模板：

> When ______ request arrives, FastAPI ______, then Python ______, data comes from ______, and the API returns ______.

## 視覺
左邊 AI 對話框提供 explanation 草稿；中間煥哥拿 checklist 比對 source、`/docs`、runtime；右邊蓋上 VERIFIED 印章。

## 煥哥
「AI 可以當助教，但最後的 explanation 要由 evidence 負責。」

## 老師講稿
這一段就是我們課程裡 AI literacy 與 engineering literacy 的交會點。

你完全可以把 function 貼給 AI，請它逐步解釋。

但我們不把 AI answer 當成 final truth。

請拿 AI 的 explanation 回頭對照 source code。再到 `/docs` 看 API contract。最後真的 run 一次 request。

如果 AI 說 function 會查 database，但你找不到任何 database operation，就要提出疑問，而不是替 AI 找理由。

最後請用自己的話完成 explanation。

這個能力比背 framework definition 更接近真正的 AI-assisted engineering。

## 核心句
> AI may propose an explanation; evidence verifies it.

## Transition
「你已經知道它現在怎麼運作。現在才有資格做一個 controlled change。」

---

# Slide S28 — LAB 3：MODIFY IT

## 目的
要求學生在已理解的 flow 上做一個小而可控的修改，實踐 L2 change discipline，但不重新教授 L2。

## 投影片內容

### Mission 3 — MODIFY

只改一件小事，例如：

```text
+ 一個 response field
+ 一個 optional query parameter
+ 一個簡單 validation rule
+ 一個 classroom-safe data field
```

規則：

```text
ONE CHANGE
CLEAR EXPECTATION
NO NEW APP
NO LARGE REWRITE
```

Before：

```json
{"city":"Hualien","temperature":29}
```

After（示意）：

```json
{"city":"Hualien","temperature":29,"unit":"C"}
```

## 視覺
同一條 endpoint flow，只有一個小模組被黃色框標記「CHANGE HERE」。其他部分鎖住，強調 controlled change。

## 煥哥
「我不是叫 AI 重寫整個系統，我知道我要改哪一小段。」

## 老師講稿
現在可以修改，但只允許 controlled change。

這不是因為我們做不到大改，而是因為工程實驗需要能夠判斷因果。

如果一次改十個地方，最後成功或失敗都很難知道原因。

所以先寫下 expectation。例如：response 要多一個 unit field，而且原本 city 與 temperature 行為不能壞。

接著可以請 AI 協助修改，但 prompt 要非常明確：只完成這個 change，不做 unrelated refactor。

這裡其實正在 reuse L2 的 change discipline，只是不重新教一遍。

## 問
「為什麼『順便把整個 project 重構得更漂亮』不是這個 Lab 的好選擇？」

## 預期答案
Scope 太大、難驗證、增加不必要變數，也破壞 controlled experiment。

## 核心句
> Small controlled changes make cause and effect observable.

## Transition
「AI 說改好了、畫面也看起來沒問題，還不能結束。下一步：TEST IT。」

---

# Slide S29 — LAB 4：TEST IT & PROVE IT

## 目的
讓學生用 runtime/API test 建立 before/after evidence，將「我覺得成功」升級為「我能證明成功」。

## 投影片內容

### Mission 4 — TEST

```text
BEFORE
capture baseline
    ↓
CHANGE
one controlled modification
    ↓
AFTER
/docs verification
    ↓
TEST
basic / automated test
    ↓
EVIDENCE
expected == actual ?
```

至少驗證：

```text
✓ New behavior works
✓ Existing key behavior still works
✓ Response is observable
✓ Test result is saved
```

Evidence：

```text
Before response
After response
Test result
Short explanation
```

## 視覺
左側 BEFORE API response，中央 change，右側 AFTER response；下方一條 test pipeline 最後蓋上 PASS/EVIDENCE。避免只有大大的綠勾，要清楚顯示證據來源。

## 煥哥
「不是『看起來有成功』，而是『我有證據說它成功』。」

## 老師講稿
這是整堂課最後一個工程習慣。

修改前先保存 baseline。

修改後先用 `/docs` 做一個直接的 API verification。

接著執行老師提供或專案既有的 basic automated test。如果這次 change 需要一個小 test，也可以在 AI 協助下建立，但必須知道 test 在檢查什麼。

我們至少要回答兩件事：新功能真的出現了嗎？原本重要行為有沒有被破壞？

最後把 before、after、test result 放在一起。

這就是 evidence。

未來進入 security scanning 時，我們也會延續同一個習慣：不是 scanner 說修好了就算，而是 fix 後要 re-verify。

## 老師補充 / 板書

```text
CLAIM + EVIDENCE
```

## 核心句
> Engineering claims require observable evidence.

## Transition
「現在回到今天一開始的問題：AI 幫我寫的系統，我真的懂了嗎？」

---

# Slide S30 — I Can Explain What My Code Does

## 目的
收斂 L3 的學習成果，形成可檢核的學生能力聲明，並自然交棒給 L4 SECURE。

## 投影片內容

### AIIS_L3 — UNDERSTAND COMPLETE

我現在可以：

```text
✓ TRACE    跟著一個 Request 走完整條路
✓ EXPLAIN  用自己的話說明系統行為
✓ MODIFY   做一個 controlled change
✓ TEST     驗證預期與實際結果
✓ EVIDENCE 保存可以檢查的證據
```

能力聲明：

> I can trace, explain, modify, and test one FastAPI endpoint in our Weather Security Center.

下一課：

```text
L3 UNDERSTAND
I know how it works.
        ↓
L4 SECURE
Is the code secure?
        ↓
Scan → Finding → Evaluate → Fix → Re-scan
```

## 視覺
Weather Security Center 從黑箱變成透明系統，Browser → HTTP → FastAPI → Python → Data → Response 全部可見。煥哥手上拿著完成的 Trace Map 與 Evidence Pack。右側下一扇門寫著 `L4 SECURE`。

## 煥哥
「現在我不只是會叫 AI 寫。我知道它怎麼跑，也知道怎麼證明我的修改沒有亂來。」

## 老師講稿
回到 Slide 00。

今天一開始我們問：working code 是不是等於 understood code？

現在大家應該知道答案。

我們從 Browser 出發，理解 HTTP request、GET、route、Python function、parameter、data source、SQLite、SQLAlchemy、validation 和 response。

但最重要的不是這些名詞本身，而是我們學會一個方法：TRACE。

面對 AI 產生的 code，不需要一開始就把全部讀完。選一條真實 flow，跟著它走，形成 explanation，再用 runtime 與 test 驗證。

今天的 Evidence Pack 就是你已經從「AI 幫我做」往「我能負責這段 code」前進的證明。

下一課我們會做一件非常自然的事情。

既然我們已經知道 code 怎麼運作，就可以開始問：這段 source code 有沒有 security weakness？

那時我們才正式進入 SECURE，使用代表性的 source-code scanning workflow：Scan → Finding → Evaluate → Fix → Re-scan。

## 問
「如果下一課 scanner 說某一行有 security finding，我們應該直接叫 AI 刪掉那一行嗎？」

## 預期答案
不應直接修改。要先理解 finding、確認 code/data flow 與影響，再做 controlled fix 並重新驗證。

## 老師補充 / 板書

```text
BUILD → MANAGE → UNDERSTAND → SECURE
```

## 核心句
> Understanding turns AI-generated code into code we can responsibly review and improve.

## Transition
**Next Mission: AIIS_L4 — SECURE**

> 「它會跑，而且我懂它。現在，我們來看看它安全嗎？」

---

# L3 Final Lab Evidence Pack

學生至少提交：

1. Endpoint method + path
2. `/docs` baseline request/response
3. Request → Route → Function → Data → Response trace map
4. Verified explanation in student's own words
5. One controlled modification
6. Before/after response evidence
7. Basic or automated test result
8. One-paragraph reflection: AI helped with what, and what did I personally verify?

# L3 Completion Criteria

A student completes L3 when they can demonstrate:

```text
I can TRACE it.
I can EXPLAIN it.
I can MODIFY it.
I can TEST it.
I can PROVE it.
```

This is the prerequisite mindset for L4 SECURE.
