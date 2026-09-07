# AIIS_L4 — Slide 15–21 Teaching Script

**Lesson:** AIIS_L4 — How to Build an AI Cybersecurity Project / Secure Development  
**Batch:** 3 — S15–S21  
**Story:** Semgrep mental model → AI + Tool → Vulnerable Sample → Scan → Finding → AI Explanation → Human Review  
**Primary tool:** Semgrep  
**Lab boundary:** local / teacher-provided / owned source code only

---

# S15 — How Does Semgrep “See” Code?

## On-slide text

# SEMGREP DOES NOT “UNDERSTAND” LIKE A HUMAN
## It looks for code structures and patterns described by rules.

```text
SOURCE CODE
    ↓
PARSE / STRUCTURE
    ↓
SECURITY RULES
    ↓
PATTERN MATCH
    ↓
FINDING
```

A finding usually tells us:

`FILE → LINE → RULE → MESSAGE`

### Important

**Match ≠ proof of compromise**

**Match = investigate this code**

## Visual composition

Left: a Python source file. Middle: code is transformed into simplified structural blocks/tree. Right: one block matches a rule card and generates a finding.

Do not show Semgrep as an AI brain. Visually distinguish deterministic rule-based inspection from generative AI.

## Character expression / pose

Spokesperson holds two cards: `RULE` and `CODE`. The matching shapes align and produce a small finding card.

## Teacher script

上一頁我們讓 Semgrep 登場。現在要先避免一個誤解：Semgrep 不是像 ChatGPT 一樣坐在那裡「讀懂整個專案然後自由回答」。

它使用 rules 去找特定 code structure 或 pattern。當某段 code 符合一條 security rule，工具就產生 finding，告訴我們檔案、位置、rule 和訊息。

這種 deterministic tool 的價值就是：同樣的 code、同樣的 rules，可以穩定重複檢查。這正好和生成式 AI 的能力互補。

所以看到 finding 時不要直接說「被駭了」。正確語言是：「這裡符合一個值得調查的 risky pattern。」

## Transition

「既然 Semgrep 擅長穩定找 pattern，而 AI 擅長解釋，那這兩個工具放在一起會怎麼樣？」

---

# S16 — AI + Semgrep: A Security Pair

## On-slide text

# TOOL FINDS. AI EXPLAINS. HUMAN DECIDES.

```text
Semgrep
Find suspicious pattern
        ↓
AI Assistant
Explain code + risk + possible fix
        ↓
Human Engineer
Check context + decide + verify
```

### Three different jobs

**Semgrep:** Where should I look?

**AI:** What might this mean?

**Human:** Is it really relevant here, and did we fix it correctly?

> AI for Security = augment the engineer, not remove the engineer.

## Visual composition

Three-person relay around the same finding card. Semgrep passes evidence to AI; AI annotates/explains; human engineer makes the final decision and checks tests.

## Character expression / pose

Spokesperson is the human engineer in the center, receiving information from both sides rather than standing behind AI.

## Teacher script

這一頁其實就是 AIIS 的核心精神。

如果只有 Semgrep，初學者看到 rule name 和 security message 可能完全不知道在講什麼。如果只有 AI，AI 又可能沒有 deterministic evidence，甚至 hallucinate 一個不存在的問題。

把兩個接起來就很好：Semgrep 告訴我們「看這裡」；AI 幫我們把 technical finding 翻譯成可以理解的語言；最後人要回到 source code 和系統 context 做判斷。

這就是 AI for Security，而不是「AI 自己負責資安」。

## AI prompt pattern shown on slide footer

`Explain this Semgrep finding using the code context. Separate evidence, inference, risk, and suggested fix. Do not claim exploitation unless evidence proves it.`

## Transition

「現在我們不要再看抽象流程。老師已經在自己的 Lab 裡故意留下一段有問題的 code。」

---

# S17 — Lab Target: Teacher-Provided Insecure Sample

## On-slide text

# LAB 04 — FIND THE PROBLEM

### Target
Teacher-provided code inside our local Weather Security Center.

### Example teaching sample

```python
import subprocess

@app.get("/tools/ping")
def ping(host: str):
    result = subprocess.run(
        f"ping -c 1 {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"output": result.stdout}
```

### Question

**The endpoint works. What could go wrong with this design?**

### Safety boundary

Do not test against external systems. We inspect the source code in our owned/local classroom project.

## Visual composition

Large code card in center. Highlight only two areas visually: `host` entering from the request and `shell=True` near command execution. A dotted path connects them, but do not reveal the final answer immediately.

