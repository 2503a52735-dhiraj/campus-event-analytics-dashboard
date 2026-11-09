import os

base_dir = r"c:\Users\gandi\OneDrive\Desktop\davproject"

with open(os.path.join(base_dir, "build_html_dashboard.py"), "r", encoding="utf-8") as f:
    code = f.read()

# Filter styling
filter_css = """
        /* ============================================================== */
        /* INTERACTIVE MASTER DASHBOARD FILTER SYSTEM */
        /* ============================================================== */
        .interactive-filter-banner {
            background: linear-gradient(145deg, #0d1527, #131d33);
            border: 1px solid #253556;
            border-radius: var(--radius-lg);
            padding: 22px 26px;
            margin-bottom: 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
            position: relative;
            overflow: hidden;
        }

        .interactive-filter-banner::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, #38bdf8, #a855f7, #f472b6, #34d399);
        }

        .filter-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid #1e2c47;
        }

        .filter-title-wrap {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .filter-icon-box {
            width: 44px;
            height: 44px;
            border-radius: 10px;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            color: #38bdf8;
        }

        .filter-header h4 {
            font-size: 1.25rem;
            font-weight: 800;
            color: #f8fafc;
            letter-spacing: -0.01em;
        }

        .filter-header p {
            font-size: 0.85rem;
            color: #94a3b8;
            margin-top: 2px;
        }

        .filter-actions {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .filter-stats-pill {
            background: rgba(52, 211, 153, 0.15);
            border: 1px solid rgba(52, 211, 153, 0.35);
            color: #34d399;
            font-size: 0.84rem;
            font-weight: 700;
            padding: 7px 14px;
            border-radius: 20px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-filter-reset {
            background: #1e293b;
            border: 1px solid #334155;
            color: #f1f5f9;
            padding: 7px 16px;
            border-radius: 8px;
            font-size: 0.84rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
        }

        .btn-filter-reset:hover {
            background: #334155;
            color: #38bdf8;
            border-color: #38bdf8;
            transform: translateY(-1px);
        }

        .filter-controls-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 14px;
            margin-bottom: 20px;
        }

        .filter-control-item {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .filter-control-item label {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #94a3b8;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .filter-control-item select,
        .filter-control-item input {
            background: #090e1a;
            border: 1px solid #23324d;
            border-radius: 8px;
            color: #f8fafc;
            padding: 9px 12px;
            font-size: 0.88rem;
            font-weight: 600;
            outline: none;
            transition: all 0.2s;
            width: 100%;
        }

        .filter-control-item select:focus,
        .filter-control-item input:focus {
            border-color: #38bdf8;
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
        }

        .dynamic-kpi-strip {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 12px;
            background: rgba(10, 15, 26, 0.6);
            border: 1px solid #1c273e;
            border-radius: var(--radius-md);
            padding: 14px 18px;
        }

        @media (max-width: 900px) {
            .dynamic-kpi-strip { grid-template-columns: repeat(2, 1fr); }
            .filter-controls-grid { grid-template-columns: 1fr; }
        }

        .kpi-mini-card {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .kpi-mini-lbl {
            font-size: 0.74rem;
            text-transform: uppercase;
            font-weight: 700;
            color: #64748b;
            letter-spacing: 0.04em;
        }

        .kpi-mini-val {
            font-size: 1.45rem;
            font-weight: 800;
            color: #f8fafc;
            font-family: 'JetBrains Mono', monospace;
            line-height: 1.2;
        }

        .kpi-mini-sub {
            font-size: 0.75rem;
            color: #94a3b8;
        }
"""

