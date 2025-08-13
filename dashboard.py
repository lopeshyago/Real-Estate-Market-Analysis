import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Rio de Janeiro Rental Market Dashboard", layout="wide")

st.title("Rio de Janeiro Rental Market Dashboard")
st.markdown("""
This dashboard presents key insights from the exploratory analysis of Rio de Janeiro's residential rental market. Use the sections below to explore price distribution, top neighborhoods, property features, and listing concentration.
""")

# Load data
csv_path = "https://docs.google.com/spreadsheets/d/1rOF77iN8ZWRxaqCbZ-E3Mh0ord3uBb7kVQGPdD-GtZ4"
sample_size = 10000
df = pd.read_csv(csv_path, nrows=sample_size)
df = df[df['price'].notnull()]
df['expenses'] = df['expenses'].fillna(0)

# Sidebar filters
st.sidebar.header("Filters")
selected_neighborhoods = st.sidebar.multiselect(
    "Select neighborhoods:",
    options=df['place_name'].unique(),
    default=df['place_name'].unique()[:5]
)
filtered_df = df[df['place_name'].isin(selected_neighborhoods)] if selected_neighborhoods else df

# Price Distribution
st.subheader("Rental Price Distribution")
fig, ax = plt.subplots(figsize=(10,4))
filtered_df['price'].plot.hist(bins=50, color='skyblue', ax=ax)
ax.set_title('Rental Price Distribution')
ax.set_xlabel('Price')
st.pyplot(fig)

# Top Neighborhoods
st.subheader("Top 5 Most Expensive and Cheapest Neighborhoods")
mean_price_by_bairro = df.groupby('place_name')['price'].mean().sort_values(ascending=False)
top5_expensive = mean_price_by_bairro.head(5)
top5_cheap = mean_price_by_bairro.tail(5)
fig, ax = plt.subplots(1,2,figsize=(12,4))
top5_expensive.plot(kind='bar', color='crimson', ax=ax[0])
ax[0].set_title('Top 5 Most Expensive Neighborhoods')
ax[0].set_ylabel('Average Price')
ax[0].tick_params(axis='x', rotation=45)
top5_cheap.plot(kind='bar', color='seagreen', ax=ax[1])
ax[1].set_title('Top 5 Cheapest Neighborhoods')
ax[1].set_ylabel('Average Price')
ax[1].tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Bedrooms vs Price
st.subheader("Relationship Between Number of Bedrooms and Price")
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x='rooms', y='price', data=filtered_df, ax=ax)
ax.set_title('Bedrooms vs Price')
ax.set_xlabel('Bedrooms')
ax.set_ylabel('Price')
st.pyplot(fig)

# Pet-Friendly and Furnished Properties
st.subheader("Proportion of Pet-Friendly and Furnished Properties")
df['pet_friendly'] = df['description'].str.contains('pet|animal', case=False, na=False)
df['furnished'] = df['description'].str.contains('mobiliado|furnished', case=False, na=False)
pet_counts = df['pet_friendly'].value_counts()
furnished_counts = df['furnished'].value_counts()
fig, ax = plt.subplots(1,2,figsize=(10,5))
pet_counts.plot.pie(autopct='%1.1f%%', labels=['No', 'Yes'], colors=['lightgray','gold'], ax=ax[0])
ax[0].set_title('Pet-Friendly Properties')
ax[0].set_ylabel('')
furnished_counts.plot.pie(autopct='%1.1f%%', labels=['No', 'Yes'], colors=['lightgray','skyblue'], ax=ax[1])
ax[1].set_title('Furnished Properties')
ax[1].set_ylabel('')
st.pyplot(fig)

# Heatmap of Listing Concentration
st.subheader("Heatmap of Listing Concentration")
df_map = df.dropna(subset=['lat','lon'])
if not df_map.empty:
    m = folium.Map(location=[-22.9, -43.2], zoom_start=11)
    heat_data = [[row['lat'], row['lon']] for idx, row in df_map.iterrows()]
    folium.plugins.HeatMap(heat_data).add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.info("Not enough location data to generate the heatmap.")

st.markdown("---")
st.markdown("**Project by Hyago Lopes | Data Source: Properati Brazil**")
