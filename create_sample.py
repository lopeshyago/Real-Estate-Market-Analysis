import pandas as pd

# Load a small sample from the full dataset
csv_path = "dataset/data/properati_br_2016_11_01_properties_rent.csv"
sample = pd.read_csv(csv_path, nrows=300)
sample.to_csv("sample_rio_rentals.csv", index=False)
print("Sample dataset saved as sample_rio_rentals.csv")
