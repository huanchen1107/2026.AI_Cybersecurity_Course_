# AIIS_L2 — MANAGE：Spec-Driven AI Engineering
## OpenSpec × Antigravity × Git × GitHub

> **Status: CANONICAL — 2026-09-07**
>
> AIIS_L2 remains inside the fixed 16-Lesson Master Curriculum. OpenSpec is the engineering method used to make L2's existing MANAGE mission explicit; it is **not a new lesson or curriculum branch**.

## Mission

核心問題：

> AI 已經幫你做出程式。但 AI 為什麼這樣改？依據哪一份規格？完成的標準是什麼？我們如何證明它真的完成？

L2 使用 L1 的同一個 **AI Weather Security Center**，不重新建立另一個 App。

L2 將學生從：

```text
Prompt → Code
```

帶到：

```text
Request → Spec → Plan → Implement → Verify → Evidence
```

## Four-Layer Mental Model

| Layer | Method / Tool | Core Question |
|---|---|---|
| **DEFINE** | OpenSpec | 要改什麼？為什麼？完成標準是什麼？ |
| **BUILD** | Antigravity | AI 如何依照 Spec 實作？ |
| **VERIFY** | Diff + Test + Acceptance Criteria + Human Review | AI 做的是不是我們要求的？ |
| **REMEMBER** | Git + GitHub | 如何保存變更、證據與歷史？ |

```text
DEFINE
OpenSpec
   ↓
BUILD
Antigravity
   ↓
VERIFY
Diff + Test + Acceptance Criteria
   ↓
REMEMBER
Git + GitHub
```

## Canonical Workflow

```text
REQUEST
  ↓
OPENSPEC CHANGE
  ↓
SPEC / REQUIREMENTS
  ↓
ACCEPTANCE CRITERIA
  ↓
ANTIGRAVITY
  ↓
PLAN
  ↓
HUMAN PLAN REVIEW
  ↓
IMPLEMENT
  ↓
DIFF
  ↓
RUN / TEST
  ↓
VERIFY AGAINST SPEC
  ↓
HUMAN REVIEW
  ↓
GIT COMMIT
  ↓
GITHUB
  ↓
HISTORY / EVIDENCE
```

Core shorthand:

> **DEFINE → BUILD → VERIFY → REMEMBER**

Core statement:

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

## Why OpenSpec Belongs Here

L2 is not a Git-command lesson and not an OpenSpec-syntax course. It teaches a minimal **Spec-Driven Development** habit:

> Requirements must not exist only inside a chat prompt.

A change should have a durable description of:
- Need / Why
- Scope
- Requirements
- Constraints
- Acceptance Criteria
- Evidence of completion

OpenSpec provides this persistent engineering contract; Antigravity implements it; tests/diff/human review verify it; Git/GitHub preserve the result.

## Primary Topics

1. Vibe Coding vs Spec-Driven Development
2. Why Prompt alone is not an engineering contract
3. Request → Change
4. OpenSpec as persistent project specification
5. Need / Why
6. Scope and Out of Scope
7. Requirements
8. Constraints
9. Acceptance Criteria
10. Antigravity reads project + spec context
11. Plan before implementation
12. Human review of AI plan
13. Controlled implementation
14. Changed files and Diff
15. Run / Test
16. Verify implementation against Acceptance Criteria
17. Git repository / working tree concept
18. Commit as named engineering checkpoint
19. Meaningful commit message
20. GitHub as shared engineering memory
21. History / traceability / evidence
22. Recovery / rollback concept

## Required Lab — One Small OpenSpec Change

Students reopen their L1 Weather Security Center and implement **one small, safe feature change**.

Recommended canonical example:

```text
Change: add-weather-last-updated

Need:
Users should know when the displayed weather data was last refreshed.

Scope:
Add a Last Updated indicator to the dashboard.

Out of Scope:
- database schema changes
- authentication changes
- API redesign
- new dependencies

Acceptance Criteria:
1. Dashboard visibly shows Last Updated.
2. Existing weather display still works.
3. Existing API behavior is not intentionally changed.
4. No unnecessary dependency is added.
5. Relevant run/test verification passes.
```

The student workflow is mandatory:

```text
Create / Review OpenSpec Change
→ Ask Antigravity to inspect repo and spec
→ AI proposes implementation plan
→ Human reviews plan
→ AI implements minimal change
→ Inspect changed files
→ Inspect diff
→ Run / test
→ Check every Acceptance Criterion
→ Human approves
→ Commit
→ Push / sync GitHub
→ Inspect history / evidence
```

## Student Evidence

Students submit evidence of:
1. original request
2. OpenSpec Change
3. Need / Why
4. Scope / Out of Scope
5. Acceptance Criteria
6. AI implementation plan
7. human plan review
8. files changed
9. diff reviewed
10. run/test result
11. acceptance-criteria verification
12. human final decision
13. commit message
14. GitHub commit/history

## What L2 Does NOT Own

L2 must stay inside the 16-Lesson Master Curriculum boundary.

- Detailed Python syntax → **L3**
- FastAPI / HTTP / API / JSON internals → **L3**
- Semgrep scan/remediation/re-scan → **L4**
- Supervised ML → **L5–L7**
- Deep Learning → **L9–L10**
- Kali / TryHackMe / Red Team → **L11–L12**
- Deep Blue Team remediation → **L13**
- ISO 27001 / Risk Governance → **L14**

OpenSpec is therefore an **engineering backbone**, not another subject branch.

## Reuse Across the Semester

L2 teaches the method once. Later lessons reuse it without reteaching the whole OpenSpec workflow.

```text
L2 Feature Request
→ OpenSpec Change → Implement → Verify → Commit

L4 Security Finding
→ OpenSpec Change → Secure Fix → Test → Re-scan → Verify

L5–L10 ML/DL Engineering Change
→ Requirement → Implementation / Experiment → Evaluation → Evidence

L13 Verified Red-Team Finding
→ OpenSpec Change → Root Cause → Fix → Regression Test → Evidence

L15–L16 Final Project
→ Spec History + Code History + Test Evidence + Security Evidence
```

## Handoff to L3

At the end of L2 students know:

> We know **WHY** the change exists.
> We know **WHAT** changed.
> We know **WHETHER** it met the acceptance criteria.
> We know **WHERE** the history is recorded.

The next question becomes:

> **But do we understand HOW the code actually works?**

That is AIIS_L3 — Python × FastAPI × HTTP × API × JSON.
