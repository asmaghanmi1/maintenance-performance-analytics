
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/maintenance_clean.csv")

# A. Downtime by production zone
zone_analysis = (
    df.groupby("zone")
    .agg(
        total_downtime=("downtime_minutes", "sum"),
        number_of_interventions=("intervention_id", "count"),
        average_downtime=("downtime_minutes", "mean")
    )
    .sort_values("total_downtime", ascending=False)
)

print("\n========== DOWNTIME BY ZONE ==========")
print(zone_analysis.round(2))

# B. Downtime by failure cause
cause_analysis = (
    df.groupby("failure_cause")
    .agg(
        total_downtime=("downtime_minutes", "sum"),
        number_of_interventions=("intervention_id", "count")
    )
    .sort_values("total_downtime", ascending=False)
)

cause_analysis["downtime_percentage"] = (
    cause_analysis["total_downtime"]
    / cause_analysis["total_downtime"].sum() * 100
)

cause_analysis["cumulative_percentage"] = (
    cause_analysis["downtime_percentage"].cumsum()
)

print("\n========== PARETO ANALYSIS ==========")
print(cause_analysis.round(2))

# C. Cost analysis by intervention type
cost_analysis = (
    df.groupby("intervention_type")
    .agg(
        total_cost=("spare_part_cost", "sum"),
        average_cost=("spare_part_cost", "mean"),
        number_of_interventions=("intervention_id", "count")
    )
)

print("\n========== COST BY INTERVENTION TYPE ==========")
print(cost_analysis.round(2))

# D. Corrective vs preventive downtime
type_analysis = (
    df.groupby("intervention_type")
    .agg(
        total_downtime=("downtime_minutes", "sum"),
        average_downtime=("downtime_minutes", "mean"),
        number_of_interventions=("intervention_id", "count")
    )
)

print("\n========== DOWNTIME BY TYPE ==========")
print(type_analysis.round(2))

# Export analysis results
zone_analysis.to_csv("data/processed/downtime_by_zone.csv")
cause_analysis.to_csv("data/processed/pareto_analysis.csv")
cost_analysis.to_csv("data/processed/cost_by_type.csv")
type_analysis.to_csv("data/processed/downtime_by_type.csv")

print("\nAnalysis completed successfully!")
print("4 analysis files exported to data/processed/")
