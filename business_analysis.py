

"""
business_analysis.py
 Exploratory analysis and visualization of key factors in the Rio de Janeiro residential rental market.
 Generates portfolio-ready charts and a listing concentration heatmap.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Path to the data file
csv_path = r"dataset/data/properati_br_2016_11_01_properties_rent.csv"
sample_size = 10000

# Load a sample from the dataset
df = pd.read_csv(csv_path, nrows=sample_size)

# Basic cleaning: remove rows without price and fill missing expenses
df = df[df['price'].notnull()]
df['expenses'] = df['expenses'].fillna(0)

# 1. Top 5 most expensive/cheapest neighborhoods
# Calculate average price per neighborhood
mean_price_by_bairro = df.groupby('place_name')['price'].mean().sort_values(ascending=False)
top5_expensive = mean_price_by_bairro.head(5)
top5_cheap = mean_price_by_bairro.tail(5)

# Save chart of most expensive neighborhoods
plt.figure(figsize=(8,4))
top5_expensive.plot(kind='bar', color='crimson')
plt.title('Top 5 Most Expensive Neighborhoods to Rent')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('figures/top5_expensive.png')
plt.close()

# Save chart of cheapest neighborhoods
plt.figure(figsize=(8,4))
top5_cheap.plot(kind='bar', color='seagreen')
plt.title('Top 5 Cheapest Neighborhoods to Rent')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('figures/top5_cheap.png')
plt.close()

# 2. Relationship between bedrooms and price
# Scatterplot: number of bedrooms vs price
plt.figure(figsize=(8,6))
sns.scatterplot(x='rooms', y='price', data=df)
plt.title('Relationship Between Number of Bedrooms and Price')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.savefig('figures/rooms_vs_price.png')
plt.close()

# 3. Proportion of pet-friendly and furnished properties
# Search for keywords in description
df['pet_friendly'] = df['description'].str.contains('pet|animal', case=False, na=False)
df['furnished'] = df['description'].str.contains('mobiliado|furnished', case=False, na=False)

pet_counts = df['pet_friendly'].value_counts()
furnished_counts = df['furnished'].value_counts()

# Pie chart for pet-friendly properties
plt.figure(figsize=(5,5))
pet_counts.plot.pie(autopct='%1.1f%%', labels=['No', 'Yes'], colors=['lightgray','gold'])
plt.title('Proportion of Pet-Friendly Properties')
plt.ylabel('')
plt.savefig('figures/pet_friendly.png')
plt.close()

# Pie chart for furnished properties
plt.figure(figsize=(5,5))
furnished_counts.plot.pie(autopct='%1.1f%%', labels=['No', 'Yes'], colors=['lightgray','skyblue'])
plt.title('Proportion of Furnished Properties')
plt.ylabel('')
plt.savefig('figures/furnished.png')
plt.close()

# 4. (Advanced) Heatmap of listing concentration by neighborhood
# Generate heatmap if location data is available
df_map = df.dropna(subset=['lat','lon'])
if not df_map.empty:
    import folium
    from folium.plugins import HeatMap
    mapa = folium.Map(location=[-22.9, -43.2], zoom_start=11)
    heat_data = [[row['lat'], row['lon']] for idx, row in df_map.iterrows()]
    HeatMap(heat_data).add_to(mapa)
    mapa.save('mapa_concentracao.html')
    print('Heatmap saved as mapa_concentracao.html')

"""
business_analysis.py
-------------------
Exploratory analysis and visualization of key factors in the Rio de Janeiro residential rental market.
Generates portfolio-ready charts and a listing concentration heatmap.
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the data file
csv_path = r"dataset/data/properati_br_2016_11_01_properties_rent.csv"
sample_size = 10000

# Load a sample from the dataset
df = pd.read_csv(csv_path, nrows=sample_size)
