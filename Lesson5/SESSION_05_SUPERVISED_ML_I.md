# Session 5 — Supervised ML I：Classification Foundations

> Canonical session mapping: Session 5 uses the Lesson5 directory for historical compatibility; the previous ISO 27001 material remains preserved in `Lesson5/README.md` as legacy course knowledge and is now taught canonically in Lesson 14.

## Concept
Feature、Label、Training/Test Data、Generalization、Classification、Logistic Regression、KNN。

## Security Meaning
把「正常 / 可疑」或「Legitimate / Phishing」變成 supervised learning problem；同時強調 label quality 與資料偏差。

## Practical Lab
使用 instructor-approved phishing/security dataset：load → clean → feature selection → split → Logistic Regression / KNN → baseline evaluation。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson05-security-classification
  title: Build a supervised security classification baseline
  role: ml_security_engineer
context:
  project: AI Weather Security Center
  stack: [Python, pandas, scikit-learn]
learning_objectives:
  - understand features labels and generalization
  - build a reproducible classification baseline
requirements:
  - load an instructor-approved dataset
  - document features and label
  - split train and test data reproducibly
  - train Logistic Regression
  - train KNN as comparison
  - report baseline metrics
security_requirements:
  - document data provenance
  - do not expose private or live sensitive data
implementation_workflow:
  - inspect repository
  - state assumptions
  - implement minimal pipeline
  - add validation
  - run models
  - save evidence
deliverables:
  - classification code
  - dataset notes
  - baseline evaluation
final_report:
  include: [features, labels, split, metrics, limitations]
```

## Evidence
Dataset description、feature/label table、reproducible split、baseline metrics、Git evidence。

## Reflection
模型是在學習 attack pattern，還是在學習 dataset artifact？