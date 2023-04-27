import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3e86ff5cf468163f0e79d65eff837b5d/flightDealSearch/prices"
bearer_token = "askdhfkasjdhfkaldsfhkjsahlk"
bearer_header = {
    "Authorization": f"Bearer {bearer_token}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_header)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_header
            )
            print(response.text)
