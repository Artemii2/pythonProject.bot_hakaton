import telebot
from telebot import types
from content import *
import time
import random
from itertools import product
bot = telebot.TeleBot('5155225672:AAELZ_QxSi0FOxri35jIw5XYwJWICJUZE8Y')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Далее")
    markup.add(button1)
    bot.send_message(message.chat.id, text=f"{greeting}",
                     parse_mode="html", reply_markup=markup)
    name.clear()
    name.append(message.from_user.first_name)

@bot.message_handler(commands=['menu'])
def send_welcome(message):
    inmarkup = types.InlineKeyboardMarkup(row_width=3)
    button1 = types.InlineKeyboardButton("7 класс", callback_data='class7')
    button2 = types.InlineKeyboardButton("8 класс", callback_data='class8')
    button3 = types.InlineKeyboardButton("9 класс", callback_data='class9')
    button4 = types.InlineKeyboardButton("10 класс", callback_data='class10')
    button5 = types.InlineKeyboardButton("11 класс", callback_data='class11')
    inmarkup.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, "Выберите свой класс:",
                     reply_markup=inmarkup)
    name.clear()
    name.append(message.from_user.first_name)

# Вопрос 2 (Форсирование Днепра)

@bot.message_handler(commands=['Вопрос_2'])
def hall_3558(message):
    bot.delete_message(message.chat.id, message.id - 2)
    bot.delete_message(message.chat.id, message.id - 1)
    pic = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\номер 33_photo-resizer.ru.jpg", 'rb')
    bot.send_photo(message.chat.id, pic)
    msg = bot.send_message(message.chat.id, qw_2)
    bot.register_next_step_handler(msg, next_question_2)

