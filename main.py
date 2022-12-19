import requests
from config import *


lat = 55.5433
lon = 37.5483
part = 'daily'
api_key = get_openweather_token()
params = {'units': 'metric',
          'lang': 'ru'}
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

req = requests.get(url, params=params)
print(req.json())