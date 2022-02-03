import requests
from datetime import datetime
import smtplib
import time

my_email = 'Insert your email'
password = 'Insert your password'

MY_LAT = 41.088115 # Your latitude
MY_LONG = 21.011504 # Your longitude

def send_email(letter):
    global my_email,password
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject:Look up!\n\n The iss is above in the sky !' )
        #connection.close()

def is_iss_overhead():
    global MY_LAT,MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_latitude <= MY_LONG + 5:
        return True

def is_night():
    global MY_LAT,MY_LONG
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1][1])
    sunset = int(data["results"]["sunset"].split('T')[1][1])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        send_email()



