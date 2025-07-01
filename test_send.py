import asyncio
from pyrogram import Client
import os

API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "8085881327:AAHtgjesSjMbyektB5W2YX1SDQAGk_MMPfc"
TARGET_CHAT_ID = 1047298304  # ← твой настоящий Chat ID

# Используем бот-сессию
app = Client("test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def send_test_message():
    await app.start()
    await app.send_message(chat_id=TARGET_CHAT_ID, text="✅ Тестовое сообщение отправлено!")
    await app.stop()

if __name__ == "__main__":
    asyncio.run(send_test_message())
