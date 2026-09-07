# AIIS_L4 — Slide 07–14 Teaching Script

**Lesson:** AIIS_L4 — How to Build an AI Cybersecurity Project / Secure Development  
**Batch:** 2 — S07–S14  
**Story:** Trust → Secrets → Access → Dependencies → Review → SAST → Semgrep  
**Primary tool:** Semgrep  

---

# S07 — Input Is a Trust Boundary

## On-slide text

# INPUT = TRUST BOUNDARY
## 外面進來的資料，不應直接被相信

```text
USER / API / FILE / SENSOR
          ↓
    [ TRUST BOUNDARY ]
          ↓
     VALIDATE FIRST
          ↓
      APPLICATION
```

Ask four questions:

- Is the **type** correct?
- Is the **format** correct?
- Is the **range** reasonable?
- Is this input **allowed here**?

> **Validate before use.**

## Visual composition

Weather Security Center is a protected building. Four streams—User, API, File, Sensor—approach one checkpoint labeled TRUST BOUNDARY. Only validated data passes through.

Use normal engineering/security checkpoint imagery, not attacker imagery.

## Character expression / pose

Spokesperson stands at the checkpoint holding a validation checklist, calmly inspecting incoming data packets.

## Teacher script

我們先從最重要的 secure coding 觀念之一開始：Trust Boundary。

Weather Security Center 的資料可能從使用者、外部 API、檔案、sensor 進來。這些資料一跨進我們的程式，就不能因為「看起來正常」而直接相信。

例如 city 應該是字串，但只有 type 是字串就夠了嗎？長度呢？允許的格式呢？某個 endpoint 是否允許這個值呢？

FastAPI/Pydantic 已經可以幫我們做很多 validation，但重點不是背 framework，而是記住：**外部資料跨進系統時，就是一條 trust boundary。**

## Mini classroom check

問學生：`city="Hualien"` 與一個長達數萬字元的 city 字串，兩個都是 string，是否都應接受？

## Transition

「除了輸入之外，還有另一種資料剛好相反：它不是外面送進來，而是我們絕對不希望送出去。」

---

# S08 — Secrets Do Not Belong in Source Code

## On-slide text

# SECRETS ≠ SOURCE CODE

### Bad idea

```python
API_KEY = "my-real-secret-key"
DB_PASSWORD = "password123"
```

### Better pattern

```text
Source Code
    ↓ reads
Environment / Secret Store
    ↓
Runtime Configuration
```

Secrets may include:
- API keys
- passwords
- tokens
- private credentials

> **Git remembers. A deleted secret may still exist in history.**

## Visual composition

Split visual: left shows a code file with a key visibly embedded and then flowing into a Git history timeline; right shows source code referencing a locked environment/configuration vault.

## Character expression / pose

Spokesperson stops a key icon from being dragged into a source-code file, pointing instead toward a locked configuration box.

## Teacher script

Vibe Coding 時很常發生一件事情：為了讓程式快點跑，我們直接把 API key 貼進 code。程式馬上成功，所以很有成就感。

但一 commit 到 Git，問題就來了。即使你後來把那一行刪掉，也不能假設 secret 從歷史中消失。

所以 secure development 要把「程式邏輯」和「敏感設定」分開。今天不用深入所有 secret-management 平台，只要建立這個基本習慣。

AI coding assistant 也必須收到同樣規則：**不要要求 AI 把真實 secret 寫進 source code。**

## Transition

「資料能不能進來是一件事；進來的人能不能做某件事情，又是另一件事。」

---

# S09 — Authentication Is Not Authorization

## On-slide text

# WHO ARE YOU? ≠ WHAT MAY YOU DO?

### Authentication
**Who are you?**

### Authorization
**What are you allowed to do?**

Example:

```text
Alice logs in       → Authenticated ✅
Alice views weather → Authorized ✅
Alice deletes users → Authorized? ❓
```

> Login success does not grant every permission.

## Visual composition

Two checkpoints in sequence.

Checkpoint 1: ID badge scanner — `Authentication`.

Checkpoint 2: permission gate with multiple doors — `Authorization`.

Weather Security Center appears behind them.

## Character expression / pose

Spokesperson first checks an ID badge, then points to a separate permissions matrix. Expression emphasizes that these are two different questions.

## Teacher script

學生很容易把「有登入」等同於「有權限」。Authentication 解決的是你是誰；Authorization 解決的是你能做什麼。

