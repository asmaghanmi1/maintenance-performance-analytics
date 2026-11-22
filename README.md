# Maintenance Performance Analytics

**End-to-end BI Case Study | Python (Pandas) | Power BI | Maintenance KPIs | Data Analysis**

An independent Business Intelligence case study inspired by my professional experience in industrial maintenance reporting at COFAT, Tunisia.

The objective is to demonstrate how existing Excel-based maintenance reporting can be extended into a structured, analytical and decision-oriented BI approach.

> **Data confidentiality:** All data in this repository is synthetic. No confidential COFAT operational data or internal reports are included. The project demonstrates the methodology, KPI model and analytical approach, not actual company performance.

---

## Key Takeaways

| Indicator | Result |
|---|---:|
| Maintenance interventions analyzed | 500 |
| Equipment units | 15 |
| Corrective maintenance rate | 73.8% |
| Total downtime | 1,096.6 hours |
| Corrective MTTR | 130.15 minutes |
| Top 3 equipment downtime contribution | 27.1% |

*All figures are calculated from the synthetic dataset.*

## 1. Professional Context

During my professional experience at **COFAT**, I contributed to weekly and monthly maintenance reporting using Excel.

I identified an opportunity to extend the existing reporting approach through Business Intelligence, particularly Power BI.

The proposed professional approach involved analyzing three months of maintenance data to identify problematic equipment, understand downtime contributors, prioritize improvement actions and define measurable performance objectives.

The public portfolio dataset is independent of that professional work: it is synthetic and covers January–October 2026. It does not represent the actual three-month COFAT analysis or its results. The Power BI dashboard is a portfolio demonstration, not a deployed COFAT solution.

## 2. Business Questions

This project addresses the following questions:

1. Which equipment generates the highest downtime?
2. Which production zones contribute most to downtime?
3. Which failure causes have the greatest impact?
4. How do corrective and preventive maintenance compare?
5. Where should improvement actions be prioritized?
6. Which KPIs should be monitored over time?

## 3. Dataset

A synthetic dataset generated with Python, containing:

| Attribute | Value |
|---|---:|
| Interventions | 500 |
| Equipment | 15 |
| Production zones | 5 |
| Period | January–October 2026 |
| Format | CSV |

### Data dictionary

| Column | Description |
|---|---|
| `intervention_id` | Unique intervention identifier |
| `equipment_id` | Equipment identifier |
| `zone` | Production zone |
| `start_datetime` | Intervention start date and time |
| `end_datetime` | Intervention end date and time |
| `downtime_minutes` | Total equipment downtime |
| `repair_duration_minutes` | Repair duration |
| `failure_cause` | Failure or intervention cause |
| `intervention_type` | Corrective or preventive |
| `spare_part_cost` | Spare parts cost |

## 4. Technology Stack

- **Python:** Data preparation and analysis.
- **Pandas:** Data cleaning, transformation and aggregation.
- **NumPy:** Numerical operations.
- **Power BI Desktop:** Interactive dashboard and visualization.
- **CSV:** Data storage and exchange.
- **Git and GitHub:** Version control.

## 5. Data Analysis Workflow

The project follows an end-to-end analytical workflow:

**1. Data generation**
- Creation of a synthetic maintenance dataset.

**2. Data preparation — `src/analyze_data.py`**
- Data type conversion.
- Category standardization.
- Duplicate checks.
- Date and duration validation.
- Clean dataset preparation.

**3. Business analysis — `src/business_analysis.py`**
- Maintenance KPI calculation.
- Downtime analysis by zone and intervention type.
- Pareto analysis of failure causes.
- Equipment performance analysis.
- Spare parts cost analysis.
- Monthly and weekly performance aggregation.

### Generated analytical datasets

