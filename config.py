
def get_bot_token():
    with open('D:/Projects/Telegram/Tokens/weather_size_token.txt','r') as token:
        bot_token = token.read()
    return bot_token

def get_openweather_token():
    with open('D:/Projects/Telegram/Tokens/openweathermap-token.txt', 'r') as token:
        weather_token = token.read()
    return weather_token

def get_borov_id():
    with open('D:/Projects/Telegram/Tokens/borovy_group_id.txt', 'r') as id:
        group_id = id.read()
    return group_id

def get_login_pikabu():
    with open('D:/Projects/Telegram/Tokens/pikabu_login_pass.txt') as auth:
        login = auth.readlines()
    return login[0].rstrip('\n')

def get_pass_pikabu():
    with open('D:/Projects/Telegram/Tokens/pikabu_login_pass.txt') as auth:
        password = auth.readlines()
    return password[1]

TG_BOT_TOKEN = get_bot_token()
OPENWEATHER_TOKEN = get_openweather_token()
DB_FILENAME = 'botuploads.db'
MY_ID = get_borov_id()
PIKABU_LOGIN = get_login_pikabu()
PIKABU_PASS = get_pass_pikabu()