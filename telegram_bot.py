import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import get_bot_token
import weather


TOKEN = get_bot_token()

MSG =  'Programm today, {}?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handller(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.reply(f'Hello! {user_full_name}')

@dp.message_handler(commands=['mi'])
async def get_weather(message: types.Message):
    await message.reply(f'{weather.weather.print_info_on_russian()}')

    # for i in range(10):
    #     time.sleep(2)

    #     await bot.send_message(user_id, MSG.format(user_name)) 


if __name__ == '__main__':
    executor.start_polling(dp)