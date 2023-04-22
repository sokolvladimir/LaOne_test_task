from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

currency_kb = InlineKeyboardMarkup()
currency_kb.add(InlineKeyboardButton(text="Список валют", callback_data="currency_list"))