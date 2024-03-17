import os
import requests

API_KEY = os.getenv('WEATHER_API_KEY')


def get_data(place, days=None, type=None):
    url = \
        f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"  # 5 day forecast with a 3-hour step
    response = requests.get(url).json()
    filtered_data = response["list"]  # gives 40 items list total
    nr_values = 8 * days  # data is served each 3 hours, so 1 day has 8 data subsets
    filtered_data = filtered_data[:nr_values]

    match type:
        case "Temperature":
            filtered_data = [item["main"]["temp"] for item in filtered_data]
        case "Sky":
            filtered_data = [item["weather"][0]["main"] for item in filtered_data]
    return filtered_data


print(get_data(place="Tokyo", days=3, type="Temperature"))