def next_question_2(message):
    if message.text == '75':
        bot.send_message(message.chat.id, "Поздравляю, это правильный ответ!")
        q1 = 1
        a.append(q1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_fd_2')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, reference_2, parse_mode="html", reply_markup=inmarkup)

    else:
        bot.send_message(message.chat.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_fd_2')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, reference_2, parse_mode="html", reply_markup=inmarkup)

# Вопрос 7 (Блокада Ленингралда)

@bot.message_handler(commands=['Вопрос_7'])
def hall_3557(message):
    bot.delete_message(message.chat.id, message.id - 2)
    bot.delete_message(message.chat.id, message.id - 1)
    msg = bot.send_message(message.chat.id, que_7)
    bot.register_next_step_handler(msg, next_question_7)

def next_question_7(message):
    if message.text == '1054 1040 1044 1054 1046':
        bot.send_message(message.chat.id, "Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_bl_6')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, ref_7, parse_mode="html", reply_markup=inmarkup)

    else:
        bot.send_message(message.chat.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_bl_6')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, ref_7, parse_mode="html", reply_markup=inmarkup)

# Вопрос 8 (Битва под Сталинградом)

@bot.message_handler(commands=['Вопрос_8'])
def hall_355(message):
    bot.delete_message(message.chat.id, message.id - 2)
    bot.delete_message(message.chat.id, message.id - 1)
    msg = bot.send_message(message.chat.id, qwestio_8)
    bot.register_next_step_handler(msg, next_question)

def next_question(message):
    if message.text == '17.7.1943':
        bot.send_message(message.chat.id, "Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_8')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, refere_8, parse_mode="html", reply_markup=inmarkup)

    else:
        bot.send_message(message.chat.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_8')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, refere_8, parse_mode="html", reply_markup=inmarkup)

# Вопрос 12 (Штурм Берлина)

@bot.message_handler(commands=['Вопрос_12'])
def hall_3556(message):
    bot.delete_message(message.chat.id, message.id - 2)
    bot.delete_message(message.chat.id, message.id - 1)
    msg = bot.send_message(message.chat.id, question_12)
    bot.register_next_step_handler(msg, reih)

def reih(message):
    if message.text == 'рейхстаг':
        bot.send_message(message.chat.id, "Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_sb_12')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, r_12, parse_mode="html", reply_markup=inmarkup)
    else:
        bot.send_message(message.chat.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_sb_12')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, r_12, parse_mode="html", reply_markup=inmarkup)

# Вопрос 5 (Курская битва)

@bot.message_handler(commands=['Вопрос_5'])
def hall_35523417(message):
    bot.delete_message(message.chat.id, message.id - 3)
    bot.delete_message(message.chat.id, message.id - 2)
    bot.delete_message(message.chat.id, message.id - 1)
    msg = bot.send_message(message.chat.id, qwes_5)
    bot.register_next_step_handler(msg, next_question_5)

def next_question_5(message):
    if message.text == '1200':
        bot.send_message(message.chat.id, "Поздравляю, это правильный ответ!")
        q9 = 1
        e.append(q9)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_6")
        markup.add(button1)
        bot.send_message(message.chat.id, refe_5, parse_mode="html", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="К сожалению, это неправильный ответ")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_6")
        markup.add(button1)
        bot.send_message(message.chat.id, refe_5, parse_mode="html", reply_markup=markup)

# Вопрос 6 (Курская битва)

@bot.message_handler(commands=['Вопрос_6'])
def hall_355735(message):
    bot.delete_message(message.chat.id, message.id - 4)
    bot.delete_message(message.chat.id, message.id - 3)
    bot.delete_message(message.chat.id, message.id - 2)
    bot.delete_message(message.chat.id, message.id - 1)
    msg = bot.send_message(message.chat.id, qwes_6)
    bot.register_next_step_handler(msg, next_question_6)

def next_question_6(message):
    if message.text == 'ЩЛХГЖЗОЯ':
        bot.send_message(message.chat.id, "Поздравляю, это правильный ответ!")
        q9 = 1
        e.append(q9)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_kb_6')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, refe_6, parse_mode="html", reply_markup=inmarkup)

    else:
        bot.send_message(message.chat.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_kb_6')
        inmarkup.add(button1)
        bot.send_message(message.chat.id, refe_6, parse_mode="html", reply_markup=inmarkup)

#Классы и залы
@bot.callback_query_handler(lambda call: call.data in ['class7', 'class8', 'class9', 'class10', 'class11'])
def callback_inline_class(call):
    if call.data == "class7":
        inmarkupp = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton("Контрнаступление под Москвой", callback_data='hall_1')
        b2 = types.InlineKeyboardButton("Битва под Сталинградом", callback_data='hall_2')
        b3 = types.InlineKeyboardButton("Блокада Ленинграда", callback_data='hall_3')
        b4 = types.InlineKeyboardButton("Курская битва", callback_data='hall_4')
        b5 = types.InlineKeyboardButton("Форсирование днепра", callback_data='hall_5')
        b6 = types.InlineKeyboardButton("Штурм Берлина", callback_data='hall_6')

        inmarkupp.add(b1, b2, b3, b4, b5, b6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Выберите зал:",
                              reply_markup=inmarkupp)
        bot.send_message(call.message.chat.id, "")
        bot.delete_message(call.message.chat.id, call.message.id + 1)

    elif call.data == 'class8' or call.data == 'class9' or call.data == 'class11' or call.data == 'class10':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{random.choice(begin_phrases)}")
        time.sleep(1.5)
        bot.delete_message(call.message.chat.id, call.message.id)
        inmarkup = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton("7 класс", callback_data='class7')
        button2 = types.InlineKeyboardButton("8 класс", callback_data='class8')
        button3 = types.InlineKeyboardButton("9 класс", callback_data='class9')
        button4 = types.InlineKeyboardButton("10 класс", callback_data='class10')
        button5 = types.InlineKeyboardButton("11 класс", callback_data='class11')
        inmarkup.add(button1, button2, button3, button4, button5)

        bot.send_message(call.message.chat.id, "Выберите свой класс:",
                         reply_markup=inmarkup)

#Залы для 7 класса
@bot.callback_query_handler(lambda call: call.data in ['hall_1', 'hall_2', 'hall_3', 'hall_4', 'hall_5', 'hall_6'])
def callback_inline_author(call):
    if call.data == 'hall_1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Предоставляется историческая справка...")
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Справка:")
        inmarkup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Далее', callback_data='spravka_1')
        inmarkup.add(button)
        bot.send_message(call.message.chat.id, hall_2, reply_markup=inmarkup)

    if call.data == 'hall_2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Предоставляется историческая справка...")
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Справка:")
        inmarkup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Далее', callback_data='spravka_2')
        inmarkup.add(button)
        bot.send_message(call.message.chat.id, hall_5, reply_markup=inmarkup)

    if call.data == 'hall_3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Предоставляется историческая справка...")
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Справка:")
        inmarkup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Далее', callback_data='spravka_3')
        inmarkup.add(button)
        bot.send_message(call.message.chat.id, hall_4, reply_markup=inmarkup)

    if call.data == 'hall_4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Предоставляется историческая справка...")
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Справка:")
        inmarkup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Далее', callback_data='spravka_4')
        inmarkup.add(button)
        bot.send_message(call.message.chat.id, hall_3, reply_markup=inmarkup)

    if call.data == 'hall_5':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Предоставляется историческая справка...")
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Справка:")
        inmarkup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Далее', callback_data='spravka_5')
        inmarkup.add(button)
        bot.send_message(call.message.chat.id, hal_1, reply_markup=inmarkup)

    if call.data == 'hall_6':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Предоставляется историческая справка...")
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Справка:")
        inmarkup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Далее', callback_data='spravka_6')
        inmarkup.add(button)
        bot.send_message(call.message.chat.id, hall_6, reply_markup=inmarkup)

@bot.callback_query_handler(lambda call: call.data in ['spravka_1', 'spravka_2', 'spravka_3', 'spravka_4', 'spravka_5', 'spravka_6'])
def references(call):
    if call.data == 'spravka_1':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Перейти к вопросам 1 зала")
        markup.add(button1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, text='Нажмите на кнопку \n'\
                                                    '"Перейти к вопросам 1 зала", чтобы начать тест.',
                              parse_mode="html", reply_markup=markup)

    if call.data == 'spravka_2':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Перейти к вопросам 2 зала")
        markup.add(button1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, text='Нажмите на кнопку \n'\
                                                    '"Перейти к вопросам 2 зала", чтобы начать тест.',
                              parse_mode="html", reply_markup=markup)

    if call.data == 'spravka_3':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Перейти к вопросам 3 зала")
        markup.add(button1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, text='Нажмите на кнопку \n'\
                                                    '"Перейти к вопросам 3 зала", чтобы начать тест.',
                              parse_mode="html", reply_markup=markup)

    if call.data == 'spravka_4':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Перейти к вопросам 4 зала")
        markup.add(button1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, text='Нажмите на кнопку \n'\
                                                    '"Перейти к вопросам 4 зала", чтобы начать тест.',
                              parse_mode="html", reply_markup=markup)

    if call.data == 'spravka_5':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Перейти к вопросам 5 зала")
        markup.add(button1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, text='Нажмите на кнопку \n'\
                                                    '"Перейти к вопросам 5 зала", чтобы начать тест.',
                              parse_mode="html", reply_markup=markup)

    if call.data == 'spravka_6':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Перейти к вопросам 6 зала")
        markup.add(button1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, text='Нажмите на кнопку \n'\
                                                    '"Перейти к вопросам 6 зала", чтобы начать тест.',
                              parse_mode="html", reply_markup=markup)

#Вопросы первого зала
@bot.message_handler(func=lambda message: True)
def hall_1(message):
    if message.text == 'Далее':
        bot.delete_message(message.chat.id, message.id-1)
        inmarkup = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton("7 класс", callback_data='class7')
        button2 = types.InlineKeyboardButton("8 класс", callback_data='class8')
        button3 = types.InlineKeyboardButton("9 класс", callback_data='class9')
        button4 = types.InlineKeyboardButton("10 класс", callback_data='class10')
        button5 = types.InlineKeyboardButton("11 класс", callback_data='class11')
        inmarkup.add(button1, button2, button3, button4, button5)

        bot.send_message(message.chat.id, "Выберите свой класс:",
                         reply_markup=inmarkup)

#Вопросы 1 зала
    if message.text == 'Перейти к вопросам 1 зала':
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='km_1.1')
        button2 = types.InlineKeyboardButton('2', callback_data='km_1.2')
        button3 = types.InlineKeyboardButton('3', callback_data='km_1.3')
        button4 = types.InlineKeyboardButton('4', callback_data='km_1.4')
        inmarkup.add(button1, button2, button3, button4)
        pic = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\номер 7.png", 'rb')
        bot.send_photo(message.chat.id, pic)
        bot.send_message(message.chat.id, qwe_1, reply_markup=inmarkup)

#Вопросы 2 зала
    if message.text == 'Перейти к вопросам 2 зала':
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_1.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_1.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_1.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_1.4')
        inmarkup.add(button1, button2, button3, button4)
        pic = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\_N11.png", 'rb')
        bot.send_photo(message.chat.id, pic)
        bot.send_message(message.chat.id, qwestio_1, reply_markup=inmarkup)

#Вопросы 3 зала
    if message.text == 'Перейти к вопросам 3 зала':
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='bl_1.1')
        button2 = types.InlineKeyboardButton('2', callback_data='bl_1.2')
        button3 = types.InlineKeyboardButton('3', callback_data='bl_1.3')
        button4 = types.InlineKeyboardButton('4', callback_data='bl_1.4')
        inmarkup.add(button1, button2, button3, button4)
        pic = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\N19_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)
        bot.send_message(message.chat.id, que_1, reply_markup=inmarkup)

#Вопросы 4 зала
    if message.text == 'Перейти к вопросам 4 зала':
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='kb_1.1')
        button2 = types.InlineKeyboardButton('2', callback_data='kb_1.2')
        button3 = types.InlineKeyboardButton('3', callback_data='kb_1.3')
        button4 = types.InlineKeyboardButton('4', callback_data='kb_1.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qwes_1, reply_markup=inmarkup)

#Вопросы 5 зала
    if message.text == 'Перейти к вопросам 5 зала':
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='fd_1.1')
        button2 = types.InlineKeyboardButton('2', callback_data='fd_1.2')
        button3 = types.InlineKeyboardButton('3', callback_data='fd_1.3')
        button4 = types.InlineKeyboardButton('4', callback_data='fd_1.4')
        inmarkup.add(button1, button2, button3, button4)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_132850_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)
        bot.send_message(message.chat.id, qw_1, reply_markup=inmarkup)

#Вопросы 6 зала
    if message.text == 'Перейти к вопросам 6 зала':
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_1.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_1.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_1.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_1.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, question_1, reply_markup=inmarkup)



@bot.callback_query_handler(lambda call: call.data in ['st_1.2', 'st_1.3', 'st_1.4', 'st_1.1', 'next_1',
                                                       'st_2.1', 'st_2.2', 'st_2.3', 'st_2.4', 'next_2',
                                                       'st_3.1', 'st_3.2', 'st_3.3', 'st_3.4', 'next_3',
                                                       'st_4.1', 'st_4.2', 'st_4.3', 'st_4.4', 'next_4',
                                                       'st_5.1', 'st_5.2', 'st_5.3', 'st_5.4', 'next_5',
                                                       'st_6.1', 'st_6.2', 'st_6.3', 'st_6.4', 'next_6',
                                                       'st_7.1', 'st_7.2', 'st_7.3', 'st_7.4', 'next_7',
                                                       'st_8.1', 'st_8.2', 'st_8.3', 'st_8.4', 'next_8',
                                                       'model_2'])
def the_battle_of_stalingrad(call):
    if call.data == 'st_1.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_1, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'st_1.2' or call.data == 'st_1.4' or call.data == 'st_1.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_1, parse_mode="html", reply_markup=inmarkup)

#Second question

    if call.data == 'next_1':
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_2.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_2.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_2.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_2.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwestio_2, reply_markup=inmarkup)

    if call.data == 'st_2.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_2, parse_mode="html", reply_markup=inmarkup)
        # markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        # button1 = types.KeyboardButton("/question_3")
        # markup.add(button1)
        # bot.send_message(call.message.chat.id, referen_3,
        #                  parse_mode="html", reply_markup=markup)

    if call.data == 'st_2.2' or call.data == 'st_2.3' or call.data == 'st_2.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_2, parse_mode="html", reply_markup=inmarkup)

#Third question

    if call.data == 'next_2':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_3.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_3.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_3.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_3.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        pic = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\номер 13_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(call.message.chat.id, pic)
        bot.send_message(call.message.chat.id, qwestio_3, reply_markup=inmarkup)

    if call.data == 'st_3.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_3, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'st_3.1' or call.data == 'st_3.3' or call.data == 'st_3.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_3, parse_mode="html", reply_markup=inmarkup)

