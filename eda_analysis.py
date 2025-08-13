
"""
eda_analysis.py
---------------
Exploratory data analysis and visualization for the Rio de Janeiro rental market dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the CSV file
csv_path = "https://docs.google.com/spreadsheets/d/1rOF77iN8ZWRxaqCbZ-E3Mh0ord3uBb7kVQGPdD-GtZ4/export?format=csv"

# Read a larger sample for analysis
sample_size = 10000
df = pd.read_csv(csv_path, nrows=sample_size)

# 1. Missing values analysis
missing = df.isnull().sum().sort_values(ascending=False)
print("Missing values per column:\n", missing)

# Suggestion for handling 'expenses' (condo fee) and 'price'
# Example: fill 'expenses' with 0 for residential rentals
# Example: remove rows without 'price'
df = df[df['price'].notnull()]
df['expenses'] = df['expenses'].fillna(0)

# 2. Outlier detection in price
plt.figure(figsize=(10,4))
sns.boxplot(x=df['price'])
plt.title('Rental Price Boxplot')
plt.show()

# Using IQR to identify outliers
def detect_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return series[(series < lower) | (series > upper)]
outliers = detect_outliers(df['price'])
print(f"Outliers detected in 'price': {len(outliers)}")

# 3. Price histogram
df['price'].plot.hist(bins=50, figsize=(10,4), color='skyblue')
plt.title('Rental Price Distribution')
plt.xlabel('Price')
plt.show()

# 4. Boxplot of price by neighborhood (place_name)
plt.figure(figsize=(12,6))
top_neighborhoods = df['place_name'].value_counts().index[:10]
sns.boxplot(x='place_name', y='price', data=df[df['place_name'].isin(top_neighborhoods)])
plt.title('Rental Price Boxplot by Neighborhood (Top 10)')
plt.xticks(rotation=45)
plt.show()
