# 2026-09-05 Knowledge Traceability & Weather Migration

## Purpose

本文件確保舊版 PHP/MySQL Weather 課程的重要知識不因 Python/FastAPI 升級而遺失。

原則：

> Replace the implementation stack, preserve the knowledge contract, deepen the learning cycle.

## Stack Migration

| Old | New |
|---|---|
| PHP | Python |
| PHP Web App | FastAPI |
| MySQL-first classroom stack | SQLite + SQLAlchemy local/lab |
| XAMPP/Laragon | Python venv / FastAPI runtime / Docker optional |
| phpMyAdmin | SQLite/DB tools + Python/ORM inspection |
| PHP password/session examples | Python/FastAPI security patterns |
| One Lesson 2 security block | Spiral BUILD → ATTACK → DEFEND → GOVERN |
| ML/DL extension inside one lesson | 3 supervised ML sessions + 2 DL sessions |

## Knowledge Traceability Matrix

| Knowledge Point | BUILD | LEARN | ATTACK | DEFEND | GOVERN |
|---|---|---|---|---|---|
| Prompt / Vibe Coding | S2-S3 | — | AI-assisted analysis | AI-assisted patch | AI-assisted risk summary |
| FastAPI / API | S3 | data source | S11-S12 attack surface | S13 hardening | S14 asset/control |
| Database / SQL | S3 | ML data source | S12 injection lab | S13 ORM/parameterized query | S14 data risk |
| Password Hashing | S3 concept + implementation | — | S11-S12 auth lab concept | S13 verify controls | S14 identity risk |
| Session Security | S3 concept | — | S12 session/auth lab | S13 secure session behavior | S14 access risk |
| Authentication | S3 | security event features | S11-S12 validation | S13 repair | S14 identity controls |
| Authorization / RBAC | S3 | role/event features | S12 broken access-control lab | S13 server-side RBAC | S14 least privilege controls |
| SQL Injection | S3 prevention concept | — | S12 authorized lab | S13 root-cause fix + regression | S14 application/data risk |
| XSS / Output Safety | S3 concept | — | S12 authorized lab | S13 safe rendering/output | S14 application risk |
| CSRF | S3 concept | — | S12 controlled scenario where applicable | S13 state-change controls | S14 application risk |
| Input Validation | S3 | feature/data cleaning link | S11-S12 malformed input observations | S13 boundary validation | S14 data integrity risk |
| Security Logging | S3 events | S5-S10 dataset | S11-S12 evidence | S13 detection/logging | S14 monitoring controls |
| Dependency Risk | S2-S3 awareness | model/library dependencies | reconnaissance/context | S13 supply-chain review | S14 supplier/control risk |
| Threat Modeling | S4 | features/attack hypotheses | validates threat assumptions | drives repairs | S14 formal risk |
| ML | data created S3 | S5-S7 | supports detection interpretation | detection tuning | model risk |
| Deep Learning | data/sequence foundation | S9-S10 | attack-sequence context | detection architecture | model governance |
| Evidence | Git/test evidence | metric evidence | S11-S12 findings | S13 regression evidence | S14 control evidence |

## Why Security Topics Are Not Removed

Old model:

```text
Lesson 2
Password → Session → SQLi → XSS → CSRF → Access Control → AI → ML/DL → Threat Model
```

New model:

```text
Week 3 BUILD
learn the safe engineering concept
       ↓
Week 11-12 ATTACK
observe what failure looks like in authorized labs
       ↓
Week 13 DEFEND
repair root cause and prove the patch
       ↓
Week 14 GOVERN
translate evidence into risk and controls
```

The new model intentionally repeats important concepts so students learn them as engineering behavior, not isolated vocabulary.

## Weather App → Semester Cyber Range

The Weather App becomes a shared system containing:

### Functional Data
- weather_data
- sensor/source data

### Identity Data
- users
- roles
- authentication state

### Security Telemetry
- login_events
- security_events
- endpoint / status / success / source metadata

These enable a single project to support Web Engineering, ML, DL, Red Team, Blue Team, and Governance.

## TryHackMe Integration

TryHackMe is not connected as a technical backend to Weather App.

It is connected pedagogically:

```text
TryHackMe
Learn standardized technique
       ↓
AI explains observations
       ↓
Student forms hypothesis
       ↓
Weather Local Cyber Range
Transfer the same reasoning
       ↓
Evidence-based finding
       ↓
FastAPI code repair
```

This avoids turning a public deployment into a classroom target while still giving students real offensive-security experience under explicit authorization.

## Production Boundary

Vulnerable teaching code must not be included in a public production build by default.

Recommended separation:

```text
project/
  app/                 # secure production application
  labs/                # local-only cyber-range material
  tests/
  ml/
  reports/
```

Production deployment process must exclude `labs/` or otherwise guarantee vulnerable lab endpoints cannot be enabled publicly.

## Curriculum Design Rule Going Forward

When expanding any future lesson, always verify:

1. Which existing knowledge point is being preserved?
2. Where was it first introduced?
3. Where is it practiced?
4. Where is it attacked/validated?
5. Where is it repaired?
6. What evidence proves learning?
7. What Antigravity YAML prompt lets the student implement it?

This traceability rule is mandatory for future course development.