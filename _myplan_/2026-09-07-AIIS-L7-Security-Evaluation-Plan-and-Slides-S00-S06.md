# AIIS_L7 — Supervised ML III: Security Evaluation

Date: 2026-09-07
Status: IN PROGRESS — Storyline + S00–S06
Phase: LEARN
Primary tool: scikit-learn metrics
Persistent project: AI Weather Security Center / security-classification dataset and Random Forest from L5–L6
Design standard: `_myplan_/AIIS-COURSE-DESIGN-STANDARD.md`

---

# 1. Lesson Position

```text
L5 — HOW DO WE TRAIN A CLASSIFIER?
        ↓
L6 — HOW DOES THE CLASSIFIER DECIDE?
        ↓
L7 — HOW GOOD — AND HOW SAFE — ARE THOSE DECISIONS?
```

L7 does not introduce another major model. Students reuse the classifier and TEST-set discipline from L5–L6 and learn how to judge whether model errors are acceptable for a cybersecurity task.

Central question:

> **「模型 Accuracy 95%，就代表它適合拿來做資安判斷嗎？」**

Answer students should discover:

> **Not necessarily. In cybersecurity, which cases the model gets wrong can matter more than the overall percentage it gets right.**

---

# 2. One Primary Mission

Students will evaluate an existing security classifier using a confusion matrix, Precision, Recall and F1; distinguish False Positive from False Negative; and explain which error is more costly in a concrete security scenario.

By the end of L7, a student should be able to move from:

```text
MODEL SCORE
```

to:

```text
MODEL EVIDENCE
→ ERROR TYPE
→ SECURITY CONSEQUENCE
→ ENGINEERING DECISION
```

---

# 3. Boundary

## THIS LESSON OWNS

- why Accuracy can mislead
- class imbalance intuition
- confusion matrix
- True Positive / True Negative
- False Positive / False Negative
- Precision
- Recall
- F1 score
- security cost of FP/FN
- `confusion_matrix`
- `classification_report`
- `precision_score`, `recall_score`, `f1_score`
- human interpretation of metrics
- evidence-backed model evaluation

## THIS LESSON PREVIEWS BUT DOES NOT DEEPLY TEACH

- ROC-AUC
- Precision–Recall curve
- threshold tuning
- probability calibration
- cost-sensitive learning

## THIS LESSON DOES NOT OWN

- a new classifier family
- full statistical learning theory
- advanced mathematical derivations
- broad benchmark competitions
- production SOC/SIEM deployment

---

# 4. PREVIEW → TEACH → REUSE

```text
L5 TEACH: train/test split, classifier, prediction
L6 REUSE: same workflow and TEST discipline
L7 REUSE: same held-out TEST data for evaluation

L6 PREVIEW: accuracy is not enough / false negatives matter
L7 TEACH: confusion matrix → precision → recall → F1 → security cost

L7 OUTPUT:
Evaluation evidence that can be reused in L8 midterm integration.
```

---

# 5. Full Lesson Storyline

```text
A model says: 95% Accuracy
        ↓
IS THAT GOOD?
        ↓
Look at the security scenario
        ↓
Rare attacks + many normal events
        ↓
Accuracy Trap
        ↓
Stop counting only RIGHT / WRONG
        ↓
Ask WHAT KIND of wrong?
        ↓
Confusion Matrix
        ↓
TP / TN / FP / FN
        ↓
False Alarm vs Missed Attack
        ↓
Precision
"When AI raises an alarm, how often is it right?"
        ↓
Recall
"Of the real attacks, how many did AI catch?"
        ↓
Precision ↔ Recall tension
        ↓
F1
        ↓
Security Cost
        ↓
Evaluate L6 Random Forest
        ↓
Human + AI-assisted interpretation
        ↓
Evidence package
        ↓
L8 integration readiness
```

Recommended size: 26–28 slides. S00–S06 establish the problem before formulas appear.

---

# 6. Slide-by-Slide Teaching Script — S00–S06

## S00 — Cover / The 95% Trap

### On-screen title
**AIIS_L7 — Security Evaluation**

### Hero question
> **Accuracy = 95%. Safe enough?**

### Visual composition
A cybersecurity operations screen shows a large green `95% ACCURACY` badge. Behind it, one small red malicious event slips through a security gate unnoticed. Huange/teacher avatar points not at 95%, but at the missed red event.

