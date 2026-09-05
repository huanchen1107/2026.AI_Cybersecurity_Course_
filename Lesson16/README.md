# Lesson 16 — Final Project Demo II & Course Closure

## Mission
完成第二批 Final Demo，並把整學期工程證據整理成可重現、可交接的 final package。

## Course Closure
```text
BUILD
Python / FastAPI / SQLite
  ↓
LEARN
Supervised ML / DL
  ↓
ATTACK
Authorized Range / Weather Cyber Range
  ↓
DEFEND
OWASP / Secure Coding / Regression Test
  ↓
GOVERN
Risk / ISO 27001
```

## Final Repository Evidence
- README / setup instructions
- architecture
- threat model
- dataset description
- ML evaluation
- optional DL evaluation
- authorized red-team report
- blue-team repair report
- security regression tests
- risk register
- AI usage statement
- known limitations / residual risks

## Antigravity YAML Prompt
```yaml
task:
  id: lesson16-final-handoff
  title: Prepare reproducible final AI cybersecurity project handoff
  role: senior_engineering_handoff_reviewer
context:
  project: student_final_project
learning_objectives:
  - make engineering work reproducible and auditable
requirements:
  - inspect full repository
  - verify setup instructions
  - verify tests and evidence references
  - identify stale or contradictory documentation
  - summarize architecture data model security findings fixes and risks
  - produce final handoff checklist
security_requirements:
  - remove secrets and credentials from documentation
  - ensure vulnerable lab components are clearly isolated
  - do not claim unresolved findings are fixed
implementation_workflow:
  - inspect repository
  - run safe available tests
  - verify documentation against code
  - flag missing evidence
  - prepare final handoff report
deliverables:
  - FINAL_HANDOFF.md
  - reproducibility checklist
  - known-limitations section
final_report:
  include: [system_status, test_status, security_status, ml_status, residual_risks, handoff_notes]
```

## Final Reflection
學生應能回答：AI 做了什麼？人驗證了什麼？哪個 finding 有證據？哪個 risk 還存在？如果明天交給另一位工程師，他能不能重現？

> AI proposes. Human understands. Lab authorizes. Evidence proves.