# AIIS_L2 — Teaching Script S01–S06
## Part A — From Vibe Coding to Spec-Driven Development

Status: PART A TEACHING SCRIPT COMPLETE — 2026-09-07
Master Curriculum Position: L2 / MANAGE

Canonical lesson statement:
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

This file expands Slides 01–06 from `_myplan_/2026-09-07-AIIS-L2-Detailed-Lecture-Plan.md` into classroom-ready teaching content. It must remain consistent with `Lesson2/README.md` and the fixed 16-lesson Master Curriculum.

---

# Slide 01 — AI Built It. What Happens Next?

## Purpose
Transition from L1 BUILD to L2 MANAGE. Create the problem before teaching tools.

```text
L1 — BUILD
     ↓
L2 — MANAGE
```

> **Working Software ≠ Managed Software**

## Visual
Left: L1 Weather Security Center with `WORKING ✓`.
Right: What should change? Why? What should NOT change? What did AI actually change? How do we know it is correct? Can we go back?

Bottom: **BUILDING was only the beginning.**

## 煥哥
Role changes `BUILDER → PROJECT LEAD`. Satisfied with working app, then thoughtful while looking at project files and questions.

## Teacher Script
Reopen L1 project. Ask whether a working system means the project is finished. Introduce customer request: users cannot tell whether weather data is fresh. Students will likely answer: ask AI to improve it.

Show deliberately ambiguous prompt:
```text
Please improve my Weather Security Center.
```

Ask what `improve` means, what AI may change, what it must not change, what DONE means, what actually changed, and what happens if it breaks.

Reveal:
```text
WORKING ✓
BUT...
CONTROL ?
HISTORY ?
EVIDENCE ?
```

Board:
```text
Working Software ≠ Managed Software
```

Course pattern:
```text
L1: WORKING ≠ SECURE
L2: WORKING ≠ MANAGED
L3: RUNNING ≠ UNDERSTOOD
L4: FINDING ≠ VERIFIED VULNERABILITY
```

Takeaway:
> **AI CAN BUILD. NOW WE MUST LEARN TO MANAGE CHANGE.**

Transition: “Add Last Updated.”

Suggested time: 6–8 min.

---

# Slide 02 — One Sentence Can Change Many Files

## Purpose
Make the change-management problem concrete. Students stop thinking `one sentence = one line` and start thinking `one request = change surface + consequences`.

> **A SMALL REQUEST CAN CREATE A LARGE CHANGE SURFACE.**

## Visual
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

## 煥哥
Role: **CHANGE OBSERVER**. Holds a tiny request card while multiple file cards expand behind it.

## Teacher Script
Ask students how many lines/files `Add Last Updated` should require. Follow the possible path from UI → backend → existing timestamp/data → styling → dependencies. Stress that `possible` does not mean `necessary`.

```text
CAN CHANGE ≠ SHOULD CHANGE
```

Mini exercise: students predict 1–3 components that may need modification and explain WHY for each.

Show deliberately overactive AI response: changes HTML/CSS/backend/config/requirements/README, upgrades dependencies, refactors service. Ask which actions were actually requested.

> **MORE CHANGES ≠ BETTER ENGINEERING.**

Accessible definition:
> **Change Surface = 一個需求可能影響到的程式、資料、設定與行為範圍。**

```text
REQUEST → CHANGE SURFACE → FILES + DATA + BEHAVIOR + DEPENDENCIES
```

Security foreshadowing only: larger unnecessary changes create more things to review and verify. Do not perform scanning here.

Transition: If we repeatedly use short prompts and let AI decide scope every time, what happens as the project grows?

Suggested time: 7–10 min.

---

# Slide 03 — The Vibe Coding Problem

## Purpose
Do not attack or dismiss Vibe Coding. Students used it successfully in L1. Clarify its strength and its boundary: it is excellent for rapidly turning intent into working software, but a growing project also needs durable engineering control.

Core distinction:

> **VIBE CODING IS GREAT FOR STARTING. ENGINEERING IS NEEDED FOR CONTINUING.**

