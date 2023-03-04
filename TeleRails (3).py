import random


import telebot
import time
from telebot import types
import os, sys
from requests.exceptions import ConnectionError, ReadTimeout
from random import shuffle
TOKEN = '5902261299:AAGXa8B4LWFh0XSvtwE4Z3pq75daxDHzSoM'
bot = telebot.TeleBot(TOKEN)
chat = 2117564356
video = 'https://youtube.com/@Telebot624'
HELP = """
/start - начать работу
/help - помощь
/fact - факт
/end - завершить работу(лучше так не делать)
/restart - заново"""

fac1 = '*Перемещение по железной дороге является в 45 раз более безопасным, чем по автодороге. Риск попасть в аварию в поезде существенно ниже, чем в машине.*'
fac2 = '*Открытие железнодорожного сообщения Москва – Санкт-Петербург стало настоящим событием. Вот только простые люди не спешили нововведением пользоваться. Страшная грохочущая штука вызывала неподдельный страх.*'
fac3 = '*Москву и Владивосток соединяет только 1 дорога – Транссибирская магистраль.*'
fac4 = '*Сегодня (в среднем) каждый россиянин проезжает по железной дороге примерно 9 раз в год. А общее количество гостей давно перевалило за 1,3 миллиарда человек в год.*'
fac5 = '*Чтобы продвинуть железнодорожные перевозки в массы, решено было сделать проезд бесплатным. И эта мера возымела действие. Поезда очень скоро перестали бояться.*'
fac6 = '*Средний возраст локомотива в ОАО «РЖД» - 50 летАО «РЖД» работает более 700 000 человек.*'
fac7 = '*Транссиб – это 9438 километров, больше 8 дней в пути. На маршруте поезд останавливается на 97 крупных станциях и проезжает множество мелких.*'
fac8 = '*Некоторые фирменные поезда имеют двухэтажные вагоны. На таких можно добраться, например, из Москвы в Воронеж, из Санкт-Петербурга в Адлер.*'
line = [fac1,fac2,fac3,fac4,fac5,fac6,fac7,fac8,]


vopr = 4
bot.send_message(chat, text='*Чтобы начать пользование, введи: /start*',parse_mode='Markdown')
bot.send_message(chat, text='*Чтобы посмотреть все команды, введи:/help*',parse_mode='Markdown')

vopros = """
*1 - от 5000 до 10000 Вольт
2 - от 27000 и более
3 - от 10000 и до 27000 Вольт максимум*"""
vopros2 = """
*a) - Закрепиться,чтобы не упасть.После выбраться через аварийный выход
б) - Уходить скорее
в) - Ничего не предпринимать и просто ждать*"""

#Начальное приветствие и обработка сообщений пользователя
@bot.message_handler(content_types=['text'])
def mes(message):
    global vopr

    if message.text == "/start":
        bot.send_message(chat, text=f"*Привет , {message.from_user.first_name} ,меня зовут TeleRails!*",
                         parse_mode="Markdown")
        start('jf')
    elif message.text == "/restart":
        bot.send_message(chat, text=f"*Привет , {message.from_user.first_name} ,меня зовут TeleRails!*",
                         parse_mode="Markdown") 
        restart("uai")
         

    elif message.text == "/help":

        help('skd')
    elif message.text == "/end":
        kon("aip")
    elif message.text == "/fact":
        fact("dsi")
    elif message.text == "Факт 1":
        bot.send_message(chat,text = fac1,parse_mode='Markdown')
    elif message.text == "Факт 2":
        bot.send_message(chat,text = fac2,parse_mode='Markdown') 
    elif message.text == "Факт 3":
        bot.send_message(chat,text = fac3,parse_mode='Markdown') 
    elif message.text == "Факт 4":
        bot.send_message(chat,text = fac4,parse_mode='Markdown') 
    elif message.text == "Факт 5":
        bot.send_message(chat,text = fac5,parse_mode='Markdown')  
    elif message.text == "Факт 6":
        bot.send_message(chat,text = fac6,parse_mode='Markdown')
    elif message.text == "Факт 7":
        bot.send_message(chat,text = fac7,parse_mode='Markdown')
    elif message.text == "Факт 8":
        bot.send_message(chat,text = fac8,parse_mode='Markdown')                                         


    elif message.text == "2":
        end("fja")

    elif message.text == "1" or "3":
        vopr -= 1
        end("aia")
   







