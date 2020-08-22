from telegram import Bot
from telegram import Update
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Updater, InlineQueryHandler, CommandHandler
from config import TG_TOKEN
import os

from opening_file import get_filename
from search import get_line
from plot_creation import research_main

def msg_hndl(bot,update):
    chat_id = update.message.chat_id
    recived_message = update.message.text
    if recived_message == 'Russia' or recived_message == 'Rusia'  :
        recived_message = 'Russian Federation'
    elif recived_message == 'Taiwan':
        recived_message = 'Taiwan Province of China'
    elif recived_message == 'Uk' or recived_message == 'GB' or recived_message == 'Great Britain':
        recived_message = 'United Kingdom'
    elif recived_message == 'USA' or recived_message == 'US' or recived_message=='usa':
        recived_message = 'United States'
    namefolder = os.getcwd()
    file_name = get_filename(namefolder, recived_message)
    if file_name != '':
        line = get_line(file_name,recived_message)
        if line != []:
            research_main(line)
            bot.send_photo(chat_id=chat_id, photo=open('test.png', 'rb'))




def do_start(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='how can i help you?')
    member = bot.getChatMember(update.message.chat_id)
    print(member)





def main():
    updater = Updater(TG_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",do_start))
    dp.add_handler(MessageHandler(Filters.text,msg_hndl))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
