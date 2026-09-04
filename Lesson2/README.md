# Lesson 2 — Vibe Coding 智慧天氣 IoT Dashboard

## Learning Goal
用 AI 協助學生從零建立 PHP + MySQL 智慧天氣系統，加入登入、Secure Coding、AI Weather Analyst、Machine Learning / Deep Learning 延伸，最後完成 Threat Modeling，作為 Lesson 3 紅隊 Lab 的目標系統。

## Course Flow

```text
VIBE CODE → DATA → DATABASE → WEB → LOGIN → SECURE → AI → ML/DL → THREAT MODEL
```

## Part 1–7：Build the Application

1. Mission：建立 AI Weather Security Center
2. Vibe Coding：從壞 Prompt 到結構化 Prompt
3. System Design：Weather API / Sensor → PHP → MySQL → Dashboard
4. Weather Data：Mock Sensor → API → 未來 IoT Sensor
5. PHP + MySQL：CONNECT / INSERT / SELECT
6. Dashboard：即時與歷史資料顯示
7. Authentication：Admin Login 與 Authentication 基礎

## Part 8：Password Security

核心：網站不應保存或知道使用者原始密碼。

- Plaintext password ❌
- MD5 / SHA1 ❌
- 單純 SHA256 不適合作為密碼儲存方案 ❌
- `password_hash()` / `password_verify()` ✅
- Password Hashing、Salt、Password-specific hashing

```php
$hash = password_hash($password, PASSWORD_DEFAULT);

if (password_verify($password, $user['password_hash'])) {
    // authenticated
}
```

核心句：**Hash, don’t encrypt passwords.**

## Part 9：Session Security

核心：Password 保護登入；Session 保護登入之後的身份。

- HTTP stateless
- Session ID
- `session_regenerate_id(true)`
- HttpOnly
- Secure on HTTPS
- SameSite
- Session timeout
- Proper logout
- Authentication vs Authorization

```php
session_regenerate_id(true);
$_SESSION['user_id'] = $user['id'];
$_SESSION['role'] = $user['role'];
```

## Part 10：SQL Injection

核心：**Never let untrusted data become SQL code.**

不安全：

```php
$sql = "SELECT * FROM users WHERE username='$username'";
```

安全方向：

```php
$stmt = $pdo->prepare(
    "SELECT * FROM users WHERE username = ?"
);
$stmt->execute([$username]);
```

概念：

```text
SQL Injection
Data → SQL Code
```

並補充 Input Validation、Whitelist、Least Privilege、Safe Error Handling。

## Part 11：XSS

核心：**不要讓不可信資料變成 Browser Code。**

```php
echo htmlspecialchars(
    $weather['note'],
    ENT_QUOTES,
    'UTF-8'
);
```

類型：
- Stored XSS
- Reflected XSS
- DOM-based XSS（概念）

重要觀念：
- Stored in DB ≠ Trusted
- API Data ≠ Trusted
- AI Output ≠ Trusted
- Output Encoding 必須考慮 Context

```text
XSS
Data → Browser Code
```

## Part 12：CSRF

核心：攻擊者利用已登入 Browser 的身份，誘導其送出使用者原本不想做的 request。

```php
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
```

驗證：

```php
if (!hash_equals(
    $_SESSION['csrf_token'],
    $_POST['csrf_token'] ?? ''
)) {
    http_response_code(403);
    exit;
}
```

核心：

```text
CSRF
Trusted Browser → Unwanted Action
```

Defense in Depth：CSRF Token + SameSite + correct HTTP method。

## Part 13：Access Control / Authorization

核心：

> Authentication：你是誰？
> Authorization：你可以做什麼？

Weather roles：
- viewer
- operator
- admin

觀念：
- Server-side authorization
- RBAC
- Horizontal privilege escalation
- Vertical privilege escalation
- IDOR / object-level authorization
- Least Privilege
- Default Deny
- UI hidden ≠ secure

完整 request pipeline：

```text
HTTP Request
    ↓
Authentication
    ↓
Authorization
    ↓
CSRF Check
    ↓
Input Validation
    ↓
Business Logic
    ↓
Prepared Statement
    ↓
Database
    ↓
Output Encoding
    ↓
Browser
```

## Part 14：AI Weather Analyst

AI 功能：
- Summary
- Risk Level
- Anomaly
- Recommendation

```text
Weather Data
     ↓
Aggregation / Feature Preparation
     ↓
Prompt Template
     ↓
LLM API
     ↓
Structured JSON
     ↓
Schema Validation
     ↓
Output Encoding
     ↓
Dashboard
```

### Structured Output Example

```json
{
  "summary": "High humidity with rising temperature.",
  "risk_level": "MEDIUM",
  "anomaly": "Temperature increased rapidly in the afternoon.",
  "recommendation": "Monitor for afternoon thunderstorms."
}
```

### AI Security

- Prompt Injection
- API Key management
- Data minimization
- LLM output validation
- Cost abuse / rate limiting
- Hallucination
- Fallback / graceful degradation
- Human-in-the-loop

核心：

