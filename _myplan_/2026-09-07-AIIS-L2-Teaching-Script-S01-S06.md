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

## Slide Title
**AI Built It. What Happens Next?**

Subtitle:
> **From Vibe Coding to Spec-Driven AI Engineering**

Small Chinese subtitle:
> AI 幫我們做出來了。接下來呢？

## Visual Composition
Left: reopen the AI Weather Security Center built in L1 and show `WORKING ✓`.

Right: progressively reveal:
```text
What should we change?
Why are we changing it?
What should NOT change?
What did AI actually change?
How do we know it is correct?
Can we go back?
```

Bottom:
> **BUILDING was only the beginning.**

Do not reveal OpenSpec as the answer yet.

## Spokesperson / 煥哥 Role
Narrative role changes from L1 BUILDER to L2 **PROJECT LEAD**. Initially satisfied, then thoughtful while looking between the working app and project files/questions.

```text
BUILDER → PROJECT LEAD
```

## Teacher Opening Script
> 上一次我們做了一件很有趣的事情。我們沒有從第一行 Python 開始寫，也沒有先花幾個星期學 HTML、CSS、FastAPI。我們先把想做的事情告訴 AI，然後透過 Antigravity，真的做出了一個 Weather Security Center。

Pause and point to `WORKING ✓`.

> 所以專案完成了嗎？

Then introduce:
> 那如果我現在說：幫我把這個網站改善一下呢？

Teacher plays customer:
> 我覺得這個 Weather Dashboard 不錯，但是我不知道現在看到的氣象資料是剛剛更新的，還是一個小時以前的。可以幫我改善一下嗎？

Expected student response: ask AI to change it.

## Deliberately Dangerous Prompt
```text
USER:
Please improve my
Weather Security Center.
```

Ask: `可以嗎？`

Reveal six questions: What does improve mean? What may AI change? What must not change? What counts as done? What actually changed? What if it breaks?

## Cognitive Conflict
```text
WORKING ✓
BUT...
CONTROL ?
HISTORY ?
EVIDENCE ?
```

> L1 我們證明 AI 可以快速做出 Working Software。L2 要處理的是：當 AI 開始不斷修改 Software，我們怎麼保持控制？

Do not reveal OpenSpec yet.

## Board Notes
```text
L1 BUILD
   ↓
L2 MANAGE
```

```text
Working Software ≠ Managed Software
```

## Course-Language Pattern
```text
L1: WORKING ≠ SECURE
L2: WORKING ≠ MANAGED
L3: RUNNING ≠ UNDERSTOOD
L4: FINDING ≠ VERIFIED VULNERABILITY
```

## Student Takeaways
1. AI is capable at BUILD.
2. AI can generate many CHANGES quickly.
3. Engineering CHANGE must be managed.

> **AI CAN BUILD. NOW WE MUST LEARN TO MANAGE CHANGE.**

## Transition to Slide 02
> 那 AI 到底有多會改？我們來看一個非常簡單的要求。我只跟它說一句話——

Reveal: **“Add Last Updated.”**

Suggested teaching time: 6–8 minutes.

---

# Slide 02 — One Sentence Can Change Many Files

## Purpose

Slide 02 makes the change-management problem concrete. A request that sounds tiny to a human can propagate through several layers of a software system. Students should stop thinking `one sentence = one line of code` and begin thinking `one request = a change with scope and consequences`.

Do NOT teach OpenSpec yet. The objective is to make students feel why a durable change definition is needed.

Core idea:

> **A SMALL REQUEST CAN CREATE A LARGE CHANGE SURFACE.**

## Slide Title

**One Sentence Can Change Many Files**

Chinese subtitle:

> 一句需求，可能牽動整個專案

Center request:

> **“Add Last Updated.”**

## Visual Composition

Start with only the user request in the center. Then progressively reveal possible project areas around it:

```text
                    USER REQUEST
                "Add Last Updated"
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      FRONTEND        BACKEND          DATA
     index.html        main.py      timestamp/data
          │              │              │
          └───────┬──────┴──────┬───────┘
                  ↓             ↓
               STYLE       DEPENDENCIES?
              style.css    requirements?
```

The question mark on dependencies is important. It shows that some changes may be unnecessary rather than automatically required.

## Spokesperson / 煥哥 Role

Role: **CHANGE OBSERVER**.

Pose:
- holds a small request card reading `Add Last Updated`;
- looks surprised as several file cards expand behind it;
- expression should communicate discovery, not panic.

Narrative:

```text
SMALL REQUEST
     ↓
CHANGE SURFACE
```

## Teacher Script — Start Small

Teacher:

> 剛才使用者其實沒有要求我們重新設計網站。他只提出一個很小的需求。

Reveal:

```text
Add Last Updated.
```

Ask students:

> 你覺得這一句話要改幾行程式？

Let students guess: one line, a few lines, one file, etc.

Then say:

> 我們先不要猜答案。我們先想：Last Updated 這個資訊到底從哪裡來？最後又要顯示在哪裡？

## Follow the Possible Change Path

Build the reasoning gradually.

### 1. UI / Frontend

> 使用者最後要在 Dashboard 上看到 Last Updated，所以畫面可能要改。

