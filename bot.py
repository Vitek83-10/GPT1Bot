from pyrogram import Client, filters
from pyrogram.types import Message

# Замените на свои значения
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "7537931821:AAFZnLwQbaX2cKElaPXtyZX1HbypU6elwpE"

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Команда /start
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("🚀 Бот успешно запущен!")

# Команда /status
@app.on_message(filters.command("status"))
async def status_command(client, message: Message):
    await message.reply_text("📊 Бот работает корректно.")

# Команда /deploy
@app.on_message(filters.command("deploy"))
async def deploy_command(client, message: Message):
    await message.reply_text("🔁 Автопоток запущен!")

# Команда /stop
@app.on_message(filters.command("stop"))
async def stop_command(client, message: Message):
    await message.reply_text("⛔️ Автопоток остановлен.")

# Команда /test
@app.on_message(filters.command("test"))
async def test_command(client, message: Message):
    await message.reply_text("📡 Тестовый сигнал отправлен.")

# Команда /metrics
@app.on_message(filters.command("metrics"))
async def metrics_command(client, message: Message):
    await message.reply_text("📊 Текущие фильтры:\n• GT Score ≥ 35\n• Volume ≥ $80K\n...")

# Команда /setmetrics
@app.on_message(filters.command("setmetrics"))
async def setmetrics_command(client, message: Message):
    await message.reply_text("⚙️ Настройка фильтров: отправьте JSON с новыми метриками.")

# Команда /ping
@app.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    await message.reply_text("🏓 Бот в сети!")

# Команда /version
@app.on_message(filters.command("version"))
async def version_command(client, message: Message):
    await message.reply_text("🤖 Версия бота: 1.0.0")

# Команда /help
@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply_text(
        "📘 *Список команд:*\n\n"
        "• /start — Запустить бота\n"
        "• /status — Проверить статус\n"
        "• /deploy — Запустить автопоток\n"
        "• /stop — Остановить автопоток\n"
        "• /test — Отправить тестовый сигнал\n"
        "• /metrics — Показать текущие фильтры\n"
        "• /setmetrics — Установить новые фильтры\n"
        "• /ping — Проверка отклика\n"
        "• /version — Показать версию бота\n"
        "• /help — Помощь и список команд\n",
        parse_mode="Markdown"
    )

# Запуск бота
app.run()
