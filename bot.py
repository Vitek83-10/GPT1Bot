import os
import asyncio
import requests
from pyrogram import Client, filters

# Чтение переменных окружения
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))
AXIOM_API_KEY = os.getenv("AXIOM_API_KEY")

app = Client("gpt1bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("✅ Бот работает и готов к бою!")

@app.on_message(filters.command("status"))
async def status_handler(client, message):
    await message.reply("📡 Статус: бот в онлайне, Axiom API подключен.")

# Пример работы с Axiom API
async def fetch_axiom_data():
    url = "https://api.axiom.xyz/v1/tokens/recent"
    headers = {
        "Authorization": f"Bearer {AXIOM_API_KEY}"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        print(data)  # пока выводим просто в консоль
    except Exception as e:
        print("Ошибка при получении данных из Axiom:", e)

# Фоновая задача
async def background_worker():
    while True:
        await fetch_axiom_data()
        await asyncio.sleep(60)

# Запуск бота
async def main():
    await app.start()
    print("🤖 Бот запущен")
    await background_worker()

if __name__ == "__main__":
    asyncio.run(main())
