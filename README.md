# WeatherAPI.com Code Challenge
## Challenge Description
Using the WeatherAPI.com API, retrieve a forecast for the next day for the following cities:
Chisinau, Madrid, Kyiv, and Amsterdam. Requirements

● The app should be written in Java (bonus points if written in Kotlin).

● The code should be tracked with git and pushed to Github or Bitbucket. 

● The data for the next day's forecast should be outputted to STDOUT. 

● The output should be formatted as a table with the dates as columns and the cities as rows. 

● The table should show the following data points for each location:
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
will be very helpful in structuring your application's data models. Bonus Points

- Writing the app in Kotlin. 
- Using Gradle as a package manager.
- Using Retrofit (https://square.github.io/retrofit/) for API interaction.