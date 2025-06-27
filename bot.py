from pyrogram import Client, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("ViktorSignalBot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🤖 Бот успешно запущен!")

@app.on_message(filters.command("status"))
async def status(client, message):
    await message.reply("✅ Статус: бот работает!")

if __name__ == "__main__":
    print("🚀 Бот запущен")
    app.run()
