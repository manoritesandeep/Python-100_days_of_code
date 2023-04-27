# import os
#
# token_id = os.environ.get("HOME")
#

# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

# import requests
# from datetime import datetime
#
# FLIGHT_SEARCH_API_KEY = "3WcaEkJCmXkoOOgrAgC8lYLGeYzZdEpF"
# KIWI_AFFILL_ID = "sandeepsolankiflightsearch"
# kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"
#
# today_date = datetime.now().strftime("%d/%m/%Y")
#
# dateFrom = today_date
# dateTo = "31/05/2023"
# fly_from = "MIA"
# fly_to = "LGA"
#
# response = requests.get(
#     url=f"https://api.tequila.kiwi.com/v2/search?fly_from={fly_from}&fly_to={fly_to}&dateFrom={dateFrom}&dateTo={dateTo}",
#
# )
# print(response.raise_for_status())

# Data_Manager file
import requests
from datetime import datetime
from pprint import pprint

bearer_token = "askdhfkasjdhfkaldsfhkjsahlk"
bearer_header = {
    "Authorization": f"Bearer {bearer_token}"
}

sheety_endpoint = "https://api.sheety.co/3e86ff5cf468163f0e79d65eff837b5d/flightDealSearch/prices"

response = requests.get(url=sheety_endpoint, headers=bearer_header)
# pprint(response.json())

sheet_data = response.json()['prices']
print(sheet_data)

for code in sheet_data[0]:
    print(code)

# import requests
# from pprint import pprint
#
# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
# TEQUILA_API_KEY = "3WcaEkJCmXkoOOgrAgC8lYLGeYzZdEpF"

# location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
# headers = {"apikey": TEQUILA_API_KEY}
#
# query = {"term": "london", "location_types": "city"}
# response = requests.get(url=location_endpoint,
#                         headers=headers,
#                         params=query)
# print(response.text)
# sample = response.text
# print(sample)
# pprint(response.json())
# results = response.json()["locations"]
# print(results)
# code = results[0]['code']
# print(code)

# origin_city_code = "LON"
# destination_city_code = "LAX"
# from_time = "26/04/2023"
# to_time = "25/10/2023"
#
# header = {"apikey": TEQUILA_API_KEY}
# search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
# query = {
#     "fly_from": origin_city_code,
#     "fly_to": destination_city_code,
#     "date_from": from_time,
#     "date_to": to_time,
#     "nights_in_dst_from": 7,
#     "nights_in_dst_to": 28,
#     "flight_type": "round",
#     "one_for_city": 1,
#     "max_stopovers": 0,
#     "curr": "USD",
# }
# response = requests.get(url=search_endpoint,
#                         headers=header,
#                         params=query)
# # pprint(response.text)
# results = response.json()["data"][0]
# # print(type(results))    # <class 'dict'>
# pprint(results)
#
# # pprint(results)["route"]
# price = results['price']
# origin_city = results["cityFrom"]
# origin_airport = results["flyFrom"]
# destination_city = results["cityTo"]
# destination_airport = results["flyTo"]
# out_date = results["local_departure"]
# return_date = results["route"][1]["local_departure"]
# # print(enumerate([price, origin_city, origin_airport, destination_city, destination_airport,out_date,return_date]))
# # print(price, origin_city, origin_airport)
# print(out_date, return_date)






