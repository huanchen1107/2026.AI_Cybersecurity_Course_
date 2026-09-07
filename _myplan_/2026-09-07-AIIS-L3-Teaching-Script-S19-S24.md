# AIIS_L3 — Slide-by-Slide Teaching Script
## S19–S24 — Database → SQLite → SQLAlchemy → Validation

Date: 2026-09-07
Lesson Mission: UNDERSTAND

---

# Slide S19 — 為什麼需要 Database？

## 目的
讓學生從「資料流動」進一步理解「資料持久保存」的需求，並把 database 放進既有 Weather Security Center 心智模型。

## 投影片內容

### 如果 Server 重開機，資料還在嗎？

只放在 Python variable：

```text
程式執行中 → 有資料
程式結束   → 可能消失
```

需要保存：

```text
Weather history
Sensor records
Station information
Application records
        ↓
     DATABASE
```

> Memory 是工作桌；Database 是資料櫃。

## 視覺
左側 Python 工作桌上放著暫時資料，關機後桌面被清空；右側 SQLite 資料櫃仍保存 weather/sensor cards。煥哥把需要留下來的資料放入資料櫃。

## 煥哥
「不是所有資料都只活在這一次 Request 裡。」

## 老師講稿
前面我們追的是一次 request，所以資料看起來一直在流動。

但是應用系統通常還需要記住東西。

例如 weather history、sensor record、station information，甚至之後系統自己的事件紀錄。

如果所有東西只放在 Python variable，程式結束或重新啟動後，資料可能就不存在。

Database 的基本角色就是 persistence，也就是讓需要留下來的資料可以持續保存。

今天不會把這堂課變成 SQL 課。我們只需要知道 database 在整個 data flow 裡扮演什麼角色，以及 Python 如何與它合作。

## 問
「現在這個 function 裡的 `temperature = 29`，Server 重開之後，它是不是等於自動建立了一筆歷史資料？」

## 預期答案
不是。程式中的值與持久保存的 database record 是不同概念。

## 核心句
> A database gives application data persistence beyond one execution.

## Transition
「我們這個 Lab 不需要先架大型 Database Server，所以使用一個非常適合教學與本地開發的選擇：SQLite。」

---

# Slide S20 — SQLite：我們的本地資料櫃

## 目的
讓學生建立 SQLite 的最小正確心智模型：它是一個輕量 relational database，適合本地 lab，而不是把它誤解成 Excel 或普通文字檔。

## 投影片內容

### SQLite

```text
Weather Security Center
        ↓
   SQLite Database
        ↓
┌─────────────────────┐
│ weather_records     │
├────┬─────────┬──────┤
│ id │ city    │ temp │
├────┼─────────┼──────┤
│ 1  │ Hualien │ 29   │
│ 2  │ Taipei  │ 31   │
└────┴─────────┴──────┘
```

適合本課：

```text
✓ Local
✓ Lightweight
✓ Easy to reproduce
✓ Good for classroom lab
```

## 視覺
SQLite 畫成 Weather Security Center 旁的小型本地資料櫃，抽屜內是 rows。避免畫成大型雲端企業資料中心，強調 local lab。

## 煥哥
「原來 Database 不一定是一台很大的 Server。」

## 老師講稿
很多同學聽到 database，腦中會想到一台很大的遠端伺服器。

SQLite 很不一樣。它很輕量，database 可以存在本地檔案中，不需要先架一套獨立 database server。

這非常適合我們的 classroom lab，因為每個人都可以在自己的 Weather Security Center 中建立可重現的資料環境。

但要注意，SQLite 仍然是 relational database，不是因為它方便就等於普通文字檔。

我們可以有 table、row、column，也可以查詢與更新資料。

今天的目標仍然不是背 SQL，而是知道：當 endpoint 需要保存或取得資料時，這裡可能是 data flow 的一站。

## 核心句
> SQLite gives our local lab a lightweight persistent data store.

## Transition
「可是 Python function 要怎麼跟這個資料櫃溝通？我們再加入一個翻譯角色。」

