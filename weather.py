import requests
from config import get_openweather_token
weather_token = get_openweather_token()

class Weather():

        def get_weather_for_now(self):
                self.lat = 55.5433
                self.lon = 37.5483
                params = {'units': 'metric',
                        'lang': 'ru'}
                url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={weather_token}'
                weather_now = requests.get(url, params=params) 
                return weather_now.json()

        def get_weather_info(self):
                weather_info_list = []
                weather_info_list.append(self.get_weather_for_now()['main']['feels_like'])
                weather_info_list.append(self.get_weather_for_now()['main']['temp'])
                weather_info_list.append(self.get_weather_for_now()['wind']['speed'])
                return weather_info_list
                 
        def print_info_on_russian(self):

                print(f'Погодка сейчас такая себе: градусов-то всего: {self.get_weather_info()[1]}, но из-за '
                      f'ебейшего ветра в {self.get_weather_info()[2]} метров в секуду, '
                      f'ощущается на {self.get_weather_info()[0]}')



weather = Weather()
bla = weather.print_info_on_russian()