# Filter HTML block
filter_html = """
    <!-- ============================================================== -->
    <!-- INTERACTIVE MASTER DASHBOARD FILTER SYSTEM -->
    <!-- ============================================================== -->
    <div class="interactive-filter-banner">
        <div class="filter-header">
            <div class="filter-title-wrap">
                <div class="filter-icon-box">
                    <i class="fa-solid fa-sliders"></i>
                </div>
                <div>
                    <h4>Interactive Live Dashboard Filters</h4>
                    <p>Select any criteria below to dynamically update all 2D/3D charts, KPIs, time series, and distributions in real time</p>
                </div>
            </div>
            <div class="filter-actions">
                <span id="filterStatsPill" class="filter-stats-pill">
                    <i class="fa-solid fa-database"></i> Showing 14,750 / 14,750 Events (100%)
                </span>
                <button class="btn-filter-reset" onclick="resetAllFilters()">
                    <i class="fa-solid fa-rotate-left"></i> Reset All Filters
                </button>
            </div>
        </div>

        <!-- 6 Interactive Filter Selectors -->
        <div class="filter-controls-grid">
            <!-- 1. Dataset Selector -->
            <div class="filter-control-item">
                <label><i class="fa-solid fa-building-columns" style="color:#38bdf8;"></i> Institution Dataset</label>
                <select id="filterDataset" onchange="onDatasetFilterChange()">
                    <option value="all">🌐 All Institutions (Combined)</option>
                    <option value="iit">🇮🇳 IIT Campus Events</option>
                    <option value="ucb">🇺🇸 University Events (UCB)</option>
                </select>
            </div>

            <!-- 2. Category Selector -->
            <div class="filter-control-item">
                <label><i class="fa-solid fa-tags" style="color:#a855f7;"></i> Event Category</label>
                <select id="filterCategory" onchange="applyGlobalFilters()">
                    <option value="all">All Categories</option>
                    <option value="Academic">Academic</option>
                    <option value="Technical">Technical</option>
                    <option value="Cultural">Cultural</option>
                    <option value="Sports">Sports</option>
                    <option value="Career">Career</option>
                    <option value="Workshop">Workshop</option>
                    <option value="Social">Social</option>
                    <option value="Research">Research</option>
                    <option value="E-Cell">E-Cell</option>
                </select>
            </div>

            <!-- 3. Campus / Department Selector -->
            <div class="filter-control-item">
                <label><i class="fa-solid fa-map-location-dot" style="color:#f472b6;"></i> Campus / Department</label>
                <select id="filterUnit" onchange="applyGlobalFilters()">
                    <option value="all">All Campuses & Departments</option>
                </select>
            </div>

            <!-- 4. Academic Year -->
            <div class="filter-control-item">
                <label><i class="fa-solid fa-calendar-days" style="color:#34d399;"></i> Academic Year</label>
                <select id="filterYear" onchange="applyGlobalFilters()">
                    <option value="all">All Years (2023 - 2026)</option>
                    <option value="2023">2023</option>
                    <option value="2024">2024</option>
                    <option value="2025">2025</option>
                    <option value="2026">2026</option>
                </select>
            </div>

            <!-- 5. Rating Tier -->
            <div class="filter-control-item">
                <label><i class="fa-solid fa-star" style="color:#fbbf24;"></i> Student CSAT Rating</label>
                <select id="filterRating" onchange="applyGlobalFilters()">
                    <option value="all">All Rating Tiers</option>
                    <option value="high">⭐ High (4.0 - 5.0)</option>
                    <option value="med">⭐ Medium (3.0 - 3.9)</option>
                    <option value="low">⭐ Needs Focus (&lt; 3.0)</option>
                </select>
            </div>

            <!-- 6. Keyword Search -->
            <div class="filter-control-item">
                <label><i class="fa-solid fa-magnifying-glass" style="color:#38bdf8;"></i> Keyword Search</label>
                <input type="text" id="filterKeyword" placeholder="Filter by event name, venue..." onkeyup="applyGlobalFilters()">
            </div>
        </div>

        <!-- Dynamic Live KPI Strip -->
        <div class="dynamic-kpi-strip">
            <div class="kpi-mini-card">
                <span class="kpi-mini-lbl">Filtered Events</span>
                <span id="kpiFilteredEvents" class="kpi-mini-val">14,750</span>
                <span class="kpi-mini-sub">Active Records</span>
            </div>
            <div class="kpi-mini-card">
                <span class="kpi-mini-lbl">Total Footfall</span>
                <span id="kpiFilteredFootfall" class="kpi-mini-val" style="color: #38bdf8;">13.12M</span>
                <span class="kpi-mini-sub">Actual Attendees</span>
            </div>
            <div class="kpi-mini-card">
                <span class="kpi-mini-lbl">Avg Turnout Rate</span>
                <span id="kpiFilteredTurnout" class="kpi-mini-val" style="color: #34d399;">64.9%</span>
                <span class="kpi-mini-sub">Conversion Yield</span>
            </div>
            <div class="kpi-mini-card">
                <span class="kpi-mini-lbl">Avg Satisfaction</span>
                <span id="kpiFilteredRating" class="kpi-mini-val" style="color: #fbbf24;">3.87 ⭐</span>
                <span class="kpi-mini-sub">Feedback Rating</span>
            </div>
            <div class="kpi-mini-card">
                <span class="kpi-mini-lbl">Financial Scale</span>
                <span id="kpiFilteredFinance" class="kpi-mini-val" style="color: #a78bfa;">₹359Cr / $13.9M</span>
                <span class="kpi-mini-sub">Budgets & Net Surplus</span>
            </div>
        </div>
    </div>
"""

