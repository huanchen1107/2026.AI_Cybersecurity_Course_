# AIIS_L7 — Content-Driven Visual Audit S00–S27

Date: 2026-09-07
Lesson: Supervised ML III — Security Evaluation
Audit target: S00–S27
Status: PASS WITH DESIGN REQUIREMENTS

## Audit Principle

Visuals must explain the security meaning of evaluation metrics. Do not convert the lesson into 28 similarly styled text cards or formula pages.

Canonical visual rhythm:

```text
HOOK → SCENARIO → CONTRADICTION → ERROR STORIES → MATRIX
→ ALARM TRUST → ATTACK CAPTURE → TRADE-OFF → MODEL EVIDENCE
→ ENGINEERING DECISION → LAB → REVIEW → SYNTHESIS
```

## Slide-by-slide visual intent

| Slide | Primary visual | Teaching function |
|---|---|---|
| S00 | 95% badge + one missed malicious event | create doubt |
| S01 | L5→L6→L7 artifact journey | continuity |
| S02 | 10,000-event population | class imbalance intuition |
| S03 | 99% vs 100 missed attacks contradiction | break Accuracy intuition |
| S04 | false alarm vs missed attack stories | human consequence |
| S05 | empty 2×2 matrix | student construction |
| S06 | completed confusion matrix | formal model |
| S07 | SOC alarm queue | Precision meaning |
| S08 | countable alarm tiles | Precision calculation |
| S09 | attackers approaching gate | Recall meaning |
| S10 | caught vs escaped attackers | Recall calculation |
| S11 | two evaluation lenses | compare questions |
| S12 | sensitivity dial | trade-off intuition |
| S13 | balance scale | F1 synthesis |
| S14 | L6 model artifact returning | project continuity |
| S15 | sealed TEST set pipeline | evaluation discipline |
| S16 | matrix generated from predictions | tool-to-concept bridge |
| S17 | classification report with highlighted attack row | read tool output |
| S18 | metric → consequence arrows | interpretation |
| S19 | two error-profile dashboards | comparison |
| S20 | engineering decision gate | judgment |
| S21 | lab mission-control board | task framing |
| S22 | predict→measure→interpret→decide pipeline | lab execution |
| S23 | evidence board | artifact construction |
| S24 | human + AI reviewer | AI-assisted critique |
| S25 | evidence package folder | submission clarity |
| S26 | continuous L5→L7 workflow | synthesis |
| S27 | human decision point between model and system | closing message |

## Persona / Huange usage

Huange should not appear on every slide. Use only when the persona performs a meaningful teaching role:

- S00: points to missed attack
- S07: questions alarm trust
- S14: brings L6 model artifact back
- S21: acts as model-review lead
- S24: compares human judgment with AI review
- S27: holds evidence at decision point

Expressions/poses must follow content:
- skeptical at S00
- overloaded/concerned at alarm-fatigue examples
- analytical during evaluation
- reviewer posture during lab
- confident but evidence-focused at closing

## Formula-density rule

Formula-first slides are prohibited.

Required sequence:

```text
security question → visual story → plain-language meaning → formula
```

Precision, Recall and F1 formulas must remain visually subordinate to the security question.

## Confusion-matrix consistency

Throughout L7:

- Positive class = ATTACK
- Negative class = NORMAL
- TP = attack caught
- FN = attack missed
- FP = false alarm
- TN = normal correctly passed

Matrix orientation must remain consistent once introduced. Never rotate Actual/Predicted axes between slides.

## Security-cost nuance

Visuals must NOT imply:

`FN is always worse than FP.`

Instead show scenario dependence:
- false positives can cause alert fatigue, unnecessary blocking, operational disruption
- false negatives can allow malicious activity through
- engineering priority depends on system objective and consequence

## AI depiction rule

S24 must depict AI as a reviewer/challenger, not an autonomous deployment authority.

Required message:

```text
AI can explain, challenge and review evidence.
Human engineers remain responsible for assumptions, risk and deployment decisions.
```

## Lab visual rule

S21–S25 should look like one continuous evidence-building activity. Reuse the same evaluation-board visual language so students perceive one workflow rather than five unrelated slides.

## PPT / NotebookLM batching

Recommended generation batches:

```text
Batch A: S00–S13
Batch B: S14–S27
```

For Batch B prompt explicitly include:

> Continue the exact visual system, typography, color palette, persona appearance and layout logic established in Batch A. Do not repeat S00–S13 content. Generate only S14–S27.

If generation quality drops, use three batches:

```text
S00–S09
S10–S18
S19–S27
```

## Final audit result

PASS if final deck preserves:
- one coherent security story
- same L5/L6 project continuity
- varied content-driven visuals
- stable confusion-matrix semantics
- low formula density
- human-centered security interpretation
- clear evidence artifact
- direct L8 handoff

Reject/regenerate any slide that becomes generic decorative cybersecurity imagery without carrying the specific concept of that page.