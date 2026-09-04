# Lesson 4 — AI Blue Team：OWASP Secure Coding 與修補

## Goal
把 Lesson 3 找到的問題轉成可驗證的修補，讓學生學會 AI-assisted secure coding，而不是只叫 AI「幫我修安全」。

## Main Topics
1. Finding → Root Cause → Fix → Test
2. OWASP Top 10 導讀
3. Broken Access Control
4. Security Misconfiguration
5. Software Supply Chain Failures
6. Cryptographic Failures
7. Injection
8. Insecure Design
9. Authentication Failures
10. Software / Data Integrity Failures
11. Security Logging and Alerting Failures
12. Exceptional Conditions / Error Handling
13. CWE Top 25 導讀
14. Dependency / GitHub Dependency Graph / Software Supply Chain
15. AI Code Review：先列 finding，再做最小修補

## Secure Repair Workflow

```text
Red-team Finding
      ↓
Reproduce
      ↓
Root Cause
      ↓
Minimal Fix
      ↓
Unit / Integration Test
      ↓
Security Regression Test
      ↓
Evidence
      ↓
Close Finding
```

## AI Review Prompt Pattern

```text
You are a secure-code reviewer.

For this finding:
1. explain the root cause
2. identify the affected trust boundary
3. propose the smallest secure fix
4. define a regression test
5. do not rewrite unrelated code
```

## Lesson 2 Controls Revisited
- Password hashing
- Session security
- Prepared statements
- Output encoding
- CSRF
- Authorization
- API key management
- AI input/output validation
- Rate limiting

## Deliverable
每組提交一份 Blue-Team Repair Report：
- Finding ID
- Root cause
- Patch summary
- Before / after behavior
- Test evidence
- Residual risk
- AI-generated suggestion vs human-verified final decision

## Core Message
> AI can suggest a patch. A secure engineering process proves that the patch actually works.
