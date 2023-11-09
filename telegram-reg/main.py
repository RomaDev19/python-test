import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from db import Database

TOKEN = '6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

db = Database('database.db')

@dp.message_handler(commands='start')
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш никнейм")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы", reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '👤 Профиль':
            pass
        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                if(len(message.text) > 15):
                    await bot.send_message(message.from_user.id, "Неверный никнейм")
                elif "@" in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Ввели запрещенный символ")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, "Успешная регистрация!", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "???")
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)