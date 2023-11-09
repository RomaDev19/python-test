import random

import telebot
from telebot import types
TOKEN = '6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('❇ Random number')
    btn2 = types.KeyboardButton('💲 Exchange rates')
    btn3 = types.KeyboardButton('🛈 Info')
    btn4 = types.KeyboardButton('… Other')

    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, 'Hello, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '❇ Random number':
            bot.send_message(message.chat.id, 'Your number ' + str(random.randint(0, 1000)))

        elif message.text == '💲 Exchange rates':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('$ Dollar exchange rate')
            btn2 = types.KeyboardButton('€ Euro exchange rate')
            btn_back = types.KeyboardButton('◅ Back')

            markup.add(btn1, btn2, btn_back)

            bot.send_message(message.chat.id, '💲 Exchange rates', reply_markup=markup)

        elif message.text == '🛈 Info':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('🤖 About this bot')
            btn2 = types.KeyboardButton('📦 Random box')
            btn_back = types.KeyboardButton('◅ Back')

            markup.add(btn1, btn2, btn_back)

            bot.send_message(message.chat.id, '🛈 Info', reply_markup=markup)

        elif message.text == '… Other':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('⚙ Settings')
            btn2 = types.KeyboardButton('🪧 Subscribe')
            btn3 = types.KeyboardButton('🧸 Sticker')
            btn_back = types.KeyboardButton('◅ Back')

            markup.add(btn1, btn2, btn3, btn_back)

            bot.send_message(message.chat.id, '… Other', reply_markup=markup)

        elif message.text == '◅ Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('❇ Random number')
            btn2 = types.KeyboardButton('💲 Exchange rates')
            btn3 = types.KeyboardButton('🛈 Info')
            btn4 = types.KeyboardButton('… Other')

            markup.add(btn1, btn2, btn3, btn4)

            bot.send_message(message.chat.id, '◅ Back', reply_markup=markup)

bot.polling(none_stop=True)