import sys
import pandas as pd
import json

output_file = r"c:\Users\gandi\OneDrive\Desktop\davproject\inspection_output.txt"

with open(output_file, "w", encoding="utf-8") as out:
    def log(msg):
        out.write(str(msg) + "\n")
        out.flush()

    xlsx_path = r"c:\Users\gandi\OneDrive\Desktop\davproject\IIT_Campus_Event_Raw_5100_Rows.xlsx"
    csv_path = r"c:\Users\gandi\OneDrive\Desktop\davproject\uncleaned_event_data.csv"

    log("=== 1. READING CSV ===")
    try:
        df_csv = pd.read_csv(csv_path)
        log(f"CSV Shape: {df_csv.shape}")
        log(f"CSV Columns: {list(df_csv.columns)}")
        log("\nCSV dtypes:\n" + str(df_csv.dtypes))
        log("\nCSV Missing Values:\n" + str(df_csv.isnull().sum()))
        log(f"\nCSV Duplicates count: {df_csv.duplicated().sum()}")
        log("\nCSV Describe:\n" + str(df_csv.describe(include='all')))
        log("\nCSV Head(5):\n" + str(df_csv.head(5)))
    except Exception as e:
        log(f"CSV Error: {e}")

    log("\n" + "="*60 + "\n")

    log("=== 2. READING EXCEL ===")
    try:
        df_excel = pd.read_excel(xlsx_path, engine='openpyxl')
        log(f"Excel Shape: {df_excel.shape}")
        log(f"Excel Columns: {list(df_excel.columns)}")
        log("\nExcel dtypes:\n" + str(df_excel.dtypes))
        log("\nExcel Missing Values:\n" + str(df_excel.isnull().sum()))
        log(f"\nExcel Duplicates count: {df_excel.duplicated().sum()}")
        log("\nExcel Describe:\n" + str(df_excel.describe(include='all')))
        log("\nExcel Head(5):\n" + str(df_excel.head(5)))
    except Exception as e:
        log(f"Excel Error: {e}")

    log("\n=== COMPLETED INSPECTION ===")

print("Done inspecting!")
