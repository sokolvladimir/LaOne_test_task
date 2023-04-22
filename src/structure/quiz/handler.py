from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.deep_linking import get_startgroup_link

from src.db.methods import DB
from src.structure.quiz.keyboard import quiz_kb, create_send_to_group_kb


async def poll_menu(call: CallbackQuery):
    await call.message.answer("Создай опрос и отправь его мне\n"
                              "Нажмите /back для возврата в главное меню", reply_markup=quiz_kb)


async def poll_processing(message: Message):
    link = await get_startgroup_link(message.poll.id)
    DB.post_poll(message.poll.id, message.poll)
    msg = await message.answer("Опрос готовиться к отправке в группу...", reply_markup=ReplyKeyboardRemove())
    await message.answer("Опрос готов к отправке в группу\n"
                         f"Нажмите /back для возврата в главное меню",
                         reply_markup=create_send_to_group_kb(link))
    await msg.delete()


def register_handlers_poll(dp):
    dp.register_callback_query_handler(poll_menu, text="poll", state="*")
    dp.register_message_handler(poll_processing, content_types="poll", state="*")
