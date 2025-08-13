
"""
explore_dataset.py
------------------
Quick overview of the Rio de Janeiro rental market dataset: columns and sample data.
"""

import pandas as pd

# Path to the CSV file
csv_path = r"dataset/data/properati_br_2016_11_01_properties_rent.csv"

# Read the first 20 rows to explore the dataset
df = pd.read_csv(csv_path, nrows=20)

# Display available columns and sample data
def quick_overview():
    print("Available columns:")
    print(df.columns)
    print("\nSample data:")
    print(df.head())

if __name__ == "__main__":
    quick_overview()
