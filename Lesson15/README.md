# Lesson 15 — Final Project Demo I

## Mission
第一批團隊完成完整 `BUILD → LEARN → ATTACK → DEFEND → GOVERN` 故事，而不是展示互不相干的功能。

## Required Demo Story
1. Problem and Asset
2. Working System
3. Architecture / Trust Boundaries
4. Dataset / Features
5. Supervised ML model
6. Security-oriented evaluation
7. Optional DL comparison
8. Authorized Red-Team Finding
9. Blue-Team Fix
10. Security Regression Evidence
11. Risk / Control / Residual Risk
12. AI Usage Statement

## Antigravity YAML Prompt
```yaml
task:
  id: lesson15-final-demo-readiness
  title: Audit final project demo readiness
  role: final_security_project_reviewer
context:
  project: student_final_project
requirements:
  - inspect repository and reports
  - verify required final-project evidence exists
  - run available tests
  - identify broken demo dependencies
  - create a presentation evidence checklist
security_requirements:
  - do not invent missing results
  - offensive evidence must come from authorized lab scope
  - production demo must not expose intentionally vulnerable lab components
implementation_workflow:
  - inspect
  - verify
  - run tests
  - list gaps
  - recommend minimal fixes before presentation
deliverables:
  - final-demo-readiness.md
  - evidence checklist
  - unresolved-risk list
final_report:
  include: [ready_items, missing_items, test_results, security_warnings, demo_order]
```

## Evaluation Focus
Correctness、security reasoning、ML evidence、attack/defense evidence、reproducibility、communication。

## Reflection
觀眾能否清楚看到「問題 → AI/ML → 攻擊 → 修補 → 風險」是一條因果鏈？