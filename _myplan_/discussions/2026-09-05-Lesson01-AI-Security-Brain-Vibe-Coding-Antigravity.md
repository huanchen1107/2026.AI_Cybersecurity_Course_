# Lesson 1 — Build Your First AI Security Brain

**Course:** 2026 AI × Cybersecurity  
**Planning date:** 2026-09-05  
**Status:** Detailed lesson architecture / teaching plan  
**Role in course:** Foundation for Lesson 2 AI Weather Security Center and Lesson 3 AI Red Team × Kali Linux

---

## 1. Lesson 1 Mission

Lesson 1 should not begin as a traditional Python or cybersecurity theory lecture. Students enter the course as **Junior AI Security Engineers** and immediately face a practical question:

> If we give AI a network/security event, can it decide whether the behavior is normal or an attack?

The lesson has two parallel goals:

1. **AI as a TOOL** — use LLMs and AI coding agents to think, explain, build, debug, and review.
2. **AI as a TECHNOLOGY** — understand and build a real machine-learning security model.

This establishes the full-course progression:

**USE AI → BUILD AI → ATTACK AI → DEFEND AI**

---

## 2. Lesson 1 Toolchain

Lesson 1 must introduce the common tool workflow that students will reuse throughout the course.

| Layer | Tool / Concept | Student role |
|---|---|---|
| AI Assistant | ChatGPT / Gemini | Ask, explain, plan, analyze, debug |
| AI Coding Agent | Antigravity | Read and modify projects, generate code, run/test/debug |
| Workspace | VS Code / Terminal / Python | Inspect and execute real code |
| Project Memory | Git / GitHub | Preserve versions, evidence, code and project history |
| ML Stack | Python + pandas + scikit-learn | Build the security model |

### Key distinction

Chat-oriented AI is useful for questions such as:

- What is a Decision Tree?
- Why is Recall important in intrusion detection?
- Explain this error.
- Review this model result.

Antigravity is used as an **agentic coding environment**:

- Read this project.
- Create `src/train.py`.
- Add a Decision Tree model.
- Run the program and tests.
- Diagnose and fix the error.
- Explain what changed.

Students should understand that AI assistance and AI coding agents are related but different working modes.

---

## 3. Secure Vibe Coding — Core Course Workflow

Vibe Coding is introduced formally in Lesson 1, but it must not be taught as blind code generation.

The course standard is **Secure Vibe Coding**:

```text
1. THINK
   ↓
What problem are we solving?

2. SPEC
   ↓
Define requirements and constraints.

3. GENERATE
   ↓
Ask the AI agent to build a small implementation.

4. READ
   ↓
Inspect what AI actually created.

5. RUN
   ↓
Execute the real program.

6. TEST
   ↓
Test normal, abnormal, and edge cases.

7. VERIFY
   ↓
Check whether results are reasonable.

8. SECURITY REVIEW
   ↓
Look for security assumptions, unsafe behavior and failure modes.
```

Student mnemonic:

> **Prompt → Build → Run → Test → Verify → Secure**

Core principle:

> AI can generate code. The human remains responsible for understanding, verification, testing and security.

---

## 4. Lesson Structure — 12 Parts

| Part | Topic | Core question | Main activity |
|---|---|---|---|
| 1 | Welcome to AI × Cybersecurity | Why combine AI and security? | Attack Detective |
| 2 | Your AI Security Toolbox | What tools will we use? | ChatGPT/Gemini/Antigravity/GitHub workflow |
| 3 | Secure Vibe Coding | How should we build with AI safely? | Prompt → Build → Run → Test → Verify → Secure |
| 4 | Antigravity Live Demo | Can an AI agent build a security app? | Build login-risk analyzer |
| 5 | Is This Really AI? | Rules or learning? | Rule-based vs ML |
| 6 | Security Data | What does AI actually see? | Security dataset exploration |
| 7 | Features & Labels | How does reality become numbers? | Feature Detective |
| 8 | First ML Security Model | How does a model learn? | Decision Tree |
| 9 | Train/Test/Evaluation | Is the model really good? | Split + confusion matrix |
| 10 | Security Metrics | Why can accuracy be dangerous? | Precision / Recall / F1 |
| 11 | Explain & Fool the AI | Why did it decide this, and can it be evaded? | Feature importance + adversarial thinking |
| 12 | Final Lab | Can students build a Security Brain? | AI Security Brain mini project |

---

# Part 1 — Welcome to AI × Cybersecurity

Start with an event instead of definitions:

```text
User: admin
Login failures: 37
Countries: 6
Time: 02:43 AM
Ports scanned: 126
Traffic: 482 MB
```

Ask:

> Is this user an attacker?

Then:

> How did you decide?

Students are already performing classification using features and patterns.

Introduce the operational problem:

