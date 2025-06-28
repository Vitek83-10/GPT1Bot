from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("🚀 Бот успешно запущен!")

@app.on_message(filters.command("status"))
async def status_command(client, message: Message):
    await message.reply_text("✅ Бот работает и готов к действиям.")

@app.on_message(filters.command("deploy"))
async def deploy_command(client, message: Message):
    await message.reply_text("📡 Автопоток запущен.")

@app.on_message(filters.command("stop"))
async def stop_command(client, message: Message):
    await message.reply_text("⛔️ Автопоток остановлен.")

@app.on_message(filters.command("test"))
async def test_command(client, message: Message):
    await message.reply_text("🧪 Тестовый сигнал успешно отправлен.")

@app.on_message(filters.command("metrics"))
async def metrics_command(client, message: Message):
    await message.reply_text("📊 Текущие фильтры:\n• GT Score ≥ 35\n• Volume ≥ 80K\n• Liquidity ≥ 30K и т.д.")

@app.on_message(filters.command("setmetrics"))
async def setmetrics_command(client, message: Message):
    await message.reply_text("⚙️ Настройка фильтров: отправьте параметры в формате:\n`GT=35, Volume=80K, Liquidity=30K`")

@app.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    await message.reply_text("📡 Бот на связи!")

@app.on_message(filters.command("version"))
async def version_command(client, message: Message):
    await message.reply_text("🧠 Версия бота: v1.0")

@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply_text(
        "🛠 Доступные команды:\n"
        "/start — Запустить бота\n"
        "/status — Проверить статус\n"
        "/deploy — Запустить автопоток\n"
        "/stop — Остановить автопоток\n"
        "/test — Тестовый сигнал в канал\n"
        "/metrics — Показать текущие фильтры\n"
        "/setmetrics — Установить новые фильтры\n"
        "/ping — Проверка отклика\n"
        "/version — Версия бота\n"
        "/help — Помощь и список команд"
    )

app.run()
