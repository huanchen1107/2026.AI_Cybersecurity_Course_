# AIIS_L5 — Slides S19–S22 + Lab + Evidence + Handoff
## Complete the First CRISP-DM Security Classification Cycle

> Date: 2026-09-07
> Status: Canonical teaching-script batch
> Parent lesson: AIIS_L5 — CRISP-DM × Security Classification Foundations
> Previous batch: S13–S18 Modeling / Logistic Regression / fit / predict
> Core Tool: scikit-learn
> Shared Project Context: AI Weather Security Center

---

# Slide 19 — Phase 5：Evaluation，不是「會跑」就代表「可用」

## 目的
把學生從「模型成功輸出 prediction」帶到「我們必須驗證模型表現」；只建立 Evaluation 的必要性，不提前深入 L7 metrics。

## 投影片內容

CRISP-DM progress:

`① Business Understanding ✓`

`② Data Understanding ✓`

`③ Data Preparation ✓`

`④ Modeling ✓`

### `⑤ EVALUATION ← NOW`

模型已經可以：

`New Observation → Prediction`

但我們還不知道：

- How often is it correct?
- What kinds of mistakes does it make?
- Are those mistakes acceptable for security use?
- Does it actually solve the original security problem?

大字：

> **A model that runs is not automatically a model we can trust.**

## 視覺
左側 CRISP-DM 六環，Phase 5 高亮。右側一個 model 顯示 `RUNNING ✓`，但旁邊仍有大型問號 `TRUST ?`。

## 煥哥
> 跑得動，只證明程式沒有在這裡停掉；不代表模型判得好。

## 老師講稿
剛才我們已經看到 model.predict() 真的輸出了 Suspicious。初學者很容易在這裡非常興奮，覺得 AI 完成了。

但是從工程角度，能輸出答案和答案值得信任，是完全不同的事情。

Evaluation 要回答的不是只有「Accuracy 是多少」，而是模型犯了什麼錯、這些錯誤在 Security 情境裡有什麼影響，以及模型是否真的解決一開始 Business Understanding 定義的問題。

今天只建立這個觀念。Confusion Matrix、Precision、Recall、F1，以及不同 Security Error 的成本，會在 L7 正式深入。

## 問
如果一個模型每次都能輸出 Normal 或 Suspicious，它算完成 Evaluation 了嗎？

## 預期答案
沒有。能輸出 prediction 不代表 prediction 的品質已被驗證。

## 老師補充 / 板書
`RUNNING ≠ RELIABLE`

## 核心句
> Evaluation asks whether the model is useful and trustworthy for the original problem—not merely whether it runs.

## Transition
為什麼 Security 特別需要小心？因為 Prediction 和 Truth 是兩回事。

---

# Slide 20 — Prediction ≠ Truth：模型一定可能犯錯

## 目的
建立 prediction、ground truth、model error 三者的關係，為 L7 的 FP/FN 正式教學埋下需求。

## 投影片內容

一筆事件有兩個不同概念：

### Model Prediction

模型說：

`SUSPICIOUS`

### Ground Truth

經過後續確認：

`NORMAL`

因此：

`Prediction ≠ Ground Truth`

模型可能：

- 猜對
- 猜錯

Security 問題：

> 不同種類的錯誤，代價可能完全不同。

今天先記住這句，不展開公式。

## 視覺
畫兩張並排卡片：左為 AI Prediction，右為 Analyst / verified Ground Truth。中間可出現 `MATCH ✓` 或 `MISMATCH !`。

## 煥哥
> AI 有答案，不代表 AI 就是答案。

## 老師講稿
這裡是整個 AI Security 課程很重要的態度。

Prediction 是模型輸出。Ground Truth 是我們用來判斷這個輸出是否正確的參考真實答案。

例如模型說 Suspicious，但經過 Analyst 調查發現只是正常使用者換了新裝置並突然大量查詢。這時模型就做錯了。

反過來也可能發生：真正有問題的事件被模型判成 Normal。

哪一種錯比較嚴重？這就開始涉及 Security Cost。今天不急著給名稱和公式，因為 L7 會把這個問題完整展開。

## 問
Security Model 的 Accuracy 很高，就一定安全嗎？

