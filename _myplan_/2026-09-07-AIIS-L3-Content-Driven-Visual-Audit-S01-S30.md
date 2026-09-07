# AIIS_L3 — Content-Driven Visual Audit（S01–S30）

Date: 2026-09-07
Status: CANONICAL VISUAL SPEC
Mission: UNDERSTAND — understand how the same AI-built Weather Security Center works.
Canonical flow: `Browser → HTTP Request → FastAPI Route → Python Function → Data → SQLite → Response → Browser`
Boundary: no new app; no repeat of L1 Vibe Coding; no repeat of L2 Git/OpenSpec; no L4 Semgrep/SAST pre-teaching.

## Audit rule
Every slide must derive Huange visual from the concept: Role → Expression → Action → Prop → direct content interaction. Generic standing/talking poses fail.

## S01–S06 — Open the black box
- S01 From BUILD/MANAGE to UNDERSTAND — Huange = System Explorer. Holds completed Weather Center, opens a transparent side panel showing internal layers. Speech: `我們已經會做、會管理；現在把黑盒子打開。`
- S02 Click → What happens? — Curious User. Finger clicks `查詢花蓮天氣`; behind the button a question trail enters the system. `我只按一下，裡面到底跑了什麼？`
- S03 System is a journey — Data-flow Guide. Uses laser pointer along Browser→Request→FastAPI→Python→Data→Response. `今天不背零件，我們跟著一次 Request 旅行。`
- S04 Browser is the starting point — Browser Operator. Types URL / presses action; browser emits a request packet. `Browser 不知道 Python；它只知道怎麼發 Request。`
- S05 Client ↔ Server — Messenger visual. Huange stands between laptop client and FastAPI server, physically passes request envelope right and response envelope left. `Client 問，Server 回。`
- S06 HTTP Request — Request Inspector. Magnifier over method/path/query; highlights only essential fields. `Request 是送給 Server 的問題單。`

## S07–S12 — FastAPI receives the request
- S07 Request arrives at FastAPI — Traffic Controller. Request packet reaches FastAPI gate; Huange directs it inward. `Request 到了，但它要交給誰？`
- S08 Route = address matcher — Route Dispatcher. Holds `/weather/{city}` address card and matches incoming path to correct lane. `Route 就像 Server 裡的地址分派。`
- S09 Decorator connects path to function — Connector Engineer. Physically clips `@app.get(...)` connector between route card and function card. `Decorator 把這個網址，接到這個 Python function。`
- S10 Path / Query parameters — Form Interpreter. Pulls `city=Hualien` or parameter value from request and places it into function input slot. `URL 裡的值，最後會變成程式的輸入。`
- S11 Python function runs — Python Mechanic. Opens function box and follows input→logic→output arrows; no generic code wall. `Route 找到人了，真正工作的是 Function。`
- S12 Return value — Output Inspector. Function produces Python object/data card; Huange checks what is about to leave. `Function 做完事情，接著要把結果交回去。`

## S13–S18 — Follow the data
- S13 Where does weather data come from? — Data Source Investigator. Traces line from function to weather data source instead of assuming data magically exists. `程式不會自己知道天氣；資料一定有來源。`
- S14 External data/API boundary — Boundary Inspector. Stands at external-source boundary; one hand receives outside data, one points to our app. `外部資料進來，就是一個系統邊界。`
- S15 JSON structure — JSON Unpacker. Opens nested JSON package and extracts only relevant fields such as location/temperature/time. `JSON 不是一坨文字；它有結構。`
- S16 Python data transformation — Data Transformer. Moves raw JSON cards through select/rename/convert pipeline into app-friendly object. `拿到資料，不等於能直接顯示。`
- S17 Data persistence question — System Thinker. Holds live-data card and asks whether some information must survive after request ends; points toward SQLite. `哪些資料只經過？哪些資料需要留下？`
- S18 SQLite = local persistent store — Database Librarian. Places structured record into SQLite drawer and retrieves an older one. `Database 讓資料在這次 Request 結束後還能被找到。`

## S19–S24 — SQLite and response path
- S19 Table / Row / Column — Database Organizer. Pulls one row from table, points to columns; maps a record to one observation. `Table 是結構；Row 是一筆資料。`
- S20 Write vs Read — Database Operator. Left action inserts/saves, right action queries/reads; two arrows clearly differentiated. `存進去和查出來，是兩種不同動作。`
- S21 Python ↔ SQLite — Adapter Engineer. Python function passes query to DB and receives rows back; Huange checks both directions. `Python 負責邏輯，SQLite 負責保存與查詢。`
- S22 Build the response — Response Builder. Combines selected data into response package; labels status/data lightly. `Server 要把結果包成 Browser 看得懂的 Response。`
- S23 Response travels back — Return Courier. Same visual callback as S05 but now response envelope travels Server→Browser. `去程是 Request；回程是 Response。`
- S24 Browser renders result — UI Renderer. Opens response package and places values into Weather Center UI fields. `Browser 收到資料後，才把結果變成你看到的畫面。`

## S25–S30 — Trace, explain, handoff
- S25 Complete request journey — System Navigator. Stands above the entire Browser→HTTP→Route→Function→Data/SQLite→Response→Browser path, follows one highlighted packet end-to-end. `現在我們終於看見一次點擊的完整旅程。`
- S26 Where can it fail? — Troubleshooter. Places neutral warning markers at request/route/data/database/response points; not security findings. `系統每一層都可能出錯，所以先學會定位。`
- S27 AI explains code, Human verifies — AI-assisted Code Reader. AI points to explanation; Huange traces actual route/function/data flow to verify it. `AI 可以幫我解釋，但我要回到 Code 與執行流程確認。`
- S28 Student Trace Lab — Coach. Gives student a Request Token and blank flow worksheet; student avatar must trace it, Huange does not solve it. `不要只說「看懂了」；把 Request 走一遍。`
- S29 Evidence: explain your system — Reviewer. Student presents architecture/data-flow evidence; Huange checks Browser/Route/Function/Data/SQLite/Response chain. `能指出證據，才算真的理解。`
- S30 UNDERSTAND → SECURE — Handoff Guide. Holds transparent understood Weather Center and points toward next road `SCAN → FIND → FIX → TEST → RE-SCAN`; Semgrep remains only a preview label. `先知道系統怎麼工作，下一課才知道 Finding 落在哪裡。`

## L3 Visual callbacks
- S02 click/question → S25 full journey answer.
- S05 Client↔Server envelopes → S23 response return.
- S08 Route matcher → S09 route-function connector → S11 function execution.
- S17 persistence question → S18 SQLite answer → S21 Python/SQLite interaction.
- S03 simplified journey → S25 completed journey.
- S01 black box opens → S30 transparent understood system.

## Audit result
S01–S30: content-driven visual direction defined for every page.
Critical visual anchors: S03, S05, S08, S09, S15, S18, S21, S25, S28, S30.

## Character arc
System Explorer → Curious User → Data-flow Guide → Browser Operator → Messenger → Request Inspector → Traffic Controller → Route Dispatcher → Connector Engineer → Form Interpreter → Python Mechanic → Output Inspector → Data Source Investigator → Boundary Inspector → JSON Unpacker → Data Transformer → System Thinker → Database Librarian → Database Organizer → Database Operator → Adapter Engineer → Response Builder → Return Courier → UI Renderer → System Navigator → Troubleshooter → AI-assisted Code Reader → Coach → Reviewer → Handoff Guide.

## PPT generation failure conditions
A slide fails if Huange is only standing, pointing generically, thumbs-up, or repeating a previous pose without conceptual reason. The visual must let a student infer the slide's concept even before reading all text.