from aiogram.utils import executor
import logging
from config import dp
from handlers import admin, callback, client, extra, fsm_anketa

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)









