# AIIS 16-Lesson Focused Course Plan

**Date:** 2026-09-07  
**Course:** AIIS — AI and Information Security / 人工智慧與資訊安全  
**Status:** Canonical teaching refinement plan  
**Principle:** Keep the existing 16-lesson backbone. Do not continuously expand required scope.

---

## 1. Course Design Decision

The existing AIIS_L1–AIIS_L16 sequence remains the canonical course backbone:

**BUILD → LEARN → ATTACK → DEFEND → GOVERN → FINAL**

The course focuses on **AI for Security**. New security technologies such as a complete AI-assisted Secure SDLC are treated as an **advanced roadmap**, not as additional required lessons.

### Core constraint: One Core Tool per Lesson

Each lesson should normally contain:

1. One core concept
2. One representative technology
3. One primary hands-on tool
4. One achievable lab
5. One evidence artifact
6. Optional “Further Exploration” tools, introduction only

Students should understand *why* a technology is used and complete one representative implementation rather than install many similar tools.

> Learn one representative tool deeply enough to understand the technology. Mention alternatives, but do not require all of them.

---

## 2. Shared Project Backbone

All lessons should reuse and progressively improve the same project whenever practical:

```text
AI Weather Security Center
        ↓
Python + FastAPI
        ↓
SQLite / SQLAlchemy
        ↓
Weather / Security Data
        ↓
ML Security Analysis
        ↓
DL Security Analysis
        ↓
Authorized Security Validation
        ↓
Secure Coding / Repair
        ↓
Risk Management
        ↓
Final Demonstration
```

Avoid creating a new unrelated application every week.

---

# 3. Detailed 16-Lesson Plan

## AIIS_L1 — Course Foundations / AI Security Engineer Mindset

**Phase:** INTRO

### Core concept
Understand the relationship between AI and Information Security and establish the AI Security Engineer mindset.

### Required knowledge
- Asset, Threat, Vulnerability, Risk
- CIA Triad
- Defensive vs offensive security
- Authorization and ethical boundary
- AI as an engineering assistant, not an unquestioned authority

### Primary activity
Use an AI assistant to analyze a simple cybersecurity scenario and identify Asset → Threat → Vulnerability → Risk.

### Core tool
**ChatGPT / Gemini — choose one classroom primary AI assistant**

### Evidence
One structured AI-assisted risk analysis reviewed by the student.

### Further Exploration — introduction only
Claude, Copilot and other LLM assistants.

---

## AIIS_L2 — AI Security Engineer Toolbox

**Phase:** BUILD

### Core concept
Prompt → Plan → Code → Run → Test → Review → Fix.

### Required knowledge
- Prompt engineering for coding
- Vibe Coding
- AI coding agents
- Git/GitHub basics
- Version-controlled evidence

### Core tool
**Antigravity + GitHub** as the standard classroom workflow.

### Lab
Ask the AI coding agent to make one controlled change, run it, test it and commit the evidence to GitHub.

### Evidence
Prompt + changed code + test result + Git commit.

### Further Exploration
Codex CLI, Claude Code, Cursor, Windsurf, other coding agents.

---

## AIIS_L3 — Python FastAPI Weather Security Center

**Phase:** BUILD

### Core concept
Build a real web/API system that will become the common cyber range for later lessons.

### Required knowledge
- Python/FastAPI
- HTTP request/response
- REST API
- CWA Open Data / fake sensor data
- SQLite/SQLAlchemy basics
- Input and output validation

### Core tool
**FastAPI**

### Lab
Build or extend one Weather Security Center API endpoint and verify it locally.

### Evidence
Working endpoint + API response + automated/basic test.

### Further Exploration
Flask, Django, Node.js/Express.

---

## AIIS_L4 — How to Build an AI Cybersecurity Project

**Phase:** BUILD

### Core concept
Security must be considered while software is being built, not only after deployment.

### Required knowledge
- Secure coding mindset
- Secrets and configuration
- Input validation
- Authentication/authorization awareness
- Dependency risk
- Static Application Security Testing (SAST)

