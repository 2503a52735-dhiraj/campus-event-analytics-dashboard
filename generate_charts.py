import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_dir = r"c:\Users\gandi\OneDrive\Desktop\davproject"
charts_dir = os.path.join(base_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

df_iit = pd.read_csv(os.path.join(base_dir, "cleaned_iit_events.csv"))
df_univ = pd.read_csv(os.path.join(base_dir, "cleaned_university_events.csv"))
df_iit_raw = pd.read_excel(os.path.join(base_dir, "IIT_Campus_Event_Raw_5100_Rows.xlsx"), engine='openpyxl')
df_univ_raw = pd.read_csv(os.path.join(base_dir, "uncleaned_event_data.csv"))

# Style configuration
plt.style.use('dark_background')
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#1e293b", "figure.facecolor": "#0f172a", "text.color": "#f8fafc", "axes.labelcolor": "#cbd5e1", "xtick.color": "#94a3b8", "ytick.color": "#94a3b8"})

# 1. Outlier Treatment Comparison (Seaborn Boxplots)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Data Cleaning: Outlier Detection & Treatment Before vs After", fontsize=16, fontweight='bold', color='#60a5fa')

# Rating before vs after
sns.boxplot(y=df_univ_raw['Student Rating (1-5)'].dropna(), ax=axes[0, 0], color='#f43f5e')
axes[0, 0].set_title("Raw Rating (Contains 99 Outliers)", color='#fca5a5', fontweight='bold')
axes[0, 0].set_ylabel("Rating Value")

sns.boxplot(y=df_univ['Student Rating (1-5)'], ax=axes[0, 1], color='#10b981')
axes[0, 1].set_title("Cleaned Rating (Clamped to 1.0 - 5.0)", color='#86efac', fontweight='bold')
axes[0, 1].set_ylabel("Rating Value")

# Budget before vs after
sns.boxplot(y=df_iit_raw['budget_inr'].dropna(), ax=axes[1, 0], color='#f43f5e')
axes[1, 0].set_title("Raw IIT Budget (Negatives & Dummy 99.9 Cr)", color='#fca5a5', fontweight='bold')
axes[1, 0].set_ylabel("Budget (INR)")

sns.boxplot(y=df_iit['budget_inr'], ax=axes[1, 1], color='#38bdf8')
axes[1, 1].set_title("Cleaned IIT Budget (Realistic Campus Bounds)", color='#93c5fd', fontweight='bold')
axes[1, 1].set_ylabel("Budget (INR)")

plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "01_outlier_treatment.png"), dpi=200)
plt.close()

# 2. Seaborn Correlation Heatmap for IIT Events
fig, ax = plt.subplots(figsize=(10, 8))
corr_cols = ['max_capacity', 'total_registrations', 'actual_attendance', 'budget_inr', 'csat_rating', 'turnout_rate', 'cost_per_attendee_inr']
corr = df_iit[corr_cols].corr()
sns.heatmap(corr, annot=True, cmap="mako", fmt=".2f", ax=ax, cbar=True, annot_kws={"size": 10, "color": "white"})
ax.set_title("IIT Campus Events: Pearson Correlation Matrix", fontsize=14, fontweight='bold', color='#38bdf8')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "02_iit_correlation_matrix.png"), dpi=200)
plt.close()

# 3. Seaborn Violin Plot: Category Satisfaction & Turnout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
sns.violinplot(data=df_iit, x='event_category', y='csat_rating', palette='mako', ax=ax1)
ax1.set_title("IIT Student CSAT Rating Density by Category", fontsize=13, fontweight='bold', color='#60a5fa')
ax1.set_xlabel("Event Category")
ax1.set_ylabel("CSAT Rating (1.0 - 5.0)")
ax1.tick_params(axis='x', rotation=30)

sns.boxplot(data=df_univ, x='Category', y='Turnout Rate (%)', palette='rocket', ax=ax2)
ax2.set_title("UCB Turnout Rate (%) Across Event Categories", fontsize=13, fontweight='bold', color='#f472b6')
ax2.set_xlabel("Event Category")
ax2.set_ylabel("Turnout Rate (%)")
ax2.tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "03_category_satisfaction_turnout.png"), dpi=200)
plt.close()

# 4. Cross-Dataset Comparison: KDE Distributions
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Turnout KDE
sns.kdeplot(df_iit['turnout_rate'], label='🇮🇳 IIT Turnout Rate', color='#38bdf8', fill=True, alpha=0.3, ax=ax1, lw=2.5)
sns.kdeplot(df_univ['Turnout Rate (%)'], label='🇺🇸 UCB Turnout Rate', color='#f472b6', fill=True, alpha=0.3, ax=ax1, lw=2.5)
ax1.set_title("Turnout Rate (%) Density Comparison", fontsize=13, fontweight='bold', color='#e2e8f0')
ax1.set_xlabel("Turnout Rate (%)")
ax1.set_ylabel("Density")
ax1.legend(facecolor='#1e293b', edgecolor='#475569')

# Rating KDE
sns.kdeplot(df_iit['csat_rating'], label='🇮🇳 IIT CSAT Rating', color='#38bdf8', fill=True, alpha=0.3, ax=ax2, lw=2.5)
sns.kdeplot(df_univ['Student Rating (1-5)'], label='🇺🇸 UCB Student Rating', color='#f472b6', fill=True, alpha=0.3, ax=ax2, lw=2.5)
ax2.set_title("Student Feedback Rating (1-5) Density Comparison", fontsize=13, fontweight='bold', color='#e2e8f0')
ax2.set_xlabel("Rating Value (1.0 - 5.0)")
ax2.set_ylabel("Density")
ax2.legend(facecolor='#1e293b', edgecolor='#475569')

plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "04_cross_dataset_comparison.png"), dpi=200)
plt.close()

print("All Seaborn and Matplotlib visualization charts successfully generated in:", charts_dir)
