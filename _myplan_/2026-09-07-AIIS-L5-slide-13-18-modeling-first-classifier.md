# AIIS_L5 — Slides S13–S18
## CRISP-DM Phase 4 Modeling → First Security Classifier

> Parent plan: `2026-09-07-AIIS-L5-CRISP-DM-Security-Classification-Plan-and-Slides-00-06.md`
> Previous batch: S07–S12
> Status: Canonical teaching-script batch
> Core Tool: scikit-learn
> Model for L5: Logistic Regression
> Boundary: Decision Tree / Random Forest depth belongs to L6; full metrics and security cost belong to L7.

---

# Slide 13 — Phase 4：Modeling，現在才輪到模型

## 目的
把前面 Business Understanding、Data Understanding、Data Preparation 串回 CRISP-DM，讓學生理解 Modeling 是第四階段，而不是 ML Project 的起點。

## 投影片內容

CRISP-DM progress:

`① Business Understanding ✓`

`② Data Understanding ✓`

`③ Data Preparation ✓`

### `④ MODELING ← NOW`

我們現在才問：

- Which model should we use?
- How do we train it?
- What patterns can it learn?
- Can it predict unseen observations?

今天只使用一個代表性模型：

# Logistic Regression

用途：

**Binary Classification**

`Normal / Suspicious`

## 視覺
持續使用六階段 CRISP-DM 導航圖，Phase 4 高亮。右側不是演算法大全，而只放一個簡單 classifier box：

`X_train + y_train → Logistic Regression → trained model`

## 煥哥
> 終於可以建 Model 了！但今天只學一個。

## 老師講稿
做到這裡，我們才真正來到 Modeling。這是我要大家記住 CRISP-DM 的原因。很多 Machine Learning 教學第一頁就建立 model，但真正做專案時，在這之前我們已經做了很多重要決策：問題是什麼、資料代表什麼、哪些是 Feature、Label 是什麼、資料如何準備、Train/Test 如何分開。

今天我們也不做 Algorithm Zoo。我們只選一個代表性模型 Logistic Regression，目標是把完整流程真正走通。名稱雖然有 Regression，但它非常常用於 Classification；數學細節不是本課主線。

## 問
為什麼今天不一次比較五種 classifier？

## 預期答案
因為本課核心是理解完整 supervised classification workflow，而不是比較演算法；其他模型後續再深化。

## 老師補充 / 板書
`CRISP-DM: Model is Phase 4, not Phase 1.`

## 核心句
> Modeling starts after we understand the problem and prepare the data.

## Transition
但是 Logistic Regression 和我們以前自己寫 if-else 規則，到底差在哪裡？

---

# Slide 14 — Rule-based vs Learning：規則誰決定？

## 目的
讓學生清楚區分人工規則系統與 supervised learning，建立「模型從 labeled examples 學參數」的直覺。

## 投影片內容

### Rule-based System

人寫規則：

```python
if failed_login > 5 and requests_per_minute > 100:
    result = "Suspicious"
```

流程：

`Human Rules + Data → Answer`

### Machine Learning

我們提供過去案例：

`Features X + Labels y → Learning Algorithm → Model`

之後：

`New X → Model → Prediction`

大字：

> **Rule-based：人直接寫判斷規則。**
>
> **ML：演算法從 labeled examples 學出可用的判斷模式。**

## 視覺
左右對照。左側工程師手持 RULE BOOK；右側模型前方是一疊 Normal / Suspicious training cards。不要把模型畫成魔法腦袋，重點是 examples → learning → model。

## 煥哥
左側：
> 規則我寫。

右側：
> 案例給模型學。

## 老師講稿
假設我們自己寫 `failed_login > 5`，數字 5 是誰決定的？是人。這就是人工規則。

Machine Learning 的思路不同。我們提供很多 Features 和已知 Labels，演算法從這些 training examples 中調整模型參數，希望得到可以對新資料做預測的模型。

這不表示 Rule-based 不好。很多 Security Control 非常適合明確規則；Machine Learning 是在資料模式較複雜、規則不容易完整人工描述時，多一種工具。

## 問
如果 `failed_login > 5` 是我們自己寫的，這個 5 是模型學到的嗎？

## 預期答案
不是，是人工指定的規則。

