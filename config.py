
def get_bot_token():
    with open('D:/Projects/Telegram/Tokens/weather_size_token.txt','r') as token:
        bot_token = token.read()
    return bot_token

def get_openweather_token():
    with open('D:/Projects/Telegram/Tokens/openweathermap-token.txt', 'r') as token:
        weather_token = token.read()
    return weather_token