例如 Alice 成功登入 Weather Security Center，只能證明她的身份。她能不能看管理資料、修改設定、刪除其他使用者，要由 authorization 決定。

今天不需要做完整 IAM 系統。我們是在建立 security review 的眼睛：看到 endpoint 時，要開始問「這個動作需要什麼權限？」

## Transition

「到目前為止我們看的都是自己寫的 code。但現代程式真正由自己寫的，可能只是一部分。」

---

# S10 — Your Dependencies Are Part of Your Application

## On-slide text

# `pip install` ALSO ADDS CODE TO YOUR SYSTEM

Our application:

```text
Our Python Code
      +
FastAPI
      +
SQLAlchemy
      +
Pydantic
      +
Other Packages
      =
Running System
```

Questions:
- What did we install?
- Which version?
- Do we still need it?
- Is there a known risk?

### Today
Understand dependency risk.

### Not today
Install five different scanners.

## Visual composition

Application assembled from LEGO-like modules. One is labeled `Our Code`; several others are external dependency modules. All become part of the same final system.

## Character expression / pose

Spokesperson examines the label/version on an incoming package before attaching it to the application.

## Teacher script

當我們 `pip install` 一個 package，其實是在把別人的 code 加入自己的系統。所以 security boundary 不會停在我們自己寫的 Python 檔案。

Dependency scanning 是專業 Secure SDLC 的重要部分。但請注意我們這門課的原則：今天不因為講到 dependency，就再裝三四套工具。

L4 的主工具仍然只有 Semgrep。Dependency risk 今天先理解概念，後面 roadmap 再看到它在完整 Secure SDLC 的位置。

## Transition

「既然風險可能藏在輸入、secret、權限、dependency，那我們是不是只要叫 AI 再 review 一次就好了？」

---

# S11 — Why Human + AI Review Still Misses Things

## On-slide text

# “PLEASE REVIEW MY CODE” IS USEFUL — BUT NOT ENOUGH

### Human review can miss
- repetitive patterns
- unfamiliar APIs
- large codebases
- known patterns we do not remember

### AI review can miss
- project context
- hidden assumptions
- false confidence
- inconsistent answers

### Better

```text
Human judgment
      +
AI assistance
      +
Deterministic security tooling
```

> **Different reviewers catch different classes of mistakes.**

## Visual composition

Three lenses inspect the same source file: Human, AI, Security Tool. Each highlights a different section. Their findings combine into one review panel.

## Character expression / pose

Spokesperson coordinates three reviewers instead of trusting a single magic AI robot.

## Teacher script

AI Code Review 很有用，我們會繼續用。但如果 prompt 只寫「幫我看這段 code 安不安全」，AI 的回答會受到上下文、模型、prompt 影響，而且有時候非常有自信地說錯。

人也會漏看。尤其 code 越多，重複的 risky pattern 越容易被忽略。

所以成熟工程不是 Human vs AI vs Tool 三選一，而是把它們組合起來。工具先找 pattern，AI 幫助解釋，人做 context judgment。

這就是今天 Semgrep 的角色。

## Transition

「那麼，有沒有一種方式，不需要把網站放到網路上，也不用先攻擊它，就直接檢查 source code？」

---

# S12 — What Is SAST?

## On-slide text

# SAST
## Static Application Security Testing

**Look at the code without needing to attack a running public system.**

```text
SOURCE CODE
     ↓
 SAST ENGINE
     ↓
RULE / PATTERN MATCHING
     ↓
 FINDINGS
     ↓
 HUMAN ANALYSIS
```

### Key idea
**Static = inspect code/artifacts without relying on live attack traffic.**

## Visual composition

Show source-code files passing through an airport-style inspection scanner. Findings emerge as annotated code lines, not as attack explosions.

Place `SAST` prominently in the center.

## Character expression / pose

Spokesperson watches a source file pass through the scanner and receives a finding report.

## Teacher script

SAST 是 Static Application Security Testing。它的重點是從 source code 或相關 artifact 找 security patterns。

這很適合我們目前的課程，因為我們的主線不是去攻擊別人的網站。我們可以在自己的電腦、自己的 Git repository 裡檢查 code。

它也很適合 Secure Development：問題越早發現，修正成本通常越低。

但 SAST 找到的是 finding，不等於已經證明世界末日。後面還要理解 context、判斷是不是 relevant，再修正和驗證。

## Board phrase

`Finding ≠ Confirmed Exploit`

