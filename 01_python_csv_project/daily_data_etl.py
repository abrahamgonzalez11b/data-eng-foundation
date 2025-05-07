import pandas as pd
from datetime import datetime
import os

# Set URL to extract data
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

# Extract
df = pd.read_csv(url)

# Transform
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")  # Clean headers
df = df.dropna()  # Remove missing values

# Load
timestamp = datetime.now().strftime("%Y%m%d")
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)
output_path = f"{output_dir}/cleaned_data_{timestamp}.csv"
df.to_csv(output_path, index=False)

print(f"✅ Data saved to {output_path}")