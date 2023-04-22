from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from src.api.currency_converter.currency_api import Currency
from src.api.currency_converter.methods import get_currency_list, check_currency
from src.structure.converter.keyboard import currency_kb
from src.structure.converter.state import FSMConverter


async def converter_menu(call: CallbackQuery, state=FSMContext):
    await call.message.edit_text("Введите сумму для конвертации.\n"
                                 "Для возврата нажмите /back", reply_markup=currency_kb)
    await FSMConverter.get_count.set()


async def count_currency(message: Message, state=FSMContext):
    if message.text.isdigit():
        await state.update_data(count=int(message.text))
        await message.answer("Введите валюты для конвертации через пробел.\n"
                             "Для возврата нажмите /back", reply_markup=currency_kb)
        await FSMConverter.get_currency.set()
    else:
        await message.answer("Некорректные данные.\n"
                             "Введите сумму для конвертации.\n"
                             "Для возврата нажмите /back", reply_markup=currency_kb)


async def currency_converter(message: Message, state=FSMContext):
    data_currencies = message.text.split()
    if len(data_currencies) == 2 and check_currency(data_currencies):
        msg = await message.answer("Подождите немного мы конвертируем...")
        c = Currency()
        count = (await state.get_data()).get("count")
        data = await c.converter(data_currencies[0].strip(),
                                 data_currencies[1].strip(),
                                 count)
        if data:
            await msg.edit_text(f"{count} {data_currencies[0]} = {round(data['result'], 2)} {data_currencies[1]}")
        else:
            await msg.edit_text("Ошибка конвертации")
        await message.answer("Для возврата нажмите /back\n"
                             "Или введите сумму для конвертации", reply_markup=currency_kb)
        return await FSMConverter.get_count.set()

    return await message.answer("Вы ввели некорректные данные.\n"
                                "Введите валюты для конвертации через пробел.\n"
                                "Пример: 'BYN RUB'\n"
                                "Для возврата нажмите /back", reply_markup=currency_kb)


async def currency_list(call: CallbackQuery, state=FSMContext):
    lst = get_currency_list()
    await call.message.answer(f"Список валют:\n{lst}\n"
                              f"Введите сумму для конвертации.\n"
                              f"Для возврата нажмите /back", reply_markup=currency_kb)
    await FSMConverter.get_count.set()


def register_handlers_converter(dp):
    dp.register_callback_query_handler(converter_menu, text="currency", state="*")
    dp.register_callback_query_handler(currency_list, text="currency_list", state="*")
    dp.register_message_handler(count_currency, state=FSMConverter.get_count)
    dp.register_message_handler(currency_converter, state=FSMConverter.get_currency)
