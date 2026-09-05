# Lesson 13 — AI Blue Team：Fix Our Code with OWASP Secure Coding

## Mission
攻擊成功不是終點。把 Lesson 12 findings 轉成 root cause、minimal patch、tests 與 regression evidence。

## Concept
OWASP Top 10、CWE、Defense in Depth、Root Cause、Minimal Patch、Security Regression Test。

## Security Meaning
AI 可以建議 patch，但只有測試與重新驗證能證明修補是否有效。

## Practical Lab
Finding → reproduce → root cause → AI-assisted review → human review → FastAPI patch → pytest → repeat security test → close finding。

重點保留原 Weather Web 知識：Password Hashing、Session、Parameterized Query/ORM、Output Safety、CSRF concepts、Authorization/RBAC、API Security、Logging、Dependency Risk、Safe Errors。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson13-blue-team-repair
  title: Repair verified Weather Cyber Range findings
  role: senior_python_security_engineer
context:
  project: AI Weather Security Center
  stack: [Python, FastAPI, SQLAlchemy, pytest]
learning_objectives:
  - connect vulnerability evidence to root cause
  - implement minimal secure fixes
requirements:
  - read red-team finding before changing code
  - reproduce finding in authorized local lab
  - identify affected trust boundary
  - implement smallest secure patch
  - add regression test
  - rerun security validation
security_requirements:
  - do not hide symptoms without fixing root cause
  - preserve server-side authorization
  - validate untrusted input
  - avoid sensitive error leakage
implementation_workflow:
  - inspect finding and repository
  - state assumptions
  - reproduce
  - explain root cause
  - patch minimally
  - run unit integration and security regression tests
  - document before and after evidence
deliverables:
  - code patch
  - pytest regression tests
  - blue-team repair report
final_report:
  include: [finding_id, root_cause, files_changed, tests_run, before_after_evidence, residual_risk]
```

## Reflection
「攻擊現在失敗」是否一定代表漏洞真的修好了？如何排除只是 UI 或測試方式改變？