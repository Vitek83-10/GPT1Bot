import os
import asyncio
import logging
import aiohttp
from pyrogram import Client
from datetime import datetime, timezone

# === Константы ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHANNEL_ID = os.getenv("CHANNEL_ID")
AXIOM_TOKEN = os.getenv("AXIOM_TOKEN")

AXIOM_API_URL = "https://api.axiom.xyz/v1/alerts/search"

# === Логгер ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === Telegram клиент ===
app = Client("signal_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === Форматирование сообщения ===
def format_alert(data: dict) -> str:
    stats = data.get("stats", {})
    token = data.get("token", {})
    symbol = token.get("symbol", "N/A")
    address = token.get("address", "N/A")
    timestamp = data.get("timestamp")

    time_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    message = f"""🧪 <b>Тестовый сигнал от Axiom</b>
📍 <b>Токен:</b> <code>{symbol}</code>
🕒 <b>Время:</b> {time_str}

💠 <b>Метрики:</b>
• MarketCap: ${int(stats.get("marketCap", 0)):,}
• Liquidity: ${int(stats.get("liquidity", 0)):,}
• Volume: ${int(stats.get("volume", 0)):,}
• GT Score: {stats.get("gtScore", 0)}

🔗 <b>Dex:</b> <a href="https://dexscreener.com/solana/{address}">DexScreener</a>
"""
    return message

# === Axiom API — получение алертов ===
async def fetch_alerts():
    headers = {
        "Authorization": f"Bearer {AXIOM_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "limit": 5,
        "order": "desc"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(AXIOM_API_URL, headers=headers, json=payload) as resp:
            if resp.status == 200:
                json_data = await resp.json()
                return json_data.get("data", [])
            else:
                logger.error(f"Ошибка Axiom API: {resp.status}")
                return []

# === Основной цикл ===
last_ids = set()

async def main_loop():
    await app.start()
    logger.info("🚀 Тестовый бот запущен...")

    while True:
        try:
            alerts = await fetch_alerts()
            for alert in alerts:
                alert_id = alert.get("id")
                if alert_id in last_ids:
                    continue
                msg = format_alert(alert)
                await app.send_message(CHANNEL_ID, msg, parse_mode="html", disable_web_page_preview=True)
                logger.info(f"📤 Отправлен тест-сигнал: {alert.get('token', {}).get('symbol')}")
                last_ids.add(alert_id)

            if len(last_ids) > 20:
                last_ids.clear()

        except Exception as e:
            logger.error(f"❌ Ошибка в цикле: {e}")

        await asyncio.sleep(60)

# === Запуск ===
if __name__ == "__main__":
    asyncio.run(main_loop())
