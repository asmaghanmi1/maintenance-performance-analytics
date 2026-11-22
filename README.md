# Maintenance Performance Analytics

**Maintenance Data Analysis | Python | Power BI | Business Intelligence**

## 1. Project Overview

Maintenance Performance Analytics is a Business Intelligence and data analysis project focused on maintenance performance monitoring.

The project demonstrates how maintenance data can be transformed into actionable insights through data preparation, KPI calculation, performance analysis, and interactive Power BI visualizations.

The main objectives are to:

- Monitor maintenance activities and downtime.
- Identify equipment with the highest downtime.
- Analyze recurring failure causes.
- Compare corrective and preventive maintenance.
- Examine maintenance costs.
- Track performance trends over time.
- Support maintenance decision-making through data visualization.

## 2. Professional Context

During my professional experience at **COFAT**, I contributed to recurring weekly and monthly maintenance reporting using Excel.

These reports provided operational visibility into maintenance activities, equipment downtime, and performance indicators.

I also identified an opportunity to extend the existing reporting approach through Business Intelligence.

The proposed analytical approach involved using a three-month maintenance dataset to:

- Identify problematic equipment.
- Understand the main sources of downtime.
- Analyze maintenance performance.
- Prioritize improvement opportunities.
- Define measurable performance objectives.

Due to company confidentiality requirements, internal operational data and reports are not included in this public repository.

This project independently demonstrates the analytical approach using a synthetic dataset. It is not a reproduction of COFAT's actual operational results, nor does it represent a deployed Power BI solution at COFAT.

## 3. Dataset Description

The project uses a synthetic dataset containing **500 maintenance interventions**.

| Attribute | Description |
|---|---|
| Number of records | 500 |
| Equipment | 15 |
| Production zones | 5 |
| Period covered | January–October 2026 |
| Data format | CSV |
| Data source | Synthetic dataset generated with Python |

### Dataset fields

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

**Important:** All records and numerical findings presented in this repository come from synthetic data. They must not be interpreted as actual COFAT operational results.

## 4. Technology Stack

- **Python:** Data preparation, transformation, analysis, and KPI calculation.
- **Pandas:** Data manipulation and aggregation.
- **NumPy:** Numerical operations.
- **Power BI Desktop:** Interactive dashboard and data visualization.
- **CSV:** Data storage and exchange.
- **Git & GitHub:** Version control and project documentation.

## 5. Project Architecture

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

## 6. Data Analysis Workflow

The project follows a structured data analysis process.

### Step 1 — Data Generation

A synthetic maintenance dataset is generated to simulate maintenance interventions across different production zones and equipment.

### Step 2 — Data Preparation

The data preparation process includes:

- Loading the raw CSV dataset.
- Checking data structure and column types.
- Converting numerical and date fields.
- Standardizing intervention categories.
- Checking duplicate records.
- Validating intervention dates and durations.
- Preparing a clean dataset for analysis.

### Step 3 — Exploratory Data Analysis

The dataset is analyzed to understand:

- Intervention distribution.
- Downtime patterns.
- Failure causes.
- Maintenance costs.
- Equipment performance.
- Monthly and weekly trends.

### Step 4 — KPI Calculation and Business Analysis

Python scripts generate aggregated datasets for further analysis and visualization.

The main analytical outputs include:

| Analysis | Objective |
|---|---|
| Downtime by zone | Compare production zones |
| Pareto analysis | Identify the main contributors to downtime |
| Cost by intervention type | Compare spare parts costs |
| Downtime by intervention type | Compare corrective and preventive maintenance |
| Equipment performance | Identify equipment requiring attention |
| Monthly performance | Monitor monthly trends |
| Weekly performance | Monitor weekly trends |

## 7. Key Performance Indicators

The project focuses on maintenance indicators such as:

| KPI | Description |
|---|---|
| Total Equipment | Number of distinct equipment |
| Total Interventions | Number of maintenance interventions |
| Total Downtime | Accumulated downtime |
| Average Downtime | Average downtime per intervention |
| Corrective Rate | Share of corrective interventions |
| Corrective MTTR | Average repair duration for corrective interventions |
| Spare Parts Cost | Total spare parts cost |

**MTTR calculation:**

The corrective MTTR is calculated using the average repair duration of corrective interventions.

