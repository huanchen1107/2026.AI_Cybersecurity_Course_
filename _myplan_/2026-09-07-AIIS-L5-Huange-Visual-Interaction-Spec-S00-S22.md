# AIIS_L5 — 煥哥 Visual Interaction Specification（Slide 00–S22）

> Date: 2026-09-07
> Status: Canonical visual supplement / mandatory for PPT generation
> Applies to: AIIS_L5 Slide 00 + S01–S22
> Purpose: Restore the L1-style rule that the spokesperson is a content-reactive visual teaching character, not merely a speech bubble.

## Global Rule — 每一頁的「煥哥」都必須有 Visual

L5 所有正式投影片都必須同時設計：

1. **Role / Costume** — 當頁角色造型
2. **Expression** — 與概念相符的表情
3. **Pose / Action** — 明確動作
4. **Prop** — 與內容互動的道具
5. **Content Interaction** — 人物必須指向、拿起、檢查、比較或操作當頁核心內容
6. **Speech Bubble** — 一句短而有記憶點的話
7. **Placement** — 建議位置與占比

禁止：每頁只放同一張站立人物、只換文字；禁止人物與內容沒有互動；禁止為了裝飾而加入無關動作。

角色一致性：同一位「煥哥」，臉部與基本服裝語言一致；可以隨教學任務切換 Security Engineer / Data Detective / ML Engineer / Analyst 等輕量角色配件，但不能像不同人物。

---

# Slide 00 — 從 Secure Software 走向 Learning System

- **Role / Costume**：Security Engineer → Data Scientist 轉場造型；一側保留盾牌 badge，一側新增 data/AI badge。
- **Expression**：期待、準備開新章節。
- **Action**：左手指向已完成的 BUILD/MANAGE/UNDERSTAND/SECURE，右手接住從 Weather Security Center 流出的 Security Data。
- **Prop**：Security Data cards + small ML model cube。
- **Interaction**：資料從既有系統流到煥哥，再進入 ML Model。
- **Speech**：`前面我們建立系統；今天開始教機器從資料學習。`
- **Placement**：中央偏右，約 22%。

# S01 — Security Analyst 看不完的資料

- **Role**：SOC Analyst。
- **Expression**：忙碌、驚訝但不慌張。
- **Action**：坐在多螢幕前，雙手試圖處理大量 Event Cards，其中少數被他圈起。
- **Prop**：三個 counter：100 / 10,000 / 1,000,000 events。
- **Interaction**：Event Cards 像資料洪流湧向工作桌。
- **Speech**：`真正的問題不是沒有資料，是資料多到看不完！`
- **Placement**：右側 25%。

# S02 — 不要從 Algorithm 開始

- **Role**：ML Project Coach。
- **Expression**：制止、提醒。
- **Action**：一手做 STOP 手勢，阻止學生衝向 Random Forest / XGBoost / Neural Network 工具箱；另一手指向大字 PROBLEM。
- **Prop**：Algorithm toolbox + Problem board。
- **Interaction**：用箭頭把錯誤路線拉回 `Problem First`。
- **Speech**：`先別挑模型。你到底要解決什麼問題？`
- **Placement**：中央偏右 20%。

# S03 — CRISP-DM：Machine Learning Project Map

- **Role**：ML Expedition Guide。
- **Expression**：有方向感、帶隊。
- **Action**：拿地圖／指南針站在 CRISP-DM 六環旁，手指 Phase 1。
- **Prop**：CRISP-DM map + compass。
- **Interaction**：人物實際沿六階段路線指引，不是站在旁邊。
- **Speech**：`不要迷路。之後做 ML，我們都回來看這張地圖。`
- **Placement**：右下 18%。

# S04 — Phase 1：Business Understanding

- **Role**：Security Product Owner / Problem Framer。
- **Expression**：思考、追問。
- **Action**：拿白板筆在問題板寫四個問句：Problem? Why? Who? Success?
- **Prop**：Problem Canvas。
- **Interaction**：把模糊的 `AI Cybersecurity System` 用紅筆劃掉，改寫成 Analyst 無法檢查大量 Events。
- **Speech**：`先不要寫 Python。先把真正的問題說清楚。`
- **Placement**：右側 22%。

# S05 — Security Problem → ML Problem

- **Role**：Problem Translator。
- **Expression**：恍然大悟／成功轉譯。
- **Action**：站在橋中央，左手拿 `Security Problem` 卡，右手放下 `Binary Classification` 卡。
- **Prop**：Translation bridge。
- **Interaction**：把 `大量事件看不完` 實際轉成 `Observation → Classifier → Normal/Suspicious`。
- **Speech**：`不是先找演算法，是先把 Security Problem 翻成 ML Task。`
- **Placement**：橋中央或右下 20%。

# S06 — Phase 2：Data Understanding

