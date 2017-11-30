# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem
# отчет о работе бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater("450246591:AAGV-8xA2dfU1Sft-KaV1u_yqu-sgxOOip4")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet, pass_args = True))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

# Вызываем функцию - эта строчка собственно запускает бота
    updater.start_polling()
    updater.idle()


# greet_user посылать сообщение обратно в Telegram
def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

# функцию, которая будет "отвечать" пользователю
def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

# planet
def planet(bot, update, args):
    today = '2017/11/25'
    try:
        planet = args[0].lower()
        if planet in ['марс', 'mars']:
            planet = ephem.Mars(today)
            const = ephem.constellation(planet)[1]
        elif planet in ['venus', "винера"]:
            planet = ephem.Venus(today)
            const = ephem.constellation(planet)[1]
        else:
            const = "Not known"
        
        update.message.reply_text(const)
    except:
        update.message.reply_text("Укажи планету")    

# wordcount
def wordcount(bot,update):
    word = update.message.text
    word_summ = len(word.split(' '))
    word_summ = int(word_summ - 1)
    logging.info(word_summ)

    try:

        if word_summ == 1:
            update.message.reply_text(str(word_summ) + " cлово")
        elif word_summ <= 4:
            update.message.reply_text(str(word_summ) + " cлова")
        elif word_summ >= 5:
            update.message.reply_text(str(word_summ) + " cлов")
        elif word_summ <= 0:
            update.message.reply_text("Вы не ввели не одного")            
    except:

        update.message.reply_text("Введите фразу!")          



main()