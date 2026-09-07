# AIIS_L5 — Slides S07–S12

> Continuation of: `2026-09-07-AIIS-L5-CRISP-DM-Security-Classification-Plan-and-Slides-00-06.md`
> Phase: LEARN
> CRISP-DM focus: Data Understanding → Data Preparation
> Core Tool: pandas + scikit-learn preparation workflow
> Shared Context: AI Weather Security Center

---

# Slide 07 — Observation / Sample：模型一次看到一筆什麼？

## 目的
讓學生把抽象的 Dataset 拆成「一列 = 一個觀察案例」，建立後續 Feature / Label 的共同語言。

## 投影片內容

Dataset 不是一大團資料。

它由很多筆 **Observation / Sample** 組成。

| failed_login | requests/min | new_device | label |
|---:|---:|---:|---|
| 0 | 8 | 0 | Normal |
| 1 | 12 | 0 | Normal |
| **8** | **160** | **1** | **Suspicious** |
| 12 | 220 | 1 | Suspicious |

把第三列拿出來：

```text
Observation #003
────────────────
failed_login = 8
requests/min = 160
new_device = 1
label = Suspicious
```

**一列資料 = 一個案例 = One Observation / Sample**

## 視覺
左側是一張完整資料表；用放大鏡把其中一列抽出，變成右側 Security Event Card。讓學生感覺 Dataset 是由很多事件卡堆疊而成，而不是抽象 CSV。

## 煥哥
拿起其中一張 Event Card：

> 「先不要看整張表。模型學習的材料，是一筆一筆的案例。」

## 老師講稿
剛才我們說 Data Understanding，要知道資料代表什麼。現在再把它拆細一點。

一個 Dataset 裡面通常有很多 Rows。每一個 Row 可以代表一次登入、一次 API request、一封 email、一個 URL，或一筆交易。

在今天的 Security 情境裡，我們把每一列想成一次 Security Observation。

例如第三筆：登入失敗八次、每分鐘 160 個 requests，而且是新裝置。過去人工確認的結果是 Suspicious。

模型不是看到「這個人看起來很可疑」。它看到的是這些被記錄下來的 observation values。

## 問
如果 Dataset 有 10,000 rows，通常代表什麼？

## 預期答案
大致代表有 10,000 個 observations / samples / cases；實際意義仍要依 Dataset 定義確認。

## 老師補充 / 板書

```text
Dataset
  ├─ Sample 1
  ├─ Sample 2
  ├─ Sample 3
  └─ ...
```

## 核心句
> **One row usually represents one observation the model can learn from.**

## Transition
一筆 Observation 裡有很多欄位，但哪些欄位是模型拿來判斷的「線索」？

---

# Slide 08 — Feature X：模型可以看的線索

## 目的
正式建立 Feature 與 X 的概念，並讓學生理解 Feature 是對真實世界的資料表示，而不是答案本身。

## 投影片內容

### Feature = 模型用來判斷的輸入線索

今天選三個 Features：

```text
failed_login
requests_per_minute
new_device
```

一筆 Observation：

```text
X = [8, 160, 1]
```

多筆資料：

```text
X =
[
  [0,   8, 0],
  [1,  12, 0],
  [8, 160, 1],
  [12,220, 1]
]
```

### X = 給模型看的輸入資料

## 視覺
偵探桌概念：三張證據卡 `Failed Login`、`Request Rate`、`New Device`，箭頭集中到 ML Model。右下角標示 `FEATURES = CLUES`。

## 煥哥
拿放大鏡：

> 「Feature 就像模型手上的線索。」

## 老師講稿
Feature 是 Machine Learning 一定會一直遇到的字。

可以把它想成模型做判斷時能夠使用的線索。

醫療模型可能看年齡、血壓、檢驗值；房價模型可能看坪數、屋齡與地點；Security Model 可能看登入失敗次數、request rate 或裝置狀態。

我們常把所有 Features 寫成大寫 X。

所以之後看到 `X_train`、`X_test`，先不要被符號嚇到。X 的核心意思就是：**模型可以看的輸入資料。**

但 Feature 不是「越多越好」。無關、錯誤、洩漏答案或不應使用的敏感資料，都可能讓模型產生問題。

## 問
使用者的明文密碼應不應該直接當 Feature？

## 預期答案
不應該。除了預測價值，還涉及安全、隱私與資料治理；Feature 選擇本身也是 Security Engineering 的一部分。

## 老師補充 / 板書

```text
X = Features = Inputs = Clues
```

## 核心句
> **Feature = what the model is allowed to see.**

## Transition
模型有了線索，但 Supervised Learning 還缺少一樣東西：過去案例的正確答案。