## 預期答案
不一定。還需要了解模型錯在哪些類型，以及不同錯誤的 Security Cost。

## 核心句
> Prediction is what the model says; ground truth is what actually happened or was verified.

## Transition
如果 Evaluation 顯示模型真的具有使用價值，CRISP-DM 最後還有一個階段。

---

# Slide 21 — Phase 6：Deployment，不是把 `.py` 丟到 Server

## 目的
建立 Deployment 的工程概念：模型必須進入可被使用、監控、更新的 workflow，而不是單純部署檔案。

## 投影片內容

CRISP-DM:

`① Business Understanding ✓`

`② Data Understanding ✓`

`③ Data Preparation ✓`

`④ Modeling ✓`

`⑤ Evaluation ✓ / Preview`

### `⑥ DEPLOYMENT ← NOW`

Deployment 不是只有：

`model.py → server`

而是：

`Security Event → Same Feature Preparation → Model → Prediction → Analyst Workflow`

還要考慮：

- How will predictions be shown?
- Who reviews them?
- What evidence is recorded?
- What happens when data changes?
- When should the model be retrained?

## 視覺
完整 operational pipeline。左邊 Weather Security Center Event，中間 Feature Preparation + Model，右邊 Analyst Dashboard / Review。下方一條 Feedback arrow 回到 future data / retraining。

## 煥哥
> Deployment 的意思是「進入工作流程」，不是「檔案上線」。

## 老師講稿
在 CRISP-DM 裡 Deployment 的意義比「把 Python 放到 Server」更完整。

真正重要的是：模型如何進入人的工作流程。

新的 Security Event 來了，必須用和 Training 相容的方式準備 Features，再交給模型。Prediction 要顯示給誰？Analyst 如何 Review？最後確認結果是否留下 Evidence？如果未來資料型態改變，模型是否還適用？

所以 Deployment 本身仍然是一個 Engineering Problem。

今天不要求學生真的建立 Production ML Platform。我們只把這個概念接回共同的 Weather Security Center。

## 問
如果 Training 時 `new_device` 用 0/1，但部署後傳入 Yes/No 字串，可能有問題嗎？

## 預期答案
有。Training 與 Deployment 的 feature preparation 必須一致。

## 老師補充 / 板書
`TRAINING PIPELINE ≈ INFERENCE PIPELINE`

## 核心句
> Deployment means putting the model into a usable, reviewable workflow with consistent data preparation.

## Transition
那麼我們這個第一個 classifier 應該放在 Weather Security Center 的哪裡？

---

# Slide 22 — 回到 Weather Security Center：AI 不是取代 Analyst，而是增加一層判斷能力

## 目的
把整堂 ML 課重新接回共享專案，形成 BUILD → SECURE → LEARN 的連續故事，而不是孤立的 sklearn 教學。

## 投影片內容

### Before L5

`Weather Security Center → Events / Logs → Human Review`

### After L5

`Weather Security Center → Security Observation → Feature Preparation → ML Classifier → Normal / Suspicious → Analyst Review`

新增的能力：

# ML-assisted Triage

不是：

`AI → Automatic punishment / block everything`

而是：

`AI Prediction → Prioritize → Human Review → Decision`

## 視覺
使用 Weather Security Center 架構圖，在原系統旁新增一個 ML Classification Module，但 Human Analyst 仍然位於決策鏈末端。CRISP-DM 六階段縮小放右上角，六個階段全部點亮。

## 煥哥
> 我們不是另外做了一個玩具 ML Notebook；我們替原本的系統增加了一個可解釋的學習流程。

## 老師講稿
現在回頭看整堂課，我希望大家發現，我們不是突然離開 Weather Security Center 去做一個完全無關的 Machine Learning 作業。

我們原本建立了一個系統，理解它、保護它；現在開始思考它累積的 Security Data 能不能協助 Security Analyst。

L5 加進來的是一個非常小但完整的 ML capability：把 observation 轉成 features，經過 classifier 產生 prediction，再交給 Analyst review。

這樣 ML 才真正成為 AI for Security 的一部分。

## 問
L5 的最終成果是「一個 Accuracy 數字」嗎？

