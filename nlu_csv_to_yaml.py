import pandas as pd
import yaml

# Load CSV from csv_data folder
df = pd.read_csv("csv_data/nlu_data.csv")

# Prepare Rasa NLU data
nlu_data = {"version": "3.1", "nlu": []}

for intent in df['intent'].unique():
    examples = df[df['intent'] == intent]['text'].tolist()
    nlu_data['nlu'].append({
        "intent": intent,
        "examples": "\n- " + "\n- ".join(examples)
    })

# Write to nlu.yml
with open("data/nlu.yml", "w") as f:
    yaml.dump(nlu_data, f, sort_keys=False)
