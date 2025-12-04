<h1 align="center">⚙️ Python Data Automation</h1>

<p align="center">
  Automated CSV Cleaning • Reporting • KPI Generation
</p>

---

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-00599C?style=for-the-badge&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Data--Automation-4CAF50?style=for-the-badge"/>
</p>

---

## 📘 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tools & Libraries](#tools--libraries)
- [Repository Structure](#repository-structure)
- [Setup & Running The Script](#setup--running-the-script)
- [Example Output](#example-output)
- [Professional Summary](#professional-summary)

---

## 📌 Project Overview
This project is a **Python automation workflow** that ingests raw CSV files, cleans the data, calculates key performance metrics, and generates both **summary reports** and **visual charts**.

Perfect for repetitive business reporting tasks — turn messy CSVs into clean insights with one command.

---

## 🚀 Features
- Reads raw CSV input  
- Handles missing values + outliers  
- Standardises date formats  
- Generates grouped aggregates (e.g., by product, region, category)  
- Exports a cleaned summary CSV  
- Saves visual charts (PNG)  
- Fully automated workflow — ready to schedule via cron or Task Scheduler

---

## 🔧 Tools & Libraries
- **Python 3**
- **Pandas** — data cleaning & transformation  
- **Matplotlib** — chart generation  
- **CSV** — input parsing  

---

## 📁 Repository Structure
python-data-automation
│── data/
│   └── sales_data.csv
│
│── output/
│   ├── summary_report.csv
│   └── charts.png
│
│── scripts/
│   └── automation.py
│
│── requirements.txt
└── README.md

---

## ▶️ Setup & Running the Script

### **1️⃣ Install dependencies and Run the automation**

pip install -r requirements.txt
python automation.py


## 📸 Example Output

![Summary Report (CSV)](assets/summary_report.png)
![Generated Chart](assets/generated_chart.png)