#Fourth question

    if call.data == 'next_3':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_4.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_4.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_4.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_4.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        pic = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\номер 14_photo-resizer.ru.png",
                   'rb')
        bot.send_photo(call.message.chat.id, pic)
        bot.send_message(call.message.chat.id, qwestio_4, reply_markup=inmarkup)

    if call.data == 'st_4.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_4, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'st_4.1' or call.data == 'st_4.3' or call.data == 'st_4.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_4, parse_mode="html", reply_markup=inmarkup)

#Fifth question

    if call.data == 'next_4':
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_5.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_5.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_5.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_5.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwestio_5, reply_markup=inmarkup)

    if call.data == 'st_5.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_5, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'st_5.2' or call.data == 'st_5.3' or call.data == 'st_5.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_5, parse_mode="html", reply_markup=inmarkup)

#Sixth question

    if call.data == 'next_5':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_6.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_6.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_6.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_6.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwestio_6, reply_markup=inmarkup)

    if call.data == 'st_6.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_6')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_6, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'st_6.2' or call.data == 'st_6.1' or call.data == 'st_6.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_6')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refere_6, parse_mode="html", reply_markup=inmarkup)

#Seventh question

    if call.data == 'next_6':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='st_7.1')
        button2 = types.InlineKeyboardButton('2', callback_data='st_7.2')
        button3 = types.InlineKeyboardButton('3', callback_data='st_7.3')
        button4 = types.InlineKeyboardButton('4', callback_data='st_7.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwestio_7, reply_markup=inmarkup)

    if call.data == 'st_7.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q3 = 1
        c.append(q3)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_8")
        markup.add(button1)
        bot.send_message(call.message.chat.id, refere_7, parse_mode="html", reply_markup=markup)

    if call.data == 'st_7.2' or call.data == 'st_7.3' or call.data == 'st_7.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_8")
        markup.add(button1)
        bot.send_message(call.message.chat.id, refere_7, parse_mode="html", reply_markup=markup)

#Result

    if call.data == 'next_8':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        scores_3 = 0
        for x in c:
            scores_3 += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        procent = int((scores_3 / 8) * 100)
        names_2 = ''
        for i in name:
            names_2 = i
        if scores_3 == 1 or scores_3 == 0:
            c.clear()
            bot.send_message(call.message.chat.id,
                             f"{names_2}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_3} из 8 ({procent}%)\n"\
                             "\n"\
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)

        else:
            c.clear()
            inmarkup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Забрать модель', callback_data='model_2')
            inmarkup.add(button1)
            bot.send_message(call.message.chat.id,
                             f"{names_2}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_3} из 8 ({procent}%)\n"\
                             "\n"\
                             'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=inmarkup)

    if call.data == 'model_2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        photo = open(
            "C:\\Users\\artem\\Downloads\\ZlPtqnT0jZwFjkzfca68CMhhmefgMta73p4S9t6ycOiJi-4fT6CmRRBQVXWVKkbIunNbfUFLKJA70NWJz3oFVJOu_photo-resizer.ru.jpg",
            'rb')
        bot.send_photo(call.message.chat.id, photo, parse_mode="html", reply_markup=markup)


#Форсирование Днепра

@bot.callback_query_handler(lambda call: call.data in ['fd_1.2', 'fd_1.3', 'fd_1.4', 'fd_1.1', 'next_fd_1',
                                                       'fd_2.1', 'fd_2.2', 'fd_2.3', 'fd_2.4', 'next_fd_2',
                                                       'fd_3.1', 'fd_3.2', 'fd_3.3', 'fd_3.4', 'next_fd_3',
                                                        'fd_4.1', 'fd_4.2', 'fd_4.3', 'fd_4.4', 'next_fd_4',
                                                        'fd_5.1', 'fd_5.2', 'fd_5.3', 'fd_5.4', 'next_fd_5',
                                                       'model_1'
                                                       ])
def forcing_the_dnieper(call):
    if call.data == 'fd_1.1':
        bot.delete_message(call.message.chat.id, call.message.id-1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q1 = 1
        a.append(q1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_2")
        markup.add(button1)
        bot.send_message(call.message.chat.id, reference_1, parse_mode="html", reply_markup=markup)

    if call.data == 'fd_1.2' or call.data == 'fd_1.3' or call.data == 'fd_1.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_2")
        markup.add(button1)
        bot.send_message(call.message.chat.id, reference_1, parse_mode="html", reply_markup=markup)

#Third question

    if call.data == 'next_fd_2':
        bot.delete_message(call.message.chat.id, call.message.id - 4)
        bot.delete_message(call.message.chat.id, call.message.id - 3)
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='fd_3.1')
        button2 = types.InlineKeyboardButton('2', callback_data='fd_3.2')
        button3 = types.InlineKeyboardButton('3', callback_data='fd_3.3')
        button4 = types.InlineKeyboardButton('4', callback_data='fd_3.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qw_3, reply_markup=inmarkup)

    if call.data == 'fd_3.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q1 = 1
        a.append(q1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_fd_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, reference_3, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'fd_3.2' or call.data == 'fd_3.3' or call.data == 'fd_3.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_fd_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, reference_3, parse_mode="html", reply_markup=inmarkup)

#Fourth question

    if call.data == 'next_fd_3':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='fd_4.1')
        button2 = types.InlineKeyboardButton('2', callback_data='fd_4.2')
        button3 = types.InlineKeyboardButton('3', callback_data='fd_4.3')
        button4 = types.InlineKeyboardButton('4', callback_data='fd_4.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qw_4, reply_markup=inmarkup)

    if call.data == 'fd_4.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q1 = 1
        a.append(q1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_fd_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, reference_4, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'fd_4.2' or call.data == 'fd_4.3' or call.data == 'fd_4.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_fd_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, reference_4, parse_mode="html", reply_markup=inmarkup)

#Fifth question

    if call.data == 'next_fd_4':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='fd_5.1')
        button2 = types.InlineKeyboardButton('2', callback_data='fd_5.2')
        button3 = types.InlineKeyboardButton('3', callback_data='fd_5.3')
        button4 = types.InlineKeyboardButton('4', callback_data='fd_5.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qw_5, reply_markup=inmarkup)

    if call.data == 'fd_5.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q1 = 1
        a.append(q1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_fd_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, reference_5, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'fd_5.2' or call.data == 'fd_5.3' or call.data == 'fd_5.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_fd_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, reference_5, parse_mode="html", reply_markup=inmarkup)

#Result

    if call.data == 'next_fd_5':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        score = 0
        for x in a:
            score += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        procent = int((score/5)*100)
        names = ''
        for i in name:
            names = i
        if score == 1:
            a.clear()
            bot.send_message(call.message.chat.id,
                             f"{names}, спасибо за тестирование!\n"\
                            "🎇\n"\
                            f"Правильных ответов {score} из 5 ({procent}%)\n"\
                             "\n"\
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)

        elif score == 0:
            a.clear()
            bot.send_message(call.message.chat.id,
                             f"{names}, спасибо за тестирование!\n" \
                             "🎇\n" \
                            f"Правильных ответов {score} из 5 ({procent}%)\n" \
                             "\n" \
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)
        else:
            a.clear()
            inmarkup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Забрать модель', callback_data='model_1')
            inmarkup.add(button1)
            bot.send_message(call.message.chat.id,
                             f"{names}, спасибо за тестирование!\n" \
                             "🎇\n" \
                            f"Правильных ответов {score} из 5 ({procent}%)\n" \
                             "\n" \
                             'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=inmarkup)

    if call.data == 'model_1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        photo = open(
            "C:\\Users\\artem\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\святой_photo-resizer.ru (1).jpg",
            'rb')
        bot.send_photo(call.message.chat.id, photo, parse_mode="html", reply_markup=markup)
        text = '<a href="https://drive.google.com/drive/folders/15wXgUK2ToNRKmbTPTbJ4rAnEofSyeVMM?usp=sharing">Церковь</a>'
        bot.send_message(call.message.chat.id, text, parse_mode='HTML')

#Контрнаступление под Москвой

@bot.callback_query_handler(lambda call: call.data in ['km_1.2', 'km_1.3', 'km_1.4', 'km_1.1', 'next_km_1',
                                                       'km_2.1', 'km_2.2', 'km_2.3', 'km_2.4', 'next_km_2',
                                                       'km_3.1', 'km_3.2', 'km_3.3', 'km_3.4', 'next_km_3',
                                                       'km_4.1', 'km_4.2', 'km_4.3', 'km_4.4', 'next_km_4',
                                                       'model_9'
                                                       ])
def counteroffensive_near_moscow(call):
    if call.data == 'km_1.4':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q2 = 1
        b.append(q2)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_km_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_1, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'km_1.2' or call.data == 'km_1.1' or call.data == 'km_1.3':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_km_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_1, parse_mode="html", reply_markup=inmarkup)

#Second question

    if call.data == 'next_km_1':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='km_2.1')
        button2 = types.InlineKeyboardButton('2', callback_data='km_2.2')
        button3 = types.InlineKeyboardButton('3', callback_data='km_2.3')
        button4 = types.InlineKeyboardButton('4', callback_data='km_2.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwe_2, reply_markup=inmarkup)

    if call.data == 'km_2.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q2 = 1
        b.append(q2)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_km_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_2, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'km_2.2' or call.data == 'km_2.1' or call.data == 'km_2.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_km_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_2, parse_mode="html", reply_markup=inmarkup)

# Third question

    if call.data == 'next_km_2':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='km_3.1')
        button2 = types.InlineKeyboardButton('2', callback_data='km_3.2')
        button3 = types.InlineKeyboardButton('3', callback_data='km_3.3')
        button4 = types.InlineKeyboardButton('4', callback_data='km_3.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwe_3, reply_markup=inmarkup)

    if call.data == 'km_3.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q2 = 1
        b.append(q2)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_km_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_3, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'km_3.2' or call.data == 'km_3.3' or call.data == 'km_3.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_km_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_3, parse_mode="html", reply_markup=inmarkup)

# Fourth question

    if call.data == 'next_km_3':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='km_4.1')
        button2 = types.InlineKeyboardButton('2', callback_data='km_4.2')
        button3 = types.InlineKeyboardButton('3', callback_data='km_4.3')
        button4 = types.InlineKeyboardButton('4', callback_data='km_4.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwe_4, reply_markup=inmarkup)

    if call.data == 'km_4.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q2 = 1
        b.append(q2)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_km_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_4, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'km_4.2' or call.data == 'km_4.3' or call.data == 'km_4.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Подвести итог', callback_data='next_km_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, referen_4, parse_mode="html", reply_markup=inmarkup)

# Result

    if call.data == 'next_km_4':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        scores = 0
        for x in b:
            scores += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        procent = int((scores / 4) * 100)
        names_1 = ''
        for i in name:
            names_1 = i
        if scores == 1:
            b.clear()
            bot.send_message(call.message.chat.id,
                             f"{names_1}, спасибо за тестирование!\n" \
                             "🎇\n" \
                             f"Правильных ответов {scores} из 4 ({procent}%)\n" \
                             "\n" \
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)

        elif scores == 0:
            b.clear()
            bot.send_message(call.message.chat.id,
                             f"{names_1}, спасибо за тестирование!\n" \
                             "🎇\n" \
                             f"Правильных ответов {scores} из 4 ({procent}%)\n" \
                             "\n" \
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)
        else:
            b.clear()
            inmarkup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Забрать модель', callback_data='model_9')
            inmarkup.add(button1)
            bot.send_message(call.message.chat.id,
                             f"{names_1}, спасибо за тестирование!\n" \
                             "🎇\n" \
                             f"Правильных ответов {scores} из 4 ({procent}%)\n" \
                             "\n" \
                             'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=inmarkup)

    if call.data == 'model_9':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        photo = open(
            "C:\\Users\\artem\\Downloads\\ZlPtqnT0jZwFjkzfca68CMhhmefgMta73p4S9t6ycOiJi-4fT6CmRRBQVXWVKkbIunNbfUFLKJA70NWJz3oFVJOu_photo-resizer.ru.jpg",
            'rb')
        bot.send_photo(call.message.chat.id, photo, parse_mode="html", reply_markup=markup)
        text = '<a href="https://drive.google.com/drive/folders/1nffg20DnE-o8X7XwMLmHl2baAiQkSMPv?usp=sharing">Пушка</a>'
        bot.send_message(call.message.chat.id, text, parse_mode='HTML')

#Штурм Берлина

@bot.callback_query_handler(lambda call: call.data in ['sb_1.2', 'sb_1.3', 'sb_1.4', 'sb_1.1', 'next_sb_1',
                                                       'sb_2.1', 'sb_2.2', 'sb_2.3', 'sb_2.4', 'next_sb_2',
                                                       'sb_3.1', 'sb_3.2', 'sb_3.3', 'sb_3.4', 'next_sb_3',
                                                       'sb_4.1', 'sb_4.2', 'sb_4.3', 'sb_4.4', 'next_sb_4',
                                                       'sb_5.1', 'sb_5.2', 'sb_5.3', 'sb_5.4', 'next_sb_5',
                                                       'sb_6.1', 'sb_6.2', 'sb_6.3', 'sb_6.4', 'next_sb_6',
                                                       'sb_7.1', 'sb_7.2', 'sb_7.3', 'sb_7.4', 'next_sb_7',
                                                       'sb_8.1', 'sb_8.2', 'sb_8.3', 'sb_8.4', 'next_sb_8',
                                                        'sb_9.1', 'sb_9.2', 'sb_9.3', 'sb_9.4', 'next_sb_9',
                                                       'sb_10.1', 'sb_10.2', 'sb_10.3', 'sb_10.4', 'next_sb_10',
                                                       'sb_11.1', 'sb_11.2', 'sb_11.3', 'sb_11.4', 'next_sb_11',
                                                       'sb_12.1', 'sb_12.2', 'sb_12.3', 'sb_12.4', 'next_sb_12',
                                                       'model_6'])
def storming_berlin(call):
    if call.data == 'sb_1.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_1, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_1.1' or call.data == 'sb_1.4' or call.data == 'sb_1.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_1, parse_mode="html", reply_markup=inmarkup)

#Second question

    if call.data == 'next_sb_1':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_2.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_2.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_2.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_2.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_2, reply_markup=inmarkup)

    if call.data == 'sb_2.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_2, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_2.2' or call.data == 'sb_2.3' or call.data == 'sb_2.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_2, parse_mode="html", reply_markup=inmarkup)

#Third question

    if call.data == 'next_sb_2':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_3.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_3.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_3.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_3.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_3, reply_markup=inmarkup)

    if call.data == 'sb_3.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_3, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_3.2' or call.data == 'sb_3.3' or call.data == 'sb_3.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_3, parse_mode="html", reply_markup=inmarkup)

#Fourth question

    if call.data == 'next_sb_3':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_4.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_4.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_4.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_4.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_4, reply_markup=inmarkup)

    if call.data == 'sb_4.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_4, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_4.2' or call.data == 'sb_4.3' or call.data == 'sb_4.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_4, parse_mode="html", reply_markup=inmarkup)

#Fifth question

    if call.data == 'next_sb_4':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_5.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_5.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_5.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_5.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_5, reply_markup=inmarkup)

    if call.data == 'sb_5.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_5, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_5.2' or call.data == 'sb_5.3' or call.data == 'sb_5.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_5, parse_mode="html", reply_markup=inmarkup)

#Sixth question

    if call.data == 'next_sb_5':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_6.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_6.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_6.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_6.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_6, reply_markup=inmarkup)

    if call.data == 'sb_6.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_6')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_6, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_6.2' or call.data == 'sb_6.3' or call.data == 'sb_6.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_6')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_6, parse_mode="html", reply_markup=inmarkup)

