from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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
        correct_option_id=0,
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
        correct_option_id=1,
        open_period=10
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
