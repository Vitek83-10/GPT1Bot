from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import os

# Переменные окружения
API_ID = 20234202
API_HASH = "fc0e099e810cbea903512acef8563b36"
BOT_TOKEN = "8085881327:AAHw2qT9ai3oTxT6N_0K5nc903u6VJn4Kn8"
AXIOM_API_KEY = "xapt-e7590452-e334-454f-81e6-095adbef4cee"
TARGET_CHAT_ID = -1002814931594  # канал "Мои сигналы"

app = Client("ViktorSignalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start_command(client, message: Message):
    message.reply_text("🚀 Бот успешно запущен!")

@app.on_message(filters.command("status"))
def status_command(client, message: Message):
    message.reply_text("✅ Бот работает и готов к действию.")

@app.on_message(filters.command("deploy"))
def deploy_command(client, message: Message):
    message.reply_text("🦾 Автопоток запущен.")
    send_signal_to_target("⚙️ Тестовый сигнал: автопоток активен.")

def send_signal_to_target(text):
    app.send_message(chat_id=TARGET_CHAT_ID, text=text)

@app.on_message(filters.command("stop"))
def stop_command(client, message: Message):
    message.reply_text("🛑 Поток остановлен.")

app.run()
