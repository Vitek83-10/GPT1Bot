import asyncio
from pyrogram import Client

# 🔐 Токен твоего бота
BOT_TOKEN = "8085881327:AAHtgjesSjMbyektB5W2YXlSDQAGk_MMPfc"

# 🆔 chat_id, куда бот отправит сообщение
CHAT_ID = 1047298304

# 📲 api_id и api_hash
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"

async def main():
    await asyncio.sleep(5)  # Подождём немного, пока бот запустится
    async with Client("ztest_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) as app:
        await app.send_message(
            chat_id=CHAT_ID,
            text="✅ Zentest_Token_Rule отработал"
        )

if __name__ == "__main__":
    asyncio.run(main())
