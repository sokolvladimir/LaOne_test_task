from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, InlineKeyboardMarkup, \
    InlineKeyboardButton

quiz_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
poll_type = KeyboardButtonPollType(type="regular")
quiz_button = KeyboardButton(text="Создать опрос", request_poll=poll_type)
quiz_kb.add(quiz_button)


def create_send_to_group_kb(url: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Отправить в группу", url=url))
    return kb