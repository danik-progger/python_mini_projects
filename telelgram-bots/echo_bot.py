import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv('.env')
bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Visit site')
    btn2 = types.KeyboardButton('Edit')
    btn3 = types.KeyboardButton('Delete')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Hey!', reply_markup=markup)
    bot.register_next_step_handler(message.chat.id, on_click)


def on_click(message):
    if message.text == 'Visit site':
        bot.send_message(message.chat.id, 'Site is open')

@bot.message_handler()
def reply(message):
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "Hello")
    elif message.text.lower() == "echo":
        bot.reply_to(message, message.text)
    else:
        bot.reply_to(message, "I don't know this command")


@bot.message_handler(content_types=['photo'])
def photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Visit site', url="https://youtube.com")
    btn2 = types.InlineKeyboardButton('Edit', callback_data='edit')
    btn3 = types.InlineKeyboardButton('Delete', callback_data='delete')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'edit':
        bot.edit_message_text(
            'New text', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'delete':
        bot.delete_message(callback.message.chat.id,
                           callback.message.message_id - 1)


print("🚀 Bot is running 🚀")
bot.infinity_polling()
print("⛔ Bot stopped ⛔")
