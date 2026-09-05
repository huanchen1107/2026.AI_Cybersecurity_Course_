# Introduction — AI × Cybersecurity × Vibe Coding

## Course Vision

本課程以「做出來、讓系統學習、在授權環境測試它、修好它、最後治理它」為主軸。

```text
BUILD → LEARN → ATTACK → DEFEND → GOVERN
```

AI 是能力，Cybersecurity 是主線。

## Course Philosophy

- AI generates. Human verifies. Security validates.
- Prompt 可以成為軟體需求、安全契約與測試規格。
- Untrusted data crossing a trust boundary may become code, command, query, browser content, or model input.
- AI Input、AI Output、External API、Database Data、ML Data 都不自動視為可信。
- Offensive security 僅限自有、授權、隔離 Lab / CTF / TryHackMe。
- Publicly accessible does not mean publicly authorized to attack.

## Shared Semester Mission

全課共用同一個主專案：`AI Weather Security Center`。

```text
Weather API / Fake Sensor
        ↓
Python + FastAPI
        ↓
SQLite / SQLAlchemy
        ↓
Dashboard + Login + Security Events
        ↓
Supervised ML / Deep Learning
        ↓
TryHackMe — Learn the Attack
        ↓
Local Weather Cyber Range — Prove it in Our Lab
        ↓
AI Blue Team — Fix Our Code
        ↓
ISO 27001 / Risk Governance
```

## Environment Model

- Vercel / production-like deployment: secure demo and non-destructive verification.
- Local Docker / VM Cyber Range: teacher-controlled vulnerable targets and authorized red-team validation.
- TryHackMe / CTF: standardized attack-learning environment under platform rules.

Core sentence:

> Learn it in the Range. Prove it in our Lab. Fix it in our Code.

## Required Lesson Format

每一個課程主題必須包含：

1. Concept
2. Security Meaning
3. Practical Example / Lab
4. Antigravity YAML Prompt
5. Test / Evidence
6. Human explanation / reflection

學生的目標不是「AI 幫我做完」，而是能說明 AI 做了什麼、為什麼這樣做、如何驗證，以及什麼風險仍然存在。