# AIIS_L5 — Final Content-Driven Visual Audit（S00–S22）

Date: 2026-09-07
Status: FINAL AUDIT PASS
Mission: LEARN — CRISP-DM × Security Classification Foundations.
Core tool: scikit-learn.
Representative model: Logistic Regression only.
Canonical storyline: `Security Problem → CRISP-DM → Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation Preview → Deployment Preview → Weather Security Center`.

This audit validates the existing `AIIS-L5-Huange-Visual-Interaction-Spec-S00-S22.md` against the final course-wide Content-Driven Visual rule.

## S00–S05 — Why ML / CRISP-DM / Problem framing
- S00 Secure Software → Learning System — PASS. Security Engineer→Data Scientist transition is content-driven; Security Data physically flows from existing Weather Security Center into ML model. Critical continuity with L4.
- S01 Too much security data — PASS. SOC Analyst is overwhelmed by increasing event volume but selects a few cases; visual expresses scale/problem before ML solution.
- S02 Don't start with algorithm — PASS. STOP gesture physically blocks algorithm toolbox and redirects attention to PROBLEM. Prevents tool-first thinking.
- S03 CRISP-DM map — PASS. Expedition Guide actively uses six-phase map/compass; establishes recurring course map rather than decorative cycle diagram.
- S04 Business Understanding — PASS. Problem Framer crosses out vague `AI Cybersecurity System` and rewrites a concrete analyst problem. Excellent action-content alignment.
- S05 Security Problem → ML Problem — PASS. Translation bridge makes abstraction conversion visible: `events too many → observation → classifier → normal/suspicious`.

## S06–S12 — Data Understanding / Preparation
- S06 Data Understanding — PASS / ANCHOR. Magnifier must stay aimed at a real dataset value (`requests/min=160`), with Missing?/Correct?/Trustworthy? questions. This is the canonical Data Detective page.
- S07 Observation — PASS. Pulling one row out of full dataset directly teaches `one row = one observation/sample`.
- S08 Feature X — PASS. Clue cards enter X folder while label is physically blocked. Strong anti-leakage visual seed.
- S09 Label y — PASS. Answer card is revealed separately from X; explicitly shows known target during training.
- S10 Data Preparation — PASS. Raw Data is operated through Select/Clean/Encode pipeline; character performs transformation rather than observing.
- S11 Clean/Select/Encode — PASS / ANCHOR. Remove irrelevant ID, repair missing, encode values, and keep label outside X. This page should visually callback S08 label-blocking.
- S12 Train/Test Split — PASS / ANCHOR. Exam Proctor seals TEST set; `DO NOT OPEN DURING TRAINING` must remain visible through S16.

## S13–S18 — Modeling / Prediction
- S13 Modeling — PASS. Model toolbox opens only after prior CRISP-DM phases are checked; contains Logistic Regression only, enforcing one-tool-per-lesson rule.
- S14 Rule-based vs Learning — PASS. Same Huange split into two roles; difference is embodied by who defines decision logic. Avoid turning this into algorithm comparison table.
- S15 First Classifier — PASS. `LogisticRegression()` cube remains marked UNTRAINED; creation ≠ learning.
- S16 model.fit() — PASS / ANCHOR. X_train + y_train feed model while TEST remains sealed in background. Critical callback to S12.
- S17 model.predict() — PASS. Unlabeled observation enters trained model; Ground Truth stays covered. Clean distinction training vs inference.
- S18 First Security Prediction — PASS / ANCHOR. Model returns SUSPICIOUS; analyst reviews instead of blocking/convicting. Prevents overclaiming AI authority.

## S19–S22 — Evaluation / Deployment / Integration
- S19 Evaluation Preview — PASS. `RUNNING ✓` vs `RELIABLE ?` creates correct transition without stealing L7 full evaluation lesson.
- S20 Prediction ≠ Truth — PASS. Huange compares Prediction card with Ground Truth and marks match/mismatch; visual introduces evaluation without metric overload.
- S21 Deployment Preview — PASS. Integration Engineer connects Feature Preparation→Model→Prediction→Analyst Review; deployment is workflow integration, not merely uploading `.py`.
- S22 Return to Weather Security Center — PASS / ANCHOR. System Architect inserts ML-assisted triage into the existing Weather Security Center, preserving Human Analyst. This closes the course-project loop and avoids toy-notebook framing.

## Mandatory visual callbacks
1. S00 existing secured system → S22 same system with ML-assisted triage.
2. S03 CRISP-DM map → phase markers on S04/S06/S10/S13/S19/S21.
3. S08 label blocked from X → S11 label still outside X.
4. S12 sealed TEST → S16 TEST remains sealed during fit.
5. S15 UNTRAINED → S16 TRAINED → S17 PREDICTION.
6. S18 Analyst Review → S22 Human Analyst remains in deployed workflow.
7. S19 `RELIABLE ?` → S20 compare Prediction vs Ground Truth.

## Final audit result
23/23 slides (S00 + S01–S22) PASS the Content-Driven Visual standard.
No slide requires generic decorative Huange.

### Highest-priority visual anchor slides
S00, S03, S06, S08, S11, S12, S16, S18, S20, S22.

### Freeze rule
L5 visual design is ready to Freeze only if the PPT generator preserves:
- same Huange identity;
- slide-specific role/expression/action/prop;
- direct manipulation of the core teaching object;
- the seven cross-slide callbacks above;
- Logistic Regression as the only representative model;
- Human Analyst in the final security workflow.

## Failure conditions
- repeated standing/talking avatar;
- generic AI brain graphics replacing dataset/model interaction;
- label accidentally shown inside Feature X;
- TEST set shown entering `.fit()`;
- prediction shown as confirmed attack/truth;
- deployment shown as only server/upload icon;
- S22 becomes a separate ML notebook instead of returning to Weather Security Center;
- introducing Random Forest/XGBoost/Neural Network as additional lesson implementations.

Conclusion: AIIS_L5 visual specification is consistent with the course-wide L1-style Content → Visual design method and can serve as the strongest ML-lesson reference for L6–L8.