import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    """The FlightSearch class is responsible for retrieving flight information."""

    def __init__(self):
        """Initialises the FlightSearch class."""

    def get_iata_code(self, city_name: str) -> str:
        """Retrieves the IATA code of a given city.
        
        Args:
            city_name (str): Name of the city as a string.

        Returns:
            str: The IATA code of the given city name.
        """
        return "TESTING"