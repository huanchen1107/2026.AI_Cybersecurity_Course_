# PPT Style & NotebookLM Long-Form Workflow v1.0

**Project:** 2026 AI × Cybersecurity Course  
**Repository:** `huanchen1107/2026.AI_Cybersecurity_Course_`  
**Purpose:** 建立 Lesson 1–16 共用的長篇簡報產出標準，使 NotebookLM 能以分批方式產出 60–100+ 頁、內容不重複且視覺風格盡量一致的簡報。  
**Version:** v1.0  
**Date:** 2026-09-06

---

## 1. 核心原則

NotebookLM 單次簡報產出適合控制在約 15 頁內。若每批重新讀取大量原始教材並重新理解內容，容易發生：

- 前後批次內容重複
- 重新生成封面或 Agenda
- 頁面順序漂移
- 視覺風格改變（Style Drift）
- 同一概念被不同批次重新解釋
- 色彩、插圖、資訊圖表與文字密度不一致

因此本專案採用：

> **Raw Sources → Complete Slide Outline → Style Setup → Clean NotebookLM Source → Batch Rendering → Merge → Image/Text Repair**

NotebookLM 的角色主要是「依照已規劃好的 Slide Outline 進行視覺化」，而不是每一批重新規劃整份課程。

---

# 2. Stage A — 先建立完整簡報大綱

不要直接把所有教材交給 NotebookLM 然後立刻要求產生 60 頁簡報。

先利用 ChatGPT / Claude / NotebookLM 等工具，根據完整教材建立整份簡報的 **Slide Outline / Slide Blueprint**。

例如 Lesson 1 預計 60 頁，應先完成 Slide 001–060 的規劃，再開始產圖。

每一頁建議至少包含：

```text
SLIDE 012
Slide ID: L01-S012
Title:
Teaching Goal:
Core Message:
Content:
Visual Intent:
Diagram / Illustration:
Key Labels:
Speaker Notes:
Transition to Next Slide:
```

其中 `Visual Intent` 非常重要，可使用：

- Full-screen Illustration
- Concept Diagram
- Architecture Diagram
- Process Flow
- Comparison
- Timeline
- Cybersecurity Dashboard
- Attack / Defense Flow
- Code / Terminal
- Demo
- YAML Prompt
- Lab Instruction
- Summary

這樣 NotebookLM 不只知道「這頁講什麼」，也知道「這頁應該如何視覺化」。

---

# 3. Slide ID 規則

每張投影片應有唯一 ID。

格式：

```text
L{Lesson}-S{Slide}
```

例如：

```text
L01-S001
L01-S002
...
L01-S060
```

用途：

1. 防止跨批次重複。
2. 保持 Slide 順序。
3. 方便 GitHub、NotebookLM、PPTX 與講稿互相追蹤。
4. 未來修改單頁時可以精確指定。

---

# 4. Stage B — Style Setup 必須放在 Outline 最前方

NotebookLM 最終使用的乾淨來源文件，最前方應先放置完整的 **PPT STYLE SETUP**。

至少定義：

## 4.1 Design Direction

本課程預設方向：

> **AI Security Operations Center × Teaching Infographic × Modern Technology Presentation**

整體要求：

- 16:9
- 現代科技感
- 專業但適合教學
- 高視覺化
- 避免大量連續文字
- 一頁一個核心訊息
- Architecture / Process / Concept 優先圖像化

## 4.2 Color System

建議固定色碼，例如：

```text
Background:   #08111F
Primary AI:   #16C7FF
Secondary:    #4F7CFF
Threat:       #FF5A5F
Defense:      #37D67A
Warning:      #FFB020
Text Primary: #F5F7FA
Text Muted:   #AAB6C5
```

不要讓不同批次自行重新決定色彩。

## 4.3 Semantic Color

- AI / Agent → Cyan
- Cybersecurity / SOC → Blue
- Attack / Threat / Risk → Red / Orange
- Defense / Secure → Green
- Warning → Amber
- Neutral Concept → White / Gray

## 4.4 Typography

- 大標題簡潔
- 避免過長段落
- 關鍵詞可加粗或高亮
- Code / YAML / Terminal 使用 monospace 視覺語言
- 中文必須清晰可辨識

## 4.5 Visual Language

優先：

- architecture diagram
- flow diagram
- comparison
- timeline
- dashboard
- network topology
- AI agent nodes
- SOC / cybersecurity interface
- clean infographic

避免：

- 無意義裝飾
- 每頁大量文字
- 不必要的 3D 字
- 過度卡通化
- 不一致 icon style
- 每批重新改變背景風格

---

# 5. Stage C — 建立「乾淨來源」

這是整個流程最重要的技巧之一。

完成完整 Outline 後，把：

1. PPT Style Setup
2. Slide 001–N Blueprint

整理成一份新的乾淨文件，再將它加入 NotebookLM Sources。

正式產生簡報時，建議 **只選這一份乾淨的 Slide Outline Source**。

不要同時選取大量原始 PDF、網頁、筆記與其他教材，否則 NotebookLM 可能再次重新解讀教材，造成：

