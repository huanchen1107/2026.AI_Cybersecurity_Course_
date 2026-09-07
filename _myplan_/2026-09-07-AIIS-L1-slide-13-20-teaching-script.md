# AIIS_L1 — Slides 13–20 Teaching Script
## WORKING ≠ SECURE → Asset → Threat → Vulnerability

Date: 2026-09-07
Status: Canonical detailed teaching script
Parent: `2026-09-07-AIIS-L1-Weather-Security-Center-Detailed-Lecture-Plan.md`

---

## Slide 13 — WORKING ✓

**Purpose:** Pause at functional success before the security turn.

**On-slide:**

# WORKING ✓

- The website runs.
- The data appears.
- The map works.
- The test passes.

**Visual:** extremely minimal success screen.

**煥哥:** satisfied rather than overly excited; relaxed posture; one hand presenting the successful website; gaze toward `WORKING ✓`.

**Teacher talk:** We know the application runs, receives data, renders output and may pass its tests. From a functional software perspective, this is success. But this is not only a software-development course.

**Transition:** fade everything except `WORKING ✓`, then ask the next question.

---

## Slide 14 — SECURE ?

**Purpose:** Major conceptual turn of the lesson.

**On-slide:**

# SECURE ?

**Working software is not automatically secure software.**

# WORKING ≠ SECURE

**Visual:** green `WORKING ✓` on the left, `SECURE ?` on the right, incomplete bridge between them.

**煥哥:** skeptical/thinking expression; one hand at chin, other pointing toward `SECURE ?`; gaze at the question mark.

**Teacher talk:** The real AIIS lesson begins here. Software Engineering asks whether a system works. Security Engineering additionally asks whether it is trustworthy and appropriately protected. AI generated the software, but that does not prove security.

**Ask:**「AI 幫我們寫出來了，所以安全嗎？」

Students may suggest scanners, antivirus, Kali, Nmap or ZAP. Do not reject these. Explain that tools come later; security does not begin by blindly launching a scanner.

**Transition:** `What are we protecting?`

---

## Slide 15 — Security Starts with Assets

**Title:** WHAT ARE WE PROTECTING?

# ASSET

**Visual:** Weather Security Center in the center with asset cards around it:
- Weather Data
- CWA API Key
- CSV Files
- Source Code
- Website
- User Access
- Service Availability
- Configuration
- Test Results

**煥哥:** detective-like focus; holding a magnifying glass toward the system; gaze toward API Key / Data assets.

**Core definition:**

> Asset = 對系統、組織或使用者有價值，因此需要保護的東西。

**Teacher talk:** Before discussing hackers, identify what has value. An asset is not only a computer. Data, secrets, code, accounts, service availability and even reputation may have value.

**Ask:**「我們剛才做的網站裡，請找出 5 個 Assets。」

---

## Slide 16 — Asset Detective

**Purpose:** Turn Asset from vocabulary into an observation skill.

**On-slide:**

### DATA
- Weather Forecast
- CSV
- User Data

### SECRET / IDENTITY
- API Key
- Account
- Configuration Secret

### SERVICE / SYSTEM
- Website
- Data Fetcher
- Database

**Challenge:** `Your job: Find 10 assets.`

**煥哥:** playful detective expression; magnifying glass in one hand, checklist in the other; leaning slightly toward the system.

**Teacher talk:** You are no longer only a user. You are a Junior Security Engineer. Your first task is to identify what is worth protecting.

**Student activity:** teams of 2–3, about 3 minutes. Record `Asset / Why valuable? / Who needs it?`.

Example:

| Asset | Why valuable? |
|---|---|
| CWA API Key | Represents authorized API access |
| Weather Data | Users depend on correctness |
| Website | Users depend on service |
| Source Code | Contains logic/configuration |
| CSV | Stores processed records |

**Transition:** Once we know the assets, ask what could harm them.

---

