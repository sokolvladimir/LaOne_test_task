import aiohttp

from src.config import CURRENCY_TOKEN


class Currency:
    def __init__(self):
        self.base_url = "https://api.apilayer.com/exchangerates_data/"
        self.token = CURRENCY_TOKEN

    async def get_currency_list(self):
        """Метод возвращает список валют"""
        url = self.base_url + "symbols"
        headers = {
            "apikey": self.token
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    return None

    async def converter(self, from_currency: str, to_currency: str, amount: int):
        """Метод возвращает курс валют"""
        url = self.base_url + "convert"
        headers = {
            "apikey": self.token
        }
        params = {
            "from": from_currency,
            "to": to_currency,
            "amount": amount
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    return None