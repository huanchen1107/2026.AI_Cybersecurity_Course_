# AIIS_L3 — UNDERSTAND：Python × FastAPI × API × JSON × Web App

> **Status: CANONICAL ALLOCATION — 2026-09-07**
>
> Earlier versions assigned AI Red Team / Kali to Lesson 3. That allocation is superseded. Red Team remains preserved in the 16-Lesson Master Curriculum at **AIIS_L11–L12**. L3 now owns the programming and web-application understanding required to understand the Weather Security Center built in L1 and managed in L2.

## Mission

核心問題：

> AI 可以幫我寫程式，但這些 Python、API、JSON 和 FastAPI 到底在做什麼？

Students do not build a new application. They use the same Weather Security Center and learn to read its essential data flow.

## Core Flow

```text
PYTHON
  ↓
FUNCTION / VARIABLE / DATA
  ↓
HTTP REQUEST / RESPONSE
  ↓
API
  ↓
JSON
  ↓
FASTAPI ROUTE
  ↓
FRONTEND ↔ BACKEND
  ↓
WEATHER DATA FLOW
```

## Primary Topics

1. Python as the implementation language
2. variables / basic types / list / dict
3. functions and simple control flow
4. modules/imports at project-reading level
5. What is HTTP?
6. request and response
7. What is an API?
8. REST-style endpoint concept
9. What is JSON?
10. Python dict ↔ JSON mental model
11. FastAPI route
12. path / query / body concepts at introductory level
13. frontend vs backend
14. external CWA API → backend → frontend data flow
15. basic persistence/database position in architecture
16. trace one request through the Weather Security Center

## Required Lab

Students choose one visible feature from the existing Weather Security Center and trace it:

```text
Browser action
→ HTTP request
→ FastAPI route
→ Python processing
→ external API / local data when applicable
→ JSON / response
→ browser display
```

Students should be able to explain the path in their own words and identify the relevant files.

## Evidence

- feature selected
- request/response explanation
- endpoint
- relevant Python function/route
- sample JSON
- frontend/backend boundary
- simple data-flow diagram
- AI explanation reviewed by student

## Responsibility Boundary

L3 does **not** become:
- another broad AI-tool lesson → L2 owns engineering workflow
- formal Semgrep remediation → L4
- Red Team / Kali / TryHackMe → L11–L12
- Blue Team repair → L13

## Core Statement

> **DON'T JUST RUN THE CODE. UNDERSTAND THE FLOW.**

Handoff to L4:

> Once we understand where data and trust cross the application, we can systematically inspect the code for security problems.