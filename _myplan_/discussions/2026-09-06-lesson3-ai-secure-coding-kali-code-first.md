# 2026-09-06 — Lesson 3 redesign: AI Secure Coding × Kali Linux

Status: **course planning discussion / proposed direction**

## Context

Lesson 2 builds the **AI Weather Security Center** with FastAPI, SQLite, AI-assisted/Vibe Coding, and normal application features. Lesson 3 should reuse that exact student-owned codebase as the security lab rather than directing students toward public third-party targets.

The teaching goal is to make cybersecurity part of the software-development loop:

> **Build → Inspect → Scan → Explain → Patch → Verify → Report**

The course should emphasize secure engineering, code review, and local/isolated verification. Kali Linux remains useful, but is positioned as a **Security Engineering Workstation**, not primarily as an attack machine.

## Core safety / authorization boundary

Course rule:

> **No public target. No third-party target. Code we own. Systems we control. Local/isolated verification only.**

Students analyze only:

1. source code supplied by the course or written by themselves;
2. dependencies/configuration belonging to that project;
3. a FastAPI service running on localhost or an explicitly isolated/authorized lab network.

This greatly reduces legal/ethical ambiguity compared with scanning arbitrary Internet systems. It is still important not to promise that any activity is universally legal in every jurisdiction; authorization and scope remain explicit course requirements.

## Revised Lesson 3 identity

Previous direction:

`AI Red Team × Kali Linux`

Recommended direction:

# `AI Secure Coding × Kali Linux — From Vibe Coding to Secure Vibe Coding`

The original red-team concepts can still be introduced conceptually, but the practical lab centers on defensive review and verification of the student's own FastAPI system.

## Learning outcomes

After Lesson 3, students should be able to:

- explain why code that runs successfully may still be insecure;
- distinguish SAST, SCA/dependency scanning, secret scanning, configuration review, and runtime verification;
- use AI as a Security Code Reviewer rather than blindly accepting AI-generated code;
- inspect FastAPI/SQLite code for common vulnerability patterns;
- map a scanner finding to the relevant source code and trust boundary;
- explain severity and realistic impact in their own words;
- use AI to propose a patch, then manually inspect that patch;
- re-scan/re-test and provide evidence that the finding was mitigated;
- understand explicit authorization and scope boundaries for security testing.

## Lesson architecture

### Phase A — Build baseline (inherits Lesson 2)

Student has a working FastAPI Weather Security Center:

```text
FastAPI Weather Security Center
├── main.py
├── routers/
├── models/
├── database.py
├── auth.py
├── requirements.txt
└── environment/configuration
```

The application is functional first. Security review happens against a real application the student understands.

### Phase B — AI source-code inspection

Do not start by attacking the running application.

AI reads the repository and performs structured review:

```text
Source Code
    ↓
AI Security Reviewer
    ↓
Trust-boundary review
    ↓
Potential findings
    ↓
Evidence: file + line/function + reasoning
```

AI should check areas such as:

- unsafe SQL construction / injection risk;
- missing authentication or authorization;
- hard-coded secrets/API keys;
- accidental `.env` exposure;
- plaintext password storage;
- overly permissive CORS;
- debug/error information leakage;
- insufficient input validation;
- unsafe file/path handling when applicable;
- insecure configuration/defaults;
- insecure randomness/token generation when applicable;
- SSRF risk if the weather application fetches user-controlled URLs;
- dependency and package risks.

AI findings are hypotheses until supported by code evidence or tool evidence.

### Phase C — Static security toolchain on Kali

Kali becomes the security engineering environment.

Suggested categories:

1. **SAST** — static source-code security analysis;
2. **SCA / dependency scan** — known vulnerable dependencies;
3. **Secret scan** — credentials/tokens accidentally stored in repository content/history as appropriate;
4. **Configuration review** — FastAPI, CORS, auth, environment and deployment configuration;
5. **AI synthesis** — correlate tool output and source context.

Do not teach students to accept scanner output automatically. False positives are part of the lesson.

## Finding format

Every finding should use a common schema:

```yaml
finding_id: Vxx
title: short finding name
severity: critical | high | medium | low | info
category: SAST | SCA | Secret | Config | Runtime
location: file/function/line when available
evidence: what was actually observed
why_it_matters: student-readable explanation
trust_boundary: what crosses a security boundary
recommended_fix: defensive remediation
verification: how to demonstrate the fix
status: open | patched | verified | false_positive
```

## Intentionally teachable findings

The course version of the Weather Security Center may deliberately contain a controlled set of beginner-friendly weaknesses, for example:

