# Lesson 6 — Supervised ML II：Tree Models for Cybersecurity

## Mission
把 Lesson 5 的分類概念推進到 Decision Tree 與 Random Forest，使用安全事件／網路流量資料建立可解釋的 intrusion classifier。

## Concept
- Decision Tree：以 feature 條件逐層切分資料。
- Random Forest：多棵 tree 投票，降低單一 tree 過度擬合風險。
- Feature Importance：協助理解哪些特徵影響模型判斷。
- Generalization：模型要能處理沒看過的資料，而不是背答案。

## Security Meaning
IDS 不只需要輸出 Attack / Normal，也要能回答「為什麼」。本課將 explainability 與 security evidence 連結。

## Practical Lab
Security Events / IDS dataset → pandas → train/test → Decision Tree → Random Forest → compare metrics → feature importance。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson06-tree-security-ml
  title: Build Decision Tree and Random Forest security classifiers
  role: ml_security_engineer
context:
  project: AI Weather Security Center
  stack: [Python, pandas, scikit-learn, pytest]
learning_objectives:
  - understand decision trees and random forests
  - compare generalization
  - interpret feature importance
requirements:
  - load an instructor-approved security dataset
  - create reproducible train/test split
  - train DecisionTreeClassifier
  - train RandomForestClassifier
  - compare metrics
  - output feature importance
security_requirements:
  - do not treat model output as automatic authority
  - document dataset assumptions and label limitations
implementation_workflow:
  - inspect repository first
  - state assumptions
  - make a minimal plan
  - implement training pipeline
  - add tests
  - run tests
  - summarize evidence
  - document unresolved risks
tests:
  - dataset schema validation passes
  - training pipeline runs reproducibly
  - predictions use expected labels
deliverables:
  - training code
  - evaluation output
  - feature importance report
  - README update
final_report:
  include: [files_changed, metrics, important_features, limitations, tests_run]
```

## Evidence
模型比較表、Feature Importance、測試結果、Git commit。

## Reflection
哪一個 feature 看似重要但可能只是資料集偏差？Random Forest 比單一 Tree 好，是否代表它一定適合 production？