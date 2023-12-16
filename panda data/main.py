import pandas


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel = (data[data['Primary Fur Color'] == 'Gray'])
black_squirrel = (data[data['Primary Fur Color'] == 'Black'])
cinnamon_squirrel = (data[data['Primary Fur Color'] == 'Cinnamon'])


dictionary = {'Primary Fur Color': ['Gray','Black','Cinnamon'],
             'sum': [len(gray_squirrel),len(black_squirrel),len(cinnamon_squirrel)]}


df = pandas.DataFrame(dictionary)
df.to_csv('squirrel_sum.csv')