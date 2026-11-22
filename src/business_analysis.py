
import pandas as pd
from pathlib import Path

# ============================================================
# 1. CONFIGURATION AND DATA LOADING
# ============================================================

DATA_PATH = Path("data/processed/maintenance_clean.csv")
OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Convert numeric columns
numeric_columns = [
    "downtime_minutes",
    "repair_duration_minutes",
    "spare_part_cost"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Standardize intervention types
df["intervention_type"] = (
    df["intervention_type"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# Convert dates
df["start_datetime"] = pd.to_datetime(
    df["start_datetime"],
    errors="coerce"
)

# ============================================================
# 2. DOWNTIME BY PRODUCTION ZONE
# ============================================================

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


# ============================================================
# 3. PARETO ANALYSIS BY FAILURE CAUSE
# ============================================================

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
    / cause_analysis["total_downtime"].sum()
    * 100
)

cause_analysis["cumulative_percentage"] = (
    cause_analysis["downtime_percentage"].cumsum()
)

print("\n========== PARETO ANALYSIS ==========")
print(cause_analysis.round(2))


# ============================================================
# 4. COST ANALYSIS BY INTERVENTION TYPE
# ============================================================

cost_analysis = (
    df.groupby("intervention_type")
    .agg(
        total_cost=("spare_part_cost", "sum"),
        average_cost=("spare_part_cost", "mean"),
        number_of_interventions=("intervention_id", "count")
    )
    .sort_values("total_cost", ascending=False)
)

print("\n========== COST BY INTERVENTION TYPE ==========")
print(cost_analysis.round(2))


# ============================================================
# 5. CORRECTIVE VS PREVENTIVE DOWNTIME
# ============================================================

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


# ============================================================
# 6. EQUIPMENT-LEVEL PERFORMANCE ANALYSIS
# ============================================================

equipment_analysis = (
    df.groupby("equipment_id")
    .agg(
        total_downtime=("downtime_minutes", "sum"),
        number_of_interventions=("intervention_id", "count"),
        average_downtime=("downtime_minutes", "mean"),
        total_spare_part_cost=("spare_part_cost", "sum"),
        average_spare_part_cost=("spare_part_cost", "mean")
    )
)

# Filter corrective interventions
corrective_df = df[
    df["intervention_type"] == "corrective"
]

# Calculate corrective MTTR by equipment
equipment_mttr = (
    corrective_df.groupby("equipment_id")
    .agg(
        corrective_interventions=("intervention_id", "count"),
        corrective_downtime=("downtime_minutes", "sum"),
        mttr_minutes=("repair_duration_minutes", "mean")
    )
)

equipment_analysis = equipment_analysis.join(
    equipment_mttr,
    how="left"
)

# Calculate each equipment's contribution to total downtime
total_downtime = df["downtime_minutes"].sum()

equipment_analysis["downtime_share_percentage"] = (
    equipment_analysis["total_downtime"]
    / total_downtime
    * 100
)

equipment_analysis = equipment_analysis.sort_values(
    "total_downtime",
    ascending=False
)

print("\n========== EQUIPMENT PERFORMANCE ANALYSIS ==========")
print(equipment_analysis.round(2))


# ============================================================
# 7. OVERALL MAINTENANCE KPIs
# ============================================================

overall_mttr = corrective_df["repair_duration_minutes"].mean()

total_spare_part_cost = df["spare_part_cost"].sum()

corrective_downtime = corrective_df["downtime_minutes"].sum()

preventive_df = df[
    df["intervention_type"] == "preventive"
]

print("\n========== OVERALL MAINTENANCE KPIs ==========")

print(f"Total equipment: {df['equipment_id'].nunique()}")
print(f"Total interventions: {len(df)}")
print(f"Total downtime: {total_downtime:.2f} minutes")
print(f"Corrective interventions: {len(corrective_df)}")
print(f"Preventive interventions: {len(preventive_df)}")
print(f"Corrective downtime: {corrective_downtime:.2f} minutes")
print(f"Corrective MTTR: {overall_mttr:.2f} minutes")
print(f"Total spare parts cost: {total_spare_part_cost:.2f}")


# ============================================================
# 8. MONTHLY PERFORMANCE ANALYSIS
# ============================================================

dated_df = df.dropna(subset=["start_datetime"]).copy()

monthly_analysis = (
    dated_df.set_index("start_datetime")
    .resample("ME")
    .agg(
        number_of_interventions=("intervention_id", "count"),
        total_downtime=("downtime_minutes", "sum"),
        average_downtime=("downtime_minutes", "mean"),
        total_spare_part_cost=("spare_part_cost", "sum")
    )
)

monthly_analysis.index = monthly_analysis.index.strftime("%Y-%m")

print("\n========== MONTHLY PERFORMANCE ==========")
print(monthly_analysis.round(2))


# ============================================================
# 9. WEEKLY PERFORMANCE ANALYSIS
# ============================================================

weekly_analysis = (
    dated_df.set_index("start_datetime")
    .resample("W")
    .agg(
        number_of_interventions=("intervention_id", "count"),
        total_downtime=("downtime_minutes", "sum"),
        average_downtime=("downtime_minutes", "mean"),
        total_spare_part_cost=("spare_part_cost", "sum")
    )
)

print("\n========== WEEKLY PERFORMANCE ==========")
print(weekly_analysis.round(2))


# ============================================================
# 10. EXPORT ANALYSIS RESULTS
# ============================================================

zone_analysis.to_csv(
    OUTPUT_DIR / "downtime_by_zone.csv"
)

cause_analysis.to_csv(
    OUTPUT_DIR / "pareto_analysis.csv"
)

cost_analysis.to_csv(
    OUTPUT_DIR / "cost_by_type.csv"
)

type_analysis.to_csv(
    OUTPUT_DIR / "downtime_by_type.csv"
)

equipment_analysis.to_csv(
    OUTPUT_DIR / "equipment_performance.csv"
)

monthly_analysis.to_csv(
    OUTPUT_DIR / "monthly_performance.csv"
)

weekly_analysis.to_csv(
    OUTPUT_DIR / "weekly_performance.csv"
)


# ============================================================
# 11. COMPLETION SUMMARY
# ============================================================

print("\n========== EXPORT SUMMARY ==========")
print("Analysis completed successfully!")
print("7 analysis files exported to data/processed/")

print("\nGenerated files:")
print("- downtime_by_zone.csv")
print("- pareto_analysis.csv")
print("- cost_by_type.csv")
print("- downtime_by_type.csv")
print("- equipment_performance.csv")
print("- monthly_performance.csv")
print("- weekly_performance.csv")
