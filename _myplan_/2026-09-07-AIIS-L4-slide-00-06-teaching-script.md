# AIIS_L4 — Slide 00–06 Teaching Script

**Course:** AIIS — AI and Information Security  
**Lesson:** AIIS_L4 — How to Build an AI Cybersecurity Project / Secure Development  
**Date:** 2026-09-07  
**Status:** L1-style slide-by-slide reconstruction — Batch 1  
**Canonical story:** Code → Scan → Understand → Fix → Re-scan → Evidence  
**Shared project:** AI Weather Security Center  
**Primary security tool:** Semgrep  

---

# S00 — AIIS_L4: How to Build an AI Cybersecurity Project

## On-slide text

**AIIS_L4**

# How to Build an AI Cybersecurity Project
## AI 寫得出程式，安全嗎？

`BUILD → SCAN → UNDERSTAND → FIX → RE-SCAN → EVIDENCE`

**Mission:** Turn our AI Weather Security Center into a system we can defend with evidence.

## Visual composition

- 16:9 course title slide consistent with L1–L3 visual language.
- Center: Weather Security Center application window.
- Left: AI coding assistant handing a block of code toward the application.
- Right: a security inspector holding a scanner/magnifier over the code; one small warning marker is visible.
- Bottom: six-stage mission ribbon: BUILD → SCAN → UNDERSTAND → FIX → RE-SCAN → EVIDENCE.
- Avoid hacker stereotypes. The visual is software engineering + security inspection.

## Character expression / pose

Course spokesperson looks confident but curious, pointing at the application with one hand and at a small warning icon with the other. Expression communicates: “It works — but have we checked it?”

## Teacher script

前三課，我們已經開始建立自己的 AI Security Engineer 工作方式，也建立了 Weather Security Center。現在有一個很重要的問題：AI 幫我們把程式寫出來，而且程式真的可以執行，這是不是代表它是安全的？答案當然不是。

今天我們第一次把「寫程式」和「資安工程」真正接起來。我們不會再做另一個新專案，而是回到同一個 Weather Security Center。今天的工作只有一條主線：先看程式，再掃描，理解工具找到的問題，修正，再掃一次，最後留下證據。

所以今天不是學十種 security tools。今天只把一個工具用懂：Semgrep。

## Transition

「在開始掃描以前，我先問大家一個最危險、也最容易被忽略的問題：程式可以正常執行，代表什麼？」

---

# S01 — It Works. Is It Safe?

## On-slide text

# It Works. Is It Safe?
## 「可以跑」和「安全」是兩件不同的事

### Functional view
- API returns `200 OK`
- Weather data appears
- Database can save records
- User can use the feature

### Security view
- Can unexpected input change behavior?
- Are secrets exposed?
- Can a user access something they should not?
- Did AI introduce an unsafe coding pattern?

> **Working software is not automatically secure software.**

## Visual composition

Split screen.

Left panel: green dashboard showing Weather Security Center working normally: API 200 OK, weather card, database check mark.

Right panel: same application shown through an X-ray/security lens, exposing warning icons around input, secret/configuration, authorization, and source code.

Center divider text: `WORKS ≠ SECURE`.

## Character expression / pose

Spokesperson on left gives a thumbs-up to the working application; the same character on right changes to a thoughtful expression while looking through a magnifying glass.

## Teacher script

寫程式的第一個直覺通常是：「可以跑就好了。」例如 API 回 200、資料有顯示、SQLite 有寫進去，大家就覺得完成了。

但資安工程師看的不是只有 Happy Path。我們會問：如果輸入不是你預期的呢？如果某個設定或密碼被直接寫進程式呢？如果一個普通使用者可以碰到管理員才能碰的功能呢？

尤其 Vibe Coding 很快。AI 很容易幫你完成功能，但「功能完成」與「安全驗證」不是同一件事情。這就是 L4 要建立的第一個觀念。

## Student prompt

請學生快速回答：

**「你曾經讓 AI 寫出一段可以跑的程式後，做過哪些檢查？」**

不需要先談漏洞名稱，只讓學生意識到大多數人的流程停在 Run。

## Transition

「那麼問題來了：一個原本正常的程式，漏洞到底是在什麼時候出現的？」

---

