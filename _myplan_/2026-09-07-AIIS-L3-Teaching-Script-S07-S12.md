# AIIS_L3 — Slide-by-Slide Teaching Script
## S07–S12 — HTTP Request → GET → Response → FastAPI Route

Date: 2026-09-07
Lesson Mission: UNDERSTAND

---

# Slide S07 — HTTP Request 是一封有格式的信

## 目的
把抽象 HTTP request 轉成學生可理解的結構化訊息，建立 method、path、parameters 的第一層心智模型。

## 投影片內容

### 一封 HTTP Request

```text
GET /weather?city=Hualien
```

拆開來：

```text
GET        → 我要做什麼？
/weather   → 我要找誰？
city=...   → 我要帶什麼資料？
```

HTTP Request 還可能包含：

```text
Method
Path
Query Parameters
Headers
Body
```

本課先抓住前三個。

## 視覺
把 HTTP request 畫成一個快遞信封：信封左上角是 `GET`，收件地址是 `/weather`，附件標籤是 `city=Hualien`。煥哥拿著放大鏡逐欄查看。

## 煥哥
「原來 Request 不是一句隨便的話，它有固定格式。」

## 老師講稿
上一頁我們看到 Browser 不會直接呼叫 Server 裡面的 Python function，而是送 HTTP request。

現在把 request 拆開。

例如 `GET /weather?city=Hualien`。

`GET` 是 HTTP method，表示這次 request 想做哪一類事情。

`/weather` 是 path，可以把它想成 Server 對外公開的一個地址。

`city=Hualien` 則是這次 request 帶進來的資訊。

真實 HTTP 還有 headers、body 等內容，但今天不要一次塞太多。我們先把 method、path、parameter 看懂，已經足夠追蹤 Weather Security Center 的第一條 flow。

## 問
「如果 `/weather` 像地址，那 `city=Hualien` 比較像什麼？」

## 預期答案
附帶條件、查詢資料、參數、我要查的城市。

## 老師補充 / 板書

```text
METHOD + PATH + INPUT
```

## 核心句
> An HTTP request is a structured message, not a random sentence.

## Transition
「我們先把第一個字 GET 看清楚。」

---

# Slide S08 — GET 到底代表什麼？

## 目的
讓學生理解 HTTP method 是 request intent 的一部分，並以 GET 為主要教學案例，不擴張成完整 REST 方法大全。

## 投影片內容

### GET = 請給我資料

```text
GET /weather?city=Hualien
```

人話：

> 「Server，請把 Hualien 的 weather data 給我。」

常見對照：

```text
GET     讀取
POST    建立／送入
PUT     更新
DELETE  刪除
```

今天主角：**GET**

## 視覺
四張小卡只讓 GET 高亮，其餘 POST/PUT/DELETE 淡化。GET 卡片上是煥哥向 Weather Server 伸手索取一張「Hualien Weather」資料卡。

## 煥哥
「今天先把 GET 追到底，不需要一次背完所有 HTTP methods。」

## 老師講稿
HTTP method 可以幫 Server 理解這次 request 的意圖。

GET 最常見的用途就是取得資料。

我們這一課不打算變成 HTTP 規格課，所以 POST、PUT、DELETE 先知道名字與大概方向即可。

今天我們刻意只追 GET，因為一個簡單 GET request 已經足夠帶我們穿越 Browser、HTTP、FastAPI、Python、Data 和 Response。

這也符合我們整門課的原則：一個代表性 workflow 做深，而不是十個工具都碰一下。

## 問
「我要查看花蓮現在的天氣，比較直覺會用 GET 還是 DELETE？」

## 預期答案
GET。

## 核心句
> GET asks the server for a resource or representation.

## Transition
「Request 現在離開 Browser，抵達 Server。接下來誰接住它？」

---

# Slide S09 — Server 收到 Request 之後呢？

## 目的
建立 request 進入 FastAPI 後的 routing 概念，為後續 decorator 與 Python function 做橋接。

## 投影片內容

```text
GET /weather?city=Hualien
        ↓
      SERVER
        ↓
    FastAPI Router
        ↓
「哪一段程式負責 /weather？」
        ↓
 Python Function
```

關鍵問題：

> Server 有很多 functions，FastAPI 怎麼知道要執行哪一個？

## 視覺
FastAPI 畫成機場轉運中心／交通警察。不同 request 有不同 path 標籤；`/weather` 被引導到 Weather function 的正確通道。

## 煥哥
「原來 FastAPI 的第一個重要工作，就是把 Request 送到正確的程式。」

## 老師講稿
想像 Server 裡面有很多功能。

有 weather、有 health check、有 sensor data，也可能有其他 API。

當 `GET /weather` 進來時，Server 不可能把每個 function 都跑一次看看。

它需要一張 routing map。

FastAPI 就負責其中非常重要的一件事：根據 HTTP method 與 path，把 request 對應到正確的 route handler，也就是我們接下來會看到的 Python function。

所以看到 FastAPI source code 時，不要只看到一堆 decorator。要把它翻譯成人話：「這個網址進來，要交給誰處理？」

## 老師補充 / 板書

```text
Request → Route → Function
```

## 核心句
> Routing connects an HTTP request to the code that handles it.

## Transition
「不過 function 執行完之後，Browser 還在等答案。所以我們先看看回程的 Response。」

---

# Slide S10 — Response：Server 回了什麼？

## 目的
建立 request/response 成對的 Web communication mental model，理解 status code 與 JSON body 的基本角色。

## 投影片內容

### REQUEST

```text
GET /weather?city=Hualien
```