Reveal:

```text
index.html
```

Ask:

> 只改 HTML 就一定夠嗎？

Do not answer immediately.

### 2. Styling

If the timestamp needs visual placement or formatting, perhaps:

```text
style.css
```

But emphasize:

> **可能需要，不代表一定要改。**

This is the first seed of minimal-change thinking.

### 3. Backend

Ask:

> HTML 要顯示時間，那時間從哪裡拿？

Possible answer:

```text
main.py
```

Maybe the backend already has the timestamp; maybe it does not. We must inspect first.

### 4. Data

Ask:

> CWA 回來的資料本來有沒有時間資訊？我們自己的程式是不是已經保存或處理了？

Reveal:

```text
existing timestamp?
weather data?
```

Key teacher statement:

> 如果資料本來就存在，我們應該優先 reuse，而不是自己再創造一套新的時間機制。

### 5. Dependencies

Now deliberately reveal:

```text
requirements.txt ?
```

Ask:

> 顯示一個時間，需要新增 Python 套件嗎？

Students may say no.

Teacher:

> 很可能不需要。但如果我們只說「幫我做」，AI 有時可能會選擇一個比需求更大的解法。

This foreshadows scope creep without yet teaching the term formally.

## Important Distinction — Possible vs Necessary

Show two columns:

```text
POSSIBLE TO CHANGE        NECESSARY TO CHANGE
------------------        -------------------
index.html                ?
style.css                 ?
main.py                   ?
helper.py                 ?
requirements.txt          ?
```

Teacher:

> 工程不是問「哪些檔案可以改」，而是問「為了完成這個需求，哪些改動真的有必要」。

Core line:

> **CAN CHANGE ≠ SHOULD CHANGE**

This is one of the most important concepts on Slide 02.

## Mini Classroom Exercise — Predict the Change Surface

Before showing any AI output, ask pairs/groups to predict:

> 如果是你，你認為 `Add Last Updated` 最少可能需要碰哪些地方？

Students write 1–3 predicted files/components.

Then ask:

> 你為什麼認為需要改它？

The goal is not to get the exact repository answer. The goal is to connect every proposed modification to a reason.

Simple worksheet:

```text
Component / File       Why might it change?
----------------       --------------------
______________         ____________________
______________         ____________________
______________         ____________________
```

## Deliberately Bad AI Response

Show a fictional response:

```text
Sure! I improved the project.

Changed:
- index.html
- style.css
- main.py
- weather_service.py
- config.py
- requirements.txt
- README.md

Also upgraded dependencies
and refactored the weather service.
```

Ask:

> 好不好？

Some students may initially interpret more changes as more work/value.

Then ask:

> 我們原本要求 Upgrade dependencies 嗎？
> 我們要求 Refactor weather service 嗎？
> README 一定需要改嗎？

Teacher conclusion:

> **More changes ≠ Better engineering.**

## Introduce the Idea of Change Surface

Use an accessible definition:

> **Change Surface = 一個需求可能影響到的程式、資料、設定與行為範圍。**

Do not turn this into formal software architecture theory. Students only need the mental model.

Visual:

```text
REQUEST
  ↓
CHANGE SURFACE
  ↓
FILES + DATA + BEHAVIOR + DEPENDENCIES
```

## Security Foreshadowing

Briefly connect to security without taking over L4:

> 改動範圍越大，需要重新確認的地方通常也越多。

Example:

```text
1 necessary file changed
vs
12 unrelated files changed
```

Ask:

> 哪一個比較容易 Review？哪一個比較容易不小心帶入問題？

Do not scan vulnerabilities here. L4 owns security scanning and verified remediation.

## Board Notes

Write:

```text
1 REQUEST
   ↓
? FILES
   ↓
? SIDE EFFECTS
```

Then:

```text
CAN CHANGE ≠ SHOULD CHANGE
```

Finally:

```text
More changes ≠ Better engineering
```

## Student Takeaways

Students should leave Slide 02 able to explain:

1. A small natural-language request can affect multiple software layers.
2. Possible changes are not automatically necessary changes.
3. Every modification should have a reason tied to the request.
4. Large unnecessary change surfaces make review and verification harder.

Core lines:

> **A SMALL REQUEST CAN CREATE A LARGE CHANGE SURFACE.**

> **CAN CHANGE ≠ SHOULD CHANGE.**

> **MORE CHANGES ≠ BETTER ENGINEERING.**

## Transition to Slide 03

Teacher:

> 所以問題已經不是 AI 會不會寫程式。AI 當然會寫。
>
> 真正的問題是：如果我們一直用一句一句的 Prompt 叫 AI 改，而且每一次都讓它自己決定範圍，專案久了會發生什麼事？

Reveal next title:

**Slide 03 — The Vibe Coding Problem**

Transition question:

> **Vibe Coding 很適合開始一個專案，但它本身夠不夠管理一個持續成長的專案？**

## Suggested Teaching Time

7–10 minutes including the change-surface prediction exercise.

---

# Slide 03–06

To be expanded sequentially. Each completed slide should be synchronized into this file while preserving the canonical 30-slide storyline.
