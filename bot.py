import telebot
import threading
from flask import Flask
import time

TOKEN = "8643111997:AAFPwsh3VC-HK47CFDtm3cM326UAKTIgtq4"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Aktif!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Sistem bağlandı Yusuf, emrindeyim!")

def run_bot():
    while True:
        try:
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except:
            time.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=7860)).start()
    run_bot()
  
