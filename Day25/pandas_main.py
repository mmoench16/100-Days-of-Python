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

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg_temp = sum(temp_list) / len(temp_list)

# print(f"Avg: {data["temp"].mean()}")
# print(f"Max: {data["temp"].max()}")

# print(data.condition)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(f"Celsius: {monday.temp[0]} | Fahrenheit: {monday.temp[0] * 9/5 + 32}")

# Create DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240715.csv")
# fur_colors = list(data["Primary Fur Color"].unique())
# del fur_colors[0]

# counts = []
# for colour in fur_colors:
#     fur_colour = data[data["Primary Fur Color"] == colour]
#     counts.append(fur_colour.shape[0])

# squirrel_dict = {
#     "Fur Color": fur_colors,
#     "Count": counts
# }

# squirrel_counts = pandas.DataFrame(squirrel_dict)
# squirrel_counts.to_csv("squirrel_count.csv")
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {name:random.randint(0,100) for name in names}

# passed_students = {name:score for (name, score) in students_scores.items() if score >= 60}
# print(passed_students)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)

