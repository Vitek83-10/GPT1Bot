import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
import subprocess

# 🔐 Данные твоего Telegram-приложения (api_id и api_hash)
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"

# 🤖 Токен твоего бота
BOT_TOKEN = "8085881327:AAHtgjesSjMbyektB5W2YXlSDQAGk_MMPfc"

# 📲 Подключение клиента
app = Client("viktor_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Команда /start
@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply("🤖 Бот запущен. Используй /help для списка команд.")

# ✅ Команда /help
@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply("📋 Команды: /start, /help, /ping, /status, /id")

# ✅ Команда /ping
@app.on_message(filters.command("ping"))
async def ping_command(client: Client, message: Message):
    await message.reply("🏓 Pong!")

# ✅ Команда /status
@app.on_message(filters.command("status"))
async def status_command(client: Client, message: Message):
    await message.reply("✅ Бот работает и готов к действиям.")

# ✅ Команда /id
@app.on_message(filters.command("id"))
async def id_command(client: Client, message: Message):
    await message.reply(f"🆔 chat_id: {message.chat.id}")

# 🚀 Запуск бота
if __name__ == "__main__":
    subprocess.Popen(["python", "Zentest_Token_Rule.py"])
    app.run()
