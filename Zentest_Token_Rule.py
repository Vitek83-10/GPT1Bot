import asyncio
from pyrogram import Client
import httpx

BOT_TOKEN = "8085881327:AAHtgjesSjMbyektB5W2YXlSDQAGk_MMPfc"
CHAT_ID = 1047298304

API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"

AXIOM_API_KEY = "xapt-e7590452-e334-454f-81e6-095adbef4cee"  # твой рабочий Axiom токен

async def main():
    async with httpx.AsyncClient() as client:
        # ⚠️ Запрос всех токенов без фильтра
        response = await client.get(
            "https://api.axiom.so/api/v1/tokens",
            headers={"Authorization": f"Bearer {AXIOM_API_KEY}"}
        )
        data = response.json()
        tokens = data.get("tokens", [])

    async with Client("ztest_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) as app:
        for token in tokens[:5]:  # только первые 5 токенов для проверки
            message = f"🔔 Новый токен: {token.get('name', 'Unnamed')} \nCA: `{token.get('address')}`"
            await app.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    asyncio.run(main())
