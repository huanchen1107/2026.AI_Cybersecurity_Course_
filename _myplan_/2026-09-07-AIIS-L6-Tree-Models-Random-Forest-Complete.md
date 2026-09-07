# AIIS_L6 — Supervised ML II: Tree Models × Security Decisions

Date: 2026-09-07
Status: COMPLETE LESSON PLAN
Phase: LEARN
Primary tool: scikit-learn `RandomForestClassifier`
Persistent project: AI Weather Security Center / security-classification dataset from L5
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

L6 continues the supervised-ML story established in L5. It does not restart the ML workflow. The same dataset, feature definitions, train/test split discipline, and sealed TEST-set visual language should be reused whenever practical.

---

# 2. One Primary Mission

Students will understand how Decision Trees and Random Forests make security-classification decisions, inspect which features the trained model relies on, and produce a careful evidence-backed security interpretation.

Central question:

> **「AI 說這筆資料有風險——它到底是根據什麼判斷的？」**

---

# 3. Boundary

## THIS LESSON OWNS

- Decision Tree intuition
- feature-based decision questions
- split-quality intuition
- overfitting intuition
- Random Forest intuition
- bootstrap sampling intuition
- random feature selection intuition
- ensemble voting intuition
- `RandomForestClassifier`
- `.fit()` callback from L5
- feature importance inspection
- security interpretation of feature ranking
- model artifact vs AI-generated explanation
- evidence package and reproducibility

## THIS LESSON DOES NOT OWN

- full derivation of Gini / entropy
- XGBoost / LightGBM implementation
- broad ensemble-learning survey
- confusion matrix as a taught concept
- Precision / Recall / F1
- threshold tuning
- ROC-AUC / PR curve
- calibration
- full model evaluation methodology

Those belong to further exploration or L7.

---

# 4. PREVIEW → TEACH → REUSE

```text
L5 TEACH: features, labels, train/test split, .fit(), prediction
L6 REUSE: same workflow; change model and inspect decisions

L6 TEACH: Decision Tree, Random Forest, Feature Importance
L7 REUSE: same trained model for security evaluation

L6 PREVIEW: false negative / accuracy can mislead
L7 TEACH: confusion matrix, precision, recall, F1, security error cost
```

---

# 5. Lesson Storyline

```text
L5 Prediction
   ↓
WHY?
   ↓
Decision Tree
   ↓
Feature Questions
   ↓
Split Quality
   ↓
Overfitting Risk
   ↓
Random Forest
   ↓
Different Samples + Different Feature Choices
   ↓
Voting
   ↓
Train
   ↓
Inspect
   ↓
Feature Importance
   ↓
Security Interpretation
   ↓
AI-assisted Review
   ↓
Evidence
   ↓
Accuracy Is Not Enough
   ↓
L7
```

---

# 6. Slide Purpose Map

| Slide | Purpose |
|---|---|
| 00 | Position L6 between L5 training and L7 evaluation |
| S01 | Reopen L5 prediction and ask WHY |
| S02 | Build Decision Tree intuition as sequential questions |
| S03 | Connect feature values to tree nodes |
| S04 | Build split-quality intuition |
| S05 | Explain overfitting intuitively |
| S06 | Introduce Random Forest as many trees |
| S07 | Explain what “random” means |
| S08 | Explain bootstrap sampling intuition |
| S09 | Explain random feature selection intuition |
| S10 | Explain ensemble voting |
| S11 | Build first RandomForestClassifier |
| S12 | Reinforce UNTRAINED → .fit() → TRAINED and sealed TEST |
| S13 | Shift from training to inspection |
| S14 | Explain feature importance correctly |
| S15 | Extract feature importance from trained model |
| S16 | Teach Important ≠ Reasonable ≠ Causal |
| S17 | Convert ML ranking into security questions |
| S18 | Place generative AI behind evidence discipline |
| S19 | Launch lab mission |
| S20 | Human Plan Gate before AI-generated code |
| S21 | Train Forest in lab |
| S22 | Inspect top features |
| S23 | Write careful security interpretation |
| S24 | Human Evidence Gate / reproducibility package |
| S25 | Consolidate L6 knowledge map |
| S26 | Create need for L7 via misleading 95% accuracy example |
| S27 | Formal handoff to L7 |

---

# Slide 00 — AIIS_L6：AI 為什麼這樣判？

## 目的
建立 L5 → L6 定位。今天不重新做分類，而是開始打開模型的判斷過程。