## 預期答案
不是。成果是從 Security Problem 到 Dataset、Features、Model、Prediction、Review 的完整可重現流程與 Evidence。

## 核心句
> Machine learning becomes useful when it is connected back to the security workflow it was meant to support.

## Transition
現在學生自己走一次完整 CRISP-DM cycle。

---

# LAB — CRISP-DM Security Classification Mini Project

## Lab Mission

使用提供的教學型 Security Event Dataset，完成一個最小但完整的 supervised binary-classification workflow。

核心任務：

> Train one Logistic Regression classifier that predicts `Normal` or `Suspicious`, then explain the result using the six CRISP-DM phases.

## Lab Boundary

本 Lab 只使用課程提供的離線／模擬 Security Dataset，不要求學生對任何外部網站、真實第三方系統或未授權目標進行掃描或攻擊。

## Dataset Schema — Representative Teaching Dataset

建議至少包含：

| Column | Meaning | Role |
|---|---|---|
| `failed_login` | recent failed login count | Feature |
| `requests_per_minute` | request rate | Feature |
| `new_device` | whether source device is new, encoded 0/1 | Feature |
| `label` | Normal / Suspicious | Target |

可增加少量非核心欄位供學生判斷是否應作 Feature，但不要讓資料準備壓過本課 Classification Foundations。

---

## Lab Step 1 — Business Understanding

學生用一句話完成：

> Security Analyst needs help prioritizing large numbers of events, so we will build a classifier to distinguish Normal from Suspicious observations.

### Evidence
`business_problem.md` 或 Notebook / worksheet 中的一段 Problem Statement。

---

## Lab Step 2 — Data Understanding

學生必須：

1. Load dataset
2. `head()` 查看前幾筆
3. 查看欄位
4. 確認 Label 值
5. 確認 Missing Values
6. 用自己的話解釋每個核心欄位

代表性程式：

```python
import pandas as pd

df = pd.read_csv("security_events.csv")
print(df.head())
print(df.info())
print(df["label"].value_counts())
```

### Evidence
Dataset preview + field interpretation。

---

## Lab Step 3 — Data Preparation

建立：

```python
features = [
    "failed_login",
    "requests_per_minute",
    "new_device",
]

X = df[features]
y = df["label"]
```

如果 `new_device` 原始資料是 Yes/No，先轉成一致 numeric representation。

確認：

- X 不包含 label
- y 是 target
- 不使用明顯 identifier 當核心 predictive feature
- Missing Values 已處理或確認不存在

### Evidence
`X.head()` / `y.head()` + feature list。

---

## Lab Step 4 — Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

學生必須回答：

> Why must the test set remain unseen during training?

### Expected Answer
因為 Test Set 用來模擬模型面對未見資料的情境；若拿 Test Data 訓練，就無法公平檢查 generalization。

### Evidence
Train/Test shape + written explanation。

---

## Lab Step 5 — Modeling

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

學生標記：

- Model object
- Training features
- Training labels
- `fit()`

### Evidence
可重現的 training code。

---

## Lab Step 6 — First Prediction

```python
prediction = model.predict(X_test)
print(prediction[:10])
```

另外建立一筆教學型 observation：

```python
new_event = pd.DataFrame([
    {
        "failed_login": 9,
        "requests_per_minute": 175,
        "new_device": 1,
    }
])

print(model.predict(new_event))
```

學生必須用文字解釋：

> The model prediction is a triage signal for analyst review, not proof that an attack occurred.

### Evidence
Prediction output + interpretation。

---

## Lab Step 7 — Evaluation Preview

本課只要求最基本的 hold-out score 作為「需要 Evaluation」的入口，不深入解釋 metrics：

```python
score = model.score(X_test, y_test)
print(score)
```

老師必須立即提醒：

> One score is not enough to understand a security classifier.

學生回答：

- 模型可能犯錯嗎？Yes.
- Accuracy 高是否代表所有 Security Error 都可以接受？No.
- 下一步需要知道什麼？模型錯在哪些類型。

正式的 Confusion Matrix / Precision / Recall / F1 / FP / FN 留給 L7。

### Evidence
Basic test score + limitation statement。

---

## Lab Step 8 — Deployment Preview

學生不必真正部署 Production Model，只畫出 integration flow：