---

# Slide S21 — SQLAlchemy：Python 與 Database 的翻譯員

## 目的
用概念層級介紹 ORM/SQLAlchemy，讓學生能閱讀既有 AI-generated project code，而不把 L3 擴張成完整 ORM 課程。

## 投影片內容

### Python 想法

```python
WeatherRecord(
    city="Hualien",
    temperature=29
)
```

### Database 想法

```text
TABLE: weather_records
ROW: Hualien | 29
```

中間：

```text
Python Objects
      ↕
  SQLAlchemy
      ↕
Database Records
```

> 本課先懂角色，不背完整 ORM API。

## 視覺
左邊 Python 工程師講「Object 語言」，右邊 SQLite 資料櫃講「Table/Row 語言」，SQLAlchemy 站中間當翻譯員。

## 煥哥
「看到 SQLAlchemy code 時，我先問它在對哪個資料表做什麼，不急著背每個 method。」

## 老師講稿
AI 產生 FastAPI project 時，我們很可能會看到 SQLAlchemy。

第一次看到時，code 可能比剛才的 FastAPI route 更陌生。

今天我們只建立一個足夠閱讀系統的概念：SQLAlchemy 可以幫 Python application 與 relational database 互動，其中 ORM 讓我們可以用 Python class/object 的方式表達部分 database model 與操作。

所以當你看到一段陌生 SQLAlchemy code，不要立刻陷入每一行語法。

先問三件事：它對哪個 model/table？它是在讀、建立、更新還是刪除？結果往哪裡走？

這樣就能繼續 trace data flow。

## 問
「如果 AI 給你 30 行 SQLAlchemy code，你今天第一個目標是全部背起來嗎？」

## 預期答案
不是。先理解 model/table、操作目的、輸入輸出與 data flow。

## 老師補充 / 板書

```text
MODEL → OPERATION → RESULT
```

## 核心句
> Read ORM code by tracing the model, operation, and resulting data flow.

## Transition
「現在資料已經能從外面進來，也能進 database。下一個問題非常重要：外面送進來的資料，我們可以直接相信嗎？」

---

# Slide S22 — 使用者輸入一定正確嗎？

## 目的
從一般軟體可靠性角度引入 untrusted/invalid input，為 validation 建立需求；只 preview security implication，不進入 L4 SAST。

## 投影片內容

我們期待：

```text
GET /weather?city=Hualien
```

但 Client 也可能送：

```text
city=
city=12345
city=<very long text>
缺少 city
```

程式不能只想：

> 「使用者應該會照我的想法輸入。」

而要問：

> 「我接受什麼？不接受什麼？」

## 視覺
FastAPI 入口像 Weather Security Center 門口。正常 `Hualien` 卡片、空白卡、數字卡、超長卡同時排隊。煥哥在入口拿著檢查表，而不是全部直接放行。

## 煥哥
「原來 Input 不是我在 code 裡想像的值，而是外面真的可以送進來的資料。」

## 老師講稿
這裡開始碰到一個從 software engineering 一路通往 cybersecurity 的核心觀念。

只要資料來自 application 外部，就不要假設它永遠符合我們心中的理想形式。

使用者可能打錯、client 可能有 bug、資料可能缺少，也可能有完全沒預期到的內容。

所以我們需要清楚定義 input contract。

今天先從 correctness 與 robustness 的角度理解 validation：什麼資料可以進入 function？型別對不對？必要欄位有沒有？格式是否合理？

下一課我們才正式把這個觀念放進 security review。

## 問
「錯誤輸入一定代表有人在攻擊嗎？」

## 預期答案
不一定。可能只是使用者輸入錯誤、client bug 或格式不符；但系統仍需要安全且可預期地處理。

## 核心句
> External input must be checked, not assumed.

## Transition
「FastAPI 為什麼很適合初學者？因為我們寫下型別與 schema 後，它可以幫我們做很多基本檢查。」

---

# Slide S23 — FastAPI 如何幫我們檢查輸入？