- V01 hard-coded API key/secret;
- V02 overly permissive CORS;
- V03 unsafe SQL string construction;
- V04 sensitive/admin route missing authorization;
- V05 insecure password storage in an auth extension;
- V06 verbose exception/debug information exposure;
- V07 weak input validation;
- V08 dependency with a known security advisory, selected carefully for the lab;
- V09 environment/secret file handling mistake;
- V10 missing or weak host/security configuration.

These are **course-owned intentional lab findings**, not instructions to seek vulnerable public websites.

## Phase D — AI Explain

Raw scanner output is converted into learning material.

For each finding, AI must explain:

1. What did the tool find?
2. Where is it in our code?
3. Why might it be dangerous?
4. Is it definitely exploitable, or only a risk/hypothesis?
5. What is the defensive fix?
6. How can we verify the fix without targeting a third party?

Students must be able to explain the issue independently; copying the AI answer is not sufficient evidence of learning.

## Phase E — Patch one vulnerability at a time

Recommended classroom rule:

> **One finding → one explanation → one patch → one verification.**

Avoid asking AI to 'fix all security problems' in one operation. Small patches make causality, review, Git diffs, and verification visible.

Workflow:

```text
Finding
  ↓
AI proposes patch
  ↓
Student reviews diff
  ↓
Run tests
  ↓
Re-run relevant security check
  ↓
Mark VERIFIED only with evidence
```

## Phase F — Local / isolated runtime verification

Only after code-only analysis is understood, run the application locally, e.g. bound to loopback (`127.0.0.1`) or inside an explicitly isolated course lab.

Purpose is **verification**, not Internet attack practice.

Examples of appropriate introductory activities:

- inspect HTTP behavior and response headers;
- inspect FastAPI/OpenAPI routes and authentication expectations;
- use ordinary requests/curl to confirm validation and authorization behavior;
- use an approved local passive web-security scanner where suitable;
- confirm that a patched route/configuration now behaves as intended.

Any later active security-testing exercise must remain limited to explicitly authorized course-owned targets and have a separately defined scope.

## Phase G — Re-scan and security report

Final student evidence should show before/after state:

```text
BEFORE
Finding V03: OPEN
Evidence: static scanner + source code

PATCH
Git diff / explanation

AFTER
Finding V03: VERIFIED
Evidence: re-scan + tests/local verification
```

Final report sections:

1. system description;
2. assets and trust boundaries;
3. tools used;
4. findings table;
5. AI explanation vs student judgment;
6. patches;
7. verification evidence;
8. false positives / limitations;
9. lessons learned.

## AI Secure Vibe Coding Loop

This becomes a recurring course concept, not only a Lesson 3 activity:

```text
BUILD
  ↓
INSPECT
  ↓
SCAN
  ↓
EXPLAIN
  ↓
PATCH
  ↓
VERIFY
  ↓
BUILD AGAIN
```

AI roles change across the loop:

- BUILD → AI coding assistant;
- INSPECT → AI security reviewer;
- SCAN → tool orchestrator / output interpreter;
- EXPLAIN → security tutor;
- PATCH → defensive coding assistant;
- VERIFY → evidence reviewer.

## Relationship to DevSecOps

This lesson introduces the principle that security is not a final penetration-test gate. Security checks are brought into the development lifecycle:

```text
Vibe Coding
    +
Security Review
    +
Automated Scanning
    +
Human Verification
    =
Secure Vibe Coding / introductory DevSecOps mindset
```

## Suggested lesson parts / slide modules

1. Why working code is not necessarily secure
2. From Vibe Coding to Secure Vibe Coding
3. Authorization, ownership, and the course safety boundary
4. FastAPI trust boundaries and attack surface — concept only
5. AI as Security Code Reviewer
6. SAST: security analysis without running the website
7. SCA: dependencies are part of your application
8. Secrets and configuration review
9. Reading a security finding: evidence vs AI guess
10. Kali Linux as a Security Engineering Workstation
11. Hands-on scan of the Weather Security Center
12. AI-assisted vulnerability explanation
13. One-finding/one-patch workflow
14. Local isolated verification
15. Re-scan and before/after evidence
16. Student security report / reflection
17. Secure Vibe Coding Loop and DevSecOps bridge

## Teaching contract integration

Each detailed part should follow the repository teaching contract:

1. Concept / Why
2. Security meaning and trust boundary
3. Practical example or authorized lab
4. Antigravity YAML prompt
5. Test / evidence
6. Reflection / explanation by the student

## Important implementation note

This document is a planning discussion. Per `_myplan_/README.md`, do not silently replace canonical `Lesson3/` teaching content until the direction is accepted and the relevant canonical files have been inspected. Next step is to reconcile this design with existing Lesson 3 material, record the accepted decision, and then promote the revised structure into `Lesson3/` with slides, instructor notes, lab instructions, YAML prompts, and assessment evidence.
