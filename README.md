# Maintenance Performance Analytics

**Business Intelligence | Data Analysis | Operational Performance**

## Project Overview

Maintenance Performance Analytics is an end-to-end data analytics project designed to explore maintenance operations and transform operational data into actionable business insights.

The project focuses on equipment downtime, maintenance interventions, failure causes, production zones, and spare parts costs.

It demonstrates how data preparation, exploratory analysis, business-oriented KPI monitoring, and interactive visualization can support operational decision-making.

**Dataset:** 500 synthetic maintenance interventions created specifically for this portfolio project. No confidential company data is used.

## Business Context

Maintenance performance has a direct impact on production continuity, equipment availability, and operational costs.

The objective of this project is to analyze maintenance data and identify performance patterns that can help answer key operational questions:

- Which production zones experience the highest downtime?
- What are the main contributors to equipment downtime?
- How does preventive maintenance compare with corrective maintenance?
- What are the main spare parts cost patterns?
- Where should improvement efforts be prioritized?

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning, transformation and aggregation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization during analysis |
| Power BI Desktop | Interactive dashboard and KPI monitoring |
| CSV | Data storage and exchange |
| Git & GitHub | Version control and project publication |

## Data Analytics Workflow

The project follows a structured analytics workflow:

**1. Data Generation**
- Creation of a synthetic dataset containing 500 maintenance interventions.
- Simulation of equipment, production zones, failure causes, intervention types, downtime and spare parts costs.

**2. Data Preparation**
- Data inspection and quality checks.
- Duplicate detection.
- Validation of intervention dates and durations.
- Preparation of a cleaned dataset for analysis.

**3. Exploratory Data Analysis**
- Analysis of downtime distribution.
- Comparison of maintenance intervention types.
- Analysis of failure causes and production zones.
- Spare parts cost analysis.

**4. Business Intelligence**
- Development of an interactive Power BI dashboard.
- Monitoring of equipment and intervention indicators.
- Analysis by production zone and failure cause.
- Interactive filtering by zone and intervention type.

## Key Findings

Based on the synthetic dataset:

| Indicator | Result |
|---|---:|
| Total interventions | 500 |
| Total equipment | 15 |
| Total downtime | 65,796 minutes |
| Corrective interventions | 369 (73.8%) |
| Preventive interventions | 131 (26.2%) |

### Operational Insights

**1. Downtime by production zone**

Assembly records the highest total downtime, with 15,399 minutes, followed by Injection with 14,667 minutes.

**2. Main failure contributors**

Mechanical failures represent the largest share of downtime, accounting for approximately 21.7% of the total.

**3. Maintenance distribution**

Corrective interventions account for 73.8% of all interventions in the dataset, compared with 26.2% for preventive maintenance.

**4. Spare parts costs**

The analysis also compares spare parts costs between preventive and corrective interventions to explore differences in maintenance expenditure.

## Power BI Dashboard

The interactive dashboard provides an overview of maintenance performance through:

- Total equipment.
- Total interventions.
- Total downtime.
- Downtime by production zone.
- Downtime by failure cause.
- Preventive versus corrective intervention distribution.
- Interactive filters for production zone and intervention type.

The dashboard is designed to help users explore operational performance and identify areas requiring further investigation.

## Business Recommendations

Based on the observed patterns, the following improvement opportunities can be investigated:

- Prioritize further analysis of downtime in the Assembly and Injection zones.
- Investigate the recurring causes of mechanical failures.
- Review preventive maintenance coverage and intervention effectiveness.
- Monitor spare parts expenditure by intervention type.
- Use regular KPI monitoring to identify changes in maintenance performance.

These are exploratory recommendations based on synthetic data, not conclusions about a real industrial organization.

## Project Structure

```text
maintenance-performance-analytics/
│
├── data/
│   ├── raw/
│   │   └── maintenance_interventions.csv
│   └── processed/
│       ├── maintenance_clean.csv
│       ├── cost_by_type.csv
│       ├── downtime_by_type.csv
│       ├── downtime_by_zone.csv
│       └── pareto_analysis.csv
│
├── reports/
│   └── Maintenance_Performance_Analytics.pbix
│
├── src/
│   ├── generate_data.py
│   ├── analyze_data.py
│   └── business_analysis.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/asmaghanmi1/maintenance-performance-analytics.git
cd maintenance-performance-analytics
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Generate the dataset**

```bash
python src/generate_data.py
```

**4. Run data preparation and analysis**

```bash
python src/analyze_data.py
```

**5. Run business analysis**

```bash
python src/business_analysis.py
```

**6. Explore the dashboard**

Open `reports/Maintenance_Performance_Analytics.pbix` using Power BI Desktop.

## Project Scope & Limitations

- The dataset is entirely synthetic and intended for educational and portfolio purposes.
- The findings demonstrate analytical methods rather than actual company performance.
- Accurate MTBF and equipment availability calculations require additional operating-time data.
- The project focuses on Python-based analysis and Power BI visualization. SQL integration can be considered as a future enhancement.

## Author

**Asma Ghanmi**

Computer Engineering Student | Data Analytics | Business Intelligence

[GitHub](https://github.com/asmaghanmi1)

---

*This project demonstrates a practical approach to transforming operational data into structured analysis, business insights, and interactive reporting.*