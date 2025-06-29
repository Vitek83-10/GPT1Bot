import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
import subprocess

# 🔐 Токен твоего бота
BOT_TOKEN = "8085881327:AAHtgjesSjMbyektB5W2YXlSDQAGk_MMPfc"

# 📲 Создание клиента
app = Client("viktor_session", bot_token=BOT_TOKEN)

# ✅ Команда /start
@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply("🤖 Бот запущен. Используй /help для списка команд.")

# ✅ Команда /help
@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply("📋 Доступные команды:\n/start — запуск\n/help — список команд\n/ping — тест\n/status — статус\n/id — показать chat_id")

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
    # ⏱ Параллельный запуск Zentest_Token_Rule.py
    subprocess.Popen(["python", "Zentest_Token_Rule.py"])
    app.run()
