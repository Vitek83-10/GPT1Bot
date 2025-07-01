import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

# 🔧 Настройки окружения
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 🎯 ID чата для отправки сигналов
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))

# 🪛 Настройка логгирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 🤖 Инициализация бота
app = Client("signal_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Команда /start
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply("👋 Бот активен и готов к приёму сигналов.")

# ✅ Команда /status
@app.on_message(filters.command("status") & filters.private)
async def status_handler(client: Client, message: Message):
    await message.reply("📡 Статус: бот запущен, ожидание сигналов...")

# ✅ Команда /test — имитация сигнала
@app.on_message(filters.command("test") & filters.private)
async def test_handler(client: Client, message: Message):
    sample = """✅ <b>Тестовый сигнал</b>
<b>ExampleToken (EXT)</b>
🕒 2025-06-30 18:45:00
🔗 <code>0xExampleAddress123</code>

📊 <b>Метрики:</b>
• 💰 MCap: $123456
• 💧 Liquidity: $34567
• 📈 Volume (5m): $45678
• 🧠 GT Score: 72
• 👥 Holders: 840
• 🏦 Top10: 14.2%
• 🕵️ Insiders: 0%
• 🧨 Snipers: 3
• 📦 Bundled: 9.3%

📡 <i>Сигнал прошёл фильтрацию по метрикам.</i>"""
    await message.reply("🧪 Тест-сигнал отправлен в канал.")
    await app.send_message(chat_id=TARGET_CHAT_ID, text=sample, parse_mode="HTML")

# 🔁 Запуск бота
app.run()
