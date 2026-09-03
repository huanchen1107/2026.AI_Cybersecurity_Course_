# 2026 AI × Cybersecurity × Vibe Coding 五課課程規劃

- Planning Date: 2026-09-03
- Planning Source: ChatGPT
- Repository: `huanchen1107/2026.AI_Cybersecurity_Course_`
- Folder: `_myplan_`
- Course Theme: Artificial Intelligence × Vibe Coding × Cybersecurity
- Design Goal: 將原書五章重新設計成一條具有故事性、實作性與資安思維的完整課程鏈。

---

## 一、整體課程核心概念

不採用單純「工具 → PHP → Kali → OWASP → ISO」逐章照講，而是改造成一條學生可以一路完成作品的專案式學習路徑：

> **BUILD → THINK → ATTACK → DEFEND → GOVERN**

也就是：

1. 用 AI 與 Vibe Coding 建立系統
2. 讓系統具備資料與 AI 能力
3. 從紅隊角度攻擊自己的系統
4. 從藍隊角度修補與強化
5. 從企業治理角度完成風險與 ISO 27001 管理

整個五課共用同一個核心專案，避免每課變成零散的小練習。

建議核心專案：

> **AI Smart Weather Security Center — 智慧天氣 IoT / Web 資安平台**

學生最終會擁有一個可展示的 Portfolio Project。

---

# 二、五課總覽

| 課次 | 主題 | 主要成果 | AI / Vibe Coding | 資安核心 |
|---|---|---|---|---|
| 第1課 | AI 資安工程師的工具箱 | 完成開發環境、GitHub 與 AI Coding Workflow | Prompt、ChatGPT / Claude / Gemini / Copilot、Coding Agent | Secret、Dependency、版本控制、AI Code Risk |
| 第2課 | Vibe Coding：智慧天氣站 | PHP + MySQL Weather Dashboard | AI 產生程式、資料分析、異常判斷 | Login、bcrypt、SQL Injection、XSS、CSRF、Session |
| 第3課 | AI 紅隊：Attack Your Own System | 使用 Kali 對自己的系統進行合法實驗室測試 | AI 協助解析掃描結果 | Nmap、OSINT、CVE、Gobuster、SQLMap、Attack Surface |
| 第4課 | AI 藍隊：OWASP Secure Coding | 修補第2、3課找到的問題 | AI Code Review、AI Fix、Secure Prompt | OWASP Top 10、CWE、Dependency、Supply Chain |
| 第5課 | AI 資安長：ISO 27001 與治理 | Security Assessment / Risk Report | AI Risk Assessment、Report Generation | ISO27001、風險、控制措施、政策、治理 |

---

# 三、第1課：AI 資安工程師的工具箱

## 課程定位

第一課只需建立共同基礎，不需要過度深入各工具。

## 建議投影片數

15–20 張。

## 建議綱要

1. 什麼是 Vibe Coding？
2. 傳統 Coding vs Vibe Coding
3. ChatGPT / Claude / Gemini / GitHub Copilot 能做什麼
4. AI Coding Agent 是什麼
5. Prompt 基本結構
6. 為什麼「明確需求」比「請幫我寫程式」重要
7. Visual Studio Code
8. Git / GitHub
9. PHP / MySQL / MariaDB
10. XAMPP / Laragon
11. phpMyAdmin
12. Kali Linux
13. VMware
14. GitHub Dependency Graph
15. AI 寫出的程式為什麼可能不安全
16. 開發循環：Prompt → Code → Run → Test → Review → Fix
17. 第2課智慧天氣站專案預告

## 核心觀念

> 不只是叫 AI 寫程式，而是要學會讓 AI 產生「可以驗證、可以測試，而且安全」的程式。

---

# 四、第2課：Vibe Coding 智慧天氣站

## 課程定位

這一課是整門課的核心 BUILD 專案。

主題：

> **AI Smart Weather Security Center**

