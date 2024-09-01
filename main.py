import telebot
import config
import random
from random import choice

bot = telebot.TeleBot(token=config.BOT_TOKEN)

# новая функция (рандомные цитаты Джейсона Стэтхема) '/quote'
@bot.message_handler(commands=['quote'])
def citata_handler(message):
    citata = choice(['Нужно делать как нужно, как не нужно делать не нужно © Джейсон Стетхэм', 
          'За двумя зайцами погонишься - не вытащишь рыбку из пруда © Джейсон Стетхэм', 
          'Каждый может кинуть камень в волка, но не каждый может кинуть волка в камень © Джейсон Стетхэм', 
          'Одна ошибка - и ты ошибся © Джейсон Стетхэм', 
          'Как корабль назовешь - так на нем и напишут © Джейсон Стетхэм', 
          'Если не знаешь как поступить, поступай как знаешь © Джейсон Стетхэм'])
    bot.reply_to(message, citata)

# новая функция (орел / решка) '/coin'
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["Орёл", "Решка"])
    bot.reply_to(message, coin)

# что делает бот? '/start' и '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я Эхобот!
Отправь чё нибудь в чат и я тебе верну такое же сообщение!\
""")

# возвращение текста 'любой текст'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()