import time
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from emoji import emojize
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
ISRO = 'AgACAgIAAxkDAAPPY6M8Oa9n9apccZaCJoinp7D6UDQAAn7DMRvwtRhJxKO2fldLAAHtAQADAgADdwADLAQ'
VIDEO = 'BAACAgIAAx0ESFLB0wACoGtjo0DOMtquJOOL3SZmeLHK-M3oVQACkSwAAhnRGUkvsLCT5aS_UCwE'
SPACE_AGENCY = [
    'AgACAgIAAxkDAAPRY6M8OnT5mIaurj7O5l85YKJMJ2cAAn_DMRvwtRhJK3Mdzspd5RkBAAMCAANtAAMsBA',
    'AgACAgIAAxkDAAPSY6M8PBopJdYHk7lS-7bHNadAT-gAAoDDMRvwtRhJCXhzF0cEGoIBAAMCAAN3AAMsBA',
    'AgACAgIAAx0ESFLB0wACoGVjo0DMBKxQZdqvw0c94ctGj3wX9AACfMMxG_C1GEkse3l7Q7v8hQEAAwIAA3gAAywE',
    'AgACAgIAAx0ESFLB0wACoGdjo0DMpl1g3x5iCpiuFXSb_H3MygACfcMxG_C1GElGXjR7QIplQgEAAwIAA3kAAywE',
    'AgACAgIAAx0ESFLB0wACoGhjo0DNS2NUGhM42MlIQ_jMWge-NQACfsMxG_C1GEnEo7Z-V0sAAe0BAAMCAAN3AAMsBA',
    'AgACAgIAAx0ESFLB0wACoGpjo0DOOcesoXnMghynhRcUsRb5BgACf8MxG_C1GEkrcx3Oyl3lGQEAAwIAA20AAywE',

]
VIDEO_NOTE = 'BAACAgIAAxkDAAPQY6M8OuDR8rkvxNh1ikw2NimQfgUAAvQnAALwtRhJC2rrlkKpkRYsBA'


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

@dp.message_handler(commands=['photo'])
async def photo_command_handler(message: types.Message):
    caption = "let's go to the moon! :rocket: :last_quarter_moon:"
    await bot.send_photo(message.from_user.id, ISRO,
    caption=emojize(caption),
    reply_to_message_id=message.message_id)

@dp.message_handler(commands=['group'])
async def group_command_handler(message: types.Message):
    media = [InputMediaVideo(VIDEO, 'City Traffic')]
    for photo_id in SPACE_AGENCY:
        media.append(InputMediaPhoto(photo_id))
    await bot.send_media_group(message.from_user.id, media)

@dp.message_handler(commands=['note'])
async def note_command_handler(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(3)
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE)
    
    
    # for i in range(10):
    #     time.sleep(2)

    #     await bot.send_message(user_id, MSG.format(user_name)) 


if __name__ == '__main__':
    executor.start_polling(dp)