# 2026-09-05 — 16 Lesson Directory Migration

The repository originally used `Introduction + Lesson1..Lesson5` as five broad modules. The 2026 master curriculum now uses 16 teaching sessions.

## Canonical Rule
From this point forward, `Lesson1` through `Lesson16` represent the 16-session course sequence.

## Migration Note
Historical Lesson 1–5 material is preserved and traced rather than silently deleted. Some original broad-module README files remain as source/legacy knowledge while canonical session-specific documents are progressively expanded.

## Canonical 16 Lessons
1. Introduction — AI × Cybersecurity
2. AI Security Engineer Toolbox
3. BUILD — Python FastAPI Weather Security Center
4. How to Build an AI Cybersecurity Project
5. Supervised ML I — Classification Foundations
6. Supervised ML II — Tree Models
7. Supervised ML III — Security Evaluation
8. Midterm AI Security Engineering Review
9. Deep Learning I — Neural Networks for Security
10. Deep Learning II — Security Sequence Analysis
11. AI Red Team I — Learn the Attack in TryHackMe
12. AI Red Team II — Prove it in Our Weather Cyber Range
13. AI Blue Team — Fix Our Code
14. GOVERN — ISO 27001 × Risk Management
15. Final Project Demo I
16. Final Project Demo II & Course Closure

## Required Lesson Contract
Every lesson must be expanded using:
`Concept → Security Meaning → Practical Lab → Antigravity YAML → Test/Evidence → Reflection`.

## Safety Contract
Offensive labs are limited to explicitly authorized training environments, localhost, teacher-controlled Docker/VM targets, CTF/TryHackMe, or equivalent explicit scope. Public production/Vercel is not the classroom exploitation target.

## Knowledge Preservation
The original Weather Web security concepts remain required: password hashing, session security, authentication vs authorization, RBAC/IDOR, injection, XSS/output safety, CSRF concepts, input validation, dependency risk, logging, safe error handling, threat modeling, OWASP repair, and ISO 27001 governance. They are redistributed through spiral learning rather than removed.