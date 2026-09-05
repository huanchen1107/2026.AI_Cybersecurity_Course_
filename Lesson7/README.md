# Lesson 7 — Supervised ML III：Security Evaluation

## Mission
從「模型會預測」進入「模型是否真的適合資安」。

## Concept
Confusion Matrix、Precision、Recall、F1、ROC-AUC concept、threshold、class imbalance、false positive、false negative。

## Security Meaning
99% Accuracy 可能是一個完全無用的 IDS。若 9,900 筆 Normal、100 筆 Attack，而模型全部猜 Normal，Accuracy 仍有 99%，但 100 個攻擊全部漏掉。

## Practical Lab
比較 Logistic Regression / Random Forest，調整 threshold，觀察 FP/FN 對 SOC / IDS 的不同成本。SVM / XGBoost 作延伸概念。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson07-security-evaluation
  title: Evaluate security classifiers beyond accuracy
  role: ml_security_evaluation_engineer
context:
  project: AI Weather Security Center
  stack: [Python, pandas, scikit-learn]
learning_objectives:
  - understand confusion matrix
  - interpret precision recall and F1 in security context
  - understand class imbalance and thresholds
requirements:
  - evaluate at least two classifiers
  - calculate confusion matrix precision recall F1
  - demonstrate an imbalanced-data accuracy trap
  - compare at least two decision thresholds where supported
security_requirements:
  - explicitly discuss false-negative security impact
  - never claim accuracy alone proves security value
implementation_workflow:
  - inspect existing Lesson 5 and 6 artifacts
  - reuse dataset pipeline where possible
  - implement evaluation
  - generate human-readable security interpretation
  - run tests
tests:
  - metric calculations are reproducible
  - confusion matrix dimensions are valid
deliverables:
  - evaluation script
  - metric comparison
  - security interpretation
  - README update
final_report:
  include: [metrics, false_positive_analysis, false_negative_analysis, recommended_threshold, limitations]
```

## Evidence
Confusion Matrix、模型比較、threshold experiment、security interpretation。

## Reflection
對你的 security mission 而言，漏掉一次攻擊和多發一次警報的成本相同嗎？