## Slide 17 — What Can Go Wrong?

**Title:** WHAT CAN GO WRONG?

# THREAT

**Visual:** Asset at center. Around it show multiple threat sources, not only a hacker:
- Attacker
- Human Error
- Software Bug
- External API Failure
- Malware
- Insider
- Hardware Failure
- Network Failure

**煥哥:** alert expression; hands slightly open to indicate multiple threat sources; gaze moving around threat icons.

**Core definition:**

> Threat = 可能造成傷害的事件、行為者或情境。

**Teacher talk:** Cybersecurity is not synonymous with hackers. Human mistakes, software failures, dependency failures and malicious actors can all create harmful situations.

**Examples:** API key placed incorrectly → human error; CWA API outage → external-service failure; malicious secret access → attacker.

---

## Slide 18 — Why Could It Succeed?

**Title:** WHY COULD IT SUCCEED?

# VULNERABILITY

**Case A**
```text
Asset: CWA API Key
Threat: Secret Exposure
Vulnerability: API Key hard-coded in source code
```

**Case B**
```text
Asset: Weather Service
Threat: External API failure
Vulnerability: No timeout / poor error handling
```

**Case C**
```text
Asset: Weather Data
Threat: Bad / unexpected external data
Vulnerability: Weak input validation
```

**煥哥:** analytical / realization expression; pointing to the causal connection between Threat and Vulnerability; gaze at the vulnerability card.

**Core distinction:**

> Threat = What may happen  
> Vulnerability = Why it may succeed

**Teacher talk:** A threat describes the harmful situation. A vulnerability describes a weakness or condition that makes the harmful outcome easier or more likely.

---

## Slide 19 — Threat ≠ Vulnerability

**Purpose:** Explicitly resolve the most common beginner confusion.

| THREAT | VULNERABILITY |
|---|---|
| API Key 被取得 | API Key hard-coded |
| 錯誤資料進來 | 沒有 validation |
| Service Down | 沒有 timeout / resilient handling |
| Unauthorized Access | 弱驗證機制 |

Center: `≠`

**煥哥:** serious and clear teaching expression; one hand indicating each column; gaze toward the central `≠`.

**Teacher talk:** If Threat and Vulnerability are mixed together, later risk analysis becomes confused.

**Quick exercise:** classify:
1. `No request timeout` → Vulnerability / weakness
2. `Attacker steals secret` → Threat event
3. `No data validation` → Vulnerability / weakness

---

## Slide 20 — Weather Center Security Cases

**Title:** PUT IT TOGETHER

### Case 1
```text
ASSET
CWA API Key
↓
THREAT
Secret Exposure
↓
VULNERABILITY
Hard-coded Secret
```

### Case 2
```text
ASSET
Weather Data
↓
THREAT
Incorrect / Malformed Input
↓
VULNERABILITY
Weak Validation
```

### Case 3
```text
ASSET
Weather Website
↓
THREAT
Service Unavailable
↓
VULNERABILITY
No Timeout / Poor Failure Handling
```

At the bottom:

`ASSET → THREAT → VULNERABILITY → SO WHAT?`

**煥哥:** detective connecting clues; holding Asset/Threat/Vulnerability cards and visually linking them; gaze toward `SO WHAT?`.

**Teacher talk:** We can now identify assets, threats and vulnerabilities. But a security engineer still needs to ask: if this happens, what is actually affected? API key exposure, incorrect weather data and an unavailable website do not damage the same security property.

**Transition:** Introduce the CIA Triad as the language for describing what security property is affected.

---

## Teaching State After Slide 20

Students should now be able to follow:

```text
WORKING ≠ SECURE
        ↓
      ASSET
        ↓
      THREAT
        ↓
  VULNERABILITY
        ↓
    SO WHAT?
        ↓
NEXT: CIA TRIAD → RISK
```

Do not introduce scanners yet. Preserve the narrative that security thinking precedes security tooling.