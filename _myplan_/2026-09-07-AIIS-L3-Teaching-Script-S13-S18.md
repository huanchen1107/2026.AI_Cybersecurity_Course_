# AIIS_L3 — Slide-by-Slide Teaching Script
## S13–S18 — Function → Parameters → JSON → /docs → Weather Data Flow

Date: 2026-09-07
Lesson Mission: UNDERSTAND

---

# Slide S13 — Route → Python Function

## 目的
讓學生看見 FastAPI route 最終會進入普通 Python function，降低 framework 神祕感。

## 投影片內容

```python
@app.get("/weather")
def get_weather(city: str):
    return {"city": city}
```

把它拆成兩層：

```text
WEB LAYER
@app.get("/weather")
        ↓
PYTHON LAYER
def get_weather(city: str)
```

> Route 決定「誰處理」；Function 決定「怎麼處理」。

## 視覺
上層是 HTTP/FastAPI 道路，下層是 Python 工作室。Request 經由 `/weather` 閘門進入 `get_weather()` 工作室。煥哥站在兩層中間指著連接箭頭。

## 煥哥
「FastAPI 沒有取代 Python，它只是把 Web Request 接到 Python。」

## 老師講稿
上一頁我們理解 `@app.get("/weather")` 是 routing rule。

現在往下一行看。

`def get_weather(city: str):` 就開始回到大家比較熟悉的 Python 世界。

這個 function 可以做計算、呼叫其他 functions、取得 weather data、查 database，最後 return 結果。

所以閱讀 FastAPI code 時，可以刻意分成兩層：上面是 Web/API contract，下面是 application logic。

這個分層非常重要。未來 debug 或 security review 時，我們會問：問題是在 Web input？routing？還是 application logic？

## 問
「如果把 function 裡面的計算邏輯改掉，但 route 完全不變，Browser 呼叫的 URL 一定要跟著改嗎？」

## 預期答案
不一定。只要 API contract/path 沒改，內部 implementation 可以改變。

## 核心句
> The route chooses the handler; the Python function performs the work.

## Transition
「可是我們的 function 有一個 `city`。它是怎麼從 URL 跑進來的？」

---

# Slide S14 — Parameter 從哪裡進來？

## 目的
讓學生把 query parameter 與 Python function parameter 對起來，第一次看懂 request input 如何進入程式。

## 投影片內容

Request：

```text
GET /weather?city=Hualien
```

Code：

```python
@app.get("/weather")
def get_weather(city: str):
    return {"city": city}
```

Mapping：

```text
city=Hualien
      ↓
city: str
      ↓
city == "Hualien"
```

## 視覺
URL 中的 `city=Hualien` 被高亮，像一顆資料膠囊沿箭頭進入 function 的 `city` 參數槽。其他 code 淡化，讓學生只追一個值。

## 煥哥
「我現在真的看到資料從 Request 進入 Python 了。」

## 老師講稿
這一頁是整堂課很關鍵的一個瞬間。

前面我們一直說 data flow，現在真的看到一筆資料跨過 Web 與 Python 的邊界。

Browser 送 `city=Hualien`。

FastAPI 根據 function signature 知道我們需要一個叫 city 的輸入，於是把 request 中的資料轉進 Python parameter。

接下來 function 裡面就可以把 `city` 當普通 Python variable 使用。

這也是為什麼 input validation 很重要：外面的使用者可以影響進入程式的資料。今天先理解這件事，後面才有能力談安全。

## 問
「`city` 的值是 programmer 寫死的，還是可能由 request 的使用者決定？」

## 預期答案
可能由 request 使用者提供。

## 老師補充 / 板書

```text
EXTERNAL INPUT → PROGRAM VARIABLE
```

## 核心句
> Request data can become program data.

## Transition
「Function 拿到資料、處理完之後，接下來要把答案送回 Browser。」

---

# Slide S15 — Return 為什麼變成 JSON？

