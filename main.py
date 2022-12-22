import requests
from datetime import datetime
import os

MY_SHEETY_ENDPOINT = (
    "https://api.sheety.co/5ec014ec8902336927c4400de70fa6b6/workoutTracking/workouts"
)

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
exercise_endpoint = (
    "https://trackapi.nutritionix.com/v2/natural/exercise"  # Accepts 'POST'
)

exercise_text = input("Tell me which exercise you did: ")

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY, "Authorization": ""}

params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 80,
    "age": 21,
}


response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer = input("Enter bearer token: ")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    bearer_headers = {"Authorization": f"Bearer {os.environ['TOKEN']}"}
    sheet_response = requests.post(
        MY_SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers
    )

    print(sheet_response.text)
