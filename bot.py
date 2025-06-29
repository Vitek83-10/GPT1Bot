import os
import logging
import requests
from pyrogram import Client, filters

logging.basicConfig(level=logging.INFO)

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
AXIOM_API_KEY = os.environ.get("AXIOM_API_KEY")
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

AXIOM_HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {AXIOM_API_KEY}"
}

# 👇 Укажи здесь ID своей организации в Axiom
WORKSPACE_ID = "viktorsignals"  # если нужно — поменяем

@bot.on_message(filters.command("test"))
async def test_axiom(_, message):
    url = "https://api.axiom.xyz/v1/alerts/search"
    payload = {
        "workspaceId": WORKSPACE_ID,
        "limit": 1
    }

    response = requests.post(url, headers=AXIOM_HEADERS, json=payload)

    if response.status_code == 200:
        await message.reply("✅ Axiom API успешно отвечает!")
    else:
        await message.reply(f"❌ Ошибка Axiom: {response.status_code}\n{response.text}")

@bot.on_message(filters.command("start") | filters.command("status"))
async def status_handler(_, message):
    await message.reply("✅ Бот работает и подключён!")

if __name__ == "__main__":
    logging.info("🚀 Тестовый бот запущен...")
    bot.run()
