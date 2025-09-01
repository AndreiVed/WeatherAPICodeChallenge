import json

from tabulate import tabulate

import requests

from settings import API_KEY, DATE, API_URL, HEADER, LOCATIONS


def average_wind_dir(wind_dir_list: list) -> str:
    """
        get common wind direction
    """
    if not wind_dir_list:
        return "N/A"
    wind_set = set(wind_dir_list)
    wind_dir_count = {key: wind_dir_list.count(key) for key in wind_set}
    max_count = max(wind_dir_count.values())
    for key, value in wind_dir_count.items():
        if value == max_count:
            return key
    return "N/A"


def get_response_data(location: str) -> dict:
    """
        get response data
    """
    if not API_KEY:
        raise ValueError(
            "API key not found. Please set the API_KEY environment variable."
        )
    params = {
        "key": API_KEY,
        "q": location,
        "dt": DATE,
        "days": 1,
        "aqi": "no",
        "alerts": "no",
    }
    try:
        response_data = requests.get(
            API_URL, params=params, timeout=10
        )
        response_data.raise_for_status()
        decoded_data = response_data.content.decode()
        return json.loads(decoded_data)
    except requests.exceptions.HTTPError as http_e:
        print(f"HTTP error occurred: {http_e} for location {location}")
    except requests.exceptions.RequestException as req_e:
        print(f"An error occurred while fetching data: {req_e} "
              f"for location {location}")
    except requests.exceptions.JSONDecodeError as json_e:
        print(f"JSON decoding error: {json_e} "
              f"from response for location {location}")
    return {}


def find_main_data(response: dict) -> tuple:
    """
        find max and min temperature, humidity, wind speed into forecast day
    """
    try:
        res_forecast = response["forecast"]["forecastday"][0]["day"]
    except (KeyError, ValueError) as e:
        print(f"Error parsing forecast data: Missing key {e}")
        return "N/A", "N/A", "N/A", "N/A"
    try:
        min_temp = res_forecast["mintemp_c"]
    except (KeyError, ValueError) as e:
        print(f"Error parsing forecast data: Missing key {e}")
        min_temp = "N/A"
    try:
        max_temp = res_forecast["maxtemp_c"]
    except (KeyError, ValueError) as e:
        print(f"Error parsing forecast data: Missing key {e}")
        max_temp = "N/A"
    try:
        humidity = res_forecast["avghumidity"]
    except (KeyError, ValueError) as e:
        print(f"Error parsing forecast data: Missing key {e}")
        humidity = "N/A"
    try:
        wind_speed = res_forecast["maxwind_kph"]
    except (KeyError, ValueError) as e:
        print(f"Error parsing forecast data: Missing key {e}")
        wind_speed = "N/A"
    return min_temp, max_temp, humidity, wind_speed


def find_largest_wind_direction(response: dict) -> str:
    """
        find the wind direction by the largest direction for the day
    """
    try:
        res_hour = response["forecast"]["forecastday"][0]["hour"]
        wind_dir_list = [hour["wind_dir"] for hour in res_hour]
    except (KeyError, ValueError) as e:
        print(f"Error parsing forecast data: Missing key {e}")
        wind_dir_list = []
    return average_wind_dir(wind_dir_list)


def parse_data(location) -> list:
    """
        get response data by location and parse response data to list of data
    """
    response = get_response_data(location)

    if not response:
        return [location, "N/A", "N/A", "N/A", "N/A", "N/A"]

    min_temp, max_temp, humidity, wind_speed = find_main_data(response)
    wind_dir = find_largest_wind_direction(response)

    return [location, min_temp, max_temp, humidity, wind_speed, wind_dir]


def print_weather_table(weather_data) -> None:
    """
        prints weather table to console via tabulate library
    """
    print(f"\nWeather Forecast for {DATE.strftime('%Y-%m-%d')}:")
    print(tabulate(weather_data, headers=HEADER))


def main() -> None:
    weather_data = [parse_data(location) for location in LOCATIONS]
    print_weather_table(weather_data)


if __name__ == "__main__":
    main()
