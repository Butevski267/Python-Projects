import requests
SHEETY_API_KEY = 'Your sheety api key'
sheety_endpoint = 'https://api.sheety.co/02e758b0eccfe4348a66b60cef05c453/flightDeals/prices'
headers= {
    'Authorization': SHEETY_API_KEY,
}

class DataManager:
    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        # ----------------------- Sheety flight deals ----------------------------#
        self.response = requests.get(url=sheety_endpoint, headers=headers)
        self.destination_data = self.response.json()['prices']

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            parameters = {
                'price':{
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json = parameters, headers=headers)
