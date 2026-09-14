#!/usr/bin/env python3
"""
Generate Lesson 0 Presentation Slides as 16:9 Images (Batch 1: Slides 1-10)
Adhering strictly to:
- Visual Style: pptsample.png / AIIS_L0.png (Vibrant Infographic + 煥哥 Avatar & Real Portrait)
- Large Bold Typography: Titles (32pt), Section Headers (24pt), Body Text (18-20pt), Badges (18-22pt)
- Rich Visual Archetypes: Deep Royal Blue (#0B4F9C), Gold Pills (#F59E0B), Colorful Outlined Cards
- Right-Hand Column: Dedicated 煥哥 Instructor Column & Action Avatars
- Aspect Ratio: 16:9 (1920 x 1080)
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
OUTPUT_DIR_COURSE = os.path.join(BASE_DIR, "slides_images")
OUTPUT_DIR_ROOT = os.path.abspath("slides_images")

os.makedirs(OUTPUT_DIR_COURSE, exist_ok=True)
os.makedirs(OUTPUT_DIR_ROOT, exist_ok=True)

# 16:9 Dimensions
WIDTH = 1920
HEIGHT = 1080

# Font Configuration
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT_PATH = "/System/Library/Fonts/STHeiti Light.ttc"

FONTS = {
    "cover_main": ImageFont.truetype(FONT_PATH, 54),
    "cover_sub": ImageFont.truetype(FONT_PATH, 30),
    "cover_en": ImageFont.truetype(FONT_PATH, 28),
    "header_title": ImageFont.truetype(FONT_PATH, 36),
    "header_sub": ImageFont.truetype(FONT_PATH, 20),
    "header_tag": ImageFont.truetype(FONT_PATH, 18),
    "card_title": ImageFont.truetype(FONT_PATH, 24),
    "card_body_bold": ImageFont.truetype(FONT_PATH, 20),
    "card_body": ImageFont.truetype(FONT_PATH, 17),
    "sidebar_title": ImageFont.truetype(FONT_PATH, 22),
    "sidebar_quote": ImageFont.truetype(FONT_PATH, 17),
    "slogan_bold": ImageFont.truetype(FONT_PATH, 21),
    "slogan_sub": ImageFont.truetype(FONT_PATH, 17),
    "badge": ImageFont.truetype(FONT_PATH, 16),
    "footer": ImageFont.truetype(FONT_LIGHT_PATH, 14),
}

# Color Tokens matching pptsample.png
COLORS = {
    "canvas_bg": (248, 250, 252),        # #F8FAFC
    "card_bg": (255, 255, 255),          # Pure White
    "royal_blue": (11, 79, 156),         # #0B4F9C Deep Royal Blue
    "sky_blue": (2, 132, 199),           # #0284C7 Sky Blue
    "sky_blue_light": (224, 242, 254),   # #E0F2FE
    "gold_amber": (245, 158, 11),        # #F59E0B Gold
    "gold_light": (254, 243, 199),       # #FEF3C7
    "emerald": (16, 185, 129),           # #10B981 Green
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
    "border_light": (226, 232, 240),     # #E2E8F0
    "white": (255, 255, 255),
}


def load_asset(filename, size=None):
    """Load image asset from assets directory."""
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


def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


def draw_header(draw, title_zh, title_en, tag="課程導論 · 世界觀", slide_num=1, total_slides=10):
    """Top Royal Blue Header Bar with Gold Badges."""
    # Top Deep Blue Header Container
    draw_rounded_rect(draw, (50, 25, WIDTH - 50, 130), radius=14, fill=COLORS["card_bg"], outline=COLORS["royal_blue"], width=2)
    
    # Left Category Tag (Gold Pill)
    tag_w = draw.textlength(tag, font=FONTS["header_tag"]) + 24
    draw_rounded_rect(draw, (75, 42, 75 + tag_w, 82), radius=12, fill=COLORS["gold_amber"])
    draw.text((87, 52), tag, font=FONTS["header_tag"], fill=COLORS["dark_navy"])
    
    # Main Chinese Title
    draw.text((75 + tag_w + 20, 38), title_zh, font=FONTS["header_title"], fill=COLORS["royal_blue"])
    
    # English Subtitle
    draw.text((75 + tag_w + 20, 85), title_en, font=FONTS["header_sub"], fill=COLORS["sky_blue"])
    
    # Page Indicator Pill
    page_str = f"{slide_num:02d} / {total_slides:02d}"
    pw = draw.textlength(page_str, font=FONTS["badge"]) + 20
    draw_rounded_rect(draw, (WIDTH - 75 - pw, 45, WIDTH - 75, 80), radius=10, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    draw.text((WIDTH - 75 - pw + 10, 53), page_str, font=FONTS["badge"], fill=COLORS["royal_blue"])


def draw_bottom_banner(draw, text_slogan, text_sub=None):
    """Signature Gold Bottom Banner matching pptsample.png."""
    draw_rounded_rect(draw, (50, HEIGHT - 130, WIDTH - 50, HEIGHT - 35), radius=12, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=2)
    
    # Gold Icon Pill
    draw_rounded_rect(draw, (70, HEIGHT - 118, 175, HEIGHT - 47), radius=8, fill=COLORS["gold_amber"])
    draw.text((82, HEIGHT - 92), "重點洞察", font=FONTS["badge"], fill=COLORS["dark_navy"])
    
    if text_sub:
        draw.text((195, HEIGHT - 114), text_slogan, font=FONTS["slogan_bold"], fill=COLORS["royal_blue"])
        draw.text((195, HEIGHT - 72), text_sub, font=FONTS["slogan_sub"], fill=COLORS["dark_navy"])
    else:
        draw.text((195, HEIGHT - 94), text_slogan, font=FONTS["slogan_bold"], fill=COLORS["royal_blue"])


def draw_huange_sidebar(base_img, draw, quote_title, quote_bullets, avatar_name="avatar_explain.png"):
    """Draw right-hand 煥哥 instructor column with photo / avatar & quotes."""
    sx = WIDTH - 450
    sy = 150
    sw = 400
    sh = HEIGHT - 300
    
    # Sidebar Card Container
    draw_rounded_rect(draw, (sx, sy, sx + sw, sy + sh), radius=16, fill=COLORS["card_bg"], outline=COLORS["sky_blue"], width=2)
    
    # Sidebar Header
    draw_rounded_rect(draw, (sx, sy, sx + sw, sy + 60), radius=16, fill=COLORS["royal_blue"])
    draw.text((sx + 20, sy + 16), "👨‍🏫 煥哥 觀點 & 講師叮嚀", font=FONTS["sidebar_title"], fill=COLORS["white"])
    
    # Portrait / Avatar Image
    portrait = load_asset("huange_portrait.png", (140, 240))
    avatar = load_asset(avatar_name, (100, 128))
    
    if portrait:
        base_img.paste(portrait, (sx + 25, sy + 75))
    elif avatar:
        base_img.paste(avatar, (sx + 35, sy + 85))
        
    # Speech Callout Card on Right
    draw_rounded_rect(draw, (sx + 180, sy + 80, sx + sw - 15, sy + 320), radius=12, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
    draw.text((sx + 195, sy + 95), "【核心信條】", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
    
    # Bullets inside Speech Callout
    for i, b in enumerate(quote_bullets[:3]):
        py = sy + 135 + i * 58
        draw.text((sx + 195, py), f"• {b[:10]}", font=FONTS["card_body_bold"], fill=COLORS["dark_navy"])
        if len(b) > 10:
            draw.text((sx + 210, py + 26), b[10:], font=FONTS["card_body"], fill=COLORS["text_muted"])
            
    # Bottom Quote Box
    draw_rounded_rect(draw, (sx + 15, sy + 335, sx + sw - 15, sy + sh - 15), radius=10, fill=COLORS["gold_light"], outline=COLORS["gold_amber"], width=1)
    draw.text((sx + 25, sy + 350), f"🌟 {quote_title}", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])


# ==========================================
# SLIDE BUILDERS (1 ~ 10)
# ==========================================

def make_slide_01():
    """Slide 1: Cover Page (Grand Hero Banner with 煥哥 & Course Mission)"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    
    # Outer Main Card
    draw_rounded_rect(draw, (50, 40, WIDTH - 50, HEIGHT - 50), radius=20, fill=COLORS["card_bg"], outline=COLORS["royal_blue"], width=3)
    
    # Top Gold Tag
    draw_rounded_rect(draw, (100, 80, 480, 135), radius=14, fill=COLORS["gold_amber"])
    draw.text((120, 95), "AIIS 2026 · 旗艦專業全端資安課程", font=FONTS["header_tag"], fill=COLORS["dark_navy"])
    
    # Main Title
    draw.text((100, 160), "人工智慧與資訊安全", font=FONTS["cover_main"], fill=COLORS["royal_blue"])
    draw.text((100, 240), "AI and Information Security (AIIS)", font=FONTS["cover_sub"], fill=COLORS["sky_blue"])
    draw.text((100, 295), "Lesson 0 · 課程導論：AI 時代的世界觀與全學期實戰旅程", font=FONTS["cover_en"], fill=COLORS["dark_navy"])
    
    # 3 Pillar Cards
    pillars = [
        ("AI is Capability", "人工智慧是前所未有的強大能力\n放大認知、重構生產力與決策鏈", COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_welcome.png"),
        ("Security is Discipline", "資訊安全是不可妥協的工程紀律\n防禦邊界、保護隱私與資產韌性", COLORS["emerald_light"], COLORS["emerald"], "avatar_inspect.png"),
        ("Range · Lab · Code", "在靶場理解攻擊、在實驗室驗證\n在代碼中落實堅不可摧的防禦", COLORS["gold_light"], COLORS["gold_amber"], "avatar_laptop.png"),
    ]
    
    card_w = (WIDTH - 200 - 450 - 40) // 3
    start_y = 380
    for i, (title, desc, bg, fg, avatar_f) in enumerate(pillars):
        cx = 100 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 360), radius=16, fill=bg, outline=fg, width=2)
        
        # Header inside card
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 60), radius=16, fill=fg)
        draw.text((cx + 20, start_y + 16), title, font=FONTS["card_title"], fill=COLORS["white"])
        
        # Desc
        lines = desc.split("\n")
        draw.text((cx + 20, start_y + 85), lines[0], font=FONTS["card_body_bold"], fill=COLORS["dark_navy"])
        if len(lines) > 1:
            draw.text((cx + 20, start_y + 125), lines[1], font=FONTS["card_body"], fill=COLORS["text_muted"])
            
        # Avatar
        av = load_asset(avatar_f, (90, 115))
        if av:
            img.paste(av, (cx + card_w - 110, start_y + 225))

    # Right Instructor Column
    draw_huange_sidebar(img, draw, "「AI 提議，人類理解，資安驗證。」", [
        "AI 放大智慧認知能力",
        "資安捍衛系統邊界紀律",
        "親手打造真實監控中心"
    ], "avatar_welcome.png")

    # Bottom Banner
    draw_bottom_banner(draw, "AI proposes. Human understands. Security validates. (AI 提議，人類理解，資安驗證)", "全學期結合 CWA 氣象 Open Data、FastAPI、機器學習與多代理攻防實戰！")
    return img


