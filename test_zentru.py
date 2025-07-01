import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN", "вставь_сюда_токен_если_без_env")
CHAT_ID = os.getenv("TEST_CHAT_ID", "вставь_сюда_ID_если_без_env")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Zentru тест: бот работает!")
