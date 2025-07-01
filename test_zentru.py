import os
from telegram import Bot

# Получаем токен и chat_id из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("TARGET_CHAT_ID")

# Создаём экземпляр бота и отправляем тестовое сообщение
bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Test passed! Бот работает.")
