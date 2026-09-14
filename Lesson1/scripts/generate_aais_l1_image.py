#!/usr/bin/env python3
"""
Generate AIIS_L1.png — 20-Panel Master Summary Thumbnail (5x4 Grid)
Matching the exact layout, colors, typography, avatars, and visual hierarchy of AIIS_L0.png.

Dimensions: 3344 x 1882 (2x Ultra HD, scaled to 1672 x 941 for standard display)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
OUTPUT_IMAGE = os.path.join(BASE_DIR, "AIIS_L1.png")
OUTPUT_IMAGE_ROOT = os.path.abspath("AIIS_L1.png")

# Canvas Dimensions (2x Super Sampled for crisp rendering)
CW = 3344
CH = 1882

COLS = 5
ROWS = 4
MARGIN_X = 24
MARGIN_Y = 24
GAP_X = 18
GAP_Y = 18

PW = (CW - 2 * MARGIN_X - (COLS - 1) * GAP_X) // COLS  # ~643 px
PH = (CH - 2 * MARGIN_Y - (ROWS - 1) * GAP_Y) // ROWS  # ~445 px

# Font paths
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"

FONTS = {
    "panel_title": ImageFont.truetype(FONT_PATH, 28),
    "panel_sub": ImageFont.truetype(FONT_PATH, 18),
    "card_title": ImageFont.truetype(FONT_PATH, 22),
    "card_body": ImageFont.truetype(FONT_PATH, 17),
    "card_bold": ImageFont.truetype(FONT_PATH, 19),
    "small": ImageFont.truetype(FONT_PATH, 15),
    "badge": ImageFont.truetype(FONT_PATH, 16),
    "callout": ImageFont.truetype(FONT_PATH, 22),
    "callout_bold": ImageFont.truetype(FONT_PATH, 24),
    "page_num": ImageFont.truetype(FONT_PATH, 20),
    "hero_title": ImageFont.truetype(FONT_PATH, 42),
    "hero_sub": ImageFont.truetype(FONT_PATH, 22),
}

# Theme Color Palette matching AIIS_L0.png
COLORS = {
    "canvas_bg": (240, 244, 248),
    "panel_bg": (255, 255, 255),
    "panel_border": (218, 226, 237),
    "royal_blue": (11, 79, 156),         # #0B4F9C
    "sky_blue": (2, 132, 199),           # #0284C7
    "sky_blue_light": (224, 242, 254),   # #E0F2FE
    "gold_amber": (245, 158, 11),        # #F59E0B
    "gold_light": (254, 243, 199),       # #FEF3C7
    "emerald": (16, 185, 129),           # #10B981
    "emerald_light": (209, 250, 229),    # #D1FAE5
    "rose_red": (225, 29, 72),           # #E11D48
    "rose_light": (255, 228, 230),       # #FFE4E6
    "purple": (124, 58, 237),            # #7C3AED
    "purple_light": (237, 233, 254),     # #EDE9FE
    "orange": (234, 88, 12),             # #EA580C
    "orange_light": (255, 237, 213),     # #FFEDD5
    "dark_navy": (15, 23, 42),           # #0F172A
    "text_dark": (15, 23, 42),
    "text_muted": (71, 85, 105),         # #475569
    "border_light": (226, 232, 240),
    "white": (255, 255, 255),
}


def load_asset(filename, size=None):
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        return None
    try:
        img = Image.open(path)
        if size:
            img = img.resize(size, Image.LANCZOS)
        return img
    except Exception:
        return None


def draw_rounded(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


def get_panel_bbox(col, row):
    x1 = MARGIN_X + col * (PW + GAP_X)
    y1 = MARGIN_Y + row * (PH + GAP_Y)
    x2 = x1 + PW
    y2 = y1 + PH
    return (x1, y1, x2, y2)


def draw_panel_header(draw, px, py, title_zh, title_en, page_num, icon_color=COLORS["sky_blue"]):
    # Icon Box
    draw_rounded(draw, (px + 16, py + 16, px + 44, py + 44), radius=6, fill=icon_color)
    # Title ZH
    draw.text((px + 52, py + 14), title_zh, font=FONTS["panel_title"], fill=COLORS["royal_blue"])
    # Subtitle EN
    draw.text((px + 52, py + 46), title_en, font=FONTS["panel_sub"], fill=COLORS["sky_blue"])
    # Page Number
    draw.text((px + PW - 42, py + PH - 34), str(page_num), font=FONTS["page_num"], fill=COLORS["royal_blue"])


# =========================================================================
# PANEL RENDERERS (1 ~ 20)
# =========================================================================

def draw_panel_01(img, draw, px, py):
    """Panel 1: AIIS_L1 Cover Hero (Matching AIIS_L0 Cover Layout)"""
    # Top Left Blue Brand Card
    draw_rounded(draw, (px + 20, py + 25, px + 220, py + 90), radius=8, fill=COLORS["royal_blue"])
    draw.text((px + 30, py + 32), "AIIS", font=FONTS["hero_title"], fill=COLORS["white"])
    
    draw.text((px + 20, py + 110), "AI and Information Security", font=FONTS["panel_sub"], fill=COLORS["sky_blue"])
    draw.text((px + 20, py + 135), "人工智慧與資訊安全", font=FONTS["panel_title"], fill=COLORS["royal_blue"])
    
    # Tag
    draw_rounded(draw, (px + 20, py + 185, px + 160, py + 225), radius=8, fill=COLORS["sky_blue"])
    draw.text((px + 32, py + 195), "AIIS_L1", font=FONTS["card_bold"], fill=COLORS["white"])
    
    draw.text((px + 20, py + 240), "BUILD: AI Weather Security Center", font=FONTS["card_bold"], fill=COLORS["dark_navy"])
    draw.text((px + 20, py + 275), "從結構化提示詞到可運行氣象監控中心", font=FONTS["card_body"], fill=COLORS["text_muted"])
    
    # Callout Banner
    draw_rounded(draw, (px + 20, py + 340, px + 360, py + 400), radius=10, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    draw.text((px + 35, py + 355), "Welcome to AIIS_L1!", font=FONTS["callout_bold"], fill=COLORS["royal_blue"])
    
    # Portrait
    portrait = load_asset("huange_portrait.png", (180, 310))
    if portrait:
        img.paste(portrait, (px + PW - 210, py + 90))
        
    draw.text((px + PW - 30, py + PH - 34), "1", font=FONTS["page_num"], fill=COLORS["royal_blue"])


def draw_panel_02(img, draw, px, py):
    """Panel 2: 課程大綱 (Course Overview)"""
    draw_panel_header(draw, px, py, "課程大綱", "Course Overview", 2)
    
    agenda = [
        "1. Prompt to Working Website",
        "2. Central Weather Admin (CWA) Data",
        "3. WORKING ✓ vs. SECURE ?",
        "4. Asset / Threat / Vulnerability / Risk",
        "5. CIA Triad in Action",
        "6. AI Role: Builder -> Analyst",
        "7. AIIS_L1_LAB01 Mini Lab",
        "8. Human Verification & Evidence"
    ]
    for i, item in enumerate(agenda):
        ay = py + 80 + i * 36
        draw_rounded(draw, (px + 24, ay, px + 50, ay + 26), radius=13, fill=COLORS["royal_blue"])
        draw.text((px + 32, ay + 3), str(i+1), font=FONTS["small"], fill=COLORS["white"])
        draw.text((px + 62, ay + 2), item, font=FONTS["card_body"], fill=COLORS["dark_navy"])
        
    av = load_asset("avatar_welcome.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 170, py + 160))
        
    draw.text((px + PW - 240, py + 380), "Let's get started!", font=FONTS["callout_bold"], fill=COLORS["orange"])


def draw_panel_03(img, draw, px, py):
    """Panel 3: One Prompt -> One Real Website"""
    draw_panel_header(draw, px, py, "提示詞到實體網站", "One Prompt -> One Real Website", 3)
    
    steps = [
        ("Structured Prompt", "結構化提示詞", COLORS["sky_blue_light"], COLORS["sky_blue"]),
        ("Antigravity Agent", "AI 自主建置代理", COLORS["purple_light"], COLORS["purple"]),
        ("Working Website", "即時氣象資安中心", COLORS["emerald_light"], COLORS["emerald"]),
        ("WORKING ≠ SECURE", "能跑不代表安全！", COLORS["rose_light"], COLORS["rose_red"]),
    ]
    
    for i, (en, zh, bg, fg) in enumerate(steps):
        sy = py + 80 + i * 75
        draw_rounded(draw, (px + 30, sy, px + PW - 200, sy + 62), radius=10, fill=bg, outline=fg, width=2)
        draw.text((px + 45, sy + 8), en, font=FONTS["card_bold"], fill=fg)
        draw.text((px + 45, sy + 32), zh, font=FONTS["small"], fill=COLORS["text_muted"])
        if i < 3:
            draw.text((px + 180, sy + 58), "↓", font=FONTS["panel_title"], fill=COLORS["sky_blue"])
            
    av = load_asset("avatar_idea.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 170, py + 160))
        
    draw.text((px + 30, py + 390), "Prompt is Engineering! Next Level!", font=FONTS["callout_bold"], fill=COLORS["orange"])


def draw_panel_04(img, draw, px, py):
    """Panel 4: Meet Antigravity & AI Agents"""
    draw_panel_header(draw, px, py, "認識 AI 協作代理", "Meet Antigravity & AI Agents", 4)
    
    cards = [
        ("Planning", "架構與任務拆解", COLORS["sky_blue_light"], COLORS["sky_blue"]),
        ("Coding", "FastAPI & 資料庫", COLORS["purple_light"], COLORS["purple"]),
        ("Tool Execution", "終端指令與測試", COLORS["emerald_light"], COLORS["emerald"]),
    ]
    cw = (PW - 60) // 3
    for i, (head, sub, bg, fg) in enumerate(cards):
        cx = px + 20 + i * (cw + 10)
        draw_rounded(draw, (cx, py + 90, cx + cw, py + 300), radius=12, fill=bg, outline=fg, width=2)
        draw_rounded(draw, (cx, py + 90, cx + cw, py + 140), radius=12, fill=fg)
        draw.text((cx + 15, py + 105), head, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 15, py + 170), sub, font=FONTS["card_bold"], fill=COLORS["dark_navy"])
        draw.text((cx + 15, py + 220), "• 自動化執行\n• 程式碼產出", font=FONTS["small"], fill=COLORS["text_muted"])

    # Bottom Callout Bar
    draw_rounded(draw, (px + 20, py + 330, px + PW - 160, py + 395), radius=10, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=1)
    draw.text((px + 35, py + 348), "“ AI 是你的全端助手，但不是安全保證！ ”", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_laptop.png", (130, 160))
    if av:
        img.paste(av, (px + PW - 145, py + 260))


def draw_panel_05(img, draw, px, py):
    """Panel 5: 結構化建置提示詞 (The Build Prompt)"""
    draw_panel_header(draw, px, py, "結構化建置提示詞", "The Structured Build Prompt", 5)
    
    sections = [
        ("1. Role", "資深全端與資安工程師", COLORS["royal_blue"]),
        ("2. Goal", "建置即時氣象資安監控中心", COLORS["sky_blue"]),
        ("3. Stack", "FastAPI + SQLite + HTML5", COLORS["purple"]),
        ("4. Boundary", "僅限 localhost 隔離環境", COLORS["rose_red"]),
    ]
    for i, (tag, val, fg) in enumerate(sections):
        sy = py + 85 + i * 65
        draw_rounded(draw, (px + 20, sy, px + PW - 160, sy + 55), radius=10, fill=COLORS["canvas_bg"], outline=COLORS["border_light"], width=1)
        draw_rounded(draw, (px + 20, sy, px + 150, sy + 55), radius=10, fill=fg)
        draw.text((px + 35, sy + 16), tag, font=FONTS["card_bold"], fill=COLORS["white"])
        draw.text((px + 165, sy + 16), val, font=FONTS["card_bold"], fill=COLORS["dark_navy"])
        
    draw_rounded(draw, (px + 20, py + 360, px + PW - 160, py + 415), radius=8, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    draw.text((px + 35, py + 375), "提示詞寫得結構化，系統架構就清晰！", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_explain.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 150, py + 200))


def draw_panel_06(img, draw, px, py):
    """Panel 6: Watch the Agent Work (Terminal & Build)"""
    draw_panel_header(draw, px, py, "觀看 Agent 自主建置", "Watch the Agent Work", 6)
    
    # Terminal UI
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 340), radius=12, fill=COLORS["dark_navy"])
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 120), radius=12, fill=(30, 41, 59))
    draw.text((px + 35, py + 92), "● ● ●  bash — antigravity agent", font=FONTS["small"], fill=(148, 163, 184))
    
    code_lines = [
        "$ pip install fastapi uvicorn sqlite3 httpx",
        "[Agent] Creating database schema: schema.sql",
        "[Agent] Fetching CWA Weather API endpoints...",
        "[Agent] Building dashboard UI & API routes...",
        "[Agent] Uvicorn running on http://127.0.0.1:8000"
    ]
    for i, line in enumerate(code_lines):
        col = COLORS["emerald"] if i == 4 else (226, 232, 240)
        draw.text((px + 35, py + 135 + i * 38), line, font=FONTS["small"], fill=col)
        
    draw.text((px + 30, py + 365), "AI 提議代碼，系統幾分鐘內成形！", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    draw.text((px + 30, py + 395), "AI runs fast, but who checks safety?", font=FONTS["small"], fill=COLORS["rose_red"])
    
    av = load_asset("avatar_laptop.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 180))


def draw_panel_07(img, draw, px, py):
    """Panel 7: It Runs! 成果展示"""
    draw_panel_header(draw, px, py, "成果展示：系統跑起來了！", "It Runs! localhost:8000", 7)
    
    # Browser Mockup
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 340), radius=12, fill=COLORS["canvas_bg"], outline=COLORS["sky_blue"], width=2)
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 125), radius=12, fill=COLORS["royal_blue"])
    draw.text((px + 35, py + 95), "[Web] AI Weather Security Center -- LIVE", font=FONTS["card_bold"], fill=COLORS["white"])
    
    features = [
        ("即時氣象看板", "即時氣溫 28.5 C / 濕度 75%"),
        ("災害預警中心", "豪雨特報與颱風路徑追蹤"),
        ("身分認證系統", "使用者登入 / API Key 管理"),
    ]
    for i, (h, b) in enumerate(features):
        fy = py + 140 + i * 62
        draw_rounded(draw, (px + 30, fy, px + PW - 195, fy + 52), radius=8, fill=COLORS["white"], outline=COLORS["border_light"], width=1)
        draw.text((px + 45, fy + 6), f"[OK] {h} :", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
        draw.text((px + 200, fy + 8), b, font=FONTS["small"], fill=COLORS["text_muted"])
        
    draw.text((px + 30, py + 375), "It's Alive! 一次提示詞就完成！", font=FONTS["callout_bold"], fill=COLORS["orange"])
    
    av = load_asset("avatar_present.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 165, py + 170))


def draw_panel_08(img, draw, px, py):
    """Panel 8: 中央氣象署 CWA Real Data"""
    draw_panel_header(draw, px, py, "中央氣象署 CWA Real Data", "Real Data, Not a Toy", 8)
    
    # Taiwan Map & Data Box
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 340), radius=12, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    
    data_items = [
        "[+] 氣溫 (Temperature)",
        "[+] 濕度 (Humidity)",
        "[+] 降雨量 (Rainfall)",
        "[+] 警報預警 (Weather Alerts)",
        "[+] 觀測資料 (Observations)"
    ]
    for i, item in enumerate(data_items):
        draw.text((px + 40, py + 110 + i * 42), item, font=FONTS["card_bold"], fill=COLORS["royal_blue"])
        
    draw_rounded(draw, (px + 20, py + 360, px + PW - 20, py + 415), radius=8, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=1)
    draw.text((px + 35, py + 375), "真實資料，真實應用！串接 CWA Open Data API", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_welcome.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 165, py + 140))


def draw_panel_09(img, draw, px, py):
    """Panel 9: WORKING ✓ vs. SECURE ? (關鍵轉折點)"""
    draw_panel_header(draw, px, py, "關鍵轉折：能跑 ≠ 安全", "WORKING ✓ vs. SECURE ?", 9)
    
    # 2 Comparison Boxes
    bw = (PW - 60) // 2
    
    # Left: Working
    draw_rounded(draw, (px + 20, py + 85, px + 20 + bw, py + 290), radius=12, fill=COLORS["emerald_light"], outline=COLORS["emerald"], width=2)
    draw_rounded(draw, (px + 20, py + 85, px + 20 + bw, py + 135), radius=12, fill=COLORS["emerald"])
    draw.text((px + 40, py + 98), "WORKING ✓ (功能正常)", font=FONTS["card_title"], fill=COLORS["white"])
    draw.text((px + 35, py + 160), "• 網頁能正常開啟\n• 氣象資料能抓取\n• API 請求有回應", font=FONTS["card_bold"], fill=COLORS["dark_navy"])
    
    # Right: Secure?
    draw_rounded(draw, (px + 40 + bw, py + 85, px + PW - 20, py + 290), radius=12, fill=COLORS["rose_light"], outline=COLORS["rose_red"], width=2)
    draw_rounded(draw, (px + 40 + bw, py + 85, px + PW - 20, py + 135), radius=12, fill=COLORS["rose_red"])
    draw.text((px + 60 + bw, py + 98), "SECURE ? (安全嗎？)", font=FONTS["card_title"], fill=COLORS["white"])
    draw.text((px + 55 + bw, py + 160), "• API Key 是否寫死？\n• 有無防禦暴力破解？\n• 外部輸入有無驗證？", font=FONTS["card_bold"], fill=COLORS["rose_red"])

    # Bottom Callout Bar
    draw_rounded(draw, (px + 20, py + 320, px + PW - 160, py + 410), radius=10, fill=COLORS["dark_navy"])
    draw.text((px + 35, py + 338), "“ 能跑不代表安全！”，這是資安工程師的第一堂課。", font=FONTS["card_bold"], fill=COLORS["gold_amber"])
    draw.text((px + 35, py + 372), "AI Proposes, Security Validates.", font=FONTS["small"], fill=COLORS["white"])
    
    av = load_asset("avatar_inspect.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 150, py + 240))


def draw_panel_10(img, draw, px, py):
    """Panel 10: 資產偵探 (Asset Detective)"""
    draw_panel_header(draw, px, py, "資產偵探：保護什麼？", "Security Starts with Assets", 10)
    
    assets = [
        ("氣象伺服器 (Server)", "系統服務與運算資源", COLORS["sky_blue"]),
        ("CWA API Key (憑證)", "第三方真實認證金鑰", COLORS["rose_red"]),
        ("SQLite 資料庫 (DB)", "使用者密碼與日誌記錄", COLORS["purple"]),
        ("管理員權限 (Identity)", "系統最高控制授權", COLORS["gold_amber"]),
    ]
    for i, (h, b, fg) in enumerate(assets):
        ay = py + 85 + i * 62
        draw_rounded(draw, (px + 20, ay, px + PW - 180, ay + 52), radius=8, fill=COLORS["canvas_bg"], outline=fg, width=1)
        draw.text((px + 35, ay + 6), f"• {h}", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
        draw.text((px + 35, ay + 28), b, font=FONTS["small"], fill=COLORS["text_muted"])
        
    draw_rounded(draw, (px + 20, py + 360, px + PW - 180, py + 415), radius=8, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=1)
    draw.text((px + 35, py + 375), "“ 沒有 Asset，就沒有 Risk！ ”", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_inspect.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 160))


def draw_panel_11(img, draw, px, py):
    """Panel 11: 什麼會造成危害？(Threat)"""
    draw_panel_header(draw, px, py, "什麼會造成危害？", "What Can Go Wrong? — Threat", 11)
    
    threats = [
        ("惡意攻擊者 (Attacker)", "外部駭客試圖取得系統控制權", COLORS["rose_red"]),
        ("惡意爬蟲 (Scraper)", "海量請求灌爆氣象 API 伺服器", COLORS["orange"]),
        ("金鑰竊取者 (Thief)", "搜尋程式碼竊取 CWA API Key", COLORS["purple"]),
        ("資料篡改者 (Tamperer)", "竄改警報發布虛假災情報告", COLORS["royal_blue"]),
    ]
    for i, (h, b, fg) in enumerate(threats):
        ty = py + 85 + i * 62
        draw_rounded(draw, (px + 20, ty, px + PW - 180, ty + 52), radius=8, fill=COLORS["canvas_bg"], outline=fg, width=1)
        draw.text((px + 35, ty + 6), f"[!] {h}", font=FONTS["card_bold"], fill=fg)
        draw.text((px + 35, ty + 28), b, font=FONTS["small"], fill=COLORS["text_muted"])
        
    draw.text((px + 25, py + 375), "威脅是外在潛在危險，無所不在！", font=FONTS["card_bold"], fill=COLORS["rose_red"])
    
    av = load_asset("avatar_inspect.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 160))


def draw_panel_12(img, draw, px, py):
    """Panel 12: 為什麼會成功？(Vulnerability)"""
    draw_panel_header(draw, px, py, "為什麼會成功？(弱點)", "Why Could It Succeed? — Vulnerability", 12)
    
    vulns = [
        ("硬編碼金鑰 (Hardcoded Secret)", "API Key 直接寫死在 Python 檔案中", COLORS["rose_red"]),
        ("缺乏速率限制 (No Rate Limit)", "未防禦每秒數千次惡意重複請求", COLORS["orange"]),
        ("未過濾使用者輸入 (No Sanitize)", "輸入框直接拼接 SQL 或命令字串", COLORS["purple"]),
        ("弱身分驗證 (Weak Auth)", "使用明文比對密碼，無雜湊加密", COLORS["royal_blue"]),
    ]
    for i, (h, b, fg) in enumerate(vulns):
        vy = py + 85 + i * 62
        draw_rounded(draw, (px + 20, vy, px + PW - 180, vy + 52), radius=8, fill=COLORS["canvas_bg"], outline=fg, width=1)
        draw.text((px + 35, vy + 6), f"[*] {h}", font=FONTS["card_bold"], fill=fg)
        draw.text((px + 35, vy + 28), b, font=FONTS["small"], fill=COLORS["text_muted"])
        
    draw.text((px + 25, py + 375), "Bug != Vulnerability！弱點是能被攻擊的破洞。", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_explain.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 160))


def draw_panel_13(img, draw, px, py):
    """Panel 13: Threat != Vulnerability (核心辨析)"""
    draw_panel_header(draw, px, py, "威脅 vs. 弱點本質差異", "Threat != Vulnerability", 13)
    
    # 2 Comparison Columns
    cw = (PW - 60) // 2
    
    # Left: Threat
    draw_rounded(draw, (px + 20, py + 85, px + 20 + cw, py + 270), radius=10, fill=COLORS["rose_light"], outline=COLORS["rose_red"], width=1)
    draw.text((px + 35, py + 95), "THREAT (威脅)", font=FONTS["card_title"], fill=COLORS["rose_red"])
    draw.text((px + 35, py + 140), "• 外在環境危害\n• 惡意攻擊者動機\n• 我們無法消滅威脅", font=FONTS["card_bold"], fill=COLORS["dark_navy"])
    
    # Right: Vulnerability
    draw_rounded(draw, (px + 35 + cw, py + 85, px + PW - 25, py + 270), radius=10, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    draw.text((px + 50 + cw, py + 95), "VULN (弱點)", font=FONTS["card_title"], fill=COLORS["sky_blue"])
    draw.text((px + 50 + cw, py + 140), "• 內部系統破洞\n• 程式碼實作缺陷\n• 我們可以修復弱點！", font=FONTS["card_bold"], fill=COLORS["dark_navy"])

    # Bottom Formula
    draw_rounded(draw, (px + 20, py + 295, px + PW - 20, py + 410), radius=10, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=2)
    draw.text((px + 35, py + 312), "【風險公式】 Risk = Threat × Vulnerability × Impact", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    draw.text((px + 35, py + 355), "-> 消弭弱點，就能切斷威脅，將風險降至最低！", font=FONTS["card_body"], fill=COLORS["dark_navy"])


def draw_panel_14(img, draw, px, py):
    """Panel 14: CIA Triad 在氣象系統的實踐"""
    draw_panel_header(draw, px, py, "資訊安全 CIA 三要素", "Confidentiality, Integrity, Availability", 14)
    
    pillars = [
        ("C · 機密性", "Confidentiality", "API Key 不外洩\n密碼安全加密", COLORS["sky_blue_light"], COLORS["sky_blue"]),
        ("I · 完整性", "Integrity", "氣象資料不被竄改\n保持真實預報", COLORS["emerald_light"], COLORS["emerald"]),
        ("A · 可用性", "Availability", "災難來臨不中斷\n服務穩定在線", COLORS["gold_light"], COLORS["gold_amber"]),
    ]
    cw = (PW - 60) // 3
    for i, (zh, en, desc, bg, fg) in enumerate(pillars):
        cx = px + 20 + i * (cw + 10)
        draw_rounded(draw, (cx, py + 90, cx + cw, py + 310), radius=12, fill=bg, outline=fg, width=2)
        draw_rounded(draw, (cx, py + 90, cx + cw, py + 140), radius=12, fill=fg)
        draw.text((cx + 12, py + 105), zh, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 12, py + 155), en, font=FONTS["small"], fill=fg)
        lines = desc.split("\n")
        draw.text((cx + 12, py + 195), lines[0], font=FONTS["card_bold"], fill=COLORS["dark_navy"])
        if len(lines) > 1:
            draw.text((cx + 12, py + 230), lines[1], font=FONTS["card_body"], fill=COLORS["text_muted"])

    draw.text((px + 30, py + 365), "Security = Trust! 信任源自於 CIA 的守護。", font=FONTS["callout_bold"], fill=COLORS["orange"])
    
    av = load_asset("avatar_welcome.png", (130, 160))
    if av:
        img.paste(av, (px + PW - 145, py + 260))


def draw_panel_15(img, draw, px, py):
    """Panel 15: 從弱點到風險評級 (Risk Matrix)"""
    draw_panel_header(draw, px, py, "從弱點到風險評級", "From Vulnerability to Risk", 15)
    
    # Risk Levels
    levels = [
        ("CRITICAL", "嚴重風險", "API Key 公開外洩，任何人皆可盜用", COLORS["rose_red"]),
        ("HIGH", "高度風險", "缺乏 Rate Limit，可能遭 DoS 癱瘓", COLORS["orange"]),
        ("MEDIUM", "中度風險", "錯誤訊息暴露資料庫欄位結構", COLORS["gold_amber"]),
        ("LOW", "低度風險", "HTTP 標頭缺少安全防禦宣告", COLORS["sky_blue"]),
    ]
    for i, (lvl, zh, desc, fg) in enumerate(levels):
        ry = py + 85 + i * 62
        draw_rounded(draw, (px + 20, ry, px + PW - 180, ry + 52), radius=8, fill=COLORS["canvas_bg"], outline=fg, width=1)
        draw_rounded(draw, (px + 20, ry, px + 125, ry + 52), radius=8, fill=fg)
        draw.text((px + 28, ry + 16), lvl, font=FONTS["badge"], fill=COLORS["white"])
        draw.text((px + 140, ry + 14), f"{zh}：{desc}", font=FONTS["small"], fill=COLORS["dark_navy"])
        
    draw.text((px + 25, py + 375), "科學化量化風險，決定防禦優先順序！", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_laptop.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 160))


def draw_panel_16(img, draw, px, py):
    """Panel 16: AI 角色切換 (Builder -> Security Analyst)"""
    draw_panel_header(draw, px, py, "AI 角色切換：建置 -> 審計", "AI Changes Role: Builder -> Analyst", 16)
    
    # 2 Role Boxes
    cw = (PW - 60) // 2
    
    draw_rounded(draw, (px + 20, py + 85, px + 20 + cw, py + 280), radius=12, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=2)
    draw_rounded(draw, (px + 20, py + 85, px + 20 + cw, py + 135), radius=12, fill=COLORS["sky_blue"])
    draw.text((px + 35, py + 98), "ROLE 1: BUILDER", font=FONTS["card_title"], fill=COLORS["white"])
    draw.text((px + 35, py + 155), "• 幫忙寫代碼\n• 快速搭出原型\n• 生成資料庫 Schema", font=FONTS["card_bold"], fill=COLORS["dark_navy"])
    
    draw_rounded(draw, (px + 40 + cw, py + 85, px + PW - 20, py + 280), radius=12, fill=COLORS["purple_light"], outline=COLORS["purple"], width=2)
    draw_rounded(draw, (px + 40 + cw, py + 85, px + PW - 20, py + 135), radius=12, fill=COLORS["purple"])
    draw.text((px + 55 + cw, py + 98), "ROLE 2: ANALYST", font=FONTS["card_title"], fill=COLORS["white"])
    draw.text((px + 55 + cw, py + 155), "• 幫忙挑漏洞\n• 進行威脅審查\n• 提供修復建議", font=FONTS["card_bold"], fill=COLORS["purple"])

    draw_rounded(draw, (px + 20, py + 310, px + PW - 20, py + 410), radius=10, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=1)
    draw.text((px + 35, py + 330), "【核心洞察】「讓 AI 成為你的安全顧問，而非唯一決策者！」", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    draw.text((px + 35, py + 368), "AI BUILDS. HUMAN VERIFIES.", font=FONTS["card_title"], fill=COLORS["orange"])


def draw_panel_17(img, draw, px, py):
    """Panel 17: 實證原則 (AI Finding != Confirmed Finding)"""
    draw_panel_header(draw, px, py, "實證原則：不盲信 AI", "AI Finding != Confirmed Finding", 17)
    
    rules = [
        ("要求 Evidence", "AI 提出的漏洞必須有具體代碼行號與證明"),
        ("區分 Fact vs. Assumption", "是實際存在的漏洞，還是 AI 的臆測？"),
        ("人類工程師簽核", "由人類做出最終判定 (Human-in-the-Loop)"),
    ]
    for i, (h, b) in enumerate(rules):
        ry = py + 85 + i * 75
        draw_rounded(draw, (px + 20, ry, px + PW - 180, ry + 65), radius=10, fill=COLORS["canvas_bg"], outline=COLORS["royal_blue"], width=1)
        draw.text((px + 35, ry + 10), f"[Pin] {h}：", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
        draw.text((px + 35, ry + 36), b, font=FONTS["small"], fill=COLORS["text_muted"])
        
    draw.text((px + 25, py + 375), "AI 提議，人類理解，資安驗證！", font=FONTS["card_bold"], fill=COLORS["rose_red"])
    
    av = load_asset("avatar_inspect.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 160))


def draw_panel_18(img, draw, px, py):
    """Panel 18: AIIS_L1_LAB01 實戰任務"""
    draw_panel_header(draw, px, py, "AIIS_L1_LAB01", "Security Risk Detective Lab", 18)
    
    # Terminal & Task
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 340), radius=12, fill=COLORS["dark_navy"])
    draw.text((px + 35, py + 98), "task: AIIS_L1_LAB01 (Risk Detective)", font=FONTS["small"], fill=COLORS["sky_blue"])
    
    tasks = [
        "[+] 1. Run local weather app (localhost:8000)",
        "[+] 2. Execute AI Security Review Prompt",
        "[+] 3. Fill Risk Detective Report Matrix",
        "[+] 4. Provide Evidence & Human Sign-off"
    ]
    for i, t in enumerate(tasks):
        draw.text((px + 35, py + 145 + i * 42), t, font=FONTS["small"], fill=COLORS["emerald"])
        
    draw.text((px + 30, py + 375), "Let's code & verify! 動手實戰！", font=FONTS["callout_bold"], fill=COLORS["orange"])
    
    av = load_asset("avatar_laptop.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 160, py + 170))


def draw_panel_19(img, draw, px, py):
    """Panel 19: 全學期主線與 L2 預告"""
    draw_panel_header(draw, px, py, "這門課的主線與預告", "Our Learning Journey & Next Step", 19)
    
    # 5 Stages Bar
    stages = [
        ("BUILD", "L1-L3", COLORS["royal_blue"]),
        ("LEARN", "L4-L7", COLORS["sky_blue"]),
        ("ATTACK", "L8-L10", COLORS["rose_red"]),
        ("DEFEND", "L11-L14", COLORS["purple"]),
        ("GOVERN", "L15-L16", COLORS["gold_amber"]),
    ]
    sw = (PW - 60) // 5
    for i, (name, less, fg) in enumerate(stages):
        sx = px + 20 + i * (sw + 5)
        draw_rounded(draw, (sx, py + 90, sx + sw, py + 170), radius=8, fill=COLORS["canvas_bg"], outline=fg, width=1)
        draw_rounded(draw, (sx, py + 90, sx + sw, py + 125), radius=8, fill=fg)
        draw.text((sx + 8, py + 98), name, font=FONTS["badge"], fill=COLORS["white"])
        draw.text((sx + 14, py + 138), less, font=FONTS["small"], fill=fg)
        
    draw_rounded(draw, (px + 20, py + 190, px + PW - 160, py + 320), radius=10, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    draw.text((px + 35, py + 205), "【下一課預告】 AIIS_L2", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    draw.text((px + 35, py + 245), "• AI Security Toolbox & Git Workflow", font=FONTS["card_body"], fill=COLORS["dark_navy"])
    draw.text((px + 35, py + 280), "• 深入 Antigravity 專案管理與版本控制", font=FONTS["card_body"], fill=COLORS["text_muted"])
    
    draw.text((px + 30, py + 375), "16 週，一個完整的 AI × 資安學習旅程。", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    av = load_asset("avatar_welcome.png", (140, 180))
    if av:
        img.paste(av, (px + PW - 150, py + 170))


def draw_panel_20(img, draw, px, py):
    """Panel 20: 最後的話 (Thank You & Closing)"""
    draw_panel_header(draw, px, py, "最後的話", "Final Message", 20)
    
    # Big Quote Box
    draw_rounded(draw, (px + 20, py + 85, px + PW - 180, py + 290), radius=14, fill=COLORS["canvas_bg"], outline=COLORS["royal_blue"], width=2)
    draw.text((px + 35, py + 105), "“ WORKING != SECURE ”", font=FONTS["card_title"], fill=COLORS["rose_red"])
    draw.text((px + 35, py + 155), "AI is the capability.\nCybersecurity is the discipline.\nAI proposes. Human understands.\nSecurity validates.", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    draw.text((px + 35, py + 250), "—— 煥哥", font=FONTS["card_bold"], fill=COLORS["dark_navy"])
    
    draw.text((px + 25, py + 325), "Thank You! See you in AIIS_L2!", font=FONTS["callout_bold"], fill=COLORS["orange"])
    draw.text((px + 25, py + 370), "Learn · Build · Secure Our Future", font=FONTS["card_bold"], fill=COLORS["royal_blue"])
    
    portrait = load_asset("huange_portrait.png", (160, 270))
    if portrait:
        img.paste(portrait, (px + PW - 180, py + 100))


def main():
    print(f"🎨 Generating AIIS_L1 Master Summary Thumbnail ({CW} x {CH})...")
    img = Image.new("RGB", (CW, CH), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    
    # Outer Frame
    draw.rectangle([(0, 0), (CW, CH)], fill=COLORS["canvas_bg"])
    
    # Grid of 20 Panels
    panel_funcs = [
        draw_panel_01, draw_panel_02, draw_panel_03, draw_panel_04, draw_panel_05,
        draw_panel_06, draw_panel_07, draw_panel_08, draw_panel_09, draw_panel_10,
        draw_panel_11, draw_panel_12, draw_panel_13, draw_panel_14, draw_panel_15,
        draw_panel_16, draw_panel_17, draw_panel_18, draw_panel_19, draw_panel_20,
    ]
    
    for idx, fn in enumerate(panel_funcs):
        row = idx // COLS
        col = idx % COLS
        px, py, px2, py2 = get_panel_bbox(col, row)
        
        # Base panel background
        draw_rounded(draw, (px, py, px2, py2), radius=16, fill=COLORS["panel_bg"], outline=COLORS["panel_border"], width=2)
        
        # Render panel content
        fn(img, draw, px, py)
        print(f"  ✓ Rendered Panel {idx+1:02d} / 20 (Col {col+1}, Row {row+1})")
        
    # Save standard & high-res versions
    img_standard = img.resize((1672, 941), Image.LANCZOS)
    img_standard.save(OUTPUT_IMAGE, "PNG", quality=95)
    img_standard.save(OUTPUT_IMAGE_ROOT, "PNG", quality=95)
    
    print(f"\n🎉 Successfully created Lesson 1 Master Thumbnail:")
    print(f"   -> Course Path: {OUTPUT_IMAGE}")
    print(f"   -> Root Path:   {OUTPUT_IMAGE_ROOT}")


if __name__ == "__main__":
    main()
