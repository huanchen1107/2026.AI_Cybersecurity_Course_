# AIIS_L0 — AI Revolution × Information Security
## 32-Slide Detailed Lecture Plan

Date: 2026-09-07
Status: Canonical detailed lecture plan
Course: AIIS — AI and Information Security（人工智慧與資訊安全）
Position: Pre-course worldview / introduction before AIIS_L1–L16

> AI is the capability. Information Security is the discipline.

## Canonical Story

```text
HUMAN TECHNOLOGY
Machine → Energy → Information → Intelligence
                         ↓
                   AI REVOLUTION
                         ↓
                 ANI → AGI → ASI
                         ↓
          Discriminate → Generate → Act
                                    ↓
                            AI CAN ACT
                                    ↓
                         SECURITY MATTERS
                                    ↓
             Asset → Threat → Vulnerability → Risk
                                    ↓
                              CIA TRIAD
                                    ↓
                    AI WEATHER SECURITY CENTER
                                    ↓
              BUILD → LEARN → ATTACK → DEFEND → GOVERN
                                    ↓
                        FIRST AI-ASSISTED LAB
                                    ↓
                   Rule ≠ Intelligence ≠ Truth
                                    ↓
                          NEXT: AIIS_L1
```

## Terminology Correction

Do NOT call the complete sequence “Four Industrial Revolutions / 四大工業革命”.
Use:

**人類歷史上的四次重要技術革命 — Four Major Technological Revolutions**

Teaching progression:

`Machine Power → Energy Power → Information Power → Intelligence Power`

Only the first is explicitly introduced as the Industrial Revolution in this teaching framework.

---

# PART A — OPENING: WHY AIIS?

## Slide 01 — AIIS: AI and Information Security
**Purpose:** Establish identity and curiosity.

**On-slide:**
- AIIS — AI and Information Security
- 人工智慧與資訊安全
- `AI is the capability. Information Security is the discipline.`

**Visual:** Human → AI → Digital World, with security shield surrounding the system.

**煥哥:** welcoming, open-hand gesture, looking toward title.

**Teacher talk:** This is not one half AI and one half cybersecurity. We will build one real system and repeatedly learn how AI changes what software can do, then ask how to make that system trustworthy and secure.

**Ask:**「你覺得 AI 和資安是兩門不同的課嗎？」

**Transition:** Before defining AI, first understand what kind of technological change we are living through.

## Slide 02 — What Era Are We Living In?
**Purpose:** Start from history rather than definitions.

**On-slide:** `我們正在經歷什麼樣的科技轉變？`

Four silhouettes only: machine → electricity → computer/network → AI brain/agent.

**煥哥:** thinking pose.

**Teacher talk:** Human history repeatedly creates technologies that amplify a limited human capability. Ask what each revolution amplified.

---

# PART B — FOUR MAJOR TECHNOLOGICAL REVOLUTIONS

## Slide 03 — Industrial Revolution: Machine Power
**Core:** Machines amplify physical power.

**On-slide:**
- Industrial Revolution
- 機械化 / 蒸汽機
- **Machine Power**
- `Human muscle → Machine power`

**Visual:** hand work → steam machine → factory.

**煥哥:** presenting toward machine illustration.

**Ask:**「蒸汽機真正放大的是人的哪一種能力？」

## Slide 04 — Energy Revolution: Energy Power
**Core:** Electricity/petroleum enable scalable energy use.

**On-slide:**
- Energy Revolution
- 電力 / 石油 / 大規模能源利用
- **Energy Power**

**Visual:** generator → grid → city/factory.

**Teacher emphasis:** The important idea is not memorizing dates; it is the change in what humans can scale.

## Slide 05 — Information Revolution: Information Power
**Core:** Computers and networks amplify information processing.

**On-slide:**
- Information Revolution
- Computer / Internet / Software
- **Information Power**

**Visual:** computer → network → cloud/data.

**Ask:**「沒有 AI，電腦已經很厲害；那 AI 到底多了什麼？」

## Slide 06 — AI Revolution: Intelligence Power
**Core:** AI amplifies cognitive capability.

**On-slide:**
- AI Revolution
- Artificial Intelligence / Machine Intelligence
- **Intelligence Power**
- `Machine → Energy → Information → Intelligence`

**Visual:** four-stage horizontal timeline; Intelligence highlighted.

**煥哥:** emphasize / raised index finger.

**Takeaway:** AI is significant because technology is beginning to amplify tasks associated with judgment, generation, planning and decision support.

---

# PART C — AI REVOLUTION: ANI → AGI → ASI

## Slide 07 — Three AI Concepts
**On-slide:** `ANI → AGI → ASI`

**Visual:** three increasing capability circles, not a guaranteed chronological prediction.

**Teacher note:** Clearly state that AGI/ASI definitions and timelines remain debated. Do not imply a confirmed arrival date.