## 目的
讓學生理解 Python return value 與 HTTP JSON response 之間的轉換，完成第一條最小 request/response trace。

## 投影片內容

Python：

```python
return {
    "city": city,
    "temperature": 29
}
```

FastAPI：

```text
Python dict
    ↓
serialize
    ↓
JSON Response
```

Client 收到：

```json
{
  "city": "Hualien",
  "temperature": 29
}
```

## 視覺
左邊 Python dict 卡片，經過 FastAPI「包裝站」，右邊變成 JSON response 包裹送回 Browser。維持同一資料球的去程/回程故事。

## 煥哥
「所以我 return 的 Python 資料，FastAPI 幫我整理成 Web Client 看得懂的 Response。」

## 老師講稿
我們現在走到回程。

Python function return 一個 dictionary。FastAPI 會協助把可序列化的資料轉成 JSON response。

所以 Browser 或其他 client 不需要懂 Python dictionary 物件，它收到的是 Web API 常見的 JSON 表示。

現在我們第一次可以完整說出一條最小 flow：Browser 送 GET request，FastAPI 找 route，把 parameter 交給 Python function，function return data，FastAPI 再形成 JSON response。

這就是理解系統的第一個閉環。

## 問
「JSON 和 Python dict 完全是同一個東西嗎？」

## 預期答案
不是。它們看起來相似，但 JSON 是資料交換格式；Python dict 是 Python 的資料結構。

## 核心句
> Python produces the result; FastAPI helps turn it into an HTTP response.

## Transition
「我們有沒有一個地方，可以不用自己手打很多工具，就直接看到這些 API contract？有，就是 `/docs`。」

---

# Slide S16 — `/docs`：API 的 X 光機

## 目的
讓學生學會使用 FastAPI 自動文件作為理解與驗證 API 的主要 inspection interface，而不是只把它當測試按鈕。

## 投影片內容

### FastAPI `/docs`

你可以看見：

```text
✓ HTTP Method
✓ Path
✓ Parameters
✓ Input schema
✓ Response
✓ Status code
```

操作：

```text
Open /docs
→ Choose endpoint
→ Try it out
→ Enter input
→ Execute
→ Inspect response
```

> `/docs` 不只是「試 API」；它是讀 API contract 的地方。

## 視覺
模擬 Swagger UI 的簡化介面，不必追求真實 screenshot。煥哥戴 X 光眼鏡，從 `/docs` 看見 endpoint 裡面的 method、parameter、response。

## 煥哥
「以前我只會按 Execute；現在我要看它告訴我什麼。」

## 老師講稿
FastAPI 很適合教學的一個原因，就是它會根據程式自動建立 OpenAPI 文件，通常可以從 `/docs` 打開互動介面。

以前大家可能只是照著老師說的按 Try it out、Execute。

今天開始要換一個角色：把 `/docs` 當 inspection tool。

先不要執行。先讀。

這個 endpoint 是 GET 還是 POST？path 是什麼？需要哪些 parameters？parameter type 是什麼？可能回什麼 response？

然後再 Execute，拿實際行為去驗證我們對 source code 的理解。

這就是 AI 時代很重要的 verification habit：先形成解釋，再用 evidence 驗證。

## 問
「如果 AI 說某 endpoint 需要 `city`，但 `/docs` 顯示根本沒有這個 parameter，我們應該相信誰？」

## 預期答案
應以實際 source/runtime/API contract 為 evidence，重新檢查 AI 的解釋。

## 老師補充 / 板書

```text
AI EXPLANATION ≠ EVIDENCE
/docs + source + test = evidence
```

## 核心句
> Use `/docs` to inspect the API contract and verify your understanding.

## Transition
「我們現在知道 request 怎麼進 function、response 怎麼回來。但真正的 weather value 從哪裡來？」

---

# Slide S17 — 天氣資料從哪裡來？

