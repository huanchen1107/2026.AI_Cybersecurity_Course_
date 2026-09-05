# Lesson 14 — GOVERN：ISO 27001 × Risk Management

## Mission
把技術 finding、ML/DL evidence、Red/Blue Team 結果提升到治理層。

## Concept
Asset、Threat、Vulnerability、Likelihood、Impact、Risk、Control、Risk Treatment、Residual Risk、ISO/IEC 27001:2022、Statement of Applicability concept。

## Security Meaning
修掉一個漏洞不代表風險歸零。組織需要決定 Treat / Accept / Avoid / Transfer，並留下責任與證據。

## Practical Lab
使用 Weather Security Center 的真實 findings 建立 Risk Register：技術 evidence → risk statement → control → owner → residual risk。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson14-security-governance
  title: Build a risk register from project security evidence
  role: security_governance_analyst
context:
  project: AI Weather Security Center
learning_objectives:
  - translate technical findings into risk language
  - understand control selection and residual risk
requirements:
  - inspect architecture threat model red-team findings and blue-team evidence
  - inventory key assets
  - create risk statements
  - assess likelihood and impact using documented rubric
  - map treatment actions and responsible owners
  - record residual risk
security_requirements:
  - distinguish evidence from assumptions
  - AI suggestions are advisory and require human review
implementation_workflow:
  - collect project evidence
  - normalize findings
  - create risk register
  - propose controls
  - identify residual risk
  - flag decisions requiring human approval
deliverables:
  - risk-register.md
  - control-mapping.md
  - residual-risk summary
final_report:
  include: [assets, top_risks, controls, residual_risks, human_decisions_required]
```

## Final Integration Package
Architecture + Asset Inventory + Threat Model + ML/DL Evidence + Red-Team Findings + Blue-Team Repairs + Regression Evidence + Risk Register。

## Reflection
如果一個漏洞修復成本高於目前風險，組織是否一定要修？誰有權做最後決策？