# JavaScript Engine for Filter Handling & Live Graph Updates
filter_js = """
        // ==============================================================
        // DYNAMIC FILTER ENGINE & REAL-TIME GRAPH SYNCHRONIZATION
        // ==============================================================
        let allEvents = dashboardData.all_events || [];
        // Schema: [ds, id, name, unit, cat, yr, mo, att, reg, cap, bud, rat, to, rev]
        
        function initFilterControls() {
            populateUnitDropdown('all');
            applyGlobalFilters();
        }

        function onDatasetFilterChange() {
            const ds = document.getElementById('filterDataset').value;
            populateUnitDropdown(ds);
            applyGlobalFilters();
        }

        function populateUnitDropdown(ds) {
            const unitSelect = document.getElementById('filterUnit');
            if (!unitSelect) return;
            const currentVal = unitSelect.value;
            
            let html = '<option value="all">All Campuses & Departments</option>';
            
            if (ds === 'all' || ds === 'iit') {
                html += '<optgroup label="🇮🇳 IIT Campuses">';
                (dashboardData.campuses || []).forEach(c => {
                    html += `<option value="${c}">${c}</option>`;
                });
                html += '</optgroup>';
            }
            
            if (ds === 'all' || ds === 'ucb') {
                html += '<optgroup label="🇺🇸 UCB Faculties & Departments">';
                (dashboardData.depts || []).forEach(d => {
                    html += `<option value="${d}">${d}</option>`;
                });
                html += '</optgroup>';
            }
            
            unitSelect.innerHTML = html;
            if (currentVal && Array.from(unitSelect.options).some(o => o.value === currentVal)) {
                unitSelect.value = currentVal;
            } else {
                unitSelect.value = 'all';
            }
        }

        function resetAllFilters() {
            document.getElementById('filterDataset').value = 'all';
            document.getElementById('filterCategory').value = 'all';
            document.getElementById('filterYear').value = 'all';
            document.getElementById('filterRating').value = 'all';
            document.getElementById('filterKeyword').value = '';
            populateUnitDropdown('all');
            applyGlobalFilters();
        }

        let filteredEventsGlobal = [];

        function applyGlobalFilters() {
            const dsVal = document.getElementById('filterDataset')?.value || 'all';
            const catVal = document.getElementById('filterCategory')?.value || 'all';
            const unitVal = document.getElementById('filterUnit')?.value || 'all';
            const yrVal = document.getElementById('filterYear')?.value || 'all';
            const ratVal = document.getElementById('filterRating')?.value || 'all';
            const kwVal = (document.getElementById('filterKeyword')?.value || '').trim().toLowerCase();

            // Filter the full dataset
            filteredEventsGlobal = allEvents.filter(e => {
                if (dsVal !== 'all' && e[0] !== dsVal) return false;
                if (catVal !== 'all' && !e[4].toLowerCase().includes(catVal.toLowerCase())) return false;
                if (unitVal !== 'all' && e[3] !== unitVal) return false;
                if (yrVal !== 'all' && String(e[5]) !== yrVal) return false;
                if (ratVal === 'high' && e[11] < 4.0) return false;
                if (ratVal === 'med' && (e[11] < 3.0 || e[11] >= 4.0)) return false;
                if (ratVal === 'low' && e[11] >= 3.0) return false;
                if (kwVal) {
                    const matchName = e[2].toLowerCase().includes(kwVal);
                    const matchUnit = e[3].toLowerCase().includes(kwVal);
                    const matchCat = e[4].toLowerCase().includes(kwVal);
                    if (!matchName && !matchUnit && !matchCat) return false;
                }
                return true;
            });

            // 1. Update KPI Strip
            updateDynamicKPIs(filteredEventsGlobal);

            // 2. Synchronize Graphs with Filtered Data
            updateFilteredCharts(filteredEventsGlobal, dsVal);

            // 3. Update Data Table Explorer
            updateExplorerTableWithFiltered(filteredEventsGlobal);
        }

        function updateDynamicKPIs(events) {
            const count = events.length;
            const totalFootfall = events.reduce((sum, e) => sum + e[7], 0);
            const avgTurnout = count > 0 ? (events.reduce((sum, e) => sum + e[12], 0) / count).toFixed(1) : 0;
            const avgRating = count > 0 ? (events.reduce((sum, e) => sum + e[11], 0) / count).toFixed(2) : 0;
            
            const iitEvents = events.filter(e => e[0] === 'iit');
            const ucbEvents = events.filter(e => e[0] === 'ucb');
            const iitBudgetCr = (iitEvents.reduce((sum, e) => sum + e[10], 0) / 100).toFixed(1);
            const ucbNetM = (ucbEvents.reduce((sum, e) => sum + (e[13] || 0), 0) / 1000).toFixed(1);

            // Filter Stats Pill
            const pill = document.getElementById('filterStatsPill');
            if (pill) {
                const pct = ((count / (allEvents.length || 1)) * 100).toFixed(1);
                pill.innerHTML = `<i class="fa-solid fa-filter"></i> Showing ${count.toLocaleString()} / 14,750 Events (${pct}%)`;
            }

            // Cards
            const elEvents = document.getElementById('kpiFilteredEvents');
            if (elEvents) elEvents.innerText = count.toLocaleString();

            const elFootfall = document.getElementById('kpiFilteredFootfall');
            if (elFootfall) {
                elFootfall.innerText = totalFootfall >= 1e6 
                    ? (totalFootfall / 1e6).toFixed(2) + 'M' 
                    : (totalFootfall / 1e3).toFixed(1) + 'k';
            }

            const elTurnout = document.getElementById('kpiFilteredTurnout');
            if (elTurnout) elTurnout.innerText = avgTurnout + '%';

            const elRating = document.getElementById('kpiFilteredRating');
            if (elRating) elRating.innerText = avgRating + ' ⭐';

            const elFinance = document.getElementById('kpiFilteredFinance');
            if (elFinance) {
                if (iitEvents.length > 0 && ucbEvents.length > 0) {
                    elFinance.innerText = `₹${iitBudgetCr}Cr / $${ucbNetM}M`;
                } else if (iitEvents.length > 0) {
                    elFinance.innerText = `₹${iitBudgetCr} Crore INR`;
                } else {
                    elFinance.innerText = `$${ucbNetM} Million USD`;
                }
            }
        }

        function updateFilteredCharts(events, dsVal) {
            if (!events || events.length === 0) return;

            // A. Monthly Line Chart (Aggregate attendance by month)
            const monthlyMap = {};
            events.forEach(e => {
                const mo = e[6];
                if (!monthlyMap[mo]) monthlyMap[mo] = { iit: 0, ucb: 0, total: 0 };
                if (e[0] === 'iit') monthlyMap[mo].iit += e[7];
                else monthlyMap[mo].ucb += e[7];
                monthlyMap[mo].total += e[7];
            });

            const months = Object.keys(monthlyMap).sort();
            const tracesMonthly = [];
            if (dsVal === 'all' || dsVal === 'iit') {
                tracesMonthly.push({
                    x: months,
                    y: months.map(m => monthlyMap[m].iit),
                    name: '🇮🇳 IIT Monthly Footfall',
                    type: 'scatter',
                    mode: 'lines+markers',
                    fill: 'tozeroy',
                    line: { color: '#38bdf8', width: 2.5 }
                });
            }
            if (dsVal === 'all' || dsVal === 'ucb') {
                tracesMonthly.push({
                    x: months,
                    y: months.map(m => monthlyMap[m].ucb),
                    name: '🇺🇸 UCB Monthly Footfall',
                    type: 'scatter',
                    mode: 'lines+markers',
                    fill: 'tozeroy',
                    line: { color: '#f472b6', width: 2.5 }
                });
            }

            if (document.getElementById('plotGalleryMonthlyLine')) {
                Plotly.react('plotGalleryMonthlyLine', tracesMonthly, {
                    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 50, r: 20, t: 20, b: 40 }, font: { color: '#cbd5e1' },
                    xaxis: { gridcolor: '#26334d' }, yaxis: { gridcolor: '#26334d', title: 'Attendees / Month' }
                });
            }

            // B. Department / Campus Ranking Bar Chart
            const unitMap = {};
            events.forEach(e => {
                const u = e[3];
                unitMap[u] = (unitMap[u] || 0) + e[7];
            });
            const sortedUnits = Object.keys(unitMap).sort((a,b) => unitMap[a] - unitMap[b]);
            const topUnits = sortedUnits.slice(-10);

            if (document.getElementById('plotGalleryHorizBar')) {
                Plotly.react('plotGalleryHorizBar', [{
                    y: topUnits,
                    x: topUnits.map(u => unitMap[u]),
                    type: 'bar', orientation: 'h',
                    marker: { color: dsVal === 'ucb' ? '#f472b6' : '#38bdf8' }
                }], {
                    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 140, r: 20, t: 20, b: 40 }, font: { color: '#cbd5e1' },
                    xaxis: { gridcolor: '#26334d', title: 'Filtered Event Footfall' }
                });
            }

            // C. Category Portfolio Donut
            const catMap = {};
            events.forEach(e => {
                const c = e[4];
                catMap[c] = (catMap[c] || 0) + 1;
            });
            const catLabels = Object.keys(catMap);
            const catValues = catLabels.map(c => catMap[c]);

            if (document.getElementById('plotGalleryDonutCat')) {
                Plotly.react('plotGalleryDonutCat', [{
                    labels: catLabels,
                    values: catValues,
                    type: 'pie', hole: 0.55,
                    marker: { colors: ['#38bdf8', '#818cf8', '#c084fc', '#f472b6', '#34d399', '#fbbf24', '#f87171'] }
                }], {
                    paper_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 20, r: 20, t: 20, b: 20 }, font: { color: '#cbd5e1' }
                });
            }

            // D. Scatter Bubble Chart (Budget vs Attendance)
            const sampleScatter = events.slice(0, 400);
            if (document.getElementById('plotGalleryBubble')) {
                Plotly.react('plotGalleryBubble', [{
                    x: sampleScatter.map(e => e[10]),
                    y: sampleScatter.map(e => e[7]),
                    text: sampleScatter.map(e => `${e[2]} (${e[3]} - ${e[4]})`),
                    mode: 'markers',
                    marker: {
                        size: sampleScatter.map(e => Math.min(24, Math.max(5, e[9] / 60))),
                        color: sampleScatter.map(e => e[11]),
                        colorscale: 'Plasma', showscale: true,
                        colorbar: { title: 'CSAT ⭐', tickfont: { color: '#94a3b8' } }
                    }
                }], {
                    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 50, r: 20, t: 20, b: 40 }, font: { color: '#cbd5e1' },
                    xaxis: { gridcolor: '#26334d', title: 'Event Budget' },
                    yaxis: { gridcolor: '#26334d', title: 'Actual Attendance' }
                });
            }

            // E. Histograms (Turnout & CSAT)
            if (document.getElementById('plotGalleryHistTurnout')) {
                Plotly.react('plotGalleryHistTurnout', [{
                    x: events.map(e => e[12]),
                    name: 'Filtered Turnout %',
                    type: 'histogram',
                    marker: { color: '#38bdf8' },
                    nbinsx: 30
                }], {
                    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 40, r: 20, t: 20, b: 40 }, font: { color: '#cbd5e1' },
                    xaxis: { gridcolor: '#26334d', title: 'Turnout Rate (%)' },
                    yaxis: { gridcolor: '#26334d', title: 'Event Frequency' }
                });
            }

            if (document.getElementById('plotGalleryHistRating')) {
                Plotly.react('plotGalleryHistRating', [{
                    x: events.map(e => e[11]),
                    name: 'Filtered CSAT Rating',
                    type: 'histogram',
                    marker: { color: '#f472b6' },
                    nbinsx: 25
                }], {
                    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 40, r: 20, t: 20, b: 40 }, font: { color: '#cbd5e1' },
                    xaxis: { gridcolor: '#26334d', title: 'Satisfaction Score (1.0 to 5.0)' },
                    yaxis: { gridcolor: '#26334d', title: 'Frequency Count' }
                });
            }

            // F. 3D WebGL Scatter Plot (Filtered Points in 3D Space)
            const sample3D = events.slice(0, 500);
            if (document.getElementById('plot3dScatter')) {
                Plotly.react('plot3dScatter', [{
                    x: sample3D.map(e => e[10]),
                    y: sample3D.map(e => e[7]),
                    z: sample3D.map(e => e[11]),
                    text: sample3D.map(e => `${e[2]}<br>${e[3]} | ${e[4]}<br>Turnout: ${e[12]}%`),
                    mode: 'markers',
                    marker: {
                        size: sample3D.map(e => Math.min(20, Math.max(4, e[9] / 70))),
                        color: sample3D.map(e => e[11]),
                        colorscale: 'Viridis',
                        colorbar: { title: 'Rating ⭐', tickfont: { color: '#94a3b8' } },
                        opacity: 0.85
                    },
                    type: 'scatter3d'
                }], {
                    paper_bgcolor: 'rgba(0,0,0,0)',
                    plot_bgcolor: 'rgba(0,0,0,0)',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                        xaxis: { title: 'Budget (Lakhs INR / $k)', color: '#94a3b8', gridcolor: '#26334d', backgroundcolor: '#101726' },
                        yaxis: { title: 'Actual Attendance', color: '#94a3b8', gridcolor: '#26334d', backgroundcolor: '#101726' },
                        zaxis: { title: 'CSAT Rating (1-5)', color: '#94a3b8', gridcolor: '#26334d', backgroundcolor: '#101726' }
                    }
                }, { responsive: true, displayModeBar: true });
            }
        }

        function updateExplorerTableWithFiltered(events) {
            const tbody = document.getElementById('tableBody');
            const thead = document.getElementById('tableHead');
            if (!tbody || !thead) return;

            thead.innerHTML = `
                <tr>
                    <th>Dataset</th>
                    <th>Event ID</th>
                    <th>Event Name</th>
                    <th>Unit / Campus</th>
                    <th>Category</th>
                    <th>Date (Mo)</th>
                    <th>Attendance</th>
                    <th>Registrations</th>
                    <th>Turnout %</th>
                    <th>Budget</th>
                    <th>Rating ⭐</th>
                </tr>
            `;

            const preview = events.slice(0, 80);
            tbody.innerHTML = preview.map(e => `
                <tr>
                    <td><span class="tag-pill ${e[0] === 'iit' ? 'tag-blue' : 'tag-purple'}">${e[0].toUpperCase()}</span></td>
                    <td style="font-family:'JetBrains Mono'; font-size:0.8rem; color:#94a3b8;">${e[1]}</td>
                    <td><strong>${e[2]}</strong></td>
                    <td style="color:#cbd5e1;">${e[3]}</td>
                    <td><span class="tag-pill tag-green">${e[4]}</span></td>
                    <td>${e[6]}</td>
                    <td style="font-weight:700; color:#38bdf8;">${e[7].toLocaleString()}</td>
                    <td>${e[8].toLocaleString()}</td>
                    <td style="font-weight:700; color:#34d399;">${e[12]}%</td>
                    <td>${e[0] === 'iit' ? '₹' + e[10] + 'L' : '$' + e[10] + 'k'}</td>
                    <td><span class="tag-pill tag-amber">${e[11]} ⭐</span></td>
                </tr>
            `).join('');
        }
"""

# Insert CSS before </style>
if "</style>" in code and "/* INTERACTIVE MASTER DASHBOARD FILTER SYSTEM */" not in code:
    code = code.replace("</style>", filter_css + "\n    </style>", 1)

# Insert HTML before <nav class="nav-container">
nav_str = '<nav class="nav-container">'
if nav_str in code and "<!-- INTERACTIVE MASTER DASHBOARD FILTER SYSTEM -->" not in code:
    code = code.replace(nav_str, filter_html + "\n    " + nav_str, 1)

# Insert JS before window.addEventListener('load'
load_str = "window.addEventListener('load'"
if load_str in code and "function initFilterControls()" not in code:
    code = code.replace(load_str, filter_js + "\n        " + load_str, 1)

# In window.addEventListener('load', add initFilterControls();
if "initFilterControls();" not in code:
    init_marker = "initRubricTable();"
    if init_marker in code:
        code = code.replace(init_marker, "initFilterControls();\n            " + init_marker, 1)

with open(os.path.join(base_dir, "build_html_dashboard.py"), "w", encoding="utf-8") as f:
    f.write(code)

print("build_html_dashboard.py updated with dynamic interactive filters.")
