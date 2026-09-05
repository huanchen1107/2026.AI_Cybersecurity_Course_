# Lesson 1 — AI 資安工程師的工具箱

## Learning Goal
建立整門課共同工具、AI-assisted development 與安全工程觀念。工具不是目的；學生要知道每個工具在 `BUILD → LEARN → ATTACK → DEFEND → GOVERN` 中扮演什麼角色。

## Main Topics

1. What is Vibe Coding?
2. Traditional Coding vs Vibe Coding
3. ChatGPT / Claude / Gemini / Copilot 類工具能做什麼
4. AI Coding Agent 與 Antigravity
5. Prompt 如何寫成 requirement / acceptance criteria
6. Requirements > 只叫 AI 寫 code
7. Python development environment
8. FastAPI preview
9. SQLite / SQLAlchemy preview
10. Git / GitHub as memory, evidence, reproducibility
11. Kali Linux / VM / Docker 概念
12. TryHackMe / CTF / authorized cyber range
13. Dependency awareness / software supply chain
14. 為什麼 AI 產生的程式可能不安全
15. Prompt → Plan → Code → Run → Test → Review → Fix
16. Lesson 2/Session 3 Preview：AI Weather Security Center

## Core Concepts

### AI Coding Agent
AI 不只是聊天工具，而可以讀 repo、規劃、修改 code、執行測試與產生文件。但 AI 的 output 必須由人驗證。

### GitHub as Engineering Memory
GitHub 保存：requirements、architecture、source code、tests、findings、patches、reports、evidence。後續 Red Team / Blue Team 都回到同一個 repo。

### Authorization Boundary

```text
Public Internet ≠ Authorized Target
Owned Code ≠ Unlimited Permission on Third-party Infrastructure
```

Offensive Lab 僅在明確授權環境中執行。

## Required Practical Lab
學生使用 AI / Antigravity 建立一個最小 Python Security Utility，例如：
- HTTP security-header checker
- log parser
- simple input validator

重點不是工具多強，而是完整走一次 AI-assisted workflow。

## Antigravity YAML Prompt Template

```yaml
task:
  id: lesson1-security-tool-001
  title: Build a minimal Python security utility
  role: senior_python_security_engineer

context:
  course: AI x Cybersecurity
  purpose: learn AI-assisted engineering workflow
  language: Python

learning_objectives:
  - turn a prompt into explicit requirements
  - inspect AI-generated code before execution
  - test expected and unexpected inputs
  - record evidence in GitHub

requirements:
  - keep the tool small and readable
  - accept only instructor-approved input
  - print structured results
  - handle errors safely

implementation_workflow:
  - state assumptions
  - propose a minimal plan
  - implement only necessary files
  - add tests
  - run tests
  - review for security issues
  - summarize files changed

constraints:
  - do not scan or attack unauthorized targets
  - do not add destructive behavior
  - prefer minimal dependencies

final_report:
  include:
    - assumptions
    - files_changed
    - tests_run
    - test_results
    - security_notes
    - unresolved_risks
```

## Core Message

> 不要只是叫 AI 寫程式；要學會讓 AI 做出可以理解、驗證、測試、追蹤，而且符合安全邊界的程式。