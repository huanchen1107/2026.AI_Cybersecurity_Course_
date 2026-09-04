# 第二課：Vibe Coding 智慧天氣 IoT Dashboard

**日期：2026-09-04**  
**Planning Source：ChatGPT**  
**Course：2026 AI × Cybersecurity Course**

> PHP + MySQL + AI + Cybersecurity。這是五課課程的核心專案：第 2 課建系統，第 3 課攻擊，第 4 課修補，第 5 課做 ISO27001 風險治理。

## 1. 課程定位

學生用 AI 協助開發一個簡單但完整的 Web App：

- 從 Weather API 或假感測器取得天氣資料
- 寫入 MySQL
- Dashboard 顯示最新資料與歷史資料
- 加入管理員登入
- 加入 AI 天氣摘要與異常判斷
- 加入基本資安防護：Password Hashing、Prepared Statements、XSS、CSRF、Session Security

核心問題：

> **AI 寫出來的程式，真的安全嗎？**

## 2. 建議時數

- **3 小時**：老師 Demo + 學生跟做基礎版
- **6 小時**：完整 Lab + 資安修補
- **9 小時**：加入 AI API、簡易 ML、展示與報告

## 3. 學習目標

學生能理解：

1. Vibe Coding 不是亂叫 AI 寫程式，而是清楚描述需求、限制、安全規則與測試條件。
2. PHP + MySQL 可以快速建立資料收集與展示系統。
3. API、登入、Session、資料庫、輸入輸出都是攻擊面。
4. AI 可以幫助開發，也可能產生不安全程式。
5. 資安功能不能只說「請加上資安功能」，而要具體列出防護項目。

學生能做到：

- 用 Prompt 產生 Web App 初版架構
- 建立 MySQL 資料表
- 用 PDO 連接 MySQL
- 用 Prepared Statements 避免 SQL Injection
- 用 `htmlspecialchars()` 避免 XSS
- 用 `password_hash()` / `password_verify()` 管理密碼
- 用 CSRF Token 保護表單
- 用 Session 管理登入狀態
- 用 AI 對天氣資料做摘要、異常判斷與建議

## 4. 課程故事線

```text
想做智慧天氣站
  ↓
用 AI 產生 PHP + MySQL 初版
  ↓
系統能動，但不一定安全
  ↓
加入登入與管理功能
  ↓
發現 SQL Injection / XSS / CSRF / Session 問題
  ↓
用 AI Review，但由人類判斷與修正
  ↓
加入 AI 天氣摘要與異常判斷
  ↓
最後問：如果你是駭客，會從哪裡攻擊？
  ↓
銜接第三課：Kali Linux 紅隊測試
```

## 5. 系統架構

```text
Weather API / Fake Sensor
        ↓
fetch_weather.php
        ↓
MySQL: weather_data
        ↓
index.php Dashboard
        ↓
ai_summary.php
        ↓
AI Analysis
```

管理功能：

```text
login.php
   ↓
password_verify()
   ↓
Session
   ↓
admin.php
```

攻擊面：

```text
Login
Input Form
Database Query
Output Page
Session Cookie
API Key
Dependency
Server Config
AI Prompt
```

## 6. 專案目錄建議

```text
weather-iot-dashboard/
├── config.php
├── db.php
├── index.php
├── login.php
├── logout.php
├── admin.php
├── fetch_weather.php
├── ai_summary.php
├── csrf.php
├── style.css
└── database.sql
```

## 7. 資料表設計

### weather_data

```sql
CREATE TABLE weather_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  city VARCHAR(100) NOT NULL,
  temperature DECIMAL(5,2) NOT NULL,
  humidity INT NOT NULL,
  rainfall DECIMAL(5,2) NOT NULL,
  wind_speed DECIMAL(5,2) NOT NULL,
  pressure DECIMAL(7,2) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### users

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) NOT NULL DEFAULT 'admin',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 8. Vibe Coding 主 Prompt

```text
你是一位 PHP Web Developer 與 Security Reviewer。
請建立一個 PHP 8 + MySQL 的智慧天氣 Dashboard。

