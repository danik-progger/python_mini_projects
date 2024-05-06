from aiogram import executor, Bot, Dispatcher, types
import os
from dotenv import load_dotenv

load_dotenv('.env')
bot = Bot(os.environ['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await message.answer('Hey 👋')

print("🚀 Bot is running 🚀")
executor.start_polling(dp)
print("⛔ Bot stopped ⛔")
