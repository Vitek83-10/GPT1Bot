import os
import asyncio
import logging
import aiohttp
from pyrogram import Client
from datetime import datetime, timezone

# === Константы и переменные ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHANNEL_ID = int(os.getenv("TARGET_CHAT_ID"))  # <-- ВАЖНО: исправлено!
AXIOM_TOKEN = os.getenv("AXIOM_API_KEY")

AXIOM_API_URL = "https://api.axiom.xyz/v1/alerts/search"

# === Настройка логгера ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === Клиент Telegram ===
app = Client("signal_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === Функция фильтрации токенов по метрикам ===
def is_token_valid(data: dict) -> bool:
    try:
        stats = data.get("stats", {})
        market_cap = stats.get("marketCap", 0)
        liquidity = stats.get("liquidity", 0)
        volume = stats.get("volume", 0)
        last_volume = stats.get("lastVolume", 0)
        volume_multiplier = stats.get("volumeMultiplier", 0)
        top10 = stats.get("top10", 100)
        holders = stats.get("holders", 0)
        insiders = stats.get("insiders", 100)
        snipers = stats.get("snipers", 100)
        bundle_supply = stats.get("bundleSupply", 100)
        gt_score = stats.get("gtScore", 0)
        migrated = stats.get("migrated", 0)

        if migrated != 1:
            return False

        return (
            market_cap >= 90000 and
            liquidity >= 30000 and
            volume >= 80000 and
            last_volume >= 15000 and
            volume_multiplier >= 4 and
            top10 <= 30 and
            holders >= 200 and
            insiders == 0 and
            snipers <= 6 and
            bundle_supply <= 35 and
            gt_score >= 35
        )
    except Exception as e:
        logger.error(f"Ошибка при фильтрации токена: {e}")
        return False

# === Форматирование Telegram-сообщения ===
def format_alert(data: dict) -> str:
    stats = data.get("stats", {})
    token = data.get("token", {})
    symbol = token.get("symbol", "N/A")
    address = token.get("address", "N/A")
    timestamp = data.get("timestamp")

    time_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    message = f"""✅ <b>Сигнал от Axiom</b>
📍 <b>Токен:</b> <code>{symbol}</code>
🕒 <b>Время:</b> {time_str}

💠 <b>Метрики:</b>
• MarketCap: ${int(stats.get("marketCap", 0)):,}
• Liquidity: ${int(stats.get("liquidity", 0)):,}
• Volume: ${int(stats.get("volume", 0)):,}
• Last Volume: ${int(stats.get("lastVolume", 0)):,}
• Volume Multiplier: {stats.get("volumeMultiplier", 0)}x
• Top10 Holders: {stats.get("top10", 0)}%
• Total Holders: {stats.get("holders", 0)}
• GT Score: {stats.get("gtScore", 0)}
• Bundle Supply: {stats.get("bundleSupply", 0)}%
• Snipers: {stats.get("snipers", 0)}
• Migrated: ✅

🔗 <b>Ссылки:</b>
• <a href="https://dexscreener.com/solana/{address}">DexScreener</a>
• <a href="https://www.birdeye.so/token/{address}?chain=solana">Birdeye</a>
• <a href="https://app.axiom.xyz/token/{address}">Axiom</a>
"""
    return message

# === Запрос к Axiom API ===
async def fetch_alerts():
    headers = {
        "Authorization": f"Bearer {AXIOM_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "limit": 15,
        "order": "desc"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(AXIOM_API_URL, json=payload, headers=headers) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data.get("data", [])
            else:
                logger.error(f"Ошибка запроса Axiom: {resp.status}")
                return []

# === Основной цикл ===
last_ids = set()

async def main_loop():
    await app.start()
    logger.info("Бот запущен и работает...")

    while True:
        try:
            alerts = await fetch_alerts()
            for alert in alerts:
                alert_id = alert.get("id")
                if alert_id in last_ids:
                    continue
                if is_token_valid(alert):
                    msg = format_alert(alert)
                    await app.send_message(CHANNEL_ID, msg, parse_mode="html", disable_web_page_preview=True)
                    logger.info(f"📤 Отправлен сигнал: {alert.get('token', {}).get('symbol')}")
                last_ids.add(alert_id)

            if len(last_ids) > 30:
                last_ids.clear()

        except Exception as e:
            logger.error(f"Ошибка в основном цикле: {e}")

        await asyncio.sleep(60)

# === Запуск ===
if __name__ == "__main__":
    asyncio.run(main_loop())
