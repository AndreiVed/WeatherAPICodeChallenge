import json
from datetime import date, timedelta

from tabulate import tabulate

import requests

API_URL = "http://api.weatherapi.com/v1/forecast.json"
API_KEY = "9ca70da4e3254418b49172244252808"
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

def average_wind_der(wind_dir_list: list) -> str|None:
    wind_set = set(wind_dir_list)

    wind_dir_count = {key: wind_dir_list.count(key) for key in wind_set}

    max_count = max(wind_dir_count.values())
    for key, value in wind_dir_count.items():
        if value == max_count:
            return key
    return None

def get_response_data(location: str) -> dict:
    # get response data
    uri = f"{API_URL}?key={API_KEY}&q={location}&dt={DATE}&days=1&aqi=no&alerts=no"
    response_data = requests.get(uri).content.decode('utf-8')
    return json.loads(response_data)

def find_main_data(response: dict) -> tuple:
    # find max and min temperature, humidity, wind speed into forecast day

    res_forecast = response["forecast"]["forecastday"][0]["day"]
    min_temp = res_forecast["mintemp_c"]
    max_temp = res_forecast["maxtemp_c"]
    humidity = res_forecast["avghumidity"]
    wind_speed = res_forecast["maxwind_kph"]
    return min_temp, max_temp, humidity, wind_speed

def find_largest_wind_direction(response: dict) -> str:
    # find the wind direction by the largest direction for the day
    res_hour = response["forecast"]["forecastday"][0]["hour"]
    wind_dir_list = [hour["wind_dir"] for hour in res_hour]
    return average_wind_der(wind_dir_list)

def parse_data(location) -> list:
    response = get_response_data(location)
    min_temp, max_temp, humidity, wind_speed = find_main_data(response)
    wind_dir = find_largest_wind_direction(response)

    # return {
    #     "Minimum Temperature (°C)": min_temp,
    #     "Maximum Temperature (°C)": max_temp,
    #     "Humidity (%)": humidity,
    #     "Wind Speed (kph)": wind_speed,
    #     "Wind Direction": wind_dir,
    # }
    return [location, min_temp, max_temp, humidity, wind_speed, wind_dir]

def print_weather_table(weather_data) -> None:
    print(tabulate(weather_data, headers=HEADER))

def main() -> None:
    # result_dict = {location: parse_data(location) for location in LOCATIONS}
    weather_data = [parse_data(location) for location in LOCATIONS]
    print_weather_table(weather_data)


main()