# Lesson 2 — BUILD：Python FastAPI AI Weather Security Center

## Learning Goal
以 AI / Antigravity 協助學生建立 Python + FastAPI + SQLite 的 AI Weather Security Center，並保留原課程所有重要 Web Security 知識點。Lesson 2 不再一次把所有安全主題講完，而是先建立概念與系統，之後在 Red Team / Blue Team 再重複、深化與驗證。

## Course Flow

```text
PROMPT → FASTAPI → DATA → SQLITE → WEB → LOGIN → SECURITY EVENTS → ML/DL DATA → THREAT MODEL
```

## Primary Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
- HTML/CSS/JS or lightweight template frontend
- pytest
- Git / GitHub
- Antigravity

## System Architecture

```text
Weather API / Fake Sensor
        ↓
      FastAPI
        ↓
 SQLite / SQLAlchemy
   ┌────┼──────────┐
   ↓    ↓          ↓
Weather Users  Security Events
   ↓    ↓          ↓
Dashboard Login   Logs
```

Recommended tables:
- users
- weather_data
- login_events
- security_events

## Part A — Build the Application

1. Mission：AI Weather Security Center
2. Vibe Coding：bad prompt → structured requirement
3. FastAPI architecture：route / service / repository / model
4. Weather API / Fake Sensor
5. SQLite + SQLAlchemy：CONNECT / INSERT / SELECT
6. Dashboard：current / historical weather
7. Authentication：login / logout
8. Roles：viewer / operator / admin
9. Security event logging
10. pytest basics

## Part B — Security Knowledge Contract

下列原 Lesson 2 知識全部保留，但採 spiral learning：BUILD 先理解，ATTACK 再體驗，DEFEND 再修補。

### Password Security
- plaintext password forbidden
- password hashing
- salt and password-specific hashing
- never log raw passwords

### Session / Authentication Security
- HTTP is stateless
- authentication vs authorization
- secure session / cookie concepts
- timeout / logout
- server-side identity decision

### SQL Injection
核心：

> Never let untrusted data become SQL code.

```text
Data → SQL Code = danger
```

BUILD 階段教授 parameterized query / ORM；攻擊細節留到授權 Cyber Range。

### XSS / Output Handling
核心：

> Never let untrusted data become browser code.

- Stored in DB ≠ Trusted
- API Data ≠ Trusted
- AI Output ≠ Trusted
- encode / escape according to output context

### CSRF
核心：

```text
Trusted Browser → Unwanted Action
```

建立 CSRF / SameSite / HTTP method 等概念，後續在安全 Lab 深化。

### Access Control / Authorization

> Authentication：你是誰？
> Authorization：你可以做什麼？

Roles:
- viewer
- operator
- admin

概念：
- server-side authorization
- RBAC
- object-level authorization / IDOR concept
- least privilege
- default deny
- UI hidden ≠ secure

## Part C — Security Data for Later AI

Weather data 可包含：
- timestamp
- temperature
- humidity
- pressure
- wind_speed
- rainfall
- source_id
- device_id
- anomaly_flag

Security events 可包含：
- timestamp
- user_id
- source_ip
- endpoint
- event_type
- status_code
- success

這些資料後續供 Session 5–10 的 ML / DL 使用。

## Part D — Lab / Production Separation

同一課程專案必須區分：

```text
Secure Production App
      ↓
    Vercel
 demo / non-destructive verification

Local Cyber Range
      ↓
 Docker / VM
      ↓
 teacher-controlled vulnerable labs
```

Lab-only vulnerable code 不應只靠一個 production environment variable 就能開啟；應採獨立路由/package/build boundary，避免被誤部署到公開 Internet。

## Part E — Threat Modeling

找出 Attack Surface：
- login
- password
- session
- form / JSON input
- database query
- browser output
- authorization
- weather API
- dependencies
- logs
- ML data/model
- deployment environment

Ending question:

> BUT... IS IT SECURE?

## Antigravity YAML Prompt — Build Core Weather App

```yaml
task:
  id: weather-build-001
  title: Build the AI Weather Security Center core application
  role: senior_python_fastapi_security_engineer

context:
  stack:
    language: Python
    backend: FastAPI
    database: SQLite
    orm: SQLAlchemy
    testing: pytest
  deployment:
    local: SQLite
    public_demo: secure_build_only

learning_objectives:
  - understand REST API and FastAPI structure
  - understand database persistence
  - understand authentication vs authorization
  - create security-relevant logs for later ML

requirements:
  endpoints:
    - /login
    - /logout
    - /weather
    - /weather/history
    - /api/weather
    - /admin
  roles:
    - viewer
    - operator
    - admin
  database_tables:
    - users
    - weather_data
    - login_events
    - security_events

security_requirements:
  - never store plaintext passwords
  - use server-side authorization
  - use parameterized queries or ORM
  - validate external API and user input
  - avoid sensitive error leakage
  - record authentication and authorization events

implementation_workflow:
  - inspect repository first
  - state assumptions
  - propose minimal architecture
  - implement smallest working vertical slice
  - add tests
  - run tests
  - perform security review
  - update README

constraints:
  - do not create publicly deployable vulnerable endpoints
  - lab-only vulnerabilities must remain outside the production build
  - keep code readable for students

final_report:
  include:
    - architecture
    - files_changed
    - tests_run
    - test_results
    - security_controls
    - unresolved_risks
```

## Spiral Learning Map

```text
Week 3 BUILD
Understand the control
      ↓
Week 11–12 ATTACK
Observe the weakness in authorized labs
      ↓
Week 13 DEFEND
Find root cause and patch
      ↓
Week 14 GOVERN
Translate finding into organizational risk
```

## Core Message

> The Weather App is not a one-week web assignment. It is the semester-long AI Cyber Range project.