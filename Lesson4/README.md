# Lesson 4 — AI Blue Team：OWASP Secure Coding × FastAPI Repair

## Goal
把 Lesson 3 在 TryHackMe / Weather Cyber Range 找到的問題，轉成可驗證、可測試、可追蹤的修補。學生不是只叫 AI「幫我修」，而是完整走過 Root Cause → Minimal Fix → Regression Test → Evidence。

## Secure Repair Workflow

```text
Red-Team Finding
      ↓
Reproduce in Authorized Lab
      ↓
Root Cause
      ↓
AI-assisted Minimal Fix
      ↓
Human Review
      ↓
pytest / Integration Test
      ↓
Security Regression Test
      ↓
Evidence
      ↓
Close Finding
```

## Main Topics

1. Finding → Root Cause → Fix → Test
2. OWASP Top 10 導讀
3. Broken Access Control / RBAC
4. Authentication and session failures
5. Injection / parameterized query / ORM
6. XSS / safe output handling
7. CSRF concept and state-changing requests
8. Security Misconfiguration
9. Software Supply Chain / dependencies
10. Cryptographic failures and password handling
11. Logging / Alerting
12. Exceptional conditions / safe error handling
13. CWE Top 25 導讀
14. AI-assisted secure code review
15. Security regression testing

## Lesson 2 Controls Revisited

- password hashing
- session / identity handling
- server-side authorization
- parameterized query / SQLAlchemy ORM
- output encoding
- CSRF-related controls where applicable
- API key management
- external input validation
- rate limiting concepts
- security logging

## Required Lab

學生選擇 Lesson 3 的 Finding，在 Local Weather Cyber Range：

1. Reproduce original weakness
2. Identify root cause in FastAPI/Python code
3. Ask AI/Antigravity for smallest secure patch
4. Review the patch manually
5. Add pytest regression test
6. Re-run the same security validation
7. Demonstrate the vulnerability is no longer reproducible
8. Record before/after evidence

## Antigravity YAML Prompt — Secure Repair

```yaml
task:
  id: blueteam-repair-001
  title: Repair a verified Weather Cyber Range finding
  role: senior_fastapi_application_security_engineer

context:
  project: AI Weather Security Center
  source_of_truth: verified_red_team_finding
  stack:
    language: Python
    backend: FastAPI
    database: SQLite
    orm: SQLAlchemy
    testing: pytest

learning_objectives:
  - identify root cause instead of patching symptoms
  - apply OWASP secure coding controls
  - create security regression tests
  - distinguish AI suggestion from human-approved fix

workflow:
  - inspect the finding and existing code
  - reproduce only inside the authorized local lab
  - explain the root cause
  - identify affected trust boundary
  - propose the smallest secure change
  - do not rewrite unrelated code
  - implement the approved fix
  - add unit_or_integration_tests
  - add security_regression_test
  - run the complete relevant test suite
  - compare before_and_after behavior

security_requirements:
  - enforce authorization server_side
  - keep untrusted data separate from SQL code
  - validate inputs at trust boundaries
  - handle browser output safely
  - avoid leaking sensitive errors
  - log security-relevant failures without secrets

constraints:
  - no production exploitation
  - no unrelated refactoring
  - do not weaken another security control to make tests pass

final_report:
  include:
    - finding_id
    - root_cause
    - files_changed
    - patch_summary
    - tests_added
    - test_results
    - before_after_evidence
    - residual_risk
    - ai_suggestion_vs_human_decision
```

## Core Message

> AI can suggest a patch. A secure engineering process proves that the patch actually works.