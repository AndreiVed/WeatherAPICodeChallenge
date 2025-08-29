import json

import requests

API_URL = "http://api.weatherapi.com/v1/forecast.json"
API_KEY = "9ca70da4e3254418b49172244252808"
LOCATIONS = ("Chisinau", "Madrid", "Kyiv", "Amsterdam")

"""
result = {
    "Kyiv": {"min_temp": 0, "max_temp": 0, "humidity": 0, "wind_speed": 0, "wind_dir": ""}
}
"""
result = {}

for loc in LOCATIONS:
    uri = f"{API_URL}?key={API_KEY}&q={loc}&days=1&aqi=no&alerts=no"
    print(uri)
    response_data = requests.get(uri).content.decode('utf-8')
    response = json.loads(response_data)
    print(loc)
    res_current = response["current"]
    res_forecast = response["forecast"]["forecastday"][0]["day"]
    # print(res_current["wind_kph"])
    # print(res_current["wind_dir"])
    # print(res_current["humidity"])
    # print(res_forecast["maxtemp_c"])
    # print(res_forecast["mintemp_c"])

    min_temp = res_forecast["mintemp_c"]
    max_temp = res_forecast["maxtemp_c"]
    humidity = res_current["humidity"]
    wind_speed = res_current["wind_kph"]
    wind_dir = res_current["wind_dir"]
    result[loc] = {
        "Minimum Temperature (°C)": min_temp,
        "Maximum Temperature (°C)": max_temp,
        "Humidity (%)": humidity,
        "Wind Speed (kph)": wind_speed,
        "Wind Direction": wind_dir,
    }

print(result)