## Character expression / pose

Spokesperson looks at the two highlighted code locations with a detective-style magnifier, inviting students to reason before the scanner is run.

## Teacher script

這是一個非常適合教學的 sample。功能需求看起來很合理：給我 host，我幫你 ping 一次，然後把結果回傳。

如果只看 Happy Path，輸入一個正常 host，它真的可能工作。所以開發者很容易說「完成」。

但請大家先不要查答案。看兩個地方：第一，`host` 是從哪裡來？第二，它最後進到哪裡？

這裡的教學目的不是讓學生學 command injection 的攻擊技巧，而是學 **untrusted input 不應直接進入危險的 execution sink**。

我們也不需要真的對任何外部主機做攻擊。source code 本身已經足夠讓我們練習 secure review。

## Teacher note

若實際課堂環境不適合 `ping`，可使用更簡化的 teacher-only toy function。核心是 source → sink data flow，不要求學生製作 exploit payload。

## Transition

「現在先不要改 code。我們讓 Security Inspector 先做第一次檢查，留下 Before evidence。」

---

# S18 — First Scan: Capture the BEFORE Evidence

## On-slide text

# STEP 1 — SCAN BEFORE FIXING

Example classroom workflow:

```bash
semgrep scan --config auto .
```

### Do not rush to fix.
First capture:

1. File
2. Line
3. Rule
4. Message
5. Relevant code

### Evidence Artifact A

**BEFORE SCAN**

`Finding exists → save the result`

## Visual composition

Terminal on left running Semgrep. On right, a clean evidence card with five fields: FILE / LINE / RULE / MESSAGE / CODE.

A large `BEFORE` stamp appears at top—not red panic imagery.

## Character expression / pose

Spokesperson takes a snapshot/clipboard note of the finding before touching the source code.

## Teacher script

很多學生看到 scanner 報錯的第一反應是趕快改掉。但今天我要大家故意慢一點。

資安工程需要 evidence。你如果一看到問題就改，最後只剩「現在沒有報錯」，卻沒有辦法說清楚原本發生什麼。

所以第一件事是保存 BEFORE scan。至少記住 file、line、rule、message 和相關 code。

Semgrep 的實際 rule 名稱可能依當時 ruleset 或版本不同，因此教材不要把某一個特定 rule ID 當永久契約。教學重點是學生能讀 finding 結構。

## Lab action

學生在 teacher-provided repository / local copy 執行指定 Semgrep scan，截取或保存結果。

## Transition

「Scanner 給我們一堆文字。真正的能力不是『有跑過 Semgrep』，而是能不能把 finding 讀懂。」

---

# S19 — Read the Finding Like an Engineer

## On-slide text

# DON'T ASK “RED OR GREEN?”
## Ask what the finding actually says.

### Read in this order

**1. WHERE?**
Which file and line?

**2. WHAT?**
Which code pattern triggered the rule?

**3. WHY?**
Why might this pattern be risky?

**4. CONTEXT?**
Can untrusted data reach it?

**5. ACTION?**
What should we investigate or change?

### For our sample

```text
Request input: host
        ↓
String construction
        ↓
Shell execution
```

## Visual composition

Finding report enlarged and annotated with numbered callouts 1–5. Beside it, a three-node data-flow diagram from input to command execution.

## Character expression / pose

Spokesperson traces the data flow with a pen rather than staring at severity color.

## Teacher script

Scanner 最容易被錯用的方法，就是只看紅色幾個、綠色幾個。真正的工程分析要回到 code。

先找位置，再看什麼 pattern 觸發，然後問為什麼 risky。最重要的是 context：這個資料是不是使用者能控制？它有沒有直接走到一個敏感 operation？

在這個 sample 裡，我們真正要學生看懂的是 data flow：request 的 `host` → 字串 → shell execution。

這比背「這叫某某漏洞」重要得多。名稱以後可以查，但 source、flow、sink 的思考方式可以帶到很多安全問題。

## Board phrase

`SOURCE → FLOW → SINK`

## Transition

「如果學生看不懂 Semgrep 的英文訊息，這時候 AI 很有用。但 prompt 不能只問：『這嚴重嗎？』」

---

# S20 — Ask AI to Explain the Finding, Not Invent a Story

## On-slide text

# AI SECURITY ANALYSIS PROMPT

```text
You are assisting with defensive source-code review.

Given:
1. the Semgrep finding,
2. the relevant source-code snippet,
3. the fact that this is our local classroom project,

explain:
- what the tool actually observed,
- what data is untrusted,
- what sensitive operation receives it,
- why this pattern may be risky,
- a safer coding approach,
- what must still be verified by a human.

Separate FACTS from INFERENCES.
Do not claim the system was exploited unless evidence proves it.
```

