# AIIS_L3 — Python FastAPI Weather Security Center
## Detailed Lecture Plan — UNDERSTAND

Date: 2026-09-07
Status: In progress
Canonical Standard: `_myplan_/AIIS-COURSE-DESIGN-STANDARD.md`

## Lesson Position

```text
L0 ORIENTATION
→ L1 BUILD
→ L2 MANAGE
→ L3 UNDERSTAND
→ L4 SECURE
```

## Primary Mission

> Understand how the same AI Weather Security Center actually works.

學生不只要能讓 AI 產生程式，而要能沿著一次真實 request 解釋：

```text
Browser
→ HTTP Request
→ FastAPI Route
→ Python Function
→ Data / Database
→ JSON Response
→ Browser
```

核心問題：

> AI 幫我把系統做出來了，但我真的懂它嗎？

## THIS LESSON OWNS

- Python / FastAPI 程式結構理解
- HTTP Request / Response 基本概念
- REST API 與 endpoint
- FastAPI route / function / parameter
- `/docs` 作為 API inspection interface
- Weather / sensor data flow
- SQLite / SQLAlchemy 基本資料流概念
- Input / output validation 基本理解
- Trace → Explain → Modify → Test → Evidence

## THIS LESSON DOES NOT OWN

- 不重新教授 L1 的完整 Vibe Coding workflow
- 不重新教授 L2 的 change/spec/review 管理流程
- 不正式教授 SAST / Semgrep（L4）
- 不正式教授 ML / DL
- 不進入 Red Team / offensive testing
- 不建立另一個新 App
- 不要求學生學習多個 Python web frameworks

## Preview → Teach → Reuse

| Concept | Earlier | L3 | Later |
|---|---|---|---|
| AI coding | L1 TEACH | REUSE | REUSE |
| Git/evidence | L1/L2 TEACH | REUSE | REUSE |
| FastAPI | L1 PREVIEW/USE | **TEACH** | REUSE |
| HTTP/API | PREVIEW | **TEACH** | REUSE |
| SQLite data flow | PREVIEW | **TEACH BASIC** | REUSE |
| Input validation | PREVIEW | **TEACH BASIC** | L4 security context REUSE |
| SAST/Semgrep | PREVIEW only | PREVIEW | **L4 TEACH** |

# Lesson Storyline

```text
AI BUILT IT
    ↓
BUT DO I UNDERSTAND IT?
    ↓
FOLLOW ONE REQUEST
    ↓
Browser → HTTP → FastAPI
    ↓
Route → Function → Data
    ↓
SQLite / Weather Data
    ↓
Validation → Response
    ↓
TRACE IT
    ↓
EXPLAIN IT
    ↓
MODIFY IT
    ↓
TEST IT
    ↓
PROVE IT WITH EVIDENCE
    ↓
NEXT: CAN THIS CODE BE INSECURE?
    ↓
L4 SECURE
```

# Slide Purpose Map

## Slide 00 — AIIS_L3: UNDERSTAND
Course positioning. L1 built, L2 managed; L3 opens the system and understands how it actually works.

## S01 — AI 寫好了，所以完成了嗎？
Create the central tension: working code is not the same as understood code.

## S02 — BUILD → MANAGE → UNDERSTAND
Place L3 precisely in the semester journey.

## S03 — 今天只追一件事：一個 Request
Reduce complexity by following one request end-to-end.

## S04 — Weather Security Center 裡到底有什麼？
Show the system as layers instead of a mysterious AI-generated codebase.

## S05 — 黑箱 vs 透明系統
Contrast “it works” with “I can explain why it works.”

## S06 — Browser 做了什麼？
Introduce client action and URL/request concept.

## S07 — HTTP Request 是一封有格式的信
Explain method, path, parameters, headers at an introductory level.

## S08 — GET 到底代表什麼？
Teach GET using the Weather Security Center context.

## S09 — Server 收到 Request 之後呢？
Transition from HTTP into FastAPI.

## S10 — Response：Server 回了什麼？
Introduce status code, body and JSON.

## S11 — FastAPI 是交通警察
Explain routing responsibility.

## S12 — `@app.get()` 是什麼？
Connect HTTP GET to a concrete FastAPI route decorator.

## S13 — Route → Python Function
Show that an endpoint eventually executes ordinary Python logic.

## S14 — Parameter 從哪裡進來？
Path/query parameters mapped into Python values.

## S15 — Return 為什麼變成 JSON？
Connect Python object to API response.

## S16 — `/docs`：API 的 X 光機
Use Swagger UI to inspect and execute endpoints.

## S17 — 天氣資料從哪裡來？
Introduce the source of weather/fake sensor data without expanding into a data-engineering lesson.

## S18 — Data Flow：Source → Python → API
Trace data through the application.

## S19 — 為什麼需要 Database？
Explain persistence through a simple Weather Security Center example.

## S20 — SQLite：我們的本地資料櫃
Teach the minimum database mental model needed for this project.

## S21 — SQLAlchemy：Python 與 Database 的翻譯員
Explain ORM concept at a conceptual level.

## S22 — 使用者輸入一定正確嗎？
Introduce the need for validation through benign malformed input.

## S23 — FastAPI 如何幫我們檢查輸入？
Explain types/Pydantic/FastAPI validation at teaching depth appropriate for L3.

## S24 — 正常 Request vs 錯誤 Request
Compare successful and rejected inputs and responses.

## S25 — Validation 也是 Security 的入口
Preview—not teach—L4: untrusted input becomes a security concern.

## S26 — LAB 1: Trace It
Students choose one existing endpoint and trace request → route → function → data → response.

## S27 — LAB 2: Explain It
AI may explain the code, but students must verify the explanation against source and execution.

## S28 — LAB 3: Modify It
Make one controlled endpoint change without creating a new application.

## S29 — LAB 4: Test It & Prove It
Use `/docs` and a basic/automated test to produce evidence that the modification behaves as expected.

## S30 — I Can Explain What My Code Does
Close L3 with evidence and handoff: understanding code makes the next question possible — is the code secure?

# Lab Contract

```text
TRACE
→ EXPLAIN
→ MODIFY
→ TEST
→ EVIDENCE
```

Students must produce:

1. Selected endpoint/path
2. Request example
3. Route/function location
4. Short data-flow explanation
5. Controlled code modification
6. Before/after API result
7. `/docs` verification
8. Basic or automated test result
9. Student explanation in their own words

AI can assist explanation and modification, but the student owns verification.

# Evidence Artifact

Minimum evidence package:

```text
Endpoint
+ Request
+ Source trace
+ Student explanation
+ Controlled change
+ Test
+ Before/After evidence
```

Success statement:

> I can trace, explain, modify, and test one FastAPI endpoint in our Weather Security Center.

# Handoff to L4

L3 ends with:

> 現在我們知道程式怎麼運作了。下一個問題不是「它會不會跑」，而是「它安全嗎？」

```text
L3 UNDERSTAND
I can explain what my code does.
        ↓
L4 SECURE
Can this code contain a vulnerability?
        ↓
Semgrep
→ Finding
→ Evaluate
→ Fix
→ Re-scan
```

L3 may preview security implications of validation, but Semgrep/SAST remains owned by L4.
