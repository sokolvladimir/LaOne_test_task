from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMConverter(StatesGroup):
    get_count = State()
    get_currency = State()