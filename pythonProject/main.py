from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Купить курс', 'Покупка курса Ромы Пирса', 'invoice', config.PAYMENT_TOKEN, 'USD', [types.LabeledPrice('Покупка курса Ромы Пирса', 5 * 100)])




executor.start_polling(dp)