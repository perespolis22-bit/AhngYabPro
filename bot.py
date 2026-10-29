
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN تنظیم نشده است.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "سلام رفیق! 🎵\n"
        "به آهنگ‌یاب پرو خوش اومدی.\n"
        "به‌زودی قابلیت جست‌وجوی آهنگ اضافه می‌شه."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "🎶 آهنگ موردنظرت رو برام بنویس!"
    )

bot.infinity_polling()
