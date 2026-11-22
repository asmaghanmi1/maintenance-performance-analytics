# Maintenance Performance Analytics

**End-to-end BI Case Study | Python (Pandas) | Power BI | Maintenance KPIs | Downtime & Failure Analysis**

Inspired by my professional experience in industrial maintenance reporting at COFAT (Tunisia), where weekly and monthly reports were produced using Excel, this project demonstrates how existing operational reporting can be extended toward an interactive, data-driven Business Intelligence approach.

All data used in this repository is **synthetic**. No confidential COFAT data or internal reports are included. The value of this project lies in its analytical methodology, KPI model, data preparation process, and dashboard design rather than the numerical results.

---

## 1. What This Project Demonstrates

| Skill expected from a Data Consultant | Implementation |
|---|---|
| Data cleaning and preparation | `src/analyze_data.py` — data type conversion, category standardization, duplicate checks, and date/duration validation |
| Python and Pandas analysis | `src/business_analysis.py` — KPI computation, Pareto analysis, equipment performance, and monthly and weekly aggregations |
| Data analysis and interpretation | Identification of downtime patterns, failure contributors, and equipment requiring further investigation |
| Data modelling and KPI definition | Maintenance performance indicators and analytical datasets |
| Business Intelligence | Interactive Power BI dashboard |
| Business recommendations | Translation of analytical findings into potential improvement actions |
| Analytical limitations | Identification of missing data required for MTBF and availability calculations |

## 2. Professional Context

During my professional experience at **COFAT**, I contributed to recurring weekly and monthly maintenance reporting using Excel.

These reports provided operational visibility into maintenance activities, equipment downtime, and performance indicators.

I identified an opportunity to extend this existing reporting approach through Business Intelligence, particularly Power BI.

The proposed analytical approach involved studying a three-month maintenance dataset to:

- Identify problematic equipment.
- Understand the main contributors to downtime.
- Analyze maintenance performance.
- Prioritize improvement opportunities.
- Define measurable performance objectives.

Due to company confidentiality requirements, actual operational data and internal reports cannot be shared publicly.

This repository independently demonstrates the proposed analytical approach using synthetic data. It does not reproduce COFAT's actual operational results and does not claim that the Power BI dashboard was deployed at COFAT.

## 3. Business Questions

The analysis addresses the following business questions:

1. Which equipment generates the highest downtime?
2. How is downtime distributed across production zones?
3. Which failure causes contribute most to downtime?
4. How do corrective and preventive maintenance compare?
5. Where should improvement actions be prioritized?
6. Which KPIs should be monitored over time?
7. How can maintenance reporting support operational decision-making?

## 4. Dataset Description

The project uses a synthetic maintenance dataset generated with Python.

| Attribute | Value |
|---|---:|
| Number of interventions | 500 |
| Equipment units | 15 |
| Production zones | 5 |
| Period covered | January–October 2026 |
| Data format | CSV |
| Data source | Synthetic dataset generated with Python |

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

All records and numerical findings in this repository are synthetic and are used exclusively to demonstrate the analytical methodology.

## 5. Technology Stack

- **Python:** Data processing and analysis.
- **Pandas:** Data manipulation, aggregation, and KPI calculation.
- **NumPy:** Numerical operations.
- **Power BI Desktop:** Interactive reporting and visualization.
- **CSV:** Data storage and exchange.
- **Git and GitHub:** Version control and project management.

## 6. Project Workflow

The project follows an end-to-end data analysis workflow.

### Step 1 — Data Generation

A synthetic dataset is generated to simulate maintenance interventions across multiple production zones and equipment units.

### Step 2 — Data Cleaning and Preparation

The preparation process includes:

- Loading the raw CSV dataset.
- Inspecting the dataset structure.
- Converting data types.
- Standardizing intervention categories.
- Checking duplicate records.
- Validating intervention dates.
- Checking repair duration consistency.
- Preparing a clean dataset for analysis.

Main script: `src/analyze_data.py`

### Step 3 — Exploratory Data Analysis

The dataset is analyzed to understand:

- Maintenance intervention distribution.
- Downtime patterns.
- Failure causes.
- Corrective and preventive maintenance.
- Equipment performance.
- Spare parts costs.
- Monthly and weekly trends.

### Step 4 — Business Analysis

Python and Pandas are used to calculate KPIs and generate aggregated datasets.

Main script: `src/business_analysis.py`

The analysis generates:

| Output | Purpose |
|---|---|
| `downtime_by_zone.csv` | Downtime comparison across production zones |
| `pareto_analysis.csv` | Ranking of failure causes by downtime |
| `cost_by_type.csv` | Spare parts cost analysis by intervention type |
| `downtime_by_type.csv` | Downtime comparison by intervention type |
| `equipment_performance.csv` | Equipment-level performance analysis |
| `monthly_performance.csv` | Monthly maintenance performance |
| `weekly_performance.csv` | Weekly maintenance performance |

## 7. Key Performance Indicators

The project focuses on the following maintenance KPIs:

| KPI | Definition |
|---|---|
| Total Equipment | Number of distinct equipment units |
| Total Interventions | Total number of maintenance interventions |
| Total Downtime | Sum of equipment downtime |
| Average Downtime | Total downtime divided by the number of interventions |
| Corrective Rate | Corrective interventions divided by total interventions |
| Corrective MTTR | Average repair duration for corrective interventions |
| Spare Parts Cost | Sum of spare parts costs |

### KPI calculation details

