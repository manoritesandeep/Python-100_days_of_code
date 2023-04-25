import datetime as dt
from datetime import timedelta

# today = dt.datetime.now().date()
# print(today)
# print(today-timedelta(days=1))
#
# # max_date = data["Time Series (Daily)"][0]
# # print(f"max: {max_date}")
#
# # check for weekend!!
# wod = today.weekday()
# print(wod)
# if wod == 6 or wod == 5:
#     print("Its a weekend!")
#
#
# # check for weekend!!!
# wod = today.weekday()
# # print(wod)
# if wod == 6 or wod == 5:
#     print("Its a weekend!")


# def get_prices():
#     # check if today is a weekend
#     if dt.datetime.now().weekday() < 5:
#         # get price difference and etc...
#         today_date = dt.datetime.now().date()
#         yesterday_date = today_date - dt.timedelta(days=1)
#         print(f"Today's date: {today_date}\nYesterday's date: {yesterday_date}")
#         price_today = float(data["Time Series (Daily)"]['2023-04-21']['4. close'])  # [str(today_date)]['2023-04-21']
#         price_yesterday = float(data["Time Series (Daily)"]['2023-04-20']['4. close'])
#         price_diff = price_today - price_yesterday
#         price_diff_percent = round(price_diff / price_today * 100, 2)
#         print(f"Today's price was: {price_today}, Yesterday's price: {price_yesterday} "
#               f"with a difference of {price_diff}, that is {price_diff_percent}%")
#     else:
#         print("Its a weekend!")


"""
from datetime import datetime

maxdate = max((x for x in d.keys()), key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

print(maxdate)
print(d[maxdate])

"""
# Get latest date from dict
# sample = {
#     "2023-04-01": 50.10,
#     "2023-04-02": 109.50,
#     "2023-04-03": 205.05,
# }
#
# maxdate = max(sample)
# print(maxdate)

# date = "2023-04-20"
# datetime = dt.datetime.strptime(date, "%Y-%m-%d")
# str_dt = str(datetime.date())
# print(type(datetime))
# print(str(datetime.date()))
# print(type(str_dt))
# print(str_dt)


print("a" + "b")    #ab


# News API docs


# Installation

# pip install newsapi-python

# Usage

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='5316f961db9a49a8b40ca443ca61e0e3')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

print(top_headlines)