技術保持簡單，重點不是背 PHP，而是理解完整 Web System、AI Workflow 與 Security by Design。

## 建議成果畫面

```text
┌──────────────────────────────────────────┐
│     🌤️ Taichung Smart Weather           │
│                                          │
│ Temperature       31.2°C                 │
│ Humidity          72%                    │
│ Rain              0 mm                   │
│ Wind              3.4 m/s                │
│                                          │
│ AI Analysis                              │
│ ⚠ 高溫、高濕，午後降雨機率增加           │
│                                          │
│ Historical Data                          │
│  ──────── temperature chart ───────      │
│                                          │
│ 🔐 Login     📊 History     🤖 AI        │
└──────────────────────────────────────────┘
```

---

## 2.1 第一階段：先看成果，不先教語法

老師先展示完成版 Dashboard。

開場問題：

> 「如果今天完全不會 PHP，你覺得能不能在 AI 的幫助下做出來？」

藉此帶入 Vibe Coding。

---

## 2.2 第二階段：取得真實天氣資料

教學上可以介紹爬蟲概念，但實作建議優先使用公開 Weather API，因為結構較穩定，也能順勢帶入 API Security。

```text
Internet
   ↓
Weather API
   ↓
PHP Collector
   ↓
MySQL
   ↓
Dashboard
   ↓
AI Analysis
```

可介紹：

- HTTP Request
- JSON
- API Key
- Public API
- Rate Limit
- API 也是攻擊面

若希望加入爬蟲，可額外安排一個簡單公開頁面資料抓取 Demo，再與 API 比較。

---

## 2.3 第三階段：PHP + MySQL 最小必要知識

資料表可先採：

```text
weather_data

id
timestamp
temperature
humidity
rainfall
wind_speed
pressure
```

學生只需先理解：

```text
取得資料
   ↓
INSERT MySQL
   ↓
SELECT 顯示
```

PHP Syntax 不需要成為本課主角。

---

## 2.4 第四階段：第一次真正的 Vibe Coding

不要只輸入：

> 幫我做天氣網站。

而是教學生使用結構化 Prompt。

### Prompt 範例

```text
ROLE
你是一位 PHP Web Developer。

GOAL
建立智慧天氣監控網站。

STACK
PHP 8
MySQL
HTML/CSS/JavaScript

FEATURES
1. Weather API
2. 儲存 MySQL
3. Dashboard
4. Historical chart
5. Login

SECURITY
使用 prepared statements
密碼使用 password_hash
輸出必須 escape
Session 必須安全管理

CONSTRAINT
程式保持簡單，適合初學者閱讀。

先提出 implementation plan，
不要立刻寫全部程式。
```

此段同時教授：

- Prompt Engineering
- Requirement Engineering
- Software Engineering
- Security Engineering

---

## 2.5 第五階段：「請加上資安功能」實驗

直接呼應原書第 2.3 節。

給 AI 一個非常簡單的 Prompt：

> 「請幫我的網站加上資安功能。」

觀察 AI 自動提出哪些措施。

應引導學生辨識至少六項：

1. Password Hashing / bcrypt
2. SQL Injection → Prepared Statements
3. XSS → Input Validation + Output Encoding
4. CSRF Token
5. Session Security
6. Authentication / Authorization

課堂核心問題：

> **AI 說安全，就真的安全嗎？**

學生開始扮演 Security Reviewer。

---

## 2.6 第六階段：SQL Injection 小實驗

不安全寫法示意：

```php
$sql = "SELECT * FROM users WHERE username='$username'";
```

讓學生找問題，再請 AI Review。

安全改寫：

```php
$stmt = $pdo->prepare(
    "SELECT * FROM users WHERE username = ?"
);
$stmt->execute([$username]);
```

核心觀念：

> AI 可以製造漏洞，也可以協助找漏洞；人仍需要理解風險與驗證結果。

所有攻防實驗限於課堂自己建置、明確授權的 Lab Environment。

---

