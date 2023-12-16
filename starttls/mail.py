import smtplib
from email.message import EmailMessage
import ssl


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

    
