from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

random_image_kb = InlineKeyboardMarkup()
random_image_kb.add(InlineKeyboardButton("Ещё хочу!", callback_data="random_image_next"))