## 2.7 第七階段：XSS 小實驗

增加 Weather Note 或 Comment 欄位。

正常輸入：

```text
今天台中很熱
```

再展示含 HTML / Script 的惡意輸入在不安全輸出時可能造成的問題。

安全概念：

```php
htmlspecialchars()
```

建立資料流思維：

```text
Input → Database → Output → Browser
```

學生理解：

> 資料本身也可能成為攻擊載體。

---

## 2.8 第八階段：Password Hashing

比較：

```text
❌ Plain text password
❌ MD5(password)
❌ SHA256(password)
✅ password_hash()
```

引導問題：

> 為什麼資料庫管理員也不應該看到使用者原始密碼？

介紹：

- Hash
- Salt
- bcrypt / password_hash
- password_verify

---

## 2.9 第九階段：加入 AI Weather Analysis

將最近一段時間的天氣資料交由 AI 做摘要與異常判斷。

```text
最近24小時

Temperature
Humidity
Pressure
Rainfall
Wind
     ↓
    AI
     ↓
Weather Summary
Risk Level
Anomaly
Recommendation
```

Dashboard 可顯示：

```text
🤖 AI Weather Analysis

過去六小時溫度持續上升，
同時濕度維持 80% 以上。
系統判定目前屬於高溫高濕狀態。
```

延伸討論：

- AI API Key 如何保護？
- Prompt 內是否可以放敏感資料？
- AI 回覆是否一定正確？
- 如何驗證 AI Output？

---

## 2.10 第十階段：從 Generative AI 帶到 Machine Learning

提問：

> 一定要使用 LLM 才叫人工智慧嗎？

答案：不是。

同一份 `weather_data` 可延伸：

```text
Regression
→ 預測下一小時溫度

Classification
→ Rain / No Rain

Clustering
→ 天氣型態分群

Anomaly Detection
→ 感測器異常

Neural Network / Deep Learning
→ 複雜天氣模式
```

此處為後續 ML / DL 課程建立概念入口，不必在第2課深入數學。

---

## 2.11 第二課結尾：BUT... IS IT SECURE?

完成作品後，最後不要以「網站完成」作結，而是突然切換到資安視角。

```text
Internet
     │
     ▼
 Weather API
     │
     ▼
 PHP Web App ───── AI API
     │
     ▼
   MySQL
     ▲
     │
   Users
```

問學生：

> 「如果你現在是駭客，你會從哪裡進來？」

可能答案：

- Login
- API
- PHP
- Database
- Session
- Password
- AI Prompt
- Dependency
- Web Server

最後顯示下一課任務：

> **NEXT MISSION — Attack Your Own System**

---

# 五、第3課：AI 紅隊 — Attack Your Own System

## 故事定位

第2課完成系統後，第3課不換案例，直接攻擊自己建置、合法授權的 Lab System。

## 建議核心流程

```text
Target Definition
      ↓
Attack Surface
      ↓
Nmap
      ↓
OSINT
      ↓
CVE
      ↓
Directory Discovery
      ↓
Web Vulnerability Testing
      ↓
Evidence
      ↓
AI-assisted Analysis
```

## 可涵蓋內容

- Kali Linux
- Mass Scan / Ping 基本概念
- Nmap
- OSINT
- Shodan 概念
- CVE / CVSS
- Gobuster / Dirb / FUZZ 概念
- SQLMap：限自己 Lab 環境示範
- Hashcat：限合法 Password Lab
- Metasploit：以靶機 / Lab 為限

AI 的角色：

- 解讀 Nmap 結果
- 解釋 CVE
- 建立攻擊面摘要
- 幫助學生產生 Security Finding Report

強調 Ethics：

> **沒有明確授權的目標，不進行掃描、測試或攻擊。**

---

# 六、第4課：AI 藍隊 — OWASP Secure Coding

## 課程定位

第三課找到問題，第四課全部回到原始碼修補。

主軸：

