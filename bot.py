from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )

def greet_user(update: Update, context: CallbackContext):
    text = 'вызван старт'
    #print(text)
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    user_text = 'hello, you print {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: $s', update.message.chat.username,
                update.message.chat.id, update.message.text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)
    
    logging.info("bot starting")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    
    
    mybot.start_polling()
    mybot.idle()

main()