- 內容重新排序
- 額外補充
- 前後批重複
- Style Drift

原始資料主要用於「產生 Outline」；乾淨 Outline 才是「產生 PPT」的 canonical source。

---

# 6. Stage D — 分批產出

## Batch 1：Slide 001–015

```text
請依照目前選取來源中的「簡報大綱」製作簡報。

嚴格遵守來源文件最前方所定義的：
- 整體視覺風格
- 背景與主色系
- 精確色碼
- 字體與文字風格
- 插圖與資訊圖表風格
- 頁面構圖規則
- 禁止出現的視覺元素

【本批生成範圍】
只生成簡報大綱中的第 1–15 頁。

請按照大綱原有頁碼、順序與每頁內容製作。
不要自行增加、刪除、合併或重新排序頁面。

本批只生成第 1–15 頁。
```

---

## Batch 2：Slide 016–030

從第二批開始，必須加入明確防呆限制。

```text
繼續製作同一份簡報。

嚴格沿用來源文件最前方定義的完整風格規範，
保持與第一批完全一致的視覺語言、背景、色碼、
字體、插圖風格、資訊圖表風格與構圖方式。

【本批生成範圍】
只生成簡報大綱中的第 16–30 頁。

【重要防呆限制】
第 1–15 頁已經完成。

不要重新生成第 1–15 頁。
不要摘要第 1–15 頁。
不要重新製作封面。
不要重新製作課程介紹或 Agenda。
不要將前 15 頁內容混入本批。
不要自行補充前面的內容。

直接從大綱第 16 頁開始。

嚴格按照來源大綱中的第 16–30 頁內容與順序製作。
不要增加、刪除、合併或重新排序頁面。

本批只生成第 16–30 頁。
```

---

# 7. Batch 3 以後通用模板

```text
繼續製作同一份簡報。

嚴格遵守來源文件最前方的完整風格規範，
保持所有批次的視覺與排版一致。

【已完成範圍】
第 {{DONE_START}}–{{DONE_END}} 頁已完成。

【本次唯一生成範圍】
第 {{START}}–{{END}} 頁。

【禁止】
不得重新生成、摘要、改寫或混入任何已完成頁面。
不得重新製作封面、Agenda 或 Introduction。
不得自行增加、刪除、合併或重新排序頁面。
不得改變既定色碼、背景、字體、插圖、
資訊圖表或構圖風格。

直接從第 {{START}} 頁開始。
只生成第 {{START}}–{{END}} 頁。
```

例如：

### 60 pages

```text
Batch 1: 01–15
Batch 2: 16–30
Batch 3: 31–45
Batch 4: 46–60
```

### 100 pages

```text
Batch 1: 01–15
Batch 2: 16–30
Batch 3: 31–45
Batch 4: 46–60
Batch 5: 61–75
Batch 6: 76–90
Batch 7: 91–100
```

---

# 8. Continuity Anchor

為了改善 Batch 切換點，例如 Slide 015 → 016，可在 Outline 中加入前後關係。

例如：

```text
L01-S015
Transition to Next Slide:
Next = L01-S016 / AI Revolution Phase 2
```

下一頁：

```text
L01-S016
Previous = L01-S015
```

如此可以降低新 Batch 看起來像另一份簡報的問題。

---

# 9. Stage E — 下載與合併 PPTX

每一批完成後：

1. 下載 PPTX。
2. 保存原始 Batch 檔案。
3. 依照 Slide ID / 頁碼合併。
4. 檢查 Batch 邊界：15→16、30→31、45→46。
5. 檢查是否出現重複頁。
6. 檢查 Style Drift。
7. 檢查中文文字與圖中文字。

建議檔名：

```text
L01_batch01_S001-S015.pptx
L01_batch02_S016-S030.pptx
L01_batch03_S031-S045.pptx
L01_batch04_S046-S060.pptx
```

最後：

```text
L01_AI_Cybersecurity_FINAL.pptx
```

---

# 10. 中文圖片文字亂碼修復

NotebookLM 產生的圖像型投影片可能出現：

- 中文亂碼
- 字形錯誤
- 中文缺字
- 標籤文字不清楚
- 圖中文字排列異常

建議流程：

1. NotebookLM 下載 PPTX。
2. 找到有問題的圖片。
3. 複製或匯出圖片。
4. 在 Gemini 建立專門的 Gem，例如「還我漂亮圖助手」。
5. 將圖片交給 Gem 重新生成／修復。
6. 使用建立圖像功能與適合圖像理解的模型。
7. 下載修復圖。
8. 覆蓋 PPT 原圖片。

## Gemini 修圖 Prompt 基本要求

```text
請重新製作這張圖片。

保持：
- 原本構圖
- 原本資訊階層
- 原本色彩
- 原本 icon / illustration style
- 原本物件位置

修正：
- 所有中文字
- 中文亂碼
- 錯字
- 缺字
- 文字對齊
- 文字清晰度

不要重新設計整張圖。
不要改變原圖所表達的資訊。
繁體中文必須完全清楚、正確、可讀。
```

