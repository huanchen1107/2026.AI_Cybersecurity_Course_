# _myplan_ — ChatGPT ↔ GitHub ↔ Antigravity Bidirectional Planning Layer

`_myplan_` is the persistent planning, synchronization, governance, and handoff layer for this course repository. It is not merely a notes folder and it is not the canonical teaching-content directory.

The design follows the same core principle used in the AI Company project: **a new ChatGPT session or a replacement coding agent must be able to recover the project from GitHub without depending on hidden conversation history.**

> GitHub is durable shared memory. ChatGPT is the interactive planning/design layer. Antigravity and other coding agents are interchangeable workers. Every meaningful change must flow back to GitHub.

## 1. Mandatory bidirectional model

```text
Human ↔ ChatGPT
       │
       │ discuss / clarify / design
       ▼
_myplan_/discussions/
       │
       ├── accepted decision ──────► DECISIONS.md
       ├── active state ───────────► CURRENT.md
       └── pending work ───────────► TODO.md
                                      │
                                      ▼
                              GitHub persistent state
                                      │
                 ┌────────────────────┴────────────────────┐
                 ▼                                         ▼
            Antigravity                              Other agents
                                               Codex / Gemini / Claude
                 │                                         │
                 └──────── implement / test / review ──────┘
                                      │
                                      ▼
                         code + tests + Git evidence
                                      │
                                      ▼
                              HANDOFF.md / feedback
                                      │
                                      ▼
                          ChatGPT MUST read GitHub again
                                      │
                                      ▼
                              next design iteration
```

This is a **closed synchronization loop**, not a one-way ChatGPT → GitHub export.

## 2. Source-of-truth ladder

Use the following authority order when sources disagree:

1. repository/root permanent policies and `AGENTS.md` when present;
2. approved architecture / course contracts in root `README.md`;
3. canonical `Lesson1/` … `Lesson16/` teaching content;
4. accepted decisions in `_myplan_/DECISIONS.md`;
5. active planning state in `CURRENT.md`, `TODO.md`, and `HANDOFF.md`;
6. dated `_myplan_/discussions/` as supporting design evidence/history;
7. prior chat memory only as temporary context.

A dated discussion is **not automatically an active requirement**. If a newer accepted decision supersedes it, keep the old discussion for provenance and record the superseding decision instead of silently rewriting history.

## 3. Required agent startup / recovery protocol

Every ChatGPT session, Antigravity worker, Codex, Gemini, Claude, or replacement agent that performs meaningful work MUST recover repository state before planning or editing.

Read in this order:

1. root `README.md`;
2. `AGENTS.md` if present;
3. `_myplan_/README.md` — this synchronization contract;
4. `_myplan_/CURRENT.md` — what is active now;
5. `_myplan_/DECISIONS.md` — decisions that must be preserved;
6. `_myplan_/TODO.md` — remaining work;
7. `_myplan_/HANDOFF.md` — previous worker's evidence and continuation point;
8. relevant files under `_myplan_/discussions/` only as needed;
9. target `Lesson*/` files and relevant source/tests.

Then inspect recent Git history / working changes when available before assuming the previous worker's state.

**Never require the human to reconstruct an earlier ChatGPT conversation if GitHub can answer the question. Never continue from remembered chat state without checking GitHub when repository state may have changed.**

## 4. ChatGPT → GitHub synchronization rule

When ChatGPT and the human reach a meaningful design result, ChatGPT should persist it to GitHub rather than leaving the result only in conversation.

Use this mapping:

```text
Long design discussion / alternatives
    → _myplan_/discussions/YYYY-MM-DD-*.md

Accepted durable decision
    → _myplan_/DECISIONS.md

Current project/lesson status
    → _myplan_/CURRENT.md

Remaining or newly discovered work
    → _myplan_/TODO.md

Work delegated to / returned from another agent
    → _myplan_/HANDOFF.md

Approved + verified teaching material
    → Lesson1/ ... Lesson16/
```

ChatGPT must not silently promote a discussion into canonical lesson content. Follow:

```text
DISCUSS → DECIDE → PLAN → IMPLEMENT → VERIFY → PROMOTE
```

## 5. GitHub / Agent → ChatGPT synchronization rule

Antigravity or any implementation agent MUST write back enough repository evidence for a later ChatGPT session to understand what actually happened.

After meaningful work, update the appropriate planning files and include at least:

```yaml
status: completed | partial | blocked
work_item: short identifier or lesson/part
changed_files:
  - path/to/file
verified_by:
  - tests / manual check / review
evidence:
  commit: <sha-if-available>
  tests: <result>
discoveries:
  - implementation facts that affect planning
decisions_needed:
  - unresolved choices
next_action:
  - exact continuation step
```

Implementation discoveries that change assumptions must flow back into planning. **Do not silently change architecture, lesson scope, security boundaries, or curriculum contracts only in code.** Record the finding in `HANDOFF.md`; update `CURRENT.md` / `TODO.md`; and add or supersede a decision in `DECISIONS.md` after approval.

## 6. Session close / handoff protocol

Before an agent stops because a task is complete, context is ending, token quota is exhausted, or another model will take over, it MUST leave the repository resumable.

Minimum handoff:

1. save meaningful work;
2. record changed files;
3. record tests/evidence and failures;
4. state what is complete vs incomplete;
5. state unresolved questions/risks;
6. give one precise `next_action`;
7. commit/push when the agent has permission and the work is ready.

The goal is:

> **Repository state must be sufficient for a replacement worker to continue an interrupted task.**

## 7. No silent rewrite / provenance rule

Preserve design history.

If a decision changes:

```text
old discussion / decision
        ↓
new evidence or requirement
        ↓
new dated discussion
        ↓
DECISIONS.md: supersedes <old decision>
```

Do not erase the reasoning that produced the old design merely to make history look clean. Git history plus dated discussions provide provenance.

## 8. Canonical teaching-content boundary

- `Lesson1/` … `Lesson16/` = approved/canonical teaching content and deliverables.
- `_myplan_/` = planning/governance/synchronization state.
- `_myplan_/discussions/` = dated design evidence and proposals.

Therefore:

```text
_myplan_ decides and coordinates
        ↓
Lesson*/ implements the approved curriculum
        ↓
verification confirms it
        ↓
HANDOFF/CURRENT report the result back
```

## 9. Course teaching contract

Every detailed lesson/part should preserve this pattern:

1. Concept / Why
2. Security meaning and trust boundary
3. Practical example or authorized lab
4. Antigravity YAML prompt
5. Test / evidence
6. Reflection / explanation by the student

AI-generated code is never accepted merely because it runs. Students must inspect, test, verify, and security-review it.

## 10. Mandatory synchronization summary for agents

Before work:

> **READ GitHub → recover CURRENT + DECISIONS + TODO + HANDOFF → inspect target canonical files.**

During work:

> **Do not guess; preserve contracts; record discoveries that change the plan.**

After work:

> **WRITE BACK GitHub → code/evidence + CURRENT/TODO/HANDOFF (+ DECISIONS when approved).**

For the next ChatGPT session:

> **READ BACK GitHub before continuing the conversation-derived plan.**

This README is a mandatory collaboration contract for this repository, not optional documentation.
