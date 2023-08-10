import requests

USER = "<<USER>>"
PASS = "<<PASSWORD>>"
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/98b013e70fc6560bb992a4610bca2509/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/98b013e70fc6560bb992a4610bca2509/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=(USER, PASS))
        data = response.json()
        self.destination_data = data["prices"]
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
                auth=(USER, PASS)
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, auth=(USER, PASS))
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
