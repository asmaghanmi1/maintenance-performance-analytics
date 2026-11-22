# Maintenance Performance Analytics

## Project Overview

Maintenance Performance Analytics is a personal data analytics project focused on analyzing maintenance operations, equipment downtime, failure causes, intervention types, and spare parts costs.

The project demonstrates a data analytics workflow using Python, Pandas, and Power BI.

**Dataset:** 500 synthetic maintenance interventions created for educational and portfolio purposes. No real company data is used.

## Business Objectives

- Analyze maintenance intervention data.
- Identify the main causes of equipment downtime.
- Compare preventive and corrective maintenance.
- Analyze downtime across production zones.
- Examine spare parts costs.
- Build an interactive Power BI dashboard.

## Technologies

- Python 3.13
- Pandas
- NumPy
- Matplotlib
- Power BI Desktop
- CSV

## Project Structure

```text
maintenance-performance-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── reports/
├── sql/
├── src/
│   ├── generate_data.py
│   ├── analyze_data.py
│   └── business_analysis.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Analytics Workflow

1. Synthetic dataset generation.
2. Data cleaning and quality checks.
3. Exploratory data analysis.
4. Business analysis of downtime, failure causes, and costs.
5. Power BI dashboard development.

## Key Business Questions

- Which production zones have the highest downtime?
- What are the main causes of equipment failures?
- What is the distribution of preventive and corrective interventions?
- How are spare parts costs distributed?

## Power BI Dashboard

The dashboard includes:

- Total equipment
- Total interventions
- Total downtime
- Downtime by production zone
- Downtime by failure cause
- Preventive vs. corrective intervention distribution
- Interactive filters

## How to Run

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Generate the dataset:

```bash
python src/generate_data.py
```

Run data cleaning and analysis:

```bash
python src/analyze_data.py
```

Run business analysis:

```bash
python src/business_analysis.py
```

## Disclaimer

This project uses synthetic data and is intended for educational and professional portfolio purposes. It does not represent the actual performance of any company.