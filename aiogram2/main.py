import aiogram
from aiogram import Bot, Dispatcher, executor, types


bot = Bot('6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    await message.reply('Hello')

    # file = open('./sime.png', 'rb')
    # await message.answer_photo(file)


@dp.message_handler(commands=['start'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site', url='https://google.com'))
    markup.add(types.KeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

executor.start_polling(dp)