> AI Input is untrusted.
> AI Output is untrusted.
> AI should not automatically become authority.

## Part 15：Machine Learning / Deep Learning Extension

### 為什麼 Part 15 必須保留
Lecture 2 到 Part 14 還沒有完整結束。Part 15 用來讓學生理解：**LLM 只是 AI 的一部分；同一份天氣資料可以直接變成傳統 ML / DL 教材。**

### 15.1 同一份資料，五種 AI 問題

`weather_data`：
- temperature
- humidity
- rainfall
- wind_speed
- pressure
- timestamp

可以轉成：

```text
Regression
→ 預測下一小時溫度

Classification
→ 預測 Rain / No Rain

Clustering
→ 找出天氣型態

Anomaly Detection
→ 找 Sensor 異常

Deep Learning
→ 學習時間序列長期模式
```

### 15.2 Regression

問題：
> 根據前幾個小時溫度、濕度、氣壓與風速，預測下一小時溫度。

```text
X = temp(t), humidity(t), pressure(t), wind(t)
y = temp(t+1)
```

可用模型：
- Linear Regression
- Random Forest Regressor
- Gradient Boosting

重點不是追求最高準確率，而是讓學生理解 supervised learning。

### 15.3 Classification

問題：
> 未來一小時會不會下雨？

```text
Label:
0 = No Rain
1 = Rain
```

可用：
- Logistic Regression
- Decision Tree
- Random Forest

教學指標：
- Accuracy
- Precision
- Recall
- Confusion Matrix

資安連結：**只看 Accuracy 可能會被誤導，偵測問題通常更重視漏報與誤報成本。**

### 15.4 Clustering

沒有標籤也可以做 AI。

```text
Hot + Humid
Cool + Dry
Rainy + Windy
Stable
```

可用 K-Means 作為入門，讓學生理解 Unsupervised Learning。

### 15.5 Anomaly Detection

這是最適合銜接 Cybersecurity 的 ML 題目。

正常 Sensor：

```text
30.1 → 30.2 → 30.5 → 30.3
```

異常：

```text
30.3 → 30.4 → 95.0
```

可能原因：
- Sensor failure
- Data corruption
- Network problem
- Malicious manipulation

可先用 Rule-based，再比較：
- Z-score
- Isolation Forest
- One-Class SVM（進階）

核心橋接：

```text
Weather anomaly detection
        ↓
Security anomaly detection
        ↓
Login anomaly
Network anomaly
Behavior anomaly
```

### 15.6 Deep Learning

當資料有時間關係，可以介紹：

```text
Past Sequence
    ↓
Neural Network
    ↓
Future Prediction
```

概念模型：
- MLP
- 1D CNN
- LSTM / GRU
- Transformer / Time-series model（概念）

本課不要求完整訓練大型模型；目標是理解 DL 和 LLM 的關係。

### 15.7 ML Pipeline

```text
Collect
  ↓
Clean
  ↓
Feature Engineering
  ↓
Train / Validation Split
  ↓
Train Model
  ↓
Evaluate
  ↓
Deploy
  ↓
Monitor
```

### 15.8 ML 本身也有 Security 問題

第一次埋下 Adversarial ML 的種子：
- Poisoned training data
- Data drift
- Malicious sensor values
- Model evasion
- Model output over-trust

學生要開始理解：

> AI Model 也是系統資產，也是攻擊面。

### 15.9 Mini Lab

基礎版：
1. 從 MySQL export weather CSV
2. 用 Python / pandas 讀取
3. 建一個簡單 Regression 或 Classification model
4. 顯示預測結果

進階版：
1. 建立 anomaly detector
2. 故意加入一筆極端 Sensor 值
3. 觀察是否被偵測
4. 討論 false positive / false negative

### 15.10 Part 15 核心句

> **LLM can explain the weather. ML can learn patterns from the weather. Security must protect both.**

## Part 16：Threat Modeling — Lesson 2 Final Integration

Lesson 2 到這裡才正式完成。

讓學生畫：

```text
Internet
   ↓
Weather API
   ↓
PHP Web App
 ┌────┼────────┐
 ↓    ↓        ↓
Login MySQL   AI API
 ↓             ↓
Session       Model
```

找出 Attack Surface：
- Login
- Password
- Session
- Form Input
- SQL
- Browser Output
- CSRF
- Authorization
- Weather API
- API Key
- Dependency
- Server
- AI Prompt
- AI Output
- ML Data
- ML Model

### Final Question

> **BUT... IS IT SECURE?**

不是用「我們已經安全」結尾，而是把系統交給下一課。

```text
NEXT MISSION
LESSON 3
AI RED TEAM + KALI LINUX
ATTACK YOUR OWN APPLICATION
```

## Lesson 2 Final Learning Outcome

學生完成的不是單純 PHP 網站，而是一個小型 AI Secure Software Engineering 系統：

```text
BUILD
  ↓
SECURE
  ↓
ADD AI
  ↓
ADD ML/DL
  ↓
MODEL THE THREATS
```

並準備在 Lesson 3 只針對自有 / 授權 / 隔離 Lab 進行紅隊測試。
