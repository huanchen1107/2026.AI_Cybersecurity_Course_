# AIIS_L7 — Teaching Script S21–S27

Date: 2026-09-07
Status: FINAL SLIDE BATCH
Lesson: Supervised ML III — Security Evaluation
Continuation: S00–S20
Primary tool: scikit-learn metrics
Persistent project: AI Weather Security Center / L5–L6 security classifier

---

# Batch Mission

The final batch converts evaluation knowledge into an engineering artifact.

```text
KNOW THE METRICS
      ↓
RUN THE LAB
      ↓
READ THE EVIDENCE
      ↓
EXPLAIN THE SECURITY CONSEQUENCE
      ↓
USE AI AS REVIEW ASSISTANT
      ↓
MAKE A HUMAN ENGINEERING DECISION
      ↓
PACKAGE THE EVIDENCE
      ↓
L8 MIDTERM INTEGRATION
```

The student must leave L7 with more than a score. The deliverable is a defensible security-evaluation statement supported by model evidence.

---

## S21 — LAB Mission: Is Our Classifier Safe Enough?

### On-screen mission card
> **LAB：評估 L6 的 Random Forest，並回答：它是否適合這個資安情境？**

### Required outputs
```text
1. Confusion Matrix
2. Precision
3. Recall
4. F1
5. FP / FN interpretation
6. Engineering recommendation
```

### Visual composition
Mission-control screen showing the existing L6 Random Forest artifact entering an `EVALUATION GATE`. Six evidence slots are initially empty.

Huange avatar holds a clipboard rather than a coding pose: 「今天不是再訓練一次，而是審查模型。」

### Teacher narration
「L5 我們把 classifier train 出來，L6 我們理解 Tree / Random Forest 怎麼做決策。今天最後一段，你們要扮演的是模型審查者。」

「不能只交 Accuracy，也不能只貼一張 confusion matrix。你必須把數字翻譯成 security consequence。」

### Lab rule
Use the same sealed TEST set. Do not retrain based on test results during the evaluation step.

### Student takeaway
Evaluation is an evidence-producing engineering task.

---

## S22 — LAB Workflow: Predict → Measure → Interpret → Decide

### On-screen workflow
```text
L6 trained model
      ↓
y_pred = model.predict(X_test)
      ↓
confusion_matrix(y_test, y_pred)
      ↓
classification_report(y_test, y_pred)
      ↓
Security Interpretation
      ↓
Recommendation
```

### Minimal code panel
```python
from sklearn.metrics import confusion_matrix, classification_report

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))
```

### Visual composition
A left-to-right pipeline with actual artifacts, not a full IDE screenshot. Code appears only in the measurement stage.

### Teacher narration
「注意，程式碼其實非常短。這堂課真正困難的地方不是把 function 打出來，而是後面的 interpretation。」

「AI 很容易幫你產生這幾行 code，但它不能替你決定這個情境能不能接受 20 個 False Negatives。」

### Vibe Coding / AI connection
Students may ask an AI assistant to explain API syntax or an error message, but must preserve:
- correct `y_test`
- correct `y_pred`
- positive-class meaning
- sealed test-set discipline

### Misconception guard
Do not let AI silently swap label meaning. Confirm which label represents `ATTACK` before interpreting metrics.

---

## S23 — LAB Evidence Board: Numbers Need Meaning

### On-screen template
```text
MODEL EVALUATION EVIDENCE

Confusion Matrix: ______
Precision:        ______
Recall:           ______
F1:               ______

False Positives mean: __________________
False Negatives mean: __________________

Most concerning error: _________________
Because: _______________________________
```

### Visual composition
A forensic evidence board with metric cards connected to operational consequences. Avoid decorative crime-scene clichés; maintain professional cyber-engineering style.

### Teacher narration
「這一頁就是你們真正要交的核心。」

「如果你只寫 `Recall = 0.82`，那還只是 machine-learning output。你還要寫：剩下沒有抓到的 Attack 對我們這個系統代表什麼。」

### Required interpretation language
Students should be able to write sentences such as:

> The model has high overall accuracy, but the false negatives show that some malicious events are still classified as normal. For this detection scenario, those missed attacks require further mitigation or human review.

### Student takeaway
A metric becomes useful only when connected to a security consequence.

---

## S24 — AI-Assisted Review: Ask AI to Challenge Your Conclusion

### On-screen hero
> **不要只叫 AI 幫你寫答案；叫 AI 挑戰你的答案。**

### Recommended prompt
```text
You are reviewing a cybersecurity classifier.

Context:
- Positive class = ATTACK
- Confusion matrix = [paste result]
- Precision = [value]
- Recall = [value]
- F1 = [value]
- Security scenario = [describe scenario]

Do NOT decide deployment for me.

1. Explain the false-positive and false-negative consequences.
2. Identify weaknesses in my interpretation.
3. Ask me three questions I should answer before deployment.
4. Separate facts from assumptions.
```

### Visual composition
Student engineer and AI reviewer face the same evidence board. AI is shown as a review assistant with question marks, not as an autonomous decision maker.

### Teacher narration
「這裡就是我們課程所說的 AI for Security。」

「AI 可以幫我們看有沒有漏掉觀點、挑戰假設、把 metric 翻成比較容易理解的語言。但是最後的 security objective、風險容忍度與部署決策，仍然是工程責任。」

### Interaction
Students compare their original conclusion with AI's challenges and mark:
- one point AI clarified
- one point AI assumed incorrectly
- one question requiring human/domain knowledge

### Guardrail
Never paste secrets, credentials, personal data, or restricted production logs into an external AI service.

