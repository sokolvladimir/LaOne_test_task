from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from src.api.weather.weather_api import Weather
from src.structure.states import FSMWeather


async def weather_menu(call: CallbackQuery, state=FSMContext):
    text = "Введите название города чтобы узнать погоду.\n" \
           "Для возврата в основное меню нажмите /back"
    await call.message.answer(text)
    await FSMWeather.get_weather.set()


async def get_weather(message: Message, state=FSMContext):
    weather = Weather()
    await weather.get_weather_by_city(message.text)  # получаем погоду по городу
    weather_info = weather.answer  # получаем ответ
    weather_info += "\n\nДля возврата в основное меню нажмите /back"
    await message.answer(weather_info)


def register_handlers_weather(dp: Dispatcher):
    dp.register_callback_query_handler(weather_menu, text="weather", state="*")
    dp.register_message_handler(get_weather, state=FSMWeather.get_weather)