`Finding = Something worth investigating`

## Transition

「所以 SAST 應該放在開發流程的哪裡？等全部寫完才掃嗎？」

---

# S13 — Shift Left: Find Security Problems Earlier

## On-slide text

# FIND IT EARLIER

```text
PLAN
 ↓
CODE
 ↓
SCAN  ← SAST can start here
 ↓
TEST
 ↓
REVIEW
 ↓
DEPLOY
```

Traditional reaction:

`Deploy → Problem → Emergency Fix`

Secure development:

`Code → Scan → Fix → Verify → Continue`

> Security is part of development, not the final decoration.

## Visual composition

Horizontal software lifecycle. A security scanner is moved from the far right/end toward the CODE stage. Use a large arrow labeled `SHIFT LEFT`.

## Character expression / pose

Spokesperson physically moves a security checkpoint earlier on the timeline, smiling as the warning is caught before deployment.

## Teacher script

Shift Left 是 secure development 很常見的概念。不是說左邊比較安全，而是把 security activity 放到 lifecycle 更早的位置。

如果問題到 production 才發現，可能要停服務、緊急修補、重新部署，甚至處理資料外洩。但如果在 coding 階段 scanner 就提醒你，修改成本小很多。

所以從今天開始，我希望學生的 Vibe Coding 心智流程不要再是 Prompt → Code → Run → Done，而要逐漸變成 Prompt → Code → Run → Test → Security Check → Review → Fix。

## Transition

「現在我們已經知道為什麼需要 SAST。接下來讓今天唯一的核心 security tool 登場。」

---

# S14 — Meet Semgrep: Our Code Security Inspector

## On-slide text

# SEMGREP
## One Representative SAST Tool

Semgrep helps us:

1. Read source code patterns
2. Apply security rules
3. Point to suspicious code
4. Explain where to investigate
5. Re-run after a fix

### Our L4 workflow

```text
Weather Security Center
          ↓
       Semgrep
          ↓
       Finding
          ↓
   AI + Human Analysis
          ↓
         Fix
          ↓
      Re-scan
```

### Remember
**Semgrep finds evidence to investigate. It does not replace engineering judgment.**

## Visual composition

Semgrep is represented as a professional code inspector standing beside the Weather Security Center source tree. A scanner highlights one line and produces a finding card with file, line, rule, and message fields.

Do not turn Semgrep into a magical shield. Emphasize inspection and evidence.

## Character expression / pose

Course spokesperson introduces the inspector with an open-hand gesture. The inspector points at one highlighted source-code line rather than celebrating a generic “secure” badge.

## Teacher script

今天只學一套代表性的 SAST 工具：Semgrep。

為什麼選它？因為學生可以很直接看到「哪一個檔案、哪一行、哪一條 rule、為什麼被標出來」，很適合把 source code、security concept 和 evidence 接在一起。

但我不希望大家形成另一個錯誤觀念：「Semgrep 沒報錯，所以我的程式百分之百安全。」沒有任何單一 scanner 能給這種保證。

Semgrep 的角色是 Security Inspector。它告訴我們哪裡值得看。接下來真正重要的是：**你看得懂 finding 嗎？你知道為什麼嗎？你修了以後有證據嗎？**

## Classroom reveal

教師此時第一次展示實際 Semgrep finding 的畫面，但暫時不要急著講所有 CLI options。

讓學生先認四個欄位：

`FILE → LINE → RULE → MESSAGE`

## Transition to S15+

「下一頁開始，我們不再只談概念。我要帶大家看 Semgrep 到底怎麼『看』程式，然後把老師故意留下的一個 insecure sample 真正掃出來。」

→ Next batch: S15 Semgrep mental model → S16 AI + Semgrep pair → S17 vulnerable sample → S18 first scan → S19 read the finding → S20 AI explanation → S21 human review.

---

# Batch 2 Teaching Intent

S07–S14 builds a funnel rather than a tool catalog:

```text
Trust Boundary
   + Secrets
   + Authorization
   + Dependencies
        ↓
There are many places to make mistakes
        ↓
Human review alone is imperfect
AI review alone is imperfect
        ↓
Use deterministic tooling as another reviewer
        ↓
SAST
        ↓
Shift security earlier
        ↓
Semgrep
```

The course deliberately does **not** turn S07–S10 into four separate labs. They are the secure-coding map. Semgrep remains the one representative hands-on security tool for AIIS_L4.