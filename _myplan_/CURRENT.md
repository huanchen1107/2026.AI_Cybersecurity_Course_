# CURRENT — Active Project State

**Updated:** 2026-09-05

## Repository state

The repository currently has `Introduction/` plus canonical `Lesson1/` through `Lesson16/`. The root README currently maps Lesson 1 to course introduction, Lesson 2 to the AI Security Engineer Toolbox, Lesson 3 to the Python/FastAPI Weather Security Center, Lessons 5–7 to three supervised-ML sessions, Lessons 11–12 to authorized AI Red Team work, Lesson 13 to Blue Team, and Lesson 14 to governance.

## Active design focus

The current ChatGPT design discussion is refining the opening of the course. A new proposal in `discussions/2026-09-05-Lesson01-AI-Security-Brain-Vibe-Coding-Antigravity.md` proposes that Lesson 1 itself introduce:

- AI as TOOL / TECHNOLOGY / TARGET
- ChatGPT / Gemini
- Antigravity as AI coding agent
- Git/GitHub as project memory
- Secure Vibe Coding
- a small AI Security Brain / supervised-learning bridge

This is newer than the existing root README mapping that separates Introduction and Toolbox across Lesson 1 and Lesson 2. **Do not silently overwrite the canonical 16-lesson mapping.** Resolve and record the opening-lesson mapping before promotion.

## Current course invariants

- Python/FastAPI is the preferred application architecture.
- SQLite is preferred for local/lab use; production may use managed PostgreSQL.
- Supervised ML is taught across three lessons.
- LLM/RL are not separate primary course strands.
- Weather Security Center remains the shared build/attack/defend project.
- Offensive work is restricted to explicit authorized/isolated labs, teacher targets, TryHackMe/CTF or equivalent authorized ranges.
- Important legacy web-security knowledge must be preserved through migration.

## Next recommended action

1. Resolve whether the new Lesson 1 combines Introduction + Toolbox + first Security Brain, or whether part of that material remains Lesson 2.
2. Once resolved, update `DECISIONS.md`.
3. Then design Lesson 1 Part 1 in full teaching format: slides + teacher notes + interaction + demo/lab + Antigravity YAML + evidence.
4. Promote approved content into `Lesson1/` and update root README mapping if necessary.
