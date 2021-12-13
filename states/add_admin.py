from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp


class Admin(StatesGroup):
    name = State()
    passw = State()


