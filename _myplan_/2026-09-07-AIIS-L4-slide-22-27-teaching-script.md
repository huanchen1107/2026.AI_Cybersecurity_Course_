# AIIS_L4 — Slide 22–27 Teaching Script

**Lesson:** AIIS_L4 — How to Build an AI Cybersecurity Project / Secure Development  
**Batch:** 4 — S22–S27  
**Story:** Root Cause → Safer Design → Fix → Regression Test → Re-scan → Evidence → GitHub  
**Primary tool:** Semgrep  
**Shared project:** AI Weather Security Center

---

# S22 — Root Cause: Don't Fix the Warning, Fix the Design

## On-slide text

# FIND THE ROOT CAUSE
## 不要只想「怎麼讓警告消失」

Our sample:

```text
Untrusted request input
        ↓
Inserted into command string
        ↓
Shell interprets the string
```

### Surface symptom
Semgrep reports a risky pattern.

### Root cause
**Untrusted data crosses directly into a dangerous execution mechanism.**

### Better question

> Can we remove the dangerous design instead of filtering around it?

## Visual composition

Use an iceberg/root diagram. Above water: `Semgrep Finding`. Below water: data-flow root cause `Untrusted Input → Shell Execution`.

Beside it, show scissors cutting the dangerous connection rather than placing many small filters around the warning.

## Character expression / pose

Spokesperson ignores a tempting “hide warning” button and points deeper into the data-flow diagram.

## Teacher script

這是整個 Lab 最重要的工程觀念之一：不要把 scanner 當成遊戲，目標不是把紅色數字變成零。

Semgrep finding 是 symptom。真正要問的是 root cause。

我們這個 sample 的核心問題，是外部輸入一路進到 shell execution。假如只是做幾個字元替換，可能看起來修了，但危險設計仍然存在。

Secure coding 優先思考的是：能不能根本不要經過 shell？有沒有較安全的 API？能不能把輸入限制成結構化、明確允許的資料？

所以我們修的是 design，不是修 scanner 的心情。

## Board phrase

`Don't silence the scanner.`

`Remove or control the risky data flow.`

## Transition

「既然 root cause 是 untrusted input 進入 shell，那我們就讓 AI 幫忙提出 safer design，但由我們決定怎麼改。」

---

# S23 — Fix: Prefer a Safer API and Explicit Validation

## On-slide text

# REMOVE THE DANGEROUS PATH

### Before

```python
subprocess.run(
    f"ping -c 1 {host}",
    shell=True,
    ...
)
```

### Safer teaching direction

```python
import ipaddress
import subprocess

@app.get("/tools/ping")
def ping(host: str):
    safe_host = str(ipaddress.ip_address(host))

    result = subprocess.run(
        ["ping", "-c", "1", safe_host],
        shell=False,
        capture_output=True,
        text=True,
        timeout=3,
    )

    return {"output": result.stdout}
```

### What changed?

`Validate → Structured arguments → No shell interpretation → Timeout`

## Visual composition

Before/After code comparison. Draw the data flow in both:

BEFORE: input → string → shell.

AFTER: input → validation → argument list → process.

The visual emphasis is the architecture change, not merely changed syntax.

## Character expression / pose

Spokesperson removes the `shell` bridge from the old path and installs a validation checkpoint plus structured-arguments path.

## Teacher script

這裡示範的是「設計方向」，不是叫學生背這幾行。

第一，使用 `ipaddress` 把我們真正允許的輸入明確化。第二，不再把整個 command 拼成一個字串交給 shell 解釋，而是使用 argument list。第三，`shell=False`。第四，加 timeout，避免 process 無限制等待。

注意：實際 production 還可能需要更多 operational controls；但今天的 learning objective 是看懂 root cause 如何映射到 safer design。

## AI remediation prompt