```text
Attack Finding
      ↓
Reproduce
      ↓
Understand Root Cause
      ↓
Ask AI for Fix
      ↓
Human Review
      ↓
Test
      ↓
Regression Test
```

## OWASP 主題

依教材可帶：

- Broken Access Control
- Security Misconfiguration
- Software Supply Chain Failures
- Cryptographic Failures
- Injection
- Insecure Design
- Authentication Failures
- Software or Data Integrity Failures
- Security Logging and Alerting Failures
- Mishandling of Exceptional Conditions
- CWE Top 25

## AI 教學重點

不是只問：

> Fix this code.

而要教：

```text
1. Identify vulnerability
2. Explain root cause
3. Estimate impact
4. Propose minimal fix
5. Write security test
6. Review side effects
```

加入重要觀念：

> **AI-generated patch ≠ Secure patch**

必須有：

- Review
- Test
- Evidence

---

# 七、第5課：AI 資安長 — ISO27001 與治理

## 課程定位

前四課處理技術，第五課讓學生第一次站在企業 CISO / Security Manager 的角度思考。

學生面對同一個 Weather System，要回答：

- 我們有哪些 Asset？
- 哪些 Threat？
- 哪些 Vulnerability？
- Risk 多大？
- 哪些控制措施？
- 誰負責？
- 如何留下 Evidence？

## 對應教材

- 組織控制
- 人員控制
- 實體控制
- 技術控制
- ISO27001 控制項目

## AI 活動

將系統資訊提供給 AI：

```text
Assets
Threats
Vulnerabilities
Existing Controls
```

要求 AI 產生初步：

```text
Risk Register
     ↓
Control Recommendation
     ↓
Priority
     ↓
Evidence Needed
```

學生再進行人工 Review。

最後完成：

> **AI Smart Weather Security Assessment Report**

---

# 八、五課共同故事線

```text
第1課
工具與 AI Coding Workflow
        ↓
第2課
BUILD
智慧天氣 Web / IoT System
        ↓
第3課
ATTACK
Red Team 測試自己的系統
        ↓
第4課
DEFEND
OWASP + Secure Coding 修補
        ↓
第5課
GOVERN
ISO27001 + Risk Management
```

整門課最後可以濃縮成一句：

> **Build it with AI. Attack it safely. Defend it correctly. Govern it responsibly.**

---

# 九、建議投影片與教學素材策略

每一課建議不要只做文字型 PPT，而採固定結構：

1. Story / Mission Opening
2. Concept
3. Architecture Diagram
4. AI Prompt
5. Live Demo
6. Student Challenge
7. Security Question
8. Fix / Reflection
9. Knowledge Map
10. Next Mission

其中第2課可優先製作 40–50 張完整投影片，包含：

- 每張 Slide Title
- 畫面內容
- Teacher Notes
- Demo Steps
- Student Lab
- Prompt Examples
- PHP / MySQL Code
- Security Experiment
- AI / ML Extension

---

# 十、下一步規劃

目前優先順序：

1. 第1課先保留綱要，不展開細節。
2. 下一階段集中完成第2課。
3. 第2課先確認 Weather API / 爬蟲資料來源。
4. 定義最小 PHP + MySQL 專案結構。
5. 定義安全與不安全兩種版本，供第2–4課共用。
6. 完成第2課 40–50 張投影片 Storyboard。
7. 再製作講師逐頁講稿與學生 Lab Sheet。

---

## 設計原則

- AI 不是獨立的一章，而是每課都使用。
- Vibe Coding 不等於「叫 AI 隨便寫程式」。
- Security 必須從需求階段就加入。
- 攻防實驗只在自己建置或明確授權的 Lab 環境。
- 學生需要理解系統，不以背 PHP 語法為核心。
- 同一個專案貫穿 Build / Attack / Defend / Govern。
- AI Output 一律需要驗證，不把 AI 當成絕對正確答案。
- 最終成果應能成為學生 Portfolio。
