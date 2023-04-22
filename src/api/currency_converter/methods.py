import json


def get_currency_list() -> str:
    """Метод возвращает список валют"""
    with open("src/api/currency_converter/symbols.json") as file:
        f = json.load(file)
    text = ""
    for k, v in f.items():
        text += f"{k} - {v}\n"
    return text


def check_currency(currency: list[str]) -> bool:
    """Метод проверяет валюту"""
    with open("src/api/currency_converter/symbols.json") as file:
        f = json.load(file)
    if f.get(currency[0].upper()) and f.get(currency[1].upper()):
        return True
    else:
        return False