### AI output is an analysis aid — not final evidence.

## Visual composition

Left: Semgrep finding + code snippet entering an AI assistant. Right: AI answer separated into five labeled boxes: FACT / DATA FLOW / RISK / FIX IDEA / VERIFY.

Visually reject one faded speech bubble saying “Your system has definitely been hacked!” with a cross-out symbol.

## Character expression / pose

Spokesperson edits a vague prompt into a structured prompt, showing the difference between casual AI use and engineering use.

## Teacher script

這就是 AI for Security 真正值得教的地方。

如果你只把一張 screenshot 丟給 AI 問「怎麼辦」，AI 可能把很多 context 自己補完。我們要教學生提供 finding、code、環境，並要求 AI 把 Fact 和 Inference 分開。

例如 Semgrep 能證明的是「這段 code 符合某個 risky pattern」。它不能單靠 static finding 證明「已經有人成功利用」。

所以 prompt 裡特別要求：沒有 evidence 就不要宣稱 exploited。這會讓學生逐漸學會 evidence-based AI usage。

## Lab action

學生把自己的 Semgrep finding 與相關 source snippet 提供給課堂指定 AI assistant，產生一份 structured explanation。

保存 Prompt + AI Response 作為 Evidence Artifact B，但標示為 `AI Analysis`, 不是 scanner evidence。

## Transition

「AI 已經給你修法了。現在可以直接按 Accept All 嗎？不行。這就是今天最重要的一關。」

---

# S21 — Human Review: Never “Accept All” Security Fixes Blindly

## On-slide text

# AI SUGGESTED A FIX. NOW YOU REVIEW IT.

Before accepting a security fix, ask:

1. Does it remove the **root cause**?
2. Does the feature still need this dangerous operation?
3. Is there a **safer API/design**?
4. Does the fix change expected behavior?
5. Can we **test** it?
6. Can we **re-scan** it?

### Bad workflow

`Finding → AI → Accept All → Done ❌`

### Engineering workflow

`Finding → AI → Human Review → Fix → Test → Re-scan → Evidence ✅`

## Visual composition

Two paths.

Top faded path: AI suggestion → giant `ACCEPT ALL` button → question mark.

Bottom primary path: AI suggestion → human review checkpoint → code change → test → scanner → evidence package.

## Character expression / pose

Spokesperson deliberately stops their hand before the Accept All button and instead opens a review checklist.

## Teacher script

這一頁我要特別停一下。因為 Vibe Coding 最容易養成的習慣就是 Accept All。

一般 UI 小修改也許問題不大，但 security remediation 不能只因為 AI 說「我已經修好」就結束。

第一個問題永遠是 root cause。以我們的 sample 來說，問題不是某個字串長得不好看，而是 untrusted input 被帶到 shell execution。那麼真正的修法應該從設計上降低或移除這個危險資料流，而不是只做表面字串替換。

接著還要測原本功能，最後 re-scan。這樣才形成 evidence chain。

下一批我們正式做這件事：Root Cause → Safer Design → Fix → Regression Test → Re-scan → Before/After Evidence。

## Transition to S22+

**「我們現在已經找到問題、理解問題，也得到 AI 的建議。接下來不是『修一行 code』，而是先回答：真正的 Root Cause 是什麼？」**

→ S22 Root Cause Analysis → S23 Fix → S24 Regression Test → S25 Re-scan → S26 Before/After → S27 GitHub Evidence.

---

# Batch 3 Teaching Intent

This batch is the pivot from lecture to evidence-driven lab:

```text
Semgrep rule-based inspection
          ↓
Semgrep + AI + Human roles
          ↓
Teacher-provided vulnerable sample
          ↓
BEFORE scan
          ↓
Read finding as SOURCE → FLOW → SINK
          ↓
Use structured AI explanation
          ↓
Human review before remediation
```

## Safety / teaching guardrail

The lab deliberately teaches vulnerability recognition and defensive source-code remediation without requiring students to create exploit payloads or target third-party systems. All scanning and code analysis stays within teacher-provided, local, owned, or explicitly authorized course environments.

## Evidence accumulated so far

- **Artifact A:** Semgrep BEFORE scan
- **Artifact B:** Prompt + AI structured explanation
- Next batch will produce:
  - code diff / remediation,
  - functional regression test,
  - AFTER scan,
  - final Before → Root Cause → Fix → Test → After evidence chain.