from pyrogram import Client, filters
from pyrogram.types import Message

# Твои данные
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "8085881327:AAHw2qT9ai3oTxT6N_0K5nc903u6VJn4Kn8"

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Команда /start
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("🚀 Бот успешно запущен!")

# Команда /status
@app.on_message(filters.command("status"))
async def status_command(client, message: Message):
    await message.reply_text("✅ Бот работает и готов к действиям.")

# Команда /deploy
@app.on_message(filters.command("deploy"))
async def deploy_command(client, message: Message):
    await message.reply_text("📡 Автопоток запущен.")

# Команда /stop
@app.on_message(filters.command("stop"))
async def stop_command(client, message: Message):
    await message.reply_text("⛔️ Автопоток остановлен.")

# Команда /test
@app.on_message(filters.command("test"))
async def test_command(client, message: Message):
    await message.reply_text("🧪 Тестовый сигнал успешно отправлен.")

# Команда /metrics
@app.on_message(filters.command("metrics"))
async def metrics_command(client, message: Message):
    await message.reply_text("📊 Текущие фильтры:\n• GT Score ≥ 35\n• Volume ≥ 80K\n• Liquidity ≥ 30K и т.д.")

# Команда /setmetrics
@app.on_message(filters.command("setmetrics"))
async def setmetrics_command(client, message: Message):
    await message.reply_text("⚙️ Настройка фильтров: отправьте параметры в формате:\n`GT=35, Volume=80K, Liquidity=30K`")

# Команда /ping
@app.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    await message.reply_text("📡 Бот на связи!")

# Команда /version
@app.on_message(filters.command("version"))
async def version_command(client, message: Message):
    await message.reply_text("🧠 Версия бота: v1.0")

# Команда /help
@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply_text(
        "🛠 Доступные команды:\n"
        "/start — Запустить бота\n"
        "/status — Проверить статус\n"
        "/deploy — Запустить автопоток\n"
        "/stop — Остановить автопоток\n"
        "/test — Тестовый сигнал\n"
        "/metrics — Показать фильтры\n"
        "/setmetrics — Установить фильтры\n"
        "/ping — Проверка связи\n"
        "/version — Версия\n"
        "/help — Помощь"
    )

app.run()