功能包含：
- 取得天氣資料
- 寫入 MySQL
- 顯示 Dashboard
- 管理員登入
- AI 摘要

資安要求：
- Prepared Statements
- password_hash / password_verify
- htmlspecialchars output encoding
- CSRF Token
- Session Security

程式保持簡單，適合初學者閱讀。

請先提出 implementation plan、專案目錄與資料表設計，
不要立刻寫完整程式。
```

核心 Vibe Coding 循環：

```text
Prompt
  ↓
Plan
  ↓
Small Code
  ↓
Run
  ↓
Test / Error
  ↓
Fix
  ↓
Security Review
```

## 9. 投影片 Storyboard：45 張

### Part A — 開場與任務設定

1. 本課標題：Vibe Coding 智慧天氣站
2. 今天要完成什麼：Weather Data → PHP → MySQL → Dashboard → AI → Security
3. 最後成果預覽：AI Weather Security Center
4. 為什麼選天氣站：資料、Dashboard、登入、AI、資安攻擊面
5. 核心問題：AI 寫出來的程式，真的安全嗎？

### Part B — Vibe Coding 方法

6. 傳統 Coding vs Vibe Coding
7. 壞 Prompt：`幫我做一個天氣網站`
8. 好 Prompt：Role / Goal / Stack / Features / Security / Constraints / Test
9. 本課主 Prompt
10. Vibe Coding 工作循環：Prompt → Plan → Small Code → Run → Fix → Review

### Part C — 系統架構與資料庫

11. 系統架構圖
12. 專案目錄
13. `weather_data` 資料表
14. `users` 資料表
15. MySQL 建表 Demo

### Part D — PHP 取得資料並寫入 MySQL

16. 資料來源：Weather API / Fake Sensor / CSV
17. 假感測器資料
18. PDO 資料庫連線
19. Prepared Statements 寫入天氣資料
20. Demo：資料進入 MySQL

假感測器可以先使用：

```php
$temperature = rand(240, 340) / 10;
$humidity = rand(50, 90);
$rainfall = rand(0, 20) / 10;
```

寫入資料：

```php
$stmt = $pdo->prepare(
    "INSERT INTO weather_data
     (city, temperature, humidity, rainfall, wind_speed, pressure)
     VALUES (?, ?, ?, ?, ?, ?)"
);
$stmt->execute([$city, $temperature, $humidity, $rainfall, $wind, $pressure]);
```

### Part E — Dashboard 顯示

21. Dashboard 顯示項目
22. 讀取最新資料
23. 顯示資料時的 XSS 風險
24. 用 `htmlspecialchars()` 安全輸出
25. Demo：Dashboard 完成

安全輸出範例：

```php
echo htmlspecialchars($latest['city'], ENT_QUOTES, 'UTF-8');
```

### Part F — 登入與密碼安全

26. 為什麼需要登入
27. 錯誤密碼儲存：明文密碼
28. 正確密碼儲存：`password_hash()`
29. 登入驗證：`password_verify()`
30. Session 基本安全：HttpOnly / SameSite / regenerate_id

```php
$hash = password_hash($password, PASSWORD_DEFAULT);
```

```php
if (password_verify($password, $user['password_hash'])) {
    session_regenerate_id(true);
    $_SESSION['user_id'] = $user['id'];
    $_SESSION['role'] = $user['role'];
}
```

### Part G — 三個重要資安實驗

31. AI 說「已加上資安功能」就夠了嗎？
32. SQL Injection 是什麼
33. Prepared Statements 修法
34. XSS 是什麼
35. Output Encoding 修法
36. CSRF 是什麼
37. CSRF Token 修法

錯誤 SQL 示範：

```php
$sql = "SELECT * FROM users WHERE username = '$username'";
```

安全版本：

```php
$stmt = $pdo->prepare(
    "SELECT * FROM users WHERE username = ?"
);
$stmt->execute([$username]);
```

CSRF Token：

```php
$_SESSION['csrf_token'] = bin2hex(random_bytes(32));
```

驗證：

```php
hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])
```

### Part H — 加入 AI 分析

38. AI 可以幫天氣站做什麼
39. AI 分析 Prompt
40. AI 輸出 JSON 格式
41. ML / DL 延伸

AI 分析可以包含：

- 摘要最近 24 小時天氣
- 判斷風險等級
- 偵測異常資料
- 提供生活建議
- 產生管理報告

Prompt：

```text
你是一位天氣資料分析助理。
請根據最近 24 小時的 temperature、humidity、rainfall、wind_speed 資料，輸出：

