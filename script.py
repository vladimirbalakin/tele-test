from config import BOT_TOKEN
from random import randint
import telebot
import time

bot = telebot.TeleBot(BOT_TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Stone', 'Paper', 'Scissors')
gameboard = ['Stone', 'Paper', 'Scissors']

@bot.message_handler(commands = ['start'])
def startMess(message):
    #print(message)
    bot.send_message(message.chat.id, 'Hello, ' + message.chat.first_name + ' ' + message.chat.last_name + '!')
@bot.message_handler(commands = ['new_game'])
def newGame(message):
    bot.send_message(message.chat.id, "Great. Choose your turn", reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def resived(message):
    #print(message)
    if message.text in gameboard:
        answer = randint(0, 2)
        bot.send_message(message.chat.id, gameboard[answer])
@bot.message_handler(content_types = ['sticker'])
def sticker_id(message):
    print(message)
bot.polling()