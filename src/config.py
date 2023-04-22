import os
from dotenv import load_dotenv

load_dotenv()

# Токен телеграм бота
API_TOKEN = os.environ.get("BOT_TOKEN", None)
print(API_TOKEN)

# API key OpenWeatherMap
WHETHER_API_KEY = os.environ.get("OWM_API_KEY", "api_key")
CAT_API_KEY = os.environ.get("CAT_API_KEY", "api_key")
CURRENCY_TOKEN = os.environ.get("CURRENCY_TOKEN", "api_key")
