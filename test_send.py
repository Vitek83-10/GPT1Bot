import asyncio
from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))  # например: 123456789

# Используем бот-сессию
app = Client("test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def send_test_message():
    await app.start()
    await app.send_message(chat_id=TARGET_CHAT_ID, text="✅ Бот успешно отправил сообщение.")
    await app.stop()

if __name__ == "__main__":
    asyncio.run(send_test_message())
