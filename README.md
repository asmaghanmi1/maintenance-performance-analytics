# Maintenance Performance Analytics

**Business Intelligence | Data Analytics | Maintenance Performance Improvement**

An independent BI case study inspired by professional experience in industrial maintenance reporting at COFAT, Tunisia.

---

## 1. Project Overview

During my professional experience at COFAT, I contributed to recurring weekly and monthly maintenance reporting using Excel.

To explore opportunities for improving the analytical dimension of this reporting, I proposed extending the existing approach through Business Intelligence tools, particularly Power BI.

The proposed initiative involved analyzing three months of maintenance data to:

- Identify problematic equipment.
- Understand equipment downtime patterns.
- Analyze recurring failure causes.
- Prioritize maintenance improvement actions.
- Define measurable performance objectives.
- Monitor maintenance performance through interactive dashboards.

This GitHub project is an independent portfolio demonstration of that analytical approach, using Python and Power BI with a synthetic dataset.

## 2. Business Context & Analytical Objectives

The project focuses on six business questions:

| Analytical Area | Business Question |
|---|---|
| Equipment Performance | Which equipment generates the highest downtime? |
| Downtime Analysis | How is downtime distributed across production zones? |
| Failure Analysis | Which failure causes contribute most to downtime? |
| Maintenance Strategy | What is the distribution of preventive and corrective interventions? |
| Improvement Priorities | Which failure categories should receive attention first? |
| Performance Monitoring | Which indicators can help monitor improvement objectives? |

## 3. Dataset Description

The project uses a synthetic dataset of 500 maintenance interventions generated with Python.

### Dataset characteristics

- 500 maintenance interventions.
- 15 distinct equipment units.
- 5 production zones.
- Preventive and corrective interventions.
- Multiple failure causes.
- Downtime, repair duration and spare parts cost information.

### Data dictionary

| Column | Description |
|---|---|
| `intervention_id` | Unique intervention identifier |
| `equipment_id` | Equipment identifier |
| `zone` | Production area |
| `start_datetime` | Intervention start date and time |
| `end_datetime` | Intervention end date and time |
| `downtime_minutes` | Equipment downtime in minutes |
| `repair_duration_minutes` | Repair duration in minutes |
| `failure_cause` | Identified failure cause |
| `intervention_type` | Preventive or corrective |
| `spare_part_cost` | Spare parts cost associated with the intervention |

## 4. Methodology & Technical Stack

### Tools and technologies

- **Python:** data generation and analysis.
- **Pandas:** data preparation and manipulation.
- **NumPy:** numerical operations.
- **Matplotlib:** data visualization.
- **Power BI Desktop:** interactive dashboards and business intelligence.
- **CSV:** data storage and exchange.
- **Git & GitHub:** version control and project publishing.

### Analytical workflow

1. **Data Generation:** create a synthetic maintenance dataset.
2. **Data Preparation:** inspect, clean and prepare the data for analysis.
3. **Exploratory Data Analysis:** examine intervention activity, downtime, failure causes and spare parts costs.
4. **Business Analysis:** calculate performance indicators and generate analytical summaries.
5. **Data Visualization:** build interactive Power BI dashboards to explore maintenance performance.

## 5. Key Performance Indicators

The project uses the following indicators:

| KPI | Definition |
|---|---|
| Total Interventions | Number of recorded maintenance interventions |
| Total Equipment | Number of distinct equipment units |
| Total Downtime | Sum of equipment downtime |
| Corrective Maintenance Rate | Corrective interventions / Total interventions × 100 |
| Preventive Maintenance Rate | Preventive interventions / Total interventions × 100 |
| Spare Parts Cost | Sum of spare parts costs |
| MTTR | Average repair duration for corrective interventions |

### KPI calculation notes

**Total Downtime (hours)**

`SUM(downtime_minutes) / 60`

**Corrective Maintenance Rate**

`(Corrective interventions / Total interventions) × 100`

**Preventive Maintenance Rate**

`(Preventive interventions / Total interventions) × 100`

**MTTR**

`Average(repair_duration_minutes)` for corrective interventions.

**MTBF and Availability:** These indicators require reliable equipment operating-time and failure-interval information. They are not presented as calculated results in this case study because the required operating-time information is not available in the current dataset.

## 6. Key Analytical Results

The following findings are derived exclusively from the synthetic dataset.

### Dataset overview

