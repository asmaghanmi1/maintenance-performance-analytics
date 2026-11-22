
import pandas as pd

# 1. Load the raw dataset
file_path = "data/raw/maintenance_interventions.csv"
df = pd.read_csv(file_path)

# 2. General information
print("\n========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== COLUMN TYPES ==========")
print(df.dtypes)

# 3. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Duplicate records
print("\n========== DUPLICATES ==========")
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate intervention IDs:",
      df["intervention_id"].duplicated().sum())

# 5. Convert dates to datetime
df["start_datetime"] = pd.to_datetime(df["start_datetime"])
df["end_datetime"] = pd.to_datetime(df["end_datetime"])

# 6. Check invalid values
print("\n========== DATA QUALITY CHECKS ==========")

print("Negative downtime:",
      (df["downtime_minutes"] < 0).sum())

print("Negative repair duration:",
      (df["repair_duration_minutes"] < 0).sum())

print("Negative spare part cost:",
      (df["spare_part_cost"] < 0).sum())

print("End date before start date:",
      (df["end_datetime"] < df["start_datetime"]).sum())

# Corrective downtime should be at least as long as repair duration
corrective = df[df["intervention_type"] == "Corrective"]

print("Corrective downtime shorter than repair:",
      (corrective["downtime_minutes"] <
       corrective["repair_duration_minutes"]).sum())

# 7. Basic statistical analysis
print("\n========== NUMERICAL SUMMARY ==========")
print(df[[
    "downtime_minutes",
    "repair_duration_minutes",
    "spare_part_cost"
]].describe().round(2))

# 8. Save a cleaned copy
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["intervention_id"])

output_path = "data/processed/maintenance_clean.csv"
df.to_csv(output_path, index=False)

print("\n========== CLEANING RESULT ==========")
print("Rows after cleaning:", len(df))
print("Clean dataset saved to:", output_path)
