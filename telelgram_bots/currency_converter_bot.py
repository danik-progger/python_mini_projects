import os
from dotenv import load_dotenv
import telebot
from telebot import types
from currency_converter import CurrencyConverter

load_dotenv('.env')
bot = telebot.TeleBot(os.environ['TOKEN'])
curr_converter = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello 👋')
    bot.send_message(message.chat.id, "What's the sum you want to convert?")
    bot.register_next_step_handler(message, get_amount)


def get_amount(message):
    msg = message.text.strip()
    if msg.isdigit() and int(msg) > 0:
        global amount
        amount = int(msg)

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Other', callback_data='other')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            message.chat.id, 'Choose currency pair', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Wrong format. Try again')
        bot.register_next_step_handler(message, get_amount)


@bot.callback_query_handler(func=lambda callback: True)
def call(callback):
    if callback.data == 'other':
        bot.send_message(
            callback.message.chat.id, 'Type your pair in format .../... where and your sum will be converted from first currency to second')
        bot.register_next_step_handler(callback.message, convert)

    else:
        try:
            currencies = callback.data.upper().split('/')
            res = curr_converter.convert(amount, currencies[0], currencies[1])
            bot.send_message(callback.message.chat.id, round(res, 2))
        except ValueError:
            bot.send_message(callback.message.chat.id,
                             'Wrong format. Try again')
            bot.register_next_step_handler(callback, call)


def convert(message):
    currencies = message.text.upper().split('/')
    res = curr_converter.convert(amount, currencies[0], currencies[1])
    bot.send_message(message.chat.id, round(res, 2))


print("🚀 Bot is running 🚀")
bot.infinity_polling()
print("⛔ Bot stopped ⛔")
