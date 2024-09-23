#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
import json

HOME_AIRPORT = "LHR"

departure_date = datetime.today() + timedelta(days=1)
return_date = departure_date + timedelta(days=6*30)

flight_search = FlightSearch()

data_manager = DataManager()

# sheet_data = data_manager.get_flight_data()

# if sheet_data[0]['iataCode'] == '':
#         for row in sheet_data:
#             row['iataCode'] = flight_search.get_iata_code(row['city'])
#         print(f"sheet_data:\n {sheet_data}")

#         data_manager.destination_data = sheet_data
#         data_manager.update_destination_codes()



with open('flight_data.txt', 'w') as f:
    f.write(json.dumps(flight_search.get_flight_data("LHR", "HND", departure_date, return_date)))