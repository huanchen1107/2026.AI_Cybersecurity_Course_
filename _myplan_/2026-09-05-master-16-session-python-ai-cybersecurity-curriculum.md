# 2026-09-05 Master Plan — 16-Session Python AI × Cybersecurity Curriculum

## Course Positioning

AI 是能力，Cybersecurity 是主線。

```text
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

Shared semester system: `AI Weather Security Center`.

## 16 Sessions

| # | Theme | Core Outcome |
|---|---|---|
| 1 | Introduction — AI × Cybersecurity | Understand semester mission, AI/ML/DL map, security ethics and authorization |
| 2 | AI Security Engineer Toolbox | Prompt, Vibe Coding, Antigravity, GitHub, AI-assisted workflow |
| 3 | BUILD — FastAPI Weather Security Center | Build Python/FastAPI/SQLite app with login, roles, logs |
| 4 | How to Build an AI Cybersecurity Project | Proposal, architecture, threat model, data and evaluation plan |
| 5 | Supervised ML I — Classification | Features, labels, train/test, Logistic Regression/KNN, phishing/security classification |
| 6 | Supervised ML II — Tree Models | Decision Tree, Random Forest, feature importance, IDS example |
| 7 | Supervised ML III — Security Evaluation | Confusion Matrix, Precision, Recall, F1, ROC-AUC concept, FP/FN, imbalance, threshold |
| 8 | Midterm AI Security Engineering Review | Working baseline, architecture, threat model, ML evidence |
| 9 | Deep Learning I — Neural Networks for Security | MLP/PyTorch, compare classical ML vs neural network |
| 10 | Deep Learning II — Security Sequence Analysis | CNN/sequence/LSTM-GRU concepts, temporal attack patterns |
| 11 | AI Red Team I — Learn the Attack | TryHackMe/Kali, scope, recon, enumeration, AI-assisted interpretation |
| 12 | AI Red Team II — Prove it in Our Lab | Transfer technique to local Weather Cyber Range, evidence-based findings |
| 13 | AI Blue Team — Fix Our Code | OWASP, root cause, minimal patch, pytest, security regression |
| 14 | GOVERN — ISO 27001 × Risk | Asset/threat/vulnerability/risk/control/residual risk integration |
| 15 | Final Project Demo I | Integrated project presentation |
| 16 | Final Project Demo II | Integrated project presentation and final evidence package |

## Shared Architecture

```text
Weather API / Fake Sensor
        ↓
Python + FastAPI
        ↓
SQLite / SQLAlchemy
   ┌────┼──────────┐
   ↓    ↓          ↓
Weather Users  Security Events
   ↓    ↓          ↓
Dashboard Login   Logs
        ↓
Supervised ML
        ↓
Deep Learning
        ↓
TryHackMe — Learn
        ↓
Local Weather Cyber Range — Transfer
        ↓
AI Blue Team — Fix
        ↓
ISO 27001 / Risk — Govern
```

## Environment Contract

### Secure Production / Demo
- Vercel or production-like hosting
- secure build only
- non-destructive verification only
- no classroom exploitation target

### Local Cyber Range
- Docker / VM / localhost
- intentionally vulnerable teacher-controlled labs
- offensive exercises only under explicit course authorization

### External Authorized Training Range
- TryHackMe / CTF / other explicit training scope
- students follow provider rules and instructor-defined learning scope

Core phrase:

> Learn it in the Range. Prove it in our Lab. Fix it in our Code.

## Required Teaching Contract for Every Topic

Every Lesson / Part must contain:

1. `Concept` — clear explanation before tools
2. `Security Meaning` — why the concept matters to security
3. `Practical Example / Lab` — observable implementation
4. `Antigravity YAML Prompt` — directly usable implementation prompt
5. `Test / Evidence` — tests, logs, screenshots, reports, commits, or metrics
6. `Reflection` — student explains result, assumptions, and remaining risk

## Antigravity Prompt Standard

Every YAML prompt should preferably include:

```yaml
task:
  id: unique-task-id
  title: clear engineering outcome
  role: explicit engineer role

context:
  project: AI Weather Security Center
  stack: {}
  environment: authorized_context

learning_objectives: []
requirements: {}
security_requirements: []
implementation_workflow: []
tests: []
constraints: []
deliverables: []
final_report:
  include: []
```

Antigravity should normally be instructed to:
- inspect the repository first
- state assumptions
- make a minimal plan
- modify only necessary files
- add tests
- run tests
- review security impact
- summarize evidence and unresolved risks

## Spiral Learning Contract

Important security knowledge is not taught only once.

Example:

```text
BUILD
Understand the control
   ↓
ATTACK
Experience the weakness in authorized lab
   ↓
DEFEND
Fix root cause and regression-test
   ↓
GOVERN
Translate technical evidence into risk and controls
```

This applies to:
- authentication
- password security
- session security
- authorization / RBAC / IDOR concepts
- injection
- XSS / output safety
- CSRF concepts
- input validation
- dependency/supply-chain risk
- security logging
- safe error handling

## Final Project Minimum Requirements

Every team must demonstrate:
1. working system
2. cybersecurity problem statement
3. at least one supervised ML model
4. security-oriented evaluation
5. threat model
6. authorized red-team validation
7. blue-team fix
8. security regression evidence
9. risk analysis
10. GitHub documentation / reproducibility

Advanced optional items:
- Deep Learning
- multiple-model comparison
- anomaly detection
- advanced dashboard
- advanced security automation

## Safety Principle

Publicly accessible does not mean publicly authorized to attack.

Offensive activity is restricted to localhost, own VM/Docker, teacher-designated systems, CTF, TryHackMe, deliberately vulnerable apps, or other explicitly authorized environments.