import requests
from datetime import datetime
import time
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 55.543781
MY_LONG = -4.664010

iss_latitude = 0.0
iss_longitude = 0.0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def get_iss_position():
    global iss_latitude
    global iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def within_5_degrees():
    within = False
    
    if ((MY_LAT - 5 <= iss_latitude <= MY_LAT + 5)
        and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)):
        within = True
    
    return within

def is_dark():
    is_dark = False

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour <= sunrise or time_now.hour >= sunset:
        is_dark = True

    return is_dark

def send_email():
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("APP_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recipient_email, 
                            msg=f"Subject:ISS Alert\n\nYou should be able to see the ISS now (weather permitting).")

while True:
    get_iss_position()
    if within_5_degrees():
        if is_dark():
            send_email()
    time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.