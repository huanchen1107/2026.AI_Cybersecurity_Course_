# AIIS_L0 — Slides 07–21 Detailed Teaching Script

Date: 2026-09-07
Parent plan: `2026-09-07-AIIS-L0-32-slide-detailed-lecture-plan.md`
Status: Detailed lecture script

## Story

```text
ANI → AGI → ASI
       ↓
BACK TO TODAY
       ↓
Discriminative AI → Generative AI → Agentic AI
                                         ↓
                                    AI CAN ACT
                                         ↓
                             SECURITY RESPONSIBILITY
                                         ↓
Asset → Threat → Vulnerability → Risk → CIA
```

# Slides 07–10 — ANI / AGI / ASI

## Slide 07 — Three AI Concepts
On-slide: `ANI → AGI → ASI`.
Use capability comparison, NOT a dated future timeline. Explain that definitions/timelines for AGI and ASI are debated. Ask whether “can do many tasks” alone proves AGI.

## Slide 08 — ANI: Artificial Narrow Intelligence
Core: `Specific Task → Strong Capability`.
Examples: spam detection, image recognition, phishing detection, recommendation. Emphasize: Narrow does not mean weak; capability is task-dependent. Bridge to later ML security detection.

## Slide 09 — AGI: Artificial General Intelligence
Visual: one intelligence core connected to language, coding, science, reasoning, planning and learning. Keywords: Generalize / Transfer / Adapt. Do not claim a company/model has definitively achieved AGI. Ask whether benchmark scores alone prove general intelligence.

## Slide 10 — ASI: Artificial Superintelligence
Compare ANI / AGI / ASI. ASI is hypothetical broad capability substantially exceeding humans. Course guard: `AIIS focuses on what we can build, test and secure TODAY.` Ask: must we wait for AGI/ASI before AI security matters? No.

# Slides 11–14 — AIIS Teaching Framework

## Slide 11 — ANI Is Already Changing
AIIS teaching framework, explicitly not universal taxonomy:

```text
Discriminative AI → Generative AI → Agentic AI
幫我判斷            幫我產生         幫我完成
JUDGE               CREATE           ACT
```

Ask which stage makes security consequences more direct.

## Slide 12 — Discriminative AI: 幫我判斷

```text
INPUT → MODEL → CLASS / SCORE / PREDICTION
```

Security cases: Email→Spam/Normal; URL→Phishing/Legitimate; Traffic→Attack/Normal; Login→Suspicious/Normal.
Bridge: Data → Features → Model → Prediction. Ask whether a suspicious prediction should automatically lock an account; preserve false-positive question for Slide 31.

## Slide 13 — Generative AI: 幫我產生

```text
Prompt → Generative AI → Text / Code / Image / Audio / Video
```

Key teaching point: natural language increasingly controls computation. Example prompt: “Write a Python program that counts failed login events.”

Important:

```text
Generate ≠ Correct ≠ Secure
```

Ask whether generated code is ready to use merely because it runs.

## Slide 14 — Agentic AI: 幫我完成

Use loop:

```text
GOAL → PLAN → CHOOSE TOOL → ACT → OBSERVE → CORRECT → COMPLETE
                              ↑                     │
                              └─────────────────────┘
```

Capabilities: Read Files / Write Code / Run Commands / Call APIs / Run Tests / Inspect Errors / Modify Code.
Compare `Prompt → Answer` with `Goal → Plan → Act → Observe → Correct → Complete`.

End with questions: if AI can read files, write code, run commands, call APIs and deploy, what can go wrong? Fade page to:

> **AI CAN ACT**
>
> **What happens when AI can ACT?**

# Slides 15–17 — Security Turn

## Slide 15 — What Happens When AI Can ACT?

Architecture:

```text
Human
  ↓
AI Agent
  ↓
Files / Code / Tools / APIs / Database / Cloud
```

Scenario repo contains `app.py`, `database.db`, `README.md`, `.env`, `api_key.txt`. Ask whether agent should read/change everything. Discuss accidental deletion, database modification, secret exposure and wrong commands.

Core:
> **The ability to act creates the need to control action.**

## Slide 16 — Capability ↑ Responsibility ↑

Compare Answer → Generate → Act. As capability/access/autonomy increase, potential impact and security responsibility increase.

Use account analogy: Guest → Student → Administrator. Administrator is not “bad”; it needs stronger controls because it can do more.

Introduce without deep dive:
> **Give only the permissions needed for the task.**

This foreshadows Least Privilege.

## Slide 17 — AI System ≠ AI Model

Architecture:
`Human → Agent → Application → API → Database → Cloud → Data`

Security concerns: Identity / Permission / Secrets / Input / Output / Data / Logs / Network / Deployment.

Examples: model may be fine while API key leaks; prediction may be correct while database is improperly modified.

Core:
> **Security is a system property.**
>
> **Security protects the SYSTEM, not only the MODEL.**

Transition to everyday thief story.

# Slides 18–21 — Security Fundamentals

## Slide 18 — Asset: What Is Worth Protecting?

Story: NT$50,000 on a table → Value → Asset.

Definition:
> **Asset = Something valuable that needs protection.**

Map physical/digital: Money→Data; Wallet→Account; House Key→Password; Safe Key→API Key; Business→Service.

Weather Center assets: Weather Data / User Account / Password / API Key / Source Code / Database / Service Availability.

Security should first ask “what do we value?”, not “how will hackers attack?”

## Slide 19 — Threat: Who or What Can Cause Harm?

Story: thief sees the money.

Definition:
> **Threat = Something capable of causing harm.**

Threats are not only hackers: attacker, malware, insider, human error, system failure, natural event. AI incorrect action can also participate in a harmful scenario.

Ask: Must a threat be malicious? No.

## Slide 20 — Vulnerability: Where Is the Weakness?

Physical examples: unlocked door / open window / exposed money.
Digital mapping: weak authentication / exposed sensitive data / API key in GitHub / missing access control / insecure configuration.

Definition:
> **Vulnerability = A weakness that can be exploited or lead to harm.**

Important distinction:
`Threat ≠ Vulnerability`.

Example: API key is an asset/credential; committing it publicly creates exposure/weakness; an attacker can exploit that weakness.

## Slide 21 — Risk + CIA Triad

Risk story:

```text
Asset + Threat + Vulnerability
              ↓
         Possible Loss
              ↓
             Risk
```

Cyber example: API Key + Attacker + Public Exposure → Unauthorized Use → Cost/Data/Service Impact.

Preview only:
`Risk ≈ Likelihood × Impact`; full treatment belongs to GOVERN.

Then ask: what does “protect data” mean?

CIA:
- Confidentiality — 誰可以看？
- Integrity — 誰可以改？資料是否保持正確完整？
- Availability — 需要時能不能用？

Weather Center mapping:
- C: user/API secrets cannot leak
- I: weather/security data cannot be improperly modified
- A: service must be available when needed

Core:
> **Security ≠ Secrecy only.**

Final mental model:

```text
WHAT DO WE VALUE?       → ASSET
WHAT CAN HARM IT?       → THREAT
WHAT WEAKNESS EXISTS?   → VULNERABILITY
WHAT COULD WE LOSE?     → RISK
WHAT MUST WE PRESERVE?  → C + I + A
```

Transition:
> 如果只在投影片上講這些，你們學不會資安。所以這學期我們需要一個真的系統。

→ **AI WEATHER SECURITY CENTER**
