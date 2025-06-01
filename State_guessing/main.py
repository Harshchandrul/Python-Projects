
# with open("weather_data.csv", 'r') as weather_file:
#     data = weather_file.readlines()
#     print(data) 
    
import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temp = int(row[1])
#             temperatures.append(temp)
    
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()

# temp_list = data['temp'].to_list()
# print(temp_list)
# average_temp = sum(temp_list) / len(temp_list) 
# print(average_temp)

# print(data.temp)
# # print(data['temp'].max())
# # print(data.temp.mean())

# ? Get Data in Row
# print(data[data.day == "Monday"])

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# to get a particular data of cell 
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp[0] * 9/5 + 32)


# # ? How to create Datafram from scratch
# data_dict = {
#     "students" : ['Harsh', 'Naman', 'Ruzul'], 
#     "score" : [75, 64, 80]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

data = pandas.read_csv('squirrel_census.csv')
primary_fur_color_list = data.PrimaryFurColor.to_list()

gray_count = len(data[data.PrimaryFurColor == "Gray"])
cinnamon_count = len(data[data.PrimaryFurColor == "Cinnamon"])
black_count = len(data[data.PrimaryFurColor == "Black"])

# Now creating DataFrame 
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon" , "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv('primary_colors.csv')


def abs():
    print("Hello world")


print('Hello world')
print('Hello world')

# this is the smooth
# this is the smooth typing in vscode
print("Hello w")

