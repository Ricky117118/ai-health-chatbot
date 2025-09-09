import pandas as pd
import yaml

# Load CSV
df = pd.read_csv("csv_data/nlu_data.csv")  # Make sure this path is correct

# Prepare Rasa NLU data
nlu_data = {"version": "3.1", "nlu": []}

# Iterate over each row (each disease)
for index, row in df.iterrows():
    # Create an intent name from the disease column
    intent = row['Disease'].lower().replace(" ", "_")

    examples_list = []

    # Collect all non-empty precautions as examples
    for col in ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']:
        if pd.notna(row[col]):
            examples_list.append(row[col])

    # Add to nlu_data if there are examples
    if examples_list:
        nlu_data['nlu'].append({
            "intent": intent,
            "examples": "\n- " + "\n- ".join(examples_list)
        })

# Write the output to nlu.yml inside the data folder
with open("data/nlu.yml", "w") as f:
    yaml.dump(nlu_data, f, sort_keys=False)

print("nlu.yml has been created successfully!")