- **Role**：**Data Detective**。
- **Expression**：皺眉、瞇眼、懷疑資料品質。
- **Action**：左手拿 Dataset，右手拿大型放大鏡，正在檢查 `requests/min = 160`。
- **Prop**：Magnifying glass；`Missing? / Correct? / Trustworthy?` 三張卡。
- **Interaction**：放大鏡必須對準 Dataset 中實際數值；頭旁浮出 `160 很高嗎？`、`1 是什麼意思？`、`誰標的 Label？`。
- **Speech**：`等等！先別急著 Training。這些資料到底代表什麼？`
- **Secondary line**：`有 Dataset，不代表你了解 Dataset。`
- **Placement**：右側 25–30%。

# S07 — Observation / Sample

- **Role**：Data Inspector。
- **Expression**：專注、正在拆解概念。
- **Action**：從整張 Dataset 抽出其中一列，像抽卡一樣拿在手上。
- **Prop**：One-row Observation Card。
- **Interaction**：背景完整 Dataset 淡化；手中單列高亮，箭頭標 `ONE ROW = ONE OBSERVATION / SAMPLE`。
- **Speech**：`先不要看整張表。這一列，就是一個案例。`
- **Placement**：右側 22%。

# S08 — Feature X

- **Role**：Evidence Collector。
- **Expression**：像偵探收集線索。
- **Action**：把 `failed_login`、`requests/min`、`new_device` 三張 clue cards 放入標示 `X` 的資料夾。
- **Prop**：Clue cards + X folder。
- **Interaction**：刻意把 `label` 卡擋在 X folder 外面。
- **Speech**：`Feature 就是模型被允許看到的線索。`
- **Placement**：右下 23%。

# S09 — Label y

- **Role**：Training Teacher。
- **Expression**：清楚、確認答案。
- **Action**：一手拿 Features X，一手翻開背面的 Answer Card `Suspicious`，放入 y 區。
- **Prop**：Answer card / target tag。
- **Interaction**：畫出 `X → ?` 與 training 時的 `X + known y`。
- **Speech**：`y 是訓練案例的已知答案；答案標錯，模型也會學錯。`
- **Placement**：右側 22%。

# S10 — Phase 3：Data Preparation

- **Role**：Data Chef / Data Engineer（避免過度卡通，可用工程整理台）。
- **Expression**：有條理、準備加工。
- **Action**：把 RAW DATA 卡送入 Preparation pipeline，另一端輸出 clean X/y。
- **Prop**：Select / Clean / Encode 三段處理台。
- **Interaction**：人物操作 pipeline，而不是旁觀。
- **Speech**：`Raw Security Data 不會自動變成 Training Data。`
- **Placement**：右側 20%。

# S11 — Clean / Select / Encode

- **Role**：Data Quality Engineer。
- **Expression**：仔細挑選。
- **Action**：用三個工具處理資料：垃圾桶移除不需要欄位、修補 Missing、converter 將 Yes/No → 1/0。
- **Prop**：trash / repair / encode icons。
- **Interaction**：把 `event_id` 移出 predictive features；把 `label` 明確留在 y，不允許偷進 X。
- **Speech**：`模型要看到有用訊號，不要讓答案偷偷混進 Feature。`
- **Placement**：右側 25%。

# S12 — Train / Test Split

- **Role**：Exam Proctor / ML Coach。
- **Expression**：嚴格、公平。
- **Action**：把一疊 Dataset cards 分成 80% TRAIN 和 20% TEST，並用封條把 TEST 暫時封住。
- **Prop**：80/20 boxes + `DO NOT OPEN DURING TRAINING` seal。
- **Interaction**：手明確阻止 Test cards 進入 Training。
- **Speech**：`考前不能偷看考題；Training 也不能偷看 Test Set。`
- **Placement**：中央偏右 22%。

# S13 — Phase 4：Modeling

- **Role**：ML Engineer。
- **Expression**：終於可以動手、但保持克制。
- **Action**：打開只有一個工具的 model toolbox：Logistic Regression。
- **Prop**：single-model toolbox。
- **Interaction**：前面三個 CRISP-DM phases 已打勾，人物現在才打開 Modeling 工具箱。
- **Speech**：`終於輪到 Model；但今天只需要一個代表性模型。`
- **Placement**：右側 22%。

# S14 — Rule-based vs Learning

- **Role**：雙角色對照，同一位煥哥左右分身。
- **Expression**：左側「我來訂規則」；右側「讓資料教模型」。
- **Action**：左側手寫 `if failed_login > 5...`；右側把 labeled examples 餵給 learning algorithm。
- **Prop**：Rule Book vs Training Cards。
- **Interaction**：中間放 `WHO DEFINES THE DECISION?`。
- **Speech**：左 `規則我寫。`／右 `案例給模型學。`
- **Placement**：左右各 15–18%。

# S15 — 第一個 Classifier：Logistic Regression

