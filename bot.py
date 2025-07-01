import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "👋 Бот активен и готов к приёму сигналов.")

@bot.message_handler(commands=["status"])
def handle_status(message):
    bot.send_message(message.chat.id, "📡 Статус: бот запущен, ожидание сигналов...")

@bot.message_handler(commands=["test"])
def handle_test(message):
    bot.send_message(message.chat.id, "🧪 Тест-сигнал отправлен в канал.")

# Обработка всех остальных сообщений (если нужно)
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.send_message(message.chat.id, "🤖 Неизвестная команда. Используй /start, /status или /test.")

if __name__ == "__main__":
    print("✅ Бот запущен и слушает команды...")
    bot.infinity_polling()
