# Week 1 Project - F1 World Championship 1950 - 2020

## Overview
This project extracts the F1 World Championship dataset form kaggle, cleans the data, and saves both raw and cleaned versions locally.

## Tools Used
- Python
- Pandas
- Kagglehub
- OS + datetime modules

## ETL Process
1. Extract: Download dataset using kagglehub
2. Transform:
    - Rename columns
    - Remove rows with too many nulls
3. Load: Saved CSVs in `raw_data/` and `clean_data/`

## Output Files
- `raw_data/drivers_raw_<timestamp>.csv`
- `clean_data/drivers_clean_<timestamp>.csv`

## Log
ETL run history is stored in `etl_log.txt1`