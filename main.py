from aiogram.utils import executor
import logging
from config import dp
from handlers import admin, callback, client, extra, fsm_anketa, notification
from  Database.bot_db import sql_create


async def on_startup(_):
    sql_create()

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
notification.register_handler_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)