---

# Slide 09 — Label y：我們告訴模型的已知答案

## 目的
建立 Label / target / y 概念，讓學生真正理解 Supervised Learning 為何是「有答案的學習」。

## 投影片內容

同一筆資料：

```text
Features X
[8, 160, 1]
      ↓
Known Answer
Suspicious
```

這個已知答案叫：

# Label / Target

今天定義：

```text
0 = Normal
1 = Suspicious
```

因此：

```text
X = [8, 160, 1]
y = 1
```

### Supervised Learning

訓練時：**X 與 y 都已知。**

## 視覺
用老師批改考卷的概念：左側是 Features 題目卡，右上角有人工確認過的 `Suspicious ✓`。畫面下方將 X 與 y 用不同區塊分開。

## 煥哥
拿著答案卡：

> 「這一次不是 AI 當老師，是我們把過去的答案交給 AI 學。」

## 老師講稿
為什麼叫 Supervised Learning？可以把它想成學習時有老師提供已知答案。

我們不只給模型 `failed_login = 8`、`requests/min = 160`、`new_device = 1`，還告訴它：這筆過去經過確認，是 Suspicious。

這個答案就是 Label，也常叫 Target，通常寫成小寫 y。

所以今天最重要的兩個符號是：X 是模型看的 Features；y 是希望模型學會預測的答案。

真正的 Dataset 裡，Label 從哪裡來是一個非常重要的問題。可能來自 Analyst review、incident record 或其他可信流程。如果 Label 本身錯很多，模型就會學錯。

## 問
如果我們只有大量 Security Events，但從來沒有人確認哪些 Normal、哪些 Suspicious，可以直接做今天這種 supervised classification 嗎？

## 預期答案
不能直接照今天的標準流程做；因為缺少可靠的 y / labels。可能需要先建立標註流程或採用其他方法，但不在本課展開。

## 老師補充 / 板書

```text
X = What the model sees
y = What we want it to learn
```

## 核心句
> **Features are the clues; labels are the known answers.**

## Transition
現在有 X 和 y 了，是不是可以直接 `model.fit()`？還不行。CRISP-DM 還有 Phase 3。

---

# Slide 10 — Phase 3：Data Preparation

## 目的
讓學生理解「有資料」與「有可訓練資料」是兩回事，正式進入 CRISP-DM Data Preparation。

## 投影片內容

CRISP-DM Navigation：

```text
① Business Understanding ✓
② Data Understanding     ✓
③ DATA PREPARATION       ← NOW
④ Modeling
⑤ Evaluation
⑥ Deployment
```

Raw Security Data：

```text
logs / CSV / DB / events
        ↓
select
clean
encode
organize
        ↓
MODEL-READY DATA
```

核心問題：

> **Can the model actually use this data?**

## 視覺
左側是一堆凌亂 Security Logs；中央是一個 Data Preparation 清理工作台；右側輸出乾淨矩陣 `X` 與 `y`。CRISP-DM 地圖 Phase 3 高亮。

## 煥哥
戴上工作手套整理資料：

> 「Raw Data 不等於 Training Data。」

## 老師講稿
這一步常常比大家想像中花更多時間。

系統真正產生的資料可能是 logs、JSON、CSV 或 Database records。裡面可能有缺值、文字、錯誤格式、無關欄位，甚至重複資料。

模型不會因為檔名叫 `security_data.csv` 就自動理解它。

Data Preparation 的工作，是把我們理解過的資料整理成模型真正可以使用的形式。

今天只教最基本的三件事情：Select、Clean、Encode。不要在 L5 把資料工程展開成另一門課。

## 問
Data Preparation 是不是只為了讓 Python 不報錯？

## 預期答案
不是。它也決定模型實際看到什麼資訊，因此會直接影響模型學到的模式與結果可信度。

## 核心句
> **Raw data must become model-ready data.**

## Transition
那今天最小可行的 Data Preparation 到底要做哪些事？

---

# Slide 11 — Select → Clean → Encode

## 目的
用一頁建立學生可操作的 Data Preparation 最小流程，不在 L5 發散到完整 Feature Engineering。

## 投影片內容

### 1. SELECT — 選模型需要的欄位

```text
failed_login
requests_per_minute
new_device
label
```

### 2. CLEAN — 檢查資料品質

```text
Missing?
Wrong type?
Impossible value?
Duplicate?
```

### 3. ENCODE — 轉成模型可用表示

```text
No  → 0
Yes → 1

Normal     → 0
Suspicious → 1
```

最後得到：

```text
X → numeric features
y → numeric labels
```