#Seventh question

    if call.data == 'next_sb_6':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_7.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_7.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_7.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_7.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_7, reply_markup=inmarkup)

    if call.data == 'sb_7.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_7')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_7, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_7.2' or call.data == 'sb_7.3' or call.data == 'sb_7.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_7')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_7, parse_mode="html", reply_markup=inmarkup)

#Eighth question

    if call.data == 'next_sb_7':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_8.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_8.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_8.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_8.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_8, reply_markup=inmarkup)

    if call.data == 'sb_8.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_8')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_8, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_8.2' or call.data == 'sb_8.3' or call.data == 'sb_8.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_8')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_8, parse_mode="html", reply_markup=inmarkup)

#Ninth question

    if call.data == 'next_sb_8':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_9.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_9.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_9.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_9.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_9, reply_markup=inmarkup)

    if call.data == 'sb_9.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_9')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_9, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_9.2' or call.data == 'sb_9.3' or call.data == 'sb_9.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_9')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_9, parse_mode="html", reply_markup=inmarkup)

#Tenth question

    if call.data == 'next_sb_9':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_10.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_10.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_10.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_10.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_10, reply_markup=inmarkup)

    if call.data == 'sb_10.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_10')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_10, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'sb_10.1' or call.data == 'sb_10.3' or call.data == 'sb_10.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_sb_10')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, r_10, parse_mode="html", reply_markup=inmarkup)

