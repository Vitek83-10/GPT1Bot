import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🤖 Бот успешно запущен и работает!")

@app.on_message(filters.command("status"))
async def status(client, message):
    await message.reply("✅ Статус: бот активен и слушает команды.")

if __name__ == "__main__":
    print("🚀 Бот запущен")
    app.run()
