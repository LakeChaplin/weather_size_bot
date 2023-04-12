import random
import time
import logging
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime, timedelta
from config import get_bot_token
import asyncio
from aiogram import executor
from aiogram.dispatcher import FSMContext, storage
from aiogram.dispatcher.filters.state import State, StatesGroup


TOKEN = get_bot_token()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# список дополнительных комментариев
additional_comments = [
    "Мой мини-кук - {} см 🤏",
    "Мой кук меньше, чем у кенгуру - {} см 😂",
    "Мой кук больше, чем у слона - {} см 😱",
    "Мой кук - {} см, мои соболезнования 🙏",
    "Мой кук - {} см, не ношу боксеры 😉",
    "Мой кук - {} см, настоящий мужик 😎",
    "Мой кук - {} см, это же не конкурс, правда? 😬",
    "Мой кук - {} см, но главное - как им пользоваться 😉",
    "Мой кук - {} см, но это не главное в жизни 😌",
    "Мой кук - {} см, но это не отменяет моих других достоинств 😏",
    "Мой кук - {} см, но это не всё, что у меня есть 😉",
    "Мой кук - {} см, это вам не размер, а энергия 💪",
    "Мой кук - {} см, но я могу удовлетворить любую женщину 😘",
    "Мой кук - {} см, но умение его использовать - главное 🔥",
    "Мой кук - {} см, но не забывайте про внутренний мир 😇",
    "Мой кук - {} см, но это только часть меня 😜",
    "Мой кук - {} см, но для меня главное - душевная связь 🤗",
    "Мой кук - {} см, но это не помешало мне стать миллионером 😎",
    "Мой кук - {} см, но это не помешало мне найти настоящую любовь ❤️",
    "Мой кук - {} см, но я думаю, что мы должны любить друг друга не за размеры 😊"
    "Мой кук - {} см, но я люблю его таким, какой он есть ❤️"
    "Мой кук - {} см, но это не главное в жизни 😌"
    "Мой кук - {} см, но для меня главное - душевная связь 🤗"
    "Мой кук - {} см, но это только часть меня 😜"

]



# определение состояния Measuring

class Measuring(State):
    def __init__(self):
        self.last_measurement_time = datetime.min



# генерируем кнопку "Share my cook size"
def get_button():
    button = types.InlineKeyboardButton("Share my cook size", callback_data="measure_cook_size")
    keyboard = types.InlineKeyboardMarkup().add(button)
    return keyboard


# обработчик команды /start
@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Нажми на кнопку 'Share my cook size', чтобы узнать размер своего кука :)",
                        reply_markup=get_button())


# обработчик нажатия на кнопку "Share my cook size"
@dp.callback_query_handler(lambda call: call.data == 'measure_cook_size')
async def measure_cook_size(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    current_time = datetime.now()

    async with state.proxy() as data:
        if 'measurement_state' not in data:
            data['measurement_state'] = Measuring()

        measurement_state = data['measurement_state']

        if measurement_state.last_measurement_time is not None and \
                current_time - measurement_state.last_measurement_time < timedelta(days=1):
            # если прошло меньше суток, сообщаем пользователю, что он уже измерял свой кук недавно
            await bot.answer_callback_query(call.id,
                                            "Вы уже измеряли свой кук недавно! Попробуйте еще раз через 24 часа.")
            return

        # генерируем размер кука от 1 до 30 см
        cook_size = random.randint(1, 30)

        # отправляем пользователю результаты измерения
        additional_comment = random.choice(additional_comments)
        await bot.send_message(chat_id=chat_id,
                               text="Ваш кук - {} см! {}".format(cook_size, additional_comment.format(cook_size)),
                               reply_markup=types.ReplyKeyboardRemove())

        # сохраняем время последнего измерения
        measurement_state.last_measurement_time = current_time
        # записываем состояние в хранилище
        await state.update_data(data)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

