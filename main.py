import requests
from config import *
weather_token = get_openweather_token()

def get_weather_for_now():
    lat = 55.5433
    lon = 37.5483
    params = {'units': 'metric',
            'lang': 'ru'}
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}'
    weather_now = requests.get(url, params=params) 
    return weather_now.json()

print(get_weather_for_now())