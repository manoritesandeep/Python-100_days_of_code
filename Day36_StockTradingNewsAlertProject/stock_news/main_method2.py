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
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_api_key = "NINRPEJ7SMOC6YSZ"

alpha_endpoint = "https://www.alphavantage.co/query"
# TIME_SERIES_DAILY_ADJUSTED
# TIME_SERIES_INTRADAY
# TIME_SERIES_DAILY
alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": alpha_api_key,
}


# 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'


def get_prices():
    ...

def check_weekend():
    if dt.datetime.now().weekday() < 5:
        # print("Its a weekday!")
        return True
    else:
        # print("Its a weekend!")
        return False


response = requests.get(alpha_endpoint, alpha_params)
response.raise_for_status()
data = response.json()
# print(data.keys())
# print(data["Time Series (Daily)"])
price = data["Time Series (Daily)"]
# wod = dt.datetime.now().weekday()
today_date = dt.datetime.now().date()
yesterday_date = today_date - dt.timedelta(days=1)
print(f"Today's date: {today_date}\nYesterday's date: {yesterday_date}")
price_today = float(data["Time Series (Daily)"][today_date]['4. close'])  # [str(today_date)]['2023-04-21']
price_yesterday = float(data["Time Series (Daily)"][yesterday_date]['4. close'])
price_diff = price_today - price_yesterday
price_diff_percent = round(price_diff / price_today * 100, 2)
print(f"Today's price was: {price_today}, Yesterday's price: {price_yesterday} "
      f"with a closing difference of ${round(price_diff, 2)}, that is {price_diff_percent}% "
      f"between {today_date} and {yesterday_date}")

# print(check_weekend())
# print(get_prices())
