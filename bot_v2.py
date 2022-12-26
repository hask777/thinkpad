from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import os
import json
import time
from scrapers.lenovo import get_data

bot = Bot(token='5926369508:AAG-ZkYWOkkWaxzt33JJmttWScfQ45Llohw', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Thinkpad', 'Перчатки', 'Снайперские винтовки']
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(*start_buttons)

    await message.answer('Выберете категорию', reply_markup=keyboard)



@dp.message_handler(Text(equals='Thinkpad'))
async def get_discount_knifes(message: types.Message):
    await message.answer('Please waiting ...')

    get_data()

    with open('thinkpad_gomel.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)

    count = []
    for index, item in enumerate(data):

        if item.get("city") == "Гомель":
            count.append(index)
            card =  f'{item.get("image")}\n'\
                    f'{hlink(item.get("title"), item.get("link"))}\n'\
                    f'{hbold("Город: ")} {item.get("city")}\n'\
                    f'{hbold("Цена: ")} {item.get("price")}\n'\
                    f'{hbold("Характеристики:")} {item.get("params")}\n'\

            if len(count) > 20:
                if index % 20 == 0:
                    time.sleep(3)

            await message.answer(card)



def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()