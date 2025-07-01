import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()  # Загружаем переменные из .env

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("TARGET_CHAT_ID")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Zentru тест: бот работает через .env!")