## Slide 08 — ANI: Artificial Narrow Intelligence
**Core:** Strong capability in bounded tasks.

Examples:
- Spam classification
- Image recognition
- Recommendation
- Phishing detection
- Generative AI applications

**Ask:**「現在我們每天使用的大部分 AI，比較接近哪一類？」

## Slide 09 — AGI: Artificial General Intelligence
**Core:** General cross-domain capability is a research/social concept, not something this course assumes is already achieved.

**Visual:** multiple domains connected to one intelligence core.

**煥哥:** analytical/explaining.

## Slide 10 — ASI: Artificial Superintelligence
**Core:** Hypothetical intelligence substantially exceeding humans across broad domains.

**Visual:** ANI / AGI / ASI comparison cards.

**Teacher caution:** This slide is conceptual context, not prediction.

**Transition:** We do not need to wait for AGI to see a major change. ANI itself has evolved in how we use it.

---

# PART D — AIIS TEACHING FRAMEWORK: DISCRIMINATE → GENERATE → ACT

## Slide 11 — ANI Is Already Changing
**On-slide:**
`Discriminative AI → Generative AI → Agentic AI`

Label clearly: **AIIS teaching framework**, not universal academic taxonomy.

**Visual:** Judge → Create → Act.

## Slide 12 — Discriminative AI: “幫我判斷”
**Flow:** `Input → Model → Class / Score / Prediction`

Security examples:
- Email → Spam / Not Spam
- URL → Phishing / Legitimate
- Traffic → Normal / Attack
- Event → Normal / Suspicious

**Course bridge:** Supervised ML / Deep Learning.

## Slide 13 — Generative AI: “幫我產生”
**Flow:** `Prompt → Generative AI → Text / Code / Image / Audio / Video`

Examples: ChatGPT, Gemini, coding assistants.

**Question:**「產生答案和判斷分類，最大的不同是什麼？」

## Slide 14 — Agentic AI: “幫我完成”
**Flow:**
`Goal → Plan → Tools → Read → Write → Run → Observe → Fix`

**Visual:** closed-loop agent workflow.

**煥哥:** professional presenting with loop diagram.

**Key distinction:** `Prompt → Answer` vs `Goal → Plan → Act → Observe → Correct → Complete`.

---

# PART E — THE SECURITY TURN

## Slide 15 — What Happens When AI Can ACT?
**Purpose:** Major dramatic transition.

**On-slide:** only major question plus diagram:
`Human → AI Agent → Files / Code / API / Database / Cloud`

**Teacher question:** If an AI only answers incorrectly, that is one kind of problem. If it can modify code, call APIs, read files and deploy systems, is an error still the same kind of problem?

**煥哥:** serious / concerned.

## Slide 16 — Capability ↑ Responsibility ↑
**On-slide:**
`AI capability ↑ → Security responsibility ↑`

Compare:
- Answering
- Generating
- Acting

Each step increases potential consequence and required controls.

## Slide 17 — AI System = More Than a Model
**Architecture:**
Human → Agent → Application → API → Database → Cloud → Data

Overlay security concerns:
Identity / Permission / Secret / Input / Data / Logging / Deployment.

**Takeaway:** We secure the whole system, not only “the AI”.

---

# PART F — SECURITY FUNDAMENTALS THROUGH A THIEF STORY

## Slide 18 — What Is Worth Protecting? Asset
Story: NT$50,000 on a table.

`Asset = something valuable that needs protection`

Map to digital world: Data / Account / API Key / Model / Service.

**煥哥:** point toward money → API key mapping.

## Slide 19 — Who or What Can Cause Harm? Threat
Story: thief wants the money.

`Threat = something capable of causing harm to an asset`

Digital: attacker / malicious actor / malware / accident / failure.

## Slide 20 — What Weakness Can Be Exploited? Vulnerability
Story:
- money left exposed
- door unlocked
- window open

Digital:
- API key committed to repository
- weak password
- missing validation
- insecure configuration

**Key:** Vulnerability is a weakness; threat is not vulnerability.

## Slide 21 — Risk + CIA Triad
**Risk story:**
`Asset + Threat + Vulnerability → possible loss / Risk`

Introduce CIA:
- Confidentiality — 誰可以看？
- Integrity — 誰可以改？
- Availability — 需要時能不能用？

**Visual:** thief story on left, cybersecurity mapping on right, CIA below.

**Future bridge:** Later governance adds likelihood, impact, controls, treatment and residual risk.

---

# PART G — SEMESTER PROJECT: AI WEATHER SECURITY CENTER

## Slide 22 — One System for the Whole Semester
**On-slide:** `AI Weather Security Center`

**Message:** We do not throw away one mini-project every week. One system grows throughout the semester.

**Visual:** small app gradually becoming a complete security center.

## Slide 23 — Real Data: CWA Open Data
**Architecture:**
`CWA Open Data → Python → FastAPI → Database → Dashboard`

