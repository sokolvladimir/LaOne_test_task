from aiogram.types import CallbackQuery

from src.api.random_picture.random_image import CatAPI
from src.structure.random_picture.keyboard import random_image_kb


async def get_random_picture(call: CallbackQuery):
    """Отправляет случайную картинку"""
    image = CatAPI()
    url_image = await image.get_image()
    if url_image is None:
        await call.message.answer("Ошибка сервера при получении картинки\n"
                                  "Для вызова основного меню нажмите /back")
    else:
        await call.message.answer_photo(url_image, caption="Случайная картинка с милым животным \n"
                                                           "Для возврата в основное меню нажмите /back",
                                        reply_markup=random_image_kb)


def register_handlers_random_picture(dp):
    dp.register_callback_query_handler(get_random_picture, text=["random_image", "random_image_next"], state="*")