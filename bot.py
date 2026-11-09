
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# هيقرأ التوكن من إعدادات السيرفر (الأمان)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEB_APP_URL = 'https://mansawy123.github.io/mining-app/'

if not BOT_TOKEN:
    print("خطأ: لم يتم العثور على التوكن!")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=WEB_APP_URL)
    btn = InlineKeyboardButton(text="🚀 ابدأ التعدين الآن", web_app=web_app)
    markup.add(btn)
    
    welcome_text = (
        f"أهلاً بك يا {message.from_user.first_name} في **Viking Miner**! ⚔️\n\n"
        "هل أنت مستعد لتعدين عملات $VIKING؟ اضغط على الزر بالأسفل لبدء اللعبة."
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

print("البوت شغال...")
bot.infinity_polling()
