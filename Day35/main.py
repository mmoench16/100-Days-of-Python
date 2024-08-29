import requests
from dotenv import load_dotenv
import os

load_dotenv()

owm_api_key = os.getenv("OWM_API_KEY")
text_belt_api_key = os.getenv("TEXTBELT_API_KEY")
recipient_number = os.getenv("RECIPIENT_NUMBER")

MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": owm_api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella.")
    # Textbelt
    resp = requests.post('https://textbelt.com/text', {
    'phone': recipient_number,
    'message': "It's going to rain today. Remember to bring an ☔️",
    'key': text_belt_api_key,
    })
    resp.raise_for_status()
    print(resp.json())