#!/usr/bin/env python3
"""
Generate Slide 1 (Cover / Overview) in 4 Distinct Visual Styles:
1. Type 1: pptsample.png / Excalidraw Infographic + 煥哥 Full-Height Portrait & Avatars
2. Type 2: Canva 繽紛資訊圖卡風 (Vibrant Colorful Card Grid + Modern Pills)
3. Type 3: 未來科技深色霓虹資安風 (Cybersecurity Dark Neon Glow)
4. Type 4: 現代旗艦商務極簡風 (Swiss Clean Executive)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
OUTPUT_DIR_COURSE = os.path.join(BASE_DIR, "slides_images")
OUTPUT_DIR_ROOT = os.path.abspath("slides_images")

os.makedirs(OUTPUT_DIR_COURSE, exist_ok=True)
os.makedirs(OUTPUT_DIR_ROOT, exist_ok=True)

WIDTH = 1920
HEIGHT = 1080

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT_PATH = "/System/Library/Fonts/STHeiti Light.ttc"

FONTS = {
    "title_hero": ImageFont.truetype(FONT_PATH, 54),
    "title_sub": ImageFont.truetype(FONT_PATH, 28),
    "title_en": ImageFont.truetype(FONT_PATH, 22),
    "card_title": ImageFont.truetype(FONT_PATH, 26),
    "card_bold": ImageFont.truetype(FONT_PATH, 20),
    "card_body": ImageFont.truetype(FONT_PATH, 17),
    "badge": ImageFont.truetype(FONT_PATH, 18),
    "slogan_bold": ImageFont.truetype(FONT_PATH, 22),
    "slogan_sub": ImageFont.truetype(FONT_PATH, 17),
    "footer": ImageFont.truetype(FONT_LIGHT_PATH, 14),
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


def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


# =========================================================================
# TYPE 1: pptsample.png / Excalidraw + 煥哥 Full-Height Portrait & Avatars
# =========================================================================
def make_type_1():
    img = Image.new("RGB", (WIDTH, HEIGHT), (248, 250, 252))
    draw = ImageDraw.Draw(img)
    
    # Outer Border Box
    draw_rounded_rect(draw, (40, 30, WIDTH - 40, HEIGHT - 35), radius=20, fill=(255, 255, 255), outline=(11, 79, 156), width=3)
    
    # Top Gold Tag
    draw_rounded_rect(draw, (80, 60, 460, 110), radius=14, fill=(245, 158, 11))
    draw.text((100, 72), "AIIS 2026 · 旗艦專業全端資安課程", font=FONTS["badge"], fill=(15, 23, 42))
    
    # Titles
    draw.text((80, 130), "人工智慧與資訊安全", font=FONTS["title_hero"], fill=(11, 79, 156))
    draw.text((80, 200), "AI and Information Security (AIIS)", font=FONTS["title_sub"], fill=(2, 132, 199))
    draw.text((80, 250), "Lesson 0 · 課程導論：AI 時代的世界觀與全學期實戰旅程", font=FONTS["title_en"], fill=(15, 23, 42))
    
    # 3 Infographic Pillar Cards
    pillars = [
        ("AI is Capability", "人工智慧是前所未有的強大能力\n放大認知、重構生產力與決策鏈", (224, 242, 254), (2, 132, 199), "avatar_welcome.png"),
        ("Security is Discipline", "資訊安全是不可妥協的工程紀律\n防禦邊界、保護隱私與資產韌性", (209, 250, 229), (16, 185, 129), "avatar_inspect.png"),
        ("Range · Lab · Code", "在靶場理解攻擊、在實驗室驗證\n在代碼中落實堅不可摧的防禦", (254, 243, 199), (245, 158, 11), "avatar_laptop.png"),
    ]
    
    card_w = (WIDTH - 160 - 450 - 40) // 3
    start_y = 330
    for i, (title, desc, bg, fg, avatar_f) in enumerate(pillars):
        cx = 80 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 440), radius=16, fill=bg, outline=fg, width=2)
        
        # Header inside card
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 65), radius=16, fill=fg)
        draw.text((cx + 18, start_y + 18), title, font=FONTS["card_title"], fill=(255, 255, 255))
        
        lines = desc.split("\n")
        draw.text((cx + 20, start_y + 95), lines[0], font=FONTS["card_bold"], fill=(15, 23, 42))
        if len(lines) > 1:
            draw.text((cx + 20, start_y + 145), lines[1], font=FONTS["card_body"], fill=(71, 85, 105))
            
        av = load_asset(avatar_f, (110, 140))
        if av:
            img.paste(av, (cx + card_w - 130, start_y + 275))

    # Right Instructor Column
    sx = WIDTH - 470
    sy = 60
    sw = 410
    sh = HEIGHT - 220
    draw_rounded_rect(draw, (sx, sy, sx + sw, sy + sh), radius=16, fill=(255, 255, 255), outline=(2, 132, 199), width=2)
    draw_rounded_rect(draw, (sx, sy, sx + sw, sy + 60), radius=16, fill=(11, 79, 156))
    draw.text((sx + 35, sy + 16), "【講師觀點 & 核心叮嚀】", font=FONTS["card_title"], fill=(255, 255, 255))
    
    portrait = load_asset("huange_portrait.png", (140, 240))
    if portrait:
        img.paste(portrait, (sx + 20, sy + 75))
        
    draw_rounded_rect(draw, (sx + 175, sy + 75, sx + sw - 15, sy + 315), radius=12, fill=(224, 242, 254), outline=(2, 132, 199), width=1)
    draw.text((sx + 190, sy + 90), "【核心信條】", font=FONTS["card_bold"], fill=(11, 79, 156))
    draw.text((sx + 190, sy + 135), "• AI 提議", font=FONTS["card_bold"], fill=(15, 23, 42))
    draw.text((sx + 190, sy + 180), "• 人類理解", font=FONTS["card_bold"], fill=(15, 23, 42))
    draw.text((sx + 190, sy + 225), "• 資安驗證", font=FONTS["card_bold"], fill=(15, 23, 42))
    
    draw_rounded_rect(draw, (sx + 15, sy + 330, sx + sw - 15, sy + sh - 15), radius=10, fill=(254, 243, 199), outline=(245, 158, 11), width=1)
    draw.text((sx + 24, sy + 348), "「在靶場理解攻擊，在代碼中落實防禦！」", font=FONTS["card_bold"], fill=(11, 79, 156))

    # Bottom Banner
    draw_rounded_rect(draw, (80, HEIGHT - 145, WIDTH - 80, HEIGHT - 55), radius=12, fill=(254, 243, 199), outline=(245, 158, 11), width=2)
    draw_rounded_rect(draw, (100, HEIGHT - 132, 210, HEIGHT - 68), radius=8, fill=(245, 158, 11))
    draw.text((115, HEIGHT - 108), "重點洞察", font=FONTS["badge"], fill=(15, 23, 42))
    draw.text((230, HEIGHT - 122), "AI proposes. Human understands. Security validates. (AI 提議，人類理解，資安驗證)", font=FONTS["slogan_bold"], fill=(11, 79, 156))
    draw.text((230, HEIGHT - 84), "全學期結合中央氣象署 CWA Open Data、FastAPI、機器學習與多代理攻防實戰！", font=FONTS["slogan_sub"], fill=(15, 23, 42))

    return img


# =========================================================================
# TYPE 2: Canva 繽紛資訊圖卡風 (Vibrant Colorful Card Grid + Modern Badges)
# =========================================================================
def make_type_2():
    img = Image.new("RGB", (WIDTH, HEIGHT), (241, 245, 249))
    draw = ImageDraw.Draw(img)
    
    # Top Vibrant Gradient Header Bar
    draw_rounded_rect(draw, (40, 30, WIDTH - 40, 200), radius=20, fill=(15, 23, 42))
    draw.rectangle([(40, 30), (WIDTH - 40, 42)], fill=(245, 158, 11))
    
    # Header Tags
    draw_rounded_rect(draw, (70, 60, 270, 95), radius=10, fill=(37, 99, 235))
    draw.text((85, 68), "【AIIS 2026 旗艦課程】", font=FONTS["badge"], fill=(255, 255, 255))
    
    draw_rounded_rect(draw, (285, 60, 485, 95), radius=10, fill=(16, 185, 129))
    draw.text((300, 68), "【全端資安實戰】", font=FONTS["badge"], fill=(255, 255, 255))
    
    # Header Title
    draw.text((70, 115), "人工智慧與資訊安全 · 導論與世界觀", font=FONTS["title_hero"], fill=(255, 255, 255))
    draw.text((WIDTH - 480, 125), "AI and Information Security", font=FONTS["title_sub"], fill=(147, 197, 253))
    
    # 4 Vibrant Grid Cards
    cards = [
        ("AI 認知能力革命", "從蒸汽機到機器智慧", "AI 放大的是人類的智慧與認知能力。\n從判別式、生成式到代理式 AI，重構軟體與產業生產力！", (239, 246, 255), (37, 99, 235), "avatar_idea.png"),
        ("資安邊界紀律", "Zero Trust 零信任架構", "絕不盲目信任模型輸出與外來提示詞。\n預先進行威脅建模，消弭漏洞，守護關鍵資料與系統資產！", (236, 253, 245), (16, 185, 129), "avatar_inspect.png"),
        ("氣象資安中心專案", "CWA Open Data × FastAPI", "以中央氣象署真實 API 為核心，\n親手打造包含身分驗證、ML 異常偵測與自動化防禦的監控中心！", (255, 247, 237), (234, 88, 12), "avatar_laptop.png"),
        ("五大實戰篇章", "BUILD -> DEFEND -> GOVERN", "從系統建置 (BUILD)、機器學習 (LEARN)、\n攻防實戰 (ATTACK) 到防禦加固 (DEFEND) 與治理 (GOVERN)！", (250, 245, 255), (147, 51, 234), "avatar_present.png"),
    ]
    
    gw = (WIDTH - 110) // 2
    gh = 300
    coords = [
        (40, 250),
        (40 + gw + 30, 250),
        (40, 580),
        (40 + gw + 30, 580)
    ]
    
    for i, (title, tag, body, bg, border_c, av_f) in enumerate(cards):
        gx, gy = coords[i]
        draw_rounded_rect(draw, (gx, gy, gx + gw, gy + gh), radius=18, fill=(255, 255, 255), outline=border_c, width=2)
        
        # Color bar on top
        draw_rounded_rect(draw, (gx, gy, gx + gw, gy + 55), radius=18, fill=bg)
        draw.text((gx + 25, gy + 15), title, font=FONTS["card_title"], fill=border_c)
        
        # Tag
        draw_rounded_rect(draw, (gx + 25, gy + 75, gx + 250, gy + 110), radius=8, fill=bg, outline=border_c, width=1)
        draw.text((gx + 35, gy + 82), f"【{tag}】", font=FONTS["card_body"], fill=border_c)
        
        # Body text
        lines = body.split("\n")
        draw.text((gx + 25, gy + 130), lines[0], font=FONTS["card_bold"], fill=(15, 23, 42))
        if len(lines) > 1:
            draw.text((gx + 25, gy + 175), lines[1], font=FONTS["card_body"], fill=(71, 85, 105))

    # Bottom Full Width Bar
    draw_rounded_rect(draw, (40, HEIGHT - 160, WIDTH - 40, HEIGHT - 35), radius=14, fill=(15, 23, 42))
    draw.text((70, HEIGHT - 125), "【課程實踐守則】 Learn it in the Range · Prove it in our Lab · Fix it in our Code", font=FONTS["slogan_bold"], fill=(245, 158, 11))
    draw.text((70, HEIGHT - 80), "在靶場洞悉威脅本質，在實驗室數據化驗證，在代碼中建構具備真正韌性的 AI 系統！", font=FONTS["slogan_sub"], fill=(255, 255, 255))
    
    return img


# =========================================================================
# TYPE 3: 未來科技深色霓虹資安風 (Cybersecurity Dark Neon Glow)
# =========================================================================
def make_type_3():
    img = Image.new("RGB", (WIDTH, HEIGHT), (10, 15, 29))
    draw = ImageDraw.Draw(img)
    
    # Outer Tech Card
    draw_rounded_rect(draw, (40, 30, WIDTH - 40, HEIGHT - 35), radius=20, fill=(15, 23, 42), outline=(0, 242, 254), width=2)
    
    # Neon Top Bar
    draw.rectangle([(40, 30), (WIDTH - 40, 36)], fill=(0, 242, 254))
    
    # Tag
    draw_rounded_rect(draw, (80, 65, 380, 105), radius=10, fill=(20, 30, 55), outline=(0, 242, 254), width=1)
    draw.text((95, 74), "[ CYBERSECURITY × AI 2026 ]", font=FONTS["badge"], fill=(0, 242, 254))
    
    # Main Hero Title
    draw.text((80, 130), "人工智慧與資訊安全 (AIIS)", font=FONTS["title_hero"], fill=(255, 255, 255))
    draw.text((80, 205), "AI is the Capability · Information Security is the Discipline", font=FONTS["title_sub"], fill=(0, 242, 254))
    
    # 3 Dark Cyber Cards
    cards = [
        ("01 / CAPABILITY", "AI 認知運算", "機器智慧、LLM 代理與自動化工作流\n重塑軟體工程與認知決策鏈", (0, 242, 254)),
        ("02 / DISCIPLINE", "資安防禦工程", "零信任邊界、Prompt 注入防護與漏洞修補\n保護關鍵模型權重與機密資料庫", (16, 185, 129)),
        ("03 / VALIDATION", "實戰攻防靶場", "CWA 氣象 Open Data 整合全端監控中心\nRange -> Lab -> Code 完整驗證閉環", (245, 158, 11)),
    ]
    
    card_w = (WIDTH - 160 - 40) // 3
    start_y = 290
    for i, (num, head, desc, neon_col) in enumerate(cards):
        cx = 80 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 440), radius=16, fill=(18, 28, 51), outline=neon_col, width=2)
        
        # Header inside card
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 70), radius=16, fill=(25, 38, 68))
        draw.text((cx + 25, start_y + 22), num, font=FONTS["card_title"], fill=neon_col)
        
        # Head
        draw.text((cx + 25, start_y + 100), head, font=FONTS["title_sub"], fill=(255, 255, 255))
        
        # Lines
        lines = desc.split("\n")
        draw.text((cx + 25, start_y + 170), lines[0], font=FONTS["card_bold"], fill=(226, 232, 240))
        if len(lines) > 1:
            draw.text((cx + 25, start_y + 225), lines[1], font=FONTS["card_body"], fill=(148, 163, 184))
            
        # Tech decorative icon box
        draw_rounded_rect(draw, (cx + 25, start_y + 320, cx + card_w - 25, start_y + 400), radius=10, fill=(10, 15, 29), outline=(40, 60, 95), width=1)
        draw.text((cx + 40, start_y + 348), "STATUS: ACTIVE / ARMED", font=FONTS["badge"], fill=neon_col)

    # Bottom Terminal Banner
    draw_rounded_rect(draw, (80, HEIGHT - 270, WIDTH - 80, HEIGHT - 55), radius=14, fill=(10, 15, 29), outline=(0, 242, 254), width=1)
    draw.text((110, HEIGHT - 235), "$ aais-security --init --mode=defend", font=FONTS["card_title"], fill=(0, 242, 254))
    draw.text((110, HEIGHT - 180), "AI proposes. Human understands. Security validates. (AI 提議，人類理解，資安驗證)", font=FONTS["slogan_bold"], fill=(255, 255, 255))
    draw.text((110, HEIGHT - 130), "從現在開始，掌握 AI 與資安雙重思維，成為未來的全能資安架構師！", font=FONTS["slogan_sub"], fill=(148, 163, 184))
    
    return img


# =========================================================================
# TYPE 4: 現代旗艦商務極簡風 (Swiss Clean Executive)
# =========================================================================
def make_type_4():
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Accent Blue Bar
    draw.rectangle([(0, 0), (WIDTH, 12)], fill=(11, 79, 156))
    
    # Outer Clean Frame
    draw_rounded_rect(draw, (60, 50, WIDTH - 60, HEIGHT - 50), radius=16, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    
    # Hero Title Block
    draw_rounded_rect(draw, (100, 90, 420, 135), radius=6, fill=(239, 246, 255), outline=(191, 219, 254), width=1)
    draw.text((120, 102), "AIIS 2026 · 國立臺灣大學旗艦課程", font=FONTS["badge"], fill=(37, 99, 235))
    
    draw.text((100, 165), "人工智慧與資訊安全", font=FONTS["title_hero"], fill=(15, 23, 42))
    draw.text((100, 240), "AI and Information Security — Course Orientation", font=FONTS["title_sub"], fill=(71, 85, 105))
    draw.text((100, 290), "Lesson 0 · 建立 AI 時代的世界觀：能力邊界、威脅模型與全學期專案", font=FONTS["title_en"], fill=(100, 116, 139))
    
    # 3 Clean Executive Cards
    cards = [
        ("01 / AI 能力維度", "Artificial Intelligence", "從傳統機器學習分類，到 LLM 生成與 Multi-Agent 自主工作流。\nAI 賦予了我們前所未有的強大生產力與運算效率。", (37, 99, 235)),
        ("02 / 資安工程紀律", "Information Security", "零信任架構、輸入驗證、Guardrails 護欄與漏洞修復。\n資訊安全是守護系統資產與隱私邊界的根本紀律。", (16, 185, 129)),
        ("03 / 全學期實戰專題", "AI Weather Security Center", "串接中央氣象署 (CWA) Open Data，親手打造全端監控系統。\n經歷 BUILD -> LEARN -> ATTACK -> DEFEND -> GOVERN 全流程。", (217, 119, 6)),
    ]
    
    card_w = (WIDTH - 200 - 40) // 3
    start_y = 360
    for i, (head, en_sub, body, accent_c) in enumerate(cards):
        cx = 100 + i * (card_w + 20)
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 400), radius=12, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
        
        # Accent Top Strip
        draw_rounded_rect(draw, (cx, start_y, cx + card_w, start_y + 8), radius=4, fill=accent_c)
        
        # Title
        draw.text((cx + 30, start_y + 35), head, font=FONTS["card_title"], fill=(15, 23, 42))
        draw.text((cx + 30, start_y + 75), en_sub, font=FONTS["card_body"], fill=accent_c)
        
        # Divider Line
        draw.line([(cx + 30, start_y + 115), (cx + card_w - 30, start_y + 115)], fill=(241, 245, 249), width=1)
        
        # Body
        lines = body.split("\n")
        draw.text((cx + 30, start_y + 145), lines[0], font=FONTS["card_bold"], fill=(30, 41, 59))
        if len(lines) > 1:
            draw.text((cx + 30, start_y + 195), lines[1], font=FONTS["card_body"], fill=(100, 116, 139))
            
        # Foot badge inside card
        draw_rounded_rect(draw, (cx + 30, start_y + 310, cx + card_w - 30, start_y + 360), radius=8, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
        draw.text((cx + 45, start_y + 325), "CORE PILLAR", font=FONTS["badge"], fill=accent_c)

    # Executive Bottom Banner
    draw_rounded_rect(draw, (100, HEIGHT - 230, WIDTH - 100, HEIGHT - 75), radius=12, fill=(15, 23, 42))
    draw.text((140, HEIGHT - 195), "“AI proposes. Human understands. Security validates.”", font=FONTS["slogan_bold"], fill=(255, 255, 255))
    draw.text((140, HEIGHT - 145), "Learn it in the Range · Prove it in our Lab · Fix it in our Code", font=FONTS["slogan_sub"], fill=(147, 197, 253))
    
    return img


def main():
    types = [
        ("slide_01_type1.png", make_type_1, "Type 1: pptsample.png / Excalidraw + 煥哥人物 IP"),
        ("slide_01_type2.png", make_type_2, "Type 2: Canva 繽紛資訊圖卡風"),
        ("slide_01_type3.png", make_type_3, "Type 3: 未來科技深色霓虹資安風"),
        ("slide_01_type4.png", make_type_4, "Type 4: 現代旗艦商務極簡風"),
    ]
    
    print("🚀 Generating Slide 1 in 4 Distinct Styles...")
    for filename, fn, label in types:
        img = fn()
        out_course = os.path.join(OUTPUT_DIR_COURSE, filename)
        out_root = os.path.join(OUTPUT_DIR_ROOT, filename)
        img.save(out_course, "PNG", quality=95)
        img.save(out_root, "PNG", quality=95)
        print(f" ✨ [{label}] Saved: {out_course}")
        
    print("\n✅ All 4 styles for Slide 1 generated successfully!")


if __name__ == "__main__":
    main()
