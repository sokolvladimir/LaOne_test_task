from aiogram import executor

from src.bot.bot_init import dp
from src.structure.converter.handler import register_handlers_converter
from src.structure.quiz.handler import register_handlers_poll
from src.structure.random_picture.handler import register_handlers_random_picture
from src.structure.start_handler import register_handlers_start
from src.structure.weather.handler import register_handlers_weather

register_handlers_start(dp)
register_handlers_weather(dp)
register_handlers_random_picture(dp)
register_handlers_poll(dp)
register_handlers_converter(dp)

executor.start_polling(dp, skip_updates=True)
