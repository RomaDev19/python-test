import telebot
import requests
import json

bot = telebot.TeleBot('6725533419:AAGZsdodkDooWmB-EjYjUZDp5_YUo9RtFcA')
API = '1b3a5e6f4fb2fa8d146691b6053b61d8'

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, nice to meet you! Please write your city or town')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Now weather is: {temp}')

        image = 'sun.png' if temp > 5.0 else 'cloud.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'It`s not correct')

bot.polling(none_stop=True)