MTBF and equipment availability are not calculated in this version because reliable equipment operating-time data is not available in the dataset.

## 8. Key Findings from the Synthetic Dataset

The following results are obtained from the 500 synthetic interventions.

### Overall maintenance performance

| Indicator | Result |
|---|---:|
| Total interventions | 500 |
| Total equipment | 15 |
| Total downtime | 65,796 minutes |
| Total downtime in hours | 1,096.60 hours |
| Corrective interventions | 369 |
| Preventive interventions | 131 |
| Corrective MTTR | 130.15 minutes |

### Corrective vs Preventive Maintenance

- Corrective interventions represent 73.8% of all interventions.
- Preventive interventions represent 26.2%.
- Corrective maintenance accounts for 63,770 minutes of downtime.
- Preventive maintenance accounts for 2,026 minutes of downtime.

### Downtime by Production Zone

| Production Zone | Downtime (minutes) |
|---|---:|
| Assembly | 15,399 |
| Injection | 14,667 |
| Electrical Control | 12,237 |
| Preparation | 12,085 |
| Cutting | 11,408 |

Assembly and Injection record the highest downtime in this synthetic dataset.

### Pareto Analysis

The Pareto analysis highlights the main contributors to downtime.

The five largest failure categories account for approximately **83.96% of total downtime**.

This analysis helps demonstrate how maintenance teams can prioritize investigation and improvement actions based on the relative contribution of failure causes.

### Equipment Performance

Equipment-level aggregation is used to compare:

- Total downtime.
- Number of interventions.
- Average downtime.
- Spare parts costs.
- Corrective interventions.
- Corrective repair duration.

The objective is to identify equipment that deserves further investigation rather than assuming that intervention frequency alone determines equipment criticality.

### Monthly and Weekly Performance

The project also includes monthly and weekly aggregations to monitor changes in:

- Intervention volume.
- Total downtime.
- Average downtime.
- Spare parts costs.

These time-based analyses provide an additional perspective on maintenance activity and performance trends.

## 9. Power BI Dashboard

The Power BI report provides an interactive view of maintenance performance.

The dashboard includes:

- Total Equipment KPI.
- Total Interventions KPI.
- Total Downtime KPI.
- Downtime by Production Zone.
- Downtime by Failure Cause.
- Corrective vs Preventive Intervention Distribution.
- Production Zone and Intervention Type slicers.

Additional analytical datasets are prepared for equipment performance, cost analysis, Pareto analysis, and time-based monitoring.

The Power BI report is available in:

`reports/Maintenance_Performance_Analytics.pbix`

## 10. How to Run the Project

### Prerequisites

- Python 3.10 or later.
- Power BI Desktop.
- Git.

### Clone the repository

```bash
git clone https://github.com/asmaghanmi1/maintenance-performance-analytics.git
```

```bash
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

### Run the data analysis

```bash
python src/analyze_data.py
```

### Run the business analysis

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

If necessary, update the CSV source path in Power BI to point to the local repository's `data/processed/maintenance_clean.csv` file.

## 11. Business Value

This project demonstrates how maintenance reporting can evolve from periodic operational reporting toward a more analytical and decision-oriented approach.

It illustrates how data analysis and Business Intelligence can support:

- Better visibility into maintenance performance.
- Identification of major downtime contributors.
- Equipment performance monitoring.
- More structured maintenance prioritization.
- Cost monitoring.
- KPI-based decision support.

The objective is not simply to present maintenance figures, but to transform operational data into meaningful information that can support improvement decisions.

## 12. Limitations and Future Improvements

Potential improvements include:

- Adding a dedicated equipment criticality analysis.
- Integrating reliable equipment operating-time data to calculate MTBF and availability.
- Improving cost analysis and financial reporting.
- Developing more advanced Power BI time-based visualizations.
- Adding maintenance performance targets.
- Exploring predictive maintenance indicators.

## 13. Author

**Asma Ghanmi**

Computer Engineering Student | Cloud & DevOps | Software Engineering | Data Analytics

- GitHub: [asmaghanmi1](https://github.com/asmaghanmi1)
- LinkedIn: [Asma Ghanmi](https://www.linkedin.com/in/asma-ghanmi-353992269/)

---

*This repository is an independent portfolio project demonstrating practical skills in Python-based data analysis, maintenance performance monitoring, KPI development, and Power BI reporting.*