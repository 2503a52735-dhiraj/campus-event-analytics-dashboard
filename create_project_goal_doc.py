import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def generate_goal_document():
    doc = docx.Document()
    
    # 0.8 inch margins for balanced 2-page academic layout
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    COLOR_PRIMARY = RGBColor(16, 44, 87)     # Navy #102C57
    COLOR_SECONDARY = RGBColor(41, 128, 185) # Blue #2980B9
    COLOR_DARK = RGBColor(33, 37, 41)        # Off-black #212529
    
    # Title: 1. PROJECT GOAL
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_num = p_title.add_run("SECTION 1: PROJECT GOAL\n")
    r_num.font.name = "Arial"
    r_num.font.size = Pt(11)
    r_num.font.bold = True
    r_num.font.color.rgb = COLOR_SECONDARY
    
    r_main = p_title.add_run("Executive Scope, Problem Context & Analytical Architecture")
    r_main.font.name = "Arial"
    r_main.font.size = Pt(17)
    r_main.font.bold = True
    r_main.font.color.rgb = COLOR_PRIMARY

    # Divider line
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(10)
    r_div = p_div.add_run("―" * 58)
    r_div.font.color.rgb = COLOR_SECONDARY
    r_div.font.size = Pt(12)

    # 1.1 Context: What Problem We Are Solving and Why It Matters
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(4)
    p_h1.paragraph_format.space_after = Pt(4)
    r_h1 = p_h1.add_run("1.1 Operational Context: What Problem We Are Solving and Why It Matters")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(12)
    r_h1.font.bold = True
    r_h1.font.color.rgb = COLOR_PRIMARY

    p_c1 = doc.add_paragraph()
    p_c1.paragraph_format.line_spacing = 1.15
    p_c1.paragraph_format.space_after = Pt(6)
    r_c1 = p_c1.add_run(
        "Modern academic institutions host thousands of curricular, co-curricular, technical, and cultural events every year to "
        "enrich campus life, cultivate industry partnerships, and advance multidisciplinary research. However, institutional event administrators "
        "routinely operate in a critical operational blind spot. Across universities, leadership faces persistent challenges including severe "
        "turnout attrition between initial online registrations and actual event-day footfall (routinely losing 25% to 35% of registered participants as "
        "'no-shows'), chronic venue capacity misallocations where auditoriums are either dangerously packed past legal fire-code safety thresholds or "
        "left largely vacant, and substantial fiscal leakages where high-budget mega-events fail to produce proportionate participant satisfaction."
    )
    r_c1.font.name = "Arial"
    r_c1.font.size = Pt(10)
    r_c1.font.color.rgb = COLOR_DARK

    p_c2 = doc.add_paragraph()
    p_c2.paragraph_format.line_spacing = 1.15
    p_c2.paragraph_format.space_after = Pt(8)
    r_c2 = p_c2.add_run(
        "Why This Matters: Higher education institutions allocate substantial portions of their annual operating capital and institutional grants "
        "toward student activities. When event records are fractured across departments and heavily contaminated with system anomalies—such as duplicate "
        "signups, negative financial budget allocations, impossible rating scale values up to 99 on a 5-point scale, and dummy placeholder codes (e.g., 99,999)—"
        "administrators are rendered incapable of performing reliable capacity forecasting, budgetary auditing, or cross-institutional benchmarking. "
        "Solving this problem is vital because universities cannot afford fiscal waste, compromised campus safety, or unverified governance. By engineering an "
        "automated data cleansing pipeline coupled with interactive visual intelligence, this project converts raw, corrupted administrative spreadsheets "
        "into verifiable, executive decision support."
    )
    r_c2.font.name = "Arial"
    r_c2.font.size = Pt(10)
    r_c2.font.color.rgb = COLOR_DARK

    # 1.2 Clear Problem Statement (3 to 5 Sentences)
    p_h2 = doc.add_paragraph()
    p_h2.paragraph_format.space_before = Pt(6)
    p_h2.paragraph_format.space_after = Pt(4)
    r_h2 = p_h2.add_run("1.2 Problem Statement (Cohesive 4-Sentence Definition)")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(12)
    r_h2.font.bold = True
    r_h2.font.color.rgb = COLOR_PRIMARY

    # Highlight box for Problem Statement
    tbl_ps = doc.add_table(rows=1, cols=1)
    tbl_ps.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
    tbl_ps.autofit = False
    tbl_ps.columns[0].width = Inches(6.9)
    cell_ps = tbl_ps.cell(0, 0)
    set_cell_background(cell_ps, "F0F4F8")
    set_cell_margins(cell_ps, top=100, bottom=100, left=140, right=140)

    p_box = cell_ps.paragraphs[0]
    p_box.paragraph_format.line_spacing = 1.15
    p_box.paragraph_format.space_after = Pt(0)

    sentences = [
        ("[Sentence 1 - Operational Breakdown] ", True),
        ("Higher education institutions experience persistent operational inefficiencies characterized by high participant attrition between online registrations and actual event turnouts, recurring physical venue capacity misallocations, and substantial fiscal leakages where high capital expenditures fail to generate proportionate student satisfaction.\n", False),
        ("[Sentence 2 - Data Contamination] ", True),
        ("Simultaneously, institutional decision-makers are hindered by disparate, raw event datasets contaminated with duplicate entries, missing attributes, negative budget allocations, and erroneous rating bounds that obscure true campus performance metrics.\n", False),
        ("[Sentence 3 - Analytical Void] ", True),
        ("Without automated data cleansing protocols and comparative cross-institutional benchmarks, leadership cannot accurately forecast facility utilization, measure event ROI, or eliminate wasteful spending.\n", False),
        ("[Sentence 4 - Engineering Solution] ", True),
        ("This project resolves this critical void by engineering an end-to-end automated data sanitization pipeline paired with an interactive 2D and 3D visualization dashboard to deliver certified, data-driven executive decision support across Indian (IIT) and global university event operations.", False)
    ]
    for txt, is_b in sentences:
        r = p_box.add_run(txt)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = is_b
        r.font.color.rgb = COLOR_PRIMARY if is_b else COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # 1.3 Objectives of the Project
    p_h3 = doc.add_paragraph()
    p_h3.paragraph_format.space_before = Pt(6)
    p_h3.paragraph_format.space_after = Pt(4)
    r_h3 = p_h3.add_run("1.3 Objectives of the Project")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(12)
    r_h3.font.bold = True
    r_h3.font.color.rgb = COLOR_PRIMARY

    objs = [
        ("1. Automated Data Engineering & Sanitization: ",
         "To construct an automated data hygiene pipeline capable of auditing 15,300 raw event entries, purging 100% of duplicate rows (550 records eliminated), contextually imputing missing values, and mathematically enforcing physical venue safety bounds."),
        ("2. Statistical & Behavioral Modeling: ",
         "To conduct rigorous statistical profiling across 11 IIT institutes and 7 university departments to quantify turnout conversion rates, venue capacity utilization, and model the empirical correlation between financial expenditure and student satisfaction (CSAT)."),
        ("3. Cross-Institutional Operational Benchmarking: ",
         "To systematically benchmark two distinct institutional operating models—India's public grant-supported IIT system versus the commercial ticketing and corporate sponsorship model of global universities (UC Berkeley)."),
        ("4. Multidimensional 2D & 3D Interactive Visualization: ",
         "To design, develop, and deploy a responsive WebGL 3D visualization platform and executive dashboard featuring 30+ interactive charts (3D Scatter, Topographic Terrain, and Trajectory curves) alongside real-time data audit gauges.")
    ]
    for o_head, o_body in objs:
        p_o = doc.add_paragraph()
        p_o.paragraph_format.line_spacing = 1.15
        p_o.paragraph_format.space_after = Pt(3)
        ro_h = p_o.add_run(o_head)
        ro_h.font.name = "Arial"
        ro_h.font.size = Pt(9.5)
        ro_h.font.bold = True
        ro_h.font.color.rgb = COLOR_SECONDARY
        ro_b = p_o.add_run(o_body)
        ro_b.font.name = "Arial"
        ro_b.font.size = Pt(9.5)
        ro_b.font.color.rgb = COLOR_DARK

    # -------------------------------------------------------------
    # PAGE BREAK -> PAGE 2: RESEARCH QUESTIONS & STRATEGIC OUTCOMES
    # -------------------------------------------------------------
    doc.add_page_break()

    # 1.4 Specific Analytical Questions Answered
    p_h4 = doc.add_paragraph()
    p_h4.paragraph_format.space_before = Pt(4)
    p_h4.paragraph_format.space_after = Pt(4)
    r_h4 = p_h4.add_run("1.4 Specific Analytical Questions Answered by the Project")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(12)
    r_h4.font.bold = True
    r_h4.font.color.rgb = COLOR_PRIMARY

    p_qdesc = doc.add_paragraph()
    p_qdesc.paragraph_format.line_spacing = 1.15
    p_qdesc.paragraph_format.space_after = Pt(6)
    r_qd = p_qdesc.add_run(
        "To provide actionable clarity for institutional administrators, the analytical pipeline and dashboard models "
        "directly resolve five critical operational and behavioral research questions:"
    )
    r_qd.font.name = "Arial"
    r_qd.font.size = Pt(10)
    r_qd.font.color.rgb = COLOR_DARK

    questions_data = [
        ("Q1. Financial Expenditure vs. Student Delight (The Budget Paradox)",
         "What is the true empirical correlation between event financial expenditure and student satisfaction ratings? Does higher budget guarantee higher feedback?",
         "Analytical Resolution: Pearson correlation analysis demonstrates a virtually zero dependency (r = 0.042, p > 0.05). This disproves the common assumption that higher budgets produce happier attendees; lavish events often suffer from crowd control bottlenecks, while low-cost, focused technical hackathons yield significantly higher peer satisfaction."),
        
        ("Q2. Turnout & Attrition Dynamics Across Event Categories",
         "How does attendee attrition vary across functional categories (Technical, Cultural, Sports, Academic, E-Cell)? Which categories maximize venue fill?",
         "Analytical Resolution: Technical (77.4%) and Cultural (76.1%) fests exhibit the highest conversion rates, while Academic seminars experience higher attrition (~32%) but tighter variance. Registrations and actual attendance maintain a strong linear correlation (r = 0.878, R² = 0.771), enabling precise predictive room reservations."),
        
        ("Q3. Revenue Generation & Fiscal Self-Sufficiency",
         "How do ticketing structures and corporate sponsorships influence net event margins and departmental ROI across different faculties?",
         "Analytical Resolution: Global university departments generated $13.97 Million in net surplus, led by Career Fairs and Law School conferences ($14,500 net profit per event). Conversely, undergraduate social and intramural sporting events operate at a planned deficit (-$1,200/event) subsidized by student activity fees."),
        
        ("Q4. Data Hygiene & Integrity Quantification",
         "What proportion of institutional event records is contaminated by human entry error, duplicate rows, dummy codes, and scale violations prior to automated sanitization?",
         "Analytical Resolution: 3.59% of raw records represented duplicate entries (550 records purged). Furthermore, 1,253 entries contained '99999' dummy registrations, 321 records breached physical venue limits, and 30 satisfaction scores violated the 5.0 ceiling (some reaching 99.0), proving that 18.6% of raw rows required cleaning."),
        
        ("Q5. Multi-Axis Interaction in 3D Coordinate Space",
         "Can multidimensional 3D parameter terrains (Budget × Attendance × CSAT) expose non-linear operational dynamics undetectable in flat 2D projections?",
         "Analytical Resolution: 3D WebGL spatial meshes reveal high-altitude engagement ridges and isolate optimal 'high-satisfaction, low-cost' events, while temporal 3D trajectory curves expose sharp biannual footfall drops during semester exam cycles (May/June & Dec) followed by orientation peaks.")
    ]

    for q_title, q_prob, q_ans in questions_data:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.line_spacing = 1.15
        p_item.paragraph_format.space_after = Pt(4)
        
        r_qt = p_item.add_run(f"• {q_title}\n")
        r_qt.font.name = "Arial"
        r_qt.font.size = Pt(9.5)
        r_qt.font.bold = True
        r_qt.font.color.rgb = COLOR_PRIMARY
        
        r_qp = p_item.add_run(f"  Target Question: {q_prob}\n")
        r_qp.font.name = "Arial"
        r_qp.font.size = Pt(9)
        r_qp.font.italic = True
        r_qp.font.color.rgb = COLOR_SECONDARY
        
        r_qa = p_item.add_run(f"  {q_ans}")
        r_qa.font.name = "Arial"
        r_qa.font.size = Pt(9)
        r_qa.font.color.rgb = COLOR_DARK

    # 1.5 Expected Outcomes & Strategic Utility
    p_h5 = doc.add_paragraph()
    p_h5.paragraph_format.space_before = Pt(6)
    p_h5.paragraph_format.space_after = Pt(4)
    r_h5 = p_h5.add_run("1.5 Strategic Administrative Significance & Governance Impact")
    r_h5.font.name = "Arial"
    r_h5.font.size = Pt(12)
    r_h5.font.bold = True
    r_h5.font.color.rgb = COLOR_PRIMARY

    p_imp = doc.add_paragraph()
    p_imp.paragraph_format.line_spacing = 1.15
    p_imp.paragraph_format.space_after = Pt(4)
    r_imp = p_imp.add_run(
        "By systematically addressing the project goal, this work provides immediate operational utility for University Registrars, "
        "Deans of Student Affairs, and Student Activity Councils: (1) Dynamic venue reservation calibrated at 75% of signups prevents 20%–30% in "
        "oversized facility rental waste; (2) Commitment micro-ticketing reduces absentee attrition from 32% down to 8%; and (3) Automated ETL data pipelines "
        "replace error-prone spreadsheets with verified executive intelligence, establishing an auditable, data-driven institutional culture."
    )
    r_imp.font.name = "Arial"
    r_imp.font.size = Pt(9.5)
    r_imp.font.color.rgb = COLOR_DARK

    # Sign-off line
    p_end = doc.add_paragraph()
    p_end.paragraph_format.space_before = Pt(8)
    p_end.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_end = p_end.add_run("SR University — Course: Data Analytics & Visualization (25CAI202PC201)")
    r_end.font.name = "Arial"
    r_end.font.size = Pt(8.5)
    r_end.font.italic = True
    r_end.font.color.rgb = COLOR_SECONDARY

    out_file = r"c:\Users\gandi\OneDrive\Desktop\davproject\Project_Goal.docx"
    doc.save(out_file)
    print(f"Project Goal document saved to: {out_file}")

if __name__ == "__main__":
    generate_goal_document()