## 目的
讓學生理解 Python type hints / Pydantic / FastAPI validation 的基本合作關係，知道 schema 不只是文件，也是 runtime contract 的一部分。

## 投影片內容

簡單參數：

```python
def get_weather(city: str):
    ...
```

結構化資料：

```python
class SensorInput(BaseModel):
    station: str
    temperature: float
```

FastAPI / Pydantic 可以協助：

```text
✓ Parse input
✓ Check required fields
✓ Validate types
✓ Produce clear validation errors
✓ Describe schema in /docs
```

## 視覺
一個 schema 模具：`station: str`、`temperature: float`。輸入資料必須通過模具才能進 application；不符合的資料被停在 validation gate。

## 煥哥
「原來 type/schema 不只是給我自己看，也可以變成 API contract。」

## 老師講稿
FastAPI 很重要的一個設計，是大量利用 Python type hints，並透過 Pydantic model 描述結構化資料。

例如 sensor input 應該有 station，而且 temperature 應該能被解析成符合定義的數值。

當 schema 寫得清楚，FastAPI 不只可以拿它產生 `/docs`，也能在 request 真正進入我們的 application logic 前協助 parse 與 validation。

注意：validation 不是萬能 security shield。它只代表我們開始建立明確的 input contract。

這堂課先學會讀這個 contract，下一課再看 source code security scanning 能發現哪些問題。

## 問
「如果 `temperature` 定義成 float，但 client 送一段完全無法轉成數字的文字，最理想的行為是什麼？」

## 預期答案
系統應拒絕/回傳清楚 validation error，而不是讓錯誤資料悄悄進入後續 logic。

## 核心句
> A schema turns expectations about input into an explicit contract.

## Transition
「我們實際比較兩個 request：一個符合 contract，一個不符合。」

---

# Slide S24 — 正常 Request vs 錯誤 Request

## 目的
透過 side-by-side comparison 讓學生讀懂 validation 的可觀察證據：input、status、response 不同。

## 投影片內容

### CASE A — Valid

```text
POST /sensor
```

```json
{
  "station": "Hualien-A",
  "temperature": 29.5
}
```

```text
→ Accepted
→ Application logic
→ Success response
```

### CASE B — Invalid

```json
{
  "station": "Hualien-A",
  "temperature": "not-a-number"
}
```

```text
→ Validation fails
→ Error response
→ Invalid data does not continue normally
```

觀察三件事：

```text
INPUT → STATUS → RESPONSE
```

## 視覺
左右兩條完全相同的入口管線。左邊正常資料通過 validation gate；右邊錯誤 temperature 被 gate 擋下並回傳 error card。避免呈現攻擊 payload，保持本課為安全、良性的 validation lab。

## 煥哥
「我不只看到 error，我可以解釋它在哪一層被擋下來。」

## 老師講稿
這裡我們開始把前面所有 mental model 用在實際 observation。

Case A 的資料符合 schema，所以 request 可以繼續進入 application logic。

Case B 的 temperature 明顯不符合我們定義的數值 contract，因此 validation layer 應該拒絕它並產生 error response。

學習重點不是背某個 status code，而是建立 trace 習慣。

看到錯誤時問：request 有沒有到 route？validation 有沒有通過？function 有沒有真的執行？response 是哪一層形成？

這就是從「看到紅字就貼給 AI」升級成 engineering diagnosis。

## 問
「如果 validation 已經拒絕 request，那我們應不應該假設後面的 database write 還是一定發生了？」

## 預期答案
不應該。要依實際 flow/evidence 判斷；正常設計下，未通過 validation 的 input 不應照正常路徑繼續寫入。

## 老師補充 / 板書

```text
INPUT → VALIDATE → LOGIC → DATA → RESPONSE
```

## 核心句
> Validation creates an observable boundary between accepted and rejected input.

## Transition
「這個 boundary 為什麼跟資安有關？下一頁只建立一個 preview，真正的 security scanning 留給 L4。」
