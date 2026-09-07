# AIIS_L5 — CRISP-DM × Security Classification Foundations

> Status: Canonical draft in progress
> Date: 2026-09-07
> Phase: LEARN
> Core Tool: scikit-learn
> Shared Project Context: AI Weather Security Center

## 1. Lesson Position

L5 is the first formal Machine Learning lesson after the BUILD / MANAGE / UNDERSTAND / SECURE sequence. The lesson changes the student role from using AI-assisted engineering tools to building a small supervised-learning capability from security-related data.

Core transition:

`BUILD → MANAGE → UNDERSTAND → SECURE → LEARN FROM DATA`

## 2. Lesson Mission

Teach students to convert a real security problem into a supervised binary-classification problem and complete a first end-to-end ML cycle using CRISP-DM.

Core question:

> Can a machine learn to identify suspicious activity from security data?

## 3. CRISP-DM as the L5–L8 ML Backbone

CRISP-DM is not a one-slide definition. It is the persistent project map for the ML section:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

The process is iterative, not a one-way waterfall.

### Lesson ownership across the ML sequence

- L5: first complete CRISP-DM cycle, with emphasis on classification foundations, features/labels, preparation, train/test, and one simple classifier.
- L6: deepen Phase 4 Modeling with Decision Tree / Random Forest concepts.
- L7: deepen Phase 5 Evaluation with confusion matrix, precision, recall, F1, FP/FN and security cost.
- L8: review/integration and Deployment preview using the shared project context.

## 4. THIS LESSON OWNS

- Security problem → ML problem translation
- CRISP-DM project thinking
- Observation / Sample
- Feature X
- Label y
- Basic data preparation
- Train/test split
- Classification foundations
- One simple scikit-learn classifier
- fit() and predict()
- First security prediction
- Evaluation and deployment only as previews sufficient to complete the first cycle

## 5. THIS LESSON DOES NOT OWN

- Deep Decision Tree / Random Forest teaching — L6
- Full metrics and security error-cost analysis — L7
- Algorithm zoo / broad model comparison
- Deep Learning — later lessons
- Reinforcement Learning — not part of the formal curriculum

## 6. Storyline

`Security Problem → CRISP-DM → Business Understanding → Data Understanding → Observation → Features / Labels → Data Preparation → Train/Test → Modeling → First Classifier → Prediction → Evaluation Preview → Deployment Preview → Evidence → L6`

## 7. Slide Purpose Map

- Slide 00 — L4 → L5: From Secure Software to Learning System
- S01 — Security Analyst cannot inspect unlimited data
- S02 — Do not start with the algorithm
- S03 — CRISP-DM: ML Project Map
- S04 — Phase 1: Business Understanding
- S05 — Security Problem → ML Problem
- S06 — Phase 2: Data Understanding
- S07 — Observation / Sample
- S08 — Feature X
- S09 — Label y
- S10 — Phase 3: Data Preparation
- S11 — Clean / Select / Encode
- S12 — Train / Test Split
- S13 — Phase 4: Modeling
- S14 — Rule-based vs Learning
- S15 — First Classifier
- S16 — model.fit()
- S17 — model.predict()
- S18 — First Security Prediction
- S19 — Phase 5: Evaluation Preview
- S20 — Prediction ≠ Truth
- S21 — Phase 6: Deployment Preview
- S22 — Return to Weather Security Center
- LAB — Complete one representative security classification workflow
- EVIDENCE — Dataset → features → model → prediction
- HANDOFF — L6 deepens Modeling

---

# Slide 00 — 從 Secure Software 走向 Learning System

## 目的
完成 L4 → L5 的階段轉換。讓學生知道前四課主要在建立與保護系統，今天第一次正式進入 Machine Learning。

## 投影片內容

**AIIS_L5 — Supervised Machine Learning I**

### CRISP-DM × Security Classification

我們已經完成：

`BUILD → MANAGE → UNDERSTAND → SECURE`

今天開始：

`LEARN FROM DATA`

核心問題：

> Can a machine learn to identify suspicious activity from security data?

## 視覺
左側 Weather Security Center，中央大量 Security Events 流出，右側 ML Model 將事件分成 NORMAL / SUSPICIOUS。CRISP-DM 六階段環形圖淡放背景，先建立視覺伏筆。

## 煥哥
從 Security Engineer 造型切換為 AI / Data Scientist 造型，手上拿 Security Data。

對話框：

> 前面我們教 AI 幫我們寫系統。今天，我們開始教機器從資料學習。

