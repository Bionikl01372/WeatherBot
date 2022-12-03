import requests
import datetime
import markups as nav
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# from markups import tomorrow

#подключение к боту через токен
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

#Функция на команду старт
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(f"Привет,{message.from_user.first_name}! Напиши мне название города и я пришлю сводку погоды!", reply_markup=nav.mainMenu)

#Функция погоды на сегодня
@dp.message_handler()
async def get_message(message: types.Message):
    #Смайлы для погоды
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
#отправка запроса погоды и запись в переменную data в формате json
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

#Берёт информацию из переменной data.с ключом и переменной к ключу
        city = data["name"]
        cur_weather = data["main"]["temp"]
        temp_feels = data["main"]["feels_like"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

#Вывод погоды
        await message.reply(f"\U0000231A {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} \U0000231A\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}° {wd}\n"
              f"Ощущается как: {temp_feels}°\n"
              f"Влажность:"f"{humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца:{sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
              f"Продолжительность дня:{length_of_the_day}\n"  
              f"Хорошего дня,{message.from_user.first_name }! \U0001F609"
              )
#проверка
    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")

#Запуск функции
if __name__ == '__main__':
    executor.start_polling(dp)