from config import BOT_TOKEN
import telebot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func = lambda message: True, content_types = [text])
def answer(message):
    bot.send_message(message.chat_id, message.text)

if __name__ == "__main__":
    bot.polling(non_stop = True)