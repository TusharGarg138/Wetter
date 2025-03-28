from venv import create

import requests
from twilio.rest import Client

#OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"

api_key = "add your api key"  # Set this in your environment variables
account_sid = "add your account sid code"  # Set this in your environment variables
auth_token = "add auth token "  # Set this in your environment variables

city = "Pune" # city name of you want to know the weather
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

#use when we are calling it with specific latitude and longitude
parameters = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"  # Optional: Fetch temperature in Celsius
}

response = requests.get(url)
data = response.json()
print(data)

will_rain = False

weather_id = data["weather"][0]["id"]
if weather_id < 700:
    will_rain = True

# Twilio SMS settings
from_number = "+1978633xxxx"  # Twilio-verified phone number
to_number = "+917717xxxxxx"  # Recipient's number (Add country code)

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# Send SMS based on weather condition
if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Don't forget to bring an umbrella ☔!",
        from_=from_number,
        to=to_number
    )
else:
    message = client.messages.create(
        body="It's a sunny day! Enjoy the sunshine ☀️!",
        from_=from_number,
        to=to_number
    )

print(f"Message sent with status: {message.status}")

