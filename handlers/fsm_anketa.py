from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    grypa = State()
    sumbit = State()


 async def