## 老師講稿
前四課主要在做 Software Engineering 與 Security Engineering。我們建立 Weather Security Center、管理 AI 產生的變更、理解系統並掃描與修正安全問題。今天開始角色稍微改變：系統開始累積很多資料，如果每天十筆，人可以看；如果每天十萬筆呢？我們開始需要問：能不能讓電腦從過去的資料學習，協助判斷新的 Security Event？這就是 L5–L7 的 Machine Learning Journey。

## 核心句
> We built the system. Now we teach it to learn from data.

## Transition
但是做 Machine Learning，第一步是不是馬上選一個 Algorithm？

---

# Slide 01 — Security Analyst 看不完的資料

## 目的
先建立真實 Security Problem，再介紹 ML。

## 投影片內容
Weather Security Center 不斷產生 Login Events、API Requests、Request Rate、Device Information、IP / Source、Errors、Security Alerts 等資料。

- 100 events：可以人工看
- 10,000 events：很困難
- 1,000,000 events：不可能逐筆看

核心問題：

> 哪些值得 Security Analyst 優先注意？

## 視覺
Security Operations Center；大量 Event Cards 湧入 Analyst 的多螢幕工作區，只有少數事件被標記 `!`。

## 煥哥
> 真正的問題不是沒有資料，而是資料多到看不完。

## 老師講稿
資安很多時候不是沒有資料，反而是資料太多。Firewall、Web Server、API、Authentication、Endpoint 都可能產生大量紀錄。真正困難的是哪些值得先看。Machine Learning 在 Security 的典型用途之一，就是協助處理大量資料的分類與排序。模型判定 Suspicious 並不等於那個人一定是攻擊者；這個觀念在 L7 會深入處理。

## 問
如果模型說 Suspicious，我們是不是應該立刻封鎖使用者？

## 預期答案
不一定，需要進一步驗證。

## 核心句
> Security has a data problem before it has an algorithm problem.

## Transition
所以我們是不是現在就搜尋「最厲害的 AI 演算法」？

---

# Slide 02 — 不要從 Algorithm 開始

## 目的
打破初學者「ML = 選演算法」的錯誤認知，為 CRISP-DM 鋪路。

## 投影片內容
常見錯誤：

`我想做 AI → 找最強 Algorithm → 下載 Dataset → model.fit()`

更好的順序：

`我們要解決什麼問題？ → 需要什麼資料？ → 資料代表什麼？ → 才能決定怎麼建模`

大字：

> Problem First. Model Later.

## 視覺
左側學生衝向 Random Forest / XGBoost / Neural Network 工具箱；右側煥哥把焦點拉回 PROBLEM。

## 老師講稿
很多人第一次學 Machine Learning，很容易從 Algorithm 開始：要不要 Neural Network？Random Forest 比較厲害嗎？XGBoost Accuracy 會不會更高？但如果連問題都沒有定義，這就像病人還沒有診斷，已經開始問哪一種藥最厲害。Machine Learning 是一個 Project Process，因此今天需要一張地圖。

## 核心句
> Do not start with the model. Start with the problem.

## Transition
這張 ML Project 地圖，就是今天開始會一直使用的 CRISP-DM。

---

# Slide 03 — CRISP-DM：Machine Learning Project Map

## 目的
正式介紹 CRISP-DM 六階段，建立 L5–L8 共用認知地圖。

## 投影片內容

**CRISP-DM — Cross-Industry Standard Process for Data Mining**

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

> 它不是只能往前走的 Waterfall，而是可以反覆回頭修正的 iterative process。

## 視覺
建立 L5–L8 固定導航圖：六個環形節點，中間為 Security ML Project；目前 Phase 1 高亮。之後每進一階段移動 Highlight。

## 煥哥
> 不要迷路。之後做 ML，我們都回來看這張地圖。

## 老師講稿
CRISP-DM 全名不需要現在背，真正需要記住的是六件事情：我們要解決什麼問題、有什麼資料、資料如何整理、如何建立模型、如何評估、最後如何使用。實務上做到 Modeling 可能發現資料不行而回到 Data Preparation；做到 Evaluation 也可能發現一開始問題定義錯誤。因此它是 iterative process。

## 問
CRISP-DM 哪一個階段寫 `model.fit()`？

## 預期答案
Modeling。

## 老師補充 / 板書
`ML Project > ML Algorithm`

## 核心句
> CRISP-DM gives us a map for the whole ML project—not just model training.

## Transition
所以現在不要碰 `model.fit()`，先做 Phase 1。

---

# Slide 04 — Phase 1：Business Understanding

## 目的
讓學生知道 ML 第一階段不是 Coding，而是定義真正要解決的問題。