# S02 — Our Weather Security Center Has Grown Up

## On-slide text

# One Project. Growing Every Lesson.

```text
L1  AI Security Engineer mindset
        ↓
L2  AI engineering toolbox
        ↓
L3  Build Weather Security Center
        ↓
L4  Secure what we built  ← YOU ARE HERE
```

### Today we do NOT build another app.

We secure the system we already own.

## Visual composition

Use a vertical evolution diagram rather than four unrelated boxes.

At the bottom/current stage, show the Weather Security Center larger than previous stages. Attach a security shield outline to it, but leave one small section unfinished to indicate today's mission.

Include a small `YOU ARE HERE` marker at L4.

## Character expression / pose

Spokesperson stands beside the growing project timeline, holding a toolbox in one hand and a security checklist in the other.

## Teacher script

這門課有一個很重要的設計：我們不要每週做一個互不相關的小作業。L3 做出的 Weather Security Center 不是做完就丟掉。

它會一路成長。今天 L4 我們做 Secure Development；後面 ML、DL、Red Team、Blue Team、Risk Management 都會再回到這個系統。

這樣學生最後看到的不是十幾個零散工具，而是一個系統從 Build 一路走到 Security Validation、Fix 和 Governance 的生命週期。

## Transition

「所以今天不是從空白開始。反而更有意思：我們要檢查自己已經寫好的東西。」

---

# S03 — Functional Correctness ≠ Security

## On-slide text

# Two Different Questions

### Software Engineer asks
**Does it do what we designed it to do?**

### Security Engineer also asks
**What else can it do that we did NOT intend?**

Examples:

`expected input → expected behavior` ✅

`unexpected input → ???` ⚠️

`normal user → normal function` ✅

`normal user → admin function?` ⚠️

## Visual composition

Main visual is two doors into the same application.

Door A labeled `Expected Use` leads to green expected behavior.

Door B labeled `Unexpected / Untrusted` leads to a large question mark before reaching the same system.

Do not depict an attacker. The focus is unintended behavior.

## Character expression / pose

Spokesperson points to the second path and raises an eyebrow/question gesture.

## Teacher script

Functional correctness 問的是：「系統有沒有照我的設計工作？」Security 多問了一個問題：「它會不會做出我沒有設計、也不希望它做的事情？」

例如我們設計一個 city 參數，希望使用者輸入 Taipei、Hualien、Taichung。但 security thinking 不會只測這三個正常值，而是問：如果輸入很長、格式奇怪、空值、特殊字元，系統怎麼處理？

今天我們不需要先學攻擊。先學會從 defensive engineering 的角度問這個問題，就已經跨進資安工程了。

## Board phrase

`Correctness = intended behavior`

`Security = control of unintended behavior`

## Transition

「今天我們就把這個想法變成一個可以操作、可以留下證據的工程任務。」

---

# S04 — Today's Mission: Find One Problem, Fix It, Prove It

## On-slide text

# SECURITY MISSION 04

## Find → Understand → Fix → Prove

```text
Teacher-provided insecure sample
            ↓
        Semgrep Scan
            ↓
       One Finding
            ↓
     AI Explanation
            ↓
       Human Review
            ↓
          Fix
            ↓
      Test + Re-scan
            ↓
        Evidence
```

### Success is NOT “the AI says it is fixed.”
### Success is **evidence**.

## Visual composition

Mission-board style, but professional rather than game-like hacking imagery.

Use connected evidence cards: CODE → SCAN → FINDING → FIX → TEST → CLEANER SCAN.

The final card should contain a small Git commit/evidence icon.

## Character expression / pose

Spokesperson is now in project-manager/security-reviewer mode, holding a clipboard and pointing to the mission path.

## Teacher script

今天的 Lab 很小，但流程很完整。我會提供一個刻意留下不安全寫法的 sample。你們不需要到網路上攻擊任何網站，也不需要猜怎麼製造漏洞。

我們只檢查自己擁有、老師提供的 source code。

Semgrep 找到問題之後，AI 可以幫忙解釋。但注意：AI 的回答不是證據。真正的證據是：原本 scan 找到什麼、我們理解 root cause、修改哪裡、功能測試有沒有通過、重新 scan 之後結果如何。

