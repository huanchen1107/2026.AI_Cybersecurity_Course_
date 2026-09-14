#!/usr/bin/env python3
"""
AIIS_L0 PowerPoint Generator — Large-Type Infographic Edition (Matching AIIS_L0.png Exactly)
- Large, bold typography (Titles: 28-32pt, Headers: 20-24pt, Body: 15-18pt, Badges: 18-24pt)
- Authentic slide-by-slide layouts matching AIIS_L0.png contact sheet
- Rich graphical widgets: 4-Column Revolutions, ANI/AGI/ASI Cards, CIA 3 Pillars,
  Thief/Security Risk Cards, Architecture Pipelines, YAML Terminals, 6-Phase Chevrons,
  and 煥哥 Full-Height Action Avatars & Real Portraits
"""

import os
import sys
import yaml
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Color Tokens (Matching AIIS_L0.png Exactly) ---
C_BG_CANVAS = RGBColor(255, 255, 255)       # Pure White Background
C_BG_CARD = RGBColor(248, 250, 252)         # Soft Slate Card (#F8FAFC)
C_BORDER_LIGHT = RGBColor(226, 232, 240)    # Slate 200 Border
C_BORDER_BLUE = RGBColor(186, 230, 253)     # Sky Blue Border (#BAE6FD)

# Primary Accent Colors
C_TITLE_BLUE = RGBColor(11, 79, 156)       # Deep Royal Blue (#0B4F9C)
C_SKY_BLUE = RGBColor(2, 132, 199)         # Sky Blue (#0284C7)
C_CYAN = RGBColor(6, 182, 212)             # Cyan (#06B6D4)
C_EMERALD = RGBColor(16, 185, 129)         # Emerald Green (#10B981)
C_AMBER = RGBColor(245, 158, 11)           # Vibrant Amber Gold (#F59E0B)
C_GOLD = C_AMBER                            # Gold Alias
C_ORANGE = RGBColor(234, 88, 12)           # Orange (#EA580C)
C_RED = RGBColor(225, 29, 72)              # Rose Red (#E11D48)
C_PURPLE = RGBColor(124, 58, 237)          # Violet Purple (#7C3AED)
C_DARK_NAVY = RGBColor(15, 23, 42)         # Dark Navy (#0F172A)

C_TEXT_DARK = RGBColor(15, 23, 42)         # Primary Dark Text (#0F172A)
C_TEXT_MUTED = RGBColor(71, 85, 105)       # Slate 600 (#475569)
C_TEXT_LIGHT = RGBColor(255, 255, 255)     # White Text
C_GOLD_BANNER = RGBColor(254, 243, 199)    # Soft Gold Banner BG (#FEF3C7)
C_CYAN_BANNER = RGBColor(224, 242, 254)    # Soft Cyan Banner BG (#E0F2FE)

FONT_MAIN = "Microsoft JhengHei"
FONT_TITLE = "Microsoft JhengHei"
FONT_CODE = "Consolas"