#Eleventh question

    if call.data == 'next_sb_10':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='sb_11.1')
        button2 = types.InlineKeyboardButton('2', callback_data='sb_11.2')
        button3 = types.InlineKeyboardButton('3', callback_data='sb_11.3')
        button4 = types.InlineKeyboardButton('4', callback_data='sb_11.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, question_11, reply_markup=inmarkup)

    if call.data == 'sb_11.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Поздравляю, это правильный ответ!")
        q6 = 1
        f.append(q6)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_12")
        markup.add(button1)
        bot.send_message(call.message.chat.id, r_11, parse_mode="html", reply_markup=markup)

    if call.data == 'st_11.1' or call.data == 'st_11.3' or call.data == 'st_11.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_12")
        markup.add(button1)
        bot.send_message(call.message.chat.id, r_11, parse_mode="html", reply_markup=markup)

#Result

    if call.data == 'next_sb_12':
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        scores_6 = 0
        for x in f:
            scores_6 += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        procent = int((scores_6 / 12) * 100)
        names_6 = ''
        for i in name:
            names_6 = i
        if scores_6 == 1 or scores_6 == 0:
            f.clear()
            bot.send_message(call.message.chat.id,
                             f"{names_6}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_6} из 12 ({procent}%)\n"\
                             "\n"\
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)

        else:
            f.clear()
            inmarkup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Забрать модель', callback_data='model_6')
            inmarkup.add(button1)
            bot.send_message(call.message.chat.id,
                             f"{names_6}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_6} из 12 ({procent}%)\n"\
                             "\n"\
                             'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=inmarkup)

    if call.data == 'model_6':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        photo = open(
            "C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\шашка_photo-resizer.ru.png",
            'rb')
        bot.send_photo(call.message.chat.id, photo, parse_mode="html", reply_markup=markup)
        text = '<a href="https://drive.google.com/drive/folders/1Vx3rkAr3DZ3r9cx6HwnkP2-T1p87KQl2?usp=sharing">Шашка</a>'
        bot.send_message(call.message.chat.id, text, parse_mode='HTML')

#Блокада Ленинграда
@bot.callback_query_handler(lambda call: call.data in ['bl_1.2', 'bl_1.3', 'bl_1.4', 'bl_1.1', 'next_bl_1',
                                                       'bl_2.1', 'bl_2.2', 'bl_2.3', 'bl_2.4', 'next_bl_2',
                                                       'bl_3.1', 'bl_3.2', 'bl_3.3', 'bl_3.4', 'next_bl_3',
                                                       'bl_4.1', 'bl_4.2', 'bl_4.3', 'bl_4.4', 'next_bl_4',
                                                       'bl_5.1', 'bl_5.2', 'bl_5.3', 'bl_5.4', 'next_bl_5',
                                                       'bl_6.1', 'bl_6.2', 'bl_6.3', 'bl_6.4', 'next_bl_6',
                                                       'bl_7.1', 'bl_7.2', 'bl_7.3', 'bl_7.4', 'next_bl_7',
                                                       'model_12'])
def storming_berlin(call):
    if call.data == 'bl_1.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_1, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'bl_1.1' or call.data == 'bl_1.4' or call.data == 'bl_1.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_1, parse_mode="html", reply_markup=inmarkup)

#Second question

    if call.data == 'next_bl_1':
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='bl_2.1')
        button2 = types.InlineKeyboardButton('2', callback_data='bl_2.2')
        button3 = types.InlineKeyboardButton('3', callback_data='bl_2.3')
        button4 = types.InlineKeyboardButton('4', callback_data='bl_2.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, que_2, reply_markup=inmarkup)

    if call.data == 'bl_2.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_2, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'bl_2.2' or call.data == 'bl_2.3' or call.data == 'bl_2.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_2, parse_mode="html", reply_markup=inmarkup)

