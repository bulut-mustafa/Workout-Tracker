import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR_WEIGHT(FLOAT)"
HEIGHT_CM = "YOUR HEIGHT(INT)"
AGE = "YOUR AGE(INT)"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]

nutritionix_headers = {
    "x-app-id" : f"{APP_ID}",
    "x-app-key": f"{APP_KEY}",
}

query_text = input("Tell me which exercises you did")
nutritionix_params = {
    "query" : query_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}

nutri_response = requests.post(url=nutritionix_endpoint, headers= nutritionix_headers, json=nutritionix_params)
result = nutri_response.json()





today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=(USERNAME,PASSWORD) )
print(sheety_response.text)


