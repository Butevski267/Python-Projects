import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = 'Insert your token'
USERNAME = 'Insert your username'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

response = requests.post(url=pixela_endpoint, json = user_params)
#print(response.text)

# --------------------------------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    'id': 'graph1',
    'name': 'Gym Graph',
    'unit': 'minute',
    'type': 'int',
    'color': 'shibafu'
}
headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers = headers)
#print(response.text)
# ------------------------------------------------------------------------------
drawing_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'

today = datetime.now()
#today = datetime(year=2022, month = 1, day=23)


pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many minutes did you workout today?')
}
response = requests.post(url=drawing_endpoint, headers = headers, json = pixel_params)
print(response.text)