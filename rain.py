from venv import create

import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "47a77221d4c2b213900e79d11bc3165e"  # Set this in your environment variables
account_sid = "AC4c9844d365d2c8ea7c4f3b8c9b6a8377"  # Set this in your environment variables
auth_token = "8c930b01ebad401074fe8cba8ad1a406"  # Set this in your environment variables

city = "Pune" # city name of you want to know the weather
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

