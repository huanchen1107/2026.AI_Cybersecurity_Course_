# AIIS_L4 — Content-Driven Visual Audit（S01–S27）

Date: 2026-09-07
Status: CANONICAL VISUAL SPEC
Mission: SECURE — scan, evaluate, fix, test, re-scan, and verify source-code security findings in the same Weather Security Center.
Core tool: Semgrep.
Canonical loop: `SCAN → FIND → UNDERSTAND → FIX → TEST → RE-SCAN → VERIFY`.
Safety boundary: course-owned/offline source code only; source-code analysis and remediation, not unauthorized external attack activity.

## Audit rule
Every slide must derive Huange visual from the slide concept. Required: Role → Expression → Action → Prop → direct interaction with code/finding/evidence. Generic hacker decoration, hooded attacker imagery, repeated pointing, or decorative terminal screens fail.

## S01–S06 — Working code becomes review target
- S01 UNDERSTAND → SECURE — Huange = Security Engineer. Receives transparent Weather Center from L3, rotates it from `HOW IT WORKS` view to `HOW COULD IT FAIL?` review view. Speech: `看懂系統之後，現在開始檢查它。`
- S02 Working ≠ Secure — Skeptical Reviewer. One hand presses RUNNING ✓, other holds magnifier over source code with `SECURE ?`. `能跑，是功能證據；不是安全證據。`
- S03 Why scan source code? — Code Inspector. Opens source repository before deployment; magnifier searches risky patterns without attacking any website. `先檢查自己的 Code，不必先去攻擊任何網站。`
- S04 Meet Semgrep — SAST Operator. Feeds repository into Semgrep scanner and receives Finding Cards; no cyber-attack imagery. `Semgrep 幫我們找值得檢查的程式模式。`
- S05 Scanner ≠ Judge — Evidence Reviewer. Semgrep raises a Finding card; Huange places it into `NEEDS REVIEW`, not `CONFIRMED VULNERABILITY`. `Finding 是線索，不是判決。`
- S06 Security loop map — Security Lead. Stands above seven stations SCAN→FIND→UNDERSTAND→FIX→TEST→RE-SCAN→VERIFY and places a single Finding Token at SCAN. `今天不是掃一次；我們要走完整個修補閉環。`

## S07–S12 — SCAN / FIND / UNDERSTAND
- S07 Define scan target — Scope Controller. Places only Weather Security Center source folder inside authorized scan boundary; external sites remain outside. `先確認 Target 是我們自己的程式碼。`
- S08 Run Semgrep — Scanner Operator. Presses SCAN; repository files pass through Semgrep and produce findings. `工具先幫我們縮小要看的範圍。`
- S09 Read a finding — Finding Reader. Holds one card showing rule/file/line/message; points to each field in order. `先讀清楚：哪個 Rule、哪個 File、哪一行、說了什麼。`
- S10 Jump to code evidence — Code Detective. Finding card is physically linked to highlighted source line; magnifier checks surrounding context. `報告說哪裡有問題，我們就回 Code 看證據。`
- S11 Pattern ≠ Exploit — Context Analyst. Left card `risky pattern`; right card `actual context`; keeps `exploit/impact` question mark until evidence exists. `看到危險模式，不代表已經證明可被利用。`
- S12 Ask four questions — Security Investigator. Places four evidence cards around finding: What input? Who controls it? What operation? What impact? `不要只問「工具說什麼」，要問「程式實際做什麼」。`

## S13–S18 — Evaluate and fix
- S13 Source → Sink concept — Data-flow Investigator. Traces one untrusted-input packet from source through code toward sensitive operation/sink. `風險常常藏在資料從哪裡來、最後到哪裡去。`
- S14 Trust boundary — Boundary Inspector. Stops external/user-controlled input at boundary gate and marks validation/control point. `跨過 Trust Boundary 的資料，不能自動相信。`
- S15 Prioritize finding — Risk Analyst. Places finding on simple Likelihood × Impact board using actual context evidence. `不是 Finding 越多越危險；先看真正的風險。`
- S16 AI-assisted explanation — AI Review Partner. AI produces explanation card; Huange checks it against Semgrep rule + source line + context. `AI 可以解釋 Finding，但不能替代 Evidence。`
- S17 Design minimal fix — Remediation Designer. Compares narrow safe patch path with giant unrelated refactor cloud; chooses minimal control. `修安全問題，不代表重寫整個系統。`
- S18 Apply fix — Secure Coder. Replaces/guards the risky operation in a focused diff; before/after code blocks physically aligned. `Fix 必須對準剛才確認的風險。`

