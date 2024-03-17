import os
import requests

API_KEY = os.getenv('WEATHER_API_KEY')


def get_data(city, days=None):
    url = \
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"  # 5 day forecast with a 3-hour step
    response = requests.get(url).json()
    filtered_data = response["list"]  # gives 40 items list total
    nr_values = 8 * days  # data is served each 3 hours, so 1 day has 8 data subsets
    filtered_data = filtered_data[:nr_values]
    return filtered_data
