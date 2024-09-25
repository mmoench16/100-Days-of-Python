#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
import time

HOME_AIRPORT = "LHR"

departure_date = datetime.today() + timedelta(days=1)
return_date = departure_date + timedelta(days=6*30)

flight_search = FlightSearch()
notification_manager = NotificationManager()
data_manager = DataManager()

sheet_data = data_manager.get_flight_data()

# print(sheet_data)

if sheet_data[0]['iataCode'] == '':
        for row in sheet_data:
            row['iataCode'] = flight_search.get_iata_code(row['city'])
            time.sleep(2)
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

for city in sheet_data:
    print(f"Getting flights for {city['city']}...")
    flight_info = flight_search.get_flight_data(HOME_AIRPORT, city['iataCode'], departure_date, return_date)
    cheapest_flight = find_cheapest_flight(flight_info)
    print(f"{city['city']}: £{cheapest_flight.price}")
    time.sleep(2)

    # print(f"Type cheapest_flight.price: {type(cheapest_flight.price)}\nType city['lowestPrice']: {type(city['lowestPrice'])}")

    if cheapest_flight.price != "N/A" and float(cheapest_flight.price) < city['lowestPrice']:
        notification_manager.send_whatsapp_message(f"Low price alert! Only £{cheapest_flight.price} to fly from {HOME_AIRPORT} to {city['city']}, on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")