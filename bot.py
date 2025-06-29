import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
AXIOM_TOKEN = os.getenv("AXIOM_TOKEN")
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))  # 👈 обязательно числом!

app = Client(
    "viktor_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# ================= Команды =================

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🤖 Бот запущен. Используй /help для списка команд.")

@app.on_message(filters.command("status"))
async def status(client, message):
    await message.reply("✅ Бот работает и готов к действиям.")

@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply(
        "🛠️ Доступные команды:\n"
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

@app.on_message(filters.command("test"))
async def test_signal(client, message):
    await app.send_message(
        chat_id=TARGET_CHAT_ID,
        text="🧪 Тестовый сигнал успешно отправлен.",
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply("🏓 Pong!")

@app.on_message(filters.command("version"))
async def version(client, message):
    await message.reply("🧬 Версия бота: 1.0.0")

# =========== Функция /id (временно, чтобы узнать ID чата) ===========

@app.on_message(filters.command("id"))
async def get_id(client, message):
    await message.reply(f"🆔 chat_id: `{message.chat.id}`")

# =========== Заглушки для deploy/stop/metrics ===========

@app.on_message(filters.command("deploy"))
async def deploy(client, message):
    await message.reply("🚀 Автопоток запущен (эмуляция).")

@app.on_message(filters.command("stop"))
async def stop(client, message):
    await message.reply("⛔ Автопоток остановлен.")

@app.on_message(filters.command("metrics"))
async def metrics(client, message):
    await message.reply("📊 Текущие фильтры: GT Score ≥ 35, Volume ≥ $7K, Migrated ✅")

@app.on_message(filters.command("setmetrics"))
async def set_metrics(client, message):
    await message.reply("⚙️ Новые фильтры установлены (эмуляция).")