處理下一張圖片時，建議建立新的聊天視窗，降低上一張圖片上下文干擾。

多張圖片可以用多個視窗平行處理。

---

# 11. 自訂背景圖片

若希望 NotebookLM 使用特定視覺背景：

1. 將背景圖片加入 Source。
2. 同時加入乾淨 Slide Outline。
3. 在 Prompt 指定：

```text
使用來源中的指定圖片作為簡報背景與主要視覺風格參考，
並嚴格按照來源文件中的文字、頁面結構與 Style Setup 生成簡報。
```

適合：

- 手繪風
- Cybersecurity SOC
- Blueprint
- AI neural network
- Dark technology
- Corporate identity

但背景圖只是視覺 reference，內容仍應以 canonical Slide Outline 為準。

---

# 12. Claude / ChatGPT + NotebookLM Workflow

可使用 Claude 或 ChatGPT 進行「內容與腳本設計」，NotebookLM 進行「視覺生成」。

推薦：

```text
Course Material
      ↓
ChatGPT / Claude
      ↓
Complete Slide Blueprint
      ↓
PPT Style Setup
      ↓
Clean Canonical Outline Source
      ↓
NotebookLM
      ↓
Batch 01 / 02 / 03 / ...
      ↓
PPTX Merge
      ↓
Gemini Image Repair
      ↓
Final PPTX
```

ChatGPT / Claude 負責：

- 教學邏輯
- 課程結構
- Slide sequencing
- 每頁教學目標
- 每頁文字
- 圖解意圖
- Speaker Notes

NotebookLM 負責：

- 視覺化
- Layout
- Illustration
- Infographic
- Slide rendering

Gemini Image Tool 負責：

- 中文圖片修復
- 圖片重製
- Style-preserving image correction

---

# 13. 極簡無文字簡報模式

某些演講型頁面可採用 Visual-first 模式：

```text
這批簡報採用極簡演講模式。

除了：
- 關鍵數字
- 必要圖表標籤
- 極少量關鍵詞

不要產生其他文字。

使用大型視覺、概念圖、象徵性場景與資訊圖表表達內容。
詳細說明由講者口頭呈現。
```

此模式不應套用到需要學生閱讀操作步驟、Code、Lab、YAML Prompt 的頁面。

---

# 14. AI × Cybersecurity Course 建議固定 Slide Types

Lesson 1–16 優先共用以下視覺語言：

1. Lesson Cover
2. Hook / Big Question
3. Learning Objectives
4. Concept
5. Comparison
6. Architecture
7. Process / Workflow
8. AI Agent
9. Security Threat
10. Attack Flow
11. Defense Flow
12. SOC Dashboard
13. Code / Terminal
14. Antigravity / Vibe Coding Prompt
15. YAML Prompt
16. Demo
17. Lab
18. Reflection / Discussion
19. Key Takeaways
20. Lesson Summary

---

# 15. Quality Gate

每一批產出後至少檢查：

## Content

- [ ] 頁碼正確
- [ ] Slide ID 對應 Outline
- [ ] 沒有重複前一批內容
- [ ] 沒有漏頁
- [ ] 沒有自行增加不在 Outline 的概念
- [ ] 教學順序正確

## Style

- [ ] 背景一致
- [ ] 色碼語意一致
- [ ] 字體風格一致
- [ ] Icon style 一致
- [ ] Illustration style 一致
- [ ] Diagram style 一致
- [ ] Batch boundary 無明顯 Style Drift

## Chinese

- [ ] 繁體中文正確
- [ ] 無亂碼
- [ ] 圖中文字可讀
- [ ] 專有名詞正確

## Teaching

- [ ] 一頁一個核心概念
- [ ] 圖像確實協助理解
- [ ] Demo / Lab 可操作
- [ ] Speaker Notes 與 Slide 對應

---

# 16. 本專案的 Canonical PPT Workflow

之後設計 Lesson 1–16 時，原則上應同時考慮：

```text
Lesson Content
    ↓
Part Design
    ↓
Slide Blueprint
    ↓
PPT Style Setup
    ↓
NotebookLM-ready Clean Source
    ↓
15-slide Batch Generation
    ↓
Quality Gate
    ↓
Merge
    ↓
Gemini Repair if needed
    ↓
Final Lecture PPT
```

因此 `_myplan_` 中的 Lesson 規劃不應只寫「這一課要講什麼」，最好逐步發展成可直接交給 NotebookLM 的 Slide Blueprint。

---

## Version History

### v1.0 — 2026-09-06

- 建立 NotebookLM 長篇簡報分批產出流程。
- 定義 Clean Outline Source 原則。
- 定義 Slide ID。
- 建立 Batch 1 / Batch 2 / Generic Batch Prompt。
- 加入 Style Setup、Continuity Anchor 與 Quality Gate。
- 加入 Gemini 中文圖片修復流程。
- 加入自訂背景與極簡無文字模式。
- 定義 AI × Cybersecurity Course Lesson 1–16 共用 PPT workflow。
