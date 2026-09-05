# Lesson 10 — Deep Learning II：Security Sequence Analysis

## Mission
理解很多攻擊不是單一 event，而是一段時間序列。

## Concept
CNN concept、sequence data、sliding window、LSTM / GRU concept、temporal dependency。

## Security Meaning
`login fail → login fail → login success → privilege change → suspicious command` 單看每筆可能正常，合起來可能形成 attack story。

## Practical Lab
把 security_events 轉為時間序列 window，建立小型 sequence classifier 或使用教師資料比較 rule-based / ML / sequence model。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson10-security-sequence
  title: Build a security-event sequence analysis lab
  role: deep_learning_security_engineer
context:
  project: AI Weather Security Center
  stack: [Python, pandas, PyTorch]
learning_objectives:
  - understand temporal security patterns
  - understand sequence windows and labels
requirements:
  - transform approved security events into ordered sequences
  - create fixed-length windows
  - implement a small sequence-model example
  - compare with a simple rule-based baseline
security_requirements:
  - avoid using live sensitive logs
  - document sequence-label assumptions
implementation_workflow:
  - inspect event schema
  - validate chronological ordering
  - build windows
  - train or run instructor-approved model
  - evaluate and explain results
tests:
  - timestamps are ordered
  - window construction is deterministic
deliverables:
  - sequence preparation code
  - model or notebook
  - comparison report
final_report:
  include: [sequence_definition, model_result, baseline_result, limitations]
```

## Reflection
哪些 security incidents 必須看「順序」才能辨識？