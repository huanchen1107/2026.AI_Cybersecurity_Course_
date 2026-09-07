# AIIS_L1 — Slides 21–27 Teaching Script
## CIA Triad → Risk Prioritization

Date: 2026-09-07
Status: Canonical detailed teaching script
Parent: `2026-09-07-AIIS-L1-Weather-Security-Center-Detailed-Lecture-Plan.md`

---

## Slide 21 — CIA Triad

**Purpose:** Give students a common language for describing what security property is harmed.

**Title:** WHAT DOES “SECURE” MEAN?

# CIA TRIAD

```text
            SECURITY
                │
      ┌─────────┼─────────┐
      ↓         ↓         ↓
      C         I         A
Confidentiality Integrity Availability
      │         │         │
    不外洩      不亂改      不停擺
```

Memory questions:
- C — Who can SEE it?
- I — Can I TRUST it?
- A — Can I USE it?

**煥哥:** professional teaching expression; one open hand pointing to the three CIA points; gaze toward the diagram.

**Teacher talk:** Do not start by memorizing three English words. Start with three practical questions: who can see it, can I trust it, and can I use it when needed? Then map those questions to Confidentiality, Integrity and Availability.

---

## Slide 22 — Confidentiality

**Title:** C — CONFIDENTIALITY

# WHO CAN SEE IT?

Main case:

```text
CWA_API_KEY
     │
     ├── Teacher / Application ✓
     │
     └── Everyone on GitHub ✗
```

**Definition:** Confidentiality = 防止未授權的資訊揭露。

Examples:
- Weather Forecast → public
- API Key → restricted
- Password → restricted
- Private User Data → restricted
- Public Temperature → public

**煥哥:** alert/protective expression; holding an API-key card near the body, other hand naturally shielding it; gaze on the secret.

**Teacher talk:** Confidentiality does not mean everything must be hidden. Public weather data is intended to be seen. The real question is authorization: who is allowed to see this information?

**Interaction:** classify sample assets as `Public` or `Restricted`.

---

## Slide 23 — Integrity

**Title:** I — INTEGRITY

# CAN I TRUST IT?

Visual scenario:

```text
CWA
Heavy Rain / 32°C
        ↓
API → Parser → CSV → Website
        ↓
Website says: Sunny / 22°C
```

Center question: `?`

**Definition:** Integrity = 資料保持正確、完整，且未被未授權修改。

**煥哥:** skeptical/confused expression; comparing original CWA information in one hand with website output in the other; gaze shifting between them.

**Teacher talk:** Nothing needs to be leaked and the server can remain online, yet the system can still be unsafe if users cannot trust the information. Wrong or unauthorized-modified data is an integrity problem.

**Forward connection:** Later AI/ML lessons will revisit the idea that bad data can produce wrong AI decisions.

---

## Slide 24 — Availability

**Title:** A — AVAILABILITY

# CAN I USE IT WHEN I NEED IT?

Visual:

```text
USER → Weather Center → Weather Alert
```

versus

```text
USER → Weather Center ✕
       SERVICE UNAVAILABLE
```

Context card: `Typhoon Day — 08:00 / SERVER DOWN`

**煥哥:** concerned/alert expression; pointing toward a service-down warning; gaze at the warning.

**Teacher talk:** A five-minute outage may be merely inconvenient in one context but serious during a disaster-warning situation. Availability is not “a system can never go down”; it means the service is available at an acceptable level when it is needed.

**Transition:** Same technical failure can have different business impact. This leads naturally to Risk.

---

## Slide 25 — One System, Three Questions

**Title:** THREE QUESTIONS. ONE SYSTEM.

```text
        C
 WHO CAN SEE IT?
        │
        │
I ───── APP ───── A
│                 │
CAN I             CAN I
TRUST IT?         USE IT?
```

Examples:

| Problem | CIA |
|---|---|
| API Key leaked | C |
| Weather data changed | I |
| Website unavailable | A |
| User account stolen | C / I / possibly A |

**煥哥:** integrating/teaching expression; positioned behind the Weather Center and connecting the three CIA directions with both hands.

**Teacher talk:** CIA is not just a memorization item. It is a fast analysis lens. One incident can affect more than one CIA property.

**Class repetition:** `Who can see it? / Can I trust it? / Can I use it?`

---

## Slide 26 — From Vulnerability to Risk

**Title:** NOT EVERY PROBLEM IS EQUALLY IMPORTANT

```text
ASSET
  ↓
THREAT
  ↓
VULNERABILITY
  ↓
CIA IMPACT
  ↓
LIKELIHOOD
  +
IMPACT
  ↓
RISK
```

# Risk ≈ Likelihood × Impact

Do not teach complex quantitative scoring in L1.

**煥哥:** Security Analyst expression; holding a simple risk-assessment board and marking Likelihood × Impact; gaze toward Risk.

**Teacher talk:** Security teams cannot treat every finding as the same priority. Ask how likely the event is and how serious the consequences would be. That leads to a basic risk judgment.

**Key distinction:** `Vulnerability ≠ Risk`.

---

## Slide 27 — Risk Ranking

**Title:** WHAT SHOULD WE FIX FIRST?

Simplified matrix:

| | Impact Low | Impact Medium | Impact High |
|---|---:|---:|---:|
| Likelihood Low | Low | Low–Med | Medium |
| Likelihood Medium | Low–Med | Medium | High |
| Likelihood High | Medium | High | Critical |

Weather Center cases:

### A — UI font looks bad
`Security Risk? Probably NOT.`

### B — No handling for API timeout
`Availability / Risk: Medium`

### C — CWA API Key is public in GitHub
`Confidentiality / Risk: High`

### D — `eval()` is used on external input
`Potentially serious / Risk: High or Critical / Needs evidence and context`

**煥哥:** prioritization/manager expression; arranging four Risk Cards from High/Critical to Low; gaze toward the highest-priority cards.

**Teacher talk:** Security Engineering is not about finding the largest number of issues. It is about identifying the issues that actually matter and fixing them in a sensible order.

**Final concept animation:**

# BUG ≠ VULNERABILITY ≠ RISK

- Bug = 程式有問題。
- Vulnerability = 這個問題可能形成安全弱點。
- Risk = 該弱點在實際情境下造成損失的可能性與影響。

---

## Teaching State After Slide 27

Students now have the complete first-pass security reasoning chain:

```text
SYSTEM
  ↓
ASSET
  ↓
THREAT
  ↓
VULNERABILITY
  ↓
CIA
  ↓
LIKELIHOOD
  ↓
IMPACT
  ↓
RISK
```

Next: change AI's role from `BUILDER` to `SECURITY ANALYST`, require evidence-aware AI review, then close L1 with the first student risk artifact and the future `SCAN → FIND → FIX → RE-SCAN → VERIFY` workflow.