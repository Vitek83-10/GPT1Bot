from pyrogram import Client, filters
from pyrogram.types import Message
import logging

# Включаем логгирование
logging.basicConfig(level=logging.INFO)

# Конфигурация
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "7537931821:AAFZnLwQbaXZ9QFY0QHx_oWArS0MneB7QkE"

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("🚀 Бот успешно запущен!")

@app.on_message(filters.command("status"))
async def status(client, message: Message):
    await message.reply("✅ Бот работает и готов к действиям.")

@app.on_message(filters.command("deploy"))
async def deploy(client, message: Message):
    await message.reply("📡 Автопоток запущен.")

@app.on_message(filters.command("stop"))
async def stop(client, message: Message):
    await message.reply("⛔️ Автопоток остановлен.")

@app.on_message(filters.command("test"))
async def test(client, message: Message):
    await message.reply("🧪 Тестовый сигнал успешно отправлен.")

@app.on_message(filters.command("metrics"))
async def metrics(client, message: Message):
    await message.reply("📊 Текущие фильтры:\n• GT Score ≥ 35\n• Volume ≥ 80K\n• Liquidity ≥ 30K и т.д.")

@app.on_message(filters.command("setmetrics"))
async def setmetrics(client, message: Message):
    await message.reply("⚙️ Настройка фильтров: отправьте параметры в формате:\nGT=35, Volume=80K, Liquidity=30K")

@app.on_message(filters.command("ping"))
async def ping(client, message: Message):
    await message.reply("📡 Бот на связи!")

@app.on_message(filters.command("version"))
async def version(client, message: Message):
    await message.reply("🧠 Версия бота: v1.0")

@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    help_text = (
        "🛠 Доступные команды:\n"
        "/start – Запустить бота\n"
        "/status – Проверить статус\n"
        "/deploy – Запустить автопоток\n"
        "/stop – Остановить автопоток\n"
        "/test – Тестовый сигнал в канал\n"
        "/metrics – Текущие фильтры\n"
        "/setmetrics – Установить фильтры\n"
        "/ping – Проверка связи\n"
        "/version – Версия бота\n"
        "/help – Список команд"
    )
    await message.reply(help_text)

# Запуск
if __name__ == "__main__":
    app.run()
