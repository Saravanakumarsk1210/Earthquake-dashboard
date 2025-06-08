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

> These contain earthquake event logs from multiple global sources with various inconsistencies, nulls, and formatting issues.

### 🔹 Cleaned Data:
- `Cleaned earthquake dataset.csv`  

> Cleaned using Python scripts—nulls handled, date and time normalized, alerts standardized, and fields like `magnitude`, `depth`, `tsunami`, and `significance (sig)` cleaned.

---

## 📊 Exploratory Data Analysis (EDA)

### Key Explorations:
- Temporal range and distribution of earthquake events
- Magnitude and depth distributions
- Alert level categorization
- Geographic distribution (continents and countries)
- High magnitude zones (>= 7.0)

### Techniques Used:
- Histograms, scatter plots, box plots (via Plotly)
- Group-wise summaries by continent and country
- Geospatial heatmaps and markers (Folium)

---

## 🖥️ Interactive Streamlit Dashboard

### Dashboard Highlights:
- **Date Range Selector** to filter events
- **Magnitude & Depth Sliders**
- **Alert Level Filters**
- **Key Metrics**: Total quakes, average magnitude, max magnitude, tsunami count
- **Geospatial Insights**:
  - Heatmap of global seismic activity
  - Marker map highlighting major events
- **Country & Continent Trends**:
  - Top 10 countries by earthquake count
  - Pie chart showing continent-wise distribution
- **Magnitude Analytics**:
  - Frequency distribution
  - Magnitude vs Depth & Significance
- **Dynamic Table**:
  - Filtered events displayed with sort by date

> 📁 Code file: `app.py`  
> 🔧 Uses: `pandas`, `plotly`, `folium`, `streamlit`, `streamlit-folium`

---

## 📂 Files Included

- `earthquake_1995-2023.csv` – Raw dataset  
- `earthquake_data.csv` – Another version of raw input  
- `Cleaned earthquake dataset.csv` – Cleaned dataset used for dashboard   
- `app.py` – Streamlit dashboard code  
- `README.md` – Project documentation (this file)

---

## 📈 Key Takeaways

| Aspect               | Insight                                                                 |
|----------------------|-------------------------------------------------------------------------|
| 🌐 Global Trends      | Seismic activity patterns across time, magnitude, and geography        |
| 📍 Hotspots           | Identified zones with high seismic recurrence                          |
| 📊 Visual Analytics   | Rich visuals for user-friendly data exploration                        |
| 📌 Alert Analysis     | Categorized impact potential of events                                 |
| 🧠 Interactive Filters| Dynamic slicers enhance user control over analysis parameters          |

---

## 💡 Final Notes

This project demonstrates how **raw geospatial data** can be transformed into actionable insights using **data cleaning**, **EDA**, and **dashboarding**. It serves as a powerful template for environmental monitoring, disaster response planning, and public awareness tools.

---