`Weather Security Center → Event → Feature Preparation → Classifier → Prediction → Analyst Review`

並寫出至少一個 deployment concern，例如：

- Feature encoding must stay consistent.
- New data may differ from training data.
- Predictions should be logged for review.
- Human review remains required for consequential security action.

### Evidence
One workflow diagram + one deployment concern。

---

# LAB FINAL EVIDENCE PACK

學生提交的不是只有 `.py` 檔，而是一條完整 evidence chain：

1. **Problem Evidence** — Security problem statement
2. **Data Evidence** — dataset preview / schema understanding
3. **Preparation Evidence** — X / y / selected features
4. **Split Evidence** — train/test separation
5. **Model Evidence** — Logistic Regression + `fit()`
6. **Prediction Evidence** — test / new observation prediction
7. **Evaluation Evidence** — basic score + limitation statement
8. **Deployment Evidence** — Weather Security Center integration diagram

Canonical evidence chain:

`Security Problem → Dataset → Features X / Label y → Train/Test → Model → Prediction → Evaluation → Security Workflow`

---

# Reflection — 六個問題把 CRISP-DM 說回來

學生應能不用看程式回答：

1. **Business Understanding** — 我們真正要解決的 Security Problem 是什麼？
2. **Data Understanding** — Dataset 每一列與每一欄代表什麼？
3. **Data Preparation** — 哪些欄位成為 X？哪一欄是 y？資料做了哪些處理？
4. **Modeling** — 使用什麼 classifier？`fit()` 做什麼？
5. **Evaluation** — 為什麼 model 可以 predict 還不代表可以信任？
6. **Deployment** — 模型如何進入 Weather Security Center / Analyst workflow？

如果學生只能背 `train_test_split()`、`fit()`、`predict()`，但無法回答這六題，代表還沒有真正完成 L5 的學習目標。

---

# L5 → L6 Handoff

L5 已回答：

> How do we complete a first supervised security-classification cycle?

學生現在已經知道：

`Problem → Data → Prepare → Train → Predict → Evaluate → Deploy`

但新的問題出現：

> Logistic Regression 是唯一選擇嗎？
>
> 如果 Security Data 的判斷規則不是簡單線性關係呢？
>
> 有沒有一種模型可以像一連串問題一樣做判斷，而且比較容易讓人看到它在問什麼？

這帶入：

# AIIS_L6 — Supervised ML II: Tree Models

L6 ownership:

`Decision Tree → Random Forest → Feature Importance → Overfitting → Security Model Interpretation`

L5 不提前教完這些內容。

---

# L5 Final Audit

## Storyline Audit

PASS:

`L4 SECURE → Security Data Problem → CRISP-DM → Classification → First Model → Prediction → Evaluation Preview → Deployment Preview → Weather Security Center → L6 Modeling Depth`

## CRISP-DM Audit

PASS — all six phases appear as one connected project cycle rather than isolated definitions.

## One Core Tool Audit

PASS — scikit-learn.

## One Representative Model Audit

PASS — Logistic Regression only for the L5 implementation.

## Persistent Project Audit

PASS — Weather Security Center remains the shared system context.

## AI for Security Audit

PASS — ML is used to support security-event triage; course does not branch into Security for AI.

## Lesson Boundary Audit

PASS:

- Tree / Random Forest depth → L6
- Full security evaluation metrics / FP-FN cost → L7
- Deep Learning → later lessons
- No RL in formal curriculum

## Safety / Authorization Audit

PASS — L5 uses offline / simulated / course-provided security observations; no external target interaction is required.

## Teaching Style Audit

PASS — Slide 00 + S01–S22 use L1-style purpose, slide content, visual, teacher script, questions/core sentence/transition as appropriate.

---

# AIIS_L5 Completion Status

**Content design: COMPLETE**

Canonical slide sequence:

`Slide 00 + S01–S22 + Lab + Evidence + Reflection + L6 Handoff`

Next recommended repository action:

1. Create / update the L5 canonical lesson README from these `_myplan_` artifacts.
2. Verify S07–S12 artifact is present and consistent.
3. Create an `AIIS-L5-COMPLETE.md` index pointing to all L5 planning files.
4. Freeze L5 after cross-file consistency audit.