## 核心句
> In rule-based systems, humans write the decision rule; in ML, the model learns patterns from labeled examples.

## Transition
那今天我們要讓哪一個演算法從案例學？

---

# Slide 15 — 第一個 Classifier：Logistic Regression

## 目的
第一次具體建立 scikit-learn classifier；控制程式碼量，讓學生看懂 API 結構而不是陷入數學。

## 投影片內容

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
```

現在的 `model`：

> 還沒有看過我們的 Training Data。

它只是：

**Untrained Model**

今天的任務：

`Untrained Model → Training → Trained Classifier`

## 視覺
三格漫畫式：

1. Empty / Untrained Model
2. Training Data 進入
3. Trained Model ready

不要在本頁出現 sigmoid 公式。

## 煥哥
指著兩行 Python：

> 建立模型很短，真正重要的是前面我們準備了什麼。

## 老師講稿
這就是 scikit-learn 很方便的地方。建立 Logistic Regression 只需要很少程式碼。

但不要被兩行程式騙了。前面我們花了很多時間定義問題、理解資料、決定 X 和 y、準備 Train/Test。這些才是 ML Project 很大的部分。

另外，Logistic Regression 的名字裡有 Regression，但今天它扮演的是 binary classifier。至於它如何用數學產生機率與 decision boundary，可以作為 Further Exploration，不在這一課展開。

## 問
執行 `LogisticRegression()` 後，模型已經學會 Normal / Suspicious 了嗎？

## 預期答案
還沒有。它尚未使用 training data 訓練。

## 老師補充 / 板書
`create model ≠ train model`

## 核心句
> Creating a model object is not the same as training a model.

## Transition
真正讓它開始學習的是下一個動作：`fit()`。

---

# Slide 16 — `model.fit()`：把 Training Examples 交給模型

## 目的
讓學生理解 `fit(X_train, y_train)` 的語意，不把一行 API 當成魔法。

## 投影片內容

```python
model.fit(X_train, y_train)
```

拆開來看：

- `X_train` = Training Features
- `y_train` = Known Training Labels
- `fit()` = Learn from the training examples

流程：

`X_train + y_train → fit() → Trained Model`

我們希望模型學到的是：

> 能夠對沒有看過的新 Observation 做合理判斷的 pattern。

而不是：

> 把 Training Data 背起來。

## 視覺
Training cards 一張張進入 model；卡片上同時有 Features 與 known Label。模型完成後貼上 `TRAINED` 標籤。

## 煥哥
> `.fit()` 很短，但它代表真正的 Training。

## 老師講稿
現在這一行才是 Training。`X_train` 是模型可以看的 Features；`y_train` 是每筆 training observation 的已知答案。

模型透過演算法調整內部參數，讓 Features 和 Labels 之間形成可用於分類的關係。

我們真正希望的不是它只會回答已經看過的資料，而是之後看到新的 observation 仍然能做合理預測。這叫 generalization。Overfitting 在這裡只先記住概念，L6 再深入。

## 問
可以寫成 `model.fit(X_test, y_test)` 嗎？

## 預期答案
不應該。Test Set 應保留給訓練後的評估，不應拿來訓練。

## 老師補充 / 板書
`TRAIN → fit()`

`TEST → later evaluation`

## 核心句
> `fit()` means learning from training examples—not learning from the test set.

## Transition
模型訓練完成後，我們終於可以給它一筆沒看過的資料。

---

# Slide 17 — `model.predict()`：讓模型面對新的 Observation

## 目的
建立 inference / prediction 的第一個直覺，清楚區分 Training 與 Prediction。

## 投影片內容

訓練：

```python
model.fit(X_train, y_train)
```

預測：

```python
prediction = model.predict(X_test)
```

兩個不同動作：

`FIT = Learn`

`PREDICT = Use what was learned`

對一筆新的 Security Observation：

```text
failed_login = 9
requests_per_minute = 175
new_device = 1
```

模型輸出：

`Suspicious`

## 視覺
上下兩段。上段 TRAINING：大量 labeled examples → model。下段 INFERENCE：一張沒有顯示答案的新 observation → trained model → prediction。

## 煥哥
> 訓練時有答案；預測時模型先不能偷看答案。

## 老師講稿
`fit()` 和 `predict()` 一定要分清楚。

Training 時我們把 X 和 y 都交給模型，因為它正在學。

Prediction 時，真正使用模型的情境是只看到新的 Features。模型要根據已經學到的 pattern 產生 prediction。

如果我們在 prediction 前就把真正 Label 告訴模型，那就失去測試意義。

## 問
Prediction 和 Label 是同一件事嗎？

## 預期答案
不是。Prediction 是模型猜的結果；Label / Ground Truth 是我們用來比較的已知真實答案。

## 老師補充 / 板書
`Prediction ≠ Ground Truth`

這句為 L7 埋伏筆。

## 核心句
> Training learns from known answers; prediction applies the learned model to unseen inputs.

## Transition
現在把整個流程放回我們的 Security 情境，看第一個 prediction 到底代表什麼。

---

# Slide 18 — First Security Prediction：模型說 Suspicious，然後呢？

## 目的
完成 L5 第一個可感知的 ML 成果，同時避免把 prediction 當作 security truth，為 Evaluation 鋪路。

## 投影片內容

### New Security Observation

| Feature | Value |
|---|---:|
| failed_login | 9 |
| requests/min | 175 |
| new_device | 1 |

```python
new_event = [[9, 175, 1]]
prediction = model.predict(new_event)
```

### Model Prediction

# `SUSPICIOUS`

但是：

> **Prediction is a model output, not proof of an attack.**

Security workflow:

`Observation → ML Prediction → Analyst Review → Security Decision`

## 視覺
中央放大一張 Security Event Card。模型輸出 `SUSPICIOUS` 黃色警示，而不是紅色「ATTACK CONFIRMED」。右側 Security Analyst 進行 Review。

## 煥哥
不要拿法槌，而拿檢查板：

> AI 提醒我「值得看」，不是替我宣布「有罪」。

## 老師講稿
這是今天非常重要的一刻。我們第一次把一筆新的 Security Observation 交給自己訓練的 classifier，它輸出 Suspicious。

但是在 Security 情境裡，我不希望學生建立一個錯誤觀念：AI 說 Suspicious 就代表 Attack Confirmed。

模型可能犯錯。正常使用者也可能突然有大量 Requests；新裝置也不代表一定惡意。因此更合理的角色是讓模型協助 Analyst 篩選值得優先查看的事件。

下一步自然產生一個問題：我們怎麼知道模型到底靠不靠得住？這正好帶進 CRISP-DM Phase 5 Evaluation。

## 問
如果模型把一個正常事件預測成 Suspicious，發生了什麼？

## 預期答案
模型做錯分類。此處只建立「模型會犯錯」概念；False Positive 名稱與成本留到 L7 深入。

## 核心句
> A security prediction is evidence for review—not automatic proof of an attack.

## Transition
我們已經完成 Modeling：

`Model → fit() → predict() → First Security Prediction`

現在 CRISP-DM 地圖要往下一格：

### `⑤ EVALUATION`

問題從「模型會不會預測？」變成：

> **How do we know whether we can trust its performance?**

---

## Batch Teaching Checkpoint

學生到 S18 應能回答：

1. Modeling 為什麼是 CRISP-DM Phase 4，而不是第一步？
2. Rule-based system 與 ML classifier 的主要差異是什麼？
3. `LogisticRegression()`、`fit()`、`predict()` 各代表什麼？
4. `X_train` 和 `y_train` 分別是什麼？
5. 為什麼不能用 Test Set 訓練？
6. Prediction 為什麼不等於 Ground Truth？
7. Security Analyst 為什麼仍然需要參與判斷？

## Boundary Check

本批刻意不深入：

- Logistic Regression 數學推導 / sigmoid
- Decision Tree / Random Forest implementation
- Hyperparameter tuning
- Confusion Matrix
- Precision / Recall / F1
- False Positive / False Negative 的正式成本分析

這些內容依課程 ownership 分別留給 L6 / L7。

## Next Batch

S19–S22 + Lab / Evidence / Handoff：

`Phase 5 Evaluation Preview → Prediction ≠ Truth → Phase 6 Deployment Preview → Weather Security Center Integration → CRISP-DM Lab → Evidence → L6 Handoff`
