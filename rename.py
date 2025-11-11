import os
import pandas as pd
import re
import shutil

# === CONFIGURATION ===
excel_column = "Datnes nosaukums"   # Column in Excel with target filenames
search_pattern = r"([A-Za-z]+[-_]\d+)"  # Pattern like PK-20 or ABC_123
valid_ext = [".jpg", ".jpeg", ".tif", ".tiff", ".png"]  # Supported formats

folder = os.path.dirname(os.path.abspath(__file__))
renamed_folder = os.path.join(folder, "renamed")

# Create output folder if not exists
os.makedirs(renamed_folder, exist_ok=True)

# === FIND EXCEL FILE ===
excel_file = None
for f in os.listdir(folder):
    if f.lower().endswith((".xlsx", ".xls")):
        excel_file = f
        break

if not excel_file:
    print("❌ No Excel file found in folder!")
    exit()

print(f"✅ Using Excel file: {excel_file}")

# === READ EXCEL DATA ===
df = pd.read_excel(os.path.join(folder, excel_file))

if excel_column not in df.columns:
    print(f"❌ Column '{excel_column}' not found in Excel!")
    exit()

# === PROCESS ROWS ===
renamed_count = 0
missing_count = 0

for new_name in df[excel_column].dropna():
    match = re.search(search_pattern, new_name)
    if not match:
        print(f"⚠️ Skipping, no valid code found in: {new_name}")
        continue

    code = match.group(1).replace("-", "_")  # Normalize like PK-20 → PK_20
    
    # Find matching file in folder
    found_file = None
    for f in os.listdir(folder):
        name, ext = os.path.splitext(f)
        if name == code and ext.lower() in valid_ext:
            found_file = f
            break

    if not found_file:
        print(f"❌ Missing file for: {code}")
        missing_count += 1
        continue

    old_path = os.path.join(folder, found_file)
    new_path = os.path.join(renamed_folder, new_name)

    # Overwrite if exists
    if os.path.exists(new_path):
        os.remove(new_path)

    shutil.move(old_path, new_path)
    print(f"✅ Renamed: {found_file} → {new_name}")
    renamed_count += 1

# === SUMMARY REPORT ===
print("\n===== SUMMARY =====")
print(f"✅ Renamed files: {renamed_count}")
print(f"❌ Missing matches: {missing_count}")
print(f"📂 Renamed files moved to: {renamed_folder}")
