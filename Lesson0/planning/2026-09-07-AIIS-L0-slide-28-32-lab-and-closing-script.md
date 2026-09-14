# AIIS_L0 — Slides 28–32 Detailed Lab & Closing Script

Date: 2026-09-07
Parent plan: `2026-09-07-AIIS-L0-32-slide-detailed-lecture-plan.md`
Status: Detailed lecture script — final section

## Story

```text
AIIS_L0_LAB01
      ↓
Security Event Analyzer
      ↓
YAML Specification
      ↓
Antigravity / Coding Agent
      ↓
Python
      ↓
Run → Test → Evidence
      ↓
ALL TESTS PASS
      ↓
But is the detection rule good?
      ↓
False Positive / Slow Pattern
      ↓
Rule ≠ Intelligence ≠ Truth
      ↓
Time Window → Features → Data → ML → Sequence Analysis
      ↓
AIIS JOURNEY
```

# Slide 28 — AIIS_L0_LAB01: Security Event Analyzer

## Core
**Your First AI-Assisted Security Program — From Requirement to Running Code**

```text
SECURITY EVENTS
      ↓
login_success
login_failed
login_failed
login_failed
      ↓
PYTHON
      ↓
COUNT + ANALYZE
      ↓
⚠ WARNING
```

Mission:
- Read events
- Count success
- Count failure
- Detect failed login count ≥ 3
- Print warning
- Test behavior

Presenter: 煥哥 coding pose, laptop visible, still engaging students.

Teacher framing: Do not say merely “ask AI to write a program.” Treat this as giving a Security Requirement to an AI Engineer.

Sample events:

```text
login_success
login_failed
login_failed
login_failed
login_success
```

Start intentionally simple:

```text
IF failed_login_count >= 3
THEN warning
```

Engineering principle: **Start simple.** Do not introduce ML yet; students should first experience why simple rules eventually become insufficient.

Expected example output:

```text
Total Events : 5
Success      : 2
Failed       : 3

WARNING:
Multiple login failures detected.
```

Transition: Do not use a vague “write me a security program” prompt. Specify the requirement.

# Slide 29 — Give AI a Specification, Not a Wish

Compare:

BAD:
```text
幫我寫一個 login security program
```

GOOD: structured, testable specification.

Core:
> **Prompt tells AI what you want. Specification tells us how to verify it.**

YAML is not the learning goal; structured requirements are.

Canonical AIIS Lab sections:
- task / id / title / role
- context
- learning_objectives
- requirements
- security_requirements
- implementation_workflow
- tests / acceptance criteria
- deliverables
- constraints / safety
- final_report / evidence

Suggested L0 YAML:

```yaml
task:
  id: AIIS_L0_LAB01
  title: Security Event Analyzer

role:
  You are a Python developer working in an educational security lab.

learning_objectives:
  - understand simple security events
  - practice AI-assisted coding
  - verify generated code with tests

requirements:
  - accept login_success and login_failed events
  - count total events
  - count successful logins
  - count failed logins
  - print a warning when failed logins >= 3

security_requirements:
  - use only local sample data
  - do not connect to external systems
  - do not perform real login attempts
  - do not attack any service

implementation_workflow:
  - explain the plan
  - write minimal Python code
  - run the program
  - execute the required tests
  - fix errors if tests fail

tests:
  - failed_logins: 0
    warning: false
  - failed_logins: 2
    warning: false
  - failed_logins: 3
    warning: true
  - failed_logins: 5
    warning: true

deliverables:
  - Python source code
  - test results
  - short explanation

final_report:
  - what was implemented
  - tests passed or failed
  - known limitations
```

Transition: Give specification to the agent, then Run and Test instead of trusting a “Done” message.

# Slide 30 — Run → Test → Evidence

Flow:

```text
CODE → RUN → TEST → EVIDENCE
```

Test matrix:

| Test | Failed Login | Expected | Result |
|---|---:|---|---|
| T01 | 0 | No Warning | PASS |
| T02 | 2 | No Warning | PASS |
| T03 | 3 | Warning | PASS |
| T04 | 5 | Warning | PASS |

Teach boundary testing: because rule is `>= 3`, values 2 and 3 are especially important.

