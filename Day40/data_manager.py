import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self.sheety_auth_token = { "Authorization": f"Bearer {os.getenv("SHEETY_AUTH_TOKEN")}" }
        self.SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.SHEETY_PRICES_ENDPOINT, headers= self.sheety_auth_token)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers= self.sheety_auth_token
            )
            print(response.text)

    def get_customer_emails(self):
        """
        Uses the Sheety API to GET all the user email addresses from the "users" sheet
        and stores the result in the DataManager's user_data attribute.

        Returns:
        dict: A dictionary of user data with the keys of the dictionary as the user's email
        address and the values as dictionaries containing the user's first name and last name.
        """
        repsonse = requests.get(url=self.SHEETY_USERS_ENDPOINT, headers= self.sheety_auth_token)
        data = repsonse.json()
        self.user_data = data["users"]
        return self.user_data

