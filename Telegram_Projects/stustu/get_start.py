from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

updater = Updater(token='1815367351:AAFntlKS61zNyGXBoICwoMFrLgsLzpMhT5k', use_context=True)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('shit', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

