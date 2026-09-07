# AIIS_L7 — Teaching Script S07–S13

Date: 2026-09-07
Status: IN PROGRESS
Lesson: Supervised ML III — Security Evaluation
Continuation: S00–S06 Accuracy Trap → Confusion Matrix
Design standard: `_myplan_/AIIS-COURSE-DESIGN-STANDARD.md`

---

# Batch Mission

S00–S06 established that Accuracy alone cannot answer a security question. S07–S13 now turns the confusion matrix into three evaluation lenses:

```text
Confusion Matrix
      ↓
Precision — Can I trust an alarm?
      ↓
Recall — Can I catch the attacks?
      ↓
Precision vs Recall — Which failure matters here?
      ↓
F1 — One balanced summary
      ↓
But security cost still needs human judgment
```

The formulas are secondary. Every metric must first be understood as a security question.

---

## S07 — Precision: When AI Cries ATTACK, How Often Is It Right?

### On-screen hero question
> **AI 發出 ATTACK 警報時，有多少是真的？**

### On-screen concept
```text
Look only at cases AI predicted ATTACK:

TP = real attack caught
FP = normal event falsely alarmed

Precision = TP / (TP + FP)
```

### Security translation
**Precision = 警報可信度**

### Visual composition
A SOC analyst receives 10 red AI alarm cards. Some cards contain genuine attacker icons; others reveal harmless normal events. A magnifying glass brackets only the `Predicted ATTACK` column of the confusion matrix.

Huange avatar asks: 「這些警報，我到底能信多少？」

### Teacher narration
「S06 我們有四格了。現在不要一次看四格。第一個問題只看 AI 已經叫出來的 ATTACK。」

「假設 AI 今天發了很多警報，資安人員每一個都要查。如果其中大量都是誤報，會發生什麼事？」

Expected answers:
- analyst workload rises
- alert fatigue
- users/services may be unnecessarily blocked
- real incidents can be buried in noise

「所以 Precision 問的不是『攻擊抓得多不多』，而是：**你叫出來的警報，到底有多可信？**」

### Board derivation
Circle the `Predicted ATTACK` column:

```text
TP
FP
```

Then derive:

```text
Precision = 真警報 / 所有 AI 警報
          = TP / (TP + FP)
```

### Student takeaway
High Precision means fewer false alarms among the cases labeled as attacks.

### Misconception guard
Precision does **not** tell us how many real attacks were missed.

### Handoff
「那如果我真正關心的是：100 個真攻擊，到底抓到幾個呢？」

---

## S08 — Precision Calculation: 10 Alarms, 8 Real

### On-screen scenario
AI raises **10 ATTACK alarms**:

- 8 are real attacks → TP = 8
- 2 are normal events → FP = 2

### Student challenge
> Precision = ?

### Visual composition
Ten large alarm tiles, eight with attacker evidence and two marked false alarm. Avoid starting with a formula card; make students count the visual objects first.

### Reveal
```text
Precision = 8 / (8 + 2)
          = 0.80
          = 80%
```

### Teacher narration
「先不要背公式。AI 說有十個 Attack，我去查，八個是真的。所以你會怎麼描述這個 AI 的警報？」

Guide students toward:

> 「AI 發警報時，大約 80% 是真的。」

Then connect the natural-language statement to the metric name.

### Security interpretation
```text
Precision 80%
≠ model is 80% accurate
≠ model caught 80% of all attacks
```

It means:

> **Among AI's ATTACK predictions, 80% were actual attacks.**

### Student takeaway
Students can calculate and narrate Precision in operational language.

### Interaction
Ask: If TP remains 8 but FP rises from 2 to 12, does Precision improve or worsen? Students answer before calculation.

---

## S09 — Recall: Of the Real Attacks, How Many Did AI Catch?

### On-screen hero question
> **真正發生的攻擊，有多少被 AI 抓到了？**

### On-screen concept
```text
Look only at REAL ATTACKS:

TP = attack caught
FN = attack missed

Recall = TP / (TP + FN)
```

### Security translation
**Recall = 攻擊捕捉率 / 漏攻擊風險的另一面**

### Visual composition
A security gate sees 10 actual red attackers approaching. Eight are intercepted; two slip through silently. A magnifying bracket now highlights the `Actual ATTACK` row of the confusion matrix.

### Teacher narration
「Precision 是從 AI 的嘴巴出發：它喊 Attack 時可信嗎？」

「Recall 完全換一個角度。現在不要管 AI 發了多少警報，我們站在真實世界這一邊：**真正的攻擊到底有多少被抓到？**」

Circle:

```text
Actual ATTACK:
TP  FN
```

「TP 是抓到的，FN 是漏掉的。所以 Recall 看的是抓到多少真攻擊。」

### Board derivation
```text
Recall = 抓到的真攻擊 / 所有真攻擊
       = TP / (TP + FN)
```

### Student takeaway
Recall focuses on coverage of actual attacks.

### Security emphasis
A low Recall means many attacks are becoming False Negatives.

### Misconception guard
Do not say high Recall automatically means a good model; it may be achieved by generating excessive alarms.

---

## S10 — Recall Calculation: We Caught 8 of 10 Attacks

### On-screen scenario
Reality contains **10 attacks**:

- 8 caught → TP = 8
- 2 missed → FN = 2

### Student challenge
> Recall = ?

### Visual composition
Ten attacker icons moving toward the protected Weather Security Center. Eight hit a detection shield; two pass through. The visual must make the denominator visibly mean `all real attacks`.

### Reveal
```text
Recall = 8 / (8 + 2)
       = 80%
```

### Teacher narration
「這一次也是 80%，但跟上一頁的 80% 意義完全不同。」

Compare:

```text
Precision 80%
→ AI 發的警報，80%是真的

Recall 80%
→ 真正的攻擊，80%被抓到
```

