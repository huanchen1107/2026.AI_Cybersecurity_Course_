# AIIS_L4 — Slide 28–29 Closing + Course Completion Check

**Lesson:** AIIS_L4 — How to Build an AI Cybersecurity Project / Secure Development  
**Batch:** 5 — S28–S29 + completion review  
**Canonical loop:** Code → Scan → Understand → Fix → Re-scan → Evidence  
**Primary hands-on tool:** Semgrep

---

# S28 — Where Today's Work Fits in a Professional Secure SDLC

## On-slide text

# TODAY WE LEARNED ONE LOOP
## Real Secure SDLC expands the same idea.

```text
PLAN
  ↓
CODE
  ↓
SAST          ← TODAY: Semgrep
  ↓
DEPENDENCY / SUPPLY-CHAIN CHECK
  ↓
TEST
  ↓
DAST / AUTHORIZED VALIDATION
  ↓
REVIEW + REMEDIATION
  ↓
DEPLOY
  ↓
MONITOR + IMPROVE
```

### Today: learn one representative tool deeply
**Semgrep → Finding → AI/Human Analysis → Fix → Test → Re-scan → Evidence**

### Further Exploration — NOT required in L4
- Bandit — Python-focused static checks
- GitHub CodeQL — semantic/code-query analysis
- SonarQube — code quality/security analysis platform
- Snyk — dependency/code security ecosystem
- Trivy — dependency/container/IaC scanning
- OWASP ZAP — later authorized dynamic testing

> **Do not collect tools. Learn the engineering loop.**

## Visual composition

A wide Secure SDLC pipeline. Only the SAST station is enlarged and illuminated, with Semgrep attached. Other stations remain smaller, labeled `Later / Further Exploration`.

At the bottom, repeat the L4 evidence chain as a compact ribbon.

## Character expression / pose

Spokesperson stands beside the complete map but places one flag only on the SAST station, communicating deliberate scope control.

## Teacher script

我們今天只學 Semgrep，不代表 professional Secure SDLC 只有 Semgrep。

真實環境還會有 dependency scanning、container scanning、dynamic testing、monitoring 等等。但是如果一堂課每看到一個名詞就裝一個工具，學生最後只會記得很多 logo。

所以 AIIS 的方法是：先用一個代表工具，把完整 engineering loop 做完。

你真正需要帶走的是：問題越早發現越好；scanner finding 要理解；AI 可以協助，但人要判斷；修完要 test；test 完要 re-scan；最後要留下 evidence。

後面的 AIIS_L11、L12、L13 會把這個思考擴展到 authorized security validation 和 remediation。今天是 Secure Development 的起點。

## Transition

「最後，我們回頭看一開始的問題：AI 寫得出可以跑的程式，安全嗎？」

---

# S29 — Mission Complete: From Vibe Coder to Security-Aware Engineer

## On-slide text

# AIIS_L4 — MISSION COMPLETE

At S01 we asked:

## “It works. Is it safe?”

Now our workflow is:

```text
PROMPT
  ↓
CODE
  ↓
RUN + TEST
  ↓
SECURITY SCAN
  ↓
UNDERSTAND
  ↓
HUMAN-REVIEWED FIX
  ↓
RE-TEST + RE-SCAN
  ↓
EVIDENCE
```

### What changed today?

Before:
`AI → Code → Run → Done`

After:
`AI → Code → Verify → Secure → Evidence`

### Your L4 Security Package

- BEFORE scan
- Finding interpretation
- AI analysis
- Human root-cause decision
- Code diff
- Functional test
- AFTER scan
- Remaining-risk statement
- GitHub record

## NEXT — AIIS_L5
### Can a machine learn patterns from security data?

**Supervised Machine Learning I — Classification**

## Visual composition

Return to the exact Weather Security Center visual language from S00. The unfinished shield from S00 is now completed, but not labeled “100% secure.” Instead attach an `Evidence Verified` folder/checklist.

Behind the application, the course journey extends toward a data table with labeled examples, visually foreshadowing machine learning.

Bottom-right teaser: `DATA → FEATURES → LABELS → MODEL`.

## Character expression / pose

Spokesperson from S00 now holds the completed evidence package. Expression is confident but professional, not triumphant. The other hand points forward toward a dataset/model icon for L5.

## Teacher script

現在回到第一頁。當時我們問：「程式可以跑，代表安全嗎？」

今天的答案不是單純的 No，而是一套新的工作方法。

以前 Vibe Coding 很容易停在 AI → Code → Run → Done。從今天開始，我希望大家多出幾個動作：Test、Security Scan、Understand、Human Review、Fix、Re-scan、Evidence。

注意我們沒有說 Weather Security Center 現在百分之百安全。專業工程師不做這種沒有證據的保證。我們能說的是：我們找到一個具體 risky pattern，理解 root cause，完成 remediation，功能測試通過，而且在目前的 Semgrep configuration 下完成 re-scan verification。

這已經是非常完整的一次 Secure Development exercise。

下一課開始，課程從 BUILD 階段進入 LEARN 階段。我們會開始問另一個問題：如果安全資料越來越多，人不可能一筆一筆看，機器能不能從已標記資料中學出 pattern？這就是 AIIS_L5 的 Supervised Machine Learning。

## Final class sentence

**AI can help us code faster. Security engineering teaches us how to trust the result less blindly—and verify it with evidence.**

---

# AIIS_L4 — COMPLETE COURSE CONSISTENCY REVIEW