## Slide Title
**The Vibe Coding Problem**

Chinese subtitle:
> 快速做出來之後，怎麼持續做對？

## Visual Composition
Left side — rapid creation:
```text
IDEA
 ↓
PROMPT
 ↓
AI
 ↓
CODE
 ↓
RUN
 ↓
WORKING ✓
```

Right side — after many iterations:
```text
Prompt #1
Prompt #2
Prompt #3
Prompt #4
Prompt #5
   ↓
Which decision is current?
Why did we change this?
What was out of scope?
What is DONE?
```

Center bridge:
```text
FAST CREATION → CONTROLLED EVOLUTION
```

## 煥哥 Role
Role: **VIBE CODER → ENGINEERING LEAD**.

Left pose: energetic, rapidly creating with AI.
Right pose: reviewing accumulated change cards and project history with a more deliberate expression.

## Teacher Script
Start positively:

> L1 的 Vibe Coding 有沒有用？當然有用。沒有它，我們可能還在設定環境，Weather Security Center 已經被 AI 幫我們做出來了。

Then ask:

> 如果今天只做一次 Demo，做到能跑可能就很有價值。但如果這個專案要活 16 週，而且每一週都繼續加功能、改程式、做安全修正呢？

Build a sequence:
```text
Week 1: Build dashboard
Week 2: Add Last Updated
Week 3: Change API behavior
Week 4: Security fix
Week 5: Add ML feature
...
```

Ask:
> 到第十次修改時，你還記得第二次修改時跟 AI 說了什麼嗎？

Key problem: chat history is conversational context, not a durable engineering contract.

## What Vibe Coding Is Good At
Show:
- idea exploration
- prototype
- quick UI
- small experiments
- learning by building
- fast feedback

Teacher:
> 我們不丟掉 Vibe Coding。我們要把它放在正確的位置。

## What a Growing Project Adds
Reveal:
```text
INTENT
SCOPE
CONSTRAINTS
DONE
EVIDENCE
HISTORY
```

Explain each with one sentence, without naming OpenSpec yet.

- Intent: why are we changing?
- Scope: what belongs in this change?
- Constraints: what must not be touched?
- Done: how do we judge completion?
- Evidence: what proves it?
- History: where is the durable record?

## Chat Is Not the Project Memory
Show:
```text
CHAT
"Can you change this?"
"Sure."
"Also make it nicer."
"Done."
```
versus
```text
PROJECT MEMORY
Change A — requirement
Change B — reason
Change C — acceptance
```

Teacher:
> 對話可以幫助思考，但重要工程決策不能只存在某一次聊天裡。

## Board Notes
```text
VIBE CODING
FAST START ✓
```
then
```text
GROWING PROJECT
needs CONTROL + MEMORY + EVIDENCE
```

## Student Takeaways
1. Vibe Coding remains useful.
2. Repeated AI changes create coordination and memory problems.
3. A persistent project needs explicit scope, completion criteria, evidence and history.

Core lines:
> **VIBE CODING GETS US STARTED. ENGINEERING KEEPS US UNDER CONTROL.**

> **CHAT HISTORY ≠ ENGINEERING CONTRACT.**

## Transition to Slide 04
Teacher:
> 如果一句 Prompt 不夠承擔長期工程決策，那我們需要把「我要 AI 做什麼」提升成什麼？

Reveal:
**Slide 04 — Prompt vs Spec**

Suggested time: 7–9 min.

---

# Slide 04 — Prompt vs Spec

## Purpose
Introduce `Spec` conceptually before introducing OpenSpec as the concrete method. Students must understand the difference between conversational instruction and durable engineering definition.

Core:
> **A PROMPT ASKS. A SPEC DEFINES.**

## Visual Composition
Two-column comparison.

```text
PROMPT                         SPEC
------                         ----
"Add Last Updated"            WHY
                               SCOPE
                               OUT OF SCOPE
                               REQUIREMENTS
                               CONSTRAINTS
                               ACCEPTANCE CRITERIA
```

