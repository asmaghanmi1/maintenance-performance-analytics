
import pandas as pd
import numpy as np

# Reproducible synthetic dataset
np.random.seed(42)

NUMBER_OF_RECORDS = 500

equipment_ids = [f"EQ-{i:03d}" for i in range(1, 16)]

zones = [
    "Cutting",
    "Preparation",
    "Injection",
    "Assembly",
    "Electrical Control"
]

failure_causes = [
    "Mechanical Failure",
    "Electrical Failure",
    "Sensor Failure",
    "Hydraulic Failure",
    "Operator Error",
    "Wear and Tear"
]

records = []

for i in range(1, NUMBER_OF_RECORDS + 1):

    intervention_type = np.random.choice(
        ["Corrective", "Preventive"],
        p=[0.75, 0.25]
    )

    start_datetime = (
        pd.Timestamp("2026-01-01")
        + pd.Timedelta(
            minutes=int(np.random.randint(0, 304 * 24 * 60))
        )
    )

    if intervention_type == "Corrective":
        repair_duration = int(np.random.randint(20, 241))
        downtime = repair_duration + int(np.random.randint(0, 91))
        failure_cause = np.random.choice(failure_causes)
        spare_part_cost = round(
            float(np.random.uniform(20, 600)), 2
        )
    else:
        repair_duration = int(np.random.randint(10, 91))
        downtime = int(np.random.randint(0, 31))
        failure_cause = "Preventive Maintenance"
        spare_part_cost = round(
            float(np.random.uniform(0, 150)), 2
        )

    end_datetime = start_datetime + pd.Timedelta(
        minutes=downtime
    )

    records.append({
        "intervention_id": f"INT-{i:04d}",
        "equipment_id": np.random.choice(equipment_ids),
        "zone": np.random.choice(zones),
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "downtime_minutes": downtime,
        "repair_duration_minutes": repair_duration,
        "failure_cause": failure_cause,
        "intervention_type": intervention_type,
        "spare_part_cost": spare_part_cost
    })

df = pd.DataFrame(records)

output_path = "data/raw/maintenance_interventions.csv"
df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print("Number of records:", len(df))
print("Number of columns:", len(df.columns))
print("Saved to:", output_path)
print("\nFirst 5 records:")
print(df.head())
