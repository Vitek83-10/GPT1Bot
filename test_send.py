import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
target_chat_id = int(os.getenv("TARGET_CHAT_ID"))

app = Client("test_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def main():
    await app.start()
    await app.send_message(chat_id=target_chat_id, text="🧪 Тестовое сообщение от Zentru запущено успешно!")
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
