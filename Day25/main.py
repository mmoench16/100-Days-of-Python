# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for idx, row in enumerate(data):
#         if idx != 0:
#             temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
# avg_temp = sum(temp_list) / len(temp_list)

# print(f"Avg: {data["temp"].mean()}")
# print(f"Max: {data["temp"].max()}")

# print(data.condition)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(f"Celsius: {monday.temp[0]} | Fahrenheit: {monday.temp[0] * 9/5 + 32}")

# Create DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
