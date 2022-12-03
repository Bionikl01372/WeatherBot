# import requests
# import datetime
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# from config import tg_bot_token, open_weather_token_tomorrow
#
btnMain = KeyboardButton('Главное меню')

#Menu
weather_today = KeyboardButton('Погода на сегодня')
weather_tommorow = KeyboardButton('Погода на завтра')
weather_on_7_days = KeyboardButton('Погода на 7 дней')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(weather_today, weather_tommorow, weather_on_7_days, btnMain)


# bot = Bot(token=tg_bot_token)
# dp = Dispatcher(bot)
#
# cnt = 2
#
# #Tommorow
# #
#
#     tommorow()