#Third question

    if call.data == 'next_bl_2':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='bl_3.1')
        button2 = types.InlineKeyboardButton('2', callback_data='bl_3.2')
        button3 = types.InlineKeyboardButton('3', callback_data='bl_3.3')
        button4 = types.InlineKeyboardButton('4', callback_data='bl_3.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        photo = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\N21_photo-resizer.ru.jpg",'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id, que_3, reply_markup=inmarkup)

    if call.data == 'bl_3.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_3, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'bl_3.1' or call.data == 'bl_3.3' or call.data == 'bl_3.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_3, parse_mode="html", reply_markup=inmarkup)

#Fourth question

    if call.data == 'next_bl_3':
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='bl_4.1')
        button2 = types.InlineKeyboardButton('2', callback_data='bl_4.2')
        button3 = types.InlineKeyboardButton('3', callback_data='bl_4.3')
        button4 = types.InlineKeyboardButton('4', callback_data='bl_4.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, que_4, reply_markup=inmarkup)

    if call.data == 'bl_4.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_4, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'bl_4.2' or call.data == 'bl_4.3' or call.data == 'bl_4.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_4')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_4, parse_mode="html", reply_markup=inmarkup)

#Fifth question

    if call.data == 'next_bl_4':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='bl_5.1')
        button2 = types.InlineKeyboardButton('2', callback_data='bl_5.2')
        button3 = types.InlineKeyboardButton('3', callback_data='bl_5.3')
        button4 = types.InlineKeyboardButton('4', callback_data='bl_5.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, que_5, reply_markup=inmarkup)

    if call.data == 'bl_5.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_5, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'bl_5.2' or call.data == 'bl_5.3' or call.data == 'bl_5.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_bl_5')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, ref_5, parse_mode="html", reply_markup=inmarkup)

#Sixth question

    if call.data == 'next_bl_5':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='bl_6.1')
        button2 = types.InlineKeyboardButton('2', callback_data='bl_6.2')
        button3 = types.InlineKeyboardButton('3', callback_data='bl_6.3')
        button4 = types.InlineKeyboardButton('4', callback_data='bl_6.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, que_6, reply_markup=inmarkup)

    if call.data == 'bl_6.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q7 = 1
        d.append(q7)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_7")
        markup.add(button1)
        bot.send_message(call.message.chat.id, ref_6, parse_mode="html", reply_markup=markup)

    if call.data == 'bl_6.2' or call.data == 'bl_6.3' or call.data == 'bl_6.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_7")
        markup.add(button1)
        bot.send_message(call.message.chat.id, ref_6, parse_mode="html", reply_markup=markup)

#Result

    if call.data == 'next_bl_6':
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        scores_4 = 0
        for x in d:
            scores_4 += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        procent = int((scores_4 / 7) * 100)
        names_4 = ''
        for i in name:
            names_4 = i
        if scores_4 == 1 or scores_4 == 0:
            d.clear()
            bot.send_message(call.message.chat.id,
                             f"{names_4}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_4} из 7 ({procent}%)\n"\
                             "\n"\
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)

        else:
            d.clear()
            inmarkup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Забрать модель', callback_data='model_12')
            inmarkup.add(button1)
            bot.send_message(call.message.chat.id,
                             f"{names_4}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_4} из 7 ({procent}%)\n"\
                             "\n"\
                             'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=inmarkup)

    if call.data == 'model_12':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        photo = open(
            "C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\реал_меч____photo-resizer.ru.jpg",
            'rb')
        bot.send_photo(call.message.chat.id, photo, parse_mode="html", reply_markup=markup)
        text = '<a href="https://drive.google.com/drive/folders/1pijw2_yhzTUXQc6FqT-u6L1N2Io1LoZm?usp=sharing">Меч</a>'
        bot.send_message(call.message.chat.id, text, parse_mode='HTML')

#Курская битва

@bot.callback_query_handler(lambda call: call.data in ['kb_1.2', 'kb_1.3', 'kb_1.4', 'kb_1.1', 'next_kb_1',
                                                       'kb_2.1', 'kb_2.2', 'kb_2.3', 'kb_2.4', 'next_kb_2',
                                                       'kb_3.1', 'kb_3.2', 'kb_3.3', 'kb_3.4', 'next_kb_3',
                                                       'kb_4.1', 'kb_4.2', 'kb_4.3', 'kb_4.4', 'next_kb_4',
                                                       'kb_5.1', 'kb_5.2', 'kb_5.3', 'kb_5.4', 'next_kb_5',
                                                       'kb_6.1', 'kb_6.2', 'kb_6.3', 'kb_6.4', 'next_kb_6',
                                                       'model_5'])
def storming_berlin(call):
    if call.data == 'kb_1.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q9 = 1
        e.append(q9)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_kb_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refe_1, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'kb_1.1' or call.data == 'kb_1.4' or call.data == 'kb_1.2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_kb_1')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refe_1, parse_mode="html", reply_markup=inmarkup)