## 投影片內容

> **AIIS_L6 — Supervised ML II**  
> **Tree Models × Security Decisions**
>
> 我們已經會讓 AI 做分類。今天要問：  
> **「它為什麼這樣判？」**
>
> `Decision Tree → Random Forest → Feature Importance`
>
> **Prediction is not enough. Understand the decision.**

## 視覺
沿用 L5 `TRAINED MODEL → PREDICTION`。放大 `Suspicious` Prediction Card，背後露出 decision path。

## 煥哥
Role: ML Security Investigator. 以放大鏡檢查 Prediction Card 背後的 Tree Path。

## 老師講稿
L5 已經讓資料進入模型並得到 prediction。今天開始追問：模型看到了什麼？哪個 feature 影響判斷？如果資料稍微不同，判斷會不會改變？資安工程不能只收答案，還要調查 Decision。

## 問
AI 預測正確一次，能不能證明它真的學對了？

## 預期答案
不能。可能只是剛好猜對，或學到錯誤規則。

## 核心句
> **Prediction tells us WHAT. Interpretation helps us ask WHY.**

## Transition
既然要追問 WHY，我們先把 L5 的模型重新打開。

---

# Slide 01 — 昨天的模型留下了一個問題

## 目的
從既有 prediction 引出 interpretation，而不是重教 train/test split。

## 投影片內容

```text
DATA → TRAIN → MODEL → PREDICTION → Suspicious
                                  ↓
                         WHY? FEATURE? RULE? TRUST?
```

> **A prediction is the beginning of investigation—not the end.**

## 視覺
重用 L5 pipeline，但把 DATA/TRAIN 淡化，Prediction 放大並連到 Feature / Rule / Trust 三條調查線。

## 煥哥
Investigator，把 Prediction Card 釘在 investigation board 上。

## 老師講稿
上一課的 workflow 已完成。今天只盯著最後的 Suspicious Card。Security Analyst 不會只看紅燈，而會追問 WHY、WHAT EVIDENCE、WHICH FEATURE、CAN I TRUST IT。

## 問
如果模型說 Suspicious，你最想先問什麼？

## 核心句
> **Don't stop at the prediction. Investigate the decision.**

## Transition
有沒有一種 ML 模型，可以把判斷畫得像人問問題一樣？

---

# Slide 02 — 如果 AI 像我們一樣問問題？

## 目的
用 sequential questions 建立 Decision Tree intuition。

## 投影片內容

```text
很多失敗登入？
   ├─ No  → Normal
   └─ Yes → 新的來源 IP？
              ├─ No  → Review
              └─ Yes → Suspicious
```

> **一連串問題 → 一個 Decision**

## 視覺
乾淨的三層 Decision Tree，每個 Node 是問題卡。

## 煥哥
Security Analyst，拿登入紀錄沿 Yes 路徑走。

## 老師講稿
Decision Tree 的直覺不是神秘大決定，而是不斷問比較小的問題，依 feature values 選分支直到 classification result。

## 問
真正做 classification 的動作是什麼？

## 預期答案
根據 feature 的值選擇分支，最後到達分類結果。

## 核心句
> **A Decision Tree classifies by asking a sequence of questions.**

## Transition
那 ML 的 Tree 問的問題從哪裡來？

---

# Slide 03 — Tree 問的是 Feature

## 目的
把 L5 Feature 概念正式連到 Decision Tree Node。

## 投影片內容

```text
Security Event
failed_logins = 18
new_ip        = 1
request_rate  = 93
hour          = 02

        ↓

failed_logins > 10?
        ↓
new_ip == 1?
        ↓
request_rate > 80?
        ↓
SUSPICIOUS
```

> **FEATURE VALUES → DECISION QUESTIONS**

## 視覺
L5 Feature Table 的同一列資料變形成 Decision Tree。

## 煥哥
Data Detective，用螢光筆圈 feature value，連到 Tree Node。

## 老師講稿
Tree 沒有獲得新情報。它仍然只看到 L5 給它的 features。若重要的 security signal 沒有進 features，Tree 不會神奇知道。

## 老師補充 / 板書

```text
MODEL KNOWLEDGE ≠ REAL WORLD
MODEL KNOWLEDGE ⊆ FEATURES WE PROVIDE
```

## 核心句
> **A model can only learn from the features it can see.**

## Transition
既然 Tree 可以問很多問題，它怎麼決定先問哪一個？

---