- **Role**：ML Builder。
- **Expression**：簡潔、專注。
- **Action**：把 `LogisticRegression()` 模型盒放上工作台，但模型盒仍顯示 `UNTRAINED`。
- **Prop**：Untrained model cube。
- **Interaction**：指向兩行 code，同時另一手指 `UNTRAINED`，防止學生誤以為建立物件等於訓練。
- **Speech**：`建立模型很短，但它現在還什麼都沒學。`
- **Placement**：右下 22%。

# S16 — `model.fit()`

- **Role**：ML Trainer。
- **Expression**：正在訓練、觀察進度。
- **Action**：把 X_train cards 與 y_train answer cards 成對送入 model。
- **Prop**：Training conveyor + TRAINED stamp。
- **Interaction**：TEST box 仍在背景封住，不能進 conveyor。
- **Speech**：`` `.fit()` 很短，但這一刻才是真正的 Training。 ``
- **Placement**：右側 22%。

# S17 — `model.predict()`

- **Role**：Inference Operator。
- **Expression**：等待模型回答。
- **Action**：拿一張沒有 Label 的 New Observation 放進 trained model；另一端接出 Prediction card。
- **Prop**：New Event Card + Prediction output。
- **Interaction**：刻意把 Ground Truth 卡蓋住，強調 prediction 時不能偷看答案。
- **Speech**：`訓練時有答案；預測時先不能偷看答案。`
- **Placement**：右側 22%。

# S18 — First Security Prediction

- **Role**：Security Analyst with AI Assistant。
- **Expression**：警覺但不武斷。
- **Action**：模型遞出 `SUSPICIOUS` 黃色卡，煥哥沒有按 BLOCK，而是拿檢查板進行 Review。
- **Prop**：Review clipboard；禁止使用法槌／罪犯圖示。
- **Interaction**：`SUSPICIOUS → Analyst Review`，不能畫成 `SUSPICIOUS → ATTACK CONFIRMED`。
- **Speech**：`AI 提醒我「值得看」，不是替我宣布「有罪」。`
- **Placement**：右側 25%。

# S19 — Phase 5：Evaluation

- **Role**：Model Reviewer / QA Engineer。
- **Expression**：質疑、驗證。
- **Action**：一手拿 `RUNNING ✓`，另一手拿大問號放在 `RELIABLE ?`。
- **Prop**：Checklist / magnifier / test report。
- **Interaction**：把「程式會跑」與「模型可信」兩張卡分開。
- **Speech**：`跑得動，不代表判得好。`
- **Placement**：右側 22%。

# S20 — Prediction ≠ Truth

- **Role**：Evidence Verifier。
- **Expression**：發現不一致。
- **Action**：左右手各拿 Prediction 與 Ground Truth 卡，發現一張 Suspicious、一張 Normal。
- **Prop**：MATCH / MISMATCH marker。
- **Interaction**：人物把兩張卡並排比較，而不是只看 Prediction。
- **Speech**：`AI 有答案，不代表 AI 就是答案。`
- **Placement**：中央偏右 23%。

# S21 — Phase 6：Deployment

- **Role**：ML / Security Integration Engineer。
- **Expression**：組裝系統、考慮全流程。
- **Action**：把 Feature Preparation、Model、Prediction、Analyst Review 四個模組接成 pipeline。
- **Prop**：pipeline connectors + log/evidence icon。
- **Interaction**：人物正在接線；Training 與 Inference preprocessing 使用相同 connector style。
- **Speech**：`Deployment 是進入工作流程，不只是把 .py 放上 Server。`
- **Placement**：右下 22%。

# S22 — 回到 Weather Security Center

- **Role**：Security AI System Architect。
- **Expression**：完成一個里程碑、指向完整系統。
- **Action**：站在 Weather Security Center architecture 前，用雷射筆指出新加入的 ML-assisted Triage module；另一手指向 Human Analyst。
- **Prop**：architecture board + six-phase CRISP-DM badge。
- **Interaction**：明確畫出 `Event → Features → ML → Prediction → Analyst Review`，人物位於系統與人的交界處。
- **Speech**：`不是另外做一個玩具 Notebook；我們替原本的 Security System 增加學習能力。`
- **Placement**：右側 20–22%。

---

# PPT Generation Mandatory Check

生成任何 L5 PPT 前，逐頁檢查：

- [ ] 煥哥是否有當頁專屬角色／配件？
- [ ] 表情是否反映當頁概念？
- [ ] 是否有明確手勢／動作？
- [ ] 是否直接與 Dataset / CRISP-DM / Model / Security Event 等核心物件互動？
- [ ] 對話是否短而有記憶點？
- [ ] 人物是否服務教學，而非裝飾？
- [ ] 是否避免連續頁重複同一 pose？
- [ ] 是否維持同一位煥哥的臉部與角色一致性？

如果任一正式內容頁只有「煥哥：一句話」而沒有 Role + Expression + Action + Prop + Interaction，該頁視為 **visual design incomplete**。
