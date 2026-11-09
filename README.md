# Campus Event Analytics & Interactive Visualization Dashboard

A comprehensive data analytics and visualization system for auditing, cleaning, and comparing multi-institutional campus event data across 11 IIT campuses and 7 university departments.

## 👥 Team Members
* **2503A52735** - G. Dhiraj Kumar
* **2503A52742** - P. John David
* **2503A52743** - S. Jashwanth

---

## 📌 Project Overview
* **Datasets Harmonized:**
  1. **IIT Campus Events:** 5,100 raw events $\rightarrow$ 4,750 cleaned records across 11 IIT campuses.
  2. **University Events (UC Berkeley):** 10,200 raw events $\rightarrow$ 10,000 cleaned records across 7 host departments.
* **Combined Scale:** 15,300 raw event entries curated to 14,750 verified records (550 duplicates removed).
* **Data Quality Score:** Improved from 81.4% (raw) to 100% (cleaned and validated).

---

## 🧹 Data Cleaning (In Simple Words)
1. **Duplicate Pruning:** Removed 350 exact duplicate rows in the IIT dataset and 200 duplicate records/Event IDs in the University dataset.
2. **Text Normalization:** Standardized all campus names into clean Title Case and resolved category typos (`'Acad'` $\rightarrow$ `'Academic'`, `'Culturall'` $\rightarrow$ `'Cultural'`).
3. **Missing Value Imputation:**
   * Missing campuses filled with `'IIT Main Campus'`; missing categories with `'General / Academic'`.
   * Missing attendance calculated from registrations and median turnout (70%–75%).
   * Missing budgets imputed using category medians; missing sponsorships set to $0.
4. **Physical Venue Capacity Law:** Where attendance exceeded venue capacity, attendance was capped to physical hall limits with raw values archived in an audit log.
5. **Glitch & Outlier Removal:** Purged 1,253 dummy registration placeholders (`'99999'`) and capped ratings entered $> 5.0$ (up to 99) back into the 1.0–5.0 range. Repaired 461 negative attendance figures and 40 negative budgets.

---

## 📊 Dashboard & Visualizations
* **Live HTML Dashboard (`index.html` / `dashboard.html`):** Full standalone interactive dashboard featuring Plotly.js charts, searchable data explorer, and KPI gauges.
* **Interactive 3D WebGL Charts:**
  * **3D Scatter Plot:** Budget vs. Attendance vs. Satisfaction (CSAT/Rating).
  * **3D Topographic Surface Mesh:** Turnout rate terrain across departments/campuses vs. categories.
  * **3D Time-Space Trajectory Curve:** Temporal evolution of footfall and CSAT over time.
* **Streamlit Application (`app.py`):** Multi-tab deep-dive analytics application with real-time filters.
* **Project Presentation (`Campus_Event_Analytics_Presentation.pptx` / `presentation.html`):** 10-slide executive presentation.

---

## 🚀 How to Run Locally

### 1. Standalone HTML Dashboard
Simply open `index.html` or `dashboard.html` in any web browser, or serve via Python:
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000`.

### 2. Streamlit Dashboard
```bash
pip install -r requirements.txt
streamlit run app.py
```