# Slide 04 — 好問題會把資料分得更清楚

## 目的
建立 split quality intuition，不陷入公式。

## 投影片內容
比較兩個問題：`hour > 12?` 與 `failed_logins > 10?`。後者分完後讓 Normal / Suspicious 更集中。

> **Good splits make groups more pure.**

## 視覺
20 個紅藍點，對比 Split A 與 Split B。

## 煥哥
Tree Builder，手持兩張 Question Cards 比較分割結果。

## 老師講稿
Tree 會尋找能讓類別更容易區分的 split。此處只看圖建立「混不混」直覺；可 preview `Gini impurity` 名稱，但不推導。

## 核心句
> **The tree searches for questions that separate the classes.**

## Transition
一直問更多問題是不是一定更好？

---

# Slide 05 — 一棵樹可以問到「太認真」

## 目的
直覺理解 Overfitting。

## 投影片內容

```text
Simple Tree        Very Deep Tree
3–4 questions      many tiny questions
pattern            memorization

TRAIN 99%
TEST  72%
```

> **More complex ≠ Better**

## 視覺
小而乾淨的 Tree 對比極度茂密、葉子貼 individual training IDs 的深樹。

## 煥哥
Model Reviewer，拿剪枝剪刀觀察過度生長的 Tree（只作 metaphor）。

## 老師講稿
類比背考古題：原題 99 分，稍微換題只剩 72 分，不代表真正理解。Machine Learning 也是一樣。

## 核心句
> **Overfitting means learning the training data better than the underlying pattern.**

## Transition
如果不要只問一棵樹呢？

---

# Slide 06 — 不要只問一棵樹

## 目的
自然引出 Random Forest。

## 投影片內容

```text
Tree 1 → Suspicious
Tree 2 → Suspicious
Tree 3 → Normal
Tree 4 → Suspicious
Tree 5 → Normal
          ↓
        VOTE
          ↓
     SUSPICIOUS
```

> **Many Trees → One Forest**

## 視覺
一張 Security Event Card 分流進五棵 Tree，再匯流到 Vote Box。

## 煥哥
Security Team Lead，整理五張 Vote Cards。

## 老師講稿
不要讓一棵 Tree 當獨裁者。建立很多不同 Trees，最後集合 decision。

## 核心句
> **Don't trust one tree. Ask the forest.**

## Transition
這些 Trees 為什麼會不一樣？

---

# Slide 07 — Random 到底 Random 在哪裡？

## 目的
Random 不等於亂猜，而是 controlled diversity。

## 投影片內容

```text
Same Training Dataset
        ↓
Controlled Randomness
        ↓
1. Different training samples
2. Different feature choices
        ↓
Different Trees
        ↓
Collective Decision
```

> **Randomness creates diversity—not chaos.**

## 視覺
Samples / Features 兩個 randomness control knobs 連到不同 Trees。

## 煥哥
ML Engineer，校正兩個控制旋鈕。

## 老師講稿
若 100 棵 Tree 完全一樣，投票只是重複同一判斷。Random Forest 刻意讓不同 Trees 有差異，以減少大家犯同一種錯誤的機會。

## 核心句
> **Randomness creates diversity—not chaos.**

## Transition
先看不同 Training Samples。

---

# Slide 08 — 每棵 Tree 都拿到不同的練習題

## 目的
建立 Bootstrap Sampling intuition。

## 投影片內容

```text
Original: A B C D E F
Tree 1 : A C C D F A
Tree 2 : B B D E F E
Tree 3 : A B D D E F
```

> **Sample WITH replacement**  
> **Bootstrap Sampling**

## 視覺
Security Event Cards 被抽給不同 Trees；明確看見重複與未抽到。

## 煥哥
Dataset Dealer，從 Training Dataset 牌堆抽卡。

## 老師講稿
抽完放回，同一 sample 可能再次抽到；每棵 Tree 因此有不同 learning experience。

## 核心句
> **Different samples create different learning experiences.**

## Transition
但如果每棵 Tree 永遠先看同一個強 Feature，仍可能很像。

---

# Slide 09 — 每次不要讓 Tree 看全部 Features

## 目的
理解 Random Feature Selection。

## 投影片內容

```text
Features:
failed_logins / new_ip / request_rate / hour / country_change / device_change

Tree A candidate set:
failed_logins / hour / device_change

Tree B candidate set:
new_ip / request_rate / country_change
```

> **Different Feature Choices → Different Trees**

