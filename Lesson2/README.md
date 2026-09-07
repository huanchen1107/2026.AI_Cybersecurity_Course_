# AIIS_L2 — MANAGE：Antigravity × Git × GitHub Engineering Workflow

> **Status: CANONICAL ALLOCATION — 2026-09-07**
>
> Earlier versions placed the full Python/FastAPI Weather App build in Lesson 2. That allocation is superseded. The app is first created in **L1**; L2 teaches students how to manage AI-generated software as an engineering project. Python/API internals move to **L3** and formal security scanning/remediation to **L4**.

## Mission

核心問題：

> AI 已經幫你做出程式，但你知道它改了什麼嗎？你能保存、追蹤、比較與恢復嗎？

L2 使用 L1 的同一個 AI Weather Security Center，不重新建立另一個 Lab。

## Core Flow

```text
OPEN EXISTING PROJECT
        ↓
ASK AI FOR ONE CONTROLLED CHANGE
        ↓
INSPECT FILES CHANGED
        ↓
DIFF — WHAT CHANGED?
        ↓
HUMAN REVIEW
        ↓
GIT — SAVE A CHECKPOINT
        ↓
COMMIT — NAME THE CHANGE
        ↓
GITHUB — SYNC ENGINEERING MEMORY
        ↓
HISTORY — TRACE WHAT HAPPENED
```

## Primary Topics

1. Antigravity project / workspace mental model
2. Existing Weather Security Center as project context
3. Prompt / task / artifact distinction
4. AI reads and modifies project files
5. File tree and project structure at a practical level
6. Controlled small feature change
7. Inspect changed files before accepting
8. Git repository / working tree concept
9. `status` and `diff` as evidence of change
10. Commit as a named engineering checkpoint
11. Meaningful commit messages
12. GitHub as remote/shared engineering memory
13. Push / sync concept
14. Commit history and traceability
15. Recovery / rollback concept
16. AI-assisted Git workflow with human approval

## Required Lab

Students reopen the L1 Weather Security Center and make one small, safe, instructor-defined change, for example:
- change dashboard title/content,
- add a simple last-updated display,
- add one presentation-level weather field,
- make a small UI improvement.

They must then:

```text
AI proposes change
→ inspect changed files
→ inspect diff
→ run the application / relevant check
→ human approves
→ commit
→ sync to GitHub
→ inspect history
```

The task should not require deep Python understanding; that belongs to L3.

## Evidence

Student evidence should include:
- requested change
- AI plan/summary
- files changed
- diff reviewed
- test/run evidence
- human decision
- commit message
- commit/history evidence

## Responsibility Boundary

L2 does **not** own:
- detailed Python syntax → L3
- FastAPI / HTTP / API / JSON internals → L3
- Semgrep scanning and remediation → L4
- Kali / TryHackMe Red Team → L11–L12

## Core Statement

> **AI CHANGES. GIT REMEMBERS. HUMAN DECIDES.**

Handoff to L3:

> Now that we can manage the code, we learn what the code actually means.