pyrogram.types import Message

# Замените на свои значения
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "7537931821:AAFZnLwQbaXZ9QFY0QHx_oWArS0MneB7QkE"

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Команда /start
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("🚀 Бот успешно запущен!")

# Команда /status