Core:
> AI saying “Done” is not evidence. AI saying “Everything works correctly” is not evidence. Execute defined tests.

If all pass, the correct conclusion is:
> **Implementation matches the specified rule.**

Do NOT conclude yet that the security detection method is correct in the real world.

GitHub evidence concept:

```text
GitHub
├── analyzer.py
├── tests/
├── README / Lab Note
└── Evidence
```

Core:
> **GitHub remembers what we built and how we verified it.**

Transition: All tests pass. Does that mean this is a good security detection rule?

# Slide 31 — PASS ≠ Intelligent

This is a key pedagogical slide.

## Scenario A — False Positive

A legitimate user mistypes a password three times. Rule fires. The user may not be an attacker.

Introduce:

```text
Normal behavior
      ↓
Detected as attack
      ↓
FALSE POSITIVE
```

## Scenario B — Slow / contextual pattern

An attacker may distribute attempts over time or across context. A naive count/reset rule can miss meaningful patterns.

Important: This is conceptual detection analysis, not instruction for attacking a real service.

## Three layers

```text
CODE CORRECTNESS
程式有沒有照規格做？
        ↓
RULE QUALITY
規則有沒有描述好問題？
        ↓
REAL-WORLD EFFECTIVENESS
在真實世界是否有效？
```

Core statement:
> **Tests can show that code follows the specification. Tests do not automatically prove that the specification models reality well.**

Chinese:
> **測試可以證明程式符合目前規格，但不能自動證明規格本身就是好的世界模型。**

Ask what is missing. Reveal future learning needs:

```text
TIME → TIME WINDOW
MORE INFORMATION → FEATURES
MANY EXAMPLES → DATA
LEARN PATTERNS → MACHINE LEARNING
SEQUENCE → DEEP LEARNING / SEQUENCE ANALYSIS
```

Teacher line:
> 現在你們終於有理由學 Machine Learning 了。不是因為課綱說要教 ML，而是因為簡單 Rule 開始不夠。

# Slide 32 — The AIIS Journey Starts Here

No new knowledge. Close the complete causal story.

```text
Machine
  ↓
Energy
  ↓
Information
  ↓
Intelligence
  ↓
AI REVOLUTION
  ↓
ANI
  ↓
Discriminate → Generate → Act
                         ↓
                    AI CAN ACT
                         ↓
                  SECURITY MATTERS
                         ↓
Asset → Threat → Vulnerability → Risk → CIA
                         ↓
             AI WEATHER SECURITY CENTER
                         ↓
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

Presenter: 煥哥 confident/open-hand closing pose; not celebration, because the journey is beginning.

Closing teaching message:

Technology revolutions amplify capability. Machine technology amplified physical capability; information technology amplified information processing; AI increasingly amplifies tasks associated with cognitive capability. Greater capability brings greater responsibility.

AIIS is therefore not about merely using AI to write lots of code, and not about collecting attack tools. It is about using AI to build systems, understanding them, verifying them, finding weaknesses in authorized environments, fixing them, producing evidence, and governing them responsibly.

Final statements:

> **AI is the capability. Information Security is the discipline.**

> **AI proposes. Human understands. Security validates.**

> **Learn it in the Range. Prove it in our Lab. Fix it in our Code.**

Next:

**AIIS_L1 — AI Tools × Prompt × Vibe Coding × Antigravity × GitHub**

# L0 Completion Contract

AIIS_L0 is complete only if students leave understanding these ideas:
1. Human technological revolutions repeatedly amplify capability.
2. AI is significant because it increasingly supports judgment, generation, planning and action.
3. Agentic AI raises security responsibility because it can act on systems and resources.
4. Security concerns the whole system, not only an AI model.
5. Asset, Threat, Vulnerability, Risk and CIA provide a first security mental model.
6. AI Weather Security Center is the semester-long shared system.
7. AIIS follows BUILD → LEARN → ATTACK → DEFEND → GOVERN.
8. AI-assisted engineering means Understand → Generate → Review → Execute → Verify.
9. AI-generated code must be tested and evidenced.
10. Passing tests proves conformance to specified behavior, not automatically real-world security effectiveness.
11. Simple rule limitations naturally motivate features, time windows, ML and later sequence analysis.
12. Offensive validation is restricted to authorized lab/range environments.