Bottom:
```text
REQUEST → SPEC → IMPLEMENTATION
```

## 煥哥 Role
Role: **SPEC THINKER**. Holds a short Prompt card in one hand and a structured Spec board in the other, showing the transformation from vague request to explicit engineering agreement.

## Teacher Script
Teacher shows:
```text
Add Last Updated.
```

Ask:
> 這句話有錯嗎？

Answer: No. It communicates intent, but leaves important engineering questions unanswered.

Then build the Spec side progressively.

### WHY
Why does the user need this?
> Users need to judge weather-data freshness.

### SCOPE
What is included?
> Display Last Updated near weather information.

### OUT OF SCOPE
What is explicitly excluded?
> No auth change, DB redesign, API redesign, dependency upgrade, unrelated refactor.

### REQUIREMENTS
What behavior should exist?
> Dashboard shall display a readable update time.

### ACCEPTANCE CRITERIA
How do we decide PASS/FAIL?
> Last Updated visible; weather still works; existing API behavior preserved; no unnecessary dependency.

## Engineering Contract Metaphor
Use accessible language:

> **Spec = Human ↔ AI 的 Engineering Contract.**

Clarify: not a legal contract; it is a shared durable definition of the intended change.

```text
HUMAN INTENT
     ↓
   SPEC
     ↓
AI IMPLEMENTATION
```

The AI is not supposed to invent the definition of DONE after coding.

## Prompt and Spec Are Not Enemies
Important nuance:

```text
PROMPT
= interaction / instruction

SPEC
= durable definition / contract
```

We still use prompts to tell the agent to inspect, plan, implement and verify. The Spec is what those prompts should refer to.

Example:
```text
Weak:
"Add Last Updated."

Better interaction:
"Read the add-weather-last-updated spec.
Inspect the repository and propose a plan.
Do not modify files yet."
```

## Mini Exercise
Give students three statements and ask Prompt or Spec element:

1. `Please make the dashboard better.` → Prompt / vague request
2. `Do not change authentication.` → Scope constraint / Out of Scope
3. `Dashboard visibly shows Last Updated.` → Acceptance Criterion

## Board Notes
```text
PROMPT = ASK
SPEC   = DEFINE
```

```text
WHY → WHAT → DONE
```

## Student Takeaways
1. Prompt and Spec serve different roles.
2. Spec makes intent, boundaries and DONE durable.
3. AI implementation should be evaluated against the Spec.

Core lines:
> **A PROMPT ASKS. A SPEC DEFINES.**

> **AI SHOULD NOT INVENT DONE.**

## Transition to Slide 05
Teacher:
> 好，那 Spec 要放在哪裡？我們是不是每次自己隨便建立一個文字檔？我們需要一個可重複的方式，把 Change 變成專案裡正式的工程物件。

Reveal:
**Slide 05 — Meet OpenSpec**

Suggested time: 8–10 min.

---

# Slide 05 — Meet OpenSpec

## Purpose
Formally introduce OpenSpec as the course's method for Spec-Driven Development. Do not turn the slide into OpenSpec syntax training. Students first learn what problem it solves and where it lives in the workflow.

Core:
> **IMPORTANT REQUIREMENTS SHOULD NOT LIVE ONLY IN CHAT HISTORY.**

## Slide Title
**Meet OpenSpec**

Subtitle:
> From Request to Durable Change

## Visual Composition
```text
USER REQUEST
     ↓
┌──────────────────────┐
│   OPENSPEC CHANGE    │
│                      │
│ WHY                  │
│ SCOPE                │
│ OUT OF SCOPE         │
│ REQUIREMENTS         │
│ ACCEPTANCE CRITERIA  │
└──────────┬───────────┘
           ↓
      AI ENGINEERING
```

Place the Change inside the project/repository visually, not floating in chat.

## 煥哥 Role
Role: **CHANGE OWNER**. Places a request card into a labeled OpenSpec Change folder, signaling that a transient request becomes a durable engineering object.

