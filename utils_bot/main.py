import os
from dotenv import load_dotenv
import telebot
from telebot import types
from utils.qr.generate_qr import create_qr
from utils.shorten_url.shorten_url import shorten_url

load_dotenv('.env')
bot = telebot.TeleBot(os.environ['UTILS_BOT_TOKEN'])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hey!')


def send_qr(message):
    create_qr(message.text)
    img = open('./utils/qr/qr.png', 'rb')
    bot.send_message(message.chat.id,  "Here is your QR code:")
    bot.send_photo(message.chat.id, img)
    img.close()

def link(message):
    lin = shorten_url(message.text)
    bot.send_message(message.chat.id, "Here is you link:\n" + lin)


@bot.message_handler(commands=['qr'])
def qr(message):
    bot.send_message(message.chat.id, 'Send your link')
    bot.register_next_step_handler(message, send_qr)


@bot.message_handler(commands=['shorten_link'])
def shorten_link(message):
    bot.send_message(message.chat.id, 'Send your link')
    print
    bot.register_next_step_handler(message, link)


print("🚀 Bot is running 🚀")
bot.infinity_polling()
print("⛔ Bot stopped ⛔")