| File | Purpose |
|---|---|
| `downtime_by_zone.csv` | Downtime by production zone |
| `pareto_analysis.csv` | Failure cause ranking |
| `cost_by_type.csv` | Spare parts cost by intervention type |
| `downtime_by_type.csv` | Corrective vs preventive downtime |
| `equipment_performance.csv` | Equipment-level performance |
| `monthly_performance.csv` | Monthly performance trends |
| `weekly_performance.csv` | Weekly performance trends |

## 6. KPI Definitions

| KPI | Calculation |
|---|---|
| Total Downtime (hours) | Total downtime minutes / 60 |
| Average Downtime | Total downtime / number of interventions |
| Corrective Rate | Corrective interventions / total interventions × 100 |
| Corrective MTTR | Average repair duration for corrective interventions |
| Spare Parts Cost | Sum of spare parts cost values |

### Calculation details

**Total Downtime (hours)**

$$
\frac{\sum Downtime\ Minutes}{60}
$$

**Average Downtime (minutes)**

$$
\frac{\sum Downtime\ Minutes}{Number\ of\ Interventions}
$$

**Corrective Rate (%)**

$$
\frac{Corrective\ Interventions}{Total\ Interventions}\times100
$$

**Corrective MTTR (minutes)**

Average repair duration calculated using corrective interventions only.

MTBF and equipment availability are not calculated because the dataset does not contain reliable equipment operating-time data.

## 7. Key Results and Findings

All findings below are calculated from the synthetic dataset.

### Overall Maintenance Performance

| Indicator | Result |
|---|---:|
| Total interventions | 500 |
| Total equipment | 15 |
| Total downtime | 65,796 minutes |
| Total downtime | 1,096.6 hours |
| Corrective interventions | 369 |
| Preventive interventions | 131 |
| Corrective rate | 73.8% |
| Corrective MTTR | 130.15 minutes |
| Average downtime per intervention | 131.6 minutes |

### Corrective vs Preventive Maintenance

| Indicator | Corrective | Preventive |
|---|---:|---:|
| Interventions | 369 | 131 |
| Share of interventions | 73.8% | 26.2% |
| Total downtime | 63,770 min | 2,026 min |
| Average downtime per intervention | 172.82 min | 15.46 min |
| Average spare parts cost | 295.94 | 81.11 |

*The monetary unit is not specified in the synthetic dataset.*

Corrective interventions account for the largest share of maintenance activity and downtime.

### Downtime by Production Zone

| Production Zone | Downtime (minutes) | Share |
|---|---:|---:|
| Assembly | 15,399 | 23.4% |
| Injection | 14,667 | 22.3% |
| Electrical Control | 12,237 | 18.6% |
| Preparation | 12,085 | 18.4% |
| Cutting | 11,408 | 17.3% |

Assembly and Injection together account for approximately 45.7% of total downtime.

### Pareto Analysis of Failure Causes

| Failure Cause | Downtime (minutes) | Share |
|---|---:|---:|
| Mechanical Failure | 14,285 | 21.7% |
| Operator Error | 11,048 | 16.8% |
| Hydraulic Failure | 10,458 | 15.9% |
| Wear and Tear | 10,196 | 15.5% |
| Electrical Failure | 9,254 | 14.1% |
| Sensor Failure | 8,529 | 13.0% |
| Preventive Maintenance | 2,026 | 3.1% |

The five largest failure categories account for approximately **83.96% of total downtime**.

### Equipment Performance

The three equipment units with the highest accumulated downtime are:

| Equipment | Downtime (minutes) |
|---|---:|
| EQ-012 | 6,315 |
| EQ-005 | 5,902 |
| EQ-013 | 5,608 |

Together, these three equipment units account for approximately **27.1% of total downtime**.

### Monthly Performance

- January recorded the highest downtime: 10,068 minutes.
- September recorded the lowest downtime: 4,650 minutes.
- January recorded the highest intervention volume: 72 interventions.
- September recorded the lowest intervention volume: 39 interventions.

