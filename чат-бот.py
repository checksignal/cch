import telebot
import datetime
import time
 
a = time.ctime(time.time())
b = datetime.date.today()

bot = telebot.TeleBot('853773962:AAGtVUwCTCMm6N7spBx14xvNpNkiUB9o01A')

board = telebot.types.ReplyKeyboardMarkup()
board.row('привет','пока',)
board.row('как дела?','какая сегодня дата?')
board.row('сколько времени?', 'Google')
board.row('Яндекс', 'Гисметео')
board.row('Электронный журнал', 'Mail.ru')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет', reply_markup = board)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'пока, рад был пообщаться :)')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'норм, я же бот :)')
    elif message.text.lower() == 'какая сегодня дата?':
        bot.send_message(message.chat.id, b)
    elif message.text.lower() == 'сколько времени?':
        bot.send_message(message.chat.id, a )
    elif message.text.lower() == 'google':
        bot.send_message(message.chat.id, 'https://www.google.ru' )
    elif message.text.lower() == 'яндекс':
        bot.send_message(message.chat.id, 'https://yandex.ru' )
    elif message.text.lower() == 'гисметео':
        bot.send_message(message.chat.id, 'https://www.gismeteo.ru' )
    elif message.text.lower() == 'электронный журнал':
        bot.send_message(message.chat.id, 'https://sgo.egov66.ru/' )
    elif message.text.lower() == 'mail.ru':
        bot.send_message(message.chat.id, 'https://mail.ru' )
    else:
        bot.send_message(message.chat.id, 'извини, но я тебя не понял...')


bot.polling()