import aiohttp
from pydantic import ValidationError

from src.api.weather.schemas import WeatherSchema
from src.config import WHETHER_API_KEY


class Weather:
    def __init__(self,
                 lang: str = "ru",
                 units: str = "metric"):
        self.base_url = "https://api.openweathermap.org/"
        self.api_key = WHETHER_API_KEY
        self.lang = lang  # Язык
        self.units = units  # Единицы изменения
        self.answer = None

    async def get_weather_by_city(self, city: str):
        """Получение данных о погоде по названию города"""
        url = self._create_url("data/2.5/weather")
        params = {"q": city,
                  "appid": self.api_key,
                  "units": self.units,
                  "lang": self.lang}
        async with aiohttp.ClientSession() as session:
            response = await session.get(url, params=params)
            self._generate_answer(await response.json())

    def _generate_answer(self, weather_dict: dict):
        """Генерация ответа для пользователя"""
        match int(weather_dict.get("cod", 0)):
            case 200:
                try:
                    weather = WeatherSchema(**weather_dict)
                    self.answer = f"Погода в городе {weather.name}:\n" \
                                  f"Температура: \n" \
                                  f"- Сейчас {weather.main.temp}°C\n" \
                                  f"- Ощущается как {weather.main.feels_like}°C\n" \
                                  f"- Минимальная {weather.main.temp_min}°C\n" \
                                  f"- Максимальная {weather.main.temp_max}°C\n" \
                                  f"Влажность: {weather.main.humidity}%\n" \
                                  f"Скорость ветра: {weather.wind.speed} м/с\n" \
                                  f"Описание: {weather.weather[0].description}\n" \
                                  f"Атмосферное давление: {weather.main.pressure} мм.рт.ст.\n" \
                                  f"Видимость: {weather.visibility} м\n" \
                                  f"Время восхода: {weather.sys.sunrise}\n" \
                                  f"Время заката: {weather.sys.sunset}\n" \
                                  f"Координаты: {weather.coord.lon}, {weather.coord.lat}\n" \
                                  f"Облачность: {weather.clouds.all}%\n"
                except ValidationError as e:
                    print(e)  # тут можно логировать ошибку
                    self.answer = "Произошла ошибка, попробуйте позже"
            case 404:
                self.answer = "Город не найден"
            case _:
                print(weather_dict)  # тут можно логировать ошибку
                self.answer = "Произошла ошибка, попробуйте позже"

    def _create_url(self, prefix: str):
        """Метод формирует url запроса"""
        return self.base_url + prefix