### Key teaching moment
Put both sentences side by side. Do not let students leave with only formulas.

### Interaction
Ask:

「如果我把系統調得非常敏感，看到任何可疑東西都喊 Attack，Recall 可能怎樣？Precision 又可能怎樣？」

Expected intuition:
- Recall may rise
- Precision may fall because FP increases

### Student takeaway
The same percentage can answer completely different security questions.

---

## S11 — Precision vs Recall: Two Different Security Questions

### On-screen content
```text
PRECISION
AI 說 Attack → 我能多相信？
Concern: False Positives

RECALL
真的 Attack → 我抓到多少？
Concern: False Negatives
```

### Visual composition
Use a balanced two-lens security dashboard rather than a generic comparison table.

Left lens: noisy SOC alarm queue → Precision.
Right lens: attacker escaping through gate → Recall.

Center: same classifier, two different evaluation questions.

### Teacher narration
「Precision 和 Recall 不是兩個互相競爭、一定要選一個的公式。它們是兩個不同問題。」

「如果你的 SOC 每分鐘幾千個誤報，分析師根本看不完，你會非常在意 Precision。」

「如果這是一個不能漏掉高風險攻擊的偵測層，你會非常在意 Recall。」

「重點不是背哪一個比較重要，而是先問：**這個安全情境最怕哪一種錯誤？**」

### Scenario interaction
Teacher gives two cases:

1. Automated blocking of employee accounts.
2. Screening for a rare high-impact malicious event.

Students discuss whether FP or FN may be more costly in each case.

### Important nuance
There is no universal rule that FN is always worse. Cost depends on the system and consequence.

### Student takeaway
Metric priority must follow the security objective and error cost.

---

## S12 — The Security Trade-off: Catch More vs Cry Wolf

### On-screen hero
> **抓得更兇，不一定代表判得更準。**

### On-screen scenario
Two fictional detector settings:

```text
Detector A — Conservative
Few alarms
Few false alarms
But misses more attacks

Detector B — Sensitive
Catches more attacks
But creates more false alarms
```

### Visual composition
A security scanner with a sensitivity dial from conservative to sensitive. Moving the dial changes two visible streams: caught attacks and false alarms. Do not introduce ROC curves here.

### Teacher narration
「很多分類器最後不是只有『模型種類』的問題，還有『判多嚴格』的問題。」

「如果門檻放寬，只要有一點可疑就叫 Attack，我們可能抓到更多攻擊；但是正常事件也更容易被叫成 Attack。」

「所以你不能看到 Recall 上升就直接宣布模型變好了，也不能看到 Precision 上升就直接宣布模型更安全。」

### Preview only
Mention:

> Later, thresholds and Precision–Recall curves can formalize this trade-off.

Do not teach threshold tuning mechanics in L7.

### Student takeaway
Evaluation metrics represent trade-offs tied to operational consequences.

### Handoff
「如果我們希望用一個數字，同時不要完全忽略 Precision 和 Recall 呢？」

---

## S13 — F1: A Balanced Summary, Not the Final Security Decision

### On-screen content
```text
Precision ↘
            F1
Recall    ↗
```

Formula shown only after concept:

```text
F1 = 2 × (Precision × Recall)
         --------------------
         Precision + Recall
```

### Hero statement
> **F1 balances Precision and Recall — but it does not know your security consequences.**

### Visual composition
A balance scale with Precision and Recall as two evidence weights feeding an F1 evaluation card. Behind the card remain two real-world icons: false alarm cost and missed-attack cost, showing that F1 itself does not encode business/security consequence.

### Teacher narration
「如果報告需要一個同時考慮 Precision 和 Recall 的摘要，常見指標就是 F1。」

「F1 不希望你只把其中一邊做得很漂亮、另一邊非常差。」

「但是注意：F1 還是不知道你的系統到底多怕 False Positive，也不知道漏掉一次攻擊可能損失多少。」

「所以工程師不能說：『F1 最高，所以一定最安全。』真正的句子應該是：『在這個安全目標與錯誤成本下，我們選擇這些評估指標，證據如下。』」

### Optional mini-example
```text
Precision = 0.80
Recall    = 0.80
F1        = 0.80
```

Then show a deliberately asymmetric conceptual example:

```text
Precision high
Recall low
→ one attractive number cannot hide missed attacks
```

No lengthy hand calculation required.

### Student takeaway
F1 is a useful combined metric, not a substitute for security judgment.

### Handoff to next batch
> 「現在我們會算了。下一步不是再做紙上例題，而是把 L6 的 Random Forest 拿回來，真的對 TEST set 做 evaluation。」

---

# S07–S13 Concept Map

```text
             CONFUSION MATRIX
                    │
          ┌─────────┴─────────┐
          │                   │
   Predicted ATTACK      Actual ATTACK
          │                   │
     TP + FP               TP + FN
          │                   │
     PRECISION              RECALL
          └─────────┬─────────┘
                    │
                    F1
                    │
          SECURITY INTERPRETATION
```

---

# Visual Rhythm Audit

```text
S07  alarm trust / column focus
S08  countable alarm tiles
S09  attack capture / row focus
S10  security gate scenario
S11  two security lenses
S12  sensitivity dial / trade-off
S13  balance / synthesis
```

Do not render S07–S13 as seven formula slides. Formula density must remain low; scenario and visual semantics lead the teaching.

---

# Planned S14–S20

```text
S14 Bring Back the L6 Random Forest
S15 Predict on the Sealed TEST Set
S16 Build confusion_matrix in scikit-learn
S17 Read classification_report
S18 Translate metrics into security language
S19 Compare two model/error profiles
S20 Which model would YOU deploy — and why?
```

The next batch moves from conceptual metrics to actual model evidence.