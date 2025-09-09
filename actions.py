import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideSymptoms(Action):
    def name(self):
        return "action_provide_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: dict):

        disease = tracker.get_slot("disease")
        if not disease:
            dispatcher.utter_message(text="Please tell me the disease name.")
            return []

        with open("data/disease_symptoms.json") as f:
            disease_data = json.load(f)

        symptoms = disease_data.get(disease.lower())
        if symptoms:
            dispatcher.utter_message(text=f"🩺 Symptoms of {disease.capitalize()}: {symptoms}")
        else:
            dispatcher.utter_message(text=f"❌ Sorry, I don't have info about {disease}.")
        return []

class ActionVaccineSchedule(Action):
    def name(self):
        return "action_vaccine_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: dict):

        vaccine = tracker.get_slot("vaccine")
        if not vaccine:
            dispatcher.utter_message(text="Please specify the vaccine.")
            return []

        with open("data/vaccine_schedule.json") as f:
            vaccine_data = json.load(f)

        schedule = vaccine_data.get(vaccine.lower())
        if schedule:
            dispatcher.utter_message(text=f"💉 {vaccine.capitalize()} vaccine schedule: {schedule}")
        else:
            dispatcher.utter_message(text=f"❌ Sorry, I don't have info about {vaccine}.")
        return []
