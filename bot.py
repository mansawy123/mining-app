import html
import os

import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

BOT_TOKEN = os.environ.get("BOT_TOKEN")  # set in the host's Variables, never in the code
WEB_APP_URL = "https://mansawy123.github.io/mining-app/"

if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN is not set")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🚀 ابدأ التعدين الآن", web_app=WebAppInfo(url=WEB_APP_URL)))

    name = html.escape(message.from_user.first_name or "Viking")
    text = (
        f"أهلاً بك يا {name} في <b>Viking Miner</b>! ⚔️\n\n"
        "هل أنت مستعد لتعدين عملات $VIKING؟ اضغط على الزر بالأسفل لبدء اللعبة."
    )
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="HTML")


print("Bot is running...")
bot.infinity_polling(skip_pending=True)
