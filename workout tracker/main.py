import requests
from datetime import datetime

my_email ='Insert your Email'
my_username = 'Insert your Username'


# ----------------------------------------------------- NUTRITIONX API ----------------------------------------------------- #
API_KEY = 'Insert your API KEY'
APP_ID = 'Insert your APP ID'
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query = input('Tell me which exercises you did: ')

headers = {
    'x-app-key': API_KEY,
    'x-app-id': APP_ID,

}
exercise_params = {
    'query': query,
    'gender': 'male',
    'weight_kg': 75.3,
    'height_cm': 184.0,
    'age': 22
}
response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
nutritionx_data = response.json()['exercises'][0]

duration = int(nutritionx_data['duration_min'])
calories = int(nutritionx_data['nf_calories'])
exercise = nutritionx_data['name']
date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H:%M:%S')


# --------------------------------------------------- SHEETY API --------------------------------------------------- #
SHEETY_API_KEY = 'Insert your sheety api key'

sheety_endpoint = 'https://api.sheety.co/02e758b0eccfe4348a66b60cef05c453/workoutTracking/workouts'

sheety_headers = {
    'Authorization': SHEETY_API_KEY
}
sheety_params = {
    'workout':{
        'date': date,
        'time': time,
        'exercise': exercise.title(),
        'duration': duration,
        'calories': calories
    }
}
response = requests.post(url=sheety_endpoint, json=sheety_params, headers = sheety_headers)
print(response.text)