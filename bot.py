from pyrogram import Client, filters
from pyrogram.types import Message, BotCommand

app = Client("bot", api_id=20234202, api_hash="fc0e099e810cbea903512acef8563b36", bot_token="ТВОЙ_ТОКЕН_СЮДА")

# Команда /start
@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply("🚀 Бот успешно запущен!")

# Команда /status
@app.on_message(filters.command("status"))
async def status_handler(client, message: Message):
    await message.reply("📡 Статус: бот работает.")

# Команда /deploy
@app.on_message(filters.command("deploy"))
async def deploy_handler(client, message: Message):
    await message.reply("🔁 Автопоток запущен.")

# Команда /test
@app.on_message(filters.command("test"))
async def test_handler(client, message: Message):
    await message.reply("📢 Это тестовый сигнал!")

# Команда /metrics
@app.on_message(filters.command("metrics"))
async def metrics_handler(client, message: Message):
    await message.reply("📊 Текущие фильтры: ...")

# Команда /setmetrics
@app.on_message(filters.command("setmetrics"))
async def setmetrics_handler(client, message: Message):
    await message.reply("⚙️ Фильтры успешно обновлены.")

# ✅ Новая команда /help
@app.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    help_text = (
        "🛠 <b>Команды управления ботом</b>:\n\n"
        "/start — Запустить бота\n"
        "/status — Проверить статус\n"
        "/deploy — Запустить автопоток\n"
        "/stop — Остановить автопоток\n"
        "/test — Тестовый сигнал\n"
        "/metrics — Показать текущие фильтры\n"
        "/setmetrics — Установить фильтры\n"
        "/ping — Проверка отклика\n"
        "/version — Показать версию\n"
        "/help — Справка по командам"
    )
    await message.reply(help_text, parse_mode="html")

# Команда /ping (опционально — можешь убрать)
@app.on_message(filters.command("ping"))
async def ping_handler(client, message: Message):
    await message.reply("🏓 Pong!")

# Команда /version (опционально)
@app.on_message(filters.command("version"))
async def version_handler(client, message: Message):
    await message.reply("🤖 Версия бота: 1.0.0")

# Запуск бота
app.run()
