# CURRENT — Active Project State

**Updated:** 2026-09-07

## Repository state

The repository has `Introduction/` plus canonical `Lesson1/` through `Lesson16/`. The canonical course architecture is now the focused 16-lesson plan recorded in `_myplan_/2026-09-07_AIIS_16_Lesson_Focused_Course_Plan.md`.

The stable course progression is:

`BUILD → LEARN → ATTACK → DEFEND → GOVERN → FINAL`

The Weather Security Center remains the shared project backbone whenever practical.

## Opening lesson mapping — RESOLVED 2026-09-07

The previous Lesson 1 planning conflict is resolved.

An earlier discussion in `discussions/2026-09-05-Lesson01-AI-Security-Brain-Vibe-Coding-Antigravity.md` proposed combining course introduction, AI toolbox, Secure Vibe Coding, Antigravity, Git/GitHub and an initial supervised-learning Security Brain inside Lesson 1.

That discussion remains useful as a source of teaching ideas, examples and activities, but **it is no longer the canonical Lesson 1 mapping**.

The approved mapping follows the later focused 16-lesson plan:

- **AIIS_L1 — Course Foundations / AI Security Engineer Mindset**
  - Asset → Threat → Vulnerability → Risk
  - CIA Triad
  - defensive/offensive distinction
  - authorization and ethical boundaries
  - AI as an engineering assistant
  - primary classroom activity: AI-assisted risk analysis

- **AIIS_L2 — AI Security Engineer Toolbox**
  - ChatGPT/Gemini working role
  - Antigravity
  - Git/GitHub
  - Prompt engineering
  - Secure Vibe Coding
  - `Prompt → Plan → Code → Run → Test → Review → Fix`

- **AIIS_L3 — Python FastAPI Weather Security Center**
  - common application/cyber-range project

- **AIIS_L4 — Secure Development / SAST**
  - Semgrep as the representative implementation

- **AIIS_L5–L7 — Supervised Machine Learning**
  - classification foundations
  - Decision Tree / Random Forest
  - security evaluation: confusion matrix, precision, recall and F1

Therefore, material from the older `AI Security Brain` Lesson 1 design is not deleted. Useful content should be redistributed into the appropriate focused lessons, especially L2 and L5–L7, rather than being taught all at once in L1.

### Canonical precedence rule

When older Lesson 1 planning documents conflict with the 2026-09-07 focused 16-lesson plan, **the 2026-09-07 focused 16-lesson plan takes precedence**.

Do not reopen the old combined-L1 mapping unless the course owner explicitly requests a new architecture change.

## Current course invariants

- Keep the 16-lesson focused backbone; do not continuously expand required scope.
- Prefer one core concept, one representative technology/tool and one achievable lab per lesson.
- Python/FastAPI is the preferred application architecture.
- SQLite is preferred for local/lab use; production may use managed PostgreSQL.
- Supervised ML is taught across three lessons (L5–L7).
- Deep learning remains core in L9–L10.
- LLM/RL are not separate primary course strands.
- Weather Security Center remains the shared build/attack/defend project.
- Offensive work is restricted to explicit authorized/isolated labs, teacher targets, TryHackMe/CTF or equivalent authorized ranges.
- Important legacy web-security knowledge must be preserved through migration.
- Advanced AI-assisted Secure SDLC technologies remain an advanced roadmap unless explicitly promoted into the core curriculum.

## Next recommended action

Design **AIIS_L1 — Course Foundations / AI Security Engineer Mindset** in full teaching format according to the resolved mapping:

1. learning outcomes
2. lesson parts
3. slide-by-slide content
4. teacher notes
5. student interaction
6. one focused AI-assisted risk-analysis lab
7. prompt/YAML where useful
8. evidence artifact

Then promote approved content into `Lesson1/` without importing the older combined-L1 scope.