## 視覺
兩個 Viewfinder 各框不同 Feature Cards。

## 煥哥
Feature Selector，以 Viewfinder 比較候選 Feature。

## 老師講稿
單棵 Tree 可能因候選 features 受限而變弱一點，但 Forest 得到更多不同觀點。

## 核心句
> **A stronger forest can come from diverse trees.**

## Transition
現在讓這些不同 Trees 一起做 Security Decision。

---

# Slide 10 — Forest 開始投票

## 目的
完整建立 classification ensemble prediction intuition。

## 投影片內容

```text
Security Event
failed_logins = 18
new_ip        = Yes
request_rate  = 93
hour          = 02

Tree 1 → Suspicious
Tree 2 → Suspicious
Tree 3 → Normal
Tree 4 → Suspicious
Tree 5 → Normal

3 vs 2 → SUSPICIOUS
```

第一次帶出 `Ensemble Learning`：many models → combine decisions → one final model。

## 視覺
五張 Vote Cards 進透明 Ballot Box。

## 煥哥
Decision Aggregator，正在數票。

## 核心句
> **Random Forest turns many tree decisions into one ensemble decision.**

## Transition
概念懂了，現在真正把 Forest 建起來。

---

# Slide 11 — 四行程式建立一座 Forest

## 目的
從概念轉入 scikit-learn implementation。

## 投影片內容

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
```

```text
RandomForestClassifier → 建立 Forest
n_estimators=100       → 100 Trees
.fit(...)              → Learn from TRAIN
```

> **Same ML workflow. Different model.**

## 視覺
L5 pipeline 只替換 MODEL 模組。

## 煥哥
ML Engineer，把 RandomForestClassifier 模組卡插入既有 pipeline。

## 老師講稿
L5 workflow 沒消失，只是 classifier 換掉。`random_state` 用於可重現實驗。

## 核心句
> **The workflow stays. The model changes.**

## Transition
建立 `model` 不代表它已經學會。

---

# Slide 12 — `.fit()` 前後，Forest 完全不同

## 目的
重用 L5 conceptual callback。

## 投影片內容

```text
BEFORE .fit()                 AFTER .fit()
UNTRAINED FOREST   → .fit() → TRAINED FOREST

X_test remains sealed 🔒
```

> **TRAIN teaches. TEST waits.**

## 視覺
沿用 L5 UNTRAINED → TRAINED；Test Box 保持封條。

## 煥哥
Training Gatekeeper，一手讓 TRAIN 通過，一手擋住 TEST。

## 老師講稿
Random Forest 再厲害，也不能偷看考卷。真正 learning 發生在 `.fit(X_train, y_train)`。

## 核心句
> **TRAIN teaches. TEST waits.**

## Transition
Forest 已經學完。L6 現在問：它最常依靠哪些 Features？

---

# Slide 13 — Forest 學到了什麼？

## 目的
把 trained model 當可調查工程物件。

## 投影片內容

```text
TRAIN → .fit() → TRAINED FOREST
                   ↓
             WHAT DID IT LEARN?
             Which features?
             How important?
             What might that mean?
```

> **INSPECT THE MODEL**

## 視覺
打開 Forest Inspection Panel，露出 Feature Bars。

## 煥哥
Model Inspector，以檢查燈照 Inspection Panel。

## 核心句
> **A trained model should be inspected—not merely trusted.**

## Transition
Feature Importance 到底告訴我們什麼？

---

# Slide 14 — 哪些 Features 被模型用得比較多？

## 目的
建立 Feature Importance 正確直覺。

## 投影片內容

```text
failed_logins  █████████ 0.36
request_rate   ███████   0.28
new_ip         █████     0.20
device_change  ███       0.10
hour           ██        0.06
```

> Higher importance = model relied more on this feature when building decisions.
>
> **IMPORTANT ≠ CAUSAL**

## 視覺
Feature Ranking；避免畫成 feature causes attack。

## 煥哥
Model Analyst，用尺量 Feature Bars，另一手指 `IMPORTANT ≠ CAUSAL`。

## 老師補充 / 板書

```text
IMPORTANCE ≈ MODEL RELIANCE
IMPORTANCE ≠ CAUSATION
```

## 核心句
> **Feature importance describes model reliance—not real-world causality.**

## Transition
直接從 trained Forest 把 importance 拿出來。

---

# Slide 15 — 把 Feature Importance 從模型取出來

## 目的
產出可保存的 Evidence Artifact。

## 投影片內容

```python
import pandas as pd

