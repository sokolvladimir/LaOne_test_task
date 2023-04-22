from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMWeather(StatesGroup):
    get_weather = State()