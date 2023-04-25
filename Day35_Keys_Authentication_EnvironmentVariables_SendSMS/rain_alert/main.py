import requests
from twilio.rest import Client
import os

API_KEY = os.environ["OWM_API_KEY"]

weather_params = {
    "LAT": 40.477090,
    "LONG": -88.993220,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

LAT = 40.477090
LONG = -88.993220
exclude = "current,minutely,daily"
# API_KEY = "300d0b26ed671216427476c190b00c1f"

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

OMW_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&exclude={exclude}&appid={API_KEY1}")
# response = requests.get(OMW_endpoint, params=weather_params)
response.raise_for_status()
# print(response.json())

weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an umbrella")
        will_rain = True

if will_rain:
    # print("Bring an Umbrella. ")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="+18334827283",
        to="ENTERNUMBERHERE"
    )
    print(message.status)

# Use PythonAnywhere to Automate the Python Script
