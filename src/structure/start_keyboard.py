from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb() -> InlineKeyboardMarkup:
    """Метод возвращает стартовую клавиатуру"""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Погода 🌦️", callback_data="weather"))
    keyboard.add(InlineKeyboardButton(text="Курс валют 💵", callback_data="currency"))
    keyboard.add(InlineKeyboardButton(text="Случайная картинка 🐷", callback_data="random_image"))
    keyboard.add(InlineKeyboardButton(text="Опросник 👨‍👩‍👦", callback_data="poll"))
    return keyboard