## S19–S24 — TEST / RE-SCAN / VERIFY
- S19 Diff review — Patch Reviewer. Magnifier compares before/after diff and checks that unrelated files were not changed. `先確認我們修了什麼，也確認沒有順便亂改。`
- S20 Functional regression test — Tester. Runs Weather Center after patch; checks existing weather data/UI behavior. `安全修補不能把原本功能修壞。`
- S21 Security-specific test — Security Verifier. Uses safe local test case to exercise the remediated code path; no attack against external targets. `功能正常還不夠；剛才的風險路徑也要驗證。`
- S22 Re-scan — Scanner Operator returns. Same repository passes through same Semgrep scanner; original Finding Token is compared before/after. `修完一定要再掃；不要靠記憶宣布問題消失。`
- S23 Finding disappeared? — Evidence Comparator. Left `BEFORE: finding present`, right `AFTER: finding absent`; Huange still checks tests/diff. `Finding 消失是重要證據，但不是唯一證據。`
- S24 Verify the fix — Security Approver. Table contains Original Evidence / Patch Diff / Functional Test / Security Test / Re-scan; only then stamps VERIFIED. `修補完成必須有一整條 Evidence Chain。`

## S25–S27 — Evidence / Lab / handoff
- S25 Remediation evidence package — Evidence Curator. Places Scan Report, Finding, Code Evidence, Risk Reasoning, Fix Diff, Test, Re-scan into one folder. `不要只交「我修好了」；交出你怎麼證明。`
- S26 Student Secure-Code Lab — Security Coach. Hands student one authorized Finding Token and seven-step worksheet; student avatar moves through loop, Huange does not solve it. `每組只要把一個 Finding 做完整，比掃出一百個更重要。`
- S27 SECURE complete → LEARN next — Handoff Guide. Holds Weather Center with green verified patch seal; points toward next phase `LEARN: Security Data → ML`, while the remediation evidence stays attached to project history. `我們已經會 Build、Manage、Understand、Secure；下一步讓機器從 Security Data 學習。`

## Critical visual callbacks
- S01 L3 transparent system → L4 review target.
- S05 `Finding ≠ Confirmed Vulnerability` → S24 VERIFIED only after evidence chain.
- S06 seven-step empty loop → S26 student completes same loop.
- S08 first scan → S22 same scanner re-scan.
- S10 original code evidence → S18 focused fix → S19 diff.
- S15 risk reasoning → S24 final verification.
- S02 `RUNNING ✓ / SECURE ?` → S24 `FUNCTION ✓ + SECURITY EVIDENCE ✓`.

## Audit result
S01–S27: content-driven visual direction defined for every page.
Critical anchor slides: S02, S05, S06, S10, S13, S14, S18, S22, S24, S26.

## Character arc
Security Engineer → Skeptical Reviewer → Code Inspector → SAST Operator → Evidence Reviewer → Security Lead → Scope Controller → Scanner Operator → Finding Reader → Code Detective → Context Analyst → Security Investigator → Data-flow Investigator → Boundary Inspector → Risk Analyst → AI Review Partner → Remediation Designer → Secure Coder → Patch Reviewer → Tester → Security Verifier → Scanner Operator → Evidence Comparator → Security Approver → Evidence Curator → Security Coach → Handoff Guide.

## PPT failure conditions
- generic hooded hacker / attack graphics unrelated to source-code review;
- character only pointing at text;
- Semgrep shown as automatically proving vulnerability;
- re-scan omitted;
- fix shown without functional regression test;
- external target attack imagery;
- same static Huange pose repeated across slides.

A student should be able to look at the illustration and infer whether the page is about scanning, reading evidence, understanding context, fixing, testing, re-scanning, or verifying.