## 投影片內容

### ① BUSINESS UNDERSTANDING

先問：

- What problem are we solving?
- Why does it matter?
- Who will use the result?
- What does success mean?

Weather Security Center 情境：

> Security Analyst 無法人工檢查所有活動紀錄。

## 視覺
CRISP-DM 六環持續存在，只有 Phase 1 高亮；右側放 Security Analyst + 大量 Events。

## 煥哥
> 先不要寫 Python。

## 老師講稿
Business 不一定代表賺錢。在我們的情境裡，可以理解為真正的任務與需求。誰使用結果？Security Analyst。為什麼需要？事件量太大。我們希望 AI 做什麼？協助找出值得注意的事件。這些問題都比「我要用 Random Forest」重要。

## 問
「我要做一個 AI Cybersecurity System。」是一個好的 Business Problem 嗎？

## 預期答案
不是，太模糊。

## 核心句
> A good ML project begins with a clearly defined real-world problem.

## Transition
現在把真實世界的 Security Problem 翻譯成 Machine Learning 可以處理的問題。

---

# Slide 05 — Security Problem → ML Problem

## 目的
教學生將 Security Problem 轉換成 ML Task。

## 投影片內容

Security Problem：

`大量 Security Events → Analyst 看不完 → 需要優先找出可疑事件`

Machine Learning Problem：

`Security Observation → CLASSIFIER → Normal / Suspicious`

這種問題叫：

# Classification

今天是兩類，因此屬於 Binary Classification。

## 視覺
左側真實 SOC；中央一座 Problem Translation 橋；右側 `X → MODEL → y`，最後分成 NORMAL / SUSPICIOUS。

## 煥哥
> 真正重要的是把 Security Problem 翻成 Machine Learning Problem。

## 老師講稿
我們不是因為課本寫 Classification，所以硬找資料來分類。Security Analyst 面對很多 Events，我們希望系統協助判斷一筆 Observation 比較像 Normal 還是 Suspicious，因此這個 Security Problem 可以轉成 Classification Problem。Classification 的核心問題就是：新的 Observation 屬於哪一個類別？

## 老師補充 / 板書
`Real-world Problem → ML Task → Classification`

## 核心句
> Classification answers: Which class does this observation belong to?

## Transition
問題定義好了。CRISP-DM 接下來不是 Modeling，而是 Data Understanding。

---

# Slide 06 — Phase 2：Data Understanding

## 目的
從「我要分類什麼」進入「我到底擁有什麼資料」。

## 投影片內容

`① Business Understanding ✓`

### ② DATA UNDERSTANDING ← NOW

我們要問：

- What data do we have?
- What does each field mean?
- How many observations?
- What values are possible?
- Is anything missing?
- Is the data trustworthy?

示意資料：

| failed_login | requests/min | new_device | label |
|---:|---:|---:|---|
| 0 | 8 | 0 | Normal |
| 1 | 12 | 0 | Normal |
| 8 | 160 | 1 | Suspicious |
| 12 | 220 | 1 | Suspicious |

## 視覺
左側 CRISP-DM Map，Phase 2 高亮；右側把一列展開為 Observation Card。

## 煥哥
> 有 Dataset，不代表你了解 Dataset。

## 老師講稿
很多 ML Tutorial 下載 CSV、看一下 `df.head()` 就立刻 Training。但真正做 ML，至少要知道每一欄代表什麼。`requests/min = 160` 是多還是少？`new_device = 1` 代表什麼？資料怎麼收集？Label 是誰判定？有沒有 Missing Values？甚至更重要的是這些 Label 值得相信嗎？如果 Training Data 本身有問題，後面模型再漂亮也沒有用。

## 問
如果一份 Dataset 有一百萬筆，是不是一定比一萬筆好？

## 預期答案
不一定。資料品質、代表性與 Label 正確性同樣重要。

## 核心句
> Before training on data, understand what the data actually means.

## Transition
下一步 S07 開始把 Dataset 拆開來看，正式建立 Observation → Feature → Label → X / y，然後進入 Phase 3 Data Preparation。

---

## 8. Current Progress

Completed and canonicalized in this file:

- L5 lesson position and mission
- L5 boundaries
- CRISP-DM as L5–L8 backbone
- Full Slide Purpose Map
- Slide 00
- Slides S01–S06

Next batch:

**S07–S12 — Observation / Sample → Feature X → Label y → Phase 3 Data Preparation → Clean/Select/Encode → Train/Test Split**

> Deprecated: the earlier pre-CRISP-DM Slide 00–S06 draft. Do not use it as canonical course content.