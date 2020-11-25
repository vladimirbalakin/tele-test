from random import randint
import time

import telebot

from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Stone', 'Paper', 'Scissors')
gameboard = ['Stone', 'Paper', 'Scissors']
winTable = {0 : 2, 1 : 0, 3 : 2}

def setWin(numUser, numBot):
    global winTable
    if numUser == numBot:
        return 'Draw'
    if winTable[numUser] == numBot:
        return 'User wins'
    else:
        return 'Bot wins'

@bot.message_handler(commands = ['start'])
def startMess(message):
    # print(message)
    bot.send_message(message.chat.id, 'Hello, ' + message.chat.first_name + ' ' + message.chat.last_name + '!')
@bot.message_handler(commands = ['new_game'])
def newGame(message):
    bot.send_message(message.chat.id, "Great. Choose your turn", reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def resived(message):
    # print(message)
    if message.text in gameboard:
        answer = randint(0, len(gameboard) - 1)
        bot.send_message(message.chat.id, gameboard[answer])
        numUser = gameboard.index(message.text)
        bot.send_message(message.chat.id, setWin(numUser, answer))
@bot.message_handler(content_types = ['sticker'])
def sticker_id(message):
    print(message)
bot.polling()
#gitignore.io
#PEP-8