The dataset extends through October 30, 2026. October should therefore be interpreted as a partial reporting period rather than a complete calendar month.

## 8. Insights and Business Recommendations

The findings illustrate how maintenance analytics can support operational decision-making.

**1. Prioritize high-downtime production zones**

Assembly and Injection represent approximately 45.7% of downtime. An equipment-level review of these zones would be a logical starting point.

**2. Investigate the main failure contributors**

Mechanical failures represent 21.7% of downtime. Root-cause analysis and a review of mechanical maintenance practices could help identify improvement opportunities.

**3. Investigate operator-related factors**

Operator error accounts for 16.8% of downtime. Reviewing operating procedures, training needs and process-related factors could be relevant.

**4. Monitor corrective maintenance**

Corrective interventions represent 73.8% of all interventions. Monitoring corrective rate and MTTR can help evaluate maintenance performance.

**5. Establish a KPI monitoring baseline**

Total downtime, corrective rate and corrective MTTR can serve as baseline indicators for periodic performance reviews.

These are potential recommendations derived from synthetic results, not conclusions about COFAT or any real industrial site.

## 9. Power BI Dashboard

The project includes an interactive Power BI report:

`reports/Maintenance_Performance_Analytics.pbix`

The dashboard includes:

- Total Equipment KPI.
- Total Interventions KPI.
- Total Downtime KPI.
- Downtime by Production Zone.
- Downtime by Failure Cause.
- Corrective vs Preventive Intervention Distribution.
- Production Zone slicer.
- Intervention Type slicer.

The report provides an interactive overview of maintenance performance and allows users to explore the dataset through filters.

## 10. Repository Structure

```text
maintenance-performance-analytics/
│
├── data/
│   ├── raw/
│   │   └── maintenance_interventions.csv
│   │
│   └── processed/
│       ├── maintenance_clean.csv
│       ├── cost_by_type.csv
│       ├── downtime_by_type.csv
│       ├── downtime_by_zone.csv
│       ├── equipment_performance.csv
│       ├── monthly_performance.csv
│       ├── pareto_analysis.csv
│       └── weekly_performance.csv
│
├── reports/
│   └── Maintenance_Performance_Analytics.pbix
│
├── src/
│   ├── generate_data.py
│   ├── analyze_data.py
│   └── business_analysis.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 11. How to Run

### Prerequisites

- Python 3.10 or later.
- Power BI Desktop.
- Git.

### Clone the repository

```bash
git clone https://github.com/asmaghanmi1/maintenance-performance-analytics.git
cd maintenance-performance-analytics
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate the dataset

```bash
python src/generate_data.py
```

### Prepare the data

```bash
python src/analyze_data.py
```

### Run the business analysis

```bash
python src/business_analysis.py
```

The processed datasets are exported to `data/processed/`.

Open `reports/Maintenance_Performance_Analytics.pbix` with Power BI Desktop. If necessary, update the CSV source path to the local repository location.

## 12. Limitations and Future Improvements

### Current limitations

- The dataset is synthetic and does not represent actual industrial performance.
- MTBF and availability require reliable equipment operating-time data.
- The monetary unit for spare parts costs is not specified.
- The project focuses on descriptive and diagnostic analytics rather than predictive modelling.

### Potential improvements

- Add SQL-based data extraction and analysis.
- Develop equipment criticality scoring.
- Introduce maintenance performance targets.
- Expand Power BI time-based analysis.
- Explore predictive maintenance indicators when sufficient historical data is available.

## 13. Author

**Asma Ghanmi**

Computer Engineering Student | Data Analytics | Python | Power BI | Software Engineering

- GitHub: [asmaghanmi1](https://github.com/asmaghanmi1)
- LinkedIn: [Asma Ghanmi](https://www.linkedin.com/in/asma-ghanmi-353992269/)

---

*An independent portfolio case study demonstrating data preparation, Python-based analysis, maintenance KPI development, and Business Intelligence reporting.*