## 目的
把 API logic 與 data source 分開，讓學生理解 endpoint 不會自己創造真實資料。

## 投影片內容

Weather Security Center 可能取得：

```text
CWA Open Data
      或
Teacher-provided / Fake Sensor Data
      ↓
Python
      ↓
FastAPI
      ↓
Client
```

關鍵問題：

> API 是資料的「來源」，還是資料的「服務入口」？

## 視覺
左邊兩個來源：氣象開放資料雲與 classroom sensor dataset；資料匯入 Weather Security Center，再經 API 提供給 Browser。避免把外部服務細節做成另一堂課。

## 煥哥
「原來 `/weather` 不代表資料出生在 `/weather`。」

## 老師講稿
這是另一個很常見的誤解。

我們打 `/weather` API，看到天氣資料，就容易以為 API 本身就是資料來源。

其實 API endpoint 更像一個服務入口。

資料可能來自中央氣象署 Open Data，也可能是我們為 classroom lab 準備的 fake sensor data，也可能已經保存到 local database。

Python application 取得、整理這些資料，再透過 FastAPI 對外提供。

今天不深入學 external API integration；我們只需要建立「source 與 endpoint 是不同角色」的 mental model。

## 問
「如果外部 weather source 暫時沒有資料，我們的 FastAPI route 還存在嗎？」

## 預期答案
可以存在，但它可能無法取得預期資料，或需要處理 error/fallback。

## 核心句
> An API endpoint serves data; it is not necessarily the original source of that data.

## Transition
「現在把剛才所有零件串起來，我們第一次追完整的 Data Flow。」

---

# Slide S18 — Data Flow：Source → Python → API

## 目的
整合 S06–S17，建立 Weather Security Center 第一張完整端到端 data-flow map，為 database 與 validation 段落奠基。

## 投影片內容

### One Request — Full Trace v1

```text
① Browser
   GET /weather?city=Hualien
        ↓
② FastAPI Route
   @app.get("/weather")
        ↓
③ Python Function
   get_weather(city)
        ↓
④ Weather Data Source
   CWA / Fake Sensor / stored data
        ↓
⑤ Python Result
   dict / model
        ↓
⑥ FastAPI Response
   JSON + Status
        ↓
⑦ Browser
   Weather UI
```

底部：

> If you can trace the data, you can start debugging the system.

## 視覺
全頁主視覺是一條清楚的 ①–⑦ 管線。Hualien 資料球從 Browser 出發，穿過 route/function/data source，再變成 response 返回。每一站沿用前面頁面的圖示，形成認知收斂。

## 煥哥
「我現在不是只看到 code，我看到資料正在 code 裡面旅行。」

## 老師講稿
我們停一下，把前面十二頁收斂成一張圖。

使用者要 Hualien weather。
Browser 形成 HTTP GET request。
FastAPI 根據 `/weather` 找到 route。
Request 的 city 進入 Python function。
Function 取得或處理 weather data。
結果 return 回來，FastAPI 形成 JSON response。
最後 Browser 才能顯示資料。

這張圖比背十個 FastAPI 語法更重要。

因為如果某一天 Hualien 顯示成 Taipei，我們就可以開始問：request 的 city 對不對？function 收到的 city 對不對？data source 查到什麼？response 回了什麼？

Debugging 就不再只是猜。

下一段，我們加入一個新的角色：Database。為什麼有些資料不能每次都重新取得，而需要保存？

## 問
「如果 `/docs` 顯示 response 已經是正確 Hualien 資料，但網頁畫面顯示 Taipei，你會優先懷疑哪一段？」

## 預期答案
較可能在 API response 之後，例如 frontend 顯示/狀態處理，而不是直接先改 database。

## 老師補充 / 板書

```text
TRACE BEFORE GUESS
```

## 核心句
> Trace the data before guessing where the problem is.

## Transition
「資料會流動，也可能需要留下來。下一站：SQLite。」