這就是 professional security engineering 很重要的 evidence mindset。

## Transition

「要做這件事，我們先要知道 Secure Coding 到底是在保護什麼。」

---

# S05 — What Is Secure Coding?

## On-slide text

# Secure Coding
## 在寫程式的同時，控制安全風險

Secure coding is not one magic function.

It is a set of engineering habits:

1. **Validate input** — 不相信所有輸入
2. **Protect secrets** — 不把敏感資訊直接放進 source code
3. **Control access** — 誰可以做什麼？
4. **Use dependencies carefully** — 你引用的 code 也是系統的一部分
5. **Review and verify** — 不因為 code 能跑就停止檢查

### Mindset

`Never blindly trust INPUT, CODE, AI, or DEPENDENCIES.`

## Visual composition

Weather Security Center in center with five protective rings or five surrounding checkpoints: INPUT, SECRETS, ACCESS, DEPENDENCIES, REVIEW.

Avoid dense text in visual; detailed labels remain in slide text.

## Character expression / pose

Spokesperson places five inspection tags around the application, expression focused and methodical.

## Teacher script

Secure Coding 不是背一堆漏洞名稱，也不是在程式最後面加一個 security function 就完成。

它比較像一組習慣。輸入進來以前要想能不能信；secret 要想放在哪裡；功能要想誰有權限；裝套件要知道你其實把別人的 code 帶進自己的系統；AI 產生的 code 也要 review。

這五個觀念今天先建立地圖。我們不會在 L4 一次實作所有 security technology。今天選一個代表性的入口：source-code scanning。

## Transition

「但為什麼我們明明沒有故意寫漏洞，漏洞還是會出現？」

---

# S06 — How Does a Vulnerability Enter Our Code?

## On-slide text

# Vulnerabilities Usually Do Not Arrive Wearing a Warning Sign

They often enter as an **engineering shortcut**.

```text
Need feature quickly
      ↓
Ask AI / write code
      ↓
Code works
      ↓
Skip security review
      ↓
Unsafe pattern remains
```

Common causes:

- We trusted input too early
- We hard-coded something for convenience
- We forgot an authorization check
- We copied an unsafe example
- AI generated a plausible but unsafe pattern
- We did not know the pattern was risky

> **A vulnerability is often a normal-looking piece of code in the wrong security context.**

## Visual composition

Show a clean-looking code pipeline. Everything appears green until a magnifying glass zooms into one ordinary line and reveals a small warning symbol.

Side mini-story: `“Just make it work first…”` → code → hidden risk.

No malicious attacker character.

## Character expression / pose

Spokesperson initially looks satisfied at the working code, then notices the magnified warning and changes to an alert/thoughtful expression.

## Teacher script

漏洞很多時候不是某個人故意寫一行「我要讓系統不安全」。它常常只是方便。

開發者趕著完成功能，先把值 hard-code；為了測試先跳過一個 check；從網路複製一段 sample；或直接接受 AI 給的第一版程式。

最重要的是，這些 code 看起來可能非常正常。所以 security review 不能只靠「我看起來覺得沒問題」。我們需要工具幫我們找已知的 risky patterns。

這就帶到下一段：Static Application Security Testing，也就是 SAST，以及我們今天的主工具 Semgrep。

## Transition to S07+

**「如果漏洞藏在看起來很普通的 source code 裡，我們能不能在程式還沒上線、甚至不用攻擊它以前，就先找到問題？」**

→ Next: Trust Boundary → Secrets → Authorization → Dependencies → SAST → Semgrep.

---

# Batch 1 Teaching Intent

S00–S06 不急著教 Semgrep 指令，而是先建立學生使用 security scanner 的理由：

```text
AI makes coding faster
        ↓
Working code can still be unsafe
        ↓
Our existing Weather Security Center becomes the object of review
        ↓
Secure coding is an engineering habit
        ↓
Unsafe patterns can look normal
        ↓
Therefore we need systematic source-code inspection
        ↓
SAST / Semgrep
```

This preserves the AIIS course principle:

**Concept first → one representative tool → achievable lab → evidence.**

The next batch should continue S07–S14 and progressively introduce Trust Boundary, Secrets, Authentication/Authorization, Dependency Risk, Code Review limitations, SAST, and finally Semgrep.