```text
Given this Semgrep finding and the source code,
propose the smallest maintainable defensive fix.

Requirements:
- remove the root cause rather than suppress the finding,
- avoid shell interpretation if not required,
- validate input according to the feature's real requirements,
- preserve expected functionality,
- explain each change,
- propose tests,
- do not disable the security rule merely to make the scan pass.
```

## Lab action

學生先閱讀 AI 建議，再由人確認修改。保存 code diff 作為 Evidence Artifact C。

## Transition

「程式變得比較安全了。但如果功能壞掉，這也不是一個好的 security fix。」

---

# S24 — Regression Test: Security Fix Must Not Break the Feature

## On-slide text

# FIX SECURITY — KEEP FUNCTIONALITY

After remediation, test expected behavior.

### Minimum checks

```text
Valid input
   ↓
Expected response?  ✅ / ❌

Invalid input
   ↓
Rejected safely?   ✅ / ❌

Application
   ↓
Still starts/runs?  ✅ / ❌
```

### Evidence Artifact D

**Functional test result after the security change**

> A security fix is incomplete if nobody checks what it broke.

## Visual composition

Balance scale: left shield `Security`; right gear `Functionality`. Both must remain balanced.

Below, three test cards: Valid Input / Invalid Input / Application Health.

## Character expression / pose

Spokesperson holds both a shield and a green test checklist, indicating security and functionality must coexist.

## Teacher script

這一步是很多 security demo 會跳過的地方。修漏洞不是把功能整個刪掉就叫安全。

我們要確認原本合法使用情境仍然工作，同時不合理輸入能被安全拒絕，而且 FastAPI application 本身還能正常啟動。

這就是 regression thinking。Security engineering 本質上仍然是 software engineering。

AI 也可以幫我們產生 test case，但 test result 本身才是 evidence。

## Lab action

學生執行老師指定的 basic/API test，保存 pass/fail 結果。

## Transition

「功能測試通過，還少最後一個安全問題：原本 Semgrep 找到的 risky pattern 現在還在嗎？」

---

# S25 — Re-scan: Verify the Security Change

## On-slide text

# STEP 2 — SCAN AGAIN

```text
BEFORE
Semgrep Finding ⚠️
      ↓
Root Cause Analysis
      ↓
Code Fix
      ↓
Functional Test ✅
      ↓
AFTER
Semgrep Re-scan
```

### Ask

- Is the original finding gone?
- Did the change create another finding?
- Are we using the same relevant scan configuration?

### Evidence Artifact E

**AFTER SCAN**

> Fix → Verify. Never stop at “I changed the code.”

## Visual composition

Same scanner from S18 used again, reinforcing repeatability. Place BEFORE and AFTER evidence cards side by side, connected by the code-change arrow.

## Character expression / pose

Spokesperson deliberately returns to the same scanner after testing instead of walking away after editing code.

## Teacher script

這就是 re-scan。它很簡單，但在工程流程裡非常重要。

我們用相同或可比較的 scan configuration 再跑一次，確認原本 finding 是否消失，也看修改有沒有引入新的問題。

注意語言仍然要精確。如果 finding 消失，我們可以說「這個 scanner 在目前 rules/config 下不再報這個 pattern」。不能直接把它誇大成「系統現在百分之百安全」。

這種精確描述就是 evidence-based security。

## Transition

「現在我們手上其實已經有一條非常漂亮的資安證據鏈。把它排在一起看看。」

---

# S26 — Before → Root Cause → Fix → Test → After

## On-slide text

# THIS IS YOUR SECURITY EVIDENCE CHAIN

```text
① BEFORE
Semgrep finding
       ↓
② UNDERSTAND
Source → Flow → Sink
       ↓
③ ROOT CAUSE
Why the design is risky
       ↓
④ FIX
Code diff + rationale
       ↓
⑤ TEST
Expected behavior still works
       ↓
⑥ AFTER
Re-scan result
```

### Add AI transparently

`AI helped explain and propose.`

`Human reviewed and verified.`

## Visual composition

