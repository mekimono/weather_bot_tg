import telebot
import requests
from config import TOKEN, API


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def index(message):
    bot.send_message(message.chat.id, 'Привет я бот погоды, введите ваш город латинской раскладкой')


@bot.message_handler(content_types=['text'])
def send_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='
                       f'{city}&appid={API}&units=metric')

    if res.status_code == 200:
        json_res = res.json()
        weather = json_res['main']['temp']

        bot.reply_to(message, f'Сейчас в этом городе температура {weather} по Цельсию')

    else:
        bot.reply_to(message, 'Неверно введен город')


bot.infinity_polling()