#Second question

    if call.data == 'next_kb_1':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='kb_2.1')
        button2 = types.InlineKeyboardButton('2', callback_data='kb_2.2')
        button3 = types.InlineKeyboardButton('3', callback_data='kb_2.3')
        button4 = types.InlineKeyboardButton('4', callback_data='kb_2.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwes_2, reply_markup=inmarkup)

    if call.data == 'kb_2.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q9 = 1
        e.append(q9)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_kb_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refe_2, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'kb_2.2' or call.data == 'kb_2.3' or call.data == 'kb_2.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_kb_2')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refe_2, parse_mode="html", reply_markup=inmarkup)

#Third question

    if call.data == 'next_kb_2':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='kb_3.1')
        button2 = types.InlineKeyboardButton('2', callback_data='kb_3.2')
        button3 = types.InlineKeyboardButton('3', callback_data='kb_3.3')
        button4 = types.InlineKeyboardButton('4', callback_data='kb_3.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, qwes_3, reply_markup=inmarkup)

    if call.data == 'kb_3.1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q9 = 1
        e.append(q9)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_kb_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refe_3, parse_mode="html", reply_markup=inmarkup)

    if call.data == 'kb_3.2' or call.data == 'kb_3.3' or call.data == 'kb_3.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="К сожалению, это неправильный ответ")
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Следующий вопрос', callback_data='next_kb_3')
        inmarkup.add(button1)
        bot.send_message(call.message.chat.id, refe_3, parse_mode="html", reply_markup=inmarkup)

