# AIIS_L1 — Slides 01–06 Teaching Script

Date: 2026-09-07
Status: Detailed teaching script
Parent plan: `_myplan_/2026-09-07-AIIS-L1-Weather-Security-Center-Detailed-Lecture-Plan.md`

Core messages:
- **WORKING ≠ SECURE**
- **AI BUILDS. HUMAN VERIFIES.**

---

## Slide 01 — Build Your First AI Weather Security Center

### Purpose
Open L1 with a build-first engineering challenge and establish the two lesson slogans.

### On-slide
**AIIS_L1**

# Build Your First AI Weather Security Center

從一段 Prompt，開始我們的 AI × Cybersecurity 工程旅程

**WORKING ≠ SECURE**

**AI BUILDS. HUMAN VERIFIES.**

### Visual composition
Center flow:

```text
PROMPT
   ↓
AI
   ↓
🌦 Weather Website
   ↓
🛡 Security
```

Background may contain a subtle Taiwan silhouette, weather layer and code elements. Keep the title dominant.

### 煥哥
- Expression: welcoming, confident smile; excited that the class will build something real.
- Pose: body slightly toward the central flow; one open hand presents `Prompt → Website`, other arm relaxed.
- Gaze: toward students.

### Teacher talk
上一堂我們認識了 AI 與資訊安全。今天開始不只是「聽」。今天我要做一件事情給大家看：我要用一段 Prompt，請 AI 幫我們建立一個真的氣象網站，而且不是假資料，我們會取得台灣中央氣象署的真實資料。

但是今天真正要學的不是「AI 好厲害」。真正的問題是：AI 幫我把網站寫出來，而且真的可以執行——這樣就代表它安全嗎？這就是今天整堂課要回答的問題。

### Interaction
Ask: 「AI 把程式做出來而且能執行，算不算完成？」

Do not resolve yet.

### Transition
「一段 Prompt，真的可以變成網站嗎？」

---

## Slide 02 — One Prompt → One Real Website

### Purpose
Create curiosity about coding agents and reverse the traditional learning sequence.

### On-slide
# ONE PROMPT → ONE REAL WEBSITE

```text
📝 Prompt
     ↓
🤖 Antigravity
     ↓
🌦 CWA Weather Data
     ↓
💻 Weather Website
```

**No copy-paste tutorial.**

**No 500-line coding demo.**

**We start from intent.**

### Visual composition
Four large connected blocks, left-to-right or top-to-bottom. Website thumbnail should be the most visually rewarding endpoint.

### 煥哥
- Expression: impressed / curious, like asking “真的可以？”
- Pose: left hand holds a Prompt card; right hand points to the completed weather-site mockup.
- Body: slight forward lean.
- Gaze: toward the website.

### Teacher talk
以前如果我說「今天做一個台灣氣象網站」，大家可能會先想到：Python 還不會、API 是什麼、JSON 是什麼、地圖怎麼畫、網站怎麼做？今天把順序倒過來。先描述我們要什麼，讓 AI Coding Agent 建立第一版，再回來研究它做了什麼、做得對不對、安不安全。

### Interaction
Ask students what they think one coding prompt can accomplish:
- only output code?
- create files?
- install packages?
- run?
- debug?
- produce a working site?

Do not reveal the answer yet.

### Transition
「先看看我們今天真正要做出的東西。」

---

## Slide 03 — What Are We Building?

### Purpose
Make the project concrete and establish the shared semester Lab.

### On-slide
# 我們今天到底要做什麼？

Mockup:

```text
┌─────────────────────────────────────────┐
│  🌦 AI WEATHER SECURITY CENTER          │
│                                         │
│  Date ▼  2026-09-07                     │
├───────────────────┬─────────────────────┤
│                   │ Northern     28°C   │
│      TAIWAN       │ Central      30°C   │
│                   │ Southern     32°C   │
│       🔵          │ Eastern      27°C   │
│        🟢         │                     │
│        🟡         │ Min / Max / Avg     │
│       🔴          │ Weather             │
│                   │                     │
└───────────────────┴─────────────────────┘
```

Feature labels:
- REAL DATA
- TAIWAN MAP
- DATE FILTER
- TEMPERATURE

### Visual composition
Website mockup on left/center; four large capability chips on right. Include a small semester continuity arrow below.

### 煥哥
- Expression: professional, confident.
- Pose: product-demo presentation gesture, open palm toward mockup.
- Gaze: toward the website.

### Teacher talk
我們不是要做 ChatGPT Hello World。今天要建立的是 AI Weather Security Center。第一版功能不複雜：真實氣象資料、台灣地圖、日期選擇、各區溫度。這個網站今天看起來只是一個氣象網站，但它會陪我們很多堂課。

Reveal:

```text
Today: Weather Website
       ↓
Later: Security Scan
       ↓
ML
       ↓
Red Team
       ↓
Blue Team
       ↓
Risk Management
```

所以今天不是做完一個作業就丟掉。我們是在建立這學期的共同 Lab。

### Transition
「以前要做出這個網站，到底需要先學多少東西？」

