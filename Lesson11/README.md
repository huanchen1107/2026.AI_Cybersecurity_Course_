# Lesson 11 — AI Red Team I：Learn the Attack in TryHackMe

## Mission
在明確授權的 TryHackMe / 教師指定 Cyber Range 中建立 Red-Team 思考，不對一般公開網站練習攻擊。

## Concept
Scope、Rules of Engagement、Recon、Enumeration、Service、Port、Attack Surface、Vulnerability Hypothesis、Evidence。

## Security Meaning
Publicly accessible does not mean publicly authorized to attack. Ownership 也不等於可以忽略第三方平台規則。

## Practical Lab
Kali + instructor-approved TryHackMe room：Recon → service enumeration → evidence。AI 用來解釋結果、區分 Observation / Hypothesis / Evidence / Next Test。

## Antigravity YAML Prompt
```yaml
task:
  id: lesson11-authorized-redteam-analysis
  title: Build an AI-assisted authorized red-team evidence workflow
  role: cybersecurity_lab_assistant
context:
  environment: explicitly_authorized_training_lab_only
  target_scope: instructor_provided
learning_objectives:
  - distinguish recon evidence from vulnerability claims
  - document authorization scope
requirements:
  - accept instructor-provided scan output or lab evidence
  - parse services and observations
  - separate observation hypothesis evidence and next safe test
  - generate a report template
security_requirements:
  - never expand scope beyond instructor-provided targets
  - no autonomous exploitation
  - no credential attacks outside the lab
  - no destructive or denial-of-service actions
implementation_workflow:
  - validate scope statement
  - analyze supplied evidence
  - explain findings
  - propose only scope-safe next steps
  - generate evidence report
deliverables:
  - evidence parser or helper script
  - red-team notes template
  - scope record
final_report:
  include: [scope, observations, hypotheses, evidence, safe_next_steps]
```

## Evidence
Scope statement、authorized target、scan/evidence notes、AI analysis、student explanation。

## Reflection
看到 open port 為什麼不能直接寫成 vulnerability？