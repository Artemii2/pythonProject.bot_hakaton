    if message.text == 'Перейти к вопросам 1 зала':
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("1")
        button2 = types.KeyboardButton("2")
        button3 = types.KeyboardButton("3")
        button4 = types.KeyboardButton("4")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qw_1,
                         parse_mode="html", reply_markup=markup)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_132850_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)
    if message.text == '1':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q1 = 1
        a.append(q1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 2")
        markup.add(button1)
        msg = bot.send_message(message.chat.id, reference_1,
                             parse_mode="html", reply_markup=markup)

    elif message.text == '2' or message.text == '3' or message.text == '4':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 2")
        markup.add(button1)
        msg = bot.send_message(message.chat.id, reference_1,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'Вопрос 2':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("13")
        button2 = types.KeyboardButton("50")
        button3 = types.KeyboardButton("75")
        button4 = types.KeyboardButton("40")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qw_2,
                         parse_mode="html", reply_markup=markup)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_133220_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)

    if message.text == '13':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q1 = 1
        a.append(q1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 3")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_2,
                             parse_mode="html", reply_markup=markup)

    elif message.text == '75' or message.text == '40' or message.text == '50':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 3")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_2,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'Вопрос 3':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("otvet 1 ")
        button2 = types.KeyboardButton("otvet 2")
        button3 = types.KeyboardButton("otvet 3")
        button4 = types.KeyboardButton("otvet 4")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qw_3,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'otvet 3':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q1 = 1
        a.append(q1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 4")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_3,
                             parse_mode="html", reply_markup=markup)

    elif message.text == 'otvet 2' or message.text == 'otvet 1' or message.text == 'otvet 4':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 4")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_3,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'Вопрос 4':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("такой-то...")
        button2 = types.KeyboardButton("такой")
        button3 = types.KeyboardButton("5")
        button4 = types.KeyboardButton("6")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qw_4,
                         parse_mode="html", reply_markup=markup)

    if message.text == '5':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q1 = 1
        a.append(q1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 5")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_4,
                             parse_mode="html", reply_markup=markup)

    elif message.text == 'такой-то...' or message.text == 'такой' or message.text == '6':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Вопрос 5")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_4,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'Вопрос 5':
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("первое")
        button2 = types.KeyboardButton("второе")
        button3 = types.KeyboardButton("третье")
        button4 = types.KeyboardButton("четвёртое")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qw_5,
                         parse_mode="html", reply_markup=markup)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_132854_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)

    if message.text == 'первое':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q1 = 1
        a.append(q1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Подвести итог")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_5,
                         parse_mode="html", reply_markup=markup)

    elif message.text == 'второе' or message.text == 'третье' or message.text == 'четвёртое':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Подвести итог")
        markup.add(button1)
        bot.send_message(message.chat.id, reference_5,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'Подвести итог':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        score = 0
        for i in a:
            score += i
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        if score == 1:
            a.clear()
            bot.send_message(message.chat.id, f' {score} набранный баллов из 5',
                             parse_mode="html", reply_markup=markup)
            # sti = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\sticker.webp", 'rb')
            # bot.send_sticker(message.chat.id, sti)
            time.sleep(1)
            bot.send_message(message.chat.id, f'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=markup)
            photo = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\A29118KODaW-7wipJfxasm6wQBfr5JS6X-ipzcnyW_hR63VrV-WLpvXom0rRBKEhA_9odMk58v1PK0MWnqkZL2__ (1).jpg",
                'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            a.clear()
            bot.send_message(message.chat.id, f' {score} набранных баллов из 5',
                             parse_mode="html", reply_markup=markup)
            # sti = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\sticker.webp", 'rb')
            # bot.send_sticker(message.chat.id, sti)
            time.sleep(1)
            bot.send_message(message.chat.id, f'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=markup)
            photo = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\ДАЙ БОГ ЭТОМУ ХАКАТОНУ\A29118KODaW-7wipJfxasm6wQBfr5JS6X-ipzcnyW_hR63VrV-WLpvXom0rRBKEhA_9odMk58v1PK0MWnqkZL2__ (1).jpg",
                'rb')
            bot.send_photo(message.chat.id, photo)

#Вопросы второго зала
    if message.text == 'Перейти к вопросам 2 зала':
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("1️⃣")
        button2 = types.KeyboardButton("2️⃣")
        button3 = types.KeyboardButton("3️⃣")
        button4 = types.KeyboardButton("4️⃣")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qwe_1,
                         parse_mode="html", reply_markup=markup)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_124807_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)

    if message.text == '4️⃣':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q2 = 1
        b.append(q2)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("2-й вопрос")
        markup.add(button1)
        msg = bot.send_message(message.chat.id, referen_1,
                             parse_mode="html", reply_markup=markup)

    elif message.text == '2️⃣' or message.text == '3️⃣' or message.text == '1️⃣':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("2-й вопрос")
        markup.add(button1)
        msg = bot.send_message(message.chat.id, referen_1,
                         parse_mode="html", reply_markup=markup)

    if message.text == '2-й вопрос':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Данилов")
        button2 = types.KeyboardButton("Петровский")
        button3 = types.KeyboardButton("Бочкарев")
        button4 = types.KeyboardButton("Данилевский")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qwe_2,
                         parse_mode="html", reply_markup=markup)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_124807_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)

    if message.text == 'Данилевский':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q2 = 1
        b.append(q2)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("3-й вопрос")
        markup.add(button1)
        bot.send_message(message.chat.id, referen_2,
                             parse_mode="html", reply_markup=markup)

    elif message.text == 'Данилов' or message.text == 'Петровский' or message.text == 'Бочкарев':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("3-й вопрос")
        markup.add(button1)
        bot.send_message(message.chat.id, referen_2,
                         parse_mode="html", reply_markup=markup)

    if message.text == '3-й вопрос':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Раменки")
        button2 = types.KeyboardButton("Котельники")
        button3 = types.KeyboardButton("Город Клин")
        button4 = types.KeyboardButton("Яхрома")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qwe_3,
                         parse_mode="html", reply_markup=markup)
        pic = open("C:\\Users\\artem\\Downloads\\IMG_20220411_124807_photo-resizer.ru.jpg", 'rb')
        bot.send_photo(message.chat.id, pic)

    if message.text == 'Яхрома':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q2 = 1
        b.append(q2)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("4-й вопрос")
        markup.add(button1)
        bot.send_message(message.chat.id, referen_3,
                             parse_mode="html", reply_markup=markup)

    elif message.text == 'Раменки' or message.text == 'Котельники' or message.text == 'Город Клин':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("4-й вопрос")
        markup.add(button1)
        bot.send_message(message.chat.id, referen_3,
                         parse_mode="html", reply_markup=markup)

    if message.text == '4-й вопрос':
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Введите номер ответа:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("220 км")
        button2 = types.KeyboardButton("250 км")
        button3 = types.KeyboardButton("100 км")
        button4 = types.KeyboardButton("220 м")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, qwe_4,
                         parse_mode="html", reply_markup=markup)

    if message.text == '220 км':
        bot.send_message(message.chat.id, 'Правильный ответ')
        q2 = 1
        b.append(q2)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Показать результат")
        markup.add(button1)
        bot.send_message(message.chat.id, referen_4,
                             parse_mode="html", reply_markup=markup)

    elif message.text == '250 км' or message.text == '100 км' or message.text == '220 м':
        bot.send_message(message.chat.id, 'Неправильный ответ')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Показать результат")
        markup.add(button1)
        bot.send_message(message.chat.id, referen_4,
                         parse_mode="html", reply_markup=markup)

    if message.text == 'Показать результат':
        bot.delete_message(message.chat.id, message.message_id - 1)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        scores = 0
        for x in b:
            scores += x
        button1 = types.KeyboardButton("/menu")
        markup.add(button1)
        if scores == 1:
            b.clear()
            bot.send_message(message.chat.id, f' {scores} набранный баллов из 4',
                             parse_mode="html", reply_markup=markup)
            # sti = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\sticker2.webp", 'rb')
            # bot.send_sticker(message.chat.id, sti)
            time.sleep(1)
            bot.send_message(message.chat.id, f'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=markup)
            photo = open("C:\\Users\\artem\\Downloads\\ZlPtqnT0jZwFjkzfca68CMhhmefgMta73p4S9t6ycOiJi-4fT6CmRRBQVXWVKkbIunNbfUFLKJA70NWJz3oFVJOu_photo-resizer.ru.jpg",'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            b.clear()
            bot.send_message(message.chat.id, f' {scores} набранных баллов из 4',
                             parse_mode="html", reply_markup=markup)
            # sti = open("C:\\Users\\artem\\OneDrive\\Рабочий стол\\sticker2.webp", 'rb')
            # bot.send_sticker(message.chat.id, sti)
            time.sleep(1)
            bot.send_message(message.chat.id, f'Вы выиграли эту замечательную 3D модель!',
                             parse_mode="html", reply_markup=markup)
            photo = open("C:\\Users\\artem\\Downloads\\ZlPtqnT0jZwFjkzfca68CMhhmefgMta73p4S9t6ycOiJi-4fT6CmRRBQVXWVKkbIunNbfUFLKJA70NWJz3oFVJOu_photo-resizer.ru.jpg", 'rb')
            bot.send_photo(message.chat.id, photo)