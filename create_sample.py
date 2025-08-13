import pandas as pd

# Load a small sample from the full dataset
csv_path = "https://docs.google.com/spreadsheets/d/1rOF77iN8ZWRxaqCbZ-E3Mh0ord3uBb7kVQGPdD-GtZ4/export?format=csv"
	sample = pd.read_csv(csv_path, nrows=300)
	if 'expenses' in sample.columns:
		sample['expenses'] = sample['expenses'].fillna(0)
sample.to_csv("sample_rio_rentals.csv", index=False)
print("Sample dataset saved as sample_rio_rentals.csv")
