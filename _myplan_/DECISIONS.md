# DECISIONS — Durable Project Decisions

This file records decisions that future ChatGPT sessions and interchangeable coding agents should treat as durable until explicitly superseded.

## D-001 — GitHub is durable project memory

Chat conversations are not the sole source of continuity. GitHub files, code, tests, commits and `_myplan_` artifacts must allow another agent to resume work without the previous conversation.

## D-002 — `_myplan_` is bidirectional

`_myplan_` is the ChatGPT ↔ GitHub ↔ Antigravity coordination layer. Agents must both read from it and write state/evidence back to it.

## D-003 — Canonical vs planning boundary

`Lesson1/`–`Lesson16/` contain canonical course content. `_myplan_` contains planning, decisions, handoff and history. A dated discussion is not automatically a canonical requirement.

## D-004 — Required promotion lifecycle

Use: `DISCUSS → DECIDE → PLAN → IMPLEMENT → VERIFY → PROMOTE`.

## D-005 — Course architecture

The course uses a 16-lesson integrated AI × Cybersecurity structure and a shared project rather than unrelated weekly demos.

The canonical focused progression is:

`BUILD → LEARN → ATTACK → DEFEND → GOVERN → FINAL`

The 2026-09-07 focused 16-lesson plan is the current architecture of record.

## D-006 — Shared technical direction

Primary stack: Python + FastAPI, local/lab SQLite + SQLAlchemy, pandas/scikit-learn for ML, PyTorch where deep learning is needed, Git/GitHub for persistent evidence and collaboration.

## D-007 — AI-assisted engineering method

Vibe Coding is taught as **Secure Vibe Coding**, not blind generation. Core loop: `Prompt → Build → Run → Test → Verify → Secure`. Humans remain responsible for requirements, interpretation, verification and security.

## D-008 — Opening curriculum mapping — RESOLVED 2026-09-07

The previous Lesson 1/Lesson 2 allocation question is resolved.

The course follows the later focused 16-lesson plan:

- **L1 = Course Foundations / AI Security Engineer Mindset.** Introduce AI × cybersecurity, Asset/Threat/Vulnerability/Risk, CIA, authorization/ethics and AI-assisted risk reasoning.
- **L2 = AI Security Engineer Toolbox.** Introduce ChatGPT/Gemini working roles, Antigravity, Git/GitHub, prompt engineering and Secure Vibe Coding.
- **L3 = FastAPI Weather Security Center.** Begin/extend the shared engineering project.
- **L4 = Secure Development / Semgrep.** Introduce representative SAST and the scan/fix/re-scan cycle.
- **L5–L7 = Supervised ML.** Classification foundations, tree models and security evaluation.

The earlier `Lesson01-AI-Security-Brain-Vibe-Coding-Antigravity` discussion is retained as a source of useful teaching material, but it does not override this mapping. Its material should be redistributed to the appropriate focused lessons rather than combining Introduction + Toolbox + ML into L1.

If older planning artifacts conflict with `_myplan_/2026-09-07_AIIS_16_Lesson_Focused_Course_Plan.md`, the later focused 16-lesson plan takes precedence unless the course owner explicitly approves another architecture change.

## D-009 — ML allocation

Supervised machine learning receives three lessons (L5–L7). Reinforcement learning and LLM topics are not separate primary strands in the current course architecture.

Deep learning remains core in L9–L10.

## D-010 — Security knowledge preservation

Migration away from the original Weather Web material must preserve important concepts including authentication, password hashing, authorization/RBAC/IDOR, SQL injection, XSS, CSRF, session security, input validation, API security, dependency risk, logging, safe error handling, threat modeling, OWASP secure coding and ISO 27001/risk concepts.

## D-011 — Offensive-security boundary

Attack activities must be limited to localhost, owned isolated VM/container labs, teacher-provided targets, TryHackMe/CTF or other explicitly authorized environments. Public accessibility does not imply permission to attack.

## D-012 — Scope discipline / representative-tool policy

Do not continuously expand the required curriculum when new tools are discovered. Each lesson should normally focus on one core concept, one representative technology/tool, one achievable lab and one evidence artifact. Alternatives belong in `Further Exploration` unless they materially replace an inferior core tool.

The complete AI-assisted Secure SDLC remains an advanced roadmap; it does not replace the canonical ML/DL/security course backbone.