importance = pd.Series(
    model.feature_importances_,
    index=X_train.columns
).sort_values(ascending=False)

print(importance)
```

## 視覺
Forest Evidence Drawer 抽出 `FEATURE IMPORTANCE REPORT`。

## 煥哥
ML Engineer，從 trained Forest 抽出報表。

## 老師講稿
先讀 model artifact，再請生成式 AI 協助解釋；不要反過來。

## 核心句
> **Read the model artifact before asking AI to explain it.**

## Transition
有 Ranking 不代表結論一定合理。

---

# Slide 16 — 「重要」不代表「合理」

## 目的
建立資安工程式懷疑。

## 投影片內容
假設 `source_port = 0.41` 排第一，追問：

```text
REAL SIGNAL?
DATASET BIAS?
DATA LEAKAGE?
```

> **Interesting ≠ Correct**

## 視覺
圈出異常高 importance，連到 Security Meaning / Dataset / Leakage 三條 investigation paths。

## 煥哥
Security Reviewer，紅筆圈 feature，同時翻 Dataset Documentation。

## 老師講稿
高 importance 是調查起點，不是老師公布答案。可 preview Data Leakage，但不發散。

## 核心句
> **High importance is a question to investigate—not a conclusion to copy.**

## Transition
所以現在需要 Security Analyst，而不只是 ML Engineer。

---

# Slide 17 — 從 ML Ranking 變成 Security Interpretation

## 目的
把 ML output 轉成 Security Questions。

## 投影片內容

| Feature | Model Says | Security Analyst Asks |
|---|---|---|
| failed_logins | High | 暴力登入訊號？ |
| request_rate | High | 自動化掃描／DoS？ |
| new_ip | Medium | 新來源真的代表風險？ |
| hour | Low | 時間訊號是否不足？ |

```text
MODEL OUTPUT → SECURITY CONTEXT → HUMAN INTERPRETATION
```

## 視覺
Feature Report 經過 Security Context Lens 轉成 questions。

## 煥哥
Security Analyst，拿 Context Lens 檢查 Feature Report。

## 核心句
> **The model finds patterns. Humans connect them to security meaning.**

## Transition
生成式 AI 可以協助解釋，但它應該站在哪個位置？

---

# Slide 18 — AI 可以解釋，但不能替 Evidence 說話

## 目的
重新連回 AIIS Evidence Discipline。

## 投影片內容

錯誤：
```text
Feature Importance → ChatGPT → “therefore causes attack” → REPORT
```

正確：
```text
MODEL ARTIFACT
    ↓
AI-ASSISTED INTERPRETATION
    ↓
HUMAN REVIEW
    ↓
DATA / SECURITY CONTEXT
    ↓
SUPPORTED CLAIM
```

> **AI CLAIM ≠ VERIFIED EVIDENCE**  
> **Let AI explain. Let evidence decide.**

## 視覺
AI conclusion 被 Evidence Gate 擋住；有 artifact + context 的 Evidence Card 才通過。

## 煥哥
Evidence Gatekeeper，阻止 AI 文字直接蓋章 CONFIRMED。

## 老師補充 / 板書

```text
AI PROPOSES
   ↓
HUMAN REVIEWS
   ↓
TOOL / DATA VERIFIES
   ↓
HUMAN DECIDES
```

## 核心句
> **AI CLAIM ≠ VERIFIED EVIDENCE.**

## Transition
概念完成，現在進入 Lab。

---

# Slide 19 — Mission Brief：調查 Security Dataset

## 目的
把概念收斂成明確任務。

## 投影片內容

MISSION：使用既有 Security Dataset 訓練 Random Forest，找出模型最依賴的 Features，並做合理 Security Interpretation。

INPUT：`X_train`, `y_train`, `X_test`, `y_test`

REQUIRED OUTPUT：
1. TRAINED MODEL
2. FEATURE IMPORTANCE
3. TOP FEATURES
4. SECURITY INTERPRETATION
5. EVIDENCE CARD

> **Goal: Understand the decision—not chase the score.**

## 視覺
Mission Board，右側五個空 Evidence Slots；TEST 仍封條。

## 煥哥
Mission Commander，指向 Required Outputs。

## 核心句
> **This lab investigates how the model decides.**

## Transition
在讓 AI 幫忙寫 code 之前，先看 Plan。

---

# Slide 20 — AI 可以寫 Code，但先過 Human Plan Gate

## 目的
把 AI-assisted coding 帶入 ML Lab，同時守住 workflow ownership。

## 投影片內容

Prompt 核心：
```text
Build a Random Forest classifier using the existing training data.
Do not change the dataset split.
Do not use test data during training.
Return code, feature importance, and evidence outputs.
```

Human checklist：
```text
□ 使用既有 X_train / y_train
□ TEST 不進 .fit()
□ RandomForestClassifier
□ 固定 random_state
□ 輸出 feature_importances_
□ 保留可重現結果
```

> **PLAN FIRST. CODE SECOND.**

## 視覺
Callback L2 Human Plan Gate。

## 煥哥
Plan Reviewer，逐項核對 AI Plan，筆尖停在 `TEST 不進 .fit()`。

## 核心句
> **AI may propose the plan. Humans approve the experiment.**

## Transition
Plan 通過，才開始建 Forest。

---

# Slide 21 — Build：Train the Forest

## 目的
完成最小可執行 Random Forest Lab。

## 投影片內容

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)
```

