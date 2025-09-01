import os
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "http://api.weatherapi.com/v1/forecast.json"
LOCATIONS = ("Chisinau", "Madrid", "Kyiv", "Amsterdam")
DATE = date.today() + timedelta(days=1)
HEADER = (
    "City",
    "Minimum Temperature (°C)",
    "Maximum Temperature (°C)",
    "Humidity (%)",
    "Wind Speed (kph)",
    "Wind Direction"
)
