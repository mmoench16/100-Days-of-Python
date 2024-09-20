import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/315a5b9eabed04aec7a5e0d7b417ab17/flightDeals/prices"

class DataManager:
    """The DataManager class is responsible for communicating with Sheety, i.e. to retrieve and/or upload data to Sheety which functions as our 'database'."""
    
    def __init__(self):
        """Initialises the DataManager class."""
        self.sheety_auth_token = { "Authorization": f"Bearer {os.getenv("SHEETY_AUTH_TOKEN")}" }
        self.destination_data = {}

    def get_flight_data(self) -> dict:
        """Retrieves current flight data from Sheety, i.e. it performs a GET request.
        
        Returns:
            dict: A dictionary of the flight data stored on Sheety.
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers= self.sheety_auth_token)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self) -> None:
        """Updates IATA codes for destination and updates flight data to Sheety, i.e. it performs a PUT request."""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers= self.sheety_auth_token)
            response.raise_for_status()
            print(response.text)
        