from sre_constants import SUCCESS
import requests
from datetime import datetime
import math

import smtplib
from email.message import EmailMessage
import ssl


def send_it(TO ='haditheking2013@gmail.com'):
        my_email = 'hadigames2022@gmail.com'
        password = 'lqehvpmvxjvkzquf'


        em = EmailMessage()
        em['From'] = my_email
        em['To'] = f'{TO}'
        em['Subject'] = 'HURRY UP AND LOOK UP'
        em.set_content('LOOK UP!!! THE ISS IS ABOVE YOU')

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',context=context) as smtp:
            smtp.login(user=my_email,password=password)
            smtp.sendmail(my_email,f'{TO}',em.as_string())
def check_iss():
    MY_LAT = 51.507351 # Your latitude
    MY_LONG = -0.127758 # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    print(iss_latitude)
    print(iss_longitude)

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    

    time_now = str(datetime.now())
    hour_now = int(time_now.split(' ')[1].split(':')[0])
    
  
    iss_tuple = (iss_latitude,iss_longitude)
    my_location_tuple = (MY_LAT,MY_LONG)
    if math.dist(iss_tuple,my_location_tuple) <=5 and (hour_now >= 18 or hour_now <= 5):
        send_it()
        print('email sent')
    else:
        print('does not match')

  
  
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
check_iss()


