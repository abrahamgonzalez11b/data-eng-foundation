Week 1: Project - Disney Movie ETL Pipeline

## Overview
This project extracts the Disney Movies dataset from Kaggle, cleans the data, and saves both raw and cleaned versions locally.

## Tools Used
- Python
- Pandas
- Kagglehub
- OS + datetime mosules

## ETL Process
1. **Extract**: Download dataset using kagglehub
2. **Transform**:
   - Rename colums
   - Remove rows with too many nulls
3. **Load**: Saved CSVs in `raw_data/` and `clean_data/`

## Output Files
- `raw_data/disney_raw_{timestap}.csv`
- `clean_data/disney_clean_{timestap}.csv`

## Log
ETL run history is stored in 1etl_log.txt`
