import requests
from twilio.rest import Client 

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = 'AUR50VSSAX5NP6YO'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
end_param = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK,
    'apikey' : api_key
}


end_data = requests.get(STOCK_ENDPOINT, params=end_param)
end_data.raise_for_status()
data = end_data.json()
yesterday = list(data["Time Series (Daily)"].keys())[1]
before_yesterday = list(data["Time Series (Daily)"].keys())[2]

yesterday_closing_price = float(data["Time Series (Daily)"][yesterday]['4. close'])
before_yesterday_closing_price = float(data["Time Series (Daily)"][before_yesterday]['4. close'])

price_increased = yesterday_closing_price-before_yesterday_closing_price

price_diffrence = abs(yesterday_closing_price-before_yesterday_closing_price)

precentage_diffrence = int(price_diffrence / before_yesterday_closing_price * 100)

before_yesetrday_5precent = before_yesterday_closing_price*0.05

if price_diffrence > before_yesetrday_5precent:
    data = requests.get('https://gnews.io/api/v4/search?q=TSLA&token=8f2c4493f78db11e3cd62d0892141e20&lang=en')
    new_data = data.json()
    title = 'Headline: '+str(new_data['articles'][0]['title'])
    body = 'Content: '+str(new_data['articles'][0]['content'])
    if price_increased > 0:
        headline = 'TSLA ↑'+str(precentage_diffrence)+'%'
    else:
        headline='TSLA ↓'+str(precentage_diffrence)+'%'
    


    account_sid = 'ACca49a86384f7462d65302462cc148692'
    auth_token = 'a736a8e4bb71a62a419e641be88db8f0'
    client = Client(account_sid, auth_token)

    message = client.messages \
      .create(
                     body= headline+'\n'+title+'\n'+body,
                     from_='+12058329544',
                     to='+447561556057'
                )

    print(message.status)



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

