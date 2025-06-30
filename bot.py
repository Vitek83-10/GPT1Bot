import asyncio
import os
import logging
import aiohttp
from pyrogram import Client

# Получение переменных из Render
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")
AXIOM_API_KEY = os.getenv("AXIOM_API_KEY")

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация Pyrogram-клиента
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Новый рабочий URL
AXIOM_URL = "https://api.axiom.trade/v1/tokens/pulse"

# Получение данных из Axiom
async def fetch_axiom_data():
    headers = {
        "Authorization": f"Bearer {AXIOM_API_KEY}",
        "accept": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(AXIOM_URL, headers=headers) as response:
            if response.status != 200:
                logger.error(f"❌ Ошибка при запросе Axiom API: {response.status}")
                return None
            return await response.json()

# Проверка токенов
async def check_axiom_tokens():
    logger.info("🟢 Axiom проверка запущена")
    print("🟢 Axiom проверка запущена")  # Будет видно в Render логах

    data = await fetch_axiom_data()
    if not data:
        return

    tokens = data.get("tokens", [])
    logger.info(f"🔍 Найдено токенов: {len(tokens)}")

    for token in tokens:
        name = token.get("name", "Unknown")
        mc = token.get("marketCap", 0)
        liq = token.get("liquidity", 0)
        vol = token.get("volume", 0)

        # Пример фильтрации
        if mc >= 90000 and liq >= 30000 and vol >= 80000:
            msg = (
                f"✅ Новый токен:\n"
                f"Name: {name}\n"
                f"MC: ${mc:,}\n"
                f"Liquidity: ${liq:,}\n"
                f"Volume: ${vol:,}"
            )
            await app.send_message(chat_id=int(TARGET_CHAT_ID), text=msg)
            logger.info(f"📤 Отправлено сообщение по токену: {name}")

# Ответ на команду /status
@app.on_message()
async def handler(_, message):
    if message.text == "/status":
        await message.reply("🤖 Бот активен и подключён.")

# Основной цикл
async def main():
    await app.start()
    while True:
        try:
            await check_axiom_tokens()
        except Exception as e:
            logger.error(f"❌ Ошибка в check_axiom_tokens: {e}")
        await asyncio.sleep(60)

# Запуск
if __name__ == "__main__":
    asyncio.run(main())
