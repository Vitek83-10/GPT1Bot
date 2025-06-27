from pyrogram import Client, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client(
    "gpt1bot_session",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    bot=True  # ВАЖНО: обязательно для запуска как бот
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🚀 Бот успешно запущен!")

@app.on_message(filters.command("status"))
async def status(client, message):
    await message.reply("✅ Статус: бот работает!")

if __name__ == "__main__":
    print("🚀 Бот запущен")
    app.run()
