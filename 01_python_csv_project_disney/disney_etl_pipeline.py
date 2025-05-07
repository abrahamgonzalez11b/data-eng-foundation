import pandas as pd
from datetime import datetime
import os
import kagglehub

# Create folders id not present
os.makedirs("raw_data", exist_ok=True)
os.makedirs("clean_data", exist_ok=True)

# Get timestap
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Step 1: Download dataset folder
path = kagglehub.dataset_download("prateekmaj21/disney-movies")

files = os.listdir(path)
print("Files in downloaded folder:", files)

csv_file = [f for f in files if f.endswith(".csv")][0]  # get first .csv
csv_path = os.path.join(path, csv_file)

# Step 2: Read CSV and save raw version
df_raw = pd.read_csv(csv_path)
raw_output_path = f"raw_data/disney_raw_{timestamp}.csv"
df_raw.to_csv(raw_output_path, index=False)

# Step 3: Clean Data
df_clean = df_raw.copy()

# Rename columns 
df_clean.columns = (
    df_clean.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", " ")
    .str.replace(r"[^\w_]", "", regex=True)
)

# Drop rows with too many missing values
df_clean.dropna(thresh=int(0.6 * len(df_clean.columns)), inplace=True)

# Save cleaned file
clean_output_path = f"clean_data/disney_clean_{timestamp}.csv"
df_clean.to_csv(clean_output_path, index=False)

# Step 4: Log Run
with open("etl_log.txt", "a") as log:
    log.write(
        f"[{timestamp}] ETL SUCCESS: {csv_file} → {clean_output_path} (rows: {len(df_clean)})\n"
    )

print(f" ETL complete! Saved raw and cleaned files.\n")
print(df_clean)