# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(sum(temp_list)/len(temp_list))
#
# print(data['temp'].mean())
# print(data['temp'].max())

# Get data in columns
# print(data['condition'])
# print(data.condition)

# Get data from rows
# print(data[data.day == "Monday"])
# print(data[data['day'] == "Monday"])
#
# print(data[data.temp == data['temp'].max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a df from scratch
data_dict = {
    "students": ["A", "B", "C", "D"],
    "grades": [15, 16, 17, 12]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")



