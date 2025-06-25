from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_TOKEN = os.getenv("API_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_USERNAME = os.getenv("BOT_USERNAME")

app = Client(
    "GPT1Bot",
    bot_token=API_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text("✅ Бот запущен и работает!")

app.run()