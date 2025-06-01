import smtplib
import requests
import datetime as dt


MY_LAT = 28.632429
MY_LNG = 77.218788

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # It returns http error if it occurs.
data = response.json()
iss_position = (float(data['iss_position']['latitude']), float(data['iss_position']['longitude']))
print(iss_position)

# Check if my position is within +5 or -5 degrees of the iss position
iss_overhead = False
if MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5 and MY_LNG - 5 <= iss_position[1] <= MY_LNG + 5:
    iss_overhead = True

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = str(data['results']['sunrise']).split('T')[1].split(':')[0]
sunset = str(data['results']['sunset']).split('T')[1].split(':')[0]
print(sunrise)
print(sunset)

now = dt.datetime.now()
time_now = now.hour
print(time_now)

if iss_overhead and time_now == sunrise:
    # send the email to myself which i can obviously do.
    pass