```text
Massive Security Events
        ↓
Feature Engineering
        ↓
Machine Learning
        ↓
Risk Prediction
        ↓
AI Security Analyst
        ↓
Human Decision
```

---

# Part 2 — Your AI Security Toolbox

Introduce the semester workflow:

```text
Human
 │
 ├─ defines the problem
 ├─ defines requirements
 ├─ evaluates evidence
 └─ remains responsible for security
       │
       ▼
AI Assistant
ChatGPT / Gemini
       │
       ▼
AI Coding Agent
Antigravity
       │
       ▼
Python / ML / Web Application
       │
       ▼
Cybersecurity System
       │
       ▼
Git / GitHub Evidence & History
```

Important teaching point:

**AI ≠ ChatGPT.**

```text
Artificial Intelligence
│
├─ Machine Learning
│  ├─ Decision Tree
│  ├─ Random Forest
│  └─ SVM
│
├─ Deep Learning
│  ├─ CNN
│  ├─ RNN
│  └─ Transformer
│
└─ Generative AI
   └─ LLM
      ├─ ChatGPT
      ├─ Gemini
      └─ Claude
```

The course will use AI tools while also teaching how AI itself works.

---

# Part 3 — What Is Vibe Coding?

Show two contrasting approaches.

Unsafe version:

> Build me an IDS.

Then blindly run whatever AI generates.

Course version:

> Define the goal, specify inputs/outputs and constraints, generate the smallest understandable version, inspect it, run it, test it, verify results, then perform a security review.

Introduce **Secure Vibe Coding** as a recurring course discipline rather than merely a productivity trick.

---

# Part 4 — Antigravity Live Demo

Teacher starts without manually writing the program.

Example agent request:

```text
Create a simple cybersecurity login-risk analyzer.

Input:
- failed login count
- login hour
- number of countries
- number of ports accessed

Output:
- LOW / MEDIUM / HIGH risk
- explanation of why

Use Python.
Keep the implementation simple enough for a beginner to understand.
```

Test a normal event:

```text
failed_login = 2
hour = 14
countries = 1
ports = 3

Risk: LOW
```

Then test a suspicious event:

```text
failed_login = 45
hour = 2
countries = 7
ports = 130

Risk: HIGH
```

Now stop and ask:

> Is this really Artificial Intelligence?

The generated application may simply contain rules such as:

```python
if failed_login > 20:
    risk = "HIGH"
```

This creates the transition into Part 5.

---

# Part 5 — Rule-Based vs Machine Learning

Explain:

```text
Rule-Based System
Human writes the rules
        ↓
IF failed_login > 20
        ↓
HIGH RISK
```

versus:

```text
Machine Learning
Historical Examples + Labels
        ↓
Model Training
        ↓
Model discovers useful patterns
        ↓
Prediction
```

Core question:

> Instead of telling the computer every security rule, can we let it learn patterns from previous attacks?

---

# Part 6 — Security Data

Humans see:

> This account looks suspicious.

A model sees:

```text
failed_login = 37
country_count = 6
login_hour = 2
port_count = 126
traffic_mb = 482
```

Introduce:

**Feature = measurable information used by a model.**

Pipeline:

```text
Real World
   ↓
Security Event
   ↓
Features
   ↓
Numbers
   ↓
Machine Learning
```

---

# Part 7 — Feature Detective + Labels

Compare:

```text
User A
failed_login = 1
port_count = 2
traffic_mb = 15
login_hour = 14
```

with:

```text
User B
failed_login = 52
port_count = 147
traffic_mb = 680
login_hour = 3
```

Ask students which looks more suspicious and why.

They have now performed informal **security feature engineering**.

Then introduce labels:

```text
X = Features
failed_login
port_count
traffic_mb
login_hour
...

Y = Label
0 = Normal
1 = Attack
```

Concept:

```text
X → ML Model → predicted y
```

Introduce supervised learning through examples rather than memorized definitions.

---

# Part 8 — Build the First ML Security Model

Recommended first model: **Decision Tree** because students can visualize its decisions.

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
```

Conceptual view:

```text
Security Examples
        ↓
     model.fit()
        ↓
Find Patterns
        ↓
Decision Rules
```

Possible learned structure:

```text
failed_login > 20?
       │
   ┌───┴───┐
  No      Yes
  │         │
Normal   port_count > 50?
              │
          ┌───┴───┐
         No      Yes
                  │
                Attack
```

---

# Part 9 — Train/Test + Confusion Matrix

Use the exam analogy:

> If students receive the exact exam and answers beforehand and score 100, have we proved that they understand the subject?

Therefore:

```text
Dataset
  │
  ├─ 80% Training
  └─ 20% Testing
```

Introduce:

```python
from sklearn.model_selection import train_test_split
```

Then confusion matrix:

| | Predicted Normal | Predicted Attack |
|---|---:|---:|
| Actual Normal | TN | FP |
| Actual Attack | FN | TP |

Ask:

> Which error is especially dangerous for a security monitoring system?

False Negative means a real attack is classified as normal.

---

# Part 10 — Accuracy Can Be Dangerous

Example:

```text
1000 events
950 Normal
50 Attack
```

A useless model predicts every event as Normal.

Accuracy = 95%.

But all 50 attacks are missed.

Core lesson:

> **Accuracy alone is dangerous in cybersecurity.**

Introduce the meaning of:

- Precision
- Recall
- F1

without overloading the first lesson with mathematical derivations.

Security interpretation is more important than memorizing formulas.

---

# Part 11 — Explainable AI + Adversarial Thinking

A security model predicts:

```text
Prediction: ATTACK
Confidence: 91%
```

Ask:

> Why?

Possible feature importance:

```text
failed_login    38%
port_count      27%
traffic_mb      18%
login_hour      10%
country_count    7%
```

Key principle:

> AI is not an oracle. Security analysts need evidence and explanations.

Then introduce an adversarial exercise.

Original:

```text
failed_login = 50
port_count = 120
→ ATTACK
```

Modify behavior:

```text
failed_login = 15
port_count = 40
→ possibly NORMAL
```

Ask:

> The attacker may still be attacking. Why did the model stop detecting it?

Introduce **adversarial thinking / detection evasion** at a conceptual, controlled level.

This prepares students for Lesson 3 AI Red Team.

---

# Part 12 — Final Lab: AI Security Brain

Students use the Secure Vibe Coding workflow and Antigravity to build a small application.

Input example:

```text
Failed Login: [ ]
Ports Accessed: [ ]
Traffic MB: [ ]
Login Hour: [ ]
Countries: [ ]
```

Output example:

```text
SECURITY ANALYSIS

Risk: HIGH
Prediction: ATTACK
Confidence: 87%

Top Reasons:
1. Failed login unusually high
2. Port scanning behavior
3. Abnormal login time

Recommended Action:
Investigate this host.
```

Students must demonstrate not only that the program runs, but also:

1. What features it uses.
2. What model it uses.
3. How training/testing is separated.
4. At least one normal test.
5. At least one attack-like test.
6. At least one edge/adversarial test.
7. What metric they use to evaluate it.
8. One limitation or security risk in the model.

---

## 5. Lesson 1 Knowledge Map

```text
CYBERSECURITY EVENT
        │
        ▼
   Security Data
        │
        ▼
      Feature
        │
        ▼
      Dataset
      X     y
        │
        ▼
 Machine Learning
        │
   ┌────┴────┐
   ▼         ▼
Training   Testing
             │
             ▼
         Prediction
             │
      ┌──────┴──────┐
      ▼             ▼
 Evaluation      Explanation
Precision/Recall  Why this alert?
      │             │
      └──────┬──────┘
             ▼
      Security Analyst
             │
             ▼
       HUMAN DECISION
```

Around the entire workflow sits the engineering loop:

```text
Human
  ↓
ChatGPT / Gemini
  ↓
Antigravity
  ↓
Code
  ↓
Run
  ↓
Test
  ↓
Verify
  ↓
Security Review
  ↓
Git / GitHub
```

---

## 6. Three Ways AI Appears in This Course

### AI as a TOOL

Use LLMs and coding agents to accelerate thinking, coding, debugging and analysis.

### AI as a TECHNOLOGY

Build and understand ML/DL models used for cybersecurity.

### AI as a TARGET

Understand that AI systems themselves can fail, be manipulated, attacked or abused.

This creates the semester theme:

> **USE AI → BUILD AI → ATTACK AI → DEFEND AI**

---

## 7. Connection to Later Lessons

```text
Lesson 1
AI Security Brain
“How can AI recognize threats?”
        │
        ▼
Lesson 2
AI Weather Security Center
“Turn AI into a real security-aware system.”
        │
        ▼
Lesson 3
AI Red Team × Kali Linux
“Attack our authorized isolated lab and test whether it survives.”
        │
        ▼
Lesson 4
Defense / Detection / AI Blue Team
“Detect, analyze and defend against attacks.”
        │
        ▼
Lesson 5
AI Security Final Challenge
“Red × Blue × AI × Secure Vibe Coding.”
```

Lesson 1 therefore establishes the common vocabulary, tools and engineering discipline used throughout the remaining course.

---

## 8. Teaching Principle

Do not make Lesson 1 a long software installation/tutorial session.

Students should see the tools only when the tools help solve the current security problem.

Recommended rhythm:

> **Question → Demo → Student prediction → AI tool → Code → Result → Security interpretation → Challenge**

Every technical concept should answer a security question, and every AI-generated artifact should be inspected and verified by a human.