### Representative security implementation
**Semgrep** for source-code security scanning.

### Lab
Intentionally use a teacher-provided insecure code sample in the local project, run Semgrep, understand one finding, fix it, and scan again.

### Evidence
Before finding → explanation → fix → after scan.

### Further Exploration
Bandit, GitHub CodeQL, SonarQube, Snyk, Trivy.

### Advanced roadmap only
Explain that professional Secure SDLC can additionally include dependency scanning, container scanning, DAST, SIEM and automated remediation. Do not require all tools here.

---

## AIIS_L5 — Supervised ML I: Classification Foundations

**Phase:** LEARN

### Core concept
Teach a machine to classify security-related observations.

### Required knowledge
- Features and labels
- Train/test split
- Classification
- Basic preprocessing
- Security dataset interpretation

### Core tool
**scikit-learn**

### Lab
Train one simple classifier on a security-related dataset.

### Evidence
Dataset → features → model → prediction.

### Further Exploration
XGBoost, LightGBM, CatBoost.

---

## AIIS_L6 — Supervised ML II: Tree Models

**Phase:** LEARN

### Core concept
Understand how decision trees and ensemble models make security classification decisions.

### Required knowledge
- Decision Tree
- Random Forest
- Feature importance
- Overfitting

### Core tool
**scikit-learn RandomForestClassifier**

### Lab
Train and inspect a tree-based model using the same or related security dataset.

### Evidence
Model + feature importance + short interpretation.

### Further Exploration
Gradient Boosting, XGBoost, LightGBM.

---

## AIIS_L7 — Supervised ML III: Security Evaluation

**Phase:** LEARN

### Core concept
Accuracy alone is not enough for cybersecurity.

### Required knowledge
- Confusion Matrix
- Precision
- Recall
- F1 score
- False Positive / False Negative
- Security cost of errors

### Core tool
**scikit-learn metrics**

### Lab
Evaluate the existing security classifier and explain which error is more dangerous for the scenario.

### Evidence
Confusion matrix + metrics + security interpretation.

### Further Exploration
ROC-AUC, PR curve, threshold tuning, calibration.

---

## AIIS_L8 — Midterm AI Security Engineering Review

**Phase:** REVIEW

### Core concept
Integrate BUILD and ML instead of adding new technology.

### Required review
- AI-assisted engineering workflow
- FastAPI Weather Security Center
- GitHub evidence
- Secure coding/SAST concept
- ML classification and evaluation

### Core tool
**Existing course toolchain only — no new major tool.**

### Lab
Mini integration challenge: modify the Weather Security Center, run tests/security check, and demonstrate an ML security result.

### Evidence
Midterm engineering evidence package.

### Further Exploration
None required. Use this week to consolidate.

---

## AIIS_L9 — Deep Learning I: Neural Networks for Security

**Phase:** LEARN

### Core concept
Move from classical ML to neural-network representation learning.

### Required knowledge
- Neuron
- Layer
- Activation
- Loss
- Training loop
- Epoch
- Overfitting

### Core tool
**PyTorch**

### Lab
Build and train one small neural network for a security classification task.

### Evidence
Model definition + loss/training result + prediction.

### Further Exploration
TensorFlow, Keras, JAX.

---

## AIIS_L10 — Deep Learning II: Security Sequence Analysis

**Phase:** LEARN

### Core concept
Security events often form sequences; order and context matter.

### Required knowledge
- Event sequence
- Time-series/security-log representation
- Windowing
- Sequence classification concept

### Core tool
**PyTorch** using one simple sequence model selected for teaching clarity.

### Lab
Use a small security-event/log sequence dataset to distinguish normal vs suspicious sequences.

### Evidence
Sequence input → model → classification result → interpretation.

### Further Exploration
LSTM, GRU, Transformer, Autoencoder. Mention alternatives without requiring multiple implementations.

---

## AIIS_L11 — AI Red Team I: Learn the Attack in TryHackMe

**Phase:** ATTACK

### Core concept
Understand offensive techniques only inside explicitly authorized environments.