Acceptance：code runs / model trained / no test data used。

## 視覺
`X_train + y_train → .fit() → TRAINED FOREST`；TEST Box 在角落鎖住。

## 煥哥
ML Builder，啟動 `.fit()` switch。

## 核心句
> **Training happens at `.fit()`.**

## Transition
現在模型完成，但今天要把它打開。

---

# Slide 22 — Inspect：把 Forest 的依賴排行拿出來

## 目的
產出本課第一份真正 Evidence Artifact。

## 投影片內容

```python
import pandas as pd

importance = pd.Series(
    model.feature_importances_,
    index=X_train.columns
).sort_values(ascending=False)

print(importance.head(5))
```

Mission Board status：
```text
TRAINED MODEL        ✓
FEATURE IMPORTANCE   ✓
TOP FEATURES         ✓
INTERPRETATION       □
EVIDENCE CARD        □
```

## 視覺
Callback S19 Mission Board；前三格完成。

## 煥哥
Model Inspector，把 Top-5 Ranking 貼到 Board。

## 核心句
> **Model output becomes useful only when we inspect and interpret it.**

## Transition
數字還需要 Security Meaning。

---

# Slide 23 — Interpret：把 Top Features 變成 Security Questions

## 目的
要求學生做有保留的解釋。

## 投影片內容

| Feature | Importance | Possible Security Meaning | Need Verification? |
|---|---:|---|---|
| failed_logins | 0.34 | brute-force signal? | Yes |
| request_rate | 0.27 | scanning / automation? | Yes |
| new_ip | 0.19 | unfamiliar source? | Yes |

```text
DO SAY: may indicate / model relies on / worth investigating
DO NOT SAY: proves / causes / confirmed attack
```

## 視覺
Evidence Interpretation Card；每個 interpretation 後保留問號。

## 煥哥
Security Investigator，貼 `VERIFY` stickers。

## 核心句
> **Good security interpretation preserves uncertainty.**

## Transition
最後一關是 Evidence Gate。

---

# Slide 24 — Human Evidence Gate：No Evidence, No Trust

## 目的
完成 L6 Lab Closure，建立可重現成果包。

## 投影片內容

EVIDENCE PACKAGE：
```text
□ Dataset version
□ Train/Test split record
□ Random Forest config
□ random_state
□ Training code
□ Feature importance output
□ Top features
□ Security interpretation
□ AI assistance record
□ Human review
```

> **SPEC DEFINES. AI IMPLEMENTS. HUMAN VERIFIES. GIT REMEMBERS.**

## 視覺
Callback L2 Human Evidence Gate；`AI says it works` 被擋住，完整 artifact package 通過。

## 煥哥
Evidence Gatekeeper，把完整 package 蓋 `ACCEPTED`。

## 老師補充 / 板書

```text
REPRODUCIBLE = DATA + CODE + CONFIG + OUTPUT
```

## 核心句
> **NO EVIDENCE, NO TRUST.**

## Transition
Lab 完成，現在把整課串回一條知識線。

---

# Slide 25 — L6 Knowledge Map：從 Tree 到 Security Interpretation

## 目的
把名詞重新串成完整因果鏈。

## 投影片內容

```text
L5 Classification Workflow
        ↓
Decision Tree
        ↓
Feature Questions
        ↓
Good Split
        ↓
Overfitting Risk
        ↓
Random Forest
        ↓
Many Diverse Trees
        ↓
Voting
        ↓
Feature Importance
        ↓
Security Interpretation
        ↓
Evidence
```

