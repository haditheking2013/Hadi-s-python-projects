##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




import smtplib
from email.message import EmailMessage
import ssl
from xml.etree.ElementTree import tostring
import pandas
import random
import datetime


def send_it(TO,lettermail):
        my_email = 'hadigames2022@gmail.com'
        password = 'lqehvpmvxjvkzquf'


        em = EmailMessage()
        em['From'] = my_email
        em['To'] = f'{TO}'
        em['Subject'] = 'Happy Birthday'
        em.set_content(f'{lettermail}')

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',context=context) as smtp:
            smtp.login(user=my_email,password=password)
            smtp.sendmail(my_email,f'{TO}',em.as_string())

random_letter = ['letter_1.txt','letter_2.txt','letter_3.txt']
date_today = datetime.datetime.now()
date_tuple = (date_today.month,date_today.day)
print(date_tuple)
data = pandas.read_csv('birthdays.csv')
the_data = (data[data.month == date_tuple[0]][data.day==date_tuple[1]] )
for index,row in the_data.iterrows():
    with open(f'letter_templates/{random.choice(random_letter)}') as letter:
        data_letter = letter.read().replace('[NAME]',row['name'])
        send_it(row['email'],data_letter)

    
    






    