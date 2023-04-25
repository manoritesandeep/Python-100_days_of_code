## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
import os
import requests
import datetime as dt
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_api_key = "NINRPEJ7SMOC6YSZ"
news_api_key = "5316f961db9a49a8b40ca443ca61e0e3"
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

alpha_endpoint = "https://www.alphavantage.co/query"
# TIME_SERIES_DAILY_ADJUSTED
# TIME_SERIES_INTRADAY
# TIME_SERIES_DAILY
alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alpha_api_key,
}

response = requests.get(alpha_endpoint,
                        params=alpha_params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
print(data)
data_list = [value for (key, value) in data.items()]
print(data_list)

yesterday_data = data_list[0]
yesterday_stock_price = float(yesterday_data["4. close"])
print(yesterday_stock_price)

# Day before yesterday's data
dayb4_yesterday_data = data_list[1]
dayb4_yesterday_stock_price = float(dayb4_yesterday_data["4. close"])
print(dayb4_yesterday_stock_price)

# Price diff and percentage change
price_diff = abs(yesterday_stock_price - dayb4_yesterday_stock_price)
print(price_diff)
percent_change = price_diff / yesterday_stock_price * 100
print(f"Percent change: {round(percent_change, 2)}")

# If percent change is greater than a threshold, get news for the stock
if percent_change > 1:
    print("Get News!!")
    # News API
    # url = "https://newsapi.org/v2/everything?q=keyword&apiKey=5316f961db9a49a8b40ca443ca61e0e3"

    newsapi = NewsApiClient(api_key=news_api_key)
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='Tesla',
                                              sources='bbc-news,the-verge',
                                              language='en')

    # /v2/everything
    all_articles = newsapi.get_everything(q='Tesla',
                                          sources='bbc-news,the-verge',
                                          domains='bbc.co.uk,techcrunch.com',
                                          from_param='2023-03-24',
                                          to=dt.datetime.now().date(),
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()
    print(f"Sources: {sources}")

    # print(top_headlines)
    # print(all_articles["articles"][0]["description"]) #["description"]
    articles = all_articles["articles"][0]["description"]

    # Send msg using twilio
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=articles,
        from_="+18334827283",
        to="ENTERNUMBERHERE"
    )
    print(message.status)
