import telebot

bot = telebot.TeleBot('7884812562:AAENmaKhdxDN3RoQrtsYykZnfdNtLL9kDlc')


@bot.message_handler(commands=['start', 'main', 'new'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['help'])
def information(message):
    bot.send_message(message.chat.id, 'Helping')


bot.polling(none_stop = True)