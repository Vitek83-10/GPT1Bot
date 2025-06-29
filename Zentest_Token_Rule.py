import asyncio
import aiohttp

# 🔑 Твой рабочий токен бота и ID чата
BOT_TOKEN = "8085881327:AAHtgjesSjMbyektB5W2YXlSDQAGk_MMPfc"
CHAT_ID = 1047298304  # твоя личка

async def main():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message = "🧪 Тестовое сообщение от Zentest! Всё работает ✅"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"chat_id": CHAT_ID, "text": message}) as resp:
            result = await resp.text()
            print("Ответ Telegram:", result)

if __name__ == "__main__":
    asyncio.run(main())
