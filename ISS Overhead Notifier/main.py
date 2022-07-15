import smtplib
from datetime import datetime
import requests
import time

MY_LAT = 28.704060
MY_LONG = 77.102493
MY_EMAIL = "roh**@gmail.com"
MY_PASSWORD = "*************"


def is_iss_overhead():
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LONG - 5 <= iss_lng <= MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        conn = smtplib.SMTP("smtp.gmail.com")
        conn.starttls()
        conn.login(MY_EMAIL, MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )
