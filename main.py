import requests

APP_ID = "fce44c68"
API_KEY = "55c0083beb6531a8628f2e920a0eee7b"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY,
}

params = {
    "query":exercise_text,
    "gender":"male",
    "weight_kg":80,
    "age": 21,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise" # Accepts 'POST'

response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)