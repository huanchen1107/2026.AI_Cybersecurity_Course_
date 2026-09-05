# Lesson 12 — AI Red Team II：Prove it in Our Weather Cyber Range

## Mission
把 Lesson 11 在授權訓練場學到的方法，移轉到自己的 Local Weather Cyber Range，形成可修補的 findings。

## Concept
Knowledge Transfer、Controlled Validation、Finding、Root Cause Hypothesis、Impact、Severity、Evidence。

## Lab Scope
只使用 localhost / Docker / VM 的教師控制 Lab。Production/Vercel 不作 exploitation target。

建議 Lab：
- Authentication
- Broken Access Control / RBAC
- Injection
- XSS / output handling
- Session security
- Logging / detection

## Practical Flow
```text
TryHackMe — Learn
      ↓
Weather Cyber Range — Transfer
      ↓
Discover → Hypothesis → Controlled Validation → Evidence → Finding
```

## Antigravity YAML Prompt
```yaml
task:
  id: lesson12-weather-cyber-range
  title: Prepare controlled Weather Cyber Range validation labs
  role: secure_cyber_range_engineer
context:
  project: AI Weather Security Center
  environment: local_docker_vm_only
learning_objectives:
  - transfer security concepts from training range to own code
  - produce evidence-based findings
requirements:
  - inspect repository
  - keep vulnerable lab components isolated from production build
  - provide teacher-controlled lab scenarios for access control input handling session and logging
  - provide reset instructions
  - provide expected evidence format
security_requirements:
  - vulnerable routes must not ship in public production build
  - bind lab services to safe local interfaces by default
  - no destructive exercises
  - document scope prominently
implementation_workflow:
  - inspect architecture
  - design isolated lab components
  - implement minimal controlled scenarios
  - add reset scripts
  - add safety checks
  - add tests proving production excludes lab routes
tests:
  - lab starts locally
  - reset restores known state
  - production profile excludes vulnerable lab endpoints
deliverables:
  - cyber-range configuration
  - teacher lab guide
  - student finding template
  - safety tests
final_report:
  include: [lab_components, isolation_controls, tests_run, known_risks]
```

## Evidence
每個 Finding：Scope、Asset、Observation、Evidence、Impact、Severity、Root Cause Hypothesis、Recommended Fix。

## Reflection
你是在證明一個漏洞，還是在證明一個假設？兩者需要什麼不同證據？