## 1. Lesson position

```text
AIIS_L0  Orientation / Storyline
AIIS_L1  AI Security Engineer Mindset
AIIS_L2  AI Engineering Toolbox
AIIS_L3  Build Weather Security Center
AIIS_L4  Secure What We Built   ← COMPLETE
AIIS_L5  Supervised ML I
```

L4 does not create a new unrelated application. It continues the shared Weather Security Center.

## 2. Complete 30-slide story

| Slide | Topic | Function |
|---|---|---|
| S00 | AIIS_L4 Secure Development | Cover / mission |
| S01 | It Works. Is It Safe? | Hook |
| S02 | Weather Security Center grows | Continuity |
| S03 | Functional ≠ Security | Core distinction |
| S04 | Find → Understand → Fix → Prove | Mission |
| S05 | Secure Coding | Foundation |
| S06 | How vulnerabilities enter code | Motivation |
| S07 | Input = Trust Boundary | Secure coding map |
| S08 | Secrets ≠ Source Code | Secure coding map |
| S09 | Authentication ≠ Authorization | Secure coding map |
| S10 | Dependency Risk | Secure coding map |
| S11 | Human + AI Review limits | Need for tooling |
| S12 | SAST | Core concept |
| S13 | Shift Left | SDLC placement |
| S14 | Meet Semgrep | Main tool |
| S15 | How Semgrep sees code | Tool mental model |
| S16 | AI + Semgrep + Human | AI for Security |
| S17 | Teacher-provided vulnerable sample | Lab target |
| S18 | BEFORE Scan | Evidence A |
| S19 | Read Finding | Source → Flow → Sink |
| S20 | AI explanation | Evidence B |
| S21 | Human Review | Judgment gate |
| S22 | Root Cause | Engineering analysis |
| S23 | Safer Design / Fix | Evidence C |
| S24 | Regression Test | Evidence D |
| S25 | Re-scan | Evidence E |
| S26 | Before → After | Evidence chain |
| S27 | GitHub traceability | Engineering record |
| S28 | Professional Secure SDLC | Broader map |
| S29 | Mission Complete → L5 | Closure / bridge |

## 3. Story arc check

The lesson follows one continuous question:

```text
AI-generated code works
        ↓
Does that mean it is safe?
        ↓
Secure coding introduces trust boundaries
        ↓
Humans and AI both miss things
        ↓
Use SAST as deterministic inspection
        ↓
Semgrep finds a concrete risky pattern
        ↓
AI explains; human judges
        ↓
Fix the root cause
        ↓
Regression test + re-scan
        ↓
Preserve evidence in GitHub
        ↓
Understand where this fits in Secure SDLC
```

**Result:** coherent; no unrelated detour.

## 4. One Core Tool rule check

Required hands-on security tool:

**Semgrep only.**

Mention-only / Further Exploration:
- Bandit
- GitHub CodeQL
- SonarQube
- Snyk
- Trivy
- OWASP ZAP (future lesson)

**Result:** passes scope-control rule.

## 5. AI for Security check

AI is used for:
- explaining a scanner finding,
- separating facts from inference,
- proposing remediation,
- proposing tests,
- assisting documentation.

AI is NOT treated as:
- security evidence by itself,
- an autonomous authority,
- proof that exploitation occurred,
- proof that the final system is fully secure.

**Result:** aligned with AI-for-Security course direction.

## 6. Vibe Coding integration check

L4 explicitly evolves the workflow:

```text
Old:
Prompt → Code → Run → Done

L4:
Prompt → Code → Run → Test → Scan → Understand → Review → Fix → Test → Re-scan → Evidence
```

**Result:** Vibe Coding is retained but upgraded with security engineering discipline.

## 7. Safety / authorization check

Hands-on work uses:
- local code,
- teacher-provided sample,
- owned Weather Security Center,
- source-code scanning.

No requirement to attack public/third-party systems. No exploit payload creation is required for the L4 learning objective.

**Result:** suitable defensive lab boundary.

## 8. Evidence-based learning check

Required student package:

1. BEFORE Semgrep result
2. Finding interpretation
3. AI analysis prompt + response
4. Human root-cause decision
5. Code diff
6. Functional/regression test
7. AFTER Semgrep result
8. Remaining-risk statement
9. GitHub record

**Result:** clear assessable output.

## 9. L1-style slide design check

Every slide batch defines:
- actual on-slide text,
- visual composition,
- spokesperson expression/action,
- teacher explanation,
- transition to next slide,
- lab/prompt where relevant.

**Result:** follows unified L0–L16 / L1-style detailed reconstruction standard.

## 10. Final canonical L4 statement

> **AIIS_L4 teaches students that secure software is not created by asking AI for “secure code.” It is created through a repeatable evidence-based engineering loop: build, inspect, understand, remediate, test, re-scan, and document. Semgrep is the representative hands-on tool; AI assists interpretation and remediation; the human engineer remains responsible for judgment and verification.**

---

# AIIS_L4 STATUS

**Slide planning:** COMPLETE — S00–S29  
**Storyline:** COMPLETE  
**Primary lab:** COMPLETE  
**AI integration:** COMPLETE  
**Security evidence chain:** COMPLETE  
**L1-style per-slide specification:** COMPLETE  
**Bridge to AIIS_L5:** COMPLETE

Next course planning target: **AIIS_L5 — Supervised Machine Learning I / Classification**, while continuing the same Weather Security Center and AI-for-Security storyline.