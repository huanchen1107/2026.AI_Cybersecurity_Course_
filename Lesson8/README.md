# Lesson 8 — Midterm AI Security Engineering Review

## Mission
期中不是只有投影片報告，而是第一次 Engineering Review：證明系統、資料、ML 與 Threat Model 已經可以連起來。

## Required Review
1. Problem Statement
2. Architecture
3. Asset / Threat / Trust Boundary
4. Dataset and Features
5. Baseline supervised ML model
6. Confusion Matrix / Precision / Recall / F1
7. Security interpretation
8. Working demo
9. GitHub evidence
10. Next-step plan

## Security Meaning
學生必須區分「模型分數」與「安全價值」，並說明資料、模型、API、帳號與部署本身都可能是資產與攻擊面。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson08-midterm-review
  title: Prepare the midterm AI security engineering review
  role: technical_project_reviewer
context:
  project: student_ai_cybersecurity_project
learning_objectives:
  - integrate software security and ML evidence
requirements:
  - inspect current repository
  - summarize architecture
  - identify assets threats and trust boundaries
  - summarize dataset and features
  - reproduce baseline ML evaluation
  - identify missing evidence
  - create a midterm review checklist
security_requirements:
  - distinguish assumptions from verified evidence
  - do not invent test results
implementation_workflow:
  - inspect repository
  - run available tests
  - run reproducible ML evaluation if available
  - identify gaps
  - prepare review summary
deliverables:
  - midterm-review.md
  - evidence checklist
  - unresolved-risk list
final_report:
  include: [working_features, metrics, security_evidence, missing_items, next_actions]
```

## Evidence
Live demo + repository + metrics + threat model + test evidence。

## Reflection
如果今天這個專案要交給另一組接手，他們能不能只靠 GitHub 重現你的結果？