## 視覺
做成三站式資料處理輸送帶：`SELECT → CLEAN → ENCODE`。一筆原始 Event 經過三站後變成 `[8,160,1] → 1`。

## 煥哥
站在輸送帶旁：

> 「不是把資料洗漂亮，是把資料變成有意義、可使用的表示。」

## 老師講稿
今天我們只抓住三個最基本動作。

第一 Select：不是 Database 有什麼欄位就全部丟進模型，而是根據問題選擇合理的 Features 與 Label。

第二 Clean：看看有沒有 missing values、型別錯誤、不合理數值或重複資料。

第三 Encode：模型通常需要適當的數值表示。例如 `new_device = Yes` 可以轉成 1，No 轉成 0；今天的 Normal / Suspicious Label 也可以編成 0 / 1。

但要提醒：真實世界的 Encoding 可以更複雜。L5 的目的不是把所有 preprocessing 技巧一次教完，而是讓學生知道 `model.fit()` 前面有一個必要的資料工程階段。

## 問
如果 `new_device` 是 Yes / No，我們為什麼可能把它轉成 1 / 0？

## 預期答案
把類別資訊轉成模型可以處理的數值表示，同時保留原本 Yes / No 的意義。

## 老師補充 / 板書

```text
RAW DATA
   ↓
SELECT
   ↓
CLEAN
   ↓
ENCODE
   ↓
X + y
```

## 核心句
> **Data preparation decides what information reaches the model.**

## Transition
現在資料終於可以拿來訓練了。但還有一個很容易犯的大錯：把全部資料都拿去 Training。

---

# Slide 12 — Train / Test Split：不能拿考古題當期末考

## 目的
建立 Train/Test Split 的直覺與實驗紀律，為 S13 Modeling 與 L7 Evaluation 奠定基礎。

## 投影片內容

先把 Dataset 分開：

```text
            DATASET
              │
       ┌──────┴──────┐
       │             │
   TRAIN SET      TEST SET
     80%             20%
       │             │
    LEARN         CHECK LATER
```

Python 概念：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Golden Rule

> **Test data must stay unseen during training.**

## 視覺
用「練習題 vs 期末考」的教室比喻。左邊 TRAIN：學生拿到題目與答案練習；右邊 TEST：考卷先放進封套，直到模型訓練完成才打開。中間畫一道清楚隔離線。

## 煥哥
雙手擋住 Test Set：

> 「這 20% 先藏起來。不能偷看！」

## 老師講稿
假設我們有 1000 筆資料。如果全部拿去 Training，然後又拿同樣 1000 筆問模型答得準不準，這不公平。

就像老師把期末考題和答案全部給學生背，最後再用同一份考卷測驗。考 100 分也不能證明學生真的能解新的問題。

所以最基本的做法，是先把資料分成 Training Set 與 Test Set，例如 80% / 20%。

Training Set 用來學習；Test Set 先收起來，模型 Training 完成後才拿出來檢查。

今天先建立這個觀念。到了 L7，我們才深入問：Test Set 上到底要用 Accuracy、Precision、Recall 還是其他指標？在 Security 裡，不同錯誤的成本是不是一樣？

## 問
模型在 Training Set 得到 100% Accuracy，是不是代表它已經可以部署？

## 預期答案
不是。Training performance 不能代表對未見資料的表現，還需要 Test / Evaluation；也可能發生 overfitting。

## 老師補充 / 板書

```text
TRAIN ≠ TEST
學習資料 ≠ 考試資料
```

`Overfitting` 在此只 Preview，不深入；完整模型行為與評估留給後續課程。

## 核心句
> **Never judge a model only with the data it learned from.**

## Transition
我們現在完成了 CRISP-DM 前三個階段：

```text
① Business Understanding ✓
② Data Understanding     ✓
③ Data Preparation       ✓

Security Problem
      ↓
Classification
      ↓
Observations
      ↓
Features X + Labels y
      ↓
Prepared Data
      ↓
Train / Test
```

下一站終於進入：

# ④ MODELING

S13 開始建立第一個真正的 Security Classifier。

---

## Batch Completion Check

S07–S12 完成後，學生應能回答：

1. Dataset 中的一列代表什麼？
2. Feature / X 是什麼？
3. Label / y 是什麼？
4. 為什麼 Raw Data 不能直接假設可訓練？
5. Data Preparation 至少包含哪些基本動作？
6. 為什麼 Train 與 Test 必須分開？
7. 目前走到 CRISP-DM 哪一個位置？

## Next Batch

**S13–S18 — Phase 4 Modeling → Rule-based vs Learning → First Classifier → `fit()` → `predict()` → First Security Prediction**
