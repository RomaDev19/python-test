import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

TOKEN = '6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA'

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    custom_keyboard = [['top-left', 'top-right'],
                       ['bottom-left', 'bottom-right']]
    markup = types.ReplyKeyboardMarkup(custom_keyboard)
    markup.add(types.KeyboardButton('Open web-site', web_app=WebAppInfo(url='https://spiffy-cupcake-7055a1.netlify.app/')))
    await message.answer('Hello, my friend!', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email {res["email"]}. Phone: {res["phone"]}')


executor.start_polling(dp)