import os
from dotenv import load_dotenv
import telebot
from telebot import types
import sqlite3

load_dotenv('.env')
bot = telebot.TeleBot(os.environ['TOKEN'])

name = ''
password = ''




def execute_sql(path, command):
    db = sqlite3.connect(path)
    print(f'✅ Connected to {path}')
    cursor = db.cursor()
    cursor.execute(command)
    print(f'✅ Executed: {command}')
    db.commit()
    cursor.close()
    db.close()
    print(f'✖️ Connection to {path} closed')



def db_fetch(path, data, db_name):
    db = sqlite3.connect(path)
    print(f'✅ Connected to {path}')
    cursor = db.cursor()
    cursor.execute(f'SELECT {data} FROM {db_name}')
    print(f'✅ Executed: SELECT {data} FROM {db_name}')
    users = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    print(f'✖️ Connection to {path} closed')

    return users


@bot.message_handler(commands=['start'])
def start(message):
    execute_sql('bot_db.sql', 'CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')

    bot.send_message(
        message.chat.id, 'Привет, для регистрации в боте введи свое имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(
        message.chat.id, 'А теперь введите пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    global password
    password = message.text.strip()
    bot.send_message(
        message.chat.id, f'Проверьте ваши данные \n Имя: {name} \n Пароль: {password}')

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Все верно')
    btn2 = types.KeyboardButton('Изменить данные')
    markup.row(btn1)
    markup.row(btn2)

    bot.send_message(
        message.chat.id, f'Для продолжения нажмите на одну из кнопок', reply_markup=markup)
    bot.register_next_step_handler(message, finish_form)


def finish_form(message):
    if message.text == 'Все верно':
        execute_sql(
            'bot_db.sql', f'INSERT INTO users (name, pass) VALUES ("{name}", "{password}")')
        bot.send_message(
            message.chat.id, 'Регистрация успешна')
    elif message.text == 'Изменить данные':
        bot.send_message(
            message.chat.id, 'Повторная регистрация')
        bot.send_message(
            message.chat.id, 'Привет, для регистрации в боте введи свое имя')
        bot.register_next_step_handler(message, user_name)
    else:
        bot.send_message(message.chat.id, 'Регистрация не удалась')


@bot.message_handler(commands=['all_users'])
def start(message):
    users = db_fetch('bot_db.sql', '*', 'users')
    list_of_users = ''
    for el in users:
        list_of_users += el[1] + ' '  + el[2] + '\n'
    bot.send_message(
        message.chat.id, 'Список всех пользователей:\n' + list_of_users)


@bot.message_handler()
def reply(message):
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "Hello")
    elif message.text.lower() == "echo":
        bot.reply_to(message, message.text)
    else:
        bot.reply_to(message, "I don't know this command")


print("🚀 Bot is running 🚀")
bot.infinity_polling()
print("⛔ Bot stopped ⛔")