## Teacher Script
> 我們現在需要的不是更多 Prompt 技巧，而是一個方法，把重要需求從聊天搬進專案。

Introduce name:
> 這一課我們使用 **OpenSpec** 來做 Spec-Driven Development。

Do not imply OpenSpec is the only possible specification methodology in industry. State:
> 在 AIIS，我們選 OpenSpec 作為代表性的實作方法，讓整班使用同一套 Change Workflow。

## What OpenSpec Does in AIIS
OpenSpec gives each meaningful change a durable identity.

Example:
```text
add-weather-last-updated
```

Inside it we can preserve:
```text
WHY
SCOPE
OUT OF SCOPE
REQUIREMENTS
ACCEPTANCE CRITERIA
```

Teacher:
> 這樣下星期、下個月，甚至換另一個 AI Agent，我們仍然可以先讀這個 Change，而不是問「你還記不記得上次聊天？」

## Change as Unit of Work
Preview a key idea that Part B will teach deeply:

```text
REQUEST
   ↓
CHANGE
   ↓
IMPLEMENTATION
   ↓
EVIDENCE
```

> **Change = 一個可以被定義、實作、驗證、保存的工程工作單位。**

Do not yet dive into folder/file syntax; S07–S12 own the first actual OpenSpec Change.

## Why This Matters for AI Agents
Show two situations:

```text
Agent A only sees:
"Add Last Updated"
```

versus
```text
Agent B sees:
Existing Repository
+ OpenSpec Change
+ Scope
+ Constraints
+ Acceptance Criteria
```

Ask:
> 哪一個 Agent 比較有機會做出我們真正要的 Change？

Important nuance:
> Spec reduces ambiguity; it does not guarantee correctness. Verification is still required.

## Semester Reuse Preview
Briefly show only:
```text
L2 Feature Change
L4 Security Fix
L13 Verified Security Repair
L15–16 Final Evidence
```

All can use the same pattern:
```text
CHANGE → IMPLEMENT → VERIFY → EVIDENCE
```

Do not expand into later lessons.

## Board Notes
```text
CHAT → temporary conversation
SPEC → durable project context
```

```text
OpenSpec = DEFINE THE CHANGE
```

## Student Takeaways
1. OpenSpec is the selected AIIS method for durable specification/change definition.
2. Important requirements should live with the project, not only in chat.
3. A Spec reduces ambiguity but does not eliminate the need for verification.

Core lines:
> **REQUIREMENTS MUST NOT LIVE ONLY IN CHAT HISTORY.**

> **OPENSPEC TURNS A REQUEST INTO A DURABLE CHANGE.**

## Transition to Slide 06
Teacher:
> OpenSpec 負責把 Change 定義清楚，但它不是整個流程。誰負責實作？誰負責判斷正不正確？誰保存歷史？

Reveal:
**Slide 06 — Four Layers of AI Engineering**

Suggested time: 7–9 min.

---

# Slide 06 — Four Layers of AI Engineering

## Purpose
Close Part A by giving students the complete L2 mental model. From this point onward, every activity should be placed into one of four layers: DEFINE, BUILD, VERIFY, REMEMBER.

This is the anchor slide for the whole lesson.

## Slide Title
**Four Layers of AI Engineering**

Chinese subtitle:
> 四層 AI 工程控制模型

## Main Visual
```text
┌──────────────────────────────────────┐
│ ① DEFINE                            │
│ OpenSpec                            │
│ What? Why? Scope? What is DONE?     │
└─────────────────┬────────────────────┘
                  ↓
┌──────────────────────────────────────┐
│ ② BUILD                             │
│ Antigravity                         │
│ Inspect → Plan → Implement          │
└─────────────────┬────────────────────┘
                  ↓
┌──────────────────────────────────────┐
│ ③ VERIFY                            │
│ Diff + Test + AC + Human Review     │
│ Did AI do what we asked?            │
└─────────────────┬────────────────────┘
                  ↓
┌──────────────────────────────────────┐
│ ④ REMEMBER                          │
│ Git + GitHub                        │
│ History + Evidence                  │
└──────────────────────────────────────┘
```