---

## S25 — Evidence Package: What You Submit

### On-screen artifact
> **L7 Evidence Package**

```text
□ Model / dataset identification
□ TEST-set confirmation
□ Confusion Matrix
□ Precision / Recall / F1
□ FP security consequence
□ FN security consequence
□ Recommended action
□ AI-review note
```

### Recommended action choices
```text
DEPLOY
DEPLOY WITH HUMAN REVIEW
IMPROVE / VALIDATE FIRST
```

Students may propose another action if justified.

### Visual composition
A clean evidence-folder graphic labeled `AIIS_L7_SECURITY_EVALUATION`, containing screenshot/chart, metrics report, interpretation note and recommendation.

### Teacher narration
「你交的不是一個漂亮分數，而是一個可被別人 review 的 evidence package。」

「如果下一個工程師問：『你為什麼說這個模型可以用？』，他應該可以從這份 evidence 找到你的理由。」

### Evidence quality rubric
A strong submission:
- uses the correct test data
- labels positive class explicitly
- reports metrics accurately
- distinguishes FP and FN
- connects errors to the scenario
- avoids claiming metrics prove absolute safety
- states recommendation with rationale

---

## S26 — L5 → L6 → L7: We Now Have a Complete ML Security Story

### On-screen storyline
```text
L5 — TRAIN
How do we build a classifier?

        ↓

L6 — EXPLAIN
How does the classifier decide?

        ↓

L7 — EVALUATE
How good — and how safe — are those decisions?
```

### Evidence chain
```text
Dataset
  → Features / Labels
  → Train/Test Split
  → Random Forest
  → Feature Importance
  → Predictions
  → Confusion Matrix
  → Precision / Recall / F1
  → Security Interpretation
```

### Visual composition
One continuous horizontal ML engineering journey using the same artifact from L5 through L7. Avoid three disconnected chapter cards.

### Teacher narration
「到這裡，三堂監督式學習不是三個獨立 demo。」

「L5 建立模型；L6 打開模型的決策邏輯；L7 檢查這些決策的品質與風險。」

「這才是一個完整的 AI Security Engineering workflow。」

### Student reflection
Ask students to finish one sentence:

> Before L7, I thought a good model meant ________. Now I would also check ________.

---

## S27 — Closing: Accuracy Is a Number. Security Is a Decision.

### Hero statement
> **Accuracy is a number. Security is a decision.**

### Supporting line
```text
Measure the model.
Understand the errors.
Explain the consequence.
Then make the decision.
```

### Visual composition
Final hero scene: Weather Security Center dashboard with a model-evaluation panel. Huange stands between an AI model icon and a shielded operational system, holding the evidence report. The human is visibly the decision point.

### Teacher closing narration
「今天最重要的不是 Precision、Recall、F1 三個英文單字。」

「真正要帶走的是：AI 模型產生的是 prediction，metrics 產生的是 evidence，而 security engineer 要把 evidence 變成 decision。」

「所以以後看到 95%、99%，第一個問題不要是『高不高？』，而是：」

> **錯在哪裡？漏掉什麼？代價是什麼？**

### L8 handoff
```text
NEXT: AIIS_L8 — Midterm AI Security Engineering Review

BUILD evidence
+ ML evidence
+ Security reasoning
→ Integrated engineering review
```

### Exit ticket
Students answer three items before leaving:

1. Precision answers what security question?
2. Recall answers what security question?
3. In your classifier scenario, which error worries you more, and why?

---

# L7 Complete Storyline

```text
S00  The 95% Trap
S01  Train → Explain → Evaluate
S02  10,000-event scenario
S03  Accuracy Trap
S04  Wrong Is Not Just Wrong
S05  Four Boxes
S06  Confusion Matrix
S07  Precision concept
S08  Precision calculation
S09  Recall concept
S10  Recall calculation
S11  Precision vs Recall
S12  Security trade-off
S13  F1
S14  Bring Back L6 Random Forest
S15  Predict on sealed TEST set
S16  confusion_matrix
S17  classification_report
S18  Translate metrics into security language
S19  Compare model/error profiles
S20  Deployment decision
S21  Lab mission
S22  Lab workflow
S23  Evidence board
S24  AI-assisted review
S25  Evidence package
S26  L5 → L6 → L7 synthesis
S27  Closing + L8 handoff
```

---

# L7 Learning Outcome Check

At the end of L7, students can:

1. Explain why Accuracy alone may be misleading in cybersecurity.
2. Read TP, TN, FP and FN from a confusion matrix.
3. Explain Precision as alarm trustworthiness.
4. Explain Recall as coverage of actual attacks.
5. Explain the operational meaning of false positives and false negatives.
6. Use F1 as a combined summary without treating it as a complete security decision.
7. Use scikit-learn metrics to evaluate the existing L6 classifier.
8. Translate model outputs into security consequences.
9. Use AI as a reviewer rather than an unquestioned decision maker.
10. Produce a reviewable evidence package and recommendation.

---

# Scope Guardrail

L7 intentionally stops here.

Further Exploration only:
- ROC-AUC
- Precision–Recall curve
- threshold tuning
- calibration
- cost-sensitive learning

These topics may be named on an optional extension slide or instructor note but must not displace the core L7 lab.

---

# Final Lesson Message

```text
MODEL SCORE
    ↓
MODEL EVIDENCE
    ↓
ERROR TYPE
    ↓
SECURITY CONSEQUENCE
    ↓
ENGINEERING DECISION
```

This is the canonical AIIS_L7 learning transformation.