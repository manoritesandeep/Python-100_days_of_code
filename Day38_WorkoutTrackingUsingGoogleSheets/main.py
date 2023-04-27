import os
import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = "60"
HEIGHT_CM = "175"
AGE = "25"

NUTRITIONIX_API = os.environ["NT_APP_ID"]
APP_ID = os.environ["NT_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/3e86ff5cf468163f0e79d65eff837b5d/myWorkouts/workouts"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITIONIX_API,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint,
                         json=params,
                         headers=headers)
result = response.json()
# print(result)

####### Sheety #######

bearer_header = {
    "Authorization": f"Bearer  {os.environ['TOKEN']}"
}
today = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")
# print(current_time)

# print(result["exercises"])
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=sheety_endpoint,
                                json=sheet_inputs,
                                headers=bearer_header)
print(sheety_response.text)
