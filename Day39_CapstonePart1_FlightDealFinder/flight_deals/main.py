from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

flight_search = FlightSearch()

notification_manager = NotificationManager()

ORIGIN_CITY_IATA = 'LON'

# for code in sheet_data[0]
if sheet_data[0]['iataCode'] == "":
    # print("Empty")
    # print(type(sheet_data)) # <class 'list'>
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    # print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow_date = datetime.now() + timedelta(days=1)
print(tomorrow_date)
return_six_month_date = tomorrow_date + timedelta(days=(6*30))
print(return_six_month_date)

for destination in sheet_data:
    # print(destination)
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination['iataCode'],
        from_time=tomorrow_date,
        to_time=return_six_month_date
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
