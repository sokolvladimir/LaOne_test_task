from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from src.db.methods import DB
from src.structure.start_keyboard import start_kb


async def start_program(message: Message, state=FSMContext):
    if state:
        await state.finish()
    if len(message.text.split()) == 2:
        _, poll_id = message.text.split()
        poll = DB.get_poll(poll_id)
        if poll:
            await message.answer_poll(**poll)
        else:
            await message.answer("Опрос не найден")
    elif message.chat.type == "private":

        text = "Привет дорогой наш пользователь!👋\n\n" \
               "Смотри что я могу:\n" \
               "1. Определять погоду в любом городе.\n" \
               "2. Определять курс валют.\n" \
               "3. Отправлять случайную картинку с милым животным.\n" \
               "4. Создавать опросы и отправлять в групповой чат."
        await message.answer(text, reply_markup=start_kb())


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_program, commands=["start", "back"], state="*")
