import asyncio
import logging
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

# ====== ПОЛНЫЕ НАСТРОЙКИ (УЖЕ ВСТАВЛЕНО) ======
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "7537931821:AAFZnLwQbaX2cKElaPXtyZX1HbypU6elwpE"
TARGET_CHAT_ID = "@Viktor83_Bot"
AXIOM_API_KEY = "xapt-e7590452-e334-454f-81e6-095adbef4cee"
# ==============================================

bot = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

@bot.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text("🚀 Бот успешно запущен!")

@bot.on_message(filters.command("status"))
async def status_command(client: Client, message: Message):
    await message.reply_text("✅ Бот работает и готов к действиям.")

@bot.on_message(filters.command("deploy"))
async def deploy_command(client: Client, message: Message):
    await message.reply_text("📡 Автопоток запущен.")
    asyncio.create_task(start_autopilot())

async def start_autopilot():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {AXIOM_API_KEY}",
                    "Content-Type": "application/json"
                }
                async with session.get("https://api.axiom.xyz/v1/tokens", headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()

                        for token in data.get("results", []):
                            if token.get("gt_score", 0) >= 60 and token.get("volume", 0) >= 7000:
                                name = token.get("name", "Unknown")
                                address = token.get("address", "N/A")
                                gt_score = token.get("gt_score", "N/A")
                                volume = token.get("volume", "N/A")
                                holders = token.get("holders", "N/A")
                                migrated = token.get("migrated", False)
                                migration_time = token.get("migration_age_minutes", None)
                                top10 = token.get("top10_holders_percent", "N/A")
                                sentiment = token.get("sentiment", "N/A")
                                creators = token.get("creators", "N/A")
                                mentions = token.get("mentions", "N/A")
                                engagements = token.get("engagements", "N/A")

                                migration_block = "🧬 Миграция: ✅" if migrated else "🧬 Миграция: ❌"
                                if migrated and migration_time:
                                    migration_block += f" ({migration_time} мин. после запуска)"

                                text = (
                                    f"📡 <b>Новый сигнал от GPT1Bot</b>\n\n"
                                    f"🪙 <b>{name}</b>\n"
                                    f"🏷 <code>{address}</code>\n\n"
                                    f"{migration_block}\n"
                                    f"👥 Holders: {holders}\n"
                                    f"💰 Top10: {top10}%\n"
                                    f"📊 GT Score: {gt_score}\n"
                                    f"💸 Volume: ${volume}\n\n"
                                    f"📣 LunarCrush:\n"
                                    f"• Engagements: {engagements}\n"
                                    f"• Mentions: {mentions}\n"
                                    f"• Creators: {creators}\n"
                                    f"• Sentiment: {sentiment}%\n\n"
                                    f"🔗 <a href='https://pump.fun/{address}'>Pump</a> | "
                                    f"<a href='https://dexscreener.com/solana/{address}'>Dex</a> | "
                                    f"<a href='https://app.lunarcrush.com/t/{address}'>LunarCrush</a>"
                                )

                                await bot.send_message(chat_id=TARGET_CHAT_ID, text=text, parse_mode="html")

            await asyncio.sleep(30)

        except Exception as e:
            logging.error(f"❌ Ошибка автопотока: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    bot.run()
