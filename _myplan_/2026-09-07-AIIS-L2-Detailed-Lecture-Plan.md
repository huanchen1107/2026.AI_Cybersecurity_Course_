# AIIS_L2 — Spec-Driven AI Engineering
## OpenSpec × Antigravity × Git × GitHub

Status: DETAILED PLANNING IN PROGRESS — 2026-09-07

Master Curriculum Position: L2 / MANAGE

Core statement:

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

Core learning loop:

```text
DEFINE → BUILD → VERIFY → REMEMBER
```

Canonical engineering flow:

```text
REQUEST → OPENSPEC CHANGE → SPEC → ACCEPTANCE CRITERIA
→ ANTIGRAVITY → PLAN → HUMAN PLAN REVIEW → IMPLEMENT
→ DIFF → RUN/TEST → VERIFY AGAINST SPEC → HUMAN REVIEW
→ GIT COMMIT → GITHUB → HISTORY/EVIDENCE
```

## Curriculum Boundary

L2 uses the same Weather Security Center created in L1. It does not rebuild the app. OpenSpec is the engineering method for L2's existing MANAGE responsibility and is not a new curriculum branch.

- Python/FastAPI/API/JSON internals → L3
- Semgrep scanning/remediation → L4
- ML/DL → L5–L10
- Red Team → L11–L12
- Blue Team → L13
- Governance → L14

## Teaching Story — 30 Slides

### PART A — FROM VIBE CODING TO SPEC-DRIVEN DEVELOPMENT — S01–S06

S01 — AI Built It. What Happens Next?
- Reopen L1 Weather Security Center.
- WORKING ✓ is not the end of engineering.
- Ask: who requested the change, what should change, what should not change, how do we know it is done?

S02 — One Sentence Can Change Many Files
- Example request: Add Last Updated.
- AI may touch multiple files.
- One prompt does not imply one controlled change.

S03 — The Vibe Coding Problem
- Vibe Coding is excellent for idea → prototype → working software.
- Growing projects need durable decisions, constraints and history.
- Message: Vibe Coding gets us started. Engineering keeps us under control.

S04 — Prompt vs Spec
- Prompt asks AI to do something.
- Spec defines need, scope, constraints and what DONE means.
- Introduce Engineering Contract concept.

S05 — Meet OpenSpec
- Do not start with syntax.
- OpenSpec answers: What? Why? Scope? Out of Scope? Done?
- Requirements should not live only in chat history.

S06 — Four Layers of AI Engineering
- DEFINE = OpenSpec
- BUILD = Antigravity
- VERIFY = Diff + Test + Acceptance Criteria + Human Review
- REMEMBER = Git + GitHub

### PART B — OUR FIRST OPENSPEC CHANGE — S07–S12

S07 — A Real Request Arrives
- Request: Users need to know when weather data was last refreshed.
- Contrast vague request with engineering change.

S08 — Change = A Unit of Engineering Work
- Introduce canonical change: `add-weather-last-updated`.
- A Change gives the request an identity and durable home.

S09 — WHY / NEED
- Need explains the problem, not implementation.
- Good: users cannot tell data freshness.
- Bad: edit index.html and add a timestamp.
- Teach problem before solution.

S10 — SCOPE / OUT OF SCOPE
- In scope: display Last Updated on dashboard.
- Out: DB schema, auth, API redesign, dependencies.
- Scope prevents AI from solving a small problem with a large rewrite.

S11 — REQUIREMENTS
- Turn intent into explicit expected behavior.
- Example: dashboard must display refresh time near weather data.
- Requirements describe behavior, not unnecessary implementation detail.

S12 — ACCEPTANCE CRITERIA = DEFINITION OF DONE
- Visible Last Updated.
- Existing weather display works.
- Existing API behavior intentionally unchanged.
- No unnecessary dependency.
- Relevant run/test verification passes.

### PART C — ANTIGRAVITY IMPLEMENTS THE SPEC — S13–S18

S13 — Give AI the Project + Spec, Not Just a Prompt
- AI context = existing repo + OpenSpec Change + constraints + acceptance criteria.