Six connected evidence cards like a forensic/engineering timeline. Each card has an artifact icon: scanner, flow diagram, root, diff, test check, scanner.

AI assistant appears as a side annotation connected to UNDERSTAND and FIX—not as owner of the entire chain.

## Character expression / pose

Spokesperson stands at the end holding a completed evidence folder rather than a generic “Secure” trophy.

## Teacher script

這六格就是我希望學生最後真正帶走的東西。

如果你只交一張 Semgrep screenshot，我不知道你有沒有理解。如果只交修改後 code，我不知道原本問題是什麼。如果只說 AI 幫我修好了，更沒有 verification。

但把 Before、Understand、Root Cause、Fix、Test、After 串起來，就可以清楚回答：我們發現什麼、為什麼改、改了什麼、功能有沒有壞、工具驗證結果如何。

這就是 evidence package，也會一路延伸到後面的 Red Team、Blue Team 和期末專題。

## Student deliverable template

```text
Finding:
Evidence:
Root Cause:
AI Assistance:
Human Decision:
Fix:
Functional Test:
Re-scan:
Remaining Risk / Limitation:
```

## Transition

「最後一件事：這些 evidence 不應該散落在桌面 screenshot。工程專案要能追蹤它的歷史。」

---

# S27 — GitHub: Make Security Work Traceable

## On-slide text

# SECURITY WORK SHOULD BE TRACEABLE

GitHub evidence can connect:

```text
Prompt / Analysis
       ↓
Finding Report
       ↓
Code Change
       ↓
Test Result
       ↓
Re-scan Result
       ↓
Commit / Documentation
```

### Suggested commit

```text
fix(security): remove unsafe shell execution in ping endpoint
```

### Commit message answers

- What changed?
- Why?
- How was it verified?

> Git history turns “trust me” into traceable engineering evidence.

## Visual composition

Git commit timeline with three stages: BEFORE finding → security fix commit → AFTER verification. Attach evidence cards to the relevant commit.

Keep GitHub as the engineering record, not decorative branding.

## Character expression / pose

Spokesperson files the completed evidence package into a version-controlled timeline and places a check mark beside the commit.

## Teacher script

L2 我們已經建立 Git/GitHub 的工程工作方式。L4 要讓學生看到，version control 不只是備份 code，也可以保存 security reasoning。

一個好的 security commit 不只是「update code」。至少要讓未來的人知道：改了什麼、為什麼改、怎麼驗證。

因此這堂課最後的成果不是「我會下 Semgrep 指令」，而是一個可以追蹤的 security change。

這也替後面課程建立共同語言。以後 Red Team 找到問題、Blue Team 修問題，都可以使用同樣的 evidence chain。

## Transition to S28+

**「我們今天只實作一個 SAST 工具，但真實公司的 Secure SDLC 當然不只 Semgrep。最後兩頁，我們把今天的位置放回完整地圖，而且不把所有工具塞進本課。」**

→ S28 Professional Secure SDLC roadmap → S29 Mission Complete + bridge to AIIS_L5.

---

# Batch 4 Teaching Intent

This batch completes the hands-on security engineering loop:

```text
Finding
  ↓
Root Cause
  ↓
Safer Design
  ↓
Human-reviewed Fix
  ↓
Regression Test
  ↓
Re-scan
  ↓
Before / After Evidence
  ↓
GitHub Traceability
```

## Required student evidence by S27

1. Semgrep BEFORE result
2. Finding interpretation: Source → Flow → Sink
3. AI analysis prompt + response
4. Human root-cause decision
5. Code diff
6. Functional/regression test result
7. Semgrep AFTER result
8. Short remaining-risk/limitation statement
9. Git commit/documentation

## Scope guardrail

Do not add another required scanner in this lab. Bandit, CodeQL, SonarQube, Snyk, Trivy and related tools belong only in the final roadmap / Further Exploration section. The learning objective is to complete one full security loop with evidence.