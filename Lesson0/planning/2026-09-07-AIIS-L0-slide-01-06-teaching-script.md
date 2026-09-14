# AIIS_L0 — Slides 01–06 Detailed Teaching Script

Date: 2026-09-07
Parent plan: `2026-09-07-AIIS-L0-32-slide-detailed-lecture-plan.md`
Status: Detailed lecture script

## Teaching rhythm

Slides 01–06 form one continuous story:

```text
AIIS
 ↓
我們正在什麼時代？
 ↓
Machine Power
 ↓
Energy Power
 ↓
Information Power
 ↓
Intelligence Power
 ↓
AI 到底發展到哪裡？
 ↓
ANI → AGI → ASI
```

Do not introduce Kali, ML details, security tools, or product tutorials yet. First establish why AI is a technological revolution.

---

# Slide 01 — AIIS: AI and Information Security

## On-slide

**AIIS — AI and Information Security**

**人工智慧與資訊安全**

> AI is the capability. Information Security is the discipline.

Conceptual visual:

```text
                    HUMAN
                      │
                      ↓
                AI CAPABILITY
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
        CODE         DATA        TOOLS
          │           │           │
          └───────────┼───────────┘
                      ↓
              DIGITAL SYSTEM
                      │
              ┌───────┴───────┐
              ↓               ↓
         CAN DO MORE      MORE TO PROTECT
                              ↓
                     INFORMATION SECURITY
```

## Presenter
煥哥：welcoming/open-hand gesture，視線朝 AIIS 架構。

## Teacher opening

不要從「今天要介紹 AI 與資安」開始，而從 consequence 開始：

> 如果 AI 只能回答問題，我們可能只需要擔心它答錯。但是如果 AI 可以讀檔案、寫程式、操作工具、連資料庫，甚至把網站部署出去，那問題就完全不一樣了。

問：

> **AI 越厲害，是不是代表我們越安全？**

收斂：

> **AI capability ↑ → Security responsibility ↑**

說明 AIIS 不是前半 AI、後半資安，而是從第一天起把 capability 與 security 放進同一個系統學習。

## Transition

> 在講 AI 之前，先把時間拉遠一點。AI 為什麼會被稱為一次革命？人類以前到底經歷過哪些類似的大轉變？

---

# Slide 02 — What Era Are We Living In?

## On-slide

**我們正在經歷什麼樣的科技轉變？**

*What Era Are We Living In?*

```text
Machine → Energy → Computer / Network → AI Intelligence
```

底部：

> **Technology amplifies human capability.**

## Visual
提問頁，避免先把答案全部揭露。四個時代以 machine / electricity / computer-network / AI-agent silhouette 表示；AI 稍突出但不先寫完整革命名稱。

## Presenter
煥哥：thinking pose，手托下巴，視線朝四個時代圖示。

## Teacher talk

> 我們先不要急著定義 AI。把人類歷史拉遠來看，每隔一段很長的時間，就會出現一種科技，把人原本做不到、做不快、做不多的事情突然放大。

舉例：人的肌肉有限、可直接使用的能源有限、人的資訊處理能力有限。

問：

> **AI 正在放大人的哪一種能力？**

不要立即回答。

再問：

> 蒸汽機、電力、電腦、AI 有什麼共同點？

學生可能回答效率、自動化、幫人做事、做以前做不到的事。

老師收斂：

> **它們都在 Amplify Human Capability。**

## Transition

> 我們從第一個最容易理解的開始：機器到底改變了什麼？

---

# Slide 03 — Industrial Revolution: Machine Power

## Core
Machines amplify physical capability.

## On-slide

**Industrial Revolution — 工業革命**

```text
BEFORE                         AFTER
Human                          Steam Power
  ↓                                ↓
Hand Tools                      Machine
  ↓                                ↓
Human Muscle                    Factory
```

> **Machine Power**

`Human Muscle → Machine Power`

## Visual
Before / After：左側人力與手工具，右側蒸汽動力、機械與工廠。不要用大量年份填滿畫面。

## Presenter
煥哥：presenting pose，指向 Machine Power。

## Teacher talk

> 以前生產能力很直接受到人的身體限制。你有十個工人，就是十個人的力量。機械化與蒸汽動力出現後，力量開始可以由 Machine 放大。

本課不要求背年份，要求記住：

> **Machine Power**

## Ask

> 挖土機和一百個拿鏟子的人，最大的差別是什麼？

收斂到 Physical Capability at Scale。

## Security foreshadow
只留一句，不展開：

> 能力被放大的同時，事故造成的影響是不是也可能被放大？

## Transition

> 但是機器要靠什麼才能一直運轉？