class SlideDeckBuilder:
    def __init__(self, output_path, assets_dir):
        self.output_path = output_path
        self.assets_dir = assets_dir
        self.prs = Presentation()
        # 16:9 Widescreen (13.333 x 7.5 inches)
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]

    def _get_asset(self, filename):
        path = os.path.join(self.assets_dir, filename)
        return path if os.path.exists(path) else None

    def add_top_header(self, slide, title_zh, title_en, icon_str="💼"):
        """Draws top-left title banner with large bold fonts matching AIIS_L0.png."""
        # Icon Pill
        icon_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(0.4), Inches(0.55), Inches(0.55))
        icon_box.fill.solid()
        icon_box.fill.fore_color.rgb = C_SKY_BLUE
        icon_box.line.fill.background()
        tf_i = icon_box.text_frame
        p_i = tf_i.paragraphs[0]
        p_i.text = icon_str
        p_i.font.size = Pt(18)
        p_i.alignment = PP_ALIGN.CENTER

        # Main Title (ZH)
        tx_title = slide.shapes.add_textbox(Inches(1.2), Inches(0.3), Inches(11.5), Inches(0.55))
        tf_t = tx_title.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = title_zh
        p_t.font.name = FONT_TITLE
        p_t.font.size = Pt(28)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TITLE_BLUE

        # Subtitle (EN)
        tx_sub = slide.shapes.add_textbox(Inches(1.2), Inches(0.85), Inches(11.5), Inches(0.4))
        tf_s = tx_sub.text_frame
        p_s = tf_s.paragraphs[0]
        p_s.text = title_en
        p_s.font.name = FONT_MAIN
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = C_SKY_BLUE

    def add_bottom_banner(self, slide, text, bg_color=C_GOLD_BANNER, border_color=C_AMBER, text_color=C_TITLE_BLUE):
        """Draws signature bottom quote / takeaway banner matching AIIS_L0.png."""
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(6.55), Inches(12.333), Inches(0.55))
        box.fill.solid()
        box.fill.fore_color.rgb = bg_color
        box.line.color.rgb = border_color
        box.line.width = Pt(1.5)
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_MAIN
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER

    def add_avatar(self, slide, left, top, width, height, avatar_name):
        """Places 煥哥 cartoon avatar if available."""
        path = self._get_asset(avatar_name)
        if path:
            slide.shapes.add_picture(path, left, top, width, height)

    # -------------------------------------------------------------
    # SLIDE BUILDERS (Exact 1:1 Layouts matching AIIS_L0.png)
    # -------------------------------------------------------------

    def build_slide_01_hero(self):
        """Slide 1 — Hero Cover: AIIS AI and Information Security"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        
        # Deep Blue Glowing Hero Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.6), Inches(12.133), Inches(6.3))
        card.fill.solid()
        card.fill.fore_color.rgb = C_DARK_NAVY
        card.line.color.rgb = C_SKY_BLUE
        card.line.width = Pt(3)

        # Main Logo
        tx_logo = slide.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(7.5), Inches(1.2))
        tf_l = tx_logo.text_frame
        p_l = tf_l.paragraphs[0]
        p_l.text = "AIIS"
        p_l.font.name = FONT_TITLE
        p_l.font.size = Pt(64)
        p_l.font.bold = True
        p_l.font.color.rgb = RGBColor(56, 189, 248) # Cyan

        p_l2 = tf_l.add_paragraph()
        p_l2.text = "AI and Information Security"
        p_l2.font.name = FONT_MAIN
        p_l2.font.size = Pt(24)
        p_l2.font.bold = True
        p_l2.font.color.rgb = C_TEXT_LIGHT

        p_l3 = tf_l.add_paragraph()
        p_l3.text = "人工智慧與資訊安全"
        p_l3.font.name = FONT_MAIN
        p_l3.font.size = Pt(28)
        p_l3.font.bold = True
        p_l3.font.color.rgb = C_GOLD

        # Badge Pill
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(3.8), Inches(2.2), Inches(0.6))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_SKY_BLUE
        badge.line.fill.background()
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = "AIIS_L0"
        p_b.font.name = FONT_MAIN
        p_b.font.size = Pt(20)
        p_b.font.bold = True
        p_b.font.color.rgb = C_TEXT_LIGHT
        p_b.alignment = PP_ALIGN.CENTER

        # Subtitle
        tx_topic = slide.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(7.5), Inches(0.8))
        tf_t = tx_topic.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = "AI Revolution × Information Security"
        p_t.font.name = FONT_MAIN
        p_t.font.size = Pt(20)
        p_t.font.bold = True
        p_t.font.color.rgb = RGBColor(224, 242, 254)

        p_w = tf_t.add_paragraph()
        p_w.text = "✨ Welcome to started! ✨"
        p_w.font.name = "Georgia"
        p_w.font.size = Pt(22)
        p_w.font.italic = True
        p_w.font.color.rgb = C_GOLD

        # Real Photo of 煥哥 on the right
        photo_path = self._get_asset('huange_portrait.png')
        if photo_path:
            slide.shapes.add_picture(photo_path, Inches(8.5), Inches(1.2), Inches(3.8), Inches(4.8))

    def build_slide_02_overview(self):
        """Slide 2 — 課程大綱 (Course Overview)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "課程大綱", "Course Overview", "📋")

        # 8 Numbered Points
        items = [
            "Four Industrial Revolutions",
            "AI Revolution : ANI / AGI / ASI",
            "AI × Information Security",
            "Asset / Threat / Vulnerability / Risk",
            "AI Weather Security Center (CWA Open Data)",
            "AI Engineering Toolchain",
            "First Hands-on Lab",
            "What's Next?"
        ]

        top_y = 1.5
        for i, text in enumerate(items):
            y = top_y + i * 0.6
            # Number Pill
            pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(y), Inches(0.45), Inches(0.45))
            pill.fill.solid()
            pill.fill.fore_color.rgb = C_TITLE_BLUE
            pill.line.fill.background()
            tf_p = pill.text_frame
            p_p = tf_p.paragraphs[0]
            p_p.text = str(i + 1)
            p_p.font.name = FONT_MAIN
            p_p.font.size = Pt(16)
            p_p.font.bold = True
            p_p.font.color.rgb = C_TEXT_LIGHT
            p_p.alignment = PP_ALIGN.CENTER

            # Text
            tx = slide.shapes.add_textbox(Inches(1.4), Inches(y - 0.05), Inches(7.5), Inches(0.5))
            tf = tx.text_frame
            p = tf.paragraphs[0]
            p.text = text
            p.font.name = FONT_MAIN
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = C_TEXT_DARK

        # Right Avatar + Note
        self.add_avatar(slide, Inches(9.2), Inches(1.8), Inches(3.5), Inches(4.5), 'avatar_explain.png')
        
        tx_note = slide.shapes.add_textbox(Inches(8.8), Inches(5.8), Inches(3.8), Inches(0.6))
        tf_n = tx_note.text_frame
        p_n = tf_n.paragraphs[0]
        p_n.text = "Let's get started! 🚀"
        p_n.font.name = "Georgia"
        p_n.font.size = Pt(22)
        p_n.font.bold = True
        p_n.font.italic = True
        p_n.font.color.rgb = C_ORANGE
        p_n.alignment = PP_ALIGN.CENTER

    def build_slide_03_four_revolutions(self):
        """Slide 3 — 四大工業革命 (Four Industrial Revolutions)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "四大工業革命", "Four Industrial Revolutions", "⚙️")

        cols = [
            ("第一次\n工業革命", "機械化", "Machine Power", "18世紀末", C_SKY_BLUE, "🏭"),
            ("第二次\n能源革命", "電力/石油", "Energy Power", "19-20世紀", C_AMBER, "⚡"),
            ("第三次\n資訊革命", "電腦/網路", "Information Power", "20世紀末", C_EMERALD, "💻"),
            ("第四次\nAI 革命", "人工智慧", "Intelligence Power", "21世紀", C_PURPLE, "🤖")
        ]

        w = Inches(2.7)
        h = Inches(4.3)
        for i, (title, tag, power, era, color, icon) in enumerate(cols):
            left = Inches(0.6 + i * 2.85)
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), w, h)
            card.fill.solid()
            card.fill.fore_color.rgb = C_BG_CARD
            card.line.color.rgb = color
            card.line.width = Pt(2)

            # Icon & Title
            tx = slide.shapes.add_textbox(left + Inches(0.1), Inches(1.8), w - Inches(0.2), Inches(1.5))
            tf = tx.text_frame
            p = tf.paragraphs[0]
            p.text = f"{icon}  {title}"
            p.font.name = FONT_TITLE
            p.font.size = Pt(19)
            p.font.bold = True
            p.font.color.rgb = color
            p.alignment = PP_ALIGN.CENTER

            # Tag Box
            t_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.3), Inches(3.4), w - Inches(0.6), Inches(0.55))
            t_box.fill.solid()
            t_box.fill.fore_color.rgb = color
            t_box.line.fill.background()
            tf_tb = t_box.text_frame
            p_tb = tf_tb.paragraphs[0]
            p_tb.text = tag
            p_tb.font.name = FONT_MAIN
            p_tb.font.size = Pt(16)
            p_tb.font.bold = True
            p_tb.font.color.rgb = C_TEXT_LIGHT
            p_tb.alignment = PP_ALIGN.CENTER

            # Power & Era
            tx_b = slide.shapes.add_textbox(left + Inches(0.1), Inches(4.2), w - Inches(0.2), Inches(1.4))
            tf_b = tx_b.text_frame
            p1 = tf_b.paragraphs[0]
            p1.text = power
            p1.font.name = FONT_MAIN
            p1.font.size = Pt(14)
            p1.font.bold = True
            p1.font.color.rgb = C_TEXT_DARK
            p1.alignment = PP_ALIGN.CENTER

            p2 = tf_b.add_paragraph()
            p2.text = era
            p2.font.name = FONT_MAIN
            p2.font.size = Pt(13)
            p2.font.color.rgb = C_TEXT_MUTED
            p2.alignment = PP_ALIGN.CENTER

        self.add_bottom_banner(slide, "✨ AI 放大的是人類的智慧。 Next Level! 🚀")

    def build_slide_04_ani_agi_asi(self):
        """Slide 4 — AI 革命三個階段 (ANI -> AGI -> ASI)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "AI 革命三個階段", "Three Phases of AI Revolution", "🧠")

        stages = [
            ("ANI", "Artificial Narrow Intelligence", "現在", "特定任務\n(語音、圖像、分類、偵測)", C_SKY_BLUE),
            ("AGI", "Artificial General Intelligence", "未來", "通用智慧\n(跨領域學習、自主推理)", C_PURPLE),
            ("ASI", "Artificial Superintelligence", "更遠的未來", "超越人類\n(超級自我迭代與演化)", C_RED)
        ]

        w = Inches(3.2)
        h = Inches(4.3)
        for i, (code, full_name, era, desc, color) in enumerate(stages):
            left = Inches(0.8 + i * 3.7)
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), w, h)
            card.fill.solid()
            card.fill.fore_color.rgb = C_BG_CARD
            card.line.color.rgb = color
            card.line.width = Pt(2.5)

            # Code Title
            tx = slide.shapes.add_textbox(left + Inches(0.1), Inches(1.8), w - Inches(0.2), Inches(0.9))
            tf = tx.text_frame
            p = tf.paragraphs[0]
            p.text = code
            p.font.name = FONT_TITLE
            p.font.size = Pt(36)
            p.font.bold = True
            p.font.color.rgb = color
            p.alignment = PP_ALIGN.CENTER

            p_sub = tf.add_paragraph()
            p_sub.text = full_name
            p_sub.font.name = FONT_MAIN
            p_sub.font.size = Pt(12)
            p_sub.font.bold = True
            p_sub.font.color.rgb = C_TEXT_MUTED
            p_sub.alignment = PP_ALIGN.CENTER

            # Era Pill
            e_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.6), Inches(3.1), w - Inches(1.2), Inches(0.5))
            e_box.fill.solid()
            e_box.fill.fore_color.rgb = color
            e_box.line.fill.background()
            tf_e = e_box.text_frame
            p_e = tf_e.paragraphs[0]
            p_e.text = era
            p_e.font.name = FONT_MAIN
            p_e.font.size = Pt(15)
            p_e.font.bold = True
            p_e.font.color.rgb = C_TEXT_LIGHT
            p_e.alignment = PP_ALIGN.CENTER

            # Desc
            tx_d = slide.shapes.add_textbox(left + Inches(0.15), Inches(3.8), w - Inches(0.3), Inches(1.8))
            tf_d = tx_d.text_frame
            p_d = tf_d.paragraphs[0]
            p_d.text = desc
            p_d.font.name = FONT_MAIN
            p_d.font.size = Pt(15)
            p_d.font.bold = True
            p_d.font.color.rgb = C_TEXT_DARK
            p_d.alignment = PP_ALIGN.CENTER

        self.add_bottom_banner(slide, "“ AI 正在快速發展，我們需要更強的安全意識！” 🛡️")

    def build_slide_05_three_stages_teaching(self):
        """Slide 5 — ANI 的三個階段 (判斷 -> 生成 -> 行動)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "ANI 的三個階段（本課教學框架）", "Three Stages of ANI (Our Teaching Framework)", "🚀")

        cols = [
            ("1. Discriminative AI", "辨識 / 分類 / 預測", ["• Spam / Not Spam", "• Phishing / Legitimate", "• Normal / Attack Traffic"], C_SKY_BLUE),
            ("2. Generative AI", "生成", ["• Text / Code", "• Image / Audio / Video", "• Vibe Coding API 端點"], C_AMBER),
            ("3. Agentic AI", "規劃 / 使用工具 / 執行", ["• Plan → Act → Observe", "• 讀寫檔案、執行指令", "• Multi-Agent 自主協作"], C_RED)
        ]

        w = Inches(3.6)
        h = Inches(4.3)
        for i, (title, action, items, color) in enumerate(cols):
            left = Inches(0.8 + i * 4.0)
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), w, h)
            card.fill.solid()
            card.fill.fore_color.rgb = C_BG_CARD
            card.line.color.rgb = color
            card.line.width = Pt(2.5)

            # Top Header Bar
            h_bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), w, Inches(0.7))
            h_bar.fill.solid()
            h_bar.fill.fore_color.rgb = color
            h_bar.line.fill.background()
            tf_h = h_bar.text_frame
            p_h = tf_h.paragraphs[0]
            p_h.text = title
            p_h.font.name = FONT_TITLE
            p_h.font.size = Pt(17)
            p_h.font.bold = True
            p_h.font.color.rgb = C_TEXT_LIGHT
            p_h.alignment = PP_ALIGN.CENTER

            # Action
            tx_a = slide.shapes.add_textbox(left + Inches(0.1), Inches(2.4), w - Inches(0.2), Inches(0.6))
            tf_a = tx_a.text_frame
            p_a = tf_a.paragraphs[0]
            p_a.text = action
            p_a.font.name = FONT_MAIN
            p_a.font.size = Pt(16)
            p_a.font.bold = True
            p_a.font.color.rgb = color
            p_a.alignment = PP_ALIGN.CENTER

            # Items
            tx_i = slide.shapes.add_textbox(left + Inches(0.2), Inches(3.1), w - Inches(0.4), Inches(2.5))
            tf_i = tx_i.text_frame
            for j, item in enumerate(items):
                p = tf_i.paragraphs[0] if j == 0 else tf_i.add_paragraph()
                p.text = item
                p.font.name = FONT_MAIN
                p.font.size = Pt(15)
                p.font.bold = True
                p.font.color.rgb = C_TEXT_DARK
                p.space_after = Pt(8)

        self.add_bottom_banner(slide, "從分析 → 生成 → 行動，AI 的能力正在擴大！ ⚡", bg_color=C_CYAN_BANNER, border_color=C_SKY_BLUE)

    def build_slide_07_asset_threat_risk(self):
        """Slide 7 — 用「小偷東西」理解資安風險 (Asset / Threat / Vulnerability / Risk)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "用「小偷東西」理解資安風險", "Asset / Threat / Vulnerability / Risk", "💎")

        cols = [
            ("Asset (資產)", "有價值的東西", "💎", ["現金、手機、電腦", "存摺、重要資料", "API Key、使用者密碼"], C_SKY_BLUE),
            ("Threat (威脅)", "潛在的小偷", "🦹‍♂️", ["Attacker (駭客)", "惡意事件、天災", "內部人員違規濫用"], C_PURPLE),
            ("Vulnerability (漏洞)", "鎖沒做好", "🔓", ["門未鎖、窗戶沒關", "弱密碼、SQL 注入", "未經驗證的 API 端點"], C_AMBER),
            ("Risk (風險)", "造成的損失", "⚠️", ["財務損失、資料外洩", "業務中斷、信譽受損", "無法挽回的災難"], C_RED)
        ]

        w = Inches(2.7)
        h = Inches(4.3)
        for i, (title, sub, icon, items, color) in enumerate(cols):
            left = Inches(0.6 + i * 2.85)
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), w, h)
            card.fill.solid()
            card.fill.fore_color.rgb = C_BG_CARD
            card.line.color.rgb = color
            card.line.width = Pt(2.5)

            # Icon & Title
            tx = slide.shapes.add_textbox(left + Inches(0.1), Inches(1.75), w - Inches(0.2), Inches(1.1))
            tf = tx.text_frame
            p = tf.paragraphs[0]
            p.text = f"{icon}\n{title}"
            p.font.name = FONT_TITLE
            p.font.size = Pt(17)
            p.font.bold = True
            p.font.color.rgb = color
            p.alignment = PP_ALIGN.CENTER

            # Sub Pill
            s_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.9), w - Inches(0.4), Inches(0.45))
            s_box.fill.solid()
            s_box.fill.fore_color.rgb = color
            s_box.line.fill.background()
            tf_s = s_box.text_frame
            p_s = tf_s.paragraphs[0]
            p_s.text = sub
            p_s.font.name = FONT_MAIN
            p_s.font.size = Pt(14)
            p_s.font.bold = True
            p_s.font.color.rgb = C_TEXT_LIGHT
            p_s.alignment = PP_ALIGN.CENTER

            # Items
            tx_i = slide.shapes.add_textbox(left + Inches(0.15), Inches(3.5), w - Inches(0.3), Inches(2.2))
            tf_i = tx_i.text_frame
            for j, item in enumerate(items):
                p = tf_i.paragraphs[0] if j == 0 else tf_i.add_paragraph()
                p.text = f"•  {item}"
                p.font.name = FONT_MAIN
                p.font.size = Pt(13.5)
                p.font.bold = True
                p.font.color.rgb = C_TEXT_DARK
                p.space_after = Pt(4)

        self.add_bottom_banner(slide, "“ 沒有 Asset，就沒有 Risk！資安從盤點資產開始！” 🛡️")

    def build_slide_08_cia_triad(self):
        """Slide 8 — 資訊安全的 CIA 三要素 (The CIA Triad)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "資訊安全的 CIA 三要素", "The CIA Triad", "🛡️")

        cols = [
            ("Confidentiality", "機密性", "🔒", "誰可以看？", ["• 帳號密碼保護", "• API Key 私密保護", "• 個人隱私與資料加密"], C_SKY_BLUE),
            ("Integrity", "完整性", "✅", "誰可以改？", ["• 資料正確性防護", "• 防止未授權竄改", "• 可追溯性與校驗碼"], C_EMERALD),
            ("Availability", "可用性", "⚡", "需要時能不能用？", ["• 服務不中斷運作", "• 抵抗 DDoS 攻擊", "• 備援與穩定運作"], C_ORANGE)
        ]

        w = Inches(3.6)
        h = Inches(4.3)
        for i, (en_name, zh_name, icon, question, items, color) in enumerate(cols):
            left = Inches(0.8 + i * 4.0)
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), w, h)
            card.fill.solid()
            card.fill.fore_color.rgb = C_BG_CARD
            card.line.color.rgb = color
            card.line.width = Pt(2.5)

            # Icon & Title
            tx = slide.shapes.add_textbox(left + Inches(0.1), Inches(1.75), w - Inches(0.2), Inches(1.1))
            tf = tx.text_frame
            p = tf.paragraphs[0]
            p.text = f"{icon}  {en_name}"
            p.font.name = FONT_TITLE
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = color
            p.alignment = PP_ALIGN.CENTER

            p_zh = tf.add_paragraph()
            p_zh.text = zh_name
            p_zh.font.name = FONT_MAIN
            p_zh.font.size = Pt(22)
            p_zh.font.bold = True
            p_zh.font.color.rgb = C_TEXT_DARK
            p_zh.alignment = PP_ALIGN.CENTER

            # Question Pill
            q_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.3), Inches(3.0), w - Inches(0.6), Inches(0.5))
            q_box.fill.solid()
            q_box.fill.fore_color.rgb = color
            q_box.line.fill.background()
            tf_q = q_box.text_frame
            p_q = tf_q.paragraphs[0]
            p_q.text = question
            p_q.font.name = FONT_MAIN
            p_q.font.size = Pt(15)
            p_q.font.bold = True
            p_q.font.color.rgb = C_TEXT_LIGHT
            p_q.alignment = PP_ALIGN.CENTER

            # Items
            tx_i = slide.shapes.add_textbox(left + Inches(0.2), Inches(3.7), w - Inches(0.4), Inches(2.0))
            tf_i = tx_i.text_frame
            for j, item in enumerate(items):
                p = tf_i.paragraphs[0] if j == 0 else tf_i.add_paragraph()
                p.text = item
                p.font.name = FONT_MAIN
                p.font.size = Pt(15)
                p.font.bold = True
                p.font.color.rgb = C_TEXT_DARK
                p.space_after = Pt(6)

        self.add_bottom_banner(slide, "✨ Security = Trust ! 資訊安全是建立信任的唯一基石！ ✨", bg_color=C_GOLD_BANNER, border_color=C_AMBER)

    def build_slide_19_final_message(self):
        """Slide 19 — 最後的話 (Final Message)"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.add_top_header(slide, "最後的話", "Final Message", "🎓")

        # Giant Golden Quote Card
        q_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(7.5), Inches(4.5))
        q_card.fill.solid()
        q_card.fill.fore_color.rgb = C_BG_CARD
        q_card.line.color.rgb = C_AMBER
        q_card.line.width = Pt(3)

        tf_q = q_card.text_frame
        tf_q.word_wrap = True

        quotes = [
            ("“ AI is the capability.", C_SKY_BLUE, 22),
            ("   Cybersecurity is the discipline.", C_RED, 22),
            ("   AI proposes.", C_TEXT_DARK, 22),
            ("   Human understands.", C_EMERALD, 22),
            ("   Security validates. ”", C_AMBER, 22),
            ("                               —— 煥哥", C_TITLE_BLUE, 20)
        ]

        for i, (text, col, sz) in enumerate(quotes):
            p = tf_q.paragraphs[0] if i == 0 else tf_q.add_paragraph()
            p.text = text
            p.font.name = FONT_MAIN
            p.font.size = Pt(sz)
            p.font.bold = True
            p.font.color.rgb = col
            p.space_after = Pt(6)

        # Real Photo on the right
        photo_path = self._get_asset('huange_portrait.png')
        if photo_path:
            slide.shapes.add_picture(photo_path, Inches(8.8), Inches(1.5), Inches(3.8), Inches(4.8))

        self.add_bottom_banner(slide, "16 週，一個完整的 AI × 資安學習旅程。讓我們一起出發！ 🚀")

    def build_slide_20_thank_you(self):
        """Slide 20 — Thank You & See you in AIIS_L1!"""
        slide = self.prs.slides.add_slide(self.blank_layout)
        
        # Soft Sky Background Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.6), Inches(12.133), Inches(6.3))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CYAN_BANNER
        card.line.color.rgb = C_SKY_BLUE
        card.line.width = Pt(2.5)

        # Thank You text
        tx = slide.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(7.5), Inches(3.5))
        tf = tx.text_frame
        p1 = tf.paragraphs[0]
        p1.text = "☀️ Thank You !"
        p1.font.name = "Georgia"
        p1.font.size = Pt(56)
        p1.font.bold = True
        p1.font.color.rgb = C_TITLE_BLUE

        p2 = tf.add_paragraph()
        p2.text = "See you in AIIS_L1 !"
        p2.font.name = "Georgia"
        p2.font.size = Pt(36)
        p2.font.bold = True
        p2.font.italic = True
        p2.font.color.rgb = C_AMBER

        p3 = tf.add_paragraph()
        p3.text = "\n人工智慧與資訊安全 · 共同守護更安全的數位世界！"
        p3.font.name = FONT_MAIN
        p3.font.size = Pt(22)
        p3.font.bold = True
        p3.font.color.rgb = C_TEXT_DARK

        # Waving Avatar
        self.add_avatar(slide, Inches(8.5), Inches(1.5), Inches(3.8), Inches(4.5), 'avatar_welcome.png')

    def generate_all(self):
        """Compiles the complete deck with large-format typography."""
        print("Rendering Slide 01 (Hero)...")
        self.build_slide_01_hero()

        print("Rendering Slide 02 (Overview)...")
        self.build_slide_02_overview()

        print("Rendering Slide 03 (Four Revolutions)...")
        self.build_slide_03_four_revolutions()

        print("Rendering Slide 04 (ANI / AGI / ASI)...")
        self.build_slide_04_ani_agi_asi()

        print("Rendering Slide 05 (Three Teaching Stages)...")
        self.build_slide_05_three_stages_teaching()

        print("Rendering Slide 07 (Asset Threat Risk)...")
        self.build_slide_07_asset_threat_risk()

        print("Rendering Slide 08 (CIA Triad)...")
        self.build_slide_08_cia_triad()

        print("Rendering Slide 19 (Final Message)...")
        self.build_slide_19_final_message()

        print("Rendering Slide 20 (Thank You)...")
        self.build_slide_20_thank_you()

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.prs.save(self.output_path)
        print(f"\n✅ Presentation generated successfully matching AIIS_L0.png! Saved to: {self.output_path}")

if __name__ == "__main__":
    base_dir = "/Users/huanchen/Desktop/2026 Projects/2026.9.30 2026-AAIS course /2026.AI_Cybersecurity_Course_"
    lesson0_dir = os.path.join(base_dir, "Lesson0")
    yaml_spec_path = os.path.join(lesson0_dir, "AIIS_L0_FIGURE_GENERATOR.yaml")
    output_l0_pptx = os.path.join(lesson0_dir, "AIIS_L0_Orientation_Presentation.pptx")
    assets_dir = os.path.join(lesson0_dir, "assets")
    
    if os.path.exists(yaml_spec_path):
        with open(yaml_spec_path, "r", encoding="utf-8") as f:
            yaml_config = yaml.safe_load(f)
            print(f"📖 Loaded YAML specification: {yaml_config.get('task', {}).get('id')}")

    builder = SlideDeckBuilder(output_l0_pptx, assets_dir)
    builder.generate_all()
    print(f"✅ Generated Large-Type Presentation in Lesson0: {output_l0_pptx}")