> **Understand the model before judging the model.**

## 視覺
Forest Investigation Journey，重用 L5 Prediction Card / Tree / Forest / Ranking / Context Lens / Evidence Card。

## 煥哥
Learning Guide，以指揮棒回指整條 Journey。

## 老師補充 / 板書

```text
TRAIN ≠ FINISH
TRAIN → INSPECT → INTERPRET → VERIFY
```

## 核心句
> **Understand the model before judging the model.**

## Transition
但是我們一直故意沒有正式回答：模型到底好不好？

---

# Slide 26 — 最危險的問題：這個模型到底好不好？

## 目的
製造 L7 的認知需求。

## 投影片內容

```text
1000 security events
950 Normal
50 Attacks

Model predicts EVERYTHING as Normal

Accuracy = 95%
Detected attacks = 0
```

> **95% ACCURACY. 0 ATTACKS FOUND.**

Preview only:
```text
FALSE NEGATIVE
ATTACK → MODEL SAYS NORMAL
```

## 視覺
左側巨大綠色 95% Score Card；右側 50 個 attacks 全部穿過 Detection Gate。

## 煥哥
Security Reviewer，一手拿 95% 卡，另一手指向漏掉的 attacks，表情警覺。

## 老師講稿
不要因高 Accuracy 就認為模型安全。此處只 preview False Negative；不要提前教 confusion matrix / recall。

## 核心句
> **A high score can still hide a dangerous security failure.**

## Transition
L7 要問的不是只猜對幾個，而是錯在哪裡、錯一次代價是多少。

---

# Slide 27 — Handoff to L7：Accuracy Is Not Enough

## 目的
正式完成 Lesson Handoff。

## 投影片內容

### WHAT WE NOW KNOW
- How Decision Trees make decisions
- Why overfitting happens
- Why Random Forest uses many trees
- How a Forest combines decisions
- How to inspect Feature Importance
- How to write careful Security Interpretation
- How to preserve Evidence

### WHAT WE STILL DO NOT KNOW
- How many attacks did we miss?
- How many normal events became false alarms?
- Which error is more dangerous?
- Is Accuracy hiding the problem?

### WHY L7 IS NECESSARY

```text
L6 — HOW DOES THE MODEL DECIDE?
                ↓
L7 — HOW GOOD IS THE DECISION?
```

Preview only:
`Confusion Matrix / Precision / Recall / F1 / False Positive / False Negative`

> **Accuracy is not enough for cybersecurity.**

## 視覺
L6 Evidence Package 交到仍鎖住的 L7 Evaluation Dashboard；只模糊露出 TP/FP/FN/TN。

## 煥哥
Handoff Engineer，把 L6 package 放上通往 L7 的傳送帶。

## 問
在入侵偵測裡，漏掉 Attack 和多產生一個警報，哪個一定比較嚴重？

## 預期答案
不能一概而論，要看系統情境、風險與代價。

## 核心句
> **Accuracy is not enough for cybersecurity.**

---

# 7. Lab Contract

## MISSION
Train one Random Forest using the existing L5 security-classification workflow; inspect top features and write evidence-backed security interpretations.

## INPUT
- L5 dataset
- X_train / y_train
- X_test / y_test retained for later evaluation
- feature definitions / dataset documentation

## STEPS
1. Reuse L5 split and feature schema.
2. Ask AI for an implementation plan.
3. Human review at Plan Gate.
4. Build `RandomForestClassifier(n_estimators=100, random_state=42)`.
5. Train using only X_train / y_train.
6. Extract `feature_importances_`.
7. Rank top features.
8. Interpret them in security context with cautious language.
9. Record AI assistance and human review.
10. Assemble evidence package.

## EXPECTED OUTPUT
- trained Random Forest
- feature-importance table
- top-5 features
- security interpretation table
- reproducible config
- evidence card/package

## TEST / VERIFY
- code runs
- model reaches trained state
- test data did not enter `.fit()`
- feature names match importance values
- importance ranking comes from actual runtime artifact
- interpretation does not claim unsupported causality

## EVIDENCE
- dataset/version
- split record
- code
- config
- random_state
- runtime output
- feature importance
- interpretation
- AI assistance record
- human-review record

