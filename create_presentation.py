import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Palette
    C_BG = RGBColor(13, 17, 23)        # #0d1117 Dark Slate
    C_CARD = RGBColor(22, 27, 34)      # #161b22 Card Background
    C_BORDER = RGBColor(48, 54, 61)    # #30363d Border
    C_BLUE = RGBColor(56, 189, 248)    # #38bdf8 Sky Blue
    C_PURPLE = RGBColor(168, 85, 247)  # #a855f7 Purple
    C_PINK = RGBColor(244, 114, 182)   # #f472b6 Pink
    C_GREEN = RGBColor(52, 211, 153)   # #34d399 Green
    C_AMBER = RGBColor(251, 191, 36)   # #fbbf24 Amber
    C_TEXT = RGBColor(240, 246, 252)   # #f0f6fc Primary Text
    C_MUTED = RGBColor(139, 148, 158)  # #8b949e Muted Text
    C_WHITE = RGBColor(255, 255, 255)
    
    blank_layout = prs.slide_layouts[6]
    base_dir = r"c:\Users\gandi\OneDrive\Desktop\davproject"
    
    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        
        # Top gradient accent bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = C_BLUE
        bar.line.fill.background()
        return bg

    def add_header(slide, title_text, category="CAMPUS EVENT ANALYTICS"):
        # Category / Pill
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_BLUE
        
        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = C_TEXT

    # ==========================================
    # SLIDE 1: Title & Team Members
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)
    
    # Title Box
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p_badge = tf1.paragraphs[0]
    p_badge.text = "DATA ANALYTICS & VISUALIZATION PROJECT"
    p_badge.font.size = Pt(13)
    p_badge.font.bold = True
    p_badge.font.color.rgb = C_BLUE
    p_badge.space_after = Pt(14)
    
    p_main = tf1.add_paragraph()
    p_main.text = "CAMPUS EVENT ANALYTICS"
    p_main.font.size = Pt(38)
    p_main.font.bold = True
    p_main.font.color.rgb = C_WHITE
    p_main.space_after = Pt(10)
    
    p_sub = tf1.add_paragraph()
    p_sub.text = "Multi-Institutional Event Integrity, Data Cleaning, and 2D/3D Analytics Dashboard"
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = C_MUTED
    
    # Team Members Card
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.8), Inches(11.3), Inches(2.7))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = C_CARD
    team_card.line.color.rgb = C_BORDER
    team_card.line.width = Pt(1)
    
    tf_team = team_card.text_frame
    tf_team.word_wrap = True
    tf_team.margin_left = Inches(0.5)
    tf_team.margin_top = Inches(0.4)
    
    p_th = tf_team.paragraphs[0]
    p_th.text = "TEAM MEMBERS"
    p_th.font.size = Pt(14)
    p_th.font.bold = True
    p_th.font.color.rgb = C_PURPLE
    p_th.space_after = Pt(16)
    
    members = [
        "2503A52735 - G. Dhiraj Kumar",
        "2503A52742 - P. John David",
        "2503A52743 - S. Jashwanth"
    ]
    for m in members:
        pm = tf_team.add_paragraph()
        pm.text = f"•  {m}"
        pm.font.size = Pt(16)
        pm.font.bold = True
        pm.font.color.rgb = C_TEXT
        pm.space_after = Pt(8)

    # ==========================================
    # SLIDE 2: Project Overview & Scope
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Project Overview & Dataset Scope")
    
    # Left Card: Overall Scope
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_CARD
    c1.line.color.rgb = C_BORDER
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = Inches(0.3)
    tf_c1.margin_top = Inches(0.3)
    
    p = tf_c1.paragraphs[0]
    p.text = "COMBINED PROJECT SCALE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(14)
    
    bullets_s2_left = [
        ("Total Raw Events Audited:", " 15,300 event records"),
        ("Cleaned & Validated Events:", " 14,750 verified records (550 duplicates purged)"),
        ("Institutional Breadth:", " 11 IIT Campuses & 7 University Departments"),
        ("Event Categories:", " 7 Diverse Categories (Technical, Cultural, Sports, etc.)"),
        ("Data Harmonization:", " Reconciled varied Excel (.xlsx) and CSV data formats")
    ]
    for b_title, b_desc in bullets_s2_left:
        p = tf_c1.add_paragraph()
        run1 = p.add_run()
        run1.text = f"• {b_title}"
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = C_TEXT
        run2 = p.add_run()
        run2.text = b_desc
        run2.font.size = Pt(13)
        run2.font.color.rgb = C_MUTED
        p.space_after = Pt(10)
        
    # Right Card: Objectives & Sources
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_CARD
    c2.line.color.rgb = C_BORDER
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = Inches(0.3)
    tf_c2.margin_top = Inches(0.3)
    
    p = tf_c2.paragraphs[0]
    p.text = "CORE OBJECTIVES & DATA SOURCES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PURPLE
    p.space_after = Pt(14)
    
    bullets_s2_right = [
        ("Data Quality Guarantee:", " Eliminate nulls, corrupt text, and impossible numbers"),
        ("Physical Capacity Law:", " Cap attendance to real venue limits with audit tracking"),
        ("Financial Transparency:", " Recalculate true net revenues, budgets, and per-capita costs"),
        ("Executive Intelligence:", " Power real-time interactive 2D and 3D web dashboards"),
        ("Data Sources:", " Central IIT Event Registry & UC Berkeley Campus Data Portal")
    ]
    for b_title, b_desc in bullets_s2_right:
        p = tf_c2.add_paragraph()
        run1 = p.add_run()
        run1.text = f"• {b_title}"
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = C_TEXT
        run2 = p.add_run()
        run2.text = b_desc
        run2.font.size = Pt(13)
        run2.font.color.rgb = C_MUTED
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 3: Dataset 1 - IIT Campus Events
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Dataset 1: IIT Campus Events (Excel)", category="DATASET PROFILE")
    
    # Left Card: Specifications
    c_iit1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_iit1.fill.solid()
    c_iit1.fill.fore_color.rgb = C_CARD
    c_iit1.line.color.rgb = C_BORDER
    tf_iit1 = c_iit1.text_frame
    tf_iit1.word_wrap = True
    tf_iit1.margin_left = Inches(0.3)
    tf_iit1.margin_top = Inches(0.3)
    
    p = tf_iit1.paragraphs[0]
    p.text = "DATASET SPECIFICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(14)
    
    iit_specs = [
        ("File Name:", " IIT_Campus_Event_Raw_5100_Rows.xlsx"),
        ("Initial Dimensions:", " 5,100 Rows × 11 Columns"),
        ("Final Dimensions:", " 4,750 Rows × 15 Curated Columns"),
        ("Duplicates Removed:", " 350 Exact Duplicate Entries"),
        ("Missing Values Resolved:", " 2,159 Total Attributes Imputed"),
        ("Currency Tracked:", " Indian Rupee (INR)")
    ]
    for k, v in iit_specs:
        p = tf_iit1.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(13)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)
        
    # Right Card: Institutional Coverage
    c_iit2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_iit2.fill.solid()
    c_iit2.fill.fore_color.rgb = C_CARD
    c_iit2.line.color.rgb = C_BORDER
    tf_iit2 = c_iit2.text_frame
    tf_iit2.word_wrap = True
    tf_iit2.margin_left = Inches(0.3)
    tf_iit2.margin_top = Inches(0.3)
    
    p = tf_iit2.paragraphs[0]
    p.text = "INSTITUTIONAL & CATEGORY COVERAGE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(14)
    
    iit_details = [
        ("11 Premier Campuses:", " IIT Bombay, IIT Delhi, IIT Madras, IIT Kanpur, IIT Kharagpur, IIT Roorkee, IIT Guwahati, IIT Hyderabad, IIT BHU, IIT Gandhinagar, IIT Main Campus"),
        ("7 Event Domains:", " Technical, Cultural, Sports, Academic, Research, E-Cell, General"),
        ("Key Logistical Fields:", " Venue Name, Max Hall Capacity, Total Registrations, Actual Attendance"),
        ("Calculated Fields Added:", " Turnout Rate (%), Capacity Utilization (%), Cost per Attendee (INR)")
    ]
    for k, v in iit_details:
        p = tf_iit2.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 4: Dataset 2 - University Events
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Dataset 2: University Events (CSV)", category="DATASET PROFILE")
    
    # Left Card: Specifications
    c_ucb1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_ucb1.fill.solid()
    c_ucb1.fill.fore_color.rgb = C_CARD
    c_ucb1.line.color.rgb = C_BORDER
    tf_ucb1 = c_ucb1.text_frame
    tf_ucb1.word_wrap = True
    tf_ucb1.margin_left = Inches(0.3)
    tf_ucb1.margin_top = Inches(0.3)
    
    p = tf_ucb1.paragraphs[0]
    p.text = "DATASET SPECIFICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PINK
    p.space_after = Pt(14)
    
    ucb_specs = [
        ("File Name:", " uncleaned_event_data.csv (UC Berkeley benchmark)"),
        ("Initial Dimensions:", " 10,200 Rows × 20 Columns"),
        ("Final Dimensions:", " 10,000 Rows × 24 Curated Columns"),
        ("Duplicates Removed:", " 200 Duplicate Records & Event IDs"),
        ("Missing Values Resolved:", " 3,546 Total Attributes Imputed"),
        ("Currency Tracked:", " US Dollars ($)")
    ]
    for k, v in ucb_specs:
        p = tf_ucb1.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(13)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)
        
    # Right Card: Departments & Financials
    c_ucb2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_ucb2.fill.solid()
    c_ucb2.fill.fore_color.rgb = C_CARD
    c_ucb2.line.color.rgb = C_BORDER
    tf_ucb2 = c_ucb2.text_frame
    tf_ucb2.word_wrap = True
    tf_ucb2.margin_left = Inches(0.3)
    tf_ucb2.margin_top = Inches(0.3)
    
    p = tf_ucb2.paragraphs[0]
    p.text = "DEPARTMENTAL & COMMERCIAL PROFILE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p.space_after = Pt(14)
    
    ucb_details = [
        ("7 Host Departments:", " Haas School of Business, EECS, Berkeley Law, College of Letters & Science, RSF Rec Sports, School of Public Health, Student Affairs"),
        ("6 Event Categories:", " Academic, Workshop, Career, Social, Sports, Cultural"),
        ("Commercial Attributes:", " Ticket Price ($), Sponsorship ($), Marketing Spend ($), Event Budget ($)"),
        ("Engineered Metrics:", " Cleaned Net Revenue ($), Turnout Rate (%), Return on Investment (ROI %)")
    ]
    for k, v in ucb_details:
        p = tf_ucb2.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 5: Data Cleaning 1 - Duplicates & Formatting
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Data Cleaning: Duplicates & Text Standardization", category="DATA CLEANING STEP 1")
    
    # Left Box: Duplicate Removal
    c_dup = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_dup.fill.solid()
    c_dup.fill.fore_color.rgb = C_CARD
    c_dup.line.color.rgb = C_BORDER
    tf_dup = c_dup.text_frame
    tf_dup.word_wrap = True
    tf_dup.margin_left = Inches(0.3)
    tf_dup.margin_top = Inches(0.3)
    
    p = tf_dup.paragraphs[0]
    p.text = "DUPLICATE DETECTION & ELIMINATION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(14)
    
    dup_points = [
        ("Why It Happened:", " Network timeouts and manual re-submissions created redundant rows across both raw files."),
        ("IIT Duplicate Action:", " Scanned 5,100 records across 11 fields. Identified and purged exactly 350 duplicate rows (settled at 4,750)."),
        ("University Duplicate Action:", " Scanned 10,200 records across 20 fields. Eliminated 200 duplicate rows & duplicate Event IDs (settled at 10,000)."),
        ("Resulting Integrity:", " Exactly 0 duplicate events remain. Zero inflation in total attendance or financial totals.")
    ]
    for k, v in dup_points:
        p = tf_dup.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(10)

    # Right Box: Text Standardization
    c_txt = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_txt.fill.solid()
    c_txt.fill.fore_color.rgb = C_CARD
    c_txt.line.color.rgb = C_BORDER
    tf_txt = c_txt.text_frame
    tf_txt.word_wrap = True
    tf_txt.margin_left = Inches(0.3)
    tf_txt.margin_top = Inches(0.3)
    
    p = tf_txt.paragraphs[0]
    p.text = "TEXT & SPELLING NORMALIZATION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PURPLE
    p.space_after = Pt(14)
    
    txt_points = [
        ("Campus Typo Resolution:", " Replaced lowercase and varied entries (e.g., 'iit bombay', 'IIT DELHI') with uniform Title Case."),
        ("Category Typo Repair:", " Corrected truncated strings and typos (e.g., 'Acad' → 'Academic', 'Culturall' → 'Cultural', 'Tech' → 'Technical')."),
        ("Date Format Unification:", " Raw dates had mixed notations (DD/MM/YYYY, MM-DD-YYYY). Standardized 100% of rows to ISO YYYY-MM-DD."),
        ("Email & String Sanitization:", " Trimmed stray leading/trailing whitespaces and repaired corrupted special characters.")
    ]
    for k, v in txt_points:
        p = tf_txt.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 6: Data Cleaning 2 - Missing Values
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Data Cleaning: Missing Values Imputation", category="DATA CLEANING STEP 2")
    
    # Left Card: IIT Imputation
    c_mv1 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_mv1.fill.solid()
    c_mv1.fill.fore_color.rgb = C_CARD
    c_mv1.line.color.rgb = C_BORDER
    tf_mv1 = c_mv1.text_frame
    tf_mv1.word_wrap = True
    tf_mv1.margin_left = Inches(0.3)
    tf_mv1.margin_top = Inches(0.3)
    
    p = tf_mv1.paragraphs[0]
    p.text = "IIT DATASET IMPUTATIONS (2,159 HANDLED)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(14)
    
    mv1_points = [
        ("Missing Campus (420 rows):", " Imputed with standard fallback 'IIT Main Campus'."),
        ("Missing Category (445 rows):", " Filled using the general mode category 'General / Academic'."),
        ("Missing Attendance (369 rows):", " Estimated mathematically by multiplying registrations by median turnout (75%)."),
        ("Missing Budget INR (484 rows):", " Filled using median budget computed for that specific event category."),
        ("Missing CSAT Rating (441 rows):", " Filled using overall campus median satisfaction rating (3.0 / 5.0).")
    ]
    for k, v in mv1_points:
        p = tf_mv1.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)

    # Right Card: University Imputation
    c_mv2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_mv2.fill.solid()
    c_mv2.fill.fore_color.rgb = C_CARD
    c_mv2.line.color.rgb = C_BORDER
    tf_mv2 = c_mv2.text_frame
    tf_mv2.word_wrap = True
    tf_mv2.margin_left = Inches(0.3)
    tf_mv2.margin_top = Inches(0.3)
    
    p = tf_mv2.paragraphs[0]
    p.text = "UNIVERSITY DATASET IMPUTATIONS (3,546 HANDLED)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PINK
    p.space_after = Pt(14)
    
    mv2_points = [
        ("Missing Actual Attendance (508 rows):", " Calculated via Registration count × department median turnout ratio (70%)."),
        ("Missing Turnout Rate (499 rows):", " Recalculated cleanly as (Actual Attendance / Registrations) × 100."),
        ("Missing Sponsorship (493 rows):", " Safely imputed with $0.00 (verified non-sponsored event)."),
        ("Missing Student Rating (506 rows):", " Imputed with category median rating score (4.0 / 5.0)."),
        ("Missing Organizer Email (518 rows):", " Filled with official fallback organizer.campus@berkeley.edu.")
    ]
    for k, v in mv2_points:
        p = tf_mv2.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 7: Data Cleaning 3 - Outliers & Logic
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Data Cleaning: Outliers & Physical Venue Constraints", category="DATA CLEANING STEP 3")
    
    # Left Card: Physical Venue Law
    c_out1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_out1.fill.solid()
    c_out1.fill.fore_color.rgb = C_CARD
    c_out1.line.color.rgb = C_BORDER
    tf_out1 = c_out1.text_frame
    tf_out1.word_wrap = True
    tf_out1.margin_left = Inches(0.3)
    tf_out1.margin_top = Inches(0.3)
    
    p = tf_out1.paragraphs[0]
    p.text = "THE PHYSICAL VENUE CAPACITY RULE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(14)
    
    out1_points = [
        ("The Physical Constraint:", " A physical hall cannot hold more attendees than its certified fire-code capacity (e.g., 800 people cannot sit in a 500-seat auditorium)."),
        ("Over-Capacity Remediation:", " 321 records where attendance exceeded hall limits were capped at 100% capacity limit."),
        ("Audit Transparency:", " The uncleaned raw attendance figures were archived in a dedicated audit field for full audit reproducibility."),
        ("Capacity Utilization:", " Normalized to a realistic range of 0% to 100% (with extreme overflow allowance up to 120% for standing halls).")
    ]
    for k, v in out1_points:
        p = tf_out1.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)

    # Right Card: Glitch Removal
    c_out2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_out2.fill.solid()
    c_out2.fill.fore_color.rgb = C_CARD
    c_out2.line.color.rgb = C_BORDER
    tf_out2 = c_out2.text_frame
    tf_out2.word_wrap = True
    tf_out2.margin_left = Inches(0.3)
    tf_out2.margin_top = Inches(0.3)
    
    p = tf_out2.paragraphs[0]
    p.text = "GLITCH & IMPOSSIBLE NUMBER PURGE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p.space_after = Pt(14)
    
    out2_points = [
        ("Dummy Registrations (1,253 entries):", " Found values like '99999'. Replaced with realistic 85% venue capacity."),
        ("Extreme Student Ratings (30 entries):", " Fixed satisfaction ratings entered as high as 99 back to the valid 1.0–5.0 ceiling."),
        ("Absurd Ticket Prices (30 entries):", " Errors up to $15,000 for student workshops capped down to standard $0–$100 prices."),
        ("Negative Values Repaired:", " Corrected 461 negative attendance counts and 40 negative budgets (e.g., -$50,000) using absolute medians.")
    ]
    for k, v in out2_points:
        p = tf_out2.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 8: Comparative Analysis & KPIs
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "Key Comparative Analysis & Performance Metrics", category="EXECUTIVE KPIS")
    
    # 4 KPI Top Cards
    kpi_defs = [
        ("TOTAL VERIFIED EVENTS", "14,750", "4,750 IIT | 10,000 Univ", C_BLUE, Inches(0.8)),
        ("TOTAL CLEANED FOOTFALL", "13.12M", "9.24M IIT | 3.88M Univ", C_GREEN, Inches(3.8)),
        ("OVERALL FINANCIAL YIELD", "$13.97M / ₹359 Cr", "Revenue & Budgets", C_PURPLE, Inches(6.8)),
        ("AVERAGE TURNOUT RATE", "65.2%", "Consistent Engagement", C_AMBER, Inches(9.8))
    ]
    for title, val, sub, color, left_pos in kpi_defs:
        k_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(1.8), Inches(2.7), Inches(1.6))
        k_card.fill.solid()
        k_card.fill.fore_color.rgb = C_CARD
        k_card.line.color.rgb = C_BORDER
        tf_k = k_card.text_frame
        tf_k.word_wrap = True
        tf_k.margin_left = Inches(0.2)
        tf_k.margin_top = Inches(0.2)
        
        pk1 = tf_k.paragraphs[0]
        pk1.text = title
        pk1.font.size = Pt(9)
        pk1.font.bold = True
        pk1.font.color.rgb = C_MUTED
        
        pk2 = tf_k.add_paragraph()
        pk2.text = val
        pk2.font.size = Pt(20)
        pk2.font.bold = True
        pk2.font.color.rgb = color
        
        pk3 = tf_k.add_paragraph()
        pk3.text = sub
        pk3.font.size = Pt(9)
        pk3.font.color.rgb = C_TEXT

    # Comparative Table below
    table_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.7), Inches(11.7), Inches(3.1))
    table_card.fill.solid()
    table_card.fill.fore_color.rgb = C_CARD
    table_card.line.color.rgb = C_BORDER
    tf_tbl = table_card.text_frame
    tf_tbl.word_wrap = True
    tf_tbl.margin_left = Inches(0.4)
    tf_tbl.margin_top = Inches(0.3)
    
    p = tf_tbl.paragraphs[0]
    p.text = "CROSS-INSTITUTIONAL BENCHMARK SUMMARY"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)
    
    comp_points = [
        ("Event Scale Comparison:", " IIT events are large-scale campus gatherings (avg 1,946 attendees/event) compared to University's workshop/seminar model (avg 388 attendees/event)."),
        ("Financial Operating Models:", " University events generate significant commercial revenue ($13.97M surplus across ticketing and sponsors), while IIT events operate under institutional grant allocations (₹359.1 Cr budget)."),
        ("Turnout Consistency:", " Both institutions demonstrated healthy attendance ratios (IIT: 66.1%, University: 64.3%), proving strong post-registration commitment."),
        ("Student CSAT & Satisfaction:", " University recorded high satisfaction (4.29 / 5.0). IIT averaged 2.98 / 5.0, signaling clear logistical optimization opportunities for high-volume technical festivals.")
    ]
    for k, v in comp_points:
        p = tf_tbl.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(6)

    # ==========================================
    # SLIDE 9: Dashboard Visualizations 1 - 2D
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "Dashboard Visualizations: 2D Operational Charts", category="VISUAL ANALYTICS")
    
    # 3 Column Cards for 2D charts
    charts_2d = [
        ("1. Monthly Trends (Line Graph)", 
         "Tracks footfall and net revenue over the 12-month calendar. Reveals two massive seasonal peaks: during August/September orientations and post-midterm festival seasons (Jan/Feb).", 
         C_BLUE, Inches(0.8)),
        ("2. Unit Performance (Bar Chart)", 
         "Compares revenue and turnout across all 11 IIT campuses and 7 University departments. Proves Haas Business, Berkeley Law, EECS, and IIT Kharagpur drive majority engagement.", 
         C_PURPLE, Inches(4.75)),
        ("3. Category Mix & Yield (Pie & Scatter)", 
         "Shows balanced event distribution across Academic, Cultural, Sports, and Workshops (~16% each). Scatter plot confirms positive correlation between budget invested and turnout.", 
         C_GREEN, Inches(8.7))
    ]
    for title, desc, color, left_pos in charts_2d:
        ch_card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(1.8), Inches(3.8), Inches(4.9))
        ch_card.fill.solid()
        ch_card.fill.fore_color.rgb = C_CARD
        ch_card.line.color.rgb = C_BORDER
        tf_ch = ch_card.text_frame
        tf_ch.word_wrap = True
        tf_ch.margin_left = Inches(0.3)
        tf_ch.margin_top = Inches(0.3)
        
        p = tf_ch.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(14)
        
        p2 = tf_ch.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = C_MUTED
        p2.space_after = Pt(14)
        
        p3 = tf_ch.add_paragraph()
        p3.text = "Key Takeaway:"
        p3.font.bold = True
        p3.font.size = Pt(12)
        p3.font.color.rgb = C_TEXT
        
        p4 = tf_ch.add_paragraph()
        p4.text = "Enables executive administrators to optimize venue staffing, security deployment, and schedule spacing to prevent campus bottlenecks."
        p4.font.size = Pt(11)
        p4.font.color.rgb = C_MUTED

    # ==========================================
    # SLIDE 10: Dashboard Visualizations 2 - 3D & Quality
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "Dashboard Visualizations: 3D Spatial Models & Audit", category="ADVANCED ANALYTICS")
    
    # Left Card: 3D Models
    c_3d = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_3d.fill.solid()
    c_3d.fill.fore_color.rgb = C_CARD
    c_3d.line.color.rgb = C_BORDER
    tf_3d = c_3d.text_frame
    tf_3d.word_wrap = True
    tf_3d.margin_left = Inches(0.3)
    tf_3d.margin_top = Inches(0.3)
    
    p = tf_3d.paragraphs[0]
    p.text = "INTERACTIVE 3D WEBGL VISUALIZATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(14)
    
    points_3d = [
        ("3D Scatter Plot (Budget vs. Attendance vs. CSAT):", " Users rotate a 360° point cloud to isolate top-rated events with minimal financial footprints."),
        ("3D Topographic Surface Mesh:", " Continuous terrain topography mapping average turnout rates across departments vs. event categories, highlighting engagement peaks and low-turnout valleys."),
        ("3D Time-Space Trajectory Curve:", " Traces how footfall, event counts, and student ratings evolve together along a continuous temporal 3D helical path.")
    ]
    for k, v in points_3d:
        p = tf_3d.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)

    # Right Card: Audit Gauges & Certification
    c_aud = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_aud.fill.solid()
    c_aud.fill.fore_color.rgb = C_CARD
    c_aud.line.color.rgb = C_BORDER
    tf_aud = c_aud.text_frame
    tf_aud.word_wrap = True
    tf_aud.margin_left = Inches(0.3)
    tf_aud.margin_top = Inches(0.3)
    
    p = tf_aud.paragraphs[0]
    p.text = "DATA QUALITY AUDIT GAUGES & SUMMARY"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(14)
    
    points_aud = [
        ("Missing Values Mitigation Gauge:", " Real-time visual dial showing missing fields plummeting from ~10% down to 0% across all records."),
        ("Capacity Law Compliance Meter:", " Confirms 100% adherence to physical venue safety limits with zero uncapped fire-code breaches."),
        ("Searchable Live Data Table:", " Embedded interactive data table with instant search, category filtering, and one-click CSV export."),
        ("Final Evaluation:", " Complete end-to-end data pipeline: from messy multi-source data to validated executive intelligence.")
    ]
    for k, v in points_aud:
        p = tf_aud.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {k}"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_TEXT
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_MUTED
        p.space_after = Pt(8)

    # Save presentation
    output_path = os.path.join(base_dir, "Campus_Event_Analytics_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == "__main__":
    build_presentation()

