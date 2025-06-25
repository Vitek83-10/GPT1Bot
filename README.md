from pyrogram import Client, filters
from pyrogram.types import Message

API_TOKEN = "YOUR_BOT_TOKEN"

app = Client("sol_alert_test_bot", bot_token=API_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("✅ Привет! Бот запущен и работает.")

@app.on_message(filters.command("status"))
async def status(client, message: Message):
    await message.reply("📡 Бот активен. Всё на связи.")

app.run()
