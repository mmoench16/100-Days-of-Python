class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date) -> None:
        """
        Initialises a FlightData object with the given parameters.

        Parameters:
        price (int): The price of the flight in GBP.
        origin_airport (str): The IATA code of the origin airport.
        destination_airport (str): The IATA code of the destination airport.
        out_date (str): The date of the outgoing flight in the format "YYYY-MM-DD".
        return_date (str): The date of the return flight in the format "YYYY-MM-DD".

        Returns:
        None
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data):
    # Handle empty data if no flight or Amadeus rate limit exceeded
    """
    Finds the cheapest flight from a given JSON response from the Amadeus API.

    Parameters:
    data (dict): The JSON response from the Amadeus API.

    Returns:
    FlightData: A FlightData object with the cheapest flight details.

    Notes:
    If the data is empty (i.e., no flight or Amadeus rate limit exceeded), it returns a FlightData object with "N/A" for all fields.
    """
    if data is None or not data["data"]:
        print("No flight data.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    

    # Data from the first flight in the JSON
    flight = data["data"][0]
    lowest_price = flight["price"]["grandTotal"]
    out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_airport = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]

    cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date)

    for flight in data["data"]:
        if flight["price"]["grandTotal"] < lowest_price:
            lowest_price = flight["price"]["grandTotal"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_airport = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
            cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date)

    return cheapest_flight
