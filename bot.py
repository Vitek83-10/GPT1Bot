import os
import logging
import asyncio
import aiohttp
from pyrogram import Client
from datetime import datetime

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))
AXIOM_API_KEY = os.environ.get("AXIOM_API_KEY")

app = Client("gpt1_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

AXIOM_ENDPOINT = "https://api.axiom.xyz/api/v1/feed/alerts/filtered"  # ← исправлено

HEADERS = {
    "accept": "application/json",
    "authorization": AXIOM_API_KEY,
    "Content-Type": "application/json",
}

PAYLOAD = {
    "filters": {
        "is_migrated": True,
        "market_cap_usd": {"$gte": 90000},
        "liquidity_usd": {"$gte": 30000},
        "volume_usd_5m": {"$gte": 80000},
        "volume_usd_last": {"$gte": 15000},
        "volume_multiplier_5m": {"$gte": 4},
        "holders_total": {"$gte": 200},
        "holders_top_10_percent": {"$lte": 30},
        "insiders_percent": 0,
        "snipers_total": {"$lte": 6},
        "bundle_percent": {"$lte": 35},
    },
    "limit": 5,
    "sort": {"timestamp": -1}
}


async def fetch_filtered_alerts():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(AXIOM_ENDPOINT, headers=HEADERS, json=PAYLOAD) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("data", [])
                else:
                    logging.error(f"❌ Ошибка при запросе Axiom API: {resp.status}")
                    return []
    except Exception as e:
        logging.error(f"❌ Ошибка запроса к Axiom: {str(e)}")
        return []


async def send_signal(alert):
    token = alert.get("token", {})
    name = token.get("name", "Unknown")
    symbol = token.get("symbol", "")
    address = token.get("address", "")
    market_cap = round(alert.get("market_cap_usd", 0))
    liquidity = round(alert.get("liquidity_usd", 0))
    volume = round(alert.get("volume_usd_5m", 0))
    gt_score = alert.get("gt_score", 0)
    holders = alert.get("holders_total", 0)
    top10 = alert.get("holders_top_10_percent", 0)
    insiders = alert.get("insiders_percent", 0)
    snipers = alert.get("snipers_total", 0)
    bundle = alert.get("bundle_percent", 0)
    timestamp = alert.get("timestamp")

    time_str = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S")

    msg = f"""✅ <b>Новый токен с миграцией!</b>
<b>{name} ({symbol})</b>
🕒 {time_str}
🔗 <code>{address}</code>

📊 <b>Метрики:</b>
• 💰 MCap: ${market_cap}
• 💧 Liquidity: ${liquidity}
• 📈 Volume (5m): ${volume}
• 🧠 GT Score: {gt_score}
• 👥 Holders: {holders}
• 🏦 Top10: {top10}%
• 🕵️ Insiders: {insiders}%
• 🧨 Snipers: {snipers}
• 📦 Bundled: {bundle}%

📡 <i>Сигнал от Axiom, миграция подтверждена.</i>"""

    await app.send_message(chat_id=TARGET_CHAT_ID, text=msg, parse_mode="HTML")


async def main_loop():
    while True:
        logging.info("🟢 Axiom проверка запущена")
        alerts = await fetch_filtered_alerts()
        for alert in alerts:
            await send_signal(alert)
        await asyncio.sleep(300)


if __name__ == "__main__":
    app.start()
    asyncio.get_event_loop().run_until_complete(main_loop())
