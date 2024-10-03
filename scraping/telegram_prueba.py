import telebot
from scraper import scrape_data as sd


BOT_TOKEN = '7505196905:AAFrQhr9A3R4aqfDMhuGSzQWM7dVbP7ZXmo'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, {sd().to_string})

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

#***********************************************************************************************************************************************
# from scraper import scrape_data as sd

# respuesta = sd()
# print(respuesta)
