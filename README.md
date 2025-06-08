# 🌍 Earthquake Analysis Dashboard (1995–2023)

> **Dataset Source**: Global earthquake records (1995–2023)  
> **Tools Used**: Python, Pandas, Plotly, Folium, Streamlit

---

## 📦 Project Structure

This project analyzes global earthquake data between **1995 and 2023** and presents findings through a **dynamic, interactive dashboard** built with Streamlit.

---

## 🧾 Dataset Information

### 🔹 Raw Data Files:
- `earthquake_1995-2023.csv`
- `earthquake_data.csv`

> These contain earthquake event logs from global sources, including missing values, inconsistencies, and unformatted fields.

### 🔹 Cleaned Data Used:
- `Cleaned earthquake dataset.csv`

> This file is the **only dataset used in the dashboard**. It was cleaned using Python scripts—null values removed, timestamps converted, alerts categorized, and numeric columns like `magnitude`, `depth`, and `significance` fixed and standardized.

---

## 📊 Exploratory Data Analysis (EDA)

### Key Explorations:
- Earthquake frequency over time
- Magnitude and depth ranges
- Alert level breakdown
- Country and continent-level trends
- Geospatial clustering of high-risk zones

### Techniques Used:
- Histograms, scatter plots, box plots (via Plotly)
- Grouped summaries using Pandas
- Folium-based mapping with heatmaps and markers

---

## 🖥️ Interactive Streamlit Dashboard

### Dashboard Features:
- **Filters**:
  - Date range selector
  - Magnitude slider
  - Depth range slider
  - Alert level multiselect

- **Metrics Displayed**:
  - Total Earthquakes
  - Average Magnitude
  - Maximum Magnitude
  - Earthquakes involving Tsunamis

- **Visualizations**:
  - 🌍 **Heatmap** of earthquake activity
  - 📌 **Marker map** of major seismic zones
  - 📊 **Top 10 Countries by Count**
  - 🧭 **Continent-wise distribution (Pie Chart)**
  - 📉 **Histogram of Magnitude Frequency**
  - 📈 **Scatter: Depth vs Magnitude**
  - 📦 **Boxplot: Magnitude vs Significance**
  - 📄 **Table View** of filtered earthquake data

> 🔧 Built with `pandas`, `plotly`, `folium`, `streamlit`, and `streamlit-folium`  
> 📁 Main app code: `app.py`

---

## 📂 Files Included

- `earthquake_1995-2023.csv` – Raw dataset  
- `earthquake_data.csv` – Alternate version of raw data  
- `Cleaned earthquake dataset.csv` – Final cleaned file used in dashboard  
- `app.py` – Streamlit dashboard code  
- `README.md` – Project documentation (this file)

---

## 📈 Key Takeaways

| Insight Area         | Description                                                           |
|----------------------|------------------------------------------------------------------------|
| 🌐 Global Patterns     | Reveals trends in frequency, magnitude, and depth globally            |
| 🗺️ Hotspot Detection   | Highlights high-seismic-risk areas across countries and continents     |
| 📊 Alert Awareness     | Understands the severity levels and preparedness requirements         |
| 📌 User Interactivity | Lets users explore data with filters and intuitive visualizations      |

---

## 💡 Final Notes

This project showcases how **cleaned geospatial event data** can be transformed into powerful, accessible dashboards that support **risk analysis**, **policy planning**, and **public awareness** on global seismic activity.

---
