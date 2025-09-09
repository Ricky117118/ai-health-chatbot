import pandas as pd
import json

# Process disease symptoms
df = pd.read_csv("datasets/disease_symptoms.csv")
disease_dict = {row["Disease"].strip().lower(): row["Symptoms"].strip() for _, row in df.iterrows()}
with open("data/disease_symptoms.json", "w") as f:
    json.dump(disease_dict, f, indent=4)

# Process vaccine schedules
df2 = pd.read_csv("datasets/vaccine_schedule.csv")
vaccine_dict = {row["Vaccine"].strip().lower(): row["Schedule"].strip() for _, row in df2.iterrows()}
with open("data/vaccine_schedule.json", "w") as f:
    json.dump(vaccine_dict, f, indent=4)

print("✅ Preprocessing complete!")
