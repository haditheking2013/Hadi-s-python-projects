import smtplib
my_email = 'hadigames2022@gmail.com'
password = 'Games2022'


with smtplib.SMTP('smtp.gmail.com') as server:
    server.starttls()
    server.login(my_email,password)