S14 — INSPECT FIRST
- Ask agent to inspect repository before modification.
- Identify likely affected files and assumptions.

S15 — PLAN BEFORE CODE
- AI proposes minimal implementation plan.
- No file modification yet.
- Expected files + reason for each change.

S16 — HUMAN PLAN REVIEW
- Is plan inside scope?
- Unexpected file changes?
- New dependencies?
- Does plan satisfy requirements?
- Human approves or revises.

S17 — IMPLEMENT THE MINIMAL CHANGE
- Agent executes approved plan.
- Minimal change; no unrelated refactor.

S18 — AI SUMMARY IS NOT EVIDENCE
- AI can summarize files changed, but students must inspect actual project/diff.
- Introduce transition to verification.

### PART D — VERIFY: DID AI DO WHAT THE SPEC SAID? — S19–S23

S19 — CHANGED FILES
- Modified / added / deleted files.
- Unexpected files are a review signal.

S20 — DIFF = BEFORE vs AFTER
- Read a small before/after example.
- Diff answers what actually changed, not what AI claims changed.

S21 — RUN / TEST
- Does Weather Security Center still run?
- Does new feature appear?
- Did existing behavior break?
- Keep implementation-level Python detail for L3.

S22 — VERIFY AGAINST ACCEPTANCE CRITERIA
- Turn each criterion into PASS / FAIL / NEEDS REVIEW.
- A working-looking UI is not enough if criteria are unmet.

S23 — HUMAN DECISION
- ACCEPT / REVISE / REJECT.
- Human approval happens after evidence, not after persuasive AI prose.

### PART E — GIT REMEMBERS — S24–S27

S24 — SOFTWARE NEEDS MEMORY
- Yesterday worked; today broke. What changed?
- Git = version history + change evidence, not merely backup.

S25 — COMMIT = NAMED CHECKPOINT
- Working files → reviewed change → commit.
- Good message: `Add last-updated indicator to weather dashboard`.
- Avoid meaningless messages like `update`.

S26 — GIT ≠ GITHUB
- Git = local version control.
- GitHub = remote/shared engineering repository.
- Push/sync connects local history to shared project memory.

S27 — GITHUB = ENGINEERING MEMORY
- Specs + source + tests + evidence + history.
- Later Red Team findings, Blue Team patches and final project evidence return to same repository.

### PART F — COMPLETE LAB + HANDOFF — S28–S30

S28 — STUDENT MISSION: ONE CONTROLLED CHANGE
- Use `add-weather-last-updated` or instructor-approved equivalent.
- Follow the full SDD workflow; do not rebuild app.

S29 — SHOW ME THE EVIDENCE
Students submit:
1. request
2. OpenSpec Change
3. Need/Why
4. Scope/Out of Scope
5. Acceptance Criteria
6. AI plan
7. human plan review
8. files changed
9. diff
10. run/test evidence
11. acceptance verification
12. human decision
13. commit message
14. GitHub history evidence

S30 — FROM MANAGE TO UNDERSTAND

```text
L1: AI BUILDS. HUMAN VERIFIES.
L2: SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.
L3: DON'T JUST RUN THE CODE. UNDERSTAND THE FLOW.
```

Closing question:

> We know WHY the change exists, WHAT changed, WHETHER it met the spec, and WHERE history is recorded. But do we understand HOW the code works?

Handoff: AIIS_L3 — Python × FastAPI × HTTP × API × JSON.

## Cross-Lesson Foreshadowing Rule

OpenSpec is formally taught in L2 and reused afterward. Earlier lessons should only preview enough to make L2 natural:
- L0: preview Spec-Driven AI Engineering as part of the engineering toolchain.
- L1: structured Build Prompt and acceptance thinking; mention that durable specifications come next.
- L2: formally teach OpenSpec/SDD.
- L3+: reuse without repeatedly teaching the entire workflow.

Future lesson design must check whether new prerequisites need PREVIEW → TEACH → REUSE placement across the curriculum.