#факты
@bot.message_handler(commands=['/fact'])
def hearts(message):
    
    bot.send_message(chat,random.choice(line),parse_mode="Markdown")



#команда конец
@bot.message_handler(commands=['/end'])
def kon(message):
    bot.send_message(chat,text="*Ваша работа завершена*",parse_mode='Markdown')
    time.sleep(5)
    bot.send_message(chat, text='*Чтобы начать пользование, введи: /start*', parse_mode='Markdown')
    bot.send_message(chat, text='*Чтобы посмотреть все команды, введи:/help*', parse_mode='Markdown')


#помощь
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(chat, text=HELP)

#команда рестарт
@bot.message_handler(commands=['restart'])
def restart(message):
    start("ii")

#команда старт
@bot.message_handler(commands=["start"])
def start(message):
    a = 1
    while a < 2:
        a += 1
        time.sleep(2)
        bot.send_message(chat, text="*Для ознакомления с правилами безопасноcти предлагаю посмотреть видео*",
                         parse_mode="Markdown")
        time.sleep(2)

    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Да", callback_data="yes")
    btn2 = types.InlineKeyboardButton("Нет", callback_data="no")
    markup.add(btn1, btn2)
    bot.send_message(chat, text="*Будешь смотреть?*", reply_markup=markup, parse_mode="Markdown")


# ответы на нажатие кнопок
@bot.callback_query_handler(func=lambda call: True)
def button(call):
    global vopr
    if call.message:
        if call.data == "yes":
            bot.send_message(call.from_user.id, text='*Отлично!*', parse_mode="Markdown")
            time.sleep(4)
            bot.send_message(call.from_user.id, text="*Ожидание загрузки...*", parse_mode="Markdown")
            bor("fj")

        elif call.data == "no":
            bot.send_message(call.from_user.id, text='*Ладно,в другой раз((*', parse_mode="Markdown")
        elif call.data == "d":
            bot.send_message(call.from_user.id, text="*Это хорошо*",parse_mode='Markdown')
            time.sleep(3)
            bot.send_message(chat, text="*Я думаю,что уже стоит переходить к чему-то серьёзному*",parse_mode='Markdown')
            tec("jg")
        elif call.data == "c":
            time.sleep(2)
            bot.send_message(chat,text=f"Лови ссылку - {video}")
            tec("jg")
        elif call.data == "f":
            time.sleep(2)

            tec("jg")



        # ответ 1
        elif call.data == "sed":

            tos("fj")
        elif call.data == "net":
            vopr -= 1
            tos("ab")
        # ответ 2
        elif call.data == "ver":
            car("gj")
        elif call.data == "xy":
            vopr -=1
            car("js")
        # ответ 3
        elif call.data == "com":
            cool("fgf")

        elif call.data == "bf" or "mg":
            vopr -= 1
            cool('sjd')







#видео
@bot.message_handler(content_types=['text'])
def bor(message):
    text = '*Вот видео:https://youtu.be/T7GQA0iIxO4* '
    bot.send_message(chat, text=text, parse_mode='Markdown')

    fact("fjh")

# вопрос о просмотре
@bot.message_handler(content_types=['text'])
def fact(message):
    bot.send_message(chat, text="*Смотри полностью!*",parse_mode='Markdown')

    markup2 = types.InlineKeyboardMarkup(row_width=2)
    bet1 = types.InlineKeyboardButton("Конечно", callback_data="d")
    bet2 = types.InlineKeyboardButton("Хочу посмотреть ещё", callback_data="c")
    bet3 = types.InlineKeyboardButton("Я даже не начинал", callback_data='f')

    markup2.add(bet1, bet2, bet3)
    bot.send_message(chat, text="*Посмотрел?*", reply_markup=markup2,parse_mode='Markdown')

# начало теста
@bot.message_handler(content_types=['text'])
def tec(message):
    time.sleep(4)
    bot.send_message(chat, text="*Сейчас будет небольшой тест*",parse_mode='Markdown')
    time.sleep(4)
    bot.send_message(chat, text="*И мы определим насколько близко ты знаком с безопасностью на ж.д*",parse_mode='Markdown')
    time.sleep(4)
    test("jg")

