import os
from datetime import datetime
import pandas as pd
import kagglehub

## Phase 1 - Extract

# Download the dataset
dataset_path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

# List the files inside the dataset
files = os.listdir(dataset_path)
print(" Dataset downloaded successfully!")
print(" Files available:", files)

# Append to the ETL log
with open("etl_log.txt", "a") as log:
    log.write(f"[{datetime.now()}] Extracted {len(files)} files frim F1 Kaggle dataset.\n")

## Phase 2 - Transform (Step 1 & 2)

# Step 1: Load drivers
csv_file = os.path.join(dataset_path, "drivers.csv")
df_raw = pd.read_csv(csv_file)

# Step 2: Save raw copy with timestap
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
raw_output_path = f"raw_data/drivers_raw_{timestamp}.csv"
df_raw.to_csv(raw_output_path, index=False)
print(f" Raw file saved to {raw_output_path}")

# Step 3: Clean data
df_clean = df_raw.copy()

# Standardize column names
df_clean.columns = (
    df_clean.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^\w]", "", regex=True)
)

# Drop rows with any missing values
df_clean.dropna(inplace=True)

# (Optional) Short by driver name
df_clean.sort_values(by='surname', inplace=True)

# Step 4: Save Cleaned Version
clean_output_path = f"clean_data/drivers_clean_{timestamp}.csv"
df_clean.to_csv(clean_output_path, index=False)
print(f"Cleaned file saved to {clean_output_path}")

with open("etl_log.txt", "a") as log:
    log.write(
        f"[{datetime.now()}] ✅ Cleaned drivers.csv → {clean_output_path} (rows: {len(df_clean)})\n"
    )

print(df_clean)