**Total Downtime (hours)**

\[
\frac{\sum Downtime\ Minutes}{60}
\]

**Average Downtime (minutes)**

\[
\frac{\sum Downtime\ Minutes}{Number\ of\ Interventions}
\]

**Corrective Rate (%)**

\[
\frac{Corrective\ Interventions}{Total\ Interventions}\times100
\]

**Corrective MTTR (minutes)**

Average repair duration calculated using corrective interventions only.

**Spare Parts Cost**

Sum of the spare parts cost values.

MTBF and equipment availability are not calculated in this version because reliable equipment operating-time data is not available in the dataset.

## 8. Key Results and Findings

The following results were obtained from the synthetic dataset.

### Overall maintenance performance

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

Corrective interventions represent the largest share of maintenance activities and downtime in this synthetic dataset.

### Downtime by Production Zone

| Production Zone | Downtime (minutes) | Share |
|---|---:|---:|
| Assembly | 15,399 | 23.4% |
| Injection | 14,667 | 22.3% |
| Electrical Control | 12,237 | 18.6% |
| Preparation | 12,085 | 18.4% |
| Cutting | 11,408 | 17.3% |

Assembly and Injection record the highest downtime, together accounting for approximately 45.7% of total downtime.

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

This Pareto analysis helps identify the categories that deserve priority during further investigation.

### Equipment Performance

The equipment-level analysis identifies the equipment with the highest accumulated downtime.

| Equipment | Downtime (minutes) |
|---|---:|
| EQ-012 | 6,315 |
| EQ-005 | 5,902 |
| EQ-013 | 5,608 |

These three equipment units account for approximately 27.1% of total downtime in the synthetic dataset.

### Monthly Performance

The monthly analysis highlights variations in maintenance activity over the dataset period.

- January recorded the highest downtime: 10,068 minutes.
- September recorded the lowest downtime: 4,650 minutes.
- January also recorded the highest intervention volume: 72 interventions.
- September recorded the lowest intervention volume: 39 interventions.

These variations demonstrate the importance of monitoring maintenance performance over time rather than relying only on cumulative indicators.

## 9. Insights and Business Recommendations

The analytical findings can be translated into potential improvement actions when applied to validated operational data.

**1. Prioritize zones with the highest downtime**

Assembly and Injection account for approximately 45.7% of downtime in the synthetic dataset.

An equipment-level investigation in these zones could help identify the main operational contributors.

**2. Investigate the leading failure causes**

Mechanical failures represent the largest failure category, accounting for approximately 21.7% of downtime.

A root-cause analysis and review of mechanical maintenance practices could be considered.

**3. Investigate operator-related factors**

Operator error represents approximately 16.8% of downtime.

Potential actions include reviewing operating procedures, identifying training needs, and examining process-related factors.

**4. Monitor the balance between corrective and preventive maintenance**

Corrective interventions represent 73.8% of total interventions.

Monitoring the corrective rate and corrective MTTR can help assess maintenance performance and identify opportunities to strengthen preventive maintenance.

**5. Establish a KPI monitoring baseline**

Total downtime, corrective rate, and corrective MTTR can serve as baseline indicators for periodic performance reviews.

These recommendations are analytical interpretations of synthetic results, not conclusions about COFAT or any other real industrial site.

## 10. Power BI Dashboard

The project includes an interactive Power BI report:

`reports/Maintenance_Performance_Analytics.pbix`

The dashboard provides an overview of maintenance performance through:

- Total Equipment KPI.
- Total Interventions KPI.
- Total Downtime KPI.
- Downtime by Production Zone.
- Downtime by Failure Cause.
- Corrective vs Preventive Intervention Distribution.
- Production Zone slicer.
- Intervention Type slicer.

The report is designed to provide a clear overview of maintenance activities and support interactive exploration of the dataset.

Additional analytical datasets are available for equipment performance, Pareto analysis, costs, and time-based monitoring.

## 11. Repository Structure

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

## 12. How to Run the Project

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

### Generate the synthetic dataset

```bash
python src/generate_data.py
```

### Run data preparation

```bash
python src/analyze_data.py
```

### Run business analysis

```bash
python src/business_analysis.py
```

The processed datasets are exported to:

```text
data/processed/
```

### Open the Power BI report

Open:

```text
reports/Maintenance_Performance_Analytics.pbix
```

If necessary, update the source path in Power BI to point to the local repository's `data/processed/maintenance_clean.csv` file.

## 13. Limitations and Future Improvements

### Current limitations

- The dataset is synthetic and does not represent real industrial performance.
- MTBF and availability require reliable equipment operating-time data.
- Cost analysis depends on the availability and correct numerical interpretation of spare parts cost values.
- The current dashboard focuses on descriptive and diagnostic analytics rather than predictive modelling.

### Potential improvements

- Add SQL queries for data extraction and analysis.
- Develop equipment criticality scoring.
- Introduce maintenance performance targets.
- Add more advanced time-based Power BI analysis.
- Explore predictive maintenance indicators when sufficient historical data is available.

## 14. Author

**Asma Ghanmi**

Computer Engineering Student | Data Analytics | Python | Power BI | Software Engineering

- GitHub: [asmaghanmi1](https://github.com/asmaghanmi1)
- LinkedIn: [Asma Ghanmi](https://www.linkedin.com/in/asma-ghanmi-353992269/)

---

*This repository is an independent portfolio case study demonstrating data preparation, Python-based analysis, maintenance KPI development, and Business Intelligence reporting.*