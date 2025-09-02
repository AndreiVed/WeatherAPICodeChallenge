# WeatherAPI.com Code Challenge
## Challenge Description
Using the WeatherAPI.com API, retrieve a forecast for the next day for the following cities:
Chisinau, Madrid, Kyiv, and Amsterdam. Requirements

1. The app should be written in Java (bonus points if written in Kotlin).

2. The code should be tracked with git and pushed to Github or Bitbucket. 

3. The data for the next day's forecast should be outputted to STDOUT. 

4. The output should be formatted as a table with the dates as columns and the cities as rows. 

5. The table should show the following data points for each location:
* Minimum Temperature (°C)
* Maximum Temperature (°C)
* Humidity (%)
* Wind Speed (kph)
* Wind Direction

## How to Use the WeatherAPI.com API
To get started with the WeatherAPI.com API, you'll need to follow a few simple steps:
1. Create an Account: Go to the WeatherAPI.com website and sign up for a free plan. The
free plan provides access to real-time, forecast, and historical weather data. 
2. Obtain an API Key: Once you've created an account, you'll find your unique API key on
your account dashboard. This key is a unique identifier that authenticates your requests. You'll need to include this key as a query parameter in every API call you make. 
3. Explore the API Documentation: The best way to understand the API is by using their
interactive documentation, specifically the Swagger tool. This tool allows you to test
different endpoints, see the required parameters, and view example JSON responses. This
will be very helpful in structuring your application's data models.

Bonus Points:

- Writing the app in Kotlin. 
- Using Gradle as a package manager.
- Using Retrofit (https://square.github.io/retrofit/) for API interaction.

## Solution
This project is a Python application that fetches weather forecasts for multiple cities using the WeatherAPI.com 
API and displays the data in a formatted table.

### Structure:
* `main.py` - this file consists main logic of fetching the API data, 
processing it, handling exceptions and printing the formatted table to the console.
* `settings.py` - this file consists constants of the project with the ability 
to modify locations and date of forecast.
* `requirements.txt` - this file lists all the external Python libraries the project depends on, 
such as Requests and Tabulate.
* `.env` - this file is used for managing environment-specific variables, 
most importantly your API key.
* `.env.sample` - this file consists the examples of .env environment-specific variables.
* `Dockerfile` - this file consists the instructions for building a Docker image of the application. 
It specifies the base image, copies the necessary files, 
and defines how the application should be run inside a container.
* `.gitignore` - this file instructs Git on which files and directories 
to ignore and not commit to the repository. 
* `.dockerignore` - this file tells the Docker build process which files 
and directories to ignore, preventing unnecessary files 
(like .env, __pycache__, or editor configuration files) 
from being added to the final image.
* `README.md` - this is the main documentation for the project. 
It provides an overview of the application, describes its features, 
and gives instructions on how to set it up and run it, both locally and with Docker.

### Features:

* **Multi-City Forecast:** Fetches and presents a one-day weather forecast for multiple predefined cities (Chisinau, Madrid, Kyiv, Amsterdam).

* **Detailed Metrics:** Displays key weather data including minimum and maximum temperature, humidity, wind speed, and wind direction.

* **Advanced Wind Direction Logic:** Calculates the most frequent wind direction for the day by analyzing hourly data.

* **Robust Error Handling:** Gracefully handles network issues, HTTP errors, and JSON parsing failures, providing clear error messages.

* **Secure Configuration:** Uses environment variables to securely manage the API key, preventing it from being hardcoded or committed to version control.

* **Containerized Environment:** Provides a Dockerfile for easy and consistent deployment in any environment using Docker.

## Getting Started

To run this application, 
you need to provide a valid API key from WeatherAPI.com.

### 1. Local deployment:
- Create venv: `python -m venv .venv`
- Activate venv: `source .venv/bin/activate`
- Install requirements: `pip install requirements.txt`
- Create a .env file and set your API_KEY from WeatherAPI.com
or use mine:
`API_KEY=9ca70da4e3254418b49172244252808`
- Run `python main.py`

### 2. Using Docker:
- Build the Docker image from the Dockerfile: `docker build -t weather_api .`
- Run the container by passing your API key 
as an environment variable using the -e flag:
`docker run -e "API_KEY=your_weather_api_key" weather_api`