| Indicator | Result |
|---|---:|
| Total interventions | 500 |
| Distinct equipment | 15 |
| Total downtime | 65,796 minutes |
| Total downtime | 1,096.6 hours |
| Corrective interventions | 369 (73.8%) |
| Preventive interventions | 131 (26.2%) |

### Downtime by production zone

| Production Zone | Downtime (minutes) |
|---|---:|
| Assembly | 15,399 |
| Injection | 14,667 |
| Electrical Control | 12,237 |
| Preparation | 12,085 |
| Cutting | 11,408 |

Assembly and Injection have the highest downtime in this synthetic dataset.

### Pareto analysis of failure causes

| Failure Cause | Downtime (minutes) | Contribution |
|---|---:|---:|
| Mechanical Failure | 14,285 | 21.71% |
| Operator Error | 11,048 | 16.79% |
| Hydraulic Failure | 10,458 | 15.90% |
| Wear and Tear | 10,196 | 15.49% |
| Electrical Failure | 9,254 | 14.07% |
| Sensor Failure | 8,529 | 12.96% |
| Preventive Maintenance | 2,026 | 3.08% |

The five largest categories account for approximately **83.96% of total downtime**.

### Maintenance type analysis

Corrective interventions represent 73.8% of all recorded interventions and account for 63,770 minutes of downtime.

Preventive interventions represent 26.2% of interventions and account for 2,026 minutes of downtime.

These figures describe the synthetic dataset and should not be interpreted as actual COFAT performance measurements or proof of preventive maintenance effectiveness.

## 7. Business Insights & Recommendations

Based on the synthetic analysis, the following improvement priorities can be explored:

**1. Focus on high-impact failure causes**

Mechanical, hydraulic and electrical failures contribute significantly to downtime. These categories can be prioritized for further investigation.

**2. Examine high-downtime production zones**

Assembly and Injection show the highest downtime in the dataset. A more detailed equipment-level analysis could help identify the main contributors within these zones.

**3. Strengthen preventive maintenance monitoring**

The distribution between preventive and corrective interventions provides a starting point for reviewing maintenance activity and identifying opportunities for better preventive planning.

**4. Monitor spare parts expenditure**

Analyzing spare parts costs by intervention type and failure cause can help identify major cost contributors and support stock management decisions.

**5. Define measurable improvement objectives**

Maintenance teams can use indicators such as downtime, corrective intervention rate and MTTR to establish performance baselines and monitor future improvement actions.

These recommendations are analytical proposals based on synthetic results, not actions implemented at COFAT.

## 8. Power BI Dashboard

The Power BI report provides an interactive view of maintenance performance.

The dashboard includes:

- Total equipment.
- Total interventions.
- Total downtime.
- Downtime by production zone.
- Downtime by failure cause.
- Preventive versus corrective intervention distribution.
- Filters for production zone and intervention type.

**Power BI report:** [Maintenance Performance Analytics](reports/Maintenance_Performance_Analytics.pbix)

## 9. Repository Structure

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
├── README.md
└── .gitignore
```

## 10. How to Run the Project

### Prerequisites

- Python 3.x
- Power BI Desktop (to open the dashboard)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate the synthetic dataset

```bash
python src/generate_data.py
```

### Run data analysis

```bash
python src/analyze_data.py
```

### Run business analysis

```bash
python src/business_analysis.py
```

The generated and processed CSV files are stored in the `data/` directory.

Open the Power BI report in `reports/` using Power BI Desktop.

## 11. Limitations & Future Improvements

### Current limitations

- The dataset is entirely synthetic.
- Results do not represent actual company performance.
- MTBF and availability are not calculated because equipment operating-time information is not available.
- The analysis is intended as a portfolio demonstration.

### Future improvements

- Add SQL queries for structured data analysis.
- Develop more detailed equipment-level performance analysis.
- Extend the KPI model with reliable operating-time information.
- Improve dashboard interactivity and analytical depth.

## 12. Data Confidentiality

This repository is an independent portfolio project inspired by professional experience at COFAT, Tunisia.

No internal COFAT datasets, reports, databases or confidential operational records are included.

All data were generated synthetically for demonstration purposes. The Python analyses, numerical findings and Power BI dashboard presented in this repository are independent portfolio work and must not be interpreted as official COFAT results.

---

## Author

**Asma Ghanmi**

Computer Engineering Student | Cloud, Software & Data Analytics

- GitHub: [asmaghanmi1](https://github.com/asmaghanmi1)
- LinkedIn: [Asma Ghanmi](https://www.linkedin.com/in/asma-ghanmi-353992269/)