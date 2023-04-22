import requests
from datetime import datetime

MY_LAT = 41.878113
MY_LONG = -87.629799

# ISS
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code)
# response.raise_for_status()
#
# data = response.json()
# # print(data)
#
# longitude = data['iss_position']["longitude"]
# latitude = data['iss_position']["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# Sunrise - Sunset times
my_params = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=my_params)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"Sunrise hour: {sunrise} and Sunset hour: {sunset}")

time_now = datetime.now()
print(f"Hour time at time now: {time_now.hour}")
