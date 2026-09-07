# AIIS_L7 — Teaching Script S14–S20

Date: 2026-09-07
Status: IN PROGRESS
Lesson: Supervised ML III — Security Evaluation
Continuation: S00–S13 Accuracy → Confusion Matrix → Precision → Recall → F1
Primary tool: scikit-learn metrics
Persistent artifact: L6 Random Forest + sealed TEST set

---

# Batch Mission

This batch moves from understanding metrics to producing model evidence.

```text
L6 Random Forest
      ↓
Sealed TEST Set
      ↓
predict()
      ↓
confusion_matrix
      ↓
classification_report
      ↓
security interpretation
      ↓
model decision
```

The core teaching rule is:

> **Metrics are not decoration after training. They are evidence used to make a security decision.**

---

## S14 — Bring Back the L6 Random Forest

### On-screen title
**No New Model Today**

### On-screen content
```python
rf_model
X_test
y_test
```

Hero statement:
> **Same model. Same TEST set. New question: Can we trust it?**

### Visual composition
Show the L6 Random Forest model artifact physically returning to the center of the lesson. Beside it is the sealed TEST-set box from L5–L6. No new dataset appears.

### Teacher narration
「前面我們已經把 Precision、Recall、F1 的意思弄清楚了。現在不再做紙上例題，直接把 L6 的 Random Forest 拿回來。」

「今天最重要的習慣是：**不要因為換了一堂課，就重新切一份 TEST data。** 我們要維持同一份 sealed TEST set，才能讓評估有一致性。」

### Student takeaway
Evaluation reuses the trained model and untouched TEST set.

### Misconception guard
Do not call `.fit()` again on the TEST set.

### Handoff
「第一步非常簡單：先讓模型對 TEST set 做 prediction。」

---

## S15 — Predict on the Sealed TEST Set

### On-screen code
```python
y_pred = rf_model.predict(X_test)
```

Then:

```text
Ground Truth: y_test
AI Prediction: y_pred
```

### Visual composition
A pipeline with two parallel rails:
- Reality rail = `y_test`
- AI rail = `y_pred`

Both enter an `EVALUATION` gate.

### Teacher narration
「這一行程式本身很簡單，但概念很重要。`y_test` 是答案，`y_pred` 是模型的回答。」

「接下來所有評估，其實都是在比較這兩個東西。」

### Board statement
```text
Evaluation = compare reality with prediction
```

### Student takeaway
All classification metrics derive from comparing actual labels with predictions.

### Interaction
Ask students: Which object is ground truth? Which object is the model's output?

---

## S16 — Build the Confusion Matrix with scikit-learn

### On-screen code
```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
```

Example output:

```text
[[TN  FP]
 [FN  TP]]
```

### Visual composition
Left: tiny code panel.
Center/right: code output morphs into the familiar S06 2×2 security matrix. The visual should explicitly connect programming output to concept.

### Teacher narration
「現在你會發現，前面學的四格不是額外知識，它會直接從程式輸出。」

「`confusion_matrix(y_test, y_pred)` 就是拿真實答案跟模型預測去建立四種結果。」

### Critical caution
Depending on label ordering, students must confirm which class is treated as positive. Do not blindly assume matrix semantics without checking label encoding.

### Teacher note
If labels are `0 = Normal`, `1 = Attack`, explain the conventional binary layout:

```text
[[TN, FP],
 [FN, TP]]
```

### Student takeaway
Students can connect scikit-learn output to TP/TN/FP/FN.

### Interaction
Give one example matrix and ask students to identify how many attacks were missed.

---

## S17 — classification_report: One Command, Several Metrics

### On-screen code
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

Representative structure:

```text
              precision  recall  f1-score  support
Normal           ...       ...      ...       ...
Attack           ...       ...      ...       ...
```

### Visual composition
Do not show a full terminal dump as the only visual. Highlight the `Attack` row and annotate three questions above it:

```text
precision → 警報可信嗎？
recall    → 攻擊抓得住嗎？
f1-score  → 兩者綜合如何？
```

### Teacher narration
「`classification_report` 很方便，一次把 Precision、Recall、F1 都整理出來。」

「但這也帶來一個危險：學生很容易把它當成『把表貼進報告就結束』。」

「真正的任務是：你能不能把這一列數字翻譯成安全語言？」

### Student takeaway
A metric table is evidence, not interpretation.

### Misconception guard
Do not focus only on weighted average or macro average before students can interpret the target Attack class.

---

## S18 — Translate Metrics into Security Language

### On-screen template
Students must complete sentences, not only copy numbers.

