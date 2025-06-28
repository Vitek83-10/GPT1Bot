from pyrogram import Client, filters
from pyrogram.types import Message

import os

# Получаем токен и API данные из переменных окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# Инициализируем клиент
app = Client(
    "gpt1bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Команда /start
@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply("🚀 Бот успешно запущен!")

# Команда /status
@app.on_message(filters.command("status"))
async def status_handler(client, message: Message):
    await message.reply("✅ Бот работает и готов к действиям.")

# Команда /help
@app.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    help_text = (
        "🤖 *Доступные команды:*\n\n"
        "/start — Запустить бота\n"
        "/status — Проверить статус\n"
        "/help — Справка по командам\n"
        "/metrics — Показать текущие метрики\n"
        "/setmetrics — Изменить метрики фильтра\n"
        "/deploy — Перезапуск фильтрации\n"
    )
    await message.reply(help_text, parse_mode="Markdown")

# Заглушки для будущих команд
@app.on_message(filters.command("metrics"))
async def metrics_handler(client, message: Message):
    await message.reply("📊 Метрики фильтра пока не настроены.")

@app.on_message(filters.command("setmetrics"))
async def setmetrics_handler(client, message: Message):
    await message.reply("⚙️ Изменение метрик фильтрации пока не реализовано.")

@app.on_message(filters.command("deploy"))
async def deploy_handler(client, message: Message):
    await message.reply("♻️ Перезапуск фильтрации активирован (заглушка).")

# Запуск бота
app.run()
