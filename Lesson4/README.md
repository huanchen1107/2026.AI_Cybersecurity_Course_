# AIIS_L4 — SECURE：Scan → Propose → Fix → Re-scan → Verify

> **Status: CANONICAL ALLOCATION — 2026-09-07**
>
> Earlier versions assigned the semester's full Blue Team / OWASP repair lesson to L4. That allocation is superseded. **AIIS_L4** now introduces the source-code Secure SDLC scanning/remediation loop. The later **AIIS_L13** remains the formal Blue Team lesson using verified Red Team findings and deeper OWASP secure repair.

## Mission

核心問題：

> 我們已經做出程式、管理程式、看懂程式。現在怎麼用 AI + security tools 系統化地檢查自己的 code，修補後再證明問題真的消失？

All work remains on student-owned / teacher-provided source code or authorized local environments.

## Canonical Workflow

```text
SCAN
 ↓
FIND
 ↓
PROPOSE
 ↓
REVIEW
 ↓
FIX
 ↓
TEST
 ↓
RE-SCAN
 ↓
VERIFY
 ↓
REPORT
```

## Primary Tool

Use **Semgrep** as the representative source-code scanner for the required implementation. Other SAST/code-review tools may be mentioned only as `Further Exploration` unless the Master Curriculum is explicitly revised.

## Primary Topics

1. Why working code can still contain security weaknesses
2. Static analysis / SAST concept
3. Semgrep basic workflow
4. Scan only owned / provided code
5. Finding vs confirmed vulnerability
6. Rule / location / evidence
7. AI-assisted explanation of findings
8. True positive / false positive / needs verification
9. Vulnerability vs risk
10. remediation proposal
11. human review before code modification
12. minimal secure fix
13. tests before/after change
14. re-scan
15. verification and evidence
16. report residual risk

## Required Lab

Run the workflow on the existing Weather Security Center:

```text
Weather Security Center source
→ Semgrep scan
→ select one understandable finding
→ inspect code/evidence
→ ask AI to explain and propose minimal remediation
→ human review
→ apply approved fix
→ run relevant tests
→ re-scan
→ compare before/after evidence
```

## Epistemic Rules

```text
AI FINDING ≠ CONFIRMED FINDING
SCANNER FINDING ≠ CONFIRMED VULNERABILITY
BUG ≠ VULNERABILITY ≠ RISK
```

Finding status vocabulary:
- CONFIRMED
- LIKELY TRUE POSITIVE
- LIKELY FALSE POSITIVE
- NEEDS VERIFICATION

Remediation vocabulary:
- FIX NOW
- VERIFY FIRST
- ACCEPT RISK
- FALSE POSITIVE / NO CHANGE

## Evidence

Students record:
- scan command/config
- original finding
- affected file/location
- scanner evidence
- AI explanation
- human classification
- proposed remediation
- approved change
- tests run/results
- re-scan result
- before/after comparison
- residual risk

## Relationship to L13

L4 is the **first Secure SDLC code-scanning loop**.

L13 later returns after authorized Red Team work and performs deeper Blue Team remediation:

```text
Verified Red-Team Finding
→ Root Cause
→ OWASP Secure Coding
→ Minimal Repair
→ Security Regression Test
→ Evidence
→ Close Finding
```

Therefore L4 must not consume L13's full Red/Blue Team storyline.

## Core Statement

> **SCAN DOES NOT PROVE. EVIDENCE + HUMAN REVIEW + RE-TEST PROVE.**

> **AI proposes. Human reviews. Tools verify.**