```text
Attack Precision = ____
Meaning: When the model predicts ATTACK, __________.

Attack Recall = ____
Meaning: Of all actual attacks, __________.

False Negatives = ____
Security implication: __________.
```

### Visual composition
A transformation pipeline:

```text
NUMBER → SENTENCE → SECURITY CONSEQUENCE
```

Huange avatar rejects a report that contains only `0.91 / 0.84 / 0.87`, then approves a report containing an interpretation.

### Teacher narration
「這一頁是今天非常重要的一頁。」

「工程師的價值不是把 `classification_report` 複製貼上，而是說清楚：這些數字對系統意味著什麼。」

Example narration:

> 「Attack Recall = 0.84，表示測試集中真正的攻擊約 84% 被模型偵測到；仍有約 16% 的攻擊落入 False Negative，需要評估這種漏偵測在本系統是否可接受。」

### Student takeaway
Every important metric should be tied to operational meaning.

### Interaction
Give students a sample Recall value and ask them to write one security sentence.

---

## S19 — Same Accuracy, Different Risk

### On-screen scenario
Two hypothetical model profiles:

```text
MODEL A
Accuracy: 95%
Attack Recall: 62%
False Negatives: high

MODEL B
Accuracy: 94%
Attack Recall: 91%
False Positives: somewhat higher
```

Question:
> **Which one is better?**

### Visual composition
Two model cards with nearly identical Accuracy badges. Underneath, show completely different error profiles. The Accuracy numbers should visually look similar; the FP/FN consequences should visually look dramatically different.

### Teacher narration
「這就是為什麼我們花一整堂課講 Accuracy 以外的東西。」

「Model A 的 Accuracy 還比較高，但漏掉很多攻擊。Model B 整體 Accuracy 少一點，可是抓攻擊的能力明顯比較高。」

「現在不能只問哪個數字最大，而要問：**我們的系統到底怕什麼？**」

### Important teaching point
Do not automatically declare Model B the winner. Ask about scenario:
- Is this only an advisory detector?
- Does every alert trigger an expensive automatic block?
- What is the cost of a missed attack?
- What is the cost of a false alarm?

### Student takeaway
Model ranking depends on error profile and system objective, not a single universal metric.

---

## S20 — Deployment Decision: Would YOU Trust This Model?

### On-screen challenge
> **You are the Security Engineer. Make the call.**

Students receive:
- confusion matrix
- Accuracy
- Precision
- Recall
- F1
- FP count
- FN count

They must choose one:

```text
A. Accept for current use
B. Accept only as human-review support
C. Needs improvement before use
```

And complete:

```text
My decision: __________
Primary evidence: __________
Most dangerous error: __________
Why: __________
```

### Visual composition
Security engineering decision board with three deployment lanes:
`Deploy`, `Human Review`, `Improve First`.

Huange/teacher avatar stands beside the board but does not point to one correct answer.

### Teacher narration
「現在你已經不是在做計算題，而是在做工程判斷。」

「我不要求全班一定選同一個答案。我要看的是：你的答案有沒有 evidence，有沒有把 FP/FN 的安全後果說清楚。」

「這也是 AI Security Engineer 和只會跑 notebook 最大的差別之一。」

### Student takeaway
A defensible deployment recommendation must cite evidence and scenario-specific risk.

### Evidence artifact seed
This decision becomes part of the L7 evidence package.

### Handoff
「下一段我們要把這個判斷正式整理成 Lab Evidence：不只讓程式跑完，而是讓別人能檢查你的結論。」

---

# S14–S20 Code Skeleton

```python
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
)

# Reuse the model trained in L6
# Do not fit on X_test / y_test

y_pred = rf_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(cm)
print(classification_report(y_test, y_pred))
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)
```

If the positive class is not encoded as `1`, explicitly set the appropriate `pos_label` or labels rather than silently producing a misleading interpretation.

---

# S14–S20 Visual Rhythm Audit

```text
S14 artifact continuity
S15 dual-track reality vs prediction
S16 code → confusion matrix transformation
S17 report highlighting
S18 number → language → consequence
S19 model comparison
S20 engineering decision board
```

The lab/code portion must not become seven terminal screenshots.

---

# Planned Final Batch S21–S27

```text
S21 Lab Mission Brief
S22 Lab Step 1 — Generate Evaluation Evidence
S23 Lab Step 2 — Inspect FP and FN
S24 Lab Step 3 — Write Security Interpretation
S25 AI-assisted Review Without Outsourcing Judgment
S26 Evidence Package + L8 Handoff
S27 Closing — Accuracy Is Not Enough
```

After S21–S27, create:
- Content-Driven Visual Audit
- L7 COMPLETE artifact
- concise Lesson7 README alignment if needed
