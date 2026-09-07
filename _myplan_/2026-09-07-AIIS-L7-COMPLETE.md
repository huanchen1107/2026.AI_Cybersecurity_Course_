# AIIS_L7 — COMPLETE

Date: 2026-09-07
Lesson: Supervised ML III — Security Evaluation
Status: COMPLETE

## Canonical lesson question

> Accuracy 95% 就代表模型適合拿來做資安判斷嗎？

## Core transformation

```text
MODEL SCORE
→ MODEL EVIDENCE
→ ERROR TYPE
→ SECURITY CONSEQUENCE
→ ENGINEERING DECISION
```

## Completed slide range

S00–S27, 28 slides total.

## Required concepts covered

- Accuracy limitation
- class imbalance intuition
- Confusion Matrix
- TP / TN / FP / FN
- Precision
- Recall
- F1
- False Positive / False Negative security consequences
- scenario-dependent error cost
- scikit-learn metrics
- sealed TEST-set evaluation
- classification_report
- human security interpretation
- AI-assisted review
- engineering recommendation

## Primary lab

Evaluate the existing L6 Random Forest classifier using the sealed TEST set and produce:

1. confusion matrix
2. Precision / Recall / F1
3. FP / FN interpretation
4. security consequence statement
5. deployment/review recommendation
6. AI-review note

## Evidence artifact

`AIIS_L7_SECURITY_EVALUATION` evidence package.

## Continuity

```text
L5 — TRAIN
L6 — EXPLAIN
L7 — EVALUATE
L8 — INTEGRATE / MIDTERM REVIEW
```

## Detailed planning files

- `2026-09-07-AIIS-L7-Security-Evaluation-Plan-and-Slides-S00-S06.md`
- `2026-09-07-AIIS-L7-Teaching-Script-S07-S13.md`
- S14–S20 detailed teaching-script batch
- `2026-09-07-AIIS-L7-Teaching-Script-S21-S27.md`
- `2026-09-07-AIIS-L7-Content-Driven-Visual-Audit-S00-S27.md`

## Further Exploration only

- ROC-AUC
- Precision–Recall curve
- threshold tuning
- calibration
- cost-sensitive learning

These are deliberately not expanded into the core lesson.

## Final message

> Accuracy is a number. Security is a decision.

AIIS_L7 planning is complete and ready for downstream PPT / NotebookLM generation and L8 integration.