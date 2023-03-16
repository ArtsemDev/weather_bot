from aiogram import Bot, Dispatcher

from utils.settings import SETTINGS
from utils.weather import OpenWeatherMapAPI


bot = Bot(token=SETTINGS.BOT_TOKEN, parse_mode='Markdown')
dp = Dispatcher()
weather = OpenWeatherMapAPI(token=SETTINGS.WEATHER_API_KEY)
