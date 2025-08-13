
"""
explore_dataset.py
------------------
Quick overview of the Rio de Janeiro rental market dataset: columns and sample data.
"""

import pandas as pd

# Path to the CSV file
csv_path = "https://docs.google.com/spreadsheets/d/1rOF77iN8ZWRxaqCbZ-E3Mh0ord3uBb7kVQGPdD-GtZ4/export?format=csv"


# Read the first 20 rows to explore the dataset
df = pd.read_csv(csv_path, nrows=20)
if 'expenses' in df.columns:
    df['expenses'] = df['expenses'].fillna(0)

# Display available columns and sample data
def quick_overview():
    print("Available columns:")
    print(df.columns)
    print("\nSample data:")
    print(df.head())

if __name__ == "__main__":
    quick_overview()
