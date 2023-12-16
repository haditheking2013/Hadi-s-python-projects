import csv
import pandas

hey = pandas.read_csv('weather_data.csv')
all_temp = hey['temp'].to_list()
print(sum(all_temp) / len(all_temp))



monday = (hey[hey.day == 'Monday'])
print(int(monday.temp * 1.8 +32))