## REFLECTION
1. Which feature surprised you most?
2. Is the highest-ranked feature security-plausible?
3. Could dataset bias or leakage explain the ranking?
4. What claim can you support, and what claim must remain uncertain?
5. What evaluation question is still unanswered for L7?

---

# 8. Reusable Antigravity Prompt / YAML

```yaml
role: "AI-assisted ML implementation partner"
context:
  course: "AIIS_L6 — Tree Models × Security Decisions"
  project: "AI Weather Security Center"
  prior_lesson: "L5 established the dataset, features, labels, train/test split, and classification workflow"
mission: |
  Build one RandomForestClassifier using the existing L5 training split,
  extract feature importance, and produce reproducible evidence for human review.
scope:
  - reuse existing X_train and y_train
  - RandomForestClassifier
  - n_estimators: 100
  - fixed random_state
  - feature_importances_
  - ranked top features
  - runtime evidence
out_of_scope:
  - changing the dataset problem
  - rebuilding the train/test split without approval
  - training on test data
  - XGBoost
  - LightGBM
  - threshold tuning
  - full L7 metric analysis
constraints:
  - "TEST data must remain outside .fit()"
  - "Do not claim causality from feature importance"
  - "AI explanation is not verified evidence"
steps:
  - inspect existing L5 data variables and feature names
  - propose an implementation plan
  - stop for human plan review
  - implement RandomForestClassifier
  - train only on X_train and y_train
  - extract and sort feature_importances_
  - print or save top features
  - provide cautious candidate security interpretations
  - identify what requires human/domain verification
human_review_gates:
  plan_gate:
    - confirm existing split is preserved
    - confirm test data is excluded from training
    - confirm only RandomForestClassifier is the primary model
  evidence_gate:
    - verify runtime output exists
    - verify feature names align with importances
    - verify interpretations preserve uncertainty
acceptance_criteria:
  - code executes successfully
  - trained model exists
  - test data was not used in fit
  - top feature importance output is produced
  - config is reproducible
  - evidence package is complete
evidence:
  - dataset_version
  - split_record
  - code_version
  - model_config
  - random_state
  - runtime_output
  - feature_importance_output
  - interpretation_notes
  - ai_assistance_record
  - human_review_record
```

---

# 9. Final Content + Visual Audit

## Curriculum / Story
- [x] One primary mission: understand model decision and feature reliance.
- [x] L5 workflow reused rather than repeated.
- [x] L7 evaluation content not taught early.
- [x] Decision Tree is conceptual bridge; Random Forest is primary implementation.
- [x] Feature importance is not represented as causality.
- [x] Persistent security dataset is reused.
- [x] Lab closes with Evidence.
- [x] L7 need is created by a security-specific accuracy failure example.

## Visual Audit
- [x] Slide 00 reuses L5 Prediction Card.
- [x] S03 reuses L5 Feature Table.
- [x] S06 → S10 reuses same Forest/Voting object with more detail.
- [x] S11–S12 reuses L5 UNTRAINED → TRAINED callback.
- [x] TEST set remains visibly sealed whenever `.fit()` appears.
- [x] S19 Mission Board empty evidence slots → S22 partial → S24 complete.
- [x] S20 Human Plan Gate → S24 Human Evidence Gate.
- [x] S25 reuses the entire lesson object journey.
- [x] S27 physically hands the L6 Evidence Package to the L7 Evaluation Gate.
- [x] Huange is an acting narrative guide rather than a decorative sticker.

## Character Audit
- [x] Investigator
- [x] Security Analyst
- [x] Data Detective
- [x] Tree Builder
- [x] Model Reviewer
- [x] Security Team Lead
- [x] ML Engineer
- [x] Dataset Dealer
- [x] Feature Selector
- [x] Decision Aggregator
- [x] Training Gatekeeper
- [x] Model Inspector
- [x] Security Reviewer
- [x] Evidence Gatekeeper
- [x] Mission Commander
- [x] Plan Reviewer
- [x] ML Builder
- [x] Security Investigator
- [x] Learning Guide
- [x] Handoff Engineer

Adjacent slides should avoid identical pose unless deliberately used as a visual callback.

---

# 10. Canonical Lesson Closure

```text
L5 — Train the classifier.
L6 — Understand the classifier's decisions.
L7 — Evaluate the classifier's security consequences.
```

**L6 CORE MEMORY:**

> **Understand the model before judging the model.**

> **AI CLAIM ≠ VERIFIED EVIDENCE.**

> **Accuracy is not enough for cybersecurity.**
