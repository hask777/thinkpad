from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import get_data
import json
import os
import time

bot = Bot(token='5926369508:AAG-ZkYWOkkWaxzt33JJmttWScfQ45Llohw', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    # start_buttons = ['Ножи', 'Перчатки', 'Снайперские винтовки']
    # keyboard = types.ReplyKeyboardMarkup()
    # keyboard.add(*start_buttons)

    get_data()

    with open('thinkpad_gomel.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("title"), item.get("link"))}\n'\
            f'{hlink(item.get("image"), item.get("link"))}\n'\
            f'{hbold("Название: ")}{item.get("Title")}\n'\
            f'{hbold("Город: ")}${item.get("city")}\n'\
            f'{hbold("Цена: ")}${item.get("price")}\n'\
            f'{hbold("Характеристики:")}{item.get("params")}'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()