---

## Slide 04 — Before AI, What Would You Need?

### Purpose
Show the traditional skill stack and motivate build-first learning without devaluing fundamentals.

### On-slide
# 做這個網站，你原本需要會多少東西？

Skill wall:

```text
Python
requests
HTTP
API
JSON
pandas
CSV
Streamlit
Folium
HTML
Environment Variables
Testing
Debugging
Git
Security
...
```

Center student bubble:

**「老師，我還沒學完耶……」**

Bottom reveal:

# BUILD FIRST → UNDERSTAND → VERIFY

### Visual composition
Skill cards float around a central learner. The BUILD FIRST arrow appears after discussion.

### 煥哥
- Expression: light humorous grimace / “很多吧？”
- Pose: both hands slightly spread while looking at the skill wall.
- Do not use prayer/closed-hands gesture.
- Gaze: toward floating skills.

### Teacher talk
照傳統順序，我可能要先教 Python，再 requests、HTTP、API、JSON、pandas、Streamlit、Folium，最後才開始做網站。這個方法沒有錯。但是 AI Coding Agent 出現之後，我們多了一種新的學習方式：先看到一個完整系統，再把它拆開學。

但是這也產生新的問題：**如果你根本不知道 AI 做了什麼，你怎麼知道它是對的？**

### Key teaching point
Build-first is not skip-understanding. It is:

**BUILD FIRST → UNDERSTAND → VERIFY**

### Transition
「所以我們需要的不是只會聊天的 AI，而是一個能協助工程工作的 Agent。」

---

## Slide 05 — Meet Antigravity

### Purpose
Introduce Antigravity at concept level without turning L1 into an Antigravity operations lesson.

### On-slide
# Meet Your AI Coding Agent

**ANTIGRAVITY**

```text
YOU
 │
 │ Requirement
 ▼
AI Coding Agent
 │
 ├─ Plan
 ├─ Create Files
 ├─ Write Code
 ├─ Run
 ├─ Test
 └─ Fix Errors
```

# YOU ARE STILL RESPONSIBLE.

### Visual composition
Human → Requirement → Agent → engineering actions. Bottom responsibility statement should be visually bold.

### 煥哥
- Expression: more serious than previous slides; responsible engineer mindset.
- Pose: one hand points to the Antigravity workflow; the other points toward himself/students.
- Gaze: toward students.

### Teacher talk
Antigravity 跟單純問 ChatGPT「請給我 Python Code」不完全一樣。Coding Agent 不只是回答一段程式，它可以在工程環境裡協助規劃、建立檔案、修改程式、執行、測試，再根據結果修正。

但最重要的一句話是：**YOU ARE STILL RESPONSIBLE.**

AI 寫錯了，誰負責？不是 AI，工程師負責。所以我們不是學「如何叫 AI 幫我把作業做完」，而是學「如何讓 AI 成為工程助手，而我仍然知道怎麼驗證」。

### Transition
「那我到底要怎麼把需求交給 Agent？」

---

## Slide 06 — The Prompt

### Purpose
Show that good AI engineering begins with structured requirements and constraints, then launch the first live demo.

### On-slide
# What If I Just Tell AI What I Want?

Prompt structure:

```text
CREATE
AI Weather Security Center

DATA
CWA F-A0010-001

FETCH
7-day weather forecast

PROCESS
Min / Max / Average Temperature

SAVE
weather_data.csv

DISPLAY
Streamlit + Taiwan Map

INTERACT
Date Selector

SECURITY
No hard-coded API key
Validate external data
Use timeout
Keep SSL verification

TEST
Run tests and validate website
```

Bottom-right CTA:

# ▶ SEND TO ANTIGRAVITY

### Visual composition
Large structured prompt card on left/center. Run button on lower right. Keep enough whitespace to feel like a launch moment.

### 煥哥
- Expression: focused, anticipatory.
- Pose: right index finger ready to press `SEND / RUN`; body slightly forward.
- Gaze: at the button.
- Emotional role: “launch sequence”.

### Teacher talk
注意，我沒有告訴 AI 第 1 行寫 `import requests`、第 2 行寫什麼。我告訴它的是我要什麼。我把需求、資料來源、輸出、UI、安全限制與測試要求講清楚。

這就是 AI Engineering 很重要的改變：從只會寫 Syntax，慢慢往 **Requirement、Constraint、Evidence** 前進。

### Live Demo
Switch to Antigravity and paste the full CWA Weather Security Center build prompt from the L1 build specification.

Say before running:

「現在開始，我先不碰程式碼。我們看看 Agent 自己會怎麼規劃。」

Then run.

### Student observation task
While the Agent works, tell students not to focus on individual Python lines yet. Watch for:
1. Does it make a plan?
2. Does it create a project structure?
3. Does it separate responsibilities into files?
4. Does it install dependencies?
5. Does it run tests?
6. Does it encounter errors?
7. What evidence does it provide that the site really works?

### Transition
Keep the Antigravity screen visible. Slide 07 explains what students should observe while the agent works.