Possible data: temperature, humidity, rainfall, wind, pressure, timestamp.

**Teacher note:** Exact datasets/API details must be verified against current CWA documentation when implementing.

## Slide 24 — BUILD → LEARN → ATTACK → DEFEND → GOVERN
**Semester journey:**
- BUILD — Weather Web App
- LEARN — ML / DL Security Intelligence
- ATTACK — Authorized security validation
- DEFEND — Find → Fix → Test
- GOVERN — Risk → Control → Evidence

**Safety label:** ATTACK means authorized local/VM/Docker/TryHackMe/CTF environments only; public production deployment is not an attack target.

**煥哥:** presenting full semester roadmap.

---

# PART H — AI ENGINEERING TOOLCHAIN

## Slide 25 — From Idea to Working System
**Flow:**
`Idea → Think → Specify → Build → Remember/Verify → Deploy → Validate`

Do not make this a product-logo collection. Teach roles first.

## Slide 26 — Who Does What?
**Role mapping:**
- ChatGPT / Gemini → Think, understand, design, explain
- Prompt / YAML → Specify requirements
- Antigravity / Codex → Build with coding agents
- GitHub → Version + Memory + Evidence + Documentation
- Vercel → Deploy secure demo
- Authorized Lab → Security validation

**Human:** Understand + Decide + Verify.

## Slide 27 — Agentic Engineering Loop
**Flow:**
`Read Repo → Plan → Code → Run → Test → Review → Fix`

Optional Multi-Agent roles:
Architect → Builder → Security Reviewer → Test Agent.

**Key message:** AI proposes; human understands; tests/evidence verify.

---

# PART I — AIIS_L0_LAB01: SECURITY EVENT ANALYZER

## Slide 28 — Your First AI-Assisted Security Program
**Input:**
`login_success / login_failed`

**Goal:** count events and warn when failed login count ≥ 3.

**Workflow:**
`Human Idea → YAML → Antigravity → Python → Run → Test → GitHub`

## Slide 29 — Give AI a Specification, Not Just a Wish
Show condensed YAML sections:
- task
- learning_objectives
- requirements
- security_requirements
- tests
- deliverables
- final_report

**Teacher point:** Good AI engineering starts with explicit requirements and acceptance criteria.

## Slide 30 — Run → Test → Evidence
Required cases:
- 1 success → no warning
- 2 failures → no warning
- 3 failures → warning
- 5 failures → warning

**Visual:** test table with PASS indicators.

**Key:** “AI generated it” is not evidence. Passing specified tests is evidence for the specified behavior.

## Slide 31 — But Is the Rule Intelligent?
**Scenario A:** legitimate user mistypes password 3 times → warning → False Positive.

**Scenario B:** attacker tries once every 10 minutes → simple count may miss it.

**Question:**「程式測試全部 PASS，是否代表偵測方法就是正確的？」

Answer: No. Tests can prove implementation matches the current specification; they do not prove the specification models reality well.

**Bridge:** Time Window → Features → ML → Sequence Analysis.

---

# PART J — CLOSING

## Slide 32 — The AIIS Journey Starts Here
**Visual:**
`Machine → Energy → Information → Intelligence`
↓
`ANI → Discriminate → Generate → Act`
↓
`Security Matters`
↓
`AI Weather Security Center`
↓
`BUILD → LEARN → ATTACK → DEFEND → GOVERN`

**Final statements:**
- `AI is the capability. Information Security is the discipline.`
- `AI proposes. Human understands. Security validates.`
- `Learn it in the Range. Prove it in our Lab. Fix it in our Code.`

**煥哥:** confident closing/open-hand pose.

**Next:** AIIS_L1 — AI Tools × Prompt × Vibe Coding × Antigravity × GitHub.

---

# Timing Recommendation

| Section | Slides | Approx. time |
|---|---:|---:|
| Opening + Revolutions | 1–6 | 25 min |
| AI Revolution + AI capabilities | 7–14 | 30 min |
| Security turn + fundamentals | 15–21 | 30 min |
| Semester project + toolchain | 22–27 | 25 min |
| Lab | 28–31 | 45–60 min |
| Closing | 32 | 5 min |

Total: approximately 160–175 minutes including interaction and lab.

# Required Teaching Contract

Every substantial section should preserve:
1. Concept
2. Security Meaning
3. Practical Example / Lab
4. Antigravity YAML Prompt where appropriate
5. Run / Test / Review / Evidence
6. Reflection

Engineering loop:
`Understand → Generate → Review → Execute → Verify`

# Scope Guard

AIIS_L0 must NOT expand into a survey of every AI topic or cybersecurity technology. Its job is to establish the worldview, shared vocabulary, semester project, safety boundary, AI-assisted engineering workflow, and first executable lab. Detailed tools and implementation belong to later lessons.