#Fourth question

    if call.data == 'next_kb_3':
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        inmarkup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1', callback_data='kb_4.1')
        button2 = types.InlineKeyboardButton('2', callback_data='kb_4.2')
        button3 = types.InlineKeyboardButton('3', callback_data='kb_4.3')
        button4 = types.InlineKeyboardButton('4', callback_data='kb_4.4')
        inmarkup.add(button1, button2, button3, button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        photo = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\N30_photo-resizer.ru.jpg",'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id, qwes_4, reply_markup=inmarkup)

    if call.data == 'kb_4.4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Поздравляю, это правильный ответ!")
        q9 = 1
        e.append(q9)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_5")
        markup.add(button1)
        bot.send_message(call.message.chat.id, refe_4, parse_mode="html", reply_markup=markup)

    if call.data == 'kb_4.1' or call.data == 'kb_4.2' or call.data == 'kb_4.3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="К сожалению, это неправильный ответ")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/Вопрос_5")
        markup.add(button1)
        bot.send_message(call.message.chat.id, refe_4, parse_mode="html", reply_markup=markup)

#Result

    if call.data == 'next_kb_6':
        bot.delete_message(call.message.chat.id, call.message.id - 3)
        bot.delete_message(call.message.chat.id, call.message.id - 2)
        bot.delete_message(call.message.chat.id, call.message.id - 1)
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        scores_9 = 0
        for x in e:
            scores_9 += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        procent = int((scores_9 / 6) * 100)
        names_9 = ''
        for i in name:
            names_9 = i
        if scores_9 == 1 or scores_9 == 0:
            e.clear()
            bot.send_message(call.message.chat.id,
                             f"{names_9}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_9} из 6 ({procent}%)\n"\
                             "\n"\
                             'К сожалению, вам не хватило баллов, чтобы получить 3Д модель. Попробуйте снова!',
                             parse_mode="html", reply_markup=markup)

        else:
            d.clear()
            inmarkup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Забрать модель', callback_data='model_5')
            inmarkup.add(button1)
            bot.send_message(call.message.chat.id,
                             f"{names_9}, спасибо за тестирование!\n"\
                             "🎇\n"\
                             f"Правильных ответов {scores_9} из 6 ({procent}%)\n"\
                             "\n"\
                             'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=inmarkup)

    if call.data == 'model_5':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="-")
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        photo = open(
            "C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\\танк_photo-resizer.ru.png",
            'rb')
        bot.send_photo(call.message.chat.id, photo, parse_mode="html", reply_markup=markup)
        text = '<a href="https://drive.google.com/drive/folders/1VCAGht-kWN8svitGIm0y-izNDyErzqFG?usp=sharing">Танк</a>'
        bot.send_message(call.message.chat.id, text, parse_mode='HTML')
bot.polling(none_stop=True)

