import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('6427474517:AAFYT5Da2ov5JFvsxg4qRF7f1Kub-haYim0')
#token

@bot.message_handler(commands=['start'])
# message тут вся инфа про пользователя 
def startFunc(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help info!</b> \n <em>blablabla</em>', parse_mode = 'html')

    

@bot.message_handler(commands=['date'])
def date(message):
    
    dtime = datetime.datetime.today()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Обновить', callback_data='edit'))
    bot.send_message(message.chat.id , f'Текущее время и дата: \n{dtime}', reply_markup = markup)
   
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'edit':
        dtime = datetime.datetime.today()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Обновить', callback_data='edit'))
        bot.edit_message_text(f'Текущее время и дата: \n{dtime}' , callback.message.chat.id,callback.message.message_id, reply_markup = markup)



bot.infinity_polling()
