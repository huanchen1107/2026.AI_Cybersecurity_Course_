# Lesson 3 — AI Red Team：TryHackMe × Kali × Weather Cyber Range

## Goal
先在 TryHackMe / CTF 等明確授權的訓練環境學習標準化攻擊技術，再把相同的思考方法移轉到本課自己的 Local Weather Cyber Range。重點是理解、驗證、蒐證，不是盲目複製指令。

核心主線：

```text
Learn it in the Range
        ↓
Understand the Technique
        ↓
Transfer the Method
        ↓
Prove it in Our Lab
        ↓
Collect Evidence
        ↓
Handoff to Blue Team
```

## Main Topics

1. Red Team / Blue Team / Purple Team
2. Scope / Authorization / Rules of Engagement
3. Kali Linux 與隔離 Lab
4. TryHackMe / CTF as authorized training range
5. Attack Surface 與 Recon
6. Nmap：service / version enumeration
7. Directory / endpoint discovery in lab
8. Authentication and access-control testing concepts
9. Injection / XSS / session weakness concepts
10. CVE research and vulnerability hypothesis
11. Evidence collection
12. Risk / severity interpretation
13. AI-assisted result explanation and prioritization
14. AI-assisted small security scripts under instructor-defined scope

## Two-Stage Lab Model

### Stage 1 — TryHackMe: Learn the Attack

```text
Mission
  ↓
Scope
  ↓
Recon
  ↓
Enumeration
  ↓
Observation
  ↓
Hypothesis
  ↓
Controlled Validation
  ↓
Evidence
```

學生要把「Observation」與「Hypothesis」分開；看到 open port 並不等於已存在 vulnerability。

### Stage 2 — Weather Cyber Range: Transfer the Knowledge

回到自己第 3 週建立的 FastAPI Weather App，但只使用 Local Docker / VM Lab build。

Teacher-controlled lab themes can include:
- lab01_authentication
- lab02_broken_access_control
- lab03_injection
- lab04_xss_output_handling
- lab05_session_security
- lab06_logging_detection

Production/Vercel build 不包含這些 vulnerable labs。

## AI-Assisted Red Team Loop

```text
OBSERVE
  ↓
ASK AI TO EXPLAIN
  ↓
FORM HYPOTHESIS
  ↓
DESIGN A SAFE TEST
  ↓
HUMAN REVIEW
  ↓
AUTHORIZED EXECUTION
  ↓
COLLECT EVIDENCE
  ↓
AI-ASSISTED ANALYSIS
  ↓
REPORT
```

核心句：

> AI proposes. Human understands. Lab authorizes. Evidence proves.

## Deliverable

每組紅隊報告包含：
- Scope
- Asset
- Observation
- Hypothesis
- Finding
- Evidence
- Impact
- Severity
- Reproduction in authorized lab
- Recommended fix
- AI assistance used

## Antigravity YAML Prompt — Analyze Red-Team Evidence

```yaml
task:
  id: redteam-analysis-001
  title: Analyze authorized cyber-range evidence
  role: cybersecurity_instructor_and_red_team_analyst

context:
  environment: instructor_authorized_lab
  target_type: TryHackMe_or_local_weather_cyber_range
  rule: do_not_assume_a_vulnerability_without_evidence

learning_objectives:
  - distinguish observation from hypothesis
  - understand service enumeration
  - create evidence-based findings
  - connect offensive observation to defensive remediation

inputs:
  allowed:
    - nmap_results
    - HTTP_requests_and_responses
    - application_logs
    - screenshots
    - instructor_provided_lab_notes

analysis_requirements:
  - list observations first
  - create hypotheses separately
  - state what evidence supports each hypothesis
  - state what evidence is still missing
  - recommend only tests that stay inside the authorized lab scope
  - identify likely defensive controls

constraints:
  - no actions against public or unauthorized targets
  - no destructive testing
  - no denial_of_service
  - no credential attacks outside instructor-provided lab accounts
  - do not automatically execute exploitation

final_report:
  include:
    - observations
    - hypotheses
    - evidence
    - findings
    - severity_rationale
    - recommended_defenses
    - unanswered_questions
```

## Safety Boundary

所有 offensive exercise 僅限：
- localhost
- self-owned VM / Docker
- teacher-designated target
- TryHackMe / CTF / deliberately vulnerable app
- other explicitly authorized environment

Publicly accessible does not mean publicly authorized to attack.