### Required knowledge
- Reconnaissance
- Scanning
- Service discovery
- Vulnerability hypothesis
- Evidence
- Authorization boundary

### Core platform
**TryHackMe**

### Representative tool
**Nmap**

### Lab workflow
```text
Recon → Scan → Discover → Analyze → Report
```

Use a teacher-selected authorized TryHackMe room.

### Evidence
Nmap result + service interpretation + learning report.

### Further Exploration
RustScan, Masscan, Nikto, Burp Suite, other Kali tools.

---

## AIIS_L12 — AI Red Team II: Weather Cyber Range

**Phase:** ATTACK

### Core concept
Transfer a security-testing concept from a training range to our own isolated application.

### Safety boundary
Only localhost, owned VM/Docker, teacher-provided target, or explicitly authorized cyber range.

### Core tool
**OWASP ZAP**

### Lab
Run a controlled web security assessment against the local Weather Security Center and investigate one representative finding.

### Workflow
```text
Observe
→ Hypothesis
→ Authorized Test
→ Evidence
→ Root Cause
→ Report
```

### Evidence
ZAP finding + HTTP/security explanation + root-cause hypothesis.

### Further Exploration
Burp Suite, Nikto, Nuclei. Kali Linux remains the general security toolbox but students do not need to master every bundled tool.

---

## AIIS_L13 — AI Blue Team: Fix Our Code

**Phase:** DEFEND

### Core concept
Finding a vulnerability is not the finish line; engineering must repair and verify it.

### Required knowledge
- OWASP secure coding
- Root cause
- Remediation
- Regression testing
- Security verification
- Logging awareness

### Core reference/tool
**OWASP secure coding guidance + AI coding assistant**

### Lab
Take one confirmed finding from the Weather Cyber Range:

```text
Finding
→ AI-assisted analysis
→ Human review
→ Fix
→ Test
→ Re-scan
→ Evidence
```

### Evidence
Before → Root Cause → Fix → Test → After.

### Further Exploration
Bandit, Semgrep, ZAP automation, Wazuh, Elastic, Splunk/SIEM.

### Advanced roadmap only
Show the professional lifecycle:

```text
AI Code Review
→ SAST
→ Dependency / Container Scan
→ DAST
→ Logging / SIEM
→ AI Analysis
→ Remediation
→ Re-scan
```

Only representative components are implemented during this course.

---

## AIIS_L14 — ISO 27001 × Risk Management

**Phase:** GOVERN

### Core concept
Technical vulnerabilities become organizational risk decisions.

### Required knowledge
- Asset
- Threat
- Vulnerability
- Impact
- Likelihood
- Risk
- Control
- Treatment
- Evidence

### Core framework
**ISO/IEC 27001 risk-management perspective**

### Lab
Take one Weather Security Center finding and convert it into a small risk record with treatment decision and evidence.

### Evidence
Technical finding → risk → control → treatment → residual-risk explanation.

### Further Exploration
NIST CSF, CIS Controls, ISO 27005.

---

## AIIS_L15 — Final Project Demo I

**Phase:** FINAL

### Core concept
Demonstrate an integrated engineering system rather than isolated homework.

### Required project components
- AI-assisted development evidence
- Weather Security Center
- ML or DL security-analysis component
- One representative security validation
- One remediation
- GitHub evidence

### Core tool
**Existing project stack only — no new tool.**

### Activity
Team demonstrations, technical review and evidence inspection.

### Evidence
Final repository + demo + technical report.

---

## AIIS_L16 — Final Project Demo II & Course Closure

**Phase:** FINAL

### Core concept
Explain not only what was built but how security was validated.

### Required final story
```text
BUILD
→ LEARN
→ ATTACK
→ DEFEND
→ GOVERN
```

Students should be able to explain:
1. What did we build?
2. Where was AI used?
3. What did ML/DL contribute?
4. What security problem did we find?
5. What evidence proved it?
6. How did we fix it?
7. How did we verify the fix?
8. What risk remains?

### Core tool
No new tool.

