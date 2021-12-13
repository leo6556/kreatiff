from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp


class Client(StatesGroup):
    name = State()
    master = State()


