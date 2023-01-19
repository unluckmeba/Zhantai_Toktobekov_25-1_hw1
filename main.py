from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram import types
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("Дальше", callback_data='button_call1')
    markup.add(button_call1)
    question = 'Какой герой лучше?'
    answers = [
        'Arc',
        'Tinker',
        'Lina',
        'PA',
        'PL',
        'Morf'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_call1')
async def quiz2(call: types.CallbackQuery):
    question = 'Какой язык лучше?'
    answers = [
        'java',
        'python',
        'C#',
        'C++'
        'html'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        open_period=10
    )


@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def eho(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=str(message.text))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