Alternative shorthand:
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

## Tool / Responsibility Mapping
| Layer | Representative method/tool | Question |
|---|---|---|
| DEFINE | OpenSpec | 要改什麼？為什麼？完成標準是什麼？ |
| BUILD | Antigravity | AI 如何依 Spec 實作？ |
| VERIFY | Diff + Test + AC + Human Review | AI 做的是不是我們要求的？ |
| REMEMBER | Git + GitHub | 如何保存變更、證據與歷史？ |

## 煥哥 Role
Role: **AI ENGINEERING LEAD**. Stands beside a four-stage control board. Calm and confident; no longer surprised by change because the workflow now gives structure.

## Teacher Script
> 前面五頁其實都在問同一件事：AI 很會做，那人怎麼保持工程控制？

Reveal one layer at a time.

### DEFINE
> 在 AI 開始修改之前，先定義 Change。OpenSpec 回答 What、Why、Scope、Done。

### BUILD
> 定義完成後才讓 Antigravity 讀 Project + Spec。它不是立刻亂改，而是 Inspect、Plan、Implement。

### VERIFY
> AI 說 Done 不算 Done。我們看 Changed Files、Diff、Run/Test，再逐項檢查 Acceptance Criteria，最後由人決定 Accept、Revise 或 Reject。

### REMEMBER
> 驗證過的 Change 才值得保存。Git 建立版本歷史，GitHub 讓專案、變更與證據成為可以持續查看的工程記憶。

## The Canonical L2 Statement
Build sentence in four beats:

```text
SPEC DEFINES.
AI IMPLEMENTS.
HUMAN VERIFIES.
GIT REMEMBERS.
```

Have the class read it once together if appropriate.

## Important: Tools Are Not the Lesson
Teacher:
> 今天不是四套工具教學。我們學的是一條工程 Workflow。工具未來可能換，但四個責任不會因為工具名稱改變就消失。

This prevents tool-centric fragmentation.

## Human Role
Overlay a human line across all four layers:

```text
HUMAN
Understand → Decide → Review → Accept
```

AI is powerful in BUILD and can assist in all layers, but responsibility for intended change and acceptance remains human-centered in this course.

## Quick Classification Exercise
Teacher reads an action; students answer layer:

- `Write acceptance criteria` → DEFINE
- `Ask Antigravity to inspect repo` → BUILD
- `Read git diff` → VERIFY
- `Run the app` → VERIFY
- `Commit accepted change` → REMEMBER
- `Push to GitHub` → REMEMBER

## Board Notes
Large:
```text
DEFINE → BUILD → VERIFY → REMEMBER
```

Under it:
```text
OpenSpec → Antigravity → Evidence/Human → Git/GitHub
```

Then the canonical statement.

## Student Takeaways
Students should now be able to explain the whole L2 architecture before touching the actual lab:

1. DEFINE prevents vague change.
2. BUILD turns an approved definition into implementation.
3. VERIFY compares reality against the definition.
4. REMEMBER preserves accepted engineering history.

Core:
> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

## Transition to Part B / Slide 07
Teacher:
> 現在我們有地圖了。接下來不要再談抽象概念。我們真的拿剛才那一句 `Add Last Updated`，建立 AIIS 的第一個 OpenSpec Change。

Reveal:
```text
add-weather-last-updated
```

Next:
**Slide 07 — A Real Request Arrives**

Suggested time: 8–10 min.

---

# Part A Completion Check

Slides 01–06 now establish the complete conceptual progression:

```text
S01 Working ≠ Managed
 ↓
S02 Small request → Change Surface
 ↓
S03 Vibe Coding → need controlled evolution
 ↓
S04 Prompt ≠ Spec
 ↓
S05 OpenSpec → durable Change
 ↓
S06 DEFINE → BUILD → VERIFY → REMEMBER
```

Part B should now move immediately into the real `add-weather-last-updated` OpenSpec Change rather than adding more conceptual tools.
