import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from config import TG_BOT_TOKEN
import weather


TOKEN = TG_BOT_TOKEN

MSG =  'Programm today, {}?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

VOICE = 'AwACAgIAAx0ESFLB0wACoGZjo0DMjwABWVWuxlZX0BwRykTjbz4AAo4sAAIZ0RlJhJ4OFG8xAAH-LAQ'

@dp.message_handler(commands=['start'])
async def start_handller(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.reply(f'Hello {user_full_name}!\n Please use /help, to see commands list.')

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    msg = text(bold('I understand the following commands:'),
    '/voice', '/photo', '/group', '/note', '/file', '/testpre', sep = '\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['mi'])
async def get_weather(message: types.Message):
    await message.reply(f'{weather.weather.print_info_on_russian()}')

@dp.message_handler(commands=['voice'])
async def voice_command_handler(message: types.Message):
    await bot.send_voice(message.from_user.id, VOICE, reply_to_message_id=message.message_id)

    # for i in range(10):
    #     time.sleep(2)

    #     await bot.send_message(user_id, MSG.format(user_name)) 


if __name__ == '__main__':
    executor.start_polling(dp)