### Teacher narration
「L5 我們學會讓模型做分類，L6 我們開始看 Random Forest 為什麼這樣判斷。今天先不要再換模型。假設我現在告訴你：我們的資安 AI 準確率 95%。你敢不敢把它接到真正的安全警報系統？」

Pause and let students vote.

「今天整堂課就是要拆掉一個很常見的錯覺：**一個數字很漂亮，不代表安全風險很低。**」

### Student takeaway
Model evaluation is a security decision, not merely a score-reporting exercise.

### Interaction
Quick vote: `95% = 可以上線 / 還不能判斷`.
Do not reveal the full answer immediately.

### Visual rule
The missed attack must be visually small but semantically dominant. This slide should create curiosity, not explain metrics yet.

---

## S01 — Where We Are: Train → Explain → Evaluate

### On-screen content
```text
L5 TRAIN
How do we train a classifier?
        ↓
L6 EXPLAIN
How does it decide?
        ↓
L7 EVALUATE
Can we trust those decisions for this security task?
```

### Visual composition
Three connected workstations or three stations on one security-engineering pipeline. L5 and L6 are marked completed; L7 is highlighted as the current station. The same dataset/model artifact visually travels forward rather than restarting.

### Teacher narration
「今天不是新的 ML 專案。我們把前兩堂的成果直接帶過來。L5 有 dataset、features、labels、train/test split；L6 有 Random Forest。L7 要做的是工程師一定要做的第三件事：**證明這個模型到底表現得怎樣。**」

「所以今天我們不追求『再學一個演算法』，而是學會『怎麼判斷演算法可不可以相信』。」

### Student takeaway
Evaluation is the next stage of the same ML lifecycle.

### Reuse cue
Keep the sealed TEST-set visual language used in L5–L6.

---

## S02 — Scenario: 10,000 Security Events

### On-screen content
**Today: 10,000 security events**

- 9,900 Normal
- 100 Attacks

Question:
> If a model predicts **NORMAL every time**, what is its Accuracy?

### Visual composition
Use a dense field of event tiles: overwhelmingly neutral/normal tiles and a small cluster of 100 red attack tiles. A deliberately lazy AI guard stamps every event `NORMAL`.

### Teacher narration
「我們先不用任何公式。假設今天 Weather Security Center 收到一萬筆事件，其中 9,900 筆正常，只有 100 筆是真正攻擊。」

「現在我做一個全世界最偷懶的 AI：不看資料、不做 Random Forest，所有東西一律回答 NORMAL。請問它 Accuracy 多少？」

Let students calculate.

### Reveal
```text
9,900 / 10,000 = 99%
```

### Teacher punch line
「99%。比剛剛的 95% 還漂亮。但它抓到幾個攻擊？」

### Student answer
`0`.

### Student takeaway
A high Accuracy can coexist with complete security failure.

### Interaction
Students calculate before the 99% reveal.

---

## S03 — The Accuracy Trap

### On-screen content
```text
99% Accuracy
BUT
100 / 100 attacks missed
```

Big statement:
> **Accuracy asks: How many were correct?**
> **Security asks: What did we fail to catch?**

### Visual composition
Split screen. Left: executive dashboard celebrating `99%`. Right: security incident timeline showing all 100 attacks crossing the boundary. Huange avatar turns from the dashboard toward the incident side.

### Teacher narration
「這就是 Accuracy Trap。Accuracy 本身沒有錯；錯的是我們把它當成唯一答案。」

「資安資料很常有不平衡：正常流量很多，真正攻擊比較少。當重要事件本來就很少時，只看總答對率，模型甚至可以靠『一直猜正常』得到很漂亮的分數。」

### Key concept
Introduce **class imbalance** intuitively, not mathematically.

### Student takeaway
Before trusting Accuracy, inspect class distribution and error types.

### Misconception guard
Do not teach students that Accuracy is always useless. Teach that it is insufficient by itself.

---

## S04 — Wrong Is Not Just Wrong

### On-screen content
Two failure stories:

```text
A. NORMAL → predicted ATTACK
   False Alarm

B. ATTACK → predicted NORMAL
   Missed Attack
```