def make_slide_02():
    """Slide 2: AI × InfoSec 核心思維 (雙軌對比)"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "為什麼 AI 時代更需要資安紀律？", "AI Capability vs. Security Discipline", "思維奠基 · 核心哲學", 2)
    
    # 2 Comparison Columns
    col_w = (WIDTH - 100 - 450 - 30) // 2
    
    # Left: AI Capability
    lx = 50
    draw_rounded_rect(draw, (lx, 150, lx + col_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=COLORS["sky_blue"], width=2)
    draw_rounded_rect(draw, (lx, 150, lx + col_w, 220), radius=16, fill=COLORS["sky_blue"])
    draw.text((lx + 24, 170), "🤖 AI is the Capability (極致能力)", font=FONTS["card_title"], fill=COLORS["white"])
    
    ai_points = [
        ("自主生成代碼與架構", "Coding Agents 快速建構複雜系統與微服務"),
        ("海量非結構化資料推論", "即時處理日誌、氣象與威脅情資進行推論"),
        ("多代理 (Multi-Agent) 協同", "自主調用外部工具、API 與資料庫完成任務"),
        ("強大但伴隨未知風險", "能力越強，攻擊者自動化滲透的威脅也同步放大")
    ]
    for i, (h, b) in enumerate(ai_points):
        py = 240 + i * 125
        draw_rounded_rect(draw, (lx + 20, py, lx + col_w - 20, py + 105), radius=12, fill=COLORS["sky_blue_light"], outline=COLORS["sky_blue"], width=1)
        draw.text((lx + 35, py + 16), f"• {h}", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
        draw.text((lx + 35, py + 54), b, font=FONTS["card_body"], fill=COLORS["text_muted"])

    # Right: Security Discipline
    rx = lx + col_w + 30
    draw_rounded_rect(draw, (rx, 150, rx + col_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=COLORS["emerald"], width=2)
    draw_rounded_rect(draw, (rx, 150, rx + col_w, 220), radius=16, fill=COLORS["emerald"])
    draw.text((rx + 24, 170), "🛡️ Security is Discipline (嚴謹紀律)", font=FONTS["card_title"], fill=COLORS["white"])
    
    sec_points = [
        ("零信任邊界防護 (Zero Trust)", "絕不盲目信任外部輸入、模型輸出與自主代理行為"),
        ("主動威脅建模 (Threat Model)", "預先辨識 Prompt Injection、資料外洩與中毒漏洞"),
        ("安全防禦機制驗證", "透過紅藍軍實戰演練與自動化 Guardrails 確保韌性"),
        ("守護企業與核心資產", "讓強大的 AI 系統在安全、合規且可受控的軌道上運作")
    ]
    for i, (h, b) in enumerate(sec_points):
        py = 240 + i * 125
        draw_rounded_rect(draw, (rx + 20, py, rx + col_w - 20, py + 105), radius=12, fill=COLORS["emerald_light"], outline=COLORS["emerald"], width=1)
        draw.text((rx + 35, py + 16), f"• {h}", font=FONTS["card_body_bold"], fill=COLORS["emerald"])
        draw.text((rx + 35, py + 54), b, font=FONTS["card_body"], fill=COLORS["text_muted"])

    # Right Sidebar
    draw_huange_sidebar(img, draw, "能力越大，防禦責任越重！", [
        "AI 帶來超高速產出",
        "資安確保系統不會翻車",
        "雙劍合璧才是現代高手"
    ], "avatar_explain.png")

    draw_bottom_banner(draw, "【核心結論】 AI 系統能力越強大，背後所需的資安架構、身分認證與驗證紀律就越關鍵！")
    return img


def make_slide_03():
    """Slide 3: 四大工業革命演進"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "四大工業革命演進：人類能力的維度放大", "Evolution of Four Industrial Revolutions", "歷史視角 · 時代演進", 3)
    
    revs = [
        ("第 1 次工業革命", "機械化與蒸汽動力", "放大「體力與機械力」", "取代人體與牲畜勞力\n開啟工廠規模化生產", COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_welcome.png"),
        ("第 2 次工業革命", "電力與石油能源", "放大「能量與規模」", "大規模流水線生產\n電網與跨區能源分發", COLORS["emerald_light"], COLORS["emerald"], "avatar_idea.png"),
        ("第 3 次資訊革命", "電腦與網際網路", "放大「資訊運算」", "軟體、資料庫與網路\n全球資訊毫秒級流通", COLORS["purple_light"], COLORS["purple"], "avatar_laptop.png"),
        ("第 4 次 AI 革命", "機器智慧與 Agent", "放大「認知與智慧」", "從資訊處理躍升至推理\n重構所有產業與安全邏輯", COLORS["gold_light"], COLORS["gold_amber"], "avatar_present.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 60) // 4
    for i, (name, core, amplify, desc, bg, fg, av_f) in enumerate(revs):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        # Header inside card
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 220), radius=16, fill=fg)
        draw.text((cx + 12, 172), name, font=FONTS["card_title"], fill=COLORS["white"])
        
        # Core Tech
        draw.text((cx + 16, 235), "核心驅動力：", font=FONTS["card_body"], fill=COLORS["text_muted"])
        draw.text((cx + 16, 265), core, font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
        
        # Amplify Box
        draw_rounded_rect(draw, (cx + 12, 330, cx + card_w - 12, 430), radius=10, fill=bg, outline=fg, width=1)
        draw.text((cx + 20, 345), "被放大的能力：", font=FONTS["card_body"], fill=COLORS["text_muted"])
        draw.text((cx + 20, 380), amplify, font=FONTS["card_body_bold"], fill=fg)
        
        # Desc
        lines = desc.split("\n")
        draw.text((cx + 16, 455), lines[0], font=FONTS["card_body"], fill=COLORS["dark_navy"])
        if len(lines) > 1:
            draw.text((cx + 16, 490), lines[1], font=FONTS["card_body"], fill=COLORS["text_muted"])
            
        # Avatar
        av = load_asset(av_f, (80, 100))
        if av:
            img.paste(av, (cx + card_w - 90, HEIGHT - 270))

    # Right Sidebar
    draw_huange_sidebar(img, draw, "每一次革命都放大一種能力！", [
        "蒸汽機放大肌肉力量",
        "電力放大能源規模",
        "電腦放大資訊運算",
        "AI 放大人類智慧大腦"
    ], "avatar_idea.png")

    draw_bottom_banner(draw, "【思考題】 蒸汽機放大力量，電力放大能源，電腦放大資訊，AI 放大的是「人類認知與智慧」！")
    return img


def make_slide_04():
    """Slide 4: AI 智慧三階段 ANI -> AGI -> ASI"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "AI 革命的三大智慧演進階段", "ANI vs. AGI vs. ASI Evolution", "概念辨析 · 演進路徑", 4)
    
    stages = [
        ("Phase 1: ANI", "專用人工智慧 (Narrow AI)", "我們目前所處的階段", [
            ("專精特定領域任務", "如圖像辨識、棋藝對弈、氣象預測模型"),
            ("資安主要挑戰", "對抗樣本攻擊、特徵偽造、資料中毒 (Poisoning)")
        ], COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_inspect.png"),
        
        ("Phase 2: AGI", "通用人工智慧 (General AI)", "即將跨越的關鍵里程碑", [
            ("具備跨領域綜合認知", "同等人類水準的自主學習與長鏈路推理"),
            ("資安主要挑戰", "目標對齊 (Alignment)、意圖劫持、邊界失效")
        ], COLORS["purple_light"], COLORS["purple"], "avatar_laptop.png"),
        
        ("Phase 3: ASI", "超級人工智慧 (Super AI)", "未來的極致願景與挑戰", [
            ("全面超越人類智慧總和", "在科學研究、策略規劃具備超人類創造力"),
            ("資安主要挑戰", "存在性風險 (Existential Risk)、全域安全治理")
        ], COLORS["gold_light"], COLORS["gold_amber"], "avatar_present.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 40) // 3
    for i, (title, sub, status, points, bg, fg, av_f) in enumerate(stages):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        # Header inside card
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 16, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 16, 198), sub, font=FONTS["card_body"], fill=COLORS["white"])
        
        # Status
        draw_rounded_rect(draw, (cx + 16, 250, cx + card_w - 16, 295), radius=8, fill=bg, outline=fg, width=1)
        draw.text((cx + 25, 262), f"📌 當前狀態：{status}", font=FONTS["card_body_bold"], fill=fg)
        
        # Points
        for j, (ph, pb) in enumerate(points):
            py = 315 + j * 160
            draw_rounded_rect(draw, (cx + 16, py, cx + card_w - 16, py + 140), radius=12, fill=COLORS["canvas_bg"], outline=COLORS["border_light"], width=1)
            draw.text((cx + 26, py + 16), f"• {ph}：", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
            draw.text((cx + 26, py + 56), pb, font=FONTS["card_body"], fill=COLORS["text_muted"])
            
        # Avatar
        av = load_asset(av_f, (80, 100))
        if av:
            img.paste(av, (cx + card_w - 90, HEIGHT - 270))

    # Right Sidebar
    draw_huange_sidebar(img, draw, "越往 AGI 前進，安全越不能馬虎！", [
        "ANI 守護單點模型漏洞",
        "AGI 需防禦自主意圖失控",
        "安全架構必須超前部署"
    ], "avatar_laptop.png")

    draw_bottom_banner(draw, "【演進路徑】 ANI (專用) -> AGI (通用) -> ASI (超級) ；AI 能力跨越越大，安全治理越早需確立！")
    return img


def make_slide_05():
    """Slide 5: 現代 AI 三大能力維度 (Discriminative -> Generative -> Agentic)"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "現代 AI 的三大核心能力維度", "Discriminative vs. Generative vs. Agentic", "技術分類 · 行為特徵", 5)
    
    types = [
        ("判別式 AI (Discriminative)", "ANALYZE & PREDICT", "分析、分類與預測", [
            ("核心數學", "學習條件機率 P(Y|X)，進行特徵分類與預測"),
            ("代表技術", "Random Forest, SVM, CNN, 異常偵測演算法"),
            ("資安應用", "惡意郵件過濾、DDoS 流量識別、入侵偵測 (IDS)")
        ], COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_inspect.png"),
        
        ("生成式 AI (Generative)", "CREATE & SYNTHESIZE", "生成、補全與重構", [
            ("核心數學", "學習聯合機率 P(X)，創造全新文字、代碼與圖像"),
            ("代表技術", "LLM (Gemini, ChatGPT), Diffusion, CodeGen"),
            ("資安應用", "自動生成安全審計報告、代碼補丁、威脅情資摘要")
        ], COLORS["emerald_light"], COLORS["emerald"], "avatar_explain.png"),
        
        ("代理式 AI (Agentic AI)", "PLAN & ACTUATE", "自主規劃與工具調用", [
            ("核心架構", "目標導向、環境感知、工具調用 (Tool Use) 與記憶閉環"),
            ("代表技術", "Multi-Agent 協同、Coding Agents、自主工作流"),
            ("資安應用", "自動化滲透測試、即時安全事件回應與自動修復")
        ], COLORS["purple_light"], COLORS["purple"], "avatar_laptop.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 40) // 3
    for i, (title, action, sub, points, bg, fg, av_f) in enumerate(types):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 16, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 16, 198), f"{action} · {sub}", font=FONTS["card_body"], fill=COLORS["white"])
        
        for j, (ph, pb) in enumerate(points):
            py = 250 + j * 150
            draw_rounded_rect(draw, (cx + 16, py, cx + card_w - 16, py + 130), radius=12, fill=bg, outline=fg, width=1)
            draw.text((cx + 26, py + 16), f"• {ph}：", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
            draw.text((cx + 26, py + 56), pb, font=FONTS["card_body"], fill=COLORS["text_muted"])
            
        av = load_asset(av_f, (80, 100))
        if av:
            img.paste(av, (cx + card_w - 90, HEIGHT - 270))

    draw_huange_sidebar(img, draw, "從「分析」到「生成」再到「行動」！", [
        "判別式 AI 是防禦之眼",
        "生成式 AI 是效率之手",
        "代理式 AI 是全自動指揮官"
    ], "avatar_explain.png")

    draw_bottom_banner(draw, "【核心洞察】 AI 自主性越高（從分析到行動），安全防禦面越廣，必須導入完整的治理體系！")
    return img


def make_slide_06():
    """Slide 6: 資安核心四要素 (Asset, Threat, Vulnerability, Risk)"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "資訊安全核心四要素與風險分析架構", "Asset, Threat, Vulnerability, Risk Framework", "資安基石 · 威脅模型", 6)
    
    elements = [
        ("1. 資產 (Asset)", "我們需要保護什麼？", [
            "系統服務與運算資源",
            "核心資料庫與 API 金鑰",
            "專有模型權重與 Prompt",
            "使用者隱私與商務機密"
        ], COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_welcome.png"),
        
        ("2. 威脅 (Threat)", "誰或什麼會造成危害？", [
            "外部惡意駭客與攻擊者",
            "Prompt Injection 注入",
            "敏感資料外洩與爬蟲",
            "供應鏈套件惡意篡改"
        ], COLORS["rose_light"], COLORS["rose_red"], "avatar_inspect.png"),
        
        ("3. 弱點 (Vuln)", "系統存在哪些漏洞？", [
            "缺乏輸入驗證過濾機制",
            "敏感設定檔硬編碼外洩",
            "權限配置失誤 (Broken Auth)",
            "未加防護的模型邊界"
        ], COLORS["gold_light"], COLORS["gold_amber"], "avatar_laptop.png"),
        
        ("4. 風險 (Risk)", "損失機率與衝擊程度？", [
            "威脅利用弱點之可能性",
            "資產受損之衝擊程度",
            "財務、法律與信譽損失",
            "需透過安全控制降至可控"
        ], COLORS["purple_light"], COLORS["purple"], "avatar_present.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 60) // 4
    for i, (title, sub, bullets, bg, fg, av_f) in enumerate(elements):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 12, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 12, 198), sub, font=FONTS["card_body"], fill=COLORS["white"])
        
        for j, b in enumerate(bullets):
            py = 250 + j * 95
            draw_rounded_rect(draw, (cx + 12, py, cx + card_w - 12, py + 80), radius=10, fill=bg, outline=COLORS["border_light"], width=1)
            draw.text((cx + 20, py + 26), f"• {b}", font=FONTS["card_body_bold"], fill=COLORS["dark_navy"])

    draw_huange_sidebar(img, draw, "資安不是憑感覺，是有公式的！", [
        "Risk = Threat × Vuln × Impact",
        "沒有弱點，威脅就無法得逞",
        "保護核心資產是最高原則"
    ], "avatar_inspect.png")

    draw_bottom_banner(draw, "【風險公式】 Risk (風險) = Threat (威脅) × Vulnerability (弱點) × Asset Impact (資產衝擊)")
    return img


def make_slide_07():
    """Slide 7: CIA Triad 資安黃金三角"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "資訊安全黃金三角：CIA Triad 在 AI 系統中的意義", "Confidentiality, Integrity, Availability Triad", "經典架構 · AI 映射", 7)
    
    pillars = [
        ("C · Confidentiality", "機密性 (秘密不被窺探)", "確保只有授權實體能存取敏感資料與模型資產", [
            ("傳統資安基礎", "加密傳輸、存取控制 (RBAC)、敏感資訊去識別化"),
            ("AI 系統新威脅", "防止 Training Data 被逆向提取 (Membership Inference)"),
            ("實戰防護重點", "保護 System Prompt 與私有 RAG 向量知識庫")
        ], COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_welcome.png"),
        
        ("I · Integrity", "完整性 (資料不被篡改)", "確保數據、模型與指令在傳輸與運算中未遭破壞", [
            ("傳統資安基礎", "數位簽章、雜湊校驗 (Hash)、防範中間人篡改 (MITM)"),
            ("AI 系統新威脅", "防止訓練資料集遭投毒 (Data Poisoning) 產生後門"),
            ("實戰防護重點", "驗證模型輸出真實性、防止 Prompt Injection 竄改邏輯")
        ], COLORS["emerald_light"], COLORS["emerald"], "avatar_inspect.png"),
        
        ("A · Availability", "可用性 (服務隨時可用)", "確保授權使用者在需要時能即時存取系統服務", [
            ("傳統資安基礎", "DDoS 流量清洗、負載平衡、備援容錯架構"),
            ("AI 系統新威脅", "防止消耗性 Prompt 攻擊導致 GPU 算力耗盡 (DoS)"),
            ("實戰防護重點", "API 速率限制 (Rate Limiting)、超時熔斷與彈性擴展")
        ], COLORS["purple_light"], COLORS["purple"], "avatar_laptop.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 40) // 3
    for i, (title, sub, defn, points, bg, fg, av_f) in enumerate(pillars):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 16, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 16, 198), sub, font=FONTS["card_body"], fill=COLORS["white"])
        
        for j, (ph, pb) in enumerate(points):
            py = 250 + j * 150
            draw_rounded_rect(draw, (cx + 16, py, cx + card_w - 16, py + 130), radius=12, fill=bg, outline=fg, width=1)
            draw.text((cx + 26, py + 16), f"• {ph}：", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
            draw.text((cx + 26, py + 56), pb, font=FONTS["card_body"], fill=COLORS["text_muted"])

    draw_huange_sidebar(img, draw, "CIA 是所有資安工程師的共同語言！", [
        "C：不該看的看不到",
        "I：不該改的改不掉",
        "A：該用的時候用得到"
    ], "avatar_explain.png")

    draw_bottom_banner(draw, "【資安基石】 CIA 是資安的永恆基石：在 AI 時代，我們將這三大原則拓展至模型、數據與代理架構！")
    return img


def make_slide_08():
    """Slide 8: 貫穿專題 AI Weather Security Center"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "貫穿全學期的實戰專題：AI Weather Security Center", "AI Weather Security Center Master Project", "實戰專案 · 系統架構", 8)
    
    sections = [
        ("1. 真實資料源串接", "中央氣象署 CWA Open Data", [
            ("即時氣象與預警 API", "真實世界數據流、API Key 認證管理"),
            ("數據清洗與持久化", "SQLite / PostgreSQL 資料庫架構設計")
        ], COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_welcome.png"),
        
        ("2. 全端系統與 AI 核心", "FastAPI + ML + Multi-Agent", [
            ("高效後端服務", "RESTful API、JWT 身分驗證與權限控制"),
            ("AI 威脅分析引擎", "機器學習異常偵測 + LLM 自動生成報告")
        ], COLORS["emerald_light"], COLORS["emerald"], "avatar_laptop.png"),
        
        ("3. 攻防實戰與防禦加固", "Range -> Lab -> Code", [
            ("紅軍滲透攻擊測試", "Prompt Injection、越獄與 API 破壞演練"),
            ("藍軍防禦加固工程", "Guardrails 護欄、鑑識日誌與 OWASP Top 10")
        ], COLORS["purple_light"], COLORS["purple"], "avatar_inspect.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 40) // 3
    for i, (title, sub, points, bg, fg, av_f) in enumerate(sections):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 16, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 16, 198), sub, font=FONTS["card_body"], fill=COLORS["white"])
        
        for j, (ph, pb) in enumerate(points):
            py = 260 + j * 180
            draw_rounded_rect(draw, (cx + 16, py, cx + card_w - 16, py + 155), radius=12, fill=bg, outline=fg, width=1)
            draw.text((cx + 26, py + 20), f"• {ph}：", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
            draw.text((cx + 26, py + 65), pb, font=FONTS["card_body"], fill=COLORS["text_muted"])

    draw_huange_sidebar(img, draw, "親手打造一套商業級監控中心！", [
        "不只是跑 Demo 玩具",
        "真實資料、真實後端",
        "親身經歷完整產品生命週期"
    ], "avatar_laptop.png")

    draw_bottom_banner(draw, "【專題特色】 親手打造具備商業級防禦能力的真實 AI 資安監控中心，完整經歷產品生命週期！")
    return img


def make_slide_09():
    """Slide 9: 全學期學習路徑五大篇章"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "全學期學習路徑：五大核心演進階段", "BUILD -> LEARN -> ATTACK -> DEFEND -> GOVERN", "課程地圖 · 成長路徑", 9)
    
    steps = [
        ("1. BUILD", "系統建置", "L1-L3", "工具箱整備\n氣象中心基礎\n專案威脅建模", COLORS["sky_blue_light"], COLORS["sky_blue"]),
        ("2. LEARN", "機器學習", "L4-L7", "監督式分類\n無監督異常偵測\n深度學習特徵", COLORS["emerald_light"], COLORS["emerald"]),
        ("3. ATTACK", "攻防實戰", "L8-L10", "提示詞注入攻擊\n越獄與模型逆向\n多模態威脅滲透", COLORS["rose_light"], COLORS["rose_red"]),
        ("4. DEFEND", "防禦加固", "L11-L14", "Guardrails 護欄\nAPI 鑑識日誌\n自動化補丁修復", COLORS["purple_light"], COLORS["purple"]),
        ("5. GOVERN", "治理合規", "L15-L16", "OWASP Top 10\nAI 倫理與法規\n期末成果評測", COLORS["gold_light"], COLORS["gold_amber"]),
    ]
    
    card_w = (WIDTH - 100 - 450 - 80) // 5
    for i, (title, name, lessons, desc, bg, fg) in enumerate(steps):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 12, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 12, 198), f"{name} ({lessons})", font=FONTS["card_body"], fill=COLORS["white"])
        
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            py = 260 + j * 95
            draw_rounded_rect(draw, (cx + 10, py, cx + card_w - 10, py + 80), radius=10, fill=bg, outline=COLORS["border_light"], width=1)
            draw.text((cx + 18, py + 26), f"• {line}", font=FONTS["card_body_bold"], fill=COLORS["dark_navy"])

    draw_huange_sidebar(img, draw, "循序漸進，成為全方位專家！", [
        "先學會蓋系統 (BUILD)",
        "再掌握演算法 (LEARN)",
        "學會打 (ATTACK) 才能防 (DEFEND)"
    ], "avatar_present.png")

    draw_bottom_banner(draw, "【成長旅程】 BUILD -> LEARN -> ATTACK -> DEFEND -> GOVERN，每一步都有可運行的真實代碼與靶場！")
    return img


def make_slide_10():
    """Slide 10: 課程公約與三大實踐信條"""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["canvas_bg"])
    draw = ImageDraw.Draw(img)
    draw_header(draw, "課程核心公約與三大實踐信條", "Three Principles: Range, Lab, Code", "課堂公約 · 行動起點", 10)
    
    creeds = [
        ("Learn it in the Range", "在靶場理解威脅本質", [
            "不只聽理論，在安全的靶場中實際觀察漏洞如何被利用",
            "洞悉駭客的思維模式與攻擊路徑"
        ], COLORS["rose_light"], COLORS["rose_red"], "avatar_inspect.png"),
        
        ("Prove it in our Lab", "在實驗室驗證防護效果", [
            "透過數據、測試腳本與科學指標評估防禦機制",
            "精準量化 Guardrails 的準確率與召回率"
        ], COLORS["sky_blue_light"], COLORS["sky_blue"], "avatar_laptop.png"),
        
        ("Fix it in our Code", "在代碼中落實堅韌防禦", [
            "資安的最終落點永遠是高質量的工程代碼",
            "在後端、資料庫與模型管線中直接實作修復方案"
        ], COLORS["emerald_light"], COLORS["emerald"], "avatar_welcome.png"),
    ]
    
    card_w = (WIDTH - 100 - 450 - 40) // 3
    for i, (title, sub, bullets, bg, fg, av_f) in enumerate(creeds):
        cx = 50 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, 150, cx + card_w, HEIGHT - 150), radius=16, fill=COLORS["card_bg"], outline=fg, width=2)
        
        draw_rounded_rect(draw, (cx, 150, cx + card_w, 230), radius=16, fill=fg)
        draw.text((cx + 16, 165), title, font=FONTS["card_title"], fill=COLORS["white"])
        draw.text((cx + 16, 198), sub, font=FONTS["card_body"], fill=COLORS["white"])
        
        for j, b in enumerate(bullets):
            py = 260 + j * 160
            draw_rounded_rect(draw, (cx + 16, py, cx + card_w - 16, py + 140), radius=12, fill=bg, outline=fg, width=1)
            draw.text((cx + 26, py + 20), "• 實踐要點：", font=FONTS["card_body_bold"], fill=COLORS["royal_blue"])
            draw.text((cx + 26, py + 65), b, font=FONTS["card_body"], fill=COLORS["text_muted"])

    draw_huange_sidebar(img, draw, "準備好一起踏上這趟旅程了嗎？", [
        "下一課：AIIS_L1 工具箱",
        "Gemini + Antigravity + Prompt",
        "打造你的第一個 AI 資安工作流"
    ], "avatar_welcome.png")

    draw_bottom_banner(draw, "【行動綱領】 歡迎加入 AIIS！從現在開始，展開你的 AI × 資訊安全大師之旅！")
    return img


def main():
    generators = [
        ("slide_01.png", make_slide_01),
        ("slide_02.png", make_slide_02),
        ("slide_03.png", make_slide_03),
        ("slide_04.png", make_slide_04),
        ("slide_05.png", make_slide_05),
        ("slide_06.png", make_slide_06),
        ("slide_07.png", make_slide_07),
        ("slide_08.png", make_slide_08),
        ("slide_09.png", make_slide_09),
        ("slide_10.png", make_slide_10),
    ]
    
    print("🎨 Generating 10 Vibrant Presentation Images matching pptsample.png...")
    for filename, fn in generators:
        img = fn()
        out_course = os.path.join(OUTPUT_DIR_COURSE, filename)
        out_root = os.path.join(OUTPUT_DIR_ROOT, filename)
        img.save(out_course, "PNG", quality=95)
        img.save(out_root, "PNG", quality=95)
        print(f" ✨ Saved: {out_course}")
        
    print("\n✅ All 10 vibrant pptsample-style slides generated successfully!")


if __name__ == "__main__":
    main()
