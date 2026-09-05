# Lesson 5 — GOVERN：AI Security Governance × ISO 27001 × Risk Management

## Goal
把 BUILD、LEARN、ATTACK、DEFEND 的技術證據提升到組織治理層次。學生不只回答「漏洞怎麼修」，還要回答風險如何處理、誰負責、是否接受 residual risk，以及技術修補如何轉成 control evidence。

## Main Topics

1. Vulnerability → Risk
2. Asset / Threat / Vulnerability / Impact / Likelihood
3. Risk = Likelihood × Impact concept
4. ISO/IEC 27001:2022 basic structure
5. Organizational / People / Physical / Technological controls
6. Control selection and applicability
7. Risk Treatment Plan
8. Statement of Applicability concept
9. Logging / Monitoring / Incident Response
10. Secure deployment and environment separation
11. AI / ML system risks: data, model, API, dependency, automation over-trust
12. Supply-chain risk
13. Residual risk
14. AI-assisted risk assessment with human accountability
15. Final integration: Build → Learn → Attack → Defend → Govern

## Weather Project Governance View

Assets can include:
- source code
- FastAPI service
- user accounts
- authentication/session state
- SQLite / production database
- weather data
- security event logs
- ML model / training data
- deployment configuration
- API keys / secrets
- dependencies

Risk examples:
- credential leakage
- broken access control
- injection
- XSS / unsafe output
- session weakness
- dependency compromise
- corrupted or malicious data
- model false negatives
- insufficient logging
- insecure production deployment
- accidental exposure of lab-only vulnerable code

## Risk Workflow

```text
Asset
  ↓
Threat
  ↓
Vulnerability
  ↓
Evidence from Red / Blue Team
  ↓
Likelihood + Impact
  ↓
Risk Rating
  ↓
Select Control
  ↓
Treat / Accept / Avoid / Transfer
  ↓
Residual Risk
  ↓
Monitor
```

## Final Course Package

每組最終需整合：
- Architecture diagram
- Asset inventory
- Threat model
- Dataset and AI/ML method
- Supervised ML evaluation
- optional / advanced DL result
- authorized red-team findings
- blue-team remediation evidence
- security regression tests
- risk register
- selected ISO 27001 controls
- residual risk
- AI usage statement

## Antigravity YAML Prompt — Risk Integration

```yaml
task:
  id: governance-risk-001
  title: Build the final security risk package from project evidence
  role: security_governance_and_risk_engineer

context:
  project: AI Weather Security Center
  framework: ISO_IEC_27001_2022_concepts
  evidence_sources:
    - architecture
    - threat_model
    - ml_evaluation
    - red_team_findings
    - blue_team_repairs
    - test_results

learning_objectives:
  - distinguish vulnerability from risk
  - connect technical evidence to controls
  - explain likelihood and impact
  - identify residual risk
  - keep final accountability with humans

requirements:
  - build an asset inventory
  - map threats and vulnerabilities to assets
  - reference actual project evidence
  - assign likelihood and impact with rationale
  - recommend treatment options
  - identify candidate controls
  - record residual risk after treatment

constraints:
  - do not invent evidence
  - mark assumptions explicitly
  - do not treat AI output as final risk acceptance authority
  - preserve traceability to source findings and tests

final_report:
  include:
    - asset_inventory
    - risk_register
    - control_mapping
    - treatment_plan
    - residual_risk
    - evidence_references
    - assumptions
    - human_decisions_required
```

## Course Closing

```text
BUILD
  ↓
LEARN
  ↓
ATTACK
  ↓
DEFEND
  ↓
GOVERN
```

> 真正的 AI 資安工程，是把需求、程式、資料、模型、攻防證據、修補測試與治理責任串成一條可驗證的工程鏈。