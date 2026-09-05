# _myplan_ — ChatGPT ↔ GitHub ↔ Antigravity Bidirectional Planning Layer

`_myplan_` is the persistent planning and handoff layer for this course repository. It is not the canonical teaching-content directory.

## Core model

```text
ChatGPT / Human discussion
        ↓
_myplan_ planning state
        ↓
GitHub persistent memory
        ↓
Antigravity / Codex / Gemini / Claude
        ↓
implementation + evidence + discoveries
        ↓
CURRENT / DECISIONS / TODO / HANDOFF
        ↓
ChatGPT reads GitHub again
        ↓
next design iteration
```

The flow is deliberately **bidirectional**. GitHub is the durable shared memory between chat sessions and interchangeable AI agents.

## Source-of-truth boundaries

- `Lesson1/` … `Lesson16/`: approved/canonical teaching content and deliverables.
- `_myplan_/`: planning state, decisions, work queue, handoff and design history.
- `_myplan_/discussions/`: dated design discussions and historical proposals; these are evidence/context, not automatically requirements.

## Required workflow

```text
DISCUSS → DECIDE → PLAN → IMPLEMENT → VERIFY → PROMOTE
```

A discussion becomes canonical course content only after the decision is recorded and the relevant `Lesson*/` files are updated and verified.

## Agent startup protocol

Any ChatGPT or coding agent continuing this project should read, in order:

1. repository root `README.md`
2. `_myplan_/README.md`
3. `_myplan_/CURRENT.md`
4. `_myplan_/DECISIONS.md`
5. `_myplan_/TODO.md`
6. `_myplan_/HANDOFF.md`
7. only the relevant files in `_myplan_/discussions/`
8. the target `Lesson*/` canonical files

Do not require prior chat history to continue the project.

## Write-back protocol

After meaningful planning or implementation:

- update `CURRENT.md` when active state changes;
- append stable decisions to `DECISIONS.md`;
- update `TODO.md` for remaining work;
- update `HANDOFF.md` with changed files, evidence, unresolved questions and next action;
- store long-form dated design material under `discussions/`;
- promote approved material to `Lesson*/` only after verification.

## Course teaching contract

Every detailed lesson/part should preserve the repository teaching pattern:

1. Concept / Why
2. Security meaning and trust boundary
3. Practical example or authorized lab
4. Antigravity YAML prompt
5. Test / evidence
6. Reflection / explanation by the student

AI-generated code is never accepted merely because it runs. Students must inspect, test, verify and security-review it.
