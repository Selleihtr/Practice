import telebot
import json
import requests

from telebot import types

API = 'cur_live_LDAmuIjxD3rxMDYVKnx3VZUCjdyVaTo008qVvJeX'

bot = telebot.TeleBot('7119492440:AAEFnCeigGiT6ikr63M8lXYp_i3qs4PqhKY')
amount = 1

setOfVal=["USD","EUR","RUB","USDC","USDT","BYN"]

image_ur =[
            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_the_United_States_%28DoS_ECA_Color_Standard%29.svg/500px-Flag_of_the_United_States_%28DoS_ECA_Color_Standard%29.svg.png"
            ,"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/500px-Flag_of_Europe.svg.png"
            ,"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/1599px-Flag_of_Russia.svg.png"
            ,"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Circle_USDC_Logo.svg/2048px-Circle_USDC_Logo.svg.png"
            ,"https://upload.wikimedia.org/wikipedia/commons/e/e9/Tether_USDT.png"
            ,"https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/1280px-Flag_of_Belarus.svg.png"
           ]

fromVal = "USD"
res = requests.get('http://api.currencyapi.com/v3/latest?apikey=cur_live_LDAmuIjxD3rxMDYVKnx3VZUCjdyVaTo008qVvJeX&currities=%7BEUR%7D%2C{fromVal}%2CCAD')

@bot.message_handler(commands=['start'])
def startFunc(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Введите /rate, чтобы конвертировать\n /help - список всех команд')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help info!</b> \n <em>/switch - поменять валюту</em>', parse_mode = 'html')

@bot.message_handler(commands=['rate'])
def rate(message):
    global amount
    global setOfVal
    try:
        bot.send_message(message.chat.id ,  f'Введите число, которое хотите конвертиорвать из {fromVal}')
        amount =  float(message.text.strip())
        bot.send_message(message.chat.id, f'Вот список основных валют в {fromVal}')
        for i in range(len(setOfVal)):
            bot.send_message(message.chat.id,f'{amount} {fromVal} = {round(res.json()["data"][setOfVal[i]]["value"]*amount/(res.json()["data"][fromVal]["value"]),3)} {setOfVal[i]}')
        amount = 1
        return
    except ValueError:
        bot.register_next_step_handler(message, rate)
        return
    
    

@bot.message_handler(commands = ['switch'])
def switch(message):
    values = ""
    num = 0
    global fromVal
    for i in range(len(setOfVal)):
        values += f'\n{i+1} {setOfVal[i]}'
    try:
        bot.send_message(message.chat.id ,  f'Текущая валюта: {fromVal}\n Введите номер валюты, чтобы изменить: {values}')
        num =  int(message.text.strip())-1
        if num >-1 and num<6:
            fromVal = setOfVal[num]
            bot.send_message(message.chat.id , f'Валюта изменена на {fromVal}')
        return
    except ValueError:
        bot.register_next_step_handler(message, switch)
        return
    
    
    
@bot.inline_handler(lambda query: len(query.query) > 0)
def inline_query_handler(inline_query):
    results = []
    global amount
    # Создаем объект InlineQueryResultButton]
    res = requests.get('http://api.currencyapi.com/v3/latest?apikey=cur_live_LDAmuIjxD3rxMDYVKnx3VZUCjdyVaTo008qVvJeX&currities=%7BEUR%7D%2C{fromVal}%2CCAD')

    for i in range(len(setOfVal)):
        if fromVal == setOfVal[i]:
            continue
        results.append(types.InlineQueryResultArticle(
        id=i,
        title=f'{fromVal} to {setOfVal[i]}',
        input_message_content = types.InputTextMessageContent(f'Курс 1 {fromVal} = {round(res.json()["data"][setOfVal[i]]["value"]*amount/(res.json()["data"][fromVal]["value"]),3)} {setOfVal[i]}'),
        thumbnail_url=f'{image_ur[i]}'
    ))

    # Добавляем объект InlineQueryResultButton в список результатов
    results.append(results)

    # Отправляем ответ на inlinequery запрос
    bot.answer_inline_query(inline_query.id, results)

bot.infinity_polling()