# вопрос 1
@bot.message_handler(content_types=['text'])
def test(message):
    markup3 = types.InlineKeyboardMarkup(row_width=1)
    bat1 = types.InlineKeyboardButton("Для безопасного перехода", callback_data="sed")
    bat2 = types.InlineKeyboardButton("Просто так,для красоты", callback_data="net")
    markup3.add(bat1, bat2)
    bot.send_message(chat, text="*Для чего сделаны пешеходные дорожки у железнодорожных путей?*", reply_markup=markup3,parse_mode='Markdown')

# вопрос 2
@bot.message_handler(content_types=['text'])
def tos(message):
    markup4 = types.InlineKeyboardMarkup(row_width=1)
    bat3 = types.InlineKeyboardButton("Стоит", callback_data="ver")
    bat4 = types.InlineKeyboardButton("Не надо", callback_data="xy")
    markup4.add(bat3, bat4)
    bot.send_message(chat, text="*А стоит ли обращать внимание на световые и звуковые сигналы?*", reply_markup=markup4,parse_mode='Markdown')

# вопрос 3
@bot.message_handler(content_types=['text'])
def car(message):
    markup5 = types.InlineKeyboardMarkup(row_width=1)
    bit3 = types.InlineKeyboardButton("Невнимательность,игры", callback_data="com")
    bit4 = types.InlineKeyboardButton("Из-за дорог", callback_data="bf")
    bit5 = types.InlineKeyboardButton("Погода виновата",callback_data='mg')
    markup5.add(bit3, bit4,bit5)
    bot.send_message(chat, text="*Из-за чего,по-вашему,происходят неприятные случаи на железных дорогах?*", reply_markup=markup5,parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def cool(message):
    time.sleep(2)
    bot.send_message(chat,text="*Давайте изменим правила работы*",parse_mode="Markdown")
    time.sleep(2)
    bot.send_message(chat,text="*Хватит с кнопок,теперь будем отвечать только цифрами *",parse_mode="Markdown")
    btc("ewi")

# вопрос 4
@bot.message_handler(content_types=['text'])
def btc(message):
    time.sleep(2)
    bot.send_message(chat, text="*Каковы показатели переменного тока на жд?*",parse_mode='Markdown')
    bot.send_message(chat, text=vopros, parse_mode='Markdown')
    time.sleep(2)
    bot.send_message(chat,text="*Выбери любую цифру ответа*",parse_mode="Markdown")



# окончание теста
@bot.message_handler(content_types=['text'])
def end(message):
    time.sleep(2)
    bot.send_message(chat,text="*Тест окончен*",parse_mode='Markdown')
    time.sleep(2)
    bot.send_message(chat, text=f"*Ваш результат - {vopr} из 4*",parse_mode='Markdown')
    time.sleep(2)
    bot.send_message(chat, text="*Пожалуйста напишите в документе Word ваши советы для улучшения безопасности на ж.д*",parse_mode='Markdown')
    time.sleep(2)
    bot.send_message(chat,text='*И отправьте его нам*',parse_mode='Markdown')

#переброска документа и ответ на неё
@bot.message_handler(content_types=['document'])
def doc(message):
    if message.content_type == 'document':
        bot.send_message(chat,text="*Ваш ответ принят*",parse_mode='Markdown')
        send("aod")

#сообщение об окончании работы 
@bot.message_handler(content_types=['text'])
def send(message):
    time.sleep(2)
    bot.send_message(chat,text="*Наша работа подходит к концу*",parse_mode="Markdown")
    time.sleep(2)
    bot.send_message(chat, text="*Для любознательных есть команда /fact*", parse_mode="Markdown")
    time.sleep(2)
    bot.send_message(chat,text="*C ней вы можете получить 8 интересных фактов о ж.д*",parse_mode="Markdown")
    time.sleep(2)
    bot.send_message(chat,text="*Кнопки есть в разделе кнопок*",parse_mode="Markdown")
#клавиатура команды факт
@bot.message_handler(content_types="text")
def fact(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    f1 = types.KeyboardButton("Факт 1")
    f2 = types.KeyboardButton("Факт 2")
    f3 = types.KeyboardButton("Факт 3")
    f4 = types.KeyboardButton("Факт 4")
    f5 = types.KeyboardButton("Факт 5")
    f6 = types.KeyboardButton("Факт 6")
    f7 = types.KeyboardButton("Факт 7")
    f8 = types.KeyboardButton("Факт 8")
    markup.add(f1,f2,f3,f4,f5,f6,f7,f8)
    bot.send_message(chat,text="Выберите один из них:",reply_markup=markup)









bot.polling(none_stop=True,timeout=123)













