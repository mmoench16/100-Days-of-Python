import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NUTRIONIX_APP_ID")
API_KEY = os.getenv("NUTRIONIX_API_KEY")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
WEIGHT = float(os.getenv("WEIGHT"))
HEIGHT = float(os.getenv("HEIGHT"))
DOB = datetime.strptime(os.getenv("DOB"), "%Y-%m-%d")
today = datetime.today()

age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

# Step 1 create endpoint variable, request header & parameters
nat_lng_ex_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nat_lng_ex_header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
nat_lng_ex_params = {
    "query": input("Tell me what exercise you did: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": age
}
# Step 2 create actual post request
response = requests.post(url=nat_lng_ex_endpoint, headers=nat_lng_ex_header, json=nat_lng_ex_params)
response.raise_for_status()
# Step 3 print response
workout_data = response.json()["exercises"]

# Step 4: Create Sheety GET & POST endpoints
sheety_get_endpoint = "https://api.sheety.co/315a5b9eabed04aec7a5e0d7b417ab17/workoutTracking/workouts"
sheety_post_endpoint = "https://api.sheety.co/315a5b9eabed04aec7a5e0d7b417ab17/workoutTracking/workouts"

# response = requests.get(sheety_get_endpoint)
# response.raise_for_status()
# print(response.json())

# Step 5: Make a post request to Sheety
workout_details = {
    "workout": {
        'date': today.strftime("%d/%m/%Y"), 
        'time': today.strftime("%H:%M:%S"), 
        'exercise': workout_data[0]["name"].title(), 
        'duration': workout_data[0]["duration_min"], 
        'calories': workout_data[0]["nf_calories"]
    }
}

auth_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}

response = requests.post(url=sheety_post_endpoint, json=workout_details, headers=auth_header)
response.raise_for_status()