---

# Slide 04 — Energy Revolution: Energy Power

## Core
Scalable generation, distribution and use of energy.

## On-slide

**Energy Revolution — 能源革命**

```text
Electricity / Petroleum
          ↓
Generator / Energy Systems
          ↓
Power Grid / Distribution
          ↓
Factory / City / Transportation
```

> **Energy Power**

Progress indicator:

`Machine → Energy ← YOU ARE HERE → Information → Intelligence`

## Visual
不要只畫燈泡。以 Power Plant → Grid → Home / Factory / City 表示 infrastructure。

## Presenter
煥哥：簡報筆指向 Power Grid。

## Teacher talk

> 有機器之後，下一個問題是：機器的能量從哪裡來？當 Electricity、Petroleum、Generator、Power Grid 等技術成熟後，能源開始能夠大規模 Generate、Transport、Distribute、Use。

明確說明：

> 這裡使用的是「四次重要技術革命」的教學框架，不把後面全部稱為第幾次工業革命。

## Ask

> 如果台灣停電一天，哪些系統會停止或受重大影響？

學生可能提到電腦、網路、交通、工廠、基地台、醫院。

收斂：

> Energy 已經變成 Infrastructure。

## Security foreshadow

> Infrastructure 越重要，Availability 是不是越重要？

CIA 暫時不解釋。

## Transition

> 有了 Machine、有了 Energy，接下來人類遇到另一個瓶頸：不是搬不動，而是資訊太多，腦袋處理不完。

---

# Slide 05 — Information Revolution: Information Power

## Core
Computers, software and networks amplify information processing.

## On-slide

**Information Revolution — 資訊革命**

```text
DATA
 ↓
COMPUTER
 ↓
SOFTWARE
 ↓
NETWORK
 ↓
INTERNET
 ↓
INFORMATION AT SCALE
```

> **Information Power**

Three verbs: **Store / Process / Communicate**

## Visual
Computer 作為中心，連向 Database / Software / Internet。避免只放一張電腦照片。

## Presenter
煥哥：tablet/laptop，analytical expression。

## Teacher talk

> 電腦真正厲害的地方，不只是算數很快。它讓我們能大規模 Store、Process、Copy、Search、Transmit Information。

比較：

> Machine Revolution 放大 Physical Power；Information Revolution 放大 Information Processing。

## Key question

> **電腦已經這麼厲害了，為什麼我們還需要 AI？**

接受學生回答後收斂：

> 傳統 Computer 非常會處理我們告訴它怎麼處理的資訊。現在我們希望 Machine 能從 Information 中做 Judgment、Prediction、Generation，甚至 Planning。

## Transition
第四個 icon 才亮起：AI Revolution。

> 所以我們才來到今天。

---

# Slide 06 — AI Revolution: Intelligence Power

## Core
AI increasingly performs or assists tasks associated with cognitive capabilities.

## On-slide

```text
Industrial          Energy          Information          AI
Revolution          Revolution      Revolution           Revolution
    ↓                   ↓               ↓                   ↓
MACHINE             ENERGY          INFORMATION          INTELLIGENCE
 POWER               POWER             POWER               POWER
```

> **Machine → Energy → Information → Intelligence**

## Visual
完整四階段 horizontal timeline；Intelligence Power 為主要 highlight。

## Presenter
煥哥：emphasizing pose，食指指向 Intelligence Power。

## Teacher talk

逐一回顧：
- Machine Power → physical capability
- Energy Power → scalable energy infrastructure
- Information Power → information processing
- Intelligence Power → tasks associated with cognition

傳統模式：

```text
Human writes rules
       ↓
Computer executes rules
```

AI-assisted pattern：

```text
Human gives goal / data
       ↓
AI
       ↓
Predict / Generate / Recommend / Plan
```

## Accuracy guard
不要說「AI 就是智慧」或進入 consciousness 哲學爭論。

較精確說法：

> **AI systems can perform or assist with tasks associated with human cognitive capabilities.**

工程上可觀察的能力包括：Classification / Prediction / Recognition / Generation / Recommendation / Planning / Tool Use。

## Ask

> 如果 AI 放大的是認知能力，那它跟蒸汽機最大的差別在哪裡？

引導：蒸汽機主要替人做 physical work；AI 開始替人完成部分 judgment、generation、planning、decision-support work。

## Transition

畫面最後出現：

> **But… what exactly is AI capable of today?**

```text
AI REVOLUTION
      ↓
ANI → AGI → ASI
```

老師：

> 如果我們說 AI 正在形成 Intelligence Power，下一個問題就是：今天的 AI 到底已經走到哪裡？

→ Slide 07.
