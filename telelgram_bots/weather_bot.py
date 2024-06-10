import os
from dotenv import load_dotenv
import telebot
import requests
import json

load_dotenv('.env')
bot = telebot.TeleBot(os.environ['TOKEN'])
weather_api = os.environ['WEATHER_API_KEY']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Everything is awesome 🎉')


@bot.message_handler()
def handle_text(message):
    city_name = message.text.strip().lower()
    query = f'https://api.openweathermap.org/data/2.5/weather?q={
        city_name}&appid={weather_api}&units=metric'
    res = requests.get(query)
    if res.status_code == 200:
        data = json.loads(res.text)
        temperature = data['main']['temp']
        if temperature < -10:
            emoji = '☃️'
        elif temperature < 0:
            emoji = '❄️'
        elif temperature < 10:
            emoji = '☁️'
        elif temperature < 20:
            emoji = '☀️'
        elif temperature < 30:
            emoji = '♨️'
        else:
            emoji = '🔥'
        bot.send_message(message.chat.id, f'{emoji} {temperature} °C')
    else:
        bot.send_message(
            message.chat.id, 'Request is not completed. Maybe you sent incorrect city')


print("🚀 Bot is running 🚀")
bot.infinity_polling()
print("⛔ Bot stopped ⛔")
