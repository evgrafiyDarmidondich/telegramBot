import telebot
from guard import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello']) # Фильтр для команд (сработает при вводе /start & /hello)
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет!!!')

@bot.message_handler(commands=['help']) # Фильтр для команд (сработает при вводе /help)
def help_message(message):
    bot.send_message(message.chat.id, "Помог чем смог!!!💁🏿")













# bot.polling(none_stop=True)
bot.infinity_polling()