### Evidence
Final presentation + final evidence package + reflection.

### Further Exploration
Show the advanced AI-assisted Secure SDLC roadmap and possible follow-on cybersecurity technologies without adding required work.

---

# 4. Tool Selection Policy

## Required representative tools

The course should aim to make students genuinely use a small set:

- AI assistant: one classroom default
- Antigravity
- GitHub
- Python
- FastAPI
- SQLite / SQLAlchemy
- scikit-learn
- PyTorch
- Semgrep
- TryHackMe
- Nmap
- OWASP ZAP
- OWASP secure-coding references
- ISO 27001 risk perspective

These are not all required in every lesson. Each lesson chooses only the representative tool needed for its objective.

## Mention-only alternatives

Alternatives can appear in one slide or a short “Further Exploration” section:

- AI coding: Codex CLI, Claude Code, Cursor, Windsurf
- SAST: Bandit, CodeQL, SonarQube, Snyk
- Dependency/container: Trivy
- DAST: Burp Suite, Nikto, Nuclei
- Recon: RustScan, Masscan
- SIEM: Wazuh, Elastic, Splunk
- ML: XGBoost, LightGBM, CatBoost
- DL: TensorFlow, Keras, JAX
- Governance: NIST CSF, CIS Controls, ISO 27005

**Mentioning a tool does not create a required lab.**

---

# 5. Advanced Roadmap — Not Required Core Curriculum

The following is retained as an advanced AI-for-Security roadmap:

```text
AI / Vibe Coding
        ↓
GitHub
        ↓
AI Code Review
        ↓
SAST
        ↓
Dependency / Container Scan
        ↓
DAST / Authorized Validation
        ↓
Security Logging / SIEM
        ↓
AI Security Analysis
        ↓
AI-assisted Remediation
        ↓
Vibe Coding Fix
        ↓
Re-scan / Regression Verification
```

The 16-lesson course demonstrates representative portions of this lifecycle. It does **not** require students to implement every technology.

Possible advanced tools: Bandit, CodeQL, Trivy, Wazuh, Elastic, Splunk, automated CI/CD security gates, SBOM, container security and more advanced security orchestration.

---

# 6. Scope Guardrails

Future curriculum changes should follow these rules:

1. **Do not add a new required lesson merely because a useful tool is discovered.**
2. Prefer replacing an inferior representative tool rather than accumulating tools.
3. New tools default to `Further Exploration`.
4. A new required tool must directly improve a learning objective that cannot be achieved adequately with the current representative tool.
5. Reuse the Weather Security Center whenever possible.
6. L8, L15 and L16 should consolidate; they should not become technology-loading weeks.
7. Preserve ML and DL as core AI learning. Secure SDLC does not replace them.
8. Offensive labs remain restricted to explicitly authorized environments.
9. AI assists; students must explain evidence and reasoning themselves.
10. Prefer **completion and understanding over breadth**.

---

# 7. Stable Course Architecture

```text
AIIS_L0  ORIENTATION
          │
          ▼
L1–L4    BUILD
AI mindset → AI tools → FastAPI → Secure development
          │
          ▼
L5–L7    LEARN ML
Classification → Trees → Security Evaluation
          │
          ▼
L8       REVIEW
Integration / Midterm
          │
          ▼
L9–L10   LEARN DL
Neural Networks → Security Sequences
          │
          ▼
L11–L12  ATTACK
TryHackMe/Nmap → Weather Cyber Range/ZAP
          │
          ▼
L13      DEFEND
Root Cause → AI-assisted Fix → Re-scan
          │
          ▼
L14      GOVERN
ISO 27001 → Risk Treatment
          │
          ▼
L15–L16  FINAL
Integrated demonstration and evidence
```

## Final teaching philosophy

> **AI is the capability. Information Security is the discipline.**

> **One core concept. One representative tool. One achievable lab.**

> **Other tools are awareness, not homework.**

> **AI proposes. Human understands. Security validates.**

This document should be used as the scope-control reference when refining individual AIIS lessons.