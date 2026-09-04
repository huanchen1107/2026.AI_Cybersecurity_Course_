# Lesson 5 — AI Security Governance：ISO 27001 與風險管理

## Goal
把前四課的技術經驗提升到組織治理層次。學生不只回答「漏洞怎麼修」，還要回答「風險要不要接受、降低、移轉或避免，以及誰負責」。

## Main Topics
1. 從 Vulnerability 到 Risk
2. Asset / Threat / Vulnerability / Impact / Likelihood
3. Risk = Likelihood × Impact 的概念模型
4. ISO/IEC 27001:2022 基本架構
5. 組織控制
6. 人員控制
7. 實體控制
8. 技術控制
9. Control selection 與適用性
10. Risk Treatment Plan
11. Statement of Applicability 概念
12. Logging / Monitoring / Incident Response
13. AI 系統的額外風險：Prompt、Model、Data、API、Supply Chain、Cost Abuse
14. AI-assisted risk assessment：AI 可協助整理，但最終風險決策由人與治理流程負責
15. Final presentation：從 Build 到 Govern

## Weather Project Governance View

資產：
- Weather database
- User account
- Session
- Source code
- API key
- AI provider integration
- ML model / training data
- Server / deployment environment

風險案例：
- Credential leakage
- Broken access control
- SQL injection
- XSS / CSRF
- Dependency compromise
- API key exposure
- Prompt injection
- AI hallucination
- Malicious or corrupted sensor data
- Lack of logging
- Availability / cost abuse

## Risk Workflow

```text
Asset
  ↓
Threat
  ↓
Vulnerability
  ↓
Likelihood + Impact
  ↓
Risk Rating
  ↓
Select Control
  ↓
Treat / Accept / Avoid / Transfer
  ↓
Monitor
```

## Final Deliverable
每組以 AI Weather Security Center 為案例，提交：
- Architecture diagram
- Asset inventory
- Threat model
- Lesson 3 red-team findings
- Lesson 4 remediation evidence
- Risk register
- Selected ISO 27001 controls
- Residual risk
- AI usage statement：AI 做了什麼、人做了什麼、哪些內容經人工驗證

## Course Closing

```text
BUILD
  ↓
ATTACK
  ↓
DEFEND
  ↓
GOVERN
```

> 真正的 AI 資安工程，不是只會用 AI 寫程式，也不是只會跑掃描工具，而是能把需求、程式、資料、模型、攻防證據與治理責任串成一個可驗證的安全流程。