1. 一句摘要
2. 風險等級：Low / Medium / High
3. 是否有異常值
4. 給一般使用者的建議

只能根據提供的資料分析，不要編造資料。
請輸出 JSON。
```

輸出範例：

```json
{
  "summary": "過去 24 小時溫度偏高且濕度上升。",
  "risk_level": "Medium",
  "anomaly": false,
  "recommendation": "外出請補充水分，午後留意降雨。"
}
```

### ML / DL 延伸

同一份 `weather_data` 可以繼續教：

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
→ 學習較複雜的時間序列模式
```

讓學生理解：**LLM 只是 AI 的一種，不是所有 AI。**

### Part I — 總結與銜接第三課

42. 今天完成了什麼
43. `BUT... IS IT SECURE?`
44. 攻擊面地圖
45. 下一課任務：Kali Linux 紅隊測試

## 10. Demo 流程

### Demo 1 — AI 產生專案計畫

要求 AI 先產生 implementation plan，不直接產生完整系統。

全班觀察：

- 有沒有資料庫？
- 有沒有安全需求？
- 有沒有目錄結構？
- 有沒有錯誤處理？
- 有沒有測試方法？

### Demo 2 — 建立 MySQL

1. 啟動 XAMPP Apache / MySQL
2. 開啟 phpMyAdmin
3. 建立 `weather_lab`
4. 匯入 `database.sql`
5. 檢查 `weather_data` 與 `users`

### Demo 3 — 產生假天氣資料

1. 執行 `fetch_weather.php`
2. 檢查資料是否寫入
3. 重複執行至少 10 次
4. 到 phpMyAdmin 看歷史資料

### Demo 4 — Dashboard

1. 讀取最新資料
2. 顯示 Temperature / Humidity / Rainfall / Wind
3. 顯示最近 10 筆資料
4. 加入簡單 CSS

### Demo 5 — Login

1. 建立 admin 帳號
2. 密碼轉成 hash
3. 登入成功進入 `admin.php`
4. 登出後不能進入 admin page

### Demo 6 — Security Review

依序檢查：

1. Prepared Statements
2. `htmlspecialchars()`
3. Password Hashing
4. CSRF Token
5. Session Cookie Settings
6. `session_regenerate_id(true)`

### Demo 7 — AI Weather Analysis

1. 從資料庫取最近資料
2. 整理成 JSON
3. 給 AI 產生摘要
4. Dashboard 顯示 AI 分析結果

## 11. 學生 Lab

### Lab A — 基礎版

- 建立 MySQL Database
- 寫入至少 10 筆天氣資料
- 顯示最新天氣
- 顯示最近 10 筆歷史資料

### Lab B — Security Version

- Login Page
- `password_hash()`
- Prepared Statements
- `htmlspecialchars()`
- CSRF Token
- Session Security

### Lab C — AI Version

- 將最近資料整理成 AI Prompt
- 產生天氣摘要
- 產生風險等級
- 顯示 AI 建議

### Lab D — Advanced Challenge

- 串接真實 Weather API
- 加入折線圖
- 加入異常偵測
- 加入 API Key 管理
- 加入 Security Check Report

