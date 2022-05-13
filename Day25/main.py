# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


import pandas


# data = pandas.read_csv("weather_data.csv")


# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())


# avg = sum(temp_list) / len(temp_list)
# print(int(avg))


# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
