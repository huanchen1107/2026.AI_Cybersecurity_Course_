# AIIS_L2 — Teaching Script S01–S06
## Part A — From Vibe Coding to Spec-Driven Development

Status: DETAILED TEACHING SCRIPT IN PROGRESS — 2026-09-07

Master Curriculum Position: L2 / MANAGE

Canonical lesson statement:

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

This file expands Slides 01–06 from `_myplan_/2026-09-07-AIIS-L2-Detailed-Lecture-Plan.md` into classroom-ready teaching content. It must remain consistent with `Lesson2/README.md` and the fixed 16-lesson Master Curriculum.

---

# Slide 01 — AI Built It. What Happens Next?

## Purpose

Slide 01 is the transition from L1 BUILD to L2 MANAGE. Do not begin by teaching OpenSpec syntax, Git commands, or GitHub mechanics. First create the engineering problem: AI can build working software quickly, but ongoing AI-generated change must be controlled.

Core transition:

```text
L1 — BUILD
     ↓
L2 — MANAGE
```

Core contrast:

> **Working Software ≠ Managed Software**

This intentionally parallels L1's `WORKING ≠ SECURE` mindset.

## Slide Title

**AI Built It. What Happens Next?**

Subtitle:

> **From Vibe Coding to Spec-Driven AI Engineering**

Small Chinese subtitle:

> AI 幫我們做出來了。接下來呢？

## Visual Composition

Left side: reopen the AI Weather Security Center built in L1 and show a large:

```text
WORKING ✓
```

Right side: progressively reveal questions:

```text
What should we change?
Why are we changing it?
What should NOT change?
What did AI actually change?
How do we know it is correct?
Can we go back?
```

Bottom statement:

> **BUILDING was only the beginning.**

Do not reveal OpenSpec as the answer yet.

## Spokesperson / 煥哥 Role

Narrative role changes from L1 BUILDER to L2 **PROJECT LEAD**.

Suggested expression and pose:
- initially satisfied while looking at the working Weather Security Center;
- then notices the project files and change questions;
- expression becomes thoughtful rather than frightened;
- one hand indicates the working website, the other indicates project files / question marks.

Narrative transition:

```text
BUILDER → PROJECT LEAD
```

The character is no longer celebrating that AI can generate software. He is beginning to manage AI-generated engineering change.

## Teacher Opening Script

Suggested delivery:

> 上一次我們做了一件很有趣的事情。
>
> 我們沒有從第一行 Python 開始寫，也沒有先花幾個星期學 HTML、CSS、FastAPI。
>
> 我們先把想做的事情告訴 AI，然後透過 Antigravity，真的做出了一個 Weather Security Center。

Pause and point to the system.

> 而且它真的可以跑。

Reveal:

```text
WORKING ✓
```

Then ask:

> 所以專案完成了嗎？

Allow students to answer. Do not immediately correct students who say yes.

Then introduce the next request:

> 那如果我現在說：幫我把這個網站改善一下呢？

## Classroom Scenario

Teacher plays the user/customer:

> 我覺得這個 Weather Dashboard 不錯，但是我不知道現在看到的氣象資料是剛剛更新的，還是一個小時以前的。可以幫我改善一下嗎？

Ask:

> 現在怎麼辦？

Expected student response:

> 叫 AI 幫我們改。

This is the desired setup.

## Deliberately Dangerous Prompt

Show:

```text
USER:

Please improve my
Weather Security Center.
```

Ask:

> 可以嗎？

Do not answer immediately. Let students identify ambiguity.

## Six Questions to Reveal

### Q1 — What does “Improve” mean?

Could mean:
- UI
- functionality
- performance
- security
- refactoring

If unspecified, AI must guess.

### Q2 — What is AI allowed to change?

```text
HTML?
CSS?
Python?
API?
Database?
Dependencies?
Everything?
```

### Q3 — What must NOT change?

Example: the request is only to show data freshness, but the agent may decide to upgrade FastAPI or redesign unrelated components.

### Q4 — What counts as DONE?

If AI says `Done!`, is that enough?

### Q5 — What did AI actually change?

If the agent reports `7 files changed`, does the human know what those seven changes were and whether they were necessary?

### Q6 — What if the change breaks the project?

Can the team identify the last known-good version and return to it?

## Cognitive Conflict

Transform the visual:

```text
WORKING ✓

BUT...

CONTROL ?
HISTORY ?
EVIDENCE ?
```

Teacher message:

> L1 我們證明了一件事：AI 可以幫我們快速做出 Working Software。
>
> L2 要處理的是另一個問題：當 AI 開始不斷修改我們的 Software，我們怎麼保持控制？

## Do Not Reveal OpenSpec Yet

The pedagogical objective is for students to feel the need for controlled change before learning the tool that supports it.

Leave the class with:

```text
AI can BUILD.

But...

How do we CONTROL CHANGE?
```

## Board Notes

Write only:

```text
L1
BUILD

 ↓

L2
MANAGE
```

Then:

```text
Working Software
      ≠
Managed Software
```

## Course-Language Pattern

Use this slide to begin a repeated AIIS reasoning pattern:

```text
L1: WORKING ≠ SECURE
L2: WORKING ≠ MANAGED
L3: RUNNING ≠ UNDERSTOOD
L4: FINDING ≠ VERIFIED VULNERABILITY
```

These are conceptual distinctions, not new curriculum branches.

## Student Takeaways

Students do not need to know how OpenSpec works yet. They should leave Slide 01 understanding only:

1. AI is very capable at BUILD.
2. AI can also generate many CHANGES quickly.
3. Engineering CHANGE must be managed.

Final slide statement:

> **AI CAN BUILD. NOW WE MUST LEARN TO MANAGE CHANGE.**

## Transition to Slide 02

Teacher:

> 那 AI 到底有多會改？我們來看一個非常簡單的要求。我只跟它說一句話——

Next slide reveals:

> **“Add Last Updated.”**

Then multiple possible files begin appearing around the request.

Next slide:

**Slide 02 — One Sentence Can Change Many Files**

## Suggested Teaching Time

6–8 minutes, including at least 2–3 minutes of student responses and discussion.

This is a problem-setup slide, not a tool-operation slide.

## Slide 01 Core Lines

> **Working Software ≠ Managed Software**

> **AI CAN BUILD. NOW WE MUST LEARN TO MANAGE CHANGE.**

---

# Slide 02–06

To be expanded sequentially. Each completed slide should be synchronized into this file while preserving the canonical 30-slide storyline.
