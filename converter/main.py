import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, enter your summ')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Incorrect value')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width = 2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data = 'USD/EUR')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data = 'EUR/USD')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data = 'USD/GBP')
        btn4 = types.InlineKeyboardButton('Another value', callback_data = 'ELSE')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Select a currency pair', reply_markup = markup)
    else:
        bot.send_message(message.chat.id, 'Incorrect value')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data != 'ELSE':
        values = call.data.split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'In result: {round(res, 2)}. Enter your summ again')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Enter value with /')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'In result: {round(res, 2)}. Enter your summ again')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Incorrect value. Enter currency again.')
        bot.register_next_step_handler(message, my_currency)

bot.polling(none_stop=True)