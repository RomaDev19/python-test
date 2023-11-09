from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA')
dp = Dispatcher(bot)

@dp.message_handler()
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    await message.answer('Hello')


executor.start_polling(dp)