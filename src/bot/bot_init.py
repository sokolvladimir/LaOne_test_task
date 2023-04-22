import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from src.config import API_TOKEN

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=f"{API_TOKEN}")
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())