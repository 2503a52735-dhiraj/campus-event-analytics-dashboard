import pandas as pd
import numpy as np

xlsx_path = r"c:\Users\gandi\OneDrive\Desktop\davproject\IIT_Campus_Event_Raw_5100_Rows.xlsx"
csv_path = r"c:\Users\gandi\OneDrive\Desktop\davproject\uncleaned_event_data.csv"

out_file = r"c:\Users\gandi\OneDrive\Desktop\davproject\deep_dive_output.txt"

with open(out_file, "w", encoding="utf-8") as f:
    def p(text=""):
        f.write(str(text) + "\n")
        f.flush()

    df_csv = pd.read_csv(csv_path)
    df_excel = pd.read_excel(xlsx_path, engine='openpyxl')

    p("=== CSV DETAILED AUDIT ===")
    p("Numeric summary:")
    num_cols_csv = df_csv.select_dtypes(include=[np.number]).columns
    for c in num_cols_csv:
        q25, q75 = df_csv[c].quantile(0.25), df_csv[c].quantile(0.75)
        iqr = q75 - q25
        lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
        outliers = df_csv[(df_csv[c] < lower) | (df_csv[c] > upper)][c]
        negs = (df_csv[c] < 0).sum()
        p(f"Col: {c} | min={df_csv[c].min()}, max={df_csv[c].max()}, negs={negs}, outliers={len(outliers)} ({len(outliers)/len(df_csv):.1%}) [IQR bounds: {lower:.2f} to {upper:.2f}]")

    p("\nCategorical columns in CSV:")
    cat_cols_csv = df_csv.select_dtypes(include=['object']).columns
    for c in cat_cols_csv:
        p(f"{c}: {df_csv[c].nunique()} unique, sample: {list(df_csv[c].dropna().unique()[:6])}")

    p("\n=== EXCEL DETAILED AUDIT ===")
    p("Numeric summary:")
    num_cols_excel = df_excel.select_dtypes(include=[np.number]).columns
    for c in num_cols_excel:
        q25, q75 = df_excel[c].quantile(0.25), df_excel[c].quantile(0.75)
        iqr = q75 - q25
        lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
        outliers = df_excel[(df_excel[c] < lower) | (df_excel[c] > upper)][c]
        negs = (df_excel[c] < 0).sum()
        p(f"Col: {c} | min={df_excel[c].min()}, max={df_excel[c].max()}, negs={negs}, outliers={len(outliers)} ({len(outliers)/len(df_excel):.1%}) [IQR bounds: {lower:.2f} to {upper:.2f}]")

    p("\nCategorical columns in Excel:")
    cat_cols_excel = df_excel.select_dtypes(include=['object']).columns
    for c in cat_cols_excel:
        p(f"{c}: {df_excel[c].nunique()} unique, sample: {list(df_excel[c].dropna().unique()[:10])}")

    p("\nIIT Campus unique values:")
    p(df_excel['iit_campus'].value_counts(dropna=False))

    p("\nEvent Category in Excel:")
    p(df_excel['event_category'].value_counts(dropna=False))

    p("\nTurnout Rate in CSV vs calculated Actual Attendance / Registrations:")
    calc_turnout = (df_csv['Actual Attendance'] / df_csv['Registrations']) * 100
    p(f"Mismatch in Turnout Rate: {(np.abs(calc_turnout - df_csv['Turnout Rate']) > 1).sum()}")

print("Deep dive completed!")
