import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('8188856331:AAEClLW5DNEWunRcwZuYNACG8131U6U1do0', parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message):
    knop = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('🤠 Начать тест')
    knop.add(btn1)
    bot.send_message(message.chat.id, 'Данный бот поможет тебе подглядеть правильный вариант в билете экзамена!\n<b>*Правильный ответ подчеркнут</b>', reply_markup=knop)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    markups = types.InlineKeyboardMarkup()
    btns1 = types.InlineKeyboardButton('#1', callback_data='n1')
    btns2 = types.InlineKeyboardButton('#2', callback_data='n2')
    btns3 = types.InlineKeyboardButton('#3', callback_data='n3')
    btns4 = types.InlineKeyboardButton('#4', callback_data='n4')
    markups.row(btns1, btns2, btns3, btns4)
    if message.text == '🤠 Начать тест':
        bot.send_message(message.chat.id, 'Выберите номер билета:', reply_markup=markups)


@bot.callback_query_handler(func=lambda callback: callback.data == 'n1')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_1_2')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 1.\n"
                                               "В каком случае водитель совершит вынужденную остановку?\n\n"
                                               "1.Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу.\n"
                                               "<u>2.Остановившись на проезжей части из-за технической неисправности транспортного средства.</u>\n"
                                               "3. В обоих перечисленных случаях.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('3 воп.', callback_data='q_1_3')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_2.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 2 Билет 1.\n"
                                               "Разрешен ли Вам съезд на дорогу с грунтовым покрытием?\n\n"
                                               "<u>1. Разрешен.</u>\n"
                                               "2. Разрешен только при технической неисправности транспортного средства.\n"
                                               "3. Запрещен.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('4 воп.', callback_data='q_1_4')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_3.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 1.\n"
                                               "Можно ли Вам остановиться в указанном месте для посадки пассажира?\n\n"
                                               "<u>1. Можно.</u>\n"
                                               "2. Можно, если Вы управляете такси.\n"
                                               "3. Нельзя.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('5 воп.', callback_data='q_1_5')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_4.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 4 Билет 1.\n"
                                               "Какие из указанных знаков запрещают движение водителям мопедов?\n\n"
                                               "1. Только А.\n"
                                               "2. Только Б.\n"
                                               "3. В и Г.\n"
                                               "<u>4. Все.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('6 воп.', callback_data='q_1_6')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_5.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 5 Билет 1.\n"
                                               "Вы намерены повернуть налево. Где следует остановиться, чтобы уступить дорогу легковому автомобилю?\n\n"
                                               "1. Перед знаком.\n"
                                               "<u>2. Перед перекрестком у линии разметки.</u>\n"
                                               "3. На перекрестке перед прерывистой линией разметки.\n"
                                               "4. В любом месте по усмотрению водителя.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_6')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('7 воп.', callback_data='q_1_7')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 6 Билет 1.\n"
                                               "Что означает мигание зеленого сигнала светофора?\n\n"
                                               "1. Предупреждает о неисправности светофора.\n"
                                               "<u>2. Разрешает движение и информирует о том, что вскоре будет включен запрещающий сигнал.</u>\n"
                                               "3. Запрещает дальнейшее движение.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_7')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('8 воп.', callback_data='q_1_8')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 7 Билет 1.\n"
                                               "Водитель обязан подавать сигналы световыми указателями поворота (рукой):\n\n"
                                               "1. Перед началом движения или перестроением.\n"
                                               "2. Перед поворотом или разворотом.\n"
                                               "3. Перед остановкой.\n"
                                               "<u>4. Во всех перечисленных случаях.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_8')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('9 воп.', callback_data='q_1_9')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_8.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 8 Билет 1.\n"
                                               "Как Вам следует поступить при повороте направо?\n\n"
                                               "1. Перестроиться на правую полосу, затем осуществить поворот.\n"
                                               "2. Продолжить движение по второй полосе до перекрестка, затем повернуть.\n"
                                               "<u>3. Возможны оба варианта действий.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_9')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('10 воп.', callback_data='q_1_10')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_9.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 9 Билет 1.\n"
                                               "По какой траектории Вам разрешено выполнить разворот?\n\n"
                                               "<u>1. Только по А.</u>\n"
                                               "2. Только по Б.\n"
                                               "3. По любой из указанных.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_10')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('11 воп.', callback_data='q_1_11')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_10.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 10 Билет 1.\n"
                                               "С какой скоростью Вы можете продолжить движение вне населенного пункта по левой полосе на легковом автомобиле?\n\n"
                                               "1. Не более 50 км/ч.\n"
                                               "2. Не менее 50 км/ч и не более 70 км/ч.\n"
                                               "<u>3. Не менее 50 км/ч и не более 90 км/ч.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_11')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('12 воп.', callback_data='q_1_12')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_11.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 11 Билет 1.\n"
                                               "Можно ли водителю легкового автомобиля выполнить опережение грузовых автомобилей вне населенного пункта по такой траектории?\n\n"
                                               "<u>1. Можно.</u>\n"
                                               "2. Можно, если скорость грузовых автомобилей менее 30 км/ч.\n"
                                               "3. Нельзя.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_12')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('13 воп.', callback_data='q_1_13')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_12.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 12 Билет 1.\n"
                                               "В каком случае водителю разрешается поставить автомобиль на стоянку в указанном месте?\n\n"
                                               "1. Только если расстояние до сплошной линии разметки не менее 3 м.\n"
                                               "2. Только если расстояние до края пересекаемой проезжей части не менее 5 м.\n"
                                               "<u>3. При соблюдении обоих перечисленных условий.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_13')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('14 воп.', callback_data='q_1_14')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_13.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 13 Билет 1.\n"
                                               "При повороте направо Вы должны уступить дорогу:\n\n"
                                               "1. Только велосипедисту.\n"
                                               "2. Только пешеходам.\n"
                                               "<u>3. Пешеходам и велосипедисту.</u>\n"
                                               "4. Никому.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_14')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('15 воп.', callback_data='q_1_15')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_14.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 14 Билет 1.\n"
                                               "Вы намерены проехать перекресток в прямом направлении. Кому Вы должны уступить дорогу?\n\n"
                                               "<u>1. Обоим трамваям.</u>\n"
                                               "2. Только трамваю А.\n"
                                               "3. Только трамваю Б.\n"
                                               "4. Никому.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_15')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('16 воп.', callback_data='q_1_16')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_15.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 15 Билет 1.\n"
                                               "Кому Вы обязаны уступить дорогу при повороте налево?\n\n"
                                               "1. Только автобусу.\n"
                                               "2. Только легковому автомобилю.\n"
                                               "<u>3. Никому.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_16')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('17 воп.', callback_data='q_1_17')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_16.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 16 Билет 1.\n"
                                               "С какой максимальной скоростью можно продолжить движение за знаком?\n\n"
                                               "1. 60 км/ч.\n"
                                               "2. 50 км/ч.\n"
                                               "3. 30 км/ч.\n"
                                               "<u>4. 20 км/ч</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_17')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('18 воп.', callback_data='q_1_18')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 17 Билет 1.\n"
                                               "Для перевозки людей на мотоцикле водитель должен иметь водительское удостоверение на право управления транспортными средствами:\n\n"
                                               "1. Категории «A» или подкатегории «A1».\n"
                                               "2. Любой категории или подкатегории в течение 2 и более лет.\n"
                                               "<u>3. Только категории «A» или подкатегории «A1» в течение 2 и более лет.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_18')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('19 воп.', callback_data='q_1_19')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 18 Билет 1.\n"
                                               "При какой неисправности разрешается эксплуатация транспортного средства?\n\n"
                                               "1. Не работают запорные устройства топливных баков.\n"
                                               "2. Не работают механизм регулировки и фиксирующее устройство сиденья водителя.\n"
                                               "3. Не работает устройство обдува ветрового стекла.\n"
                                               "<u>4. Не работает стеклоподъемник.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_19')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('20 воп.', callback_data='q_1_20')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 19 Билет 1.\n"
                                               "В случае, когда правые колеса автомобиля наезжают на неукрепленную влажную обочину, рекомендуется:\n\n"
                                               "1. Затормозить и полностью остановиться.\n"
                                               "2. Затормозить и плавно направить автомобиль на проезжую часть.\n"
                                               "<u>3. Не прибегая к торможению, плавно направить автомобиль на проезжую часть.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_20')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(callback.message.chat.id, "Вопрос 20 Билет 1.\n"
                                               "Что понимается под временем реакции водителя?\n\n"
                                               "1. Время с момента обнаружения водителем опасности до полной остановки транспортного средства.\n"
                                               "<u>2. Время с момента обнаружения водителем опасности до начала принятия мер по ее избежанию.</u>\n"
                                               "3. Время, необходимое для переноса ноги с педали управления подачей топлива на педаль тормоза.\n", reply_markup=markup)












@bot.callback_query_handler(func=lambda callback: callback.data == 'n2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_2_2')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 2.\n"
                                               "Сколько полос для движения имеет данная дорога?\n\n"
                                               "1. Две.\n"
                                               "2. Четыре.\n"
                                               "3. Пять.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_2_2')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 2.\n"
                                               "Можно ли Вам въехать на мост первым?\n\n"
                                               "1. Можно.\n"
                                               "2. Можно, если Вы не затрудните движение встречному автомобилю.\n"
                                               "3. Нельзя.\n", reply_markup=markup)




bot.polling(non_stop=True)

