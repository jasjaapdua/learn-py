# data = []
# with open("./weather_data.csv", 'r') as f:
#     data = f.readlines()

# table = [row.rstrip('\n') for row in data]

# print(table)

# import csv

# with open("weather_data.csv", 'r') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#         print(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
type(data)
print(data["temp"])