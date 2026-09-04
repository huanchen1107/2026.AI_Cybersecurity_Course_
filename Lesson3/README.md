# Lesson 3 — AI Red Team：Kali Linux 攻擊自己的系統

## Goal
把 Lesson 2 的 Weather Security Center 當作受控靶機，只在自有、授權、隔離 Lab / VM / Container 進行紅隊測試。

## Main Topics
1. Red Team / Blue Team / Purple Team
2. Kali Linux 與隔離 Lab
3. Attack Surface 與 Recon
4. Ping / Mass Scan（概念）
5. Nmap：服務與版本辨識
6. OSINT：只針對合法公開資訊與課堂目標
7. Shodan 與 CVE 判讀（以公開案例 / Lab 為主）
8. CVE 資料庫自動比對
9. Directory Discovery：Dirb / Gobuster / FFUF（僅 Lab）
10. SQLMap（僅自建 vulnerable endpoint / CTF）
11. Hashcat：密碼雜湊與防禦概念（使用課堂測試 hash）
12. Metasploit：框架概念與受控靶機示範
13. Evidence Collection：不要只說「打到了」，要留證據
14. AI 輔助：解釋掃描結果、CVE、優先級，但不得自動擴權到未授權目標

## Lab Flow

```text
Scope Definition
   ↓
Recon
   ↓
Service Enumeration
   ↓
Vulnerability Hypothesis
   ↓
Controlled Validation
   ↓
Evidence
   ↓
Risk Rating
   ↓
Handoff to Lesson 4
```

## Deliverable
每組輸出一份紅隊報告：
- Scope
- Asset
- Finding
- Evidence
- Impact
- Severity
- Reproduction in Lab
- Recommended Fix

## Safety Boundary
所有 offensive exercise 僅限：
- localhost
- 自有 VM
- 教師指定靶機
- CTF / deliberately vulnerable app
- 明確授權環境

禁止對未授權網路、網站、帳號或第三方系統進行掃描、利用、憑證嘗試或破壞性操作。
