import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFERS_ENDPOINT="https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    """The FlightSearch class is responsible for retrieving flight information."""

    def __init__(self):
        """Initialises the FlightSearch class.
        
        The constructor performs the following tasks:
        1. Retrieves the API key and secret from the .env file.

        Instance variables: 
        _api_key (str): The API key used to access the Amadeus API, sourced from the .env file.
        _api_secret (str): The API secret used to access the Amadeus API, sourced from the .env file.
        _token (str): The access token used to access the Amadeus API obtained by calling the _get_new_token() method.
        """
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def get_iata_code(self, city_name: str) -> str:
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.
        
        Parameters:
        city_name (str): The name of the city for which to find the IATA code.
        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError, 
        or "Not Found" if no match is found due to a KeyError.
        
        The function sends a GET request to the CITY_SEARCH_ENDPOINT with a query that specifies the city
        name and other parameters to refine the search. It then attempts to extract the IATA code
        from the JSON response. 
        - If the city is not found in the response data (i.e., the data array is empty, leading to 
        an IndexError), it logs a message indicating that no airport code was found for the city and 
        returns "N/A".
        - If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading 
        to a KeyError), it logs a message indicating that no airport code was found for the city 
        and returns "Not Found".
        """

        params = {
            "keyword": city_name,
        }

        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        response = requests.get(url=CITY_SEARCH_ENDPOINT, headers=headers, params=params)

        try:
            iata_code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"No airport code found for {city_name}.")
            return "Not Found"

        return iata_code
    
    def _get_new_token(self) -> None:
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        
        Returns:
            str: The new access token obtained from the API response.
        """
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": f"{self._api_key}",
            "client_secret": f"{self._api_secret}"
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        response.raise_for_status()

        return response.json()["access_token"]
    
    def get_flight_data(self, origin_city_code: str, destination_city_code: str, from_date: str, to_date: str) -> dict | None:
        """
        Retrieves flight data for a specified origin city, destination city, and time range using the Amadeus API.
        """

        header = {
            "Authorization": f"Bearer {self._token}"
        }

        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_date.strftime("%Y-%m-%d"),
            "returnDate": to_date.strftime("%Y-%m-%d"),
            "currencyCode": "GBP",
            "adults": 1,
            "max": 10
        }

        response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, headers=header, params=query)
        response.raise_for_status()

        return response.json()