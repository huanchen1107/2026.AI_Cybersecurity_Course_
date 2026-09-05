# Lesson 9 — Deep Learning I：Neural Networks for Security

## Mission
從 classical ML 進入 Neural Network，但不預設 DL 一定比較好。

## Concept
Neuron、Layer、Weight、Activation、Loss、Gradient / Backpropagation concept、Epoch、Overfitting、MLP、PyTorch training loop。

## Security Meaning
Security data 可以使用 neural network，但模型複雜度、可解釋性、運算成本與錯誤成本都必須評估。

## Practical Lab
同一份 security classification data：Random Forest baseline vs PyTorch MLP。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson09-pytorch-security-mlp
  title: Build and compare a PyTorch MLP security classifier
  role: deep_learning_security_engineer
context:
  project: AI Weather Security Center
  stack: [Python, pandas, scikit-learn, PyTorch]
learning_objectives:
  - understand neural-network training pipeline
  - compare DL with classical ML baseline
requirements:
  - reuse an approved security dataset
  - preprocess features consistently
  - build a small MLP
  - train with reproducible settings
  - evaluate using security metrics
  - compare against Random Forest baseline
security_requirements:
  - document overfitting risk
  - do not claim DL is better without evidence
implementation_workflow:
  - inspect prior ML pipeline
  - preserve comparable split
  - implement minimal MLP
  - train evaluate and compare
  - document limitations
tests:
  - tensor dimensions are validated
  - inference output maps to expected labels
deliverables:
  - PyTorch model code
  - training history
  - comparison report
final_report:
  include: [architecture, metrics, baseline_comparison, limitations]
```

## Reflection
如果 Random Forest 表現相同甚至更好，為什麼仍有人使用 DL？