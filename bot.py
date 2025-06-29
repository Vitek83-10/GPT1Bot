import os
import logging
import requests
from pyrogram import Client, filters

# === Константы и переменные ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHANNEL_ID = int(os.getenv("TARGET_CHAT_ID"))  # <-- ВАЖНО: без кавычек, нужен int
AXIOM_TOKEN = os.getenv("AXIOM_API_KEY")

AXIOM_API_URL = "https://api.axiom.xyz/v1/alerts/search"  # <-- ВАЖНО: правильный URL

# === Настройка логгера ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === Инициализация клиента Pyrogram ===
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === Обработка команды /start ===
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply("✅ Бот работает и подключён!")

# === Основной запуск и запрос в Axiom ===
@app.on_message(filters.command("test") & filters.private)
async def test_handler(client, message):
    logger.info("Команда /test получена, делаем запрос в Axiom...")

    headers = {
        "Authorization": f"Bearer {AXIOM_TOKEN}",
        "Content-Type": "application/json"
    }

    query = {
        "filter": {
            "stream": ["alerts"]
        },
        "limit": 1,
        "order": "desc"
    }

    try:
        response = requests.post(AXIOM_API_URL, headers=headers, json=query)
        if response.status_code == 200:
            data = response.json()
            await message.reply(f"✅ Успешный запрос Axiom:\n{data}")
        else:
            logger.error(f"Ошибка запроса Axiom: {response.status_code}")
            await message.reply(f"❌ Ошибка Axiom: {response.status_code}")
    except Exception as e:
        logger.exception("Ошибка при запросе к Axiom")
        await message.reply(f"❌ Исключение: {e}")

# === Запуск бота ===
if __name__ == "__main__":
    logger.info("Бот запущен и работает...")
    app.run()
