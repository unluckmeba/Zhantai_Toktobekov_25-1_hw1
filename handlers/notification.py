import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer("Ok")


async def go_to_sleep():
    for id in chat_id:
        await bot.send_message(id, "Пора спать!")


async def wake_up():
    video = open('media/video.mp4', 'rb')
    for id in chat_id:
        await bot.send_video(id, video=video, caption="ВСТАВАААЙ ЭРЖАН")


async def scheduler():
    aioschedule.every().day.at('19:26').do(go_to_sleep)
    aioschedule.every().day.at('19:30').do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)
