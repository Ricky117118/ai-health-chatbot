import pandas as pd
import yaml

# Load your CSV
df = pd.read_csv("csv_data/nlu_data.csv")

# ---- Generate NLU data ----
nlu_data = {"version": "3.1", "nlu": []}
stories_data = {"version": "3.1", "stories": []}
responses = {}

for _, row in df.iterrows():
    disease = row["Disease"].strip().lower().replace(" ", "_")  # e.g. malaria → malaria
    intent_name = f"ask_precaution_{disease}"
    response_name = f"utter_precaution_{disease}"

    # Add sample training phrases for each disease
    examples = [
        f"What are the precautions for {row['Disease']}?",
        f"How can I prevent {row['Disease']}?",
        f"{row['Disease']} prevention tips",
    ]

    nlu_data["nlu"].append({
        "intent": intent_name,
        "examples": "\n- " + "\n- ".join(examples)
    })

    # Add response
    precautions = [str(row[c]) for c in ["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"] if pd.notna(row[c])]
    responses[response_name] = [{"text": "\n".join(f"{i+1}. {p}" for i, p in enumerate(precautions))}]

    # Add story
    stories_data["stories"].append({
        "story": f"{row['Disease']} precaution path",
        "steps": [
            {"intent": intent_name},
            {"action": response_name}
        ]
    })

# ---- Write files ----
with open("data/nlu.yml", "w") as f:
    yaml.dump(nlu_data, f, sort_keys=False, allow_unicode=True)

with open("domain.yml", "w") as f:
    yaml.dump({"version": "3.1", "responses": responses}, f, sort_keys=False, allow_unicode=True)

with open("data/stories.yml", "w") as f:
    yaml.dump(stories_data, f, sort_keys=False, allow_unicode=True)

print("✅ NLU, domain, and stories files generated!")