Question:
> Are these two mistakes equally costly?

### Visual composition
Two comic-like security-control-room scenes. A: harmless weather/API event triggers a noisy alarm and analyst workload. B: real malicious event passes silently and reaches the protected system.

### Teacher narration
「在一般考試裡，答錯一題就是錯一題。但資安不是這樣。」

「正常資料被 AI 說成攻擊，會怎樣？可能造成誤報、浪費分析師時間、使用者被擋。」

「真正攻擊被 AI 說成正常，又會怎樣？可能讓攻擊直接穿過防線。」

「所以我們下一步不能只問『錯幾個』，而要問：**錯的是哪一種？**」

### Student takeaway
Different classification errors produce different operational consequences.

### Interaction
Ask students which error is worse. Accept scenario-dependent answers; do not impose FN as universally worse.

---

## S05 — We Need Four Boxes

### On-screen content
```text
                 AI PREDICTION
              ATTACK       NORMAL
REAL ATTACK      ?            ?
REAL NORMAL      ?            ?
```

Prompt:
> We know Reality. We know AI's Prediction. How many possible combinations exist?

### Visual composition
An empty 2×2 investigation board. Use icons for Reality and AI Prediction. The four cells are initially question marks. This is a build-up slide before naming TP/TN/FP/FN.

### Teacher narration
「我們其實只需要整理兩件事：真實世界是什麼，以及 AI 說它是什麼。」

「真實有 Attack / Normal 兩種；預測也有 Attack / Normal 兩種。兩兩組合，就只有四種情況。」

Have students describe the four cases in ordinary language first.

### Student takeaway
The confusion matrix is not an arbitrary formula; it is a complete map of actual-vs-predicted outcomes.

### Teaching rule
Do NOT show TP/TN/FP/FN abbreviations until students understand the four stories.

---

## S06 — Confusion Matrix: The Security Error Map

### On-screen content
```text
                         PREDICTED
                    ATTACK       NORMAL
ACTUAL ATTACK        TP            FN
ACTUAL NORMAL        FP            TN
```

Security translation:

- TP = Attack caught
- TN = Normal correctly passed
- FP = False alarm
- FN = Attack missed

### Visual composition
Use a large 2×2 confusion matrix as the central object, but each cell contains a small scenario illustration rather than only letters. Emphasize FP and FN as operational error cells.

### Teacher narration
「現在才把名字放上去。True / False 講的是 AI 有沒有判對；Positive / Negative 講的是 AI 判成我們關心的目標類別還是非目標類別。」

「今天我們把 ATTACK 定義成 Positive。所以 TP 就是真攻擊而且抓到了；FN 就是真攻擊，但是模型說 Normal——也就是漏掉攻擊。」

「請不要死背 TP、TN、FP、FN 的位置。永遠先看兩件事：**Actual 是什麼？Predicted 是什麼？**」

### Board explanation
```text
TRUE  = prediction agrees with reality
FALSE = prediction disagrees with reality

POSITIVE = model says ATTACK
NEGATIVE = model says NORMAL
```

### Student takeaway
Students can translate every confusion-matrix cell into a cybersecurity event story.

### Interaction
Teacher calls four mini-scenarios; students answer TP/TN/FP/FN.

### Handoff to S07
Next question:

> 「有了這四格，我們要怎樣回答：AI 發出警報時，到底有多可信？」

This naturally introduces Precision.

---

# 7. S00–S06 Visual Rhythm

```text
S00  mystery / provocative hero
S01  continuity map
S02  quantitative scenario
S03  visual contradiction
S04  two error stories
S05  construct the 2×2 logic
S06  formalize confusion matrix
```

Avoid seven consecutive text-card slides. The visual object should change with the teaching purpose.

---

# 8. Planned Next Batch

S07–S13 will teach:

```text
S07 Precision — When AI cries ATTACK, how often is it right?
S08 Precision calculation from the matrix
S09 Recall — Of real attacks, how many did AI catch?
S10 Recall calculation
S11 Precision vs Recall — two different security questions
S12 Why one metric cannot rule every scenario
S13 F1 — balanced summary, but still not business/security cost
```

Later slides will connect the metrics to the actual L6 Random Forest, `sklearn.metrics`, evidence, AI-assisted interpretation, and L8 handoff.
