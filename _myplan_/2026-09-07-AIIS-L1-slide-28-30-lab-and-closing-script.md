# AIIS_L1 — Slides 28–30 Lab and Closing Script
## AI Builder → AI Security Analyst → Human Verification

Date: 2026-09-07
Status: Canonical detailed teaching script
Parent: `2026-09-07-AIIS-L1-Weather-Security-Center-Detailed-Lecture-Plan.md`

---

## Slide 28 — AI Changes Role: Builder → Security Analyst

**Purpose:** Show that the same AI assistant can help review the system, while human verification remains mandatory.

**On-slide:**

```text
AI BUILDER
Prompt → Plan → Code → Run
             ↓
          SWITCH
             ↓
AI SECURITY ANALYST
Observe → Question → Analyze → Recommend
```

Bottom:

# AI ASSISTS. HUMAN VERIFIES.

**Visual:** left side shows `Prompt → Antigravity → Weather Website`; right side shows `Weather Website → AI Review → Possible Risks → Evidence? → Human Decision`.

**煥哥:** preferably two states: left side confident builder holding a Prompt card and presenting the site; right side serious reviewer holding a checklist / magnifier and examining the risk report. If using one character, one hand represents Build, the other Review. Gaze toward the Security Analyst side.

**Teacher talk:** AI first acted as Builder. Now we can ask it to become a Security Analyst. But an AI statement is not automatically a confirmed security finding. The engineer must ask `Why? Where? What evidence? Can we verify it?`

**Key teaching state:**

```text
AI Finding ≠ Confirmed Finding

CONFIRMED
ASSUMPTION
NEEDS VERIFICATION
```

**Review prompt:**

```text
Review the AI Weather Security Center
from a cybersecurity risk perspective.

Do not modify the code.

Identify:
1. Asset
2. Threat
3. Possible vulnerability
4. CIA impact
5. Likelihood
6. Impact
7. Risk level
8. Recommended control

For every finding:
- distinguish confirmed evidence from assumptions
- explain what evidence supports the conclusion
- if the issue cannot be confirmed, write:
  NEEDS VERIFICATION

Do not invent vulnerabilities.
Do not modify the application.
```

**Demo rule:** If AI says something like `API Key may be hard-coded`, immediately ask whether the evidence proves it. If not, classify it as `NEEDS VERIFICATION`.

**Transition:** Students now become the Security Engineer.

---

## Slide 29 — AI Security Risk Detective: Student Mini Lab

**Title:** YOUR TURN — AI SECURITY RISK DETECTIVE

**Subtitle:** AI 可以幫忙，但最後的判斷是你的。

**Scenario:**

```text
AI WEATHER SECURITY CENTER

• CWA weather API
• Streamlit website
• Regional temperature map
• CSV output

Additional observations:
• Admin account exists
• MFA is disabled
• 46 failed login attempts
• Logins observed from 5 countries
• API key may be stored in configuration
• User data exists in local storage
• No backup has been confirmed
```

The wording intentionally mixes observations, possibilities, and unknowns so students must distinguish facts from assumptions.

**Student worksheet:**

| Field | Student Analysis |
|---|---|
| Asset | What are we protecting? |
| Threat | What may happen? |
| Vulnerability | What weakness exists? |
| CIA | C / I / A |
| Likelihood | Low / Medium / High |
| Impact | Low / Medium / High |
| Risk | Low / Medium / High / Critical |
| Control | What could reduce risk? |
| Evidence | What proves this? |
| AI Suggestion | What did AI say? |
| Human Review | Accept / Reject / Verify |

**煥哥:** encouraging coach; handing a magnifying glass toward students and pointing to the Risk Worksheet; gaze toward students.

**Mandatory reflection:**

```text
AI suggested:
_________________________

My decision:
[ ] ACCEPT
[ ] REJECT
[ ] NEEDS VERIFICATION

Because:
_________________________
```

**Teacher questions while circulating:**
1. `你的 Evidence 在哪裡？`
2. `這是 Fact 還是 Assumption？`
3. `你為什麼把它排 High？`

**Teaching example:** 46 failed logins are suspicious evidence, but by themselves do not prove a successful compromise. More logs and source context are required.

---

## Slide 30 — This Is Only the Beginning

**Title:** TODAY WE BUILT IT. NEXT, WE LEARN TO TRUST IT.

**Main story:**

```text
PROMPT
  ↓
ANTIGRAVITY
  ↓
REAL CWA DATA
  ↓
WEATHER WEBSITE
  ↓
WORKING ✓
  ↓
SECURE ?
  ↓
ASSET
  ↓
THREAT
  ↓
VULNERABILITY
  ↓
CIA
  ↓
RISK
  ↓
AI REVIEW
  ↓
HUMAN VERIFICATION
```

**Future path:**

```text
NEXT
SCAN
  ↓
FIND
  ↓
UNDERSTAND
  ↓
FIX
  ↓
TEST
  ↓
RE-SCAN
  ↓
VERIFY
```

**煥哥:** confident guide; holding the completed Weather Security Center in one hand and pointing toward the future `SCAN → FIX → VERIFY` road with the other; gaze forward, not a repeated thumbs-up pose.

**Teacher talk:** Today we built a real system with AI and deliberately refused to equate `working` with `secure`. Revisit: Asset, Threat, Vulnerability, CIA, Risk, AI Assistance, Human Verification.

**Closing lines:**

# AI BUILDS. HUMAN VERIFIES.
# WORKING ≠ SECURE.

**Preview:**
- L2: Antigravity + GitHub engineering workflow
- L3: Understand Python / API / JSON / Data / Web internals
- L4: Semgrep `SCAN → FIND → FIX → TEST → RE-SCAN`

**Exit Ticket:**
1. Name one Asset in the Weather Security Center.
2. Explain Threat vs Vulnerability.
3. Complete: `AI ________. Human ________.`

Expected: `AI assists/builds. Human verifies.`

---

## L1 Closed-Loop Narrative

```text
BUILD
 ↓
WOW
 ↓
QUESTION
 ↓
SECURITY THINKING
 ↓
RISK
 ↓
AI REVIEW
 ↓
HUMAN VERIFY
 ↓
NEXT: SCAN / FIX / VERIFY
```

煥哥角色弧線：`Host → Builder → Observer → Celebrator → Skeptic → Detective → Analyst → Coach → Guide`.