## 12. 老師教學重點

### 不要讓 AI 一次寫完整系統

```text
先規劃
→ 建資料庫
→ DB 連線
→ 資料寫入
→ Dashboard
→ Login
→ Security Review
→ AI Analysis
```

### 資安需求必須具體

不要只說：

```text
請加上資安功能。
```

要說：

```text
請加入：
- password_hash / password_verify
- PDO prepared statements
- htmlspecialchars output encoding
- CSRF token
- session_regenerate_id
- HttpOnly / SameSite Cookie
```

### AI Code Review 檢查清單

- 有沒有 SQL Injection？
- 有沒有 XSS？
- 密碼是否明文儲存？
- Session 是否安全？
- API Key 是否寫死在程式碼？
- 錯誤訊息是否洩漏系統資訊？
- 使用者是否能存取不該存取的頁面？

## 13. 評量

學生提交：

1. GitHub 專案
2. Dashboard 截圖
3. Database 截圖
4. Security Checklist
5. AI Analysis 截圖
6. 300 字心得：AI 幫了什麼？AI 有什麼風險？

| 項目 | 配分 |
|---|---:|
| 功能完成度 | 30 |
| 資安修補 | 30 |
| AI 應用 | 20 |
| 程式可讀性 | 10 |
| 展示說明 | 10 |

## 14. 給 AI Coding Agent 的實作 Prompt

```text
你是一位課程助教與 PHP 資安工程師。
請建立適合教學使用的 PHP 8 + MySQL 專案。

Project: weather-iot-dashboard

目標：建立智慧天氣 IoT Dashboard。

必要功能：
1. MySQL 儲存 weather_data。
2. users 資料表儲存管理員帳號。
3. PDO 連線資料庫。
4. 所有 SQL 使用 Prepared Statements。
5. 密碼使用 password_hash / password_verify。
6. 所有 HTML 輸出使用 htmlspecialchars。
7. POST 表單加入 CSRF Token。
8. 登入後使用 session_regenerate_id(true)。
9. Dashboard 顯示最新資料與最近 10 筆資料。
10. 第一版先用假天氣資料，不依賴外部 API。
11. 程式保持簡單，適合初學者閱讀。

第一階段只輸出：
- Project Tree
- database.sql 設計
- 每個檔案用途
- Implementation Plan
- Test Plan
- Security Checklist

不要一次輸出所有程式碼。
等確認 architecture 後，再逐檔案實作。
```

## 15. 與後續課程的共同專案關係

```text
LESSON 02
BUILD
Vibe Coding + PHP + MySQL + AI
        ↓
LESSON 03
ATTACK
Kali Linux + Red Team
        ↓
LESSON 04
DEFEND
OWASP + Secure Coding + AI Review
        ↓
LESSON 05
GOVERN
ISO27001 + Risk Assessment + AI Report
```

### 第 3 課直接測試本課系統

- Nmap：找服務
- Gobuster / FUZZ：找 Web attack surface
- SQLMap：在隔離的教學環境驗證 SQL Injection
- XSS 測試
- Authentication / Session 測試
- CVE 與 Dependency 檢查

所有攻擊實驗限定於**本課自己建立、明確授權的隔離 Lab 環境**。

### 第 4 課再修補同一系統

將問題映射到 OWASP / CWE，例如：

- Broken Access Control
- Security Misconfiguration
- Injection
- Authentication Failures
- Software / Data Integrity
- Logging and Alerting

### 第 5 課把同一系統提升為企業案例

- Asset Inventory
- Risk Assessment
- Access Control
- Technical Controls
- Incident Logging
- AI-assisted Security Report

---

## 核心教學口訣

> **BUILD → ATTACK → DEFEND → GOVERN**

以及 Vibe Coding 的工程原則：

> **AI generates. Human verifies. Security validates.**

AI 可以幫我們快速建立程式；但是否正確、是否安全、是否值得部署，仍需要工程師驗證。