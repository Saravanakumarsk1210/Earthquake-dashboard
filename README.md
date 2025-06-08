# 🌍 Earthquake Analysis Dashboard (1995–2023)

> **Tool Used**: Streamlit, Pandas, Plotly, Folium  
> **Data Source**: USGS Earthquake Catalog (1995–2023)

---

## 📌 Project Overview

This project provides a comprehensive analysis and interactive dashboard for global earthquakes recorded between **1995 and 2023**. The objective is to offer insights into the frequency, severity, and geographic distribution of seismic activity over time.

The dashboard is developed using **Streamlit**, with advanced visualizations powered by **Plotly** and **Folium** for geospatial insights.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `earthquake_data.csv` | **Raw dataset** containing unprocessed global earthquake data |
| `Cleaned earthquake dataset.csv` | **Processed dataset** used in the dashboard |
| `app.py` | Streamlit app script to launch the interactive dashboard |

---

## 🧾 Dataset Information

### 🔹 Raw Data: `earthquake_data.csv`

- Contains historical earthquake records with attributes such as:
  - `date_time`
  - `latitude`, `longitude`
  - `magnitude`, `depth`
  - `location`, `country`, `continent`
  - `alert`, `tsunami`, `sig` (significance score)

### 🔹 Cleaned Data: `Cleaned earthquake dataset.csv`

The raw data was cleaned and transformed using **Pandas**:
- Converted `date_time` into standard datetime format
- Ensured numeric data types for `magnitude`, `depth`, and `sig`
- Imputed or removed null entries where necessary
- Mapped latitude/longitude to continents and countries
- Normalized alert levels and created magnitude bins

---

## ⚙️ How to Run the Dashboard

1. Clone the repository or download the files  
2. Install required libraries:

```bash
pip install streamlit pandas plotly folium streamlit-folium
```
3.Run the Streamlit app:


```bash
streamlit run app.py
```
