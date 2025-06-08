import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static

# Load dataset
@st.cache_data
def load_data():
    file_path = "final earthquake dataset.csv"
    df = pd.read_csv(file_path)
    return df

# Load data and preprocess
df = load_data()
df['date_time'] = pd.to_datetime(df['date_time'])

# Dashboard layout
st.title("Earthquake Analysis Dashboard")
st.sidebar.header("Filters")

# Filters
date_range = st.sidebar.date_input("Select Date Range", [df['date_time'].min(), df['date_time'].max()])
min_magnitude = st.sidebar.slider("Minimum Magnitude", float(df['magnitude'].min()), float(df['magnitude'].max()), float(df['magnitude'].min()))
max_depth = st.sidebar.slider("Maximum Depth (km)", 0, int(df['depth'].max()), int(df['depth'].max()))
alert_filter = st.sidebar.multiselect("Select Alert Levels", options=df['alert'].unique(), default=df['alert'].unique())

# Apply filters
filtered_df = df[(df['date_time'] >= pd.Timestamp(date_range[0])) & 
                 (df['date_time'] <= pd.Timestamp(date_range[1])) & 
                 (df['magnitude'] >= min_magnitude) & 
                 (df['depth'] <= max_depth) & 
                 (df['alert'].isin(alert_filter))]

# Section 1: Key Metrics Summary
st.header("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Earthquakes", len(filtered_df))
col2.metric("Average Magnitude", round(filtered_df['magnitude'].mean(), 2))
col3.metric("Max Magnitude", filtered_df['magnitude'].max())
col4.metric("Earthquakes with Tsunami", filtered_df['tsunami'].sum())

# Section 2: Geospatial Insights
st.header("Geospatial Insights")
st.subheader("Heatmap of Earthquakes")
m = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=1)
heat_data = filtered_df[['latitude', 'longitude']].values.tolist()
HeatMap(data=heat_data, radius=10, blur=15, max_zoom=1).add_to(m)
folium_static(m)

st.subheader("High Seismicity Zones")
m2 = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=1)
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        icon=folium.Icon(color='red' if row['magnitude'] >= 7 else 'orange', icon='info-sign'),
        popup=f"Location: {row['location']}<br>Magnitude: {row['magnitude']}<br>Depth: {row['depth']} km<br>Alert: {row['alert']}"
    ).add_to(m2)
folium_static(m2)

# Section 3: Earthquake Counts by Continent and Country
st.header("Earthquake Counts by Continent and Country")
continent_country_df = filtered_df.groupby(['continent', 'country']).size().reset_index(name='count')

# Bar chart for countries
st.subheader("Top 10 Countries with Highest Earthquake Counts")
top_countries = continent_country_df.sort_values(by='count', ascending=False).head(10)
fig = px.bar(top_countries, x='country', y='count', color='continent', title="Top Countries by Earthquake Count")
st.plotly_chart(fig)

# Pie chart for continents
st.subheader("Earthquake Distribution by Continent")
continent_counts = continent_country_df.groupby('continent')['count'].sum().reset_index()
fig = px.pie(continent_counts, values='count', names='continent', title="Earthquake Counts by Continent")
st.plotly_chart(fig)

# Section 4: Magnitude Insights
st.header("Magnitude Insights")

# Histogram for magnitude frequencies
st.subheader("Frequency of Different Magnitudes")
fig = px.histogram(filtered_df, x='magnitude', nbins=20, title="Magnitude Frequency Distribution")
st.plotly_chart(fig)

# Scatter plot for depth vs. magnitude
st.subheader("Depth vs. Magnitude")
fig = px.scatter(filtered_df, x='magnitude', y='depth', color='alert', size='sig', title="Depth vs. Magnitude (Colored by Alert Level)")
st.plotly_chart(fig)

# Boxplot for magnitude vs. significance
st.subheader("Magnitude vs. Significance")
fig = px.box(filtered_df, x='magnitude', y='sig', title="Significance by Magnitude")
st.plotly_chart(fig)

# Section 5: Detailed Earthquake Table
st.header("Earthquake encountered lists")
st.dataframe(filtered_df[['magnitude', 'date_time', 'location', 'depth', 'alert', 'tsunami']].sort_values(by='date_time', ascending=False))