### RESPONSE

```text
Status: 200 OK

{
  "city": "Hualien",
  "temperature": 29,
  "condition": "Sunny"
}
```

兩個先看懂：

```text
Status Code → 發生什麼結果？
Body        → Server 回了什麼資料？
```

## 視覺
左右雙向箭頭：Browser → Request → Server；Server → Response → Browser。Response 是一個透明包裹，外面貼 `200 OK`，裡面裝 JSON weather card。

## 煥哥
「Request 是去程，Response 是回程。」

## 老師講稿
Web communication 通常不是 Browser 只送出去就結束。

Server 要回答。

Response 裡我們今天先注意兩件事。

第一個是 status code。`200 OK` 告訴 client：這次 request 正常完成。

第二個是 response body，也就是真正回來的資料。API 很常使用 JSON。

所以一個 endpoint 的理解不能停在「request 進去了」。我們還要知道它最後回什麼。

之後遇到錯誤輸入時，我們也會看到不是每次都回 200。那時 status code 就會幫我們理解發生了什麼。

## 問
「如果 Server 回 `200 OK`，但 JSON 裡的城市資料錯了，代表整個系統一定正確嗎？」

## 預期答案
不一定。HTTP request 可能成功完成，但 business/data logic 仍可能錯誤。

## 核心句
> A response tells us both the outcome and the returned data.

## Transition
「現在去程和回程都有了。我們正式打開 FastAPI source code。」

---

# Slide S11 — FastAPI 是交通警察

## 目的
用一致比喻建立 FastAPI 在本課架構中的定位：接 HTTP、做 routing、協助 validation、形成 response；避免把 framework 當成魔法。

## 投影片內容

### FastAPI 在中間做什麼？

```text
HTTP Request
     ↓
┌─────────────────┐
│     FastAPI     │
│ ① 找 Route      │
│ ② 接收 Input    │
│ ③ 協助 Validation│
│ ④ 呼叫 Function │
│ ⑤ 形成 Response │
└────────┬────────┘
         ↓
    HTTP Response
```

> FastAPI 不是魔法；它把 Web 規則和 Python code 接起來。

## 視覺
FastAPI 是站在十字路口的交通警察，手上有 route map；HTTP request 車輛依 path 被導向不同 Python function。不要使用過多工具 logo，維持 Weather Security Center 世界觀。

## 煥哥
「所以 FastAPI 是 Web 世界和 Python 世界中間的橋。」

## 老師講稿
我們現在可以給 FastAPI 一個比較完整、但仍然簡單的定位。

它讓我們用 Python 很方便地建立 Web API。

HTTP request 進來後，FastAPI 根據 route 找到程式、接收參數、協助檢查輸入，執行我們的 Python function，再把結果整理成 Web client 能收到的 response。

這些工作如果全部自己從很底層寫，會麻煩很多。Framework 幫我們處理大量共通工作。

但是 framework 幫我們做，不代表我們不需要理解。

恰恰相反，我們要知道「哪一部分是 FastAPI 幫忙，哪一部分是我們自己的 Python logic」。這對下一課的 security review 也很重要。

## 問
「FastAPI 本身會知道 Hualien 今天幾度嗎？」

## 預期答案
不會。Weather data/logic 仍來自我們的 application/data source；FastAPI 主要處理 Web/API framework 工作。

## 核心句
> FastAPI connects HTTP behavior to Python application logic.

## Transition
「那 routing map 在 code 裡長什麼樣子？下一頁只看一行。」

---

# Slide S12 — `@app.get()` 是什麼？

## 目的
把學生已理解的 GET + path + routing 映射到一段最小 FastAPI code，完成從 Web concept 到 source code 的第一次對照。

## 投影片內容

```python
@app.get("/weather")
def get_weather(city: str):
    return {"city": city}
```

不要先背語法，先翻譯：

```text
@app.get("/weather")
        ↓
「如果收到 GET /weather」
        ↓
def get_weather(...)
        ↓
「執行這個 Python function」
```

一句話：

> HTTP Route → Python Function

## 視覺
左邊是 `GET /weather?city=Hualien` request 卡；中央 `@app.get("/weather")` 像一個配對插槽；右邊 Python function 被點亮。用連線清楚表現 request 與 source code 的 mapping。

## 煥哥
「我以前只把 `@app.get()` 當特殊語法，現在知道它是在宣告 routing 規則。」

## 老師講稿
現在請大家不要急著背 decorator 這個名詞。

先做翻譯。

`@app.get("/weather")` 可以先理解成：「當一個 GET request 來到 `/weather` 時，下面這個 function 負責處理。」

所以前面學的 HTTP 並不是另外一門無關的理論。

如果你不知道 GET、path、request 是什麼，看到這一行只會覺得是 FastAPI 的神祕語法。

一旦知道 HTTP，你會發現 source code 其實正在描述我們剛才畫的 routing map。

這就是今天 UNDERSTAND 的方法：概念和 code 一直互相對照。

下一頁我們就往下走一行，看看 request 如何真的進入普通 Python function。

## 問
「如果 request 是 `GET /weather`，但是程式只有 `@app.get("/sensor")`，這兩個會直接配對嗎？」

## 預期答案
不會；method/path 必須對應到已定義的 route。

## 老師補充 / 板書

```text
GET + /weather
      ⇅
@app.get("/weather")
```

## 核心句
> A FastAPI route declaration maps an HTTP request pattern to Python code.

## Transition
「Route 找到了。現在 Request 